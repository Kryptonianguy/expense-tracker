import pytest
import requests
import sqlite3
from werkzeug.security import check_password_hash
from website import create_app

"""This function tests whether the login page loads or not."""
def test_login_page_loads_or_not():
    url = "http://127.0.0.1:5000/login"
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Assert the status code to be 200 (OK)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        print("Login Page loaded SUCCESSFULLY!")
    except requests.exceptions.ConnectionError:
        pytest.fail("Failed to connect to the server. Make sure the server is running.")

# Fetch an existing user from the database
def get_existing_user():
    db_path = "D:/Projects/expense-tracker/website/expense_tracker.db"  # Use forward slashes for compatibility
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM User WHERE email = ?", ("sachin@sach.com",))
    user = cursor.fetchone()
    conn.close()
    return user

# Setup fixture to check login page accessibility
@pytest.fixture
def setup_method():
    print("Setting up the Environment")
    url = "http://127.0.0.1:5000/login"
    response = requests.get(url)
    assert response.status_code == 200, "Failed to connect to the login page."
    return response

# Setup Flask test client fixture
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True  # Enable test mode
    with app.test_client() as client:
        yield client  # Provide the test client to the tests

"""Function to Test login with valid credentials"""
def test_login_with_valid_credentials(client):
    user = get_existing_user()
    if not user:
        pytest.fail("No user found in the database")

    username, hashed_password = user
    input_password = "sach1234"  # Replace with actual test password

    if not check_password_hash(hashed_password, input_password):
        pytest.fail("Password does not match stored hash")

    response = client.post("/login", data={"username": username, "password": input_password})
    assert response.status_code == 200, "Login failed with valid credentials"

# Teardown fixture
@pytest.fixture
def teardown_method():
    print("Tearing down the test Environment")


# def test_login_with_unregistered_email():
#     pass
#
# def test_login_with_invalid_password():
#     pass
#
# def test_login_with_empty_fields():
#     pass
#
# def test_login_with_sql_injection():
#     pass