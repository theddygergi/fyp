import imaplib
import email
from email.header import decode_header
import re
 
def get_outlook_otp(username, password):
    # IMAP server settings for Outlook
    imap_host = "outlook.office365.com"
    imap_port = 993
 
    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(imap_host, imap_port)
    mail.login(username, password)
 
    # Select the inbox folder
    mail.select("inbox")
 
    # Search for all emails in the inbox in reverse order
    result, data = mail.search(None, "ALL")
    email_ids = data[0].split()
 
    # Fetch the last email
    latest_email_id = email_ids[-1]
 
    # Fetch the email data
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
 
    # Parse the raw email into a message object
    message = email.message_from_bytes(raw_email)
 
    # Decode the email body
    if message.is_multipart():
        for part in message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
 
            if content_type == "text/plain" and "attachment" not in content_disposition:
                body = part.get_payload(decode=True).decode()
    else:
        body = message.get_payload(decode=True).decode()
 
    print(body)
    # Close the connection
    mail.close()
    mail.logout()
 
    # Extract 6-digit numbers from the email body
    pattern = r'\b\d{6}\b'
    six_digit_numbers = re.findall(pattern, body)
 
    # Return the OTP code
    if len(six_digit_numbers) >= 5:  # Assuming OTP code is the 5th 6-digit number found
        return six_digit_numbers[4]
    else:
        return None
    
print(get_outlook_otp("michael.me2@hotmail.com","random1$A"))