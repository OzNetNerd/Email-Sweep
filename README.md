# Email Sweep (ES)

Uses Trend Micro [Cloud App Security (CAS)](https://www.trendmicro.com/en_au/business/products/user-protection/sps/email-and-collaboration/cloud-app-security.html) to scan and delete/quarantine harmful emails.

## Usage

Set the CAS API as an environment variable:

```
export CAS_KEY=<API_KEY>
export CAS_URL=<SERVICE_URL>
```

See [this page](http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/getting-started-with/understanding-the-ur.aspx) for Service URL options (Default: `api.tmcas.trendmicro.com`) 

Run the script using one or more of the filters. For more information on the filters, see [this page](http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/supported-cloud-app-/threat-investigation/sweep-for-email-mess.aspx).

```
$ python3 EmailSweep.py -h
usage: runner.py [-h] [--mailbox MAILBOX] [--lastndays LASTNDAYS]
                 [--start START] [--end END] [--subject SUBJECT]
                 [--file_sha1 FILE_SHA1] [--file_name FILE_NAME]
                 [--file_extension FILE_EXTENSION] [--url URL]
                 [--sender SENDER] [--recipient RECIPIENT]
                 [--message_id MESSAGE_ID] [--source_ip SOURCE_IP]
                 [--source_domain SOURCE_DOMAIN] [--log_level LOG_LEVEL]
                 [--limit LIMIT]

Email Sweep

optional arguments:
  -h, --help            show this help message and exit
  --mailbox MAILBOX     Email address of the mailbox to search in
  --lastndays LASTNDAYS
                        Number of days before the point of time when the
                        request is sent
  --start START         Start time during which email message are to search
  --end END             End time during which email message are to search
  --subject SUBJECT     Subject of email messages to search for
  --file_sha1 FILE_SHA1
                        SHA-1 hash value of the attachment file to search for
  --file_name FILE_NAME
                        Name of the attachment file to search for
  --file_extension FILE_EXTENSION
                        Filename extension of attachment files to search for
  --url URL             URL in email body or attachments to search for
  --sender SENDER       Sender email address of email messages to search for
  --recipient RECIPIENT
                        Recipient email address of email messages to search
                        for
  --message_id MESSAGE_ID
                        Internet message ID of the email message to search for
  --source_ip SOURCE_IP
                        Source IP address of email messages to search for
  --source_domain SOURCE_DOMAIN
                        Source domain of email messages to search for
  --log_level LOG_LEVEL
                        Log level
  --limit LIMIT         Limit the number of entries
```

### Defaults

* `log_level` is set to `INFO` by default
* If `limit` is not set to a number under 500, all matching emails will be discovered
