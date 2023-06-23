import requests

def check_proxies():
    # Read the proxy list from the file
    with open('proxies.txt', 'r') as file:
        proxies = file.read().splitlines()

    # List to store the working proxies
    working_proxies = []

    # Set the login and password for authentication
    login = 'your_login'
    password = 'your_password'

    # Iterate through the proxies and check their availability
    for proxy in proxies:
        try:
            # Construct the proxy URL with authentication
            proxy_url = f'http://{login}:{password}@{proxy}'

            # Perform a request using the proxy
            response = requests.get('http://example.com', proxies={'http': proxy_url, 'https': proxy_url}, timeout=5)

            if response.ok:
                working_proxies.append(proxy)
        except requests.exceptions.RequestException:
            pass

    # Save the working proxies to the result file
    with open('result.txt', 'w') as result_file:
        result_file.write('\n'.join(working_proxies))

    print(f"Total working proxies: {len(working_proxies)}")
    print("Working proxies saved to result.txt")

# Execute the check_proxies function
check_proxies()
