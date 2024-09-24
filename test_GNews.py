
from gnews import GNews
import requests
from bs4 import BeautifulSoup


url = 'https://news.google.com/rss/articles/CBMiK2h0dHBzOi8vemRuZXQuY28ua3Ivdmlldy8_bm89MjAyMzA0MTYxMTA1NDnSAQA?oc=5'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'

}

# cookies = {'CONSENT': 'YES+cb.20220419-08-p0.cs+FX+111'}
cookies = {'CONSENT': 'YES+US.en+202101'}

r = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.wrap)
print(soup.a['href'])


def get_real_url(google_news_url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    cookies = {'CONSENT': 'YES+cb.20220419-08-p0.cs+FX+111'}
    # Send a GET request to the Google News URL
    response = requests.get(google_news_url, headers=headers, cookies=cookies)

    # Get the final redirected URL
    real_url = BeautifulSoup(response.text, 'html.parser')

    return real_url


# Example Google News URL
google_news_url = 'https://news.google.com/read/CBMivgFBVV95cUxNSG1HTDVCRXAzajJTQkV4TW9jb3cyc0dhSzRfc19tRUV6OGYzdWg1UzJGRk1iTHBJS3pFMGowdXNMcXhyaWVTTUxrWjEyVzF0WjhIRm1iYjBaa3paYkN0US1lNnJlY2pTbWgyY3BBSlFGX18wNS1rSmVjcWtvOVc5SXhfYTlaM3NSSjJNSm1UUjRDeFQybWpJOXktUkxfMVBKMnZ0ZkZJZVFzNVhXLTlFR1ZmVUdMSmZycVktX3Rn?hl=en-US&gl=US&ceid=US%3Aen'

# Get the real URL
# real_url = get_real_url(google_news_url)
# print(f'Real URL: {real_url}')

# Initialize the GNews object
# google_news = GNews(language='en', country='US')

# # Fetch the news articles related to a topic
# news = google_news.get_news('DIPG')
# print(len(news))
# print(news)

# # Check if we got the articles
# if news:

#     # Display the title, link, and thumbnail for each article
#     for article in news[:3]:
#         print(f"Title: {article['title']}")
#         print(f"Link: {article['url']}")
#         print(f"Thumbnail: {article['img']}")
#         print("\n")
# else:
#     print("No articles found.")
