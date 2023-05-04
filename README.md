# Survey

![Am I Responsive image](/images/Screenshot%202023-05-04%20at%2022.32.09.png)</details>
by: Diego Serrano
[View Live Project](https://survey-project.herokuapp.com/)

For the third project I decided to create a survey that allows the user to enter personal data, answer questions, and then have these questions sent to a data base in Google Sheets. I have always liked surveys as I find them to be an easy method to review things, or collect data that can be used in the future, I was curious on how to create a program that could accomplish this. The love sandwiches project also made me want to recreate something similar, and try myself to connect google sheets to my program.

# Project Goal

My goal is to create an app where a person can enter personal data, and answers to questions and then this data can be sent to a database.

## User Goal

Review a product.

## App Owner Goal

Get data about customers, as well as feedback about the product they are using.

# User Experience

## Target Audience

The survey is designed to be answered by anyone between the ages of 18-120.

## User Requirements and Expectations

The layout is organized and self explanatory, it includes a welcome message, it provides the user with feedback during usage, it includes two screens one for personal data, and another one containing the survey, in the end a thank you message is displayed.

## User Stories

- I want to receive a welcome message.
- I want to always be shown instructions that I can read an follow.
- I want to get feedback when I've done something wrong or right.
- I want to know if my data is sent correctly.
- I want to get a thank you message once I've finished the survey.

## Site Stories

- I want the app to be easy to follow.
- I want the instructions for the user to be clear.
- I want to make sure the user enters the right data.
- I want to give the user feedback to their answers.
- I want to collect the data the user enters.

# Technology Used

## Language Used

Python

## Python Libraries Used

- gspread
- os
- pprint

## Other websites used

- Github was used for deploying the repository.
- Visual Studio Code was used for writing the code.
- Heroku was used to deploy the program online.

## 3rd Party Python Libraries used

- Google Sheets API was used to store the user's data.
- Google OAUTH was used to connect my google account to the project.

# Features

## User Greeting

The program shows a welcome message at the start.

<details> <summary>View welcome message</summary>

![View welcome message](/images/welcome-message.png)

</details>

## Feedback

The program provides the user with feedback until they enter the right data

<details> <summary>View feedback </summary>

![View user feedback](/images/user-feedback.png)
![View user feedback](/images/user-feedback2.png)

</details>

## Thank You Message

Once the survey has been completed the user receives a thank you message.

<details> <summary>Thank you message </summary>

![View thank you message](/images/thankyou-message.png)

</details>

## Google Sheets

The data entered by the user is stored in Google Sheets which is a nice feature.

<details> <summary>View </summary>

![Personal Data Image](/images/survey.png)
![Survey Image](/images/personaldata.png)
![Google Sheets Image](/images/google-sheets.png)
![Google Sheets Image 2](/images/google-sheets2.png)

</details>

# Testing

The game was tested on both Chrome and Safari, and it ran fine. However it was not working on a mobile phone, I checked for info on Slack before asking, and I saw someone had asked this question before, to which fellow students responded that this project was not supposed to be tested on a mobile device.

## Validator Testing

No errors were found using the [PEP8 Validator](https://pep8ci.herokuapp.com/) only minor details that have to do with the environment I was working on.

<details> <summary>View </summary>

![View testing](/images/testing.png)

</details>

## Bugs

|                              Bug                               |                     Solution                      |
| :------------------------------------------------------------: | :-----------------------------------------------: |
| When a user entered wrong data, the question would show again. | Moved the input message outside of the while loop |
|          Both surveys were showing in the same page.           |            Import os to clear terminal            |

# Deployment

## Heroku

To deploy the website on Heroku the steps described on Code Institute's tutorial were followed these include:

- Create an account
- Add app and name
- Choose region
- Click create an app
- Click settings tab
- Click config var
- Store CREDS file in key and add values
- Store PORT key and value
- Add buildpacks
- Add Python buildpack so that it is on top
- Add Nodejs buildpack after
- Open deploy
- Choose GitHub deploy method, connect and login
- I chose manual deploy but there is also an option for automatic deploy from Github

# Credits

The [love-sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/02-accessing-user-data/03-validating-our-data-part-2) project was used to get a general idea on how to make my own project. I borrowed the ideas to import gspread, import credentials from google.auth.
These videos also helped me during my learning journey and helped me as a source of inspiration for my project.

[How to Validate User Inputs in Python | Input Validation in Python](https://www.youtube.com/watch?v=LUWyA3m_-r0)

[Build a Personality Survey Pt 2 - Python 3 6](https://www.youtube.com/watch?v=CfeULNd5-4Q)

[Create a QUIZ GAME with Python 💯](https://www.youtube.com/watch?v=zehwgTB0vV8)

[While loops in Python are easy ♾️](https://www.youtube.com/watch?v=rRTjPnVooxE&t=1s)

[Python Tutorial - Multiple Choice Quiz](https://www.youtube.com/watch?v=myJ36xIR7Yg)

# Acknowledgements

I want to thank my mentor Mo Shami for helping me and giving me advice, even though I was only able to have one meeting with him during this project due to health and time, he helped me as always.
I also want to thank the Student Care and Tutor Assistance teams who helped me a lot specially throughout this project as I encountered multiple challenges.
