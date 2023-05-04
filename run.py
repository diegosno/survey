# Import required libraries
import gspread
from google.oauth2.service_account import Credentials
import os
import time


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
welcome_message = "Welcome to our product's survey\n"
instructions = "Please enter your details\n"

# Print the welcome message to the console
print(welcome_message)
print(instructions)

# Define function to get personal data from the user


def get_personal_data():
    """
    Prompts the user to enter personal data. 
    Returns a dictionary containing first_name, last_name, age, email, gender, country.
    """
    # Loop until valid input is entered for each field
    # Get user's first name
    first_name = input('Enter your first name:\n')
    while True:
        if not first_name.isalpha():
            print('INVALID: Enter only letters')
            first_name = input()
        else:
            break
    first_name = first_name.capitalize()

# Get user's last name
    last_name = input('Enter your last name:\n')
    while True:
        if not last_name.isalpha():
            print('INVALID: Enter only letters')
            last_name = input()
        else:
            break
    last_name = last_name.capitalize()

# Get user's age
    age = input('Enter your age:\n')
    while True:
        if age.isdigit() and int(age) in range(18, 121):
            age = int(age)
            break
        else:
            print('INVALID: Enter an age between 18 and 120')
            age = input()

# Get user's email
    email = input('Enter your email:\n')
    while True:
        if "@" in email and "." in email and email.index("@") < email.index("."):
            break
        else:
            print('INVALID: Format should be example@example.com')
            email = input()

# Get user's gender
    gender = input('Enter your gender (woman/man/other):\n').lower()
    while True:
        if gender in ['woman', 'man', 'other']:
            break
        else:
            print('INVALID: Value should be woman, man, or other\n')
            gender = input().lower()

# Get user's country
    country = input('Enter your country:\n')
    while True:
        if country.isalpha():
            country = country.capitalize()
            break
        else:
            print('INVALID: Enter a valid country name\n')
            country = input()

# Return the user's personal data
    return first_name, last_name, age, email, gender, country


# Loop until personal data is successfully uploaded to the worksheet
while True:
    """
    Uploads personal data to a specified worksheet in Google Sheets.
    """
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
        print("Please fill out the form again. If error persists refresh.\n")


# Display thank you message
print(f"Thank you {first_name}. You are now being redirected to our survey.\n")

# Clear terminal screen after 3 seconds
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

# Survey message
print(f"Thank you {first_name}. Please complete the following survey:\n")


# Define function to get survey responses
def get_survey_responses():
    """
    Prompts the user to answer the survey questions. 
    Returns data stored in variables.
    """

   # Question 1
    quality = input(
        "How satisfied are you with the product's quality? (1-5)\n")

    while not quality.isdigit() or int(quality) not in range(1, 6):
        print("INVALID: Enter a valid number between 1 and 5.\n")
        quality = input()

    if quality == "5":
        print("We are glad to hear!\n")
    elif quality in ["3", "4"]:
        print("We will do better!\n")
    else:
        print("Sad to hear! Contact us so we find a solution.\n")

    # Question 2
    recommend = input("Would you recommend this product to others? (Yes/No)\n")

    while recommend.lower() not in ['yes', 'no']:
        print("INVALID: Answer must be Yes or No.\n")
        recommend = input()

    if recommend.lower() == 'yes':
        print("Awesome!")
    else:
        print("Sad to hear! Contact us so we find a solution.\n")

    # Question 3
    expectations = input("Did the product meet your expectations? (1-5)\n")
    while not (expectations.isdigit() and 1 <= int(expectations) <= 5):
        print("INVALID: Enter a valid number between 1 and 5.\n")
        expectations = input()
    if expectations == "5":
        print("We are glad to hear that!\n")
    elif expectations in ["3", "4"]:
        print("We will do better!\n")
    else:
        print("Sad to hear! Contact us so we find a solution.\n")

    # Question 4
    frequency = input(
        "How often do you use the product? (daily, weekly, monthly)\n")
    while not frequency.lower() in ['daily', 'weekly', 'monthly']:
        print("INVALID: Please enter either daily, weekly, or monthly.\n")
        frequency = input()

    # Question 5
    price_value = input(
        "How was the price compared to the product's value? (excellent, good, bad)\n")
    while not price_value.lower() in ['excellent', 'good', 'bad']:
        print("INVALID: Please enter either excellent, good, or bad.\n")
        price_value = input()

    if price_value.lower() in ['excellent', 'good']:
        print("We're glad to hear that!\n")
    else:
        print("Sad to hear! Contact us so we find a solution.\n")

    # Question 6
    features = input(
        "How important were missing features in your purchase decision? (very important, not very important, not important)\n")
    while not features.lower() in ['very important', 'not very important', 'not important']:
        print("INVALID: Please enter either very important, not very important, or not important.\n")
        features = input()

    return quality, recommend, expectations, frequency, price_value, features


# Loop until survey responses is successfully uploaded to the worksheet

while True:
    """
    Uploads survey responses to specified worksheet in Google Sheets.
    """
    quality, recommend, expectations, frequency, price_value, features = get_survey_responses()

    try:
        print(f"Uploading data to {worksheet2.title}...\n")
        worksheet2.append_row(
            [quality, recommend, expectations, frequency, price_value, features])
        print(f"Data sent successfully to {worksheet2.title}\n")
        break
    except Exception as e:
        print(
            f"An error occurred while uploading data to {worksheet2.title}: {str(e)}\n")
        print("Please fill out the form again. If error persists refresh.\n")


# Display goodbye message
print(f"Thank you {first_name}. We appreciate your feedback\n")
