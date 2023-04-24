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
#user_input_names = input()

#INSERT value checker (check that no numberes are present below)

#Convert input to list
#user_list = user_input_names.split(' ')
user_list = ['alex', 'nathan', 'joe', 'tom', 'bert', 'phil', 'chris']
user_length = len(user_list)

#Ask user for the lenght of list that they would like returned

#Global variable for user input


def length_input():

    """
    Ask user for length of list to return and checks input

    Args:
        None

    Returns:
        Lenght of user 
    """

    print('Input the length of list you would like returned')
    user_output_length = input()
    user_output_length = int(user_output_length)

    #Check the user input if it fits the criteria 
    #(positive integer and shorter not larger than the list length)

    if (user_output_length < 1):
        print('Incorrect input, try again')

        #Asking the user to input again
        length_input()
    else:
        print('Input accepted')

    return user_output_length


user_output_length = length_input()

#Generate the random numbers to select the names from

def list_remover(user_output_length):

    """
    Removes number of items 

    Args:
        Amount of names required for final list

    Returns:
        Outputs list name 
    """

    while len(user_list) > (user_output_length):

        #Assign a random number between 0 and list size
        temp = random.randint(0, (len(user_list) - 1))

        #Remove the index from list
        user_list.pop(temp)
    print(user_list)
    
list_remover(user_output_length)
