from time import sleep
import os
import argparse
import sys
import json
from onncas import Cas

APP_NAME = 'EmailSweep'
SUCCESS_STRING = 'Success'


class EmailSweep(Cas):
    def __init__(self, service='exchange', account_provider='office365', action_type='MAIL_QUARANTINE', **kwargs):
        super().__init__(**kwargs)

        self.service = service
        self.account_provider = account_provider
        self.action_type = action_type
        self.processed_msg_id = set()

        self.run_report = {
            'Success': [],
            'ResourceNotFound': [],
            'OtherErrors': [],

        }

    def get_entries(self, sweep_params, get_all=True):
        email_sweep = self.sweep_emails(params=sweep_params, get_all=get_all)
        email_entries = email_sweep['entries']
        num_entries = len(email_entries)
        json_output = json.dumps(email_entries)
        self.logger.entry('info', f'Sweep completed:\n{json_output}')
        self.logger.entry('info', f'Found {num_entries} entries')

        return email_entries

    def prepare_mitigation(self, email_entries):
        self.logger.entry('info', 'Preparing entries for mitigation...')
        mitigate_entries = []

        for result in email_entries:
            mailbox = result['mailbox']
            msg_id = result['mail_message_id']
            delivery_time = result['mail_message_delivery_time']

            mitigate_email_entry = {
                'action_type': self.action_type,
                'service': self.service,
                'account_provider': self.account_provider,
                'mailbox': mailbox,
                'mail_message_id': msg_id,
                'mail_message_delivery_time': delivery_time,
            }

            mitigate_entries.append(mitigate_email_entry)
            self.logger.entry('debug', f'Added entry: {mitigate_email_entry}')

        return mitigate_entries

    def generate_reports(self):
        json_output = json.dumps(self.run_report)
        self.logger.entry('info', f'All entries have been processed')
        self.logger.entry('info', f'Detailed report:\n'
                                  f'{json_output}')

        summary_report = []
        for report_status, value in self.run_report.items():
            entry_count = f'{report_status}: {len(value)}'
            summary_report.append(entry_count)

        joined_summary = '\n'.join(summary_report)
        self.logger.entry('info', f'Summary report:\n{joined_summary}')

    @staticmethod
    def proceed_prompt():
        while True:
            user_response = input('Would you like to proceed? (YES/NO): ')

            if user_response.upper() == 'YES':
                return True

            elif user_response.upper() == 'NO':
                return False

    def run(self, email_entries):
        mitigate_entries = self.prepare_mitigation(email_entries)
        proceed = self.proceed_prompt()

        if not proceed:
            sys.exit()

        self.logger.entry('info', 'Executing mitigation call')
        run_mitigation = self.set_email_mitigation(mitigate_entries)
        api_response = run_mitigation['api']
        self.logger.entry('info', f'Mitigation results:\n{api_response}')

        batch_id = api_response['batch_id']
        self.logger.entry('info', f'Extracted mitigation batch ID: {batch_id}')

        batch_id_param = {'batch_id': batch_id}

        while True:
            self.logger.entry('info', 'Querying mitigation status')
            mitigate_query_response = self.get_email_mitigation(params=batch_id_param)
            response_entries = mitigate_query_response['api']
            self.logger.entry('info', f'Mitigation query entries:\n{response_entries}')

            action_entries = response_entries['actions']
            done_processing = self._check_status(action_entries)

            if done_processing:
                break

            sleep_time = 10
            self.logger.entry('info', f'Some entries are still processing. Sleeping {sleep_time} seconds before trying'
                                      f' again')
            sleep(sleep_time)

        self.generate_reports()

    def _check_status(self, action_entries):
        num_entries = len(action_entries)
        done_count = 0

        for entry in action_entries:
            msg_id = entry['mail_message_id']

            if msg_id in self.processed_msg_id:
                done_count += 1
                continue

            error_message = entry['error_message']
            error_code = entry['error_code']
            status = entry['status']
            self.logger.entry('info', f'Processing entry:\n{entry}')

            if status == SUCCESS_STRING:
                done_count += 1
                self.logger.entry('info', 'Successfully processed entry')
                self.logger.entry('info', f'{done_count}/{num_entries} entries processed')
                self.processed_msg_id.add(msg_id)
                self.run_report['Success'].append(entry)
                continue

            elif error_code == 0 and SUCCESS_STRING not in status:
                self.logger.entry('info', 'Entry is still being processed')
                self.logger.entry('info', f'{done_count}/{num_entries} entries processed')
                return False

            elif error_code != 0:
                done_count += 1
                if error_message == 'ResourceNotFound':
                    self.logger.entry('warning', 'Resource not found. It is likely to have been deleted or quarantined '
                                                 'previously')
                    self.logger.entry('info', f'{done_count}/{num_entries} entries processed')
                    self.processed_msg_id.add(msg_id)
                    self.run_report['ResourceNotFound'].append(entry)
                    continue

                else:
                    self.logger.entry('error', f'{error_message}:\n{entry}')
                    self.logger.entry('info', f'{done_count}/{num_entries} entries processed')
                    self.processed_msg_id.add(msg_id)
                    self.run_report['OtherErrors'].append(entry)
                    continue

        if done_count == num_entries:
            return True


def get_args():
    parser = argparse.ArgumentParser(description='Email Sweep')

    parser.add_argument('--mailbox', action='store', help='Email address of the mailbox to search in')
    parser.add_argument('--lastndays', action='store', type=int, help='Number of days before the point of time when the '
                                                                      'request is sent')
    parser.add_argument('--start', action='store', help='Start time during which email message are to search')
    parser.add_argument('--end', action='store', help='End time during which email message are to search')
    parser.add_argument('--subject', action='store', help='Subject of email messages to search for')
    parser.add_argument('--file_sha1', action='store', help='SHA-1 hash value of the attachment file to search for')
    parser.add_argument('--file_name', action='store', help='Name of the attachment file to search for')
    parser.add_argument('--file_extension', action='store', help='Filename extension of attachment files to search for')
    parser.add_argument('--url', action='store', help='URL in email body or attachments to search for')
    parser.add_argument('--sender', action='store', help='Sender email address of email messages to search for')
    parser.add_argument('--recipient', action='store', help='Recipient email address of email messages to search for')
    parser.add_argument('--message_id', action='store', help='Internet message ID of the email message to search for')
    parser.add_argument('--source_ip', action='store', help='Source IP address of email messages to search for')
    parser.add_argument('--source_domain', action='store', help='Source domain of email messages to search for')
    parser.add_argument('--log_level', action='store', default='INFO', help='Log level (DEBUG, INFO, WARNINING)')
    parser.add_argument('--limit', action='store', type=int, default=500, help='Limit the number of entries')

    all_args = vars(parser.parse_args())
    args = {key: value for key, value in all_args.items() if value is not None}

    return args


def main():
    args = get_args()

    if len(args) <= 2:
        sys.exit('Error: You must supply at least 1 filter')

    log_level = args.pop('log_level').upper()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    log_file_path = f'{dir_path}{os.sep}log.txt'
    print(log_file_path)
    es = EmailSweep(app_name=APP_NAME, print_logger=True, log_level=log_level, log_file_path=log_file_path)

    email_entries = es.get_entries(args)
    es.run(email_entries)


if __name__ == '__main__':
    main()
