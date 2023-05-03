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


# Loop until data is successfully uploaded to the worksheet
while True:
    first_name, last_name, age, email, gender, country = get_personal_data()

    try:
        print(f"Uploading data to {worksheet.title}...\n")
        worksheet.append_row(
            [first_name, last_name, email, age, gender, country])
        print(f"Data sent successfully to {worksheet.title}\n")
        break
    except Exception as e:
        print(
            f"An error occurred while uploading data to {worksheet.title}: {str(e)}\n")
        print("Please fill out the form again.\n")

# display thank you message
print(f"Thank you {first_name}. You are now being redirected to our survey.\n")


def get_survey_responses():
    survey = {'quality': None, 'recommend': None,
              'expectations': None, 'frequency': None, 'price_value': None, 'features': None}
    questions = [{
        'name': 'quality',
        'question': "How satisfied are you with the product's quality? (Enter a number from 0 to 5) ",
        'validation': lambda x: x.isdigit() and 0 <= int(x) <= 5
    },  {
            'name': 'recommend',
            'question': "Would you recommend this product to others? (yes, maybe, no) ",
            'validation': lambda x: x in ['yes', 'maybe', 'no']
        },
    {
            'name': 'expectations',
            'question': "Did the product meet your expectations? (Enter a number from 0 to 5) ",
            'validation': lambda x: x.isdigit() and 0 <= int(x) <= 5
        },
    {
            'name': 'frequency',
            'question': "How often do you use the product? (daily, weekly, monthly) ",
            'validation': lambda x: x in ['daily', 'weekly', 'monthly']
        },
