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
welcome_message = "Welcome to our product's survey\n"
instructions = "Please enter your details\n"

# Print the welcome message to the console
print(welcome_message)
print(instructions)

# Define function to get personal data from the user


def get_personal_data():

    # Loop until valid input is entered for each field
    # Get user's first name
    while True:
        first_name = input('Enter your first name:\n')
        if first_name.isalpha():
            break
        else:
            print('INVALID: Enter only letters\n')

# Get user's last name
    while True:
        last_name = input('Enter your last name:\n')
        if last_name.isalpha():
            break
        else:
            print('INVALID: Enter only letters\n')

# Get user's age
    while True:
        age = input('Enter your age:\n')
        try:
            age = int(age)
            break
        except ValueError:
            print('INVALID: Enter a number\n')

# Get user's email
    while True:
        email = input('Enter your email:\n')
        if "@" in email and "." in email and email.index("@") < email.index("."):
            break
        else:
            print('INVALID: Format should be example@example.com\n')

# Get user's gender
    while True:
        gender = input('Enter your gender m(male)/f(female)/o(other)):\n')
        if gender in ['m', 'f', 'o']:
            break
        else:
            print('INVALID: Value should be m, f, or o\n')

# Get user's country
    while True:
        country = input('Enter your country:\n')
        if country.isalpha():
            break
        else:
            print('INVALID: Enter a valid country name\n')

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
        print("Please fill out the form again. If error persists refresh.\n")


# Display thank you message
print(f"Thank you {first_name}. You are now being redirected to our survey.\n")


def get_survey_results():

   # Question 1
    while True:
        quality = input(
            "How satisfied are you with the product's quality? (1-5)\n")
        if quality.isdigit() and 1 <= int(quality) <= 5:
            if quality == "5":
                print("We are glad to hear!\n")
            elif quality in ["3", "4"]:
                print("We will do better!\n")
            else:
                print("Sad to hear! Contact us so we find a solution.\n")
            break
        else:
            print("INVALID: Enter a valid number\n")

    # Question 2
    while True:
        recommend = input(
            "Would you recommend this product to others? (Yes/No)\n")
        if recommend.lower() == 'yes':
            print("Awesome!")
            break
        elif recommend.lower() == 'no':
            print("Sad to hear! Contact us so we find a solution.\n")
            break
        else:
            print("INVALID: Answer must be Yes or No\n")

    # Question 3
    while True:
        expectations = input("Did the product meet your expectations? (1-5)\n")
        if expectations.isdigit() and 1 <= int(expectations) <= 5:
            if expectations == "5":
                print("We are glad to hear!\n")
            elif recommend in ["3", "4"]:
                print("We will do better!\n")
            else:
                print("Sad to hear! Contact us so we find a solution.\n")
            break
        else:
            print("INVALID: Enter a valid number\n")

    # Question 4
    while True:
        frequency = input(
            "How often do you use the product? (daily, weekly, monthly)\n")
        if frequency.lower() in ['daily', 'weekly', 'monthly']:
            break
        else:
            print("INVALID: Please enter either daily, weekly, or monthly.")


get_survey_results()
