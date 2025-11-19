import random
import time

import requests
import pytest
from pprint import pformat

# --- Configuration Constants ---
BASE_URL = "https://qa-student-management-system.vercel.app"
API_ENDPOINT = "/api/student"
SAFE_PAGE_SIZE = 10

# Define a consistent schema for validation
REQUIRED_STUDENT_SCHEMA = {
    "_id": str,
    "department": str,
    "email": str,
    "name": str,
    "registrationId": int,

}

OPTIONAL_STUDENT_SCHEMA = {
    "age":int
}


@pytest.fixture(scope="module")
def api_config():
    """Provides base configuration for all tests."""
    return {
        "BASE_URL": BASE_URL,
        "API_ENDPOINT": API_ENDPOINT,
        "REQUIRED_SCHEMA": REQUIRED_STUDENT_SCHEMA,
        "OPTIONAL_SCHEMA": OPTIONAL_STUDENT_SCHEMA,
        "PAGE_SIZE": SAFE_PAGE_SIZE
    }


@pytest.fixture(scope="module")
def student_data():
    """Provides valid data for creating a test student."""
    # Generate unique email using timestamp and random number
    timestamp = int(time.time())
    random_num = random.randint(1000, 9999)
    unique_email = f"test.student.{timestamp}.{random_num}@example.com"

    return {
        "name": "Fixture Test Student",
        "email": unique_email,
        "department": "CSE",
        "registrationId": timestamp
    }


@pytest.fixture(scope="module")
def created_student_id(api_config, student_data):
    """
    Creates a student before the module tests run and cleans it up afterward.
    Yields the ID of the created student.
    """
    base_url = api_config['BASE_URL']
    api_endpoint = api_config['API_ENDPOINT']

    create_url = f"{base_url}{api_endpoint}"
    print(f"\n[SETUP] Creating test student: {student_data['name']}")
    response = requests.post(create_url, json=student_data)

    assert response.status_code == 201, (
        f"Setup Failed: Could not create student. "
        f"Status: {response.status_code}, Response: {response.text}"
    )

    student_id = response.json().get("_id")
    assert student_id is not None, "Setup Failed: Created student missing _id."

    yield student_id

    delete_url = f"{base_url}{api_endpoint}/{student_id}"
    print(f"\n[TEARDOWN] Deleting test student with ID: {student_id}")
    requests.delete(delete_url)
    # The cleanup will now likely succeed since the student was created successfully.