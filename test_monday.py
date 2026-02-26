import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjYyNjM5MjY4OCwiYWFpIjoxMSwidWlkIjoxMDAzNjYxMzcsImlhZCI6IjIwMjYtMDItMjZUMTU6NDE6NDAuNDYyWiIsInBlciI6Im1lOndyaXRlIiwiYWN0aWQiOjMzOTg0NzY1LCJyZ24iOiJhcHNlMiJ9.tFsa_ir1pCkxTm4c5ZCu1c-UlhjBpo8gA-FexaZdYJw"
query = """
{
  boards(limit: 10) {
    id
    name
  }
}
"""

response = requests.post(
    "https://api.monday.com/v2",
    json={"query": query},
    headers={
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }
)

print("Status:", response.status_code)
print("Response:", response.json())