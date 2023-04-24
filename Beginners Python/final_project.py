import random

"""
Aim of code to generate a list of names from a given 
list of names. The length of list should be asked for
and then returned
"""

"""
Control flow:
Ask user for input of the names
    Check for legit input (no numbers etc)
Ask user for lenght of list they wish to be returned
    Check input is positive intger, else re-ask
Randomly select x amount of names and output the list
"""

#Asks user for their shortlist of names
print('Please input your shortlist of names, make sure to separate the names by a single space.')
user_input_names = input()

#INSERT value checker (check that no numberes are present below)

#Convert input to list
user_list = user_input_names.split(' ')

#Ask user for the lenght of list that they would like returned


def length_input():

    """
    Ask user for length of list to return and checks input

    Args:
        None

    Returns:
        If the input was accepted  
    """

    print('Input the length of list you would like returned')
    user_output_length = input()

    #Check the user input if it fits the criteria 
    #(positive integer and shorter not larger than the list length)

    if (user_output_length < 1) or (user_output_length != int) or (user_output_length >= len(user_list)):
        print('Incorrect input, try again')

        #Asking the user to input again
        length_input()
    else:
        print('Input accepted')


length_input()
