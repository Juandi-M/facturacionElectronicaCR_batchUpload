# facturacionElectronicaCR_batchUpload

## Overview

This project involves automating the process of extracting data from XML attachments in Outlook emails and pushing the extracted data to the Ministerio de Hacienda de Costa Rica API. It leverages the Microsoft Graph API for email interactions and implements OAuth 2.0 for authentication.

### High-Level Workflow

1. **Authenticate to Graph API**: Use OAuth 2.0 to authenticate with the Microsoft Graph API and obtain an access token.
2. **Download XMLs from Mail Attachments in Outlook**: Access and download XML attachments from Outlook emails, filtering based on specific criteria.
3. **Extract Required Data from XMLs**: Parse the XML files to extract necessary fields using an XML parsing library.
4. **Push Data to Ministerio de Hacienda API**: Construct a JSON payload with the extracted data and send it to the Ministerio de Hacienda's API endpoint.

### Pseudo Code

```python
import requests
import xml.etree.ElementTree as ET
import base64
import json
import utils  # assuming utils contains necessary functions

def main():
    # Authenticate to Graph API
    token = utils.get_graph_access_token(...)

    # Download XMLs from Mail Attachments
    emails = utils.get_emails_from_senders(token, ...)
    for email in emails:
        xml_content = utils.download_attachment_from_email(token, email, ...)

        # Extract Data from XMLs
        extracted_data = extract_data_from_xml(xml_content)

        # Push Data to Ministerio de Hacienda API
        push_data_to_ministerio_de_hacienda_api(extracted_data)

def extract_data_from_xml(xml_content):
    # Parse and extract data
    tree = ET.ElementTree(ET.fromstring(xml_content))
    return extracted_data

def push_data_to_ministerio_de_hacienda_api(data):
    json_payload = construct_json_payload(data)
    url = "https://api_endpoint_here"
    response = requests.post(url, json=json_payload, headers={"Authorization": "Bearer ...", "Content-Type": "application/json"})

def construct_json_payload(data):
    return json_payload

if __name__ == "__main__":
    main()
```

### Project File Structure

- `main.py`: Main entry point of the application.
- `config.py`: Contains configuration settings and constants.
- `graph_api_handler.py`: Handles Microsoft Graph API interactions.
- `xml_parser.py`: Parses XML files and extracts data.
- `hacienda_api_handler.py`: Manages communication with the Ministerio de Hacienda API.
- `utils.py`: Provides utility functions for the project.
- `requirements.txt`: Lists all Python package dependencies.

### Azure Graph API Setup

1. **Create an Azure Account**: Sign up for a free Azure account.
2. **Register an Application in Azure AD**: Navigate to Azure Portal, access Azure Active Directory, and register a new application.
3. **Generate Client Secret**: Under app registration, create a new client secret.
4. **Configure Permissions for Microsoft Graph**: Add necessary permissions like `Mail.Read`.
5. **Grant Admin Consent**: If required, grant admin consent for permissions.
6. **Obtain Tenant ID**: Find your Azure AD tenant ID in the Azure Active Directory section.
7. **Implement OAuth 2.0**: Use Azure app registration details to implement OAuth 2.0 in your Python application.
8. **Test Your Application**: Ensure authentication and API calls work correctly.

### Security and Compliance

- **Security**: Keep your client secret secure and out of source control.
- **Documentation**: Refer to Microsoft’s documentation for specific details and updates.
- **Compliance**: Ensure your app complies with Microsoft's terms and relevant data protection regulations.

### Dependencies

Install the project dependencies by running:

```bash
pip install -r requirements.txt
```

### Running the Application

To run the application, execute:

```bash
python main.py
```

Ensure that all configuration settings in `config.py` are correctly set before running the application.