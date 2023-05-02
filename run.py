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
personaldata = SHEET.worksheet('Personal Data')
pdata = personaldata.get_all_values()
print(pdata)

# Define welcome page strings
welcome_message = "Welcome to our product's survey"
instructions = "To get started please enter your details"

# Print the welcome message to the console
print(welcome_message)
print(instructions)

# Prompt user for first name
while True:
    first_name = input("Please enter your first name: ")
    if first_name.isalpha():
        print(f"Hello, {first_name}!")
        # Write user input to Google Sheets spreadsheet
        personaldata.append_row(['', first_name])
        break
    else:
        print("Invalid input. Please enter only letters for your first name.")
