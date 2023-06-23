Simnple http proxy checker with auth. We read the list of proxies from the proxies.txt file, iterate through each proxy, and construct the proxy URL with authentication credentials. We then make a request using the constructed proxy URL, and if the response is successful, we add the proxy to the list of working proxies.

Finally, we save the working proxies to the result.txt file, print the total count of working proxies, and indicate that the working proxies have been saved to the file.

Please make sure to replace 'your_login' and 'your_password' with your actual authentication credentials, and ensure that the proxies.txt file is in the same directory as the script.
