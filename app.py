from config import API_KEY, DB_PASSWORD
import requests

def make_request():
    url = f"https://api.example.com/data?token={API_KEY}"
    response = requests.get(url)
    print("Response status:", response.status_code)

def connect_db():
    print(f"Connecting to DB with password: {DB_PASSWORD}")
    # Fake DB connection logic
    return True

if __name__ == "__main__":
    make_request()
    connect_db()
