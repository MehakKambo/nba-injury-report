import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
from datetime import date
 
# Returns the current local date
today = date.today().strftime('%B %d, %Y')

# Your Twilio account SID and auth token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# The phone number you want to send the PDF to
to_number = 'phone number you wanna send to' 

#Fetch URL
url = "https://official.nba.com/nba-injury-report-2022-23-season/"

# Send a GET request to the URL and store the response
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")

pdf_link = soup.find("a", string="12:30 a.m ET report").get("href")

client = Client(account_sid, auth_token)

# Send the PDF file as an MMS message
message = client.messages.create(
    to=to_number,
    media_url=pdf_link,
    from_='your twilio phone number here',
    body=f"Here is your {today}\'s NBA injury report."
)

print(message.sid)