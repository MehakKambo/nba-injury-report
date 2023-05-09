import requests
from bs4 import BeautifulSoup


url = "https://official.nba.com/nba-injury-report-2022-23-season/"

# Send a GET request to the URL and store the response
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")
pdf_link = soup.find("a", string="12:30 a.m ET report").get("href")
file_name = "NbaInjuryReport.pdf"
pdf_response = requests.get(pdf_link)
with open(file_name, "wb") as f:
    f.write(pdf_response.content)
    print("Your file", file_name, "has been downloaded.")