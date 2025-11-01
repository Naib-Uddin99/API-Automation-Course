import requests

BASE_URL = "https://qa-student-management-system.vercel.app"

# GET request
response = requests.get(f"{BASE_URL}/api/student")
print("Status Code:", response.status_code)
print("Response Body:", response.json())
