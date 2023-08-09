#!/usr/bin/python3
import requests

# Set up the API endpoint and parameters
api_url = "https://api.datadoghq.com/api/v1/dashboard/"
api_key = '7affd2815a0d36afaf4fa0da7323d110'
api_app_key = '7ec7b31584d4d7fe24d336f89af66af8dfc0fc8c'
headers = {
    'Content-type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': api_app_key
}
query_params = {'filter': 'host:145153'}

# Make the API call to get the host details
response = requests.get(api_url, headers=headers, params=query_params)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()
    print(response_json)

