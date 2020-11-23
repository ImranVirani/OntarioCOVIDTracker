import os
import requests
from bs4 import BeautifulSoup
from time import sleep
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

while True:
    page = requests.get('https://covid-19.ontario.ca/')
    soup = BeautifulSoup(page.text, 'html.parser')
    # Checks to see number of cases before update
    totalCases1 = soup.find(class_='ontario-infographic-number')
    totalCases1 = totalCases1.contents
    totalCases1 = totalCases1[0]
    totalCases1 = str(totalCases1)
    totalCases1 = totalCases1.strip()
    
    # Removes comma in the number and then coverts to an integer
    totalCases1= totalCases1.split(",")
    totalCases1 = totalCases1[0]+ totalCases1[1]
    totalCases1 = int(totalCases1)
    print(totalCases1)

    page = requests.get('https://covid-19.ontario.ca/')
    soup = BeautifulSoup(page.text, 'html.parser')
    # Checks to see number of cases before update
    totalCases2 = soup.find(class_='ontario-infographic-number')
    totalCases2 = totalCases1.contents
    totalCases2= totalCases2[0]
    totalCases2 = str(totalCases2)
    totalCases2 = totalCases2.strip()
    
    # Removes comma in the number and then coverts to an integer
    totalCases2 = totalCases2.split(",")
    totalCases2 = totalCases1[0]+ totalCases1[1]
    totalCases2 = int(totalCases1)
    print(totalCases2)
 
    if (totalCases1 == totalCases2):
        print("not update")
    else:
        newCases = totalCases2 - totalCases1
        print("updated!")
        # Updates current number of cases to be latest number of cases to be compared against the next days numbers
        totalCases1 = totalCases2
        html_messages = 'The number of new cases in Ontario is'+ ' ' + str(newCases)
        
        # If you would like to send to multiple people, pass in an array to_emails variable
        message = Mail(from_email=os.environ.get('TEST_SEND_EMAIL'),to_emails=os.environ.get('TEST_REC_EMAIL'), subject='Covid-19 Numbers have been updated',html_content=html_messages)
        
        # Sends email and checks for errors(boilerplate taken from Sengrid)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
    sleep(300)
