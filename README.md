# Email Sweep (ES)

Uses Trend Micro [Cloud App Security (CAS)](https://www.trendmicro.com/en_au/business/products/user-protection/sps/email-and-collaboration/cloud-app-security.html) to scan and delete/quarantine harmful emails.

## Setup
### API Key

Create a CAS API key with the following permissions:

* Threat Investigation
* Threat Mitigation for Email Message

### Installation
### Linux

Set the CAS API as an environment variable:

```
export CAS_KEY=<API_KEY>
export CAS_URL=<SERVICE_URL>
```

### Windows

Set the CAS API as an environment variable:

```
set CAS_KEY=<API_KEY>
set CAS_URL=<SERVICE_URL>
```

**Note**: If you do not have Python on your machine, you can use `EmailSweep.exe` instead of `EmailSweep.py`.

## Usage 

Run the script using one or more of the filters. For more information on the filters, see [this page](http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/supported-cloud-app-/threat-investigation/sweep-for-email-mess.aspx).

**Note:** See [this page](http://docs.trendmicro.com/en-us/enterprise/cloud-app-security-integration-api-online-help/getting-started-with/understanding-the-ur.aspx) for Service URL options (Default: `api.tmcas.trendmicro.com`)

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

* `action_type` is set to `MAIL_QUARANTINE`
* `log_level` is set to `INFO`
* If `limit` is not set to a number under 500, all matching emails will be discovered


## Examples

```
EmailSweep.py --subject "Demo email" --lastndays 1
INFO - Using CAS URL: https://api.tmcas.trendmicro.com
INFO - Obtaining CAS API key
INFO - Running sweep call...
INFO - Calling GET https://api.tmcas.trendmicro.com/v1/sweeping/mails
Using parameters: {'lastndays': 1, 'subject': 'Demo email', 'limit': 500}
INFO - Sweep completed: 
[{
	"mail_message_sender": "hes-test@hes-demo.net",
	"mail_message_recipient": ["HES-Test@hes-demo.net"],
	"mail_message_subject": "Trend Micro Hosted Email Security quarantined spam 12/20/2019 08:00:00 for hes-test@hes-demo.net",
	"mailbox": "hes-test@hes-demo.net",
	"mail_urls": ["https://euq.hes.trendmicro.com/uiserver/deliverqtforenduserex?recipient=6865732d74657374406865732d64656d6f2e6e6574&request=52656c2c2c6147567a4c58526c633352416147567a4c57526c62573875626d56302c482d3233333838372c313537363731353135342c313537393330373135342c34623662613663322d366436382d346534622d393830372d6661386233306364366234332c7174353a323032303031313930303a3339393337343b7174363a323032303031313930303a3431323639362c627a4d324e574e76626d356c59335276636e5a6862476c6b59585270623235415a57313164475673593238756232357461574e7962334e765a6e5175593239742c312c31", "https://euq.hes.trendmicro.com/uiserver/deliverqtforenduserex?recipient=6865732d74657374406865732d64656d6f2e6e6574&request=4170722c2c6147567a4c58526c633352416147567a4c57526c62573875626d56302c482d3233333838372c313537363731353135342c313537393330373135342c34623662613663322d366436382d346534622d393830372d6661386233306364366234332c7174353a323032303031313930303a3339393337343b7174363a323032303031313930303a3431323639362c627a4d324e574e76626d356c59335276636e5a6862476c6b59585270623235415a57313164475673593238756232357461574e7962334e765a6e5175593239742c312c31", "https://euq.hes.trendmicro.com"],
	"source_domain": "hes-demo.net",
	"source_ip": "54.219.191.19",
	"mail_message_delivery_time": "2019-12-19T21:12:37.000Z",
	"mail_message_id": "<20191219210830.1D3BE14537E8@ifout4.hes.trendmicro.com>",
	"mail_unique_id": "AAMkAGE5M2UzYzQ5LTA1MmQtNDg5Yy1hOWM3LTk5NjAyZGFiMTU5YQBGAAAAAACUddeMzsPITJVSYsrik-rqBwAwK0-FMtGHTqodixbgCgWYAAAAAAEMAAAwK0-FMtGHTqodixbgCgWYAAFpJDa8AAA=",
	"mail_attachments": [],
	"mail_internet_headers": [{
		"Value": "hes-test@hes-demo.net",
		"HeaderName": "From"
	}, {
		"Value": "emailsecurity@hes.trendmicro.com",
		"HeaderName": "Return-Path"
	}, {
		"Value": "spf=pass (sender IP is 54.219.191.19)\r\n smtp.mailfrom=hes.trendmicro.com; hes-demo.net; dkim=none (message not\r\n signed) header.d=none;hes-demo.net; dmarc=fail action=oreject\r\n header.from=hes-demo.net;compauth=none reason=451",
		"HeaderName": "Authentication-Results"
	}]
}, {
	"mail_message_sender": "will_robinson@trendmicro.com",
	"mail_message_recipient": ["edie.clarke@emutelco.com"],
	"mail_message_subject": "RE: Demo email",
	"mailbox": "edie.clarke@emutelco.com",
	"mail_urls": ["www.trendmicro.com.au", "https://www.trendmicro.com/privacy", "https://resources.trendmicro.com/rs/trendmicroincorporated/images/logo_signature_2015.jpg"],
	"source_domain": "trendmicro.com",
	"source_ip": "13.238.202.162",
	"mail_message_delivery_time": "2019-12-19T23:05:33.000Z",
	"mail_message_id": "<82b33fa3ec924fdf8630e2fd4edbbd59@trendmicro.com>",
	"mail_unique_id": "AAMkADMzYzdlMTg3LTI1NDYtNDdjNC1iYjc3LTY2ZGE4ZGIxODQwOQBGAAAAAAACA3vsD5FoS6QV_XeCB1xWBwA3csq5TsaPQIEv-gdsoICyAAAAAAEMAAA3csq5TsaPQIEv-gdsoICyAAAt8UoQAAA=",
	"mail_attachments": [],
	"mail_internet_headers": [{
		"Value": "\"will_robinson@trendmicro.com\" <will_robinson@trendmicro.com>",
		"HeaderName": "From"
	}, {
		"Value": "will_robinson@trendmicro.com",
		"HeaderName": "Return-Path"
	}, {
		"Value": "spf=fail (sender IP is 13.238.202.162)\r\n smtp.mailfrom=trendmicro.com; emutelco.com; dkim=pass (signature was\r\n verified) header.d=trendmicro.com;emutelco.com; dmarc=pass action=none\r\n header.from=trendmicro.com;compauth=pass reason=100",
		"HeaderName": "Authentication-Results"
	}]
}, {
	"mail_message_sender": "will_robinson@trendmicro.com",
	"mail_message_recipient": ["edie.clarke@emutelco.com"],
	"mail_message_subject": "RE: Demo email",
	"mailbox": "edie.clarke@emutelco.com",
	"mail_urls": ["www.trendmicro.com.au", "https://www.trendmicro.com/privacy", "https://resources.trendmicro.com/rs/trendmicroincorporated/images/logo_signature_2015.jpg"],
	"source_domain": "trendmicro.com",
	"source_ip": "13.238.202.160",
	"mail_message_delivery_time": "2019-12-19T23:05:44.000Z",
	"mail_message_id": "<7643da46df4e4f39bbe9416afc2370e0@trendmicro.com>",
	"mail_unique_id": "AAMkADMzYzdlMTg3LTI1NDYtNDdjNC1iYjc3LTY2ZGE4ZGIxODQwOQBGAAAAAAACA3vsD5FoS6QV_XeCB1xWBwA3csq5TsaPQIEv-gdsoICyAAAAAAEMAAA3csq5TsaPQIEv-gdsoICyAAAt8UoRAAA=",
	"mail_attachments": [],
	"mail_internet_headers": [{
		"Value": "\"will_robinson@trendmicro.com\" <will_robinson@trendmicro.com>",
		"HeaderName": "From"
	}, {
		"Value": "<82b33fa3ec924fdf8630e2fd4edbbd59@trendmicro.com>",
		"HeaderName": "In-Reply-To"
	}, {
		"Value": "will_robinson@trendmicro.com",
		"HeaderName": "Return-Path"
	}, {
		"Value": "spf=fail (sender IP is 13.238.202.160)\r\n smtp.mailfrom=trendmicro.com; emutelco.com; dkim=pass (signature was\r\n verified) header.d=trendmicro.com;emutelco.com; dmarc=pass action=none\r\n header.from=trendmicro.com;compauth=pass reason=100",
		"HeaderName": "Authentication-Results"
	}]
}, {
	"mail_message_sender": "will_robinson@trendmicro.com",
	"mail_message_recipient": ["edie.clarke@emutelco.com"],
	"mail_message_subject": "RE: Demo email",
	"mailbox": "edie.clarke@emutelco.com",
	"mail_urls": ["www.trendmicro.com.au", "https://www.trendmicro.com/privacy", "https://resources.trendmicro.com/rs/trendmicroincorporated/images/logo_signature_2015.jpg"],
	"source_domain": "trendmicro.com",
	"source_ip": "13.238.202.160",
	"mail_message_delivery_time": "2019-12-19T23:05:46.000Z",
	"mail_message_id": "<f1e0a8a256cc48038839f4994842db7b@trendmicro.com>",
	"mail_unique_id": "AAMkADMzYzdlMTg3LTI1NDYtNDdjNC1iYjc3LTY2ZGE4ZGIxODQwOQBGAAAAAAACA3vsD5FoS6QV_XeCB1xWBwA3csq5TsaPQIEv-gdsoICyAAAAAAEMAAA3csq5TsaPQIEv-gdsoICyAAAt8UoSAAA=",
	"mail_attachments": [],
	"mail_internet_headers": [{
		"Value": "\"will_robinson@trendmicro.com\" <will_robinson@trendmicro.com>",
		"HeaderName": "From"
	}, {
		"Value": "<82b33fa3ec924fdf8630e2fd4edbbd59@trendmicro.com>",
		"HeaderName": "In-Reply-To"
	}, {
		"Value": "will_robinson@trendmicro.com",
		"HeaderName": "Return-Path"
	}, {
		"Value": "spf=fail (sender IP is 13.238.202.160)\r\n smtp.mailfrom=trendmicro.com; emutelco.com; dkim=pass (signature was\r\n verified) header.d=trendmicro.com;emutelco.com; dmarc=pass action=none\r\n header.from=trendmicro.com;compauth=pass reason=100",
		"HeaderName": "Authentication-Results"
	}]
}, {
	"mail_message_sender": "will_robinson@trendmicro.com",
	"mail_message_recipient": ["edie.clarke@emutelco.com"],
	"mail_message_subject": "RE: Demo email",
	"mailbox": "edie.clarke@emutelco.com",
	"mail_urls": ["www.trendmicro.com.au", "https://www.trendmicro.com/privacy", "https://resources.trendmicro.com/rs/trendmicroincorporated/images/logo_signature_2015.jpg"],
	"source_domain": "trendmicro.com",
	"source_ip": "13.238.202.162",
	"mail_message_delivery_time": "2019-12-19T23:43:44.000Z",
	"mail_message_id": "<d7e8d82585e64caca7ae65917426ec31@trendmicro.com>",
	"mail_unique_id": "AAMkADMzYzdlMTg3LTI1NDYtNDdjNC1iYjc3LTY2ZGE4ZGIxODQwOQBGAAAAAAACA3vsD5FoS6QV_XeCB1xWBwA3csq5TsaPQIEv-gdsoICyAAAAAAEMAAA3csq5TsaPQIEv-gdsoICyAAAt8UoTAAA=",
	"mail_attachments": [],
	"mail_internet_headers": [{
		"Value": "\"will_robinson@trendmicro.com\" <will_robinson@trendmicro.com>",
		"HeaderName": "From"
	}, {
		"Value": "<f1e0a8a256cc48038839f4994842db7b@trendmicro.com>",
		"HeaderName": "In-Reply-To"
	}, {
		"Value": "will_robinson@trendmicro.com",
		"HeaderName": "Return-Path"
	}, {
		"Value": "spf=fail (sender IP is 13.238.202.162)\r\n smtp.mailfrom=trendmicro.com; emutelco.com; dkim=pass (signature was\r\n verified) header.d=trendmicro.com;emutelco.com; dmarc=pass action=none\r\n header.from=trendmicro.com;compauth=pass reason=100",
		"HeaderName": "Authentication-Results"
	}]
}, {
	"mail_message_sender": "will_robinson@trendmicro.com",
	"mail_message_recipient": ["edie.clarke@emutelco.com"],
	"mail_message_subject": "RE: Demo email",
	"mailbox": "edie.clarke@emutelco.com",
	"mail_urls": ["www.trendmicro.com.au", "https://www.trendmicro.com/privacy", "https://resources.trendmicro.com/rs/trendmicroincorporated/images/logo_signature_2015.jpg"],
	"source_domain": "trendmicro.com",
	"source_ip": "13.238.202.160",
	"mail_message_delivery_time": "2019-12-19T23:43:49.000Z",
	"mail_message_id": "<623fe923727540da8f9cb72c2155cf4b@trendmicro.com>",
	"mail_unique_id": "AAMkADMzYzdlMTg3LTI1NDYtNDdjNC1iYjc3LTY2ZGE4ZGIxODQwOQBGAAAAAAACA3vsD5FoS6QV_XeCB1xWBwA3csq5TsaPQIEv-gdsoICyAAAAAAEMAAA3csq5TsaPQIEv-gdsoICyAAAt8UoUAAA=",
	"mail_attachments": [],
	"mail_internet_headers": [{
		"Value": "\"will_robinson@trendmicro.com\" <will_robinson@trendmicro.com>",
		"HeaderName": "From"
	}, {
		"Value": "<f1e0a8a256cc48038839f4994842db7b@trendmicro.com>",
		"HeaderName": "In-Reply-To"
	}, {
		"Value": "will_robinson@trendmicro.com",
		"HeaderName": "Return-Path"
	}, {
		"Value": "spf=fail (sender IP is 13.238.202.160)\r\n smtp.mailfrom=trendmicro.com; emutelco.com; dkim=pass (signature was\r\n verified) header.d=trendmicro.com;emutelco.com; dmarc=pass action=none\r\n header.from=trendmicro.com;compauth=pass reason=100",
		"HeaderName": "Authentication-Results"
	}]
}]
INFO - Found 6 entries
INFO - Preparing entries for mitigation...
Would you like to proceed? (YES/NO): yes
```

Note that the script pauses for user input at this point. If `no` is entered, the script will exit without making any changes. To proceed, enter `yes`.

```
INFO - Executing mitigation call
INFO - Calling POST https://api.tmcas.trendmicro.com/v1/mitigation/mails
Using parameters: [{'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'mailbox': 'hes-test@hes-demo.net', 'mail_message_id': '<20191219210830.1D3BE14537E8@ifout4.hes.trendmicro.com>', 'mail_message_delivery_time': '2019-12-19T21:12:37.000Z'}, {'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<82b33fa3ec924fdf8630e2fd4edbbd59@trendmicro.com>', 'mail_message_delivery_time': '2019-12-19T23:05:33.000Z'}, {'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<7643da46df4e4f39bbe9416afc2370e0@trendmicro.com>', 'mail_message_delivery_time': '2019-12-19T23:05:44.000Z'}, {'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<f1e0a8a256cc48038839f4994842db7b@trendmicro.com>', 'mail_message_delivery_time': '2019-12-19T23:05:46.000Z'}, {'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<d7e8d82585e64caca7ae65917426ec31@trendmicro.com>', 'mail_message_delivery_time': '2019-12-19T23:43:44.000Z'}, {'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<623fe923727540da8f9cb72c2155cf4b@trendmicro.com>', 'mail_message_delivery_time': '2019-12-19T23:43:49.000Z'}]
INFO - Call completed successfully
INFO - Mitigation results:
{'code': 0, 'msg': '', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'traceId': '5e20dc78-e42e-4424-9cda-3ed3f9653a21'}
INFO - Extracted mitigation batch ID: 15ea27a4-8ffc-48d4-a90f-ebb977c06f30
INFO - Querying mitigation status
INFO - Calling GET https://api.tmcas.trendmicro.com/v1/mitigation/mails
Using parameters: {'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'limit': 500}
INFO - Call completed successfully
INFO - Mitigation query entries:
{'code': 0, 'msg': '', 'count': 6, 'current_link': 'https://api.tmcas.trendmicro.com/v1/mitigation/mails?batch_id=15ea27a4-8ffc-48d4-a90f-ebb977c06f30&limit=500', 'next_link': None, 'actions': [{'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'hes-test@hes-demo.net', 'mailbox': 'hes-test@hes-demo.net', 'mail_message_id': '<20191219210830.1D3BE14537E8@ifout4.hes.trendmicro.com>', 'action_id': 'ce4203bb-17da-463f-a67d-a8e76c373970', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Failed', 'action_requested_at': '2019-12-19T23:44:31.436Z', 'action_executed_at': '2019-12-19T23:44:32.610Z', 'error_code': -999, 'error_message': 'The action for these mails failed.'}, {'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'edie.clarke@emutelco.com', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<82b33fa3ec924fdf8630e2fd4edbbd59@trendmicro.com>', 'action_id': 'b1159fee-ec77-40ac-bca1-73628f0dd889', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Skipped', 'action_requested_at': '2019-12-19T23:44:31.786Z', 'action_executed_at': '2019-12-19T23:44:32.380Z', 'error_code': 200, 'error_message': 'ResourceNotFound'}, {'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'edie.clarke@emutelco.com', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<7643da46df4e4f39bbe9416afc2370e0@trendmicro.com>', 'action_id': '7671ff45-bcaf-48d1-8083-55d124da81ce', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Skipped', 'action_requested_at': '2019-12-19T23:44:31.886Z', 'action_executed_at': '2019-12-19T23:44:32.156Z', 'error_code': 200, 'error_message': 'ResourceNotFound'}, {'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'edie.clarke@emutelco.com', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<f1e0a8a256cc48038839f4994842db7b@trendmicro.com>', 'action_id': 'd2de2fbf-4af6-434b-85a6-e15cfdbb8081', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Skipped', 'action_requested_at': '2019-12-19T23:44:31.993Z', 'action_executed_at': '2019-12-19T23:44:32.476Z', 'error_code': 200, 'error_message': 'ResourceNotFound'}, {'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'edie.clarke@emutelco.com', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<d7e8d82585e64caca7ae65917426ec31@trendmicro.com>', 'action_id': '0b8102f3-189c-4092-b399-3af2899eefd5', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Success', 'action_requested_at': '2019-12-19T23:44:32.143Z', 'action_executed_at': '2019-12-19T23:44:33.323Z', 'error_code': 0, 'error_message': ''}, {'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'edie.clarke@emutelco.com', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<623fe923727540da8f9cb72c2155cf4b@trendmicro.com>', 'action_id': '21f2b331-f3d3-4c10-bd17-0870749eecbc', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Success', 'action_requested_at': '2019-12-19T23:44:32.350Z', 'action_executed_at': '2019-12-19T23:44:34.003Z', 'error_code': 0, 'error_message': ''}], 'traceId': '6c733b7e-d48b-4b8c-bfc6-90a169b62008'}
INFO - Processing entry:
{'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'hes-test@hes-demo.net', 'mailbox': 'hes-test@hes-demo.net', 'mail_message_id': '<20191219210830.1D3BE14537E8@ifout4.hes.trendmicro.com>', 'action_id': 'ce4203bb-17da-463f-a67d-a8e76c373970', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Failed', 'action_requested_at': '2019-12-19T23:44:31.436Z', 'action_executed_at': '2019-12-19T23:44:32.610Z', 'error_code': -999, 'error_message': 'The action for these mails failed.'}
ERROR - The action for these mails failed.:
{'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'hes-test@hes-demo.net', 'mailbox': 'hes-test@hes-demo.net', 'mail_message_id': '<20191219210830.1D3BE14537E8@ifout4.hes.trendmicro.com>', 'action_id': 'ce4203bb-17da-463f-a67d-a8e76c373970', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Failed', 'action_requested_at': '2019-12-19T23:44:31.436Z', 'action_executed_at': '2019-12-19T23:44:32.610Z', 'error_code': -999, 'error_message': 'The action for these mails failed.'}
INFO - 1/6 entries processed
INFO - Processing entry:
{'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'edie.clarke@emutelco.com', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<82b33fa3ec924fdf8630e2fd4edbbd59@trendmicro.com>', 'action_id': 'b1159fee-ec77-40ac-bca1-73628f0dd889', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Skipped', 'action_requested_at': '2019-12-19T23:44:31.786Z', 'action_executed_at': '2019-12-19T23:44:32.380Z', 'error_code': 200, 'error_message': 'ResourceNotFound'}
WARNING - Resource not found. It is likely to have been deleted or quarantined previously
INFO - 2/6 entries processed
INFO - Processing entry:
{'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'edie.clarke@emutelco.com', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<7643da46df4e4f39bbe9416afc2370e0@trendmicro.com>', 'action_id': '7671ff45-bcaf-48d1-8083-55d124da81ce', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Skipped', 'action_requested_at': '2019-12-19T23:44:31.886Z', 'action_executed_at': '2019-12-19T23:44:32.156Z', 'error_code': 200, 'error_message': 'ResourceNotFound'}
WARNING - Resource not found. It is likely to have been deleted or quarantined previously
INFO - 3/6 entries processed
INFO - Processing entry:
{'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'edie.clarke@emutelco.com', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<f1e0a8a256cc48038839f4994842db7b@trendmicro.com>', 'action_id': 'd2de2fbf-4af6-434b-85a6-e15cfdbb8081', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Skipped', 'action_requested_at': '2019-12-19T23:44:31.993Z', 'action_executed_at': '2019-12-19T23:44:32.476Z', 'error_code': 200, 'error_message': 'ResourceNotFound'}
WARNING - Resource not found. It is likely to have been deleted or quarantined previously
INFO - 4/6 entries processed
INFO - Processing entry:
{'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'edie.clarke@emutelco.com', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<d7e8d82585e64caca7ae65917426ec31@trendmicro.com>', 'action_id': '0b8102f3-189c-4092-b399-3af2899eefd5', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Success', 'action_requested_at': '2019-12-19T23:44:32.143Z', 'action_executed_at': '2019-12-19T23:44:33.323Z', 'error_code': 0, 'error_message': ''}
INFO - Successfully processed entry
INFO - 5/6 entries processed
INFO - Processing entry:
{'action_type': 'MAIL_QUARANTINE', 'service': 'exchange', 'account_provider': 'office365', 'account_user_email': 'edie.clarke@emutelco.com', 'mailbox': 'edie.clarke@emutelco.com', 'mail_message_id': '<623fe923727540da8f9cb72c2155cf4b@trendmicro.com>', 'action_id': '21f2b331-f3d3-4c10-bd17-0870749eecbc', 'batch_id': '15ea27a4-8ffc-48d4-a90f-ebb977c06f30', 'status': 'Success', 'action_requested_at': '2019-12-19T23:44:32.350Z', 'action_executed_at': '2019-12-19T23:44:34.003Z', 'error_code': 0, 'error_message': ''}
INFO - Successfully processed entry
INFO - 6/6 entries processed
INFO - All entries have been processed
INFO - Detailed report:
{
	"Success": [{
		"action_type": "MAIL_QUARANTINE",
		"service": "exchange",
		"account_provider": "office365",
		"account_user_email": "edie.clarke@emutelco.com",
		"mailbox": "edie.clarke@emutelco.com",
		"mail_message_id": "<d7e8d82585e64caca7ae65917426ec31@trendmicro.com>",
		"action_id": "0b8102f3-189c-4092-b399-3af2899eefd5",
		"batch_id": "15ea27a4-8ffc-48d4-a90f-ebb977c06f30",
		"status": "Success",
		"action_requested_at": "2019-12-19T23:44:32.143Z",
		"action_executed_at": "2019-12-19T23:44:33.323Z",
		"error_code": 0,
		"error_message": ""
	}, {
		"action_type": "MAIL_QUARANTINE",
		"service": "exchange",
		"account_provider": "office365",
		"account_user_email": "edie.clarke@emutelco.com",
		"mailbox": "edie.clarke@emutelco.com",
		"mail_message_id": "<623fe923727540da8f9cb72c2155cf4b@trendmicro.com>",
		"action_id": "21f2b331-f3d3-4c10-bd17-0870749eecbc",
		"batch_id": "15ea27a4-8ffc-48d4-a90f-ebb977c06f30",
		"status": "Success",
		"action_requested_at": "2019-12-19T23:44:32.350Z",
		"action_executed_at": "2019-12-19T23:44:34.003Z",
		"error_code": 0,
		"error_message": ""
	}],
	"ResourceNotFound": [{
		"action_type": "MAIL_QUARANTINE",
		"service": "exchange",
		"account_provider": "office365",
		"account_user_email": "edie.clarke@emutelco.com",
		"mailbox": "edie.clarke@emutelco.com",
		"mail_message_id": "<82b33fa3ec924fdf8630e2fd4edbbd59@trendmicro.com>",
		"action_id": "b1159fee-ec77-40ac-bca1-73628f0dd889",
		"batch_id": "15ea27a4-8ffc-48d4-a90f-ebb977c06f30",
		"status": "Skipped",
		"action_requested_at": "2019-12-19T23:44:31.786Z",
		"action_executed_at": "2019-12-19T23:44:32.380Z",
		"error_code": 200,
		"error_message": "ResourceNotFound"
	}, {
		"action_type": "MAIL_QUARANTINE",
		"service": "exchange",
		"account_provider": "office365",
		"account_user_email": "edie.clarke@emutelco.com",
		"mailbox": "edie.clarke@emutelco.com",
		"mail_message_id": "<7643da46df4e4f39bbe9416afc2370e0@trendmicro.com>",
		"action_id": "7671ff45-bcaf-48d1-8083-55d124da81ce",
		"batch_id": "15ea27a4-8ffc-48d4-a90f-ebb977c06f30",
		"status": "Skipped",
		"action_requested_at": "2019-12-19T23:44:31.886Z",
		"action_executed_at": "2019-12-19T23:44:32.156Z",
		"error_code": 200,
		"error_message": "ResourceNotFound"
	}, {
		"action_type": "MAIL_QUARANTINE",
		"service": "exchange",
		"account_provider": "office365",
		"account_user_email": "edie.clarke@emutelco.com",
		"mailbox": "edie.clarke@emutelco.com",
		"mail_message_id": "<f1e0a8a256cc48038839f4994842db7b@trendmicro.com>",
		"action_id": "d2de2fbf-4af6-434b-85a6-e15cfdbb8081",
		"batch_id": "15ea27a4-8ffc-48d4-a90f-ebb977c06f30",
		"status": "Skipped",
		"action_requested_at": "2019-12-19T23:44:31.993Z",
		"action_executed_at": "2019-12-19T23:44:32.476Z",
		"error_code": 200,
		"error_message": "ResourceNotFound"
	}],
	"OtherErrors": [{
		"action_type": "MAIL_QUARANTINE",
		"service": "exchange",
		"account_provider": "office365",
		"account_user_email": "hes-test@hes-demo.net",
		"mailbox": "hes-test@hes-demo.net",
		"mail_message_id": "<20191219210830.1D3BE14537E8@ifout4.hes.trendmicro.com>",
		"action_id": "ce4203bb-17da-463f-a67d-a8e76c373970",
		"batch_id": "15ea27a4-8ffc-48d4-a90f-ebb977c06f30",
		"status": "Failed",
		"action_requested_at": "2019-12-19T23:44:31.436Z",
		"action_executed_at": "2019-12-19T23:44:32.610Z",
		"error_code": -999,
		"error_message": "The action for these mails failed."
	}]
}
INFO - Summary report:
Success: 2
ResourceNotFound: 3
OtherErrors: 1
```

## Reports

After the script runs, it will provide a status report for each of the entries it actioned. The statuses are as follows:
* `Success`: Action completed successfully
* `ResourceNotFound`: Resource is no longer there (most likely due to it being deleted or quarantined previously)  
* `OtherErrors`: Error occurred while performing the action (e.g the mailbox no longer exists)
