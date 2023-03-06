import io
import re

"""
	Student: Edgar Nunez
	Module: gladysUserLogin
	Description: This module requires an email in order to start to run the app.
    If the adress is an invalid one, the app doesn't start.

"""


def login():
    """Function which convert the input email in lower case / 
       If the email is correct, then it asks for the password / 

    Returns:
        userName
    """

    while True:

        emailAddress = input(
            "\nPlease enter an e-mail to inicialited the app: ")
        lowerEmail = emailAddress.lower()

        if (is_valid_email(lowerEmail) == True):
            password = input("Please enter your password: ")
            print("Inicialiting West's App...")
            break
        else:
            print("\nInvalid email adress, try again please.")
    return lowerEmail  # = userName


def is_valid_email(lowerEmail):
    """ Function to valid if a email is correct. Using regular expressios for get the possible ch in 
    the correct position, the function also works to validate if there is a "@" and a dot (.) // 

    Regular expressions (called REs, or regexes, or regex patterns) are essentially a tiny, highly 
    specialized programming language embedded inside Python and made available through the re module. 
    Using this little language, you specify the rules for the set of possible strings that you want to match;
    this set might contain English sentences, or e-mail addresses, or TeX commands, or anything you like. 


    Args:
        lowerEmail: _email input already passed to lower case_

    Returns:
        Boolean: - True is the email is valid
                 - False for incorrect email adress
    """

    regular_expresion = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    if re.match(regular_expresion, lowerEmail):
        return True
    return False
