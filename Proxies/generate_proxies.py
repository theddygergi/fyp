import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time


# Function to scrape proxies from a website
def scrape_proxies(url):
    proxies = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for row in soup.find_all('tr'):
                columns = row.find_all('td')
                if len(columns) >= 2:
                    proxy = columns[0].text.strip() + ':' + columns[1].text.strip()
                    proxies.append(proxy)
    except Exception as e:
        print(f"Error scraping proxies from {url}: {e}")
    return proxies

# Function to check proxy connectivity
def check_proxy(proxy):
    try:
        response = requests.get('https://www.google.com', proxies={"https": proxy}, timeout=10)
        if response.status_code == 200:
            return proxy
    except Exception as e:
        pass
    return None

# Main function to generate working proxies and save to a text file
def generate_working_proxies():
    # List of URLs to scrape proxies from
    urls = [
        'https://www.sslproxies.org/',
        'https://free-proxy-list.net/'
        # Add more URLs if needed
    ]

    # Scrape proxies from each URL
    all_proxies = []
    for url in urls:
        all_proxies.extend(scrape_proxies(url))

    # Remove duplicate proxies
    all_proxies = list(set(all_proxies))

    # Check the connectivity of proxies
    working_proxies = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_proxy, proxy) for proxy in all_proxies]
        for future in futures:
            result = future.result()
            if result:
                working_proxies.append(result)

    # Save working proxies to a text file
    with open('working_proxies.txt', 'w') as file:
        for proxy in working_proxies:
            file.write(proxy + '\n')

    print(f"Total working proxies: {len(working_proxies)}")
    print("Working proxies saved to 'working_proxies.txt'")
    return working_proxies

