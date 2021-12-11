if all(x.isalpha() or x.isspace() for x in input_value):
                num = input_value
                all_input_data.append(input_value)
                
                print("Thank you!.\n")
                get_job_title()
            else:
                print("Sor