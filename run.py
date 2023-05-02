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
