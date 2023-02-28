import io

"""
	Student: Gabriel Solomon
	Module: gladysUserLogin
	Description: This module does …
"""


def login():
    """
            document your function definition here. what does it do?
    """

    """
		delete the remaining code *in this function* and replace it with
		your own code. add more code to do what the assignment asks of you.
	"""
    arroba = '@'
    space = " "
    emailAddress = input("Please enter an e-mail to inicialited the app: ")
    lowerEmail = emailAddress.lower()

    if arroba not in lowerEmail or space in lowerEmail:
        print("E-mail adress no valid, please try again")
    else:
        return lowerEmail
        print(lowerEmail)
