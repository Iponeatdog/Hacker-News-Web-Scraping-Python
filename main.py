from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []
articles= []
for item in soup.find_all("span", class_="titleline"):
    link = item.find("a")
    articles.append(link)
# print("Articles", articles)
for tag in articles:
    article_text = tag.getText()
    article_texts.append(article_text)
    article_link = tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_upvote_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_upvote_index])
print(article_links[max_upvote_index])
print(article_upvotes[max_upvote_index])
