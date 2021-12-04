import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('call_data')


def get_call_data():
    """
    Get call figures input from the user
    """
    print("Enter the number of inbound calls received.\n")

    data_str = input("Enter your data here: ")
    print(f"The figuers you entered are {data_str}")

get_call_data()