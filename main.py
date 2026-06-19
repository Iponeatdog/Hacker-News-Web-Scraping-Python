from bs4 import BeautifulSoup
# import lxml
import requests

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())
# print(soup.a)

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText(), tag.get("href"))

# print(soup.find(name="h1", id="name").getText())
# print(soup.find(name="h3", class_="heading").getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)

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