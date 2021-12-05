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

    while True:   
        print("Enter the number of inbound calls received.\n")

        data_request = input("Enter your data here: ")

        call_data = data_request.split(",")
        

        if validate_data(call_data):
            print("Data is valid!")
            break

    return call_data


def validate_data(values):
    """
    Converts string values into integers.
    Raises ValueError if strings cannot be coverted into int,
    or if there is more than one value.
    """
    try:
        [int(value) for value in values]
        if len(values) != 1:
            raise ValueError(
                f"Only 1 value is required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


data = get_call_data()