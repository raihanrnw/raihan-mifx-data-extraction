import requests
import csv

# defined the headers with my personal API key because without key got error missing_api_key
headers = {
    "x-api-key": "reqres_b2acd70468a54b77a975410b9acd7de5"
}

# passing the headers into get request api
response = requests.get("https://reqres.in/api/users?page=2", headers=headers)

# if condition when status code 200 OK then we will convert to csv and generate value to csv
if response.status_code == 200:
    users = response.json()["data"]

    #  created file as users.csv
    with open("users.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["first_name", "last_name", "email"], extrasaction='ignore')

        # this to create csv column and the values
        writer.writerow({"first_name": "First Name", "last_name": "Last Name", "email": "Email"})

        # write into users.csv file
        writer.writerows(users)

        # logging if write is successful
    print("Convert Done! File csv generated successfully, please check the users.csv on root directory")
else:
        # logging else status code get api it not 200
    print(f"Failed to fetch data, Status code: {response.status_code}")