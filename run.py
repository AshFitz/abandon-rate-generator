import gspread
import os
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


#string input only
def get_rep_name():
    """
    Get the representative's name from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must contain only alpha numeric values. The loop will
    repeatedly request data until the data is valid.
    """
    clear_terminal()
    num = None
    print("We need the representative's name.\n")

    while num is None:
        input_value = input("Please enter your name here: ").lower().strip()
        if input_value.isalpha():
            num = input_value
            
            print("Thank you for your name \n")
            get_dept_name()
        else:
            print("Sorry you have entered {input}, please enter text only.".format(input=input_value))


#string input only
def get_dept_name():
    """
    Get the department name from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must contain only alpha numeric values. The loop will
    repeatedly request data until the data is valid.
    """
    clear_terminal()
    print("Now we need your department name. \n")
    while True:
        dep_name_input = input("Please enter the name of your department: ").lower().strip()

        if dep_name_input.isalpha():
            print("Thank you for your department name \n")

        else: 
            print("Sorry you have entered {input}, please enter text only.".format(input=dep_name_input))  



#num
def get_inbound_calls():
    """
    Get call figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string with 1 number. The loop
    will repeatedly request data until the data is valid.
    """

    while True: 
        print("Enter the number of inbound calls received.\n")

        try:

            inbound_input = int(input("Enter your data here: "))

        except ValueError:
            print(f"You have entered characters, please ensure it is only numbers")
            continue
        else:
            print("that all worked ok")
            break   


#num
def get_dropped_calls():
    """
    Description needed
    """ 

# def update_call_worksheet(data):
#     """
#     Update call worksheet, add the call data provided.
#     """

#     print("Updating call worksheet....\n")
#     call_worksheet = SHEET.worksheet("call_data")
#     call_worksheet.append_column(data)
#     print("Call worksheet updated successfully.\n")


# data = all_input_data

def clear_terminal():
    os.system('clear')


all_input_data = []
get_rep_name()
