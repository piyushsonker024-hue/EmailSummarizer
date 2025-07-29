from imaplib import IMAP4_SSL
from email import message_from_bytes
from email.header import decode_header
from collections import defaultdict
import email
from config import EMAIL, PASSWORD, IMAP_SERVER

def connect_email():
    mail = IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    return mail

def fetch_emails(mail, num_emails=20):
    mail.select("inbox")
    result, data = mail.search(None, 'ALL')
    email_ids = data[0].split()[-num_emails:]
    emails = []
    for e_id in email_ids:
        result, msg_data = mail.fetch(e_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = message_from_bytes(raw_email)
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8", errors="ignore")
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain" and "attachment" not in str(part.get("Content-Disposition", "")):
                    try:
                        body = part.get_payload(decode=True).decode()
                    except:
                        body = part.get_payload()
                    break
        else:
            try:
                body = msg.get_payload(decode=True).decode('utf-8')
            except UnicodeDecodeError:
                try:
                    body = msg.get_payload(decode=True).decode('latin1')
                except:
                    body = msg.get_payload(decode=True).decode(errors='replace')
        emails.append({
            "subject": subject,
            "body": body
        })
    return emails
