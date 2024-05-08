# Outlook OTP Extractor for TikTok Verification

This script is designed to extract email verification links from Outlook emails, specifically for TikTok verification mails sent when first time verifying for TikTok copyright.

## Prerequisites

- Python 3.x installed on your system
- `imaplib` library available (usually comes with Python standard library)
- `email` library available (usually comes with Python standard library)
- `BeautifulSoup` library available (can be installed via pip)

## Usage

1. Import the `get_outlook_otp` function from the script.
2. Provide your Outlook email address and password as arguments to the function.
3. The function connects to your Outlook account, fetches the latest email from the inbox, extracts the HTML content, and parses it to find the verification link.
4. If a verification link is found, it is returned by the function.
5. You can then use the verification link in your application, such as for completing email verification processes when signing up for online services.



## Important Note

Ensure that you provide valid Outlook credentials to authenticate with the Outlook server. This script assumes that the verification link is contained within the latest email's HTML content and follows a specific format. Adjustments may be needed based on variations in email formatting or verification link retrieval logic.

