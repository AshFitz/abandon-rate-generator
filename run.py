import gspread
import os
import datetime
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    ******** Abandon Rate Generator ********
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
    This is calculated by dividing the number of abandonded calls by the total number of calls received.\n
    """)
    print(
    """
    Here is an example: If a call center receives 1000 calls and 50 of those calls are abandoned,
    the abandon rate is 5%.\n
    """)

    abandon_rate_options()


def abandon_rate_options():
    """
    Provide the user with two options. One option to generate the abandon rate
    by inputting recent call data or the other option to view recent abandon
    rates generated. Run a while loop to to check the users input. If True, the try
    block runs and the selected option is executed. If False handle the exception.

    """
    print("Enter '1' to generate the abandon rate? \n")

    print("Or\n")

    print("Enter '2' view previous abandon rates? \n")

    option_value =''
    while option_value not in [1, 2]:
        try:
            option_value = int(input("Choose your option: "))
            if option_value == 1:
                get_rep_name()
            elif option_value == 2:
                print("this will be the get call")
                get_call_sheet()
            else:
                print("Oops, you have entered {input} that is an invalid option".format(input=option_value))
                print("Please select option '1' or '2'")
                continue
        
        except ValueError:
            print("Sorry you have entered an invalid input, please select from option '1' or '2'")


def get_rep_name():
    """
    Get the representative's name from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must contain only alpha numeric values. The loop will
    repeatedly request data until the data is valid.
    """
    num = None
    print("Firstly, we need your name.\n")

    get_date()
    while num is None:
        input_value = input("Please enter your name here: ").lower().strip()
        if all(x.isalpha() or x.isspace() for x in input_value):
            num = input_value
            all_input_data.append(input_value)
            
            print("Thank you!.\n")
            get_job_title()
        else:
            print("Sorry we can't accept {input}, please enter text only.".format(input=input_value))


def get_job_title():
    """
    Get the uses job title.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must contain only alpha numeric values. The loop will
    repeatedly request data until the data is valid.
    """
    num = None
    print("We also need your job title.\n")
    
    while num is None:
        input_value = input("Please enter your job title here: ").lower().strip()
        if all(x.isalpha() or x.isspace() for x in input_value):
            num = input_value
            all_input_data.append(input_value)
            
            print("Thank you for letting us know your job title.\n")
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
        if all(x.isalpha() or x.isspace() for x in input_value):
            num = input_value
            all_input_data.append(input_value)
            
            print("Thank you!.\n")
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
            global inbound_calls
            
            if inbound_calls == None:
                inbound_calls = inbound_input
                all_input_data.append(inbound_calls)

            else:
                inbound_calls = None
            
        except ValueError:
            print(f"You have entered characters, please ensure it is only numbers")
            continue
        else:
            print("Yayy customers! You are nearly there!")
            get_dropped_calls()
        


def get_dropped_calls():
    """
    Get dropped call figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string with 1 number. The loop
    will repeatedly request data until the data is valid.
    """ 
    print("Finally we need you to enter the number of dropped calls.\n")

    while True: 
        try:
            dropped_input = int(input("Enter your data here: "))
            global dropped_calls 
            
            if dropped_calls == None: 
                dropped_calls = dropped_input
                all_input_data.append(dropped_calls)

            else: 
                inbound_calls = None   
            
        except ValueError:
            print(f"You have entered characters, please ensure it is only numbers")
            continue
        else:
            print("Now let's get generating!")
            calculate_abandon_rate()
          


def calculate_abandon_rate():
    """
    Calculate the abandon rate by dividing the dropped number
    of calls by the total number of inbound calls and multiplying the result by 100.
    Implement the format method which returns the devided calls as a string with 
    only 1 floating point number.
    """
    divided_calls = (dropped_calls / inbound_calls) * 100
    percentage = '{:.1f}'.format(divided_calls)
    print(f"{percentage}%")
    all_input_data.append(percentage +"%")

    update_call_worksheet(all_input_data)


def update_call_worksheet(data):
    """
    Update call worksheet, add new row with the list data provided.
    """

    print("Updating call worksheet.....\n")
    call_worksheet = SHEET.worksheet("call_data")
    call_worksheet.append_row(data)
    print("Call worksheet updated successfully!\n")




def get_call_sheet():
    print("Enter '1' to view all of the previous abandon rate submissions? \n")
    print("Or")
    print("Enter '2' to view the most recent abandon rate submission? \n")


    selected_option =''
    while selected_option not in [1, 2]:
        try:
            selected_option = int(input("Choose your option: "))
            if selected_option == 1:
                get_all_data = SHEET.worksheet("call_data").get_all_values()
                pprint(get_all_data)
                # start_generator()
            elif selected_option == 2:
                get_most_recent_data = SHEET.worksheet("call_data").get_all_values()
                last_row = get_most_recent_data[-1]
                pprint(last_row)
                # start_generator()
            else:
                print("Oops, you have entered {input} that is an invalid option".format(input=option_value))
                print("Please select option '1' or '2'")
                continue
        
        except ValueError:
            print("Sorry you have entered an invalid input, please select from option '1' or '2'")

def get_date():
    date = datetime.date.today()
    all_input_data.append(str(date))
    print(date)
    



def main():
    """
    Update!!!
    """
# def clear_terminal():
#     os.system('clear')

all_input_data = []

inbound_calls = None
dropped_calls = None

start_generator()
# get_call_sheet()
