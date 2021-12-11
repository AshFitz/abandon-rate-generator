import gspread
import os
import datetime
from google.oauth2.service_account import Credentials
from generator.validations import validate_text, validate_numbers

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('call_data')


class Generator:
    """
    Constructor to initalize locally scoped lists.
    """
    def __init__(self):
        self.all_input_data = []
        self.inbound_calls = []
        self.dropped_calls = []
        self.dictionary = ['Date', 'Representative Name', 'Job Title', 'Department Name', 'Inbound Calls', 'Dropped Calls']

    def start_generator(self):
        print("""
        ------------------------------------
        ****** Abandon Rate Generator ******
        ------------------------------------
        """)
        print(r"""
                  _______________  
                /    ,,_____,,    \:.
                |__| [1][2][3] |__|:  :
                   / [4][5][6] \   :  :
                  /  [7][8][9]  \   :  :
                 /   [*][0][#]   \   ..
                |_________________|
        """)
        return self.description()

    def description(self):
        """
        Describe the generator functionality. Explain the meaning of abandon rate.
        """
        print("""
        The Abandon Rate Generator can be used to track how the call center is performing.\n
        """)

        print("""
        The abandon rate is the % of customers that abandon their call before speaking to a call center representative.
        This is calculated by dividing the number of abandonded calls by the total number of calls received.\n
        """)
        print("""
        Here is an example: If a call center receives 1000 calls and 50 of those calls are abandoned,
        the abandon rate is 5%.\n
        """)

        self.abandon_rate_options()

    def abandon_rate_options(self):
        """
        Provide the user with two options. One option to generate the abandon rate
        by inputting recent call data or the other option to view recent abandon
        rates generated. Run a while loop to to check the users input. If True, the try
        block runs and the selected option is executed. If False handle the exception.

        """
        print("Enter '1' to generate the abandon rate.")

        print("Or")

        print("Enter '2' view previous abandon rates.\n")

        option_value = ''
        while option_value not in [1, 2]:
            try:
                option_value = int(input("Choose your option:\n"))
                if option_value == 1:
                    self.get_rep_name()
                elif option_value == 2:
                    self.get_call_sheet()
                else:
                    print("Oops, you have entered {input} that is an invalid option".format(input=option_value))
                    print("Please select option '1' or '2'")
            except ValueError:
                print("Sorry you have entered an invalid input, please select from option '1' or '2'")

    def get_rep_name(self):
        """
        Get the representative's name from the user.
        Run a while loop to collect a valid string of data from the user
        via the terminal, which must contain only alpha numeric values. The loop will
        repeatedly request data until the data is valid.
        """
        print("Please provide us with your name.\n")
        self.get_date()

        while True:
            text_input = input("Enter your name here:\n").lower().strip()
            if (validate_text(text_input)):
                print("Thank you for your name.\n")
                self.all_input_data.append(text_input)
                self.get_job_title()
                break
            else:
                print("Sorry we can't accept {input}, please enter text only.".format(input=text_input))

    def get_job_title(self):
        """
        Get the uses job title.
        Run a while loop to collect a valid string of data from the user
        via the terminal, which must contain only alpha numeric values. The loop will
        repeatedly request data until the data is valid.
        """
        print("Please provide us with your job title.\n")
        
        while True:
            text_input = input("Enter your job title here:\n").lower().strip()
            if(validate_text(text_input)):
                print("Thank you for letting us know your job title.\n")
                self.all_input_data.append(text_input)
                self.get_dept_name()
                break
            else:
                print("Sorry we can't accept {input}, please enter text only.".format(input=text_input))

    def get_dept_name(self):
        """
        Get the department name from the user.
        Run a while loop to collect a valid string of data from the user
        via the terminal, which must contain only alpha numeric values. The loop will
        repeatedly request data until the data is valid.
        """
        print("Please provide us with your department name.\n")
        while True:
            text_input = input("Enter your department name here:\n").lower().strip()
            if(validate_text(text_input)):
                print("Thank you for letting us know your department.\n")
                self.all_input_data.append(text_input)
                self.get_inbound_calls()
                break
            else:
                print("Sorry we can't accept {input}, please enter text only.".format(input=text_input))

    def get_inbound_calls(self):
        """
        Get inbound call figures input from the user.
        Run a while loop to collect a valid string of data from the user
        via the terminal, which must be a string with 1 number. The loop
        will repeatedly request data until the data is valid.
        """
        print("Please enter the number of inbound calls, e.g.100.\n")
        while True:
            number_input = input("Enter the inbound calls here:\n")              
            if(validate_numbers(number_input)):
                self.inbound_calls.append(number_input)
                self.get_dropped_calls()
                break
            else:
                print("You have entered characters, please ensure it is only numbers")

    def get_dropped_calls(self):
        """
        Get dropped call figures input from the user.
        Run a while loop to collect a valid string of data from the user
        via the terminal, which must be a string with 1 number. The loop
        will repeatedly request data until the data is valid.
        """ 
        print("You are nearly there!")
        print("Please enter the number of dropped calls, e.g.5.\n") 

        while True: 
            number_input = input("Enter the number of dropped calls here:\n")
            inbound_to_check = int(self.inbound_calls[0])
            if(validate_numbers(number_input)):
                if(int(number_input) > inbound_to_check):
                    print("The number of inbound calls must be greater than the number of dropped calls.")
                    inbound_to_check = []
                    self.inbound_calls = []
                    return False
                else:
                    self.all_input_data.append(self.inbound_calls[0])
                    self.all_input_data.append(number_input)
                    self.dropped_calls.append(number_input)
                    print("Thank you!")
                    self.confirm_user_input()
                    return

            else:
                print("You have entered characters, please ensure it is only numbers")

    def confirm_user_input(self):
        """
        Display the user their current inputs as a list
        if user is happy calculate the abandon rate
        if not return to the start to try again.
        """
        print("Before we calculate the percentage we want to check if the information is correct.")         
        print(self.all_input_data)
        to_check = self.all_input_data
        
        for val, key in zip(self.dictionary, to_check):
            print(val,"=", key)
        print("If this information is correct type 'y' otherwise type 'n'")

        option_input = ''
        while option_input not in ['y', 'n']:
            try:
                option_input = input("Please enter 'y' or 'n':\n").lower().strip()
                if option_input == 'y':
                    self.calculate_abandon_rate()
                elif option_input == 'n':
                    self.start_generator()
                else:
                    print("Oops, you have entered {input} that is an invalid option".format(input=text_input))
                    print("Please select option 'y' or 'n'")

            except ValueError:
                print("Sorry you have entered an invalid input, please select from option 'y' or 'n'")

        

    def calculate_abandon_rate(self):
        """
        Calculate the abandon rate by dividing the dropped number
        of calls by the total number of inbound calls and multiplying the result by 100.
        Implement the format method which returns the devided calls as a string with 
        only 1 floating point number.
        """
        dropped_calls_to_calc = int(self.dropped_calls[0])
        inbound_calls_to_calc = int(self.inbound_calls[0])
        divided_calls = (dropped_calls_to_calc / inbound_calls_to_calc) * 100
        percentage = '{:.1f}'.format(divided_calls)
        print(f"{percentage}%")
        self.all_input_data.append(percentage + "%")
        self.update_call_worksheet(self.all_input_data)

        if(divided_calls < 5):
            print(
            """
            ----------------------------------------
            Your abandon rate is {percentage}% that is great
            ----------------------------------------
            """.format(percentage=percentage))
        elif(divided_calls >= 5):
            print("Your abandon rate is {percentage}% that is high".format(percentage=percentage))


    def update_call_worksheet(self, data):
        """
        Update call worksheet, add new row with the list data provided.
        """
        print("Updating call worksheet.....\n")
        call_worksheet = SHEET.worksheet("call_data")
        call_worksheet.append_row(data)
        print("Call worksheet updated successfully!\n")

    #to fix
    def get_call_sheet(self):
        print("Enter '1' to view the most recent abandon rate submission.")
        print("Or")
        print("Enter '2' to return home.\n")

        selected_option = ''
        while selected_option not in [1, 2]:
            try:
                selected_option = int(input("Choose your option:\n"))
                if selected_option == 1:
                    get_most_recent_data = SHEET.worksheet("call_data").get_all_values()
                    last_row = get_most_recent_data[-1]
                    self.clear_terminal()
                    print(last_row)
                    # self.clear_terminal()
                elif selected_option == 2:
                    self.start_generator()
                else:
                    print("Oops, you have entered {input} that is an invalid option".format(input=option_value))
                    print("Please select option '1' or '2'")
                    # continue
            
            except ValueError:
                print("Sorry you have entered an invalid input, please select from option '1' or '2'")

    def get_date(self):
        date = datetime.date.today()
        self.all_input_data.append(str(date))
        print(date)
        
    def clear_terminal(self):
        os.system('clear')

