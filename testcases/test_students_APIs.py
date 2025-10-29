import requests
import time
from pprint import pformat

BASE_URL = "https://qa-student-management-system.vercel.app"


# HEADERS = {
#     "Authorization": "Bearer your_token_here",  # Replace with valid token if needed
#     "Content-Type": "application/json"
# }


# def test_get_users():
#     response = requests.get(f"{BASE_URL}/api/student")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)


def test_get_all_students_api():
    api_endpoint = "/api/student"
    params = {"pageSize": -1}

    # Step 1: Send GET request
    response = requests.get(f"{BASE_URL}{api_endpoint}", params=params)
    time.sleep(2)  # small delay

    # Step 2: Validate response status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Step 3: Parse JSON response
    json_response = response.json()

    # Step 5: Define expected schema for course object
    student_schema = {
        "_id": str,
        "name": str,
        "email": str,
        "department": str,
        "registrationId": int,
        "age": int
    }

    # Step 6: Validate each course object
    for user in json_response:
        user_name = user["name"]

        # Ensure correct schema
        expected_keys = set(student_schema.keys())
        actual_keys = set(user.keys())
        assert expected_keys == actual_keys, (
            f"❌ Schema mismatch in user '{user_name}'.\n"
            f"Expected keys:\n{pformat(expected_keys)}\nGot:\n{pformat(actual_keys)}"
        )
        # Validate data types
        for key, expected_type in student_schema.items():
            assert isinstance(user[key], expected_type), (
                f"❌ Invalid type for '{key}' in user '{user_name}'. "
                f"Expected {expected_type.__name__}, got {type(user[key]).__name__}"
            )

        print(f"✅ User '{user_name}' validated successfully.")


def test_search_students_by_name():
    api_endpoint = "/api/student"
    params = {"pageSize": -1}

    # Step 1: Send GET request
    response = requests.get(f"{BASE_URL}{api_endpoint}", params=params)
    time.sleep(2)  # small delay

    # Step 2: Validate response status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Step 3: Parse JSON response
    student_list_response_data = response.json()
    print("List of Students JSON", student_list_response_data)
    for student in student_list_response_data:
        expected_student_name = student['name']
        expected_student_email = student['email']
        expected_student_department = student['department']
        expected_student_registration_id = student['registrationId']
        #expected_student_age = student['age']

        print("[DEBUG] Student Name", expected_student_name)

        params = {
            "name": expected_student_name
        }
        response = requests.get(f"{BASE_URL}{api_endpoint}", params=params)

        response_data = response.json()

        for filtered_student in response_data:
            actual_student_name = filtered_student['name']
            actual_student_email = filtered_student['email']
            actual_student_department = filtered_student['department']
            actual_student_registration_id = filtered_student['registrationId']
            #actual_student_age = filtered_student['age']



            print("[DEBUG] Actual Student Name", actual_student_name)

            assert expected_student_name.lower() in actual_student_name.lower(), f"ASSERTION FAILED: Search query did not return the correct list of venues in the API response. actual_name:'{actual_student_name}', search_param:'{expected_student_name}'"
            print(
                f"✅ ASSERTION PASSED: Search query returned the correct list of students in the API response. actual_name:'{actual_student_name}' , search_param:'{expected_student_name}'")

            assert expected_student_email.lower() in actual_student_email.lower(), f"ASSERTION FAILED: Search query did not return the correct list of venues in the API response. actual_email:'{actual_student_email}', search_param:'{expected_student_name}'"
            print(
                f"✅ ASSERTION PASSED: Search query returned the correct list of students in the API response. actual_email:'{actual_student_email}' , search_param:'{expected_student_name}'")

            assert expected_student_department.lower() in actual_student_department.lower(), f"ASSERTION FAILED: Search query did not return the correct list of venues in the API response. actual_department:'{actual_student_department}', search_param:'{expected_student_name}'"
            print(
                f"✅ ASSERTION PASSED: Search query returned the correct list of students in the API response. actual_department:'{actual_student_department}' , search_param:'{expected_student_name}'")

            assert expected_student_registration_id == actual_student_registration_id, f"ASSERTION FAILED: Search query did not return the correct list of venues in the API response. actual_registration_id:'{actual_student_registration_id}', search_param:'{expected_student_name}'"
            print(
                f"✅ ASSERTION PASSED: Search query returned the correct list of students in the API response. actual_registration_id:'{actual_student_registration_id}' , search_param:'{expected_student_name}'")

           # assert expected_student_age == actual_student_age, f"ASSERTION FAILED: Search query did not return the correct list of venues in the API response. actual_age:'{actual_student_age}', search_param:'{expected_student_name}'"
           # print(
           #     f"✅ ASSERTION PASSED: Search query returned the correct list of students in the API response. actual_age:'{actual_student_age}' , search_param:'{expected_student_name}'")