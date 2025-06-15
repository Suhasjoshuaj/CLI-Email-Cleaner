import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def get_service(permanent=False, verbose=False):
    scope = 'https://mail.google.com/' if permanent else 'https://www.googleapis.com/auth/gmail.modify'
    SCOPES = [scope]

    # Temporary file before we identify the email
    temp_token_file = 'token_temp.json'
    creds = None

    # Try loading temp credentials if they exist
    if os.path.exists(temp_token_file):
        creds = Credentials.from_authorized_user_file(temp_token_file, SCOPES)

    # If no valid creds, authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if verbose:
                print(f"[INFO] Launching browser to authenticate...")
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open(temp_token_file, 'w') as token:
            token.write(creds.to_json())

    # Build service and fetch authenticated email
    service = build('gmail', 'v1', credentials=creds)
    profile = service.users().getProfile(userId='me').execute()
    email = profile['emailAddress']
    final_token_file = f'token_{email}.json'

    # Rename temp token to final token if not already there
    if not os.path.exists(final_token_file):
        os.rename(temp_token_file, final_token_file)
    else:
        os.remove(temp_token_file)  # token already exists, remove temp

    # Validate scope
    if permanent and 'https://mail.google.com/' not in creds.scopes:
        print("[ERROR] Your credentials do not have permission to permanently delete emails.")
        print("Delete the token file and re-authenticate using --permanent.")
        exit(1)

    if verbose:
        print(f"[INFO] Authenticated as: {email}")
        print(f"[DEBUG] Using scopes: {SCOPES}")

    return service, email
