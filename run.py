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

# Define function to get personal data from the user


def get_personal_data():

    # Loop until valid input is entered for each field
    # Get user's first name
    while True:
        first_name = input('Enter your first name: ')
        if first_name.isalpha():
            break
        else:
            print('INVALID: Enter only letters')

# Get user's last name
    while True:
        last_name = input('Enter your last name: ')
        if last_name.isalpha():
            break
        else:
            print('INVALID: Enter only letters')

# Get user's age
    while True:
        age = input('Enter your age: ')
        try:
            age = int(age)
            break
        except ValueError:
            print('INVALID: Enter a number')

# Get user's email
    while True:
        email = input('Enter your email: ')
        if "@" in email and "." in email and email.index("@") < email.index("."):
            break
        else:
            print('INVALID: Format should be example@example.com')

# Get user's gender
    while True:
        gender = input('Enter your gender m(male)/f(female)/o(other)): ')
        if gender in ['m', 'f', 'o']:
            break
        else:
            print('INVALID: Value should be m, f, or o')

# Get user's country
    while True:
        country = input('Enter your country: ')
        if country.isalpha():
            break
        else:
            print('INVALID: Enter a valid country name')

# Return the user's personal data
    return first_name, last_name, age, email, gender, country


# Call function to get the user's personal data
# first_name, last_name, age, email, gender, country = get_personal_data()

# Append the user's data to the worksheet
# worksheet.append_row([first_name, last_name, email, age, gender, country])

# display thank you message
print("Thank you. You are now being redirected to our survey page.")


def get_survey_responses():
    quality = input(
        "How satisfied are you with the product's quality? (Enter a number from 0 to 5) ")
    try:
        quality = int(quality)
        if quality < 0 or quality > 5:
            print("Please enter a number from 0 to 5.")

            return get_survey_responses()
        else:
            return quality
    except ValueError:
        print("Please enter a number.")

    recommend = input(
        "Would you recommend this product to others? (Enter a number from 0 to 5) ")

    return get_survey_responses()


quality, recommend, expectations, frequency, price_value, features = get_survey_responses()
