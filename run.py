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



def get_rep_name():
    """
    Get the representative's name from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string. The loop will
    repeatedly request data until the data is valid.
    """

    while True:
        print("We need the representative's name.\n")

        rep_name_input = input("Please enter you name here: ")

        test = rep_name_input
        print(test)

        if validate_int(rep_name_input):
            all_input_data.append(rep_name_input)
            print(all_input_data)
            
        
            get_dept_name() 
            break
            

def get_dept_name():
    """
    Description needed
    """
    
    while True:
        print("Now we need your department name.")

        dep_name_input = input("Please enter the name of your department: ")

        if validate_int(dep_name_input):
            all_input_data.append(dep_name_input)
            print(all_input_data)
            
        
            get_inbound_calls()
            break




def get_inbound_calls():
    """
    Get call figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string with 1 number. The loop
    will repeatedly request data until the data is valid.
    """

    while True:   
        print("Enter the number of inbound calls received.\n")

        inbound_input = input("Enter your data here: ")

        inbound_calls = inbound_input
        print(inbound_calls)
       

        if validate_int(inbound_calls):
            print("Data is valid!")
            break

    return inbound_calls



def get_dropped_calls():
    """
    Description needed
    """





def validate_string(values):
    """
    Description needed
    """





def validate_int(values):
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


# def update_call_worksheet(data):
#     """
#     Update call worksheet, add the call data provided.
#     """

#     print("Updating call worksheet....\n")
#     call_worksheet = SHEET.worksheet("call_data")
#     call_worksheet.append_column(data)
#     print("Call worksheet updated successfully.\n")


# data = all_input_data

all_input_data = []
get_rep_name()
