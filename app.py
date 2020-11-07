import sys
import sqlite3
connection = sqlite3.connect("mailingList.db")
cursor = connection.cursor()
command1 = """CREATE TABLE IF NOT EXISTS
emails(email_id INTEGER PRIMARY KEY, email TEXT)"""

cursor.execute(command1) 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from time import sleep
chrome_options = Options()
import os
from time import sleep
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")

# chrome_options.headless = True # also works
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://covid-19.ontario.ca/")
while True:
    # Checks to see number of cases before update
    totalCases1 = driver.find_element_by_class_name("ontario-infographic-number")
    
    totalCases1 = totalCases1.text
    # Removes comma in the number and then coverts to an integer
    totalCases1= totalCases1.split(",")
    totalCases1 = totalCases1[0]+ totalCases1[1]
    totalCases1 = int(totalCases1)
    # Refreshes page to check for new numbers
    driver.refresh()
    # Finds amount of new cases(if there are any)
    totalCases2 = driver.find_element_by_class_name("ontario-infographic-number")
    totalCases2 = totalCases2.text
    # Removes comma and covert to an integer so that the new and old cases can be subtracted to find the number of new cases that have been added
    totalCases2= totalCases2.split(",")
    totalCases2 = totalCases2[0]+ totalCases2[1]
    totalCases2 = int(totalCases2)
    # Finds date and time to compare against
    if (totalCases1 == totalCases2):
        print("not update")
    else:
        newCases = totalCases2 - totalCases1
        # Uncomment the 3 lines commented out below to enable desktop notifications for mac.
        '''if (sys.platform == "darwin"):
            updateNotification = f"osascript -e 'display notification \"There are {newCases} new cases\" with title \"Covid-19 Numbers Have been Updated\"'"
            os.system(updateNotification)
            '''
        print("updated!")
        totalCases1 = totalCases2
        html_messages = '<strong>The number of new cases in Ontario is'+ ' ' + str(newCases) + ' ' + '</strong>'
        # Attempting to figure out a way to send to a list of people using a sqlite database.
        message = Mail(from_email=os.environ.get('TEST_SEND_EMAIL'),to_emails=os.environ.get('TEST_REC_EMAIL'), subject='Covid-19 Numbers have been updated',html_content=html_messages)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)

    sleep(300)
driver.quit()
