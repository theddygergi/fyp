from bs4 import BeautifulSoup
import imaplib
import email

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

    # Initialize body variable
    body = ""

    # Check content type and extract body
    if message.is_multipart():
        for part in message.walk():
            content_type = part.get_content_type()
            if content_type == "text/html":
                body = part.get_payload(decode=True).decode()
                break
    else:
        body = message.get_payload(decode=True).decode()

    # Close the connection
    mail.close()
    mail.logout()

    # Parse HTML content to find the verification link
    if body:
        soup = BeautifulSoup(body, "html.parser")
        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if "verify-email" in href:
                return href

    return None

