import requests


class NewsFeed:
    """
    A class used to request news of a certain type in a range of dates, it then builds an e-mail body consisting of the
    requested information

    """

    base_url = "https://newsapi.org/v2/everything?"
    api_key = ""  # Sign up and add your API key here

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''

        for article in articles:  # Add text here if you want to modify the email body
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"apiKey={self.api_key}"
        return url


if __name__ == '__main__':
    news_feed = NewsFeed(interest='candy', from_date='2021-06-26', to_date='2021-06-27', language='en')  # I <3 Candy
    print(news_feed.get())
