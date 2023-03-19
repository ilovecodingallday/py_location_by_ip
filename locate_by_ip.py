import requests

ip_address = input("Enter the IP address: ")

# Make a GET request to the IP-API
response = requests.get("http://ip-api.com/json/{}".format(ip_address))

# Check if the response was successful
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()

    # Print out the location information
    print("\nIP Address: ", data["query"])
    print("City: ", data["city"])
    print("Region: ", data["regionName"])
    print("Country: ", data["country"])
    print("Latitude: ", data["lat"])
    print("Longitude: ", data["lon"])
else:
    print("Error: Unable to retrieve location information")










