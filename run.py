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


def start_generator():
    print("""
    -----------------------------------------
    ******** Aboandon Rate Generator ********
    -----------------------------------------
    """)
    print(r"""
              _              _
             | |------------| |
          .-'| |            | |`-.
        .'   | |            | |   `.
     .-'      \ \          / /      `-.
   .'        _.| |--------| |._        `.
  /    -.  .'  | |        | |  `.  .-    \
 /       `(    | |________| |    )'       \
|          \  .i------------i.  /          |
|        .-')/                \(`-.        |
\    _.-'.-'/     ________     \`-.`-._    /
 \.-'_.-'  /   .-' ______ `-.   \  `-._`-./\
  `-'     /  .' .-' _   _`-. `.  \     `-' \\
         | .' .' _ (3) (2) _`. `. |        //
        / /  /  (4)  ___  (1)_\  \ \       \\
        | | |  _   ,'   `.==' `| | |       //
        | | | (5)  | A.F | (O) | | |      //
        | | |   _  `.___.' _   | | |      \\
        | \  \ (6)  _   _ (9) /  / |      //
        /  `. `.   (7) (8)  .' .'  \      \\
       /     `. `-.______.-' .'     \     //
      /        `-.________.-'        \ __//
     |                                |--'
     |================================|
     "--------------------------------"
    """)
    description()



def description():
    """
    Describe the generator functionality. Explain the meaning of abandon rate.
    """
    print(
    """
    The Abandon Rate Generator can be used track how a call center is performing.\n
    """)

    print(
    """
    The abandon rate is the percentage of customers that abandon their call before speaking to a call center representative.
    This is calculated by dividing the number of abandonded call by the total number of calls received.\n
    """)
    print(
    """
    Here is an example: If a call center receives 1000 calls and 50 of those calls are abandoned,
    the abandon rate is 5%.\n
    """)

    get_rep_name()

    # print("Do you want to generate your abandon rate?\n")

    # print("Or\n")

    # print("Do you want to view your previous abandon rate?")



def get_rep_name():
    """
    Get the representative's name from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must contain only alpha numeric values. The loop will
    repeatedly request data until the data is valid.
    """
    num = None
    print("We need the representative's name.\n")

    while num is None:
        input_value = input("Please enter your name here: ").lower().strip()
        if input_value.isalpha():
            num = input_value
            
            print("Thank you for your name.\n")
            get_dept_name()
        else:
            print("Sorry we can't accept {input}, please enter text only.".format(input=input_value))



def get_dept_name():
    """
    Get the department name from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must contain only alpha numeric values. The loop will
    repeatedly request data until the data is valid.
    """
    num = None
    print("Now we need your department name.\n")
    
    while num is None:
        input_value = input("Please enter your department name here: ").lower().strip()
        if input_value.isalpha():
            num = input_value
            
            print("Thank you for your letting us know your department.\n")
            get_inbound_calls()
        else:
            print("Sorry we can't accept {input}, please enter text only.".format(input=input_value))




def get_inbound_calls():
    """
    Get inbound call figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string with 1 number. The loop
    will repeatedly request data until the data is valid.
    """
    print("Next we need you to enter the number of inbound calls received.\n")

    while True: 
        try:
            inbound_input = int(input("Please enter the inbound calls here: "))
            inbound_calls = inbound_input
            all_input_data.append(inbound_input)

        except ValueError:
            print(f"You have entered characters, please ensure it is only numbers")
            continue
        else:
            print("Yayy customers.")
            get_dropped_calls()
        


def get_dropped_calls():
    """
    Get dropped call figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string with 1 number. The loop
    will repeatedly request data until the data is valid.
    """ 
    print("Enter the number of dropped calls.\n")

    while True: 
        try:

            dropped_input = int(input("Enter your data here: "))
            dropped_calls = dropped_input
            all_input_data.append(dropped_input)

        except ValueError:
            print(f"You have entered characters, please ensure it is only numbers")
            continue
        else:
            print("Its sad to miss customer calls....But you are nearly there!")
          


# def calculate_abandon_rate():

# def clear_terminal():
#     os.system('clear')

# all_input_data = []
start_generator()