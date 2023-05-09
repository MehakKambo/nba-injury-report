# NBA Injury Report Scraper with Twilio SMS Notification

This Python project uses web scraping with BeautifulSoup (bs4) to fetch the latest NBA injury report PDF file from the official NBA website. The project also utilizes Twilio to send a text message notification to a specified phone number containing the injury report PDF file.

# Installation
To use this project, you will need to have Python 3 and the following Python packages installed:

- requests
- bs4 (BeautifulSoup)
- twilio
- datetime

You can install these packages by running the following command:

```bash
python3 -m pip install -r requirements.txt
```

# Usage
Before using this project, you will need to create a Twilio account and get a Twilio phone number. You will also need to set up your Twilio account credentials (account_sid and auth_token) and specify the recipient's phone number in the send_sms() function in main.py.

To run the project, simply execute the main.py script:

``` bash
python nba.py
```
This will fetch the latest NBA injury report PDF file using web scraping with bs4 and send a text message notification containing the URL of the injury report PDF file to the specified phone number using Twilio.

# Contributing
If you would like to contribute to this project, feel free to submit a pull request or open an issue. All contributions are welcome!
