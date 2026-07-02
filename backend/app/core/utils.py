import hashlib
from datetime import datetime
import re

def compute_email_hash(message_id: str, internal_date: str) -> str:
    """Generate a stable, unique hash for deduplicating emails"""
    data = f"{message_id}:{internal_date}"
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def clean_html(raw_html: str) -> str:
    """Basic HTML cleaner if needed, though frontend should handle safe rendering"""
    # Just a placeholder for any needed server-side cleaning
    if not raw_html:
        return ""
    # Strip some obvious malicious tags if necessary, but returning as-is for MVP
    return raw_html

def extract_domain(email_addr: str) -> str:
    """Extract domain from an email address string like 'Name <name@domain.com>'"""
    match = re.search(r'@([\w.-]+)', email_addr)
    if match:
        return match.group(1).lower()
    return ""
