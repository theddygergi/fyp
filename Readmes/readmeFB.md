# Facebook Copyright Form Automation Script

This Python script automates the process of submitting a copyright infringement report on Facebook's platform.

## Prerequisites

- Python 3.x installed on your system
- Necessary Python packages installed: Selenium, Undetected-Chromedriver, BeautifulSoup.

## Installation
- Install the required Python packages using pip:
```bash
   pip install selenium undetected-chromedriver beautifulsoup4
```

## Usage

1. Make sure you have a Facebook account and valid credentials.
2. Update the `email_element.send_keys()` and `password_element.send_keys()` lines with your Facebook login credentials.
3. Customize the script according to your specific requirements:
   - Modify the `photo_url.send_keys()` and `photo_url2.send_keys()` lines with the URLs of the photos you want to report.
   - Adjust any other input values as needed based on your specific use case.


## Important Note

- It's recommended to review and customize the script according to your specific requirements before running it in a production environment.
