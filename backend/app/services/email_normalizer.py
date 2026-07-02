import base64
from datetime import datetime
from app.models.email import Email
from app.core.utils import compute_email_hash, extract_domain

def parse_headers(headers: list) -> dict:
    return {h['name'].lower(): h['value'] for h in headers}

def get_body_data(payload: dict) -> tuple:
    """Returns (text_body, html_body)"""
    text_body = ""
    html_body = ""

    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                data = part['body'].get('data')
                if data:
                    text_body += base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
            elif part['mimeType'] == 'text/html':
                data = part['body'].get('data')
                if data:
                    html_body += base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
            elif 'parts' in part:
                # recursively parse nested parts (like multipart/alternative)
                sub_text, sub_html = get_body_data(part)
                text_body += sub_text
                html_body += sub_html
    else:
        # Simple email with no parts
        data = payload['body'].get('data')
        if data:
            decoded = base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
            if payload.get('mimeType') == 'text/html':
                html_body = decoded
            else:
                text_body = decoded

    return text_body, html_body

def normalize_email(gmail_msg: dict, user_id: str) -> Email:
    """Converts a raw Gmail message dictionary into an SQLAlchemy Email object."""
    headers = parse_headers(gmail_msg['payload']['headers'])
    
    subject = headers.get('subject', '(No Subject)')
    sender = headers.get('from', '')
    
    sender_name = sender
    sender_email = sender
    if '<' in sender and '>' in sender:
        parts = sender.split('<')
        sender_name = parts[0].strip(' "')
        sender_email = parts[1].strip('>')

    text_body, html_body = get_body_data(gmail_msg['payload'])
    
    internal_date = gmail_msg.get('internalDate')
    received_at = datetime.fromtimestamp(int(internal_date) / 1000.0) if internal_date else None
    
    email_hash = compute_email_hash(gmail_msg['id'], internal_date or "0")

    return Email(
        user_id=user_id,
        gmail_message_id=gmail_msg['id'],
        thread_id=gmail_msg['threadId'],
        subject=subject,
        sender_name=sender_name,
        sender_email=sender_email,
        snippet=gmail_msg.get('snippet', ''),
        body_text=text_body,
        body_html=html_body,
        labels=gmail_msg.get('labelIds', []),
        internal_date=internal_date,
        received_at=received_at,
        hash=email_hash,
        status="FETCHED"
    )
