import requests

BASE_URL = "https://qa-student-management-system.vercel.app"

# POST request
new_user = {
    "name": "Naib Uddin",
    "email": "afmn.uddin@asthait.com",
    "department": "CSE",
    "registrationId": 698746,
    "age": 25
  }
post_response = requests.post(f"{BASE_URL}/api/student", json=new_user)
print("POST Response:", post_response.json())

# PUT request
# update_user = {"name": "Alice Updated", "email": "alice@updated.com"}
# put_response = requests.put(f"{BASE_URL}/users/1", json=update_user)
# print("PUT Response:", put_response.json())
#
# # DELETE request
# delete_response = requests.delete(f"{BASE_URL}/users/1")
# print("DELETE Status Code:", delete_response.status_code)