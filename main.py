import os
from dotenv import load_dotenv

def get_token_from_env():
    token = os.getenv("DBX_RECIPIENT_TOKEN")
    if token is None:
        raise ValueError("DBX_RECIPIENT_TOKEN environment variable is not set.")
    return token

def main():
    load_dotenv()  # Load environment variables from .env file
    token = get_token_from_env()
    print("Hello from test-dbx-delta-share-access!")
    print(f"Using token: {token}")


if __name__ == "__main__":
    main()
