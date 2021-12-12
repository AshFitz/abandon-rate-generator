import gspread
import os
import datetime
from google.oauth2.service_account import Credentials
from generator.validations import validate_text, validate_numbers

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("call_data")


class Generator:
    """
    Constructor to initalize locally scoped lists in
    current instance.
    """

    def __init__(self):
        self.all_input_data = []
        self.inbound_calls = []
        self.dropped_calls = []
        self.dictionary = [
            "Date",
            "Representative Name",
            "Job Title",
            "Department Name",
            "Inbound Calls",
            "Dropped Calls",
        ]

    def start_generator(self):
        """
        Start generator is called and used to
        display print statements to the user.
        """

        print(
            """
        ------------------------------------
        ****** Abandon Rate Generator ******
        ------------------------------------"""
        )
        print(
            r"""
                  _______________
                /    ,,_____,,    \:.
                |__| [1][2][3] |__|:  :
                   / [4][5][6] \   :  :
                  /  [7][8][9]  \   :  :
                 /   [*][0][#]   \   ..
                |_________________|"""
        )

        self.description()

    def description(self):
        """
        Describes the generator functionality. Explain the meaning
        of abandon rate to the user.
        """
        print(
            """
        The Abandon Rate Generator can be used to track how the call center
        is performing.\n
        """
        )

        print(
            """
        The abandon rate is the % of customers that abandon their call before
        speaking to a call center representative.
        This is calculated by dividing the number of abandonded calls by the
        total number of calls received.\n
        """
        )
        print(
            """
        Here is an example: If a call center receives 1000 calls and
        50 of those calls are abandoned,
        the abandon rate is 5%.\n
        """
        )

        input("Press enter to continue....")
        if input:
            self.abandon_rate_options()

    def abandon_rate_options(self):
        """
        Provide the user with two options. One option to navigate to
        generate the abandon rate area. The other to navigate to
        view previous abandon rates. Check that 1, 2 is in the option
        value, if it is, use conditions to determain what is called next
        handle the value error with an exception to notify user of invalid
        input.
        """
        self.clear_terminal()
        print("Enter '1' to generate the abandon rate.")

        print("Or")

        print("Enter '2' view previous abandon rates.\n")

        option_value = ""
        while option_value not in [1, 2]:
            try:
                option_value = int(input("Choose your option:\n"))
                if option_value == 1:
                    self.clear_terminal()
                    self.get_rep_name()
                    break
                elif option_value == 2:
                    self.clear_terminal()
                    self.get_call_sheet()
                    break
                else:
                    print(
                        "Oops, you have entered {input}"
                        "that is an invalid option".format(
                            input=option_value
                        )
                    )
                    print("Please select option '1' or '2'")
                    continue
            except ValueError:
                print(
                    "Sorry you have entered an invalid input,"
                    "please select from option '1' or '2'"
                )

    def get_rep_name(self):
        """
        Get the representative's name from the user.
        Run a while loop to collect a valid string of data from the user
        via the terminal, is passed to the validate_text function, this
        then checks if the string is valid using built in methods,
        I set the input to lower and strip white spacing to ensure
        easier validation.
        The loop will repeatedly request data until the data is valid.
        when the contition returns true from validating, we proceed with
        clearing the terminal, update the user of the success, add the
        input to a list, and call the next function.
        """
        print("Please provide us with your name.\n")
        self.get_date()

        while True:
            text_input = input("Enter your name here:\n").lower().strip()
            if validate_text(text_input):
                self.clear_terminal()
                print("Thank you for your name.\n")
                self.all_input_data.append(text_input)
                self.get_job_title()
                break
            else:
                print(
                    "Sorry we can't accept {input},"
                    "please enter text only.".format(
                        input=text_input
                    )
                )

    def get_job_title(self):
        """
        Get the users job title.
        Run a while loop and collect a users input, attempt to validate
        the string of data from the user via the terminal,
        which must contain only alpha numeric values.
        The loop will repeatedly request data until the data is valid.
        when the contition returns true from validating, we proceed with
        clearing the terminal, update the user of the success, add the
        input to a list, and call the next function.
        """
        print("Please provide us with your job title.\n")

        while True:
            text_input = input("Enter your job title here:\n").lower().strip()
            if validate_text(text_input):
                self.clear_terminal()
                print("Thank you for letting us know your job title.\n")
                self.all_input_data.append(text_input)
                self.get_dept_name()
                break
            else:
                print(
                    "Sorry we can't accept {input},"
                    "please enter text only.".format(
                        input=text_input
                    )
                )

    def get_dept_name(self):
        """
        Get the department name from the user.
        collect an input from the user, pass the input to the validate_text
        function the function must only return alphabatical chars,
        if it returns true, clear terminal, update user with success,
        append the input to the list, and call the next function.
        If it fails, handle it by outputting to the user their
        input was invalid and what to do, to fix the issue.
        """
        print("Please provide us with your department name.\n")
        while True:
            text_input = input("Enter your department"
                               "name here:\n").lower().strip()
            if validate_text(text_input):
                self.clear_terminal()
                print("Thank you for letting us know your department.\n")
                self.all_input_data.append(text_input)
                self.get_inbound_calls()
                break
            else:
                print(
                    "Sorry we can't accept {input},"
                    "please enter text only.".format(
                        input=text_input
                    )
                )

    def get_inbound_calls(self):
        """
        Get inbound call figures input from the user via input.
        pass the input to the validate_numbers function, if it
        returns true we proceed by clearing the terminal,
        append the input to the inbound_calls list, notify the
        user their input has worked and call the next function.
        If it returns false, handle it by outputting to the user
        their input was invalid and how to fix it.
        """
        print("Please enter the number of inbound calls, e.g.'100'.\n")
        while True:
            number_input = input("Enter the inbound calls here:\n")
            if validate_numbers(number_input):
                self.clear_terminal()
                self.inbound_calls.append(number_input)
                print("Thank you!")
                self.get_dropped_calls()
                break
            else:
                print("You have entered characters,"
                      "please ensure it is only numbers")

    def get_dropped_calls(self):
        """
        Get dropped call figures input from the user via input,
        Validate the input by passing the validate_numbers function
        the users input, if it returns true, clear the terminal and
        also store the first item in the inbound calls list to a new
        variable called inbound to check, this then allows us to handle
        if the dropped calls number is greater than the inbound calls.
        Handle by letting the user know if it is greater than inbound calls
        print message to user, reset the inbound_to_check to an empty list.
        If it passes validation, append to the lists. Notify user of success.
        Call next func which allows the user to verify their inputs before
        posting to the spreadsheet.
        """
        print("You are nearly there!")
        print("Please enter the number of dropped calls, e.g.'5'.\n")

        while True:
            number_input = input("Enter the number of dropped calls here:\n")
            inbound_to_check = int(self.inbound_calls[0])
            if validate_numbers(number_input):
                self.clear_terminal()
                if int(number_input) > inbound_to_check:
                    print(
                        "The number of inbound calls must be greater than"
                        "the number of dropped calls."
                    )
                    inbound_to_check = []
                    self.inbound_calls = []
                    break
                else:
                    self.all_input_data.append(self.inbound_calls[0])
                    self.all_input_data.append(number_input)
                    self.dropped_calls.append(number_input)
                    print("Thank you!")
                    self.confirm_user_input()

            else:
                print("You have entered characters,"
                      "please ensure it is only numbers")

    def confirm_user_input(self):
        """
        Display the user their current inputs as a list
        if user is happy with their inputs we calculate the abandon rate
        Run a forloop on the dict that hold the keys, and also the
        to check list, and print them together for ease of viewing.
        if not return to the start to try again. Handle any exeptions.
        """
        print(
            "Before we calculate the percentage we want to check"
            "if the information is correct.\n"
        )
        to_check = self.all_input_data

        for val, key in zip(self.dictionary, to_check):
            print(val, "=", key)
        print("\nIf this information is correct type 'y' otherwise type 'n'")

        option_input = ""
        while option_input not in ["y", "n"]:
            try:
                option_input = input("Please"
                                     "enter 'y' or 'n':\n").lower().strip()
                if option_input == "y":
                    self.clear_terminal()
                    self.calculate_abandon_rate()
                elif option_input == "n":
                    self.clear_terminal()
                    self.start_generator()
                else:
                    print(
                        "Oops, you have entered {input} that is"
                        "an invalid option".format(
                            input=option_input
                        )
                    )
                    print("Please select option 'y' or 'n'")

            except ValueError:
                print(
                    "Sorry you have entered an invalid input, please select"
                    "from option 'y' or 'n'"
                )

    def calculate_abandon_rate(self):
        """
        Calculate the abandon rate by dividing the dropped number of calls by
        the total number of inbound calls and multiplying the result by 100.
        Implement the format method which returns the devided calls as a string
        with only 1 floating point number, check conditions if
        its below a number notify the user of the condition
        all the user to continue by pressint enter.
        """
        dropped_calls_to_calc = int(self.dropped_calls[0])
        inbound_calls_to_calc = int(self.inbound_calls[0])
        divided_calls = (dropped_calls_to_calc / inbound_calls_to_calc) * 100
        percentage = "{:.1f}".format(divided_calls)
        self.all_input_data.append(percentage + "%")
        self.update_call_worksheet(self.all_input_data)

        if divided_calls < 5:
            print(
                """
            ----------------------------------------
            Your abandon rate is {percentage}% that is great
            ----------------------------------------
            """.format(
                    percentage=percentage
                )
            )
            input("Press enter to return to the start....")
            if input:
                self.start_generator()
        elif divided_calls >= 5:
            print(
                "Your abandon rate is {percentage}% that is high".format(
                    percentage=percentage
                )
            )
            input("Press enter to return to the start....")
            if input:
                self.start_generator()

    def update_call_worksheet(self, data):
        """
        Update call worksheet takes one parameter,
        specify the worksheet name, update a new
        row with the data thats has been passed as arguement.
        Update the user with a print statement to say its updating.
        and when it was successful.
        """
        print("Updating call worksheet.....\n")
        call_worksheet = SHEET.worksheet("call_data")
        call_worksheet.append_row(data)
        print("Call worksheet updated successfully!\n")

    def get_call_sheet(self):
        """
        function to allow the user to choose between,
        getting the most recent submission to the sheet,
        view the full spreadsheet if necessary or if they
        dont want any of these options to return home.
        """
        print("Enter '1' to view the most recent abandon rate submission.")
        print("Or")
        print("Enter '2' to view the full spreadsheet.\n")
        print("Enter '3' to return home.\n")

        selected_option = ""
        while selected_option not in [1, 2, 3]:
            try:
                selected_option = int(input("Choose your option:\n"))
                if selected_option == 1:
                    self.clear_terminal()
                    data = SHEET.worksheet("call_data").get_all_values()
                    last_row = data[-1]
                    for val, key in zip(self.dictionary, last_row):
                        print(val, "=", key)
                    input("Press enter to return to the start....")
                    if input:
                        self.abandon_rate_options()

                elif selected_option == 2:
                    self.clear_terminal()
                    print(
                        "Copy the link below into a new tab."
                        "This will display the full spreadsheet"
                        "with all data."
                    )
                    print(
                        "https://docs.google.com/spreadsheets/d/1IuRuySISMZsv3"
                        "4Ujaw6ERiFJoHikSjU6SIPbojHFTFI/edit?usp=sharing"
                    )
                    input("Press enter to return to the start....")
                    if input:
                        self.abandon_rate_options()
                elif selected_option == 3:
                    self.clear_terminal()
                    self.start_generator()
                else:
                    print(
                        "Oops, you have entered {input} that"
                        "is an invalid option".format(input=selected_option)
                    )
                    print("Please select option '1' or '2'")

            except ValueError:
                print(
                    "Sorry you have entered an invalid input,"
                    "please select from option '1' or '2'"
                )

    def get_date(self):
        """
        Function that gets the current date
        today, so we can keep track of the dates
        the user has inputted their information.
        """
        date = datetime.date.today()
        self.all_input_data.append(str(date))

    def clear_terminal(self):
        """
        Function that can be called in the class,
        it uses os and we are accessing the system
        method and passing the value clear, this in return
        will clearn the terminal throughout the application
        when necessary.
        """
        os.system("clear")
