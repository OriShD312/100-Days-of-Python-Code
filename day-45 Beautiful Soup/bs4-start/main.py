from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
ycomb_page = response.text

soup = BeautifulSoup(ycomb_page, "html.parser")
articles = soup.find_all(class_="titleline")
article_titles = []
article_links = []
for article in articles:
    text = article.text
    article_titles.append(text)
    link = article.a.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]
mvp = article_upvotes.index(max(article_upvotes))

print(article_titles[mvp])
print(article_links[mvp])
# print(article_upvotes[mvp])
