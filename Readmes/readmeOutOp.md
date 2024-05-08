# Outlook OTP Extractor for Social Media Reporting

This script extracts OTP (One-Time Password) codes from Outlook emails, primarily used for obtaining OTPs when submitting report forms on Facebook and Instagram.

## Prerequisites

- Python 3.x installed on your system
- `imaplib` library available (usually comes with Python standard library)
- `email` library available (usually comes with Python standard library)
- `re` library available (usually comes with Python standard library)

## Usage

1. Import the `get_outlook_otp` function from the script.
2. Provide your Outlook email address and password as arguments to the function.
3. The function connects to your Outlook account, fetches the latest email from the inbox, extracts the OTP code, and returns it.
4. You can then use the returned OTP code in your application, such as when submitting report forms on Facebook or Instagram.

## Important Note

Ensure that you provide valid Outlook credentials to authenticate with the Outlook server. This script assumes that the OTP code is contained within the latest email's body and follows a specific format (typically a 6-digit number). Adjustments may be needed based on variations in email formatting or OTP retrieval logic.
