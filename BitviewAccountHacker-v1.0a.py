import requests
from requests.models import Response

API_URL = "https://api-inference.huggingface.co/models/roberta-large"
headers = {"Authorization": " "}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
## response= bitview(query(payload))
## print(response)
output = query({"inputs": "Enter your sql database to hack."})
print(query({"C:\\Users\\Public\\Documents\\Bitview\\Bitview.db": "password"}))

## Import the sqlite3 library
import sqlite3
print("Scanning Bitview database for passwords")
## Connect to the database
conn = sqlite3.connect('C:\\Users\\Public\\Documents\\Bitview\\Bitview.db')
c = conn.cursor()
## Query the database
c.execute("SELECT * FROM tbl_user")
## Loop through the results

# import sqldatabase
# import sqlite3
for row in c:
	print(row)
	print("\n")
	print("Scanning password database")
	print("\n")
	cursor = conn.cursor()
 
	print(Response,cursor)
conn.close()
 