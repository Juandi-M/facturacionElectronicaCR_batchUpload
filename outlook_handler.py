# outlook_handler.py

import os
import requests
import utils
import config

def get_emails_from_senders(token, senders):
    url = "https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messages"
    emails = utils.make_graph_api_request(url, token)
    
    # Filter emails by sender and process further
    filtered_emails = [email for email in emails['value'] if any(sender in email['from']['emailAddress']['address'] for sender in senders)]
    return filtered_emails

def download_attachment_from_email(token, email, save_path):
    # Check for attachments in the email
    if email.get('hasAttachments'):
        message_id = email['id']
        url = f"https://graph.microsoft.com/v1.0/me/messages/{message_id}/attachments"
        attachments = utils.make_graph_api_request(url, token)

        for attachment in attachments['value']:
            if attachment['contentType'] == 'application/xml':
                attachment_content = attachment['contentBytes']
                file_name = attachment['name']
                save_attachment(attachment_content, file_name, save_path, email['receivedDateTime'])

def save_attachment(content, file_name, save_path, received_time):
    try:
        date_folder = utils.parse_received_time(received_time)
        full_path = os.path.join(save_path, date_folder)
        os.makedirs(full_path, exist_ok=True)
        file_path = os.path.join(full_path, file_name)

        # Decode the base64 content and write to a file
        with open(file_path, "wb") as file:
            file.write(base64.b64decode(content))
    except Exception as e:
        utils.log_exception(e)

# Additional utility function in utils.py for parsing the received time
def parse_received_time(received_time):
    """Parse the received time from ISO 8601 format to YYYY-MM-DD."""
    # You can use dateutil.parser here for parsing ISO 8601 formatted string
    # Example: dateutil.parser.isoparse(received_time).strftime("%Y-%m-%d")
    pass
