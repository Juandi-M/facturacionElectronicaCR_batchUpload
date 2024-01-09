# High Level Plan:

1. Authenticate to Graph API
Use OAuth 2.0 to authenticate with the Microsoft Graph API.
Obtain an access token to make authenticated requests.
2. Download XMLs from Mail Attachments in Outlook
Use the Graph API to access and download attachments from Outlook emails.
Filter emails based on specific criteria (like sender or subject) to find the relevant ones containing XML attachments.
3. Extract Required Data from XMLs
Parse the downloaded XML files to extract the necessary fields.
This step will depend on the structure of your XML files. You'll likely use an XML parsing library like xml.etree.ElementTree in Python.
4. Push the JSON with Extracted Data to Ministerio de Hacienda de Costa Rica API
Construct a JSON payload using the extracted data.
Use the HTTP POST method to send this JSON payload to the Ministerio de Hacienda's API endpoint.
Handle the authentication (if any) required by the Ministerio de Hacienda API.
Manage the responses and possible errors from the API.

## Psuedo Code

import requests
import xml.etree.ElementTree as ET
import base64
import json
import utils  # assuming utils contains necessary functions

def main():
    # Step 1: Authenticate to Graph API
    token = utils.get_graph_access_token( ... )  # OAuth details

    # Step 2: Download XMLs from Mail Attachments
    emails = utils.get_emails_from_senders(token, ...)
    for email in emails:
        xml_content = utils.download_attachment_from_email(token, email, ...)

        # Step 3: Extract Required Data from XMLs
        extracted_data = extract_data_from_xml(xml_content)

        # Step 4: Push JSON to Ministerio de Hacienda API
        push_data_to_ministerio_de_hacienda_api(extracted_data)

def extract_data_from_xml(xml_content):
    # Parse the XML content and extract the needed data
    tree = ET.ElementTree(ET.fromstring(xml_content))
    # Extraction logic here
    return extracted_data

def push_data_to_ministerio_de_hacienda_api(data):
    # Construct JSON payload
    json_payload = construct_json_payload(data)

    # Send data to the Ministerio de Hacienda API
    url = "https://api_endpoint_here"
    response = requests.post(url, json=json_payload, headers={"Authorization": "Bearer ...", "Content-Type": "application/json"})
    # Handle response

def construct_json_payload(data):
    # Logic to construct JSON payload from extracted data
    return json_payload

if __name__ == "__main__":
    main()


## Proposed file structure:

Project File Structure
main.py

The main entry point of your application.
Orchestrates the workflow by calling functions from other modules.
config.py

Contains configuration settings such as API credentials, email filter criteria, and file paths.
Stores constants used across the project.
graph_api_handler.py

Handles interactions with the Microsoft Graph API.
Includes functions for authenticating and downloading email attachments.
xml_parser.py

Responsible for parsing XML files and extracting necessary data.
Contains the logic to navigate and interpret the XML structure of your invoices.
hacienda_api_handler.py

Manages communication with the Ministerio de Hacienda API.
Includes functions to construct JSON payloads from extracted data and push them to the API.
utils.py

Provides utility functions used throughout the project.
Could include general-purpose functions for logging, error handling, and other common tasks.
requirements.txt

Lists all Python package dependencies for your project.
Ensures consistent environments across different setups.

## Azure Graph API:

1. Create an Azure Account
If you don't already have one, you'll need to create an Azure account. You can sign up for a free account which includes some free services.

2. Register an Application in Azure Active Directory (Azure AD)
Navigate to Azure Portal: Once logged in, go to the Azure Portal.
Access Azure Active Directory: Find and select Azure Active Directory from the portal menu.
Register a New Application:
Go to "App registrations" and select "New registration".
Enter a name for your application.
Choose supported account types (depending on who will be using your application).
Set a redirect URI (Web) if necessary. For desktop or daemon apps, this might not be needed.
After registration, note down the Application (client) ID. You will need this in your application.
3. Generate Client Secret (for Non-Public Apps)
Under the same app registration, navigate to "Certificates & secrets".
Click on "New client secret", provide a description, and set an expiry period.
Save the client secret value safely, as it won't be displayed again.
4. Configure Permissions for Microsoft Graph
In the app registration, go to "API permissions".
Click on "Add a permission" and choose Microsoft Graph.
Select the type of permissions your application needs (Delegated or Application permissions).
Add permissions like Mail.Read, Mail.ReadWrite, etc., depending on your application’s requirements.
5. Grant Admin Consent (if Required)
For certain permissions, especially those involving access to user data, you may need to grant admin consent.
This can be done in the "API permissions" section of your app registration.
6. Obtain Tenant ID
Your Azure AD tenant ID can be found in the Azure Active Directory section.
This ID is needed for the OAuth authentication process.
7. Implement OAuth 2.0 in Your Application
In your Python application, use the Azure app registration details (client ID, client secret, tenant ID) to implement OAuth 2.0 authentication.
Obtain access tokens to authenticate your API requests to Microsoft Graph.
8. Test Your Application
Ensure your application can authenticate and successfully make calls to the Microsoft Graph API.
Handle token refreshes as needed.
Final Notes
Security: Keep your client secret secure. Do not expose it in your code or check it into source control.
Documentation: Reference Microsoft’s documentation for specific details and any updates in the process.
Compliance: Ensure your app complies with Microsoft's terms and any relevant data protection regulations.
