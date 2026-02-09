# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "delta-sharing",
#     "pandas",
# ]
# ///
import os
import delta_sharing
import argparse

FILE_PATH = f"{os.getcwd()}/config.share"

def get_token_from_env():
    token = os.getenv("DBX_RECIPIENT_TOKEN")
    if token is None:
        raise ValueError("DBX_RECIPIENT_TOKEN environment variable is not set.")
    return token

def load_table_as_pandas(table_name):
    return delta_sharing.load_as_pandas(f"{FILE_PATH}#{table_name}")

def get_all_tables():
    client = delta_sharing.SharingClient(FILE_PATH)
    return client.list_all_tables()

def main():
    parser = argparse.ArgumentParser(description='Load Delta Sharing table as pandas DataFrame')
    parser.add_argument('--table', help='Name of the table to load')
    args = parser.parse_args()
    table = args.table

    if (table is not None):
        result = load_table_as_pandas(table)
        print("\nDataFrame info:")
        result.info()
        print(result)
        
    else:
        print("Shared tables:\n")
        tables = get_all_tables()
        for table in tables:
            print(table)

if __name__ == "__main__":
    main()
