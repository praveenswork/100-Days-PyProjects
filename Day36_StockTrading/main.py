import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()

TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
MY_NUMBER = os.getenv("MY_NUMBER")
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_KEY = os.getenv("TWILIO_AUTH_KEY")

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_ENDPOINT , params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list =[ value for (key,value) in data.items()]
yesterday_data  = data_list[0]
yesterday_closing_price =yesterday_data["4. close"]


day_before_yesterday_data  = data_list[1]
day_before_yesterday_closing_price =day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
up_down =None

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#percentage
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

## STEP 2:Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if diff_percent > 1:
    news_params = {
        "apikey" : NEWS_API_KEY,
        "qInTitle" :COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT,news_params)
    news_response.raise_for_status,
    news_data = news_response.json()['articles']
    three_articles  = news_data[:3]
    # print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down} {diff_percent}%  \n Headline: {article['description']} \n Brief: {article['content']}" for article in three_articles]
    # print(formatted_articles)

    client = Client(TWILIO_SID,TWILIO_AUTH_KEY)
## STEP 3: Send a seperate message with the percentage change and each article's title and description to your phone number. 
    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_ = TWILIO_NUMBER,
            to = MY_NUMBER
        )
    print(message.status)
