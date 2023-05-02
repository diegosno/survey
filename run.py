# Import required libraries
import gspread
from google.oauth2.service_account import Credentials

# Define API access scopes
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load and authorize API credentials
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Access Google Sheets spreadsheet
SHEET = GSPREAD_CLIENT.open('Survey')


worksheet = SHEET.worksheet('Personal Data')
worksheet2 = SHEET.worksheet('Survey Responses')

# Define welcome page strings
welcome_message = "Welcome to our product's survey"
instructions = "Please enter your details"

# Print the welcome message to the console
print(welcome_message)
print(instructions)


def get_personal_data():

    while True:
        first_name = input('Enter your first name: ')
        if first_name.isalpha():
            break
        else:
            print('INVALID: Enter only letters')

    while True:
        last_name = input('Enter your last name: ')
        if last_name.isalpha():
            break
        else:
            print('INVALID: Enter only letters')

    while True:
        age = input('Enter your age: ')
        try:
            age = int(age)
            break
        except ValueError:
            print('INVALID: Enter a number')

    while True:
        email = input('Enter your email: ')
        if "@" in email and "." in email and email.index("@") < email.index("."):
            break
        else:
            print('INVALID: Format should be example@example')

    while True:
        gender = input('Enter your gender (m/f/o): ')
        if gender.isalpha():
            break
        else:
            print('INVALID: Value should be m, f, o')

    while True:
        country = input('Enter your country: ')
        if country.isalpha():
            break
        else:
            print('INVALID: Enter only letters')

    return first_name, last_name, age, email, gender, country


first_name, last_name, age, email, gender, country = get_personal_data()


worksheet.append_row([first_name, last_name, email, age, gender, country])


# display thank you message
print("Thank you, you are now being redirected to our survey page.")

quality = input("How satisfied are you with the product's quality?")
recommend = input("Would you recommend this product to others?")
expectations = input("Did the product meet your expectations?")
frequency = input("How often do you use the product?")
price_value = input("How was the price compared to the product's value?")
features = input(
    "How important were missing features in your purchase decision?")

ratings = (("1", "2", "3", "4", "5"),
           ("1", "2", "3", "4", "5"),
           ("1", "2", "3", "4", "5"),
           ("1", "2", "3", "4", "5"),
           ("1", "2", "3", "4", "5"),
           ("1", "2", "3", "4", "5"))

chosenanswers = []
questionnumber = 0


for question in questions:
    print(question)
    for rating in ratings[questionnumber]:
        print(rating)

    choose = input("Enter a value on a scale of 1 - 5")
    chosenanswers.append(choose)

    questionnumber += 1

worksheet2.append_row([])
