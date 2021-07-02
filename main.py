import time
import datetime
import yagmail
import pandas as pd
from news import NewsFeed


user = ''  # Enter Gmail account here.  For example, sushi@gmail.com
password = ''  # Enter password for the user above, here.


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today,
                         language='en')
    email = yagmail.SMTP(user=user, password=password)
    email.send(to=row['email'],
               subject=f"Check out what's happening in the news about {row['interest'].title()}.",
               contents=f"Hey {row['name'].title()},\n See whats new in {row['interest']}. \n \n {news_feed.get()}")


while True:  # Send  every 24 hours.
    if datetime.datetime.now().hour == 23 and datetime.datetime.now().minute == 59:
        df = pd.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)

