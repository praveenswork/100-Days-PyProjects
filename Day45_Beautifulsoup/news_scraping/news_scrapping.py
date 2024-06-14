import requests
from bs4 import BeautifulSoup

news_url ="https://news.ycombinator.com/"
response = requests.get(news_url)
news_data = response.text

soup = BeautifulSoup(news_data, "html.parser")
news_articles = soup.find_all(name="tr",class_ = "athing")
news_score = soup.find_all("span", class_ = "score")
# print(news_articles)
article_list = []
for article in news_articles:
    article_text = article.find(name="span",class_ = "titleline")
    texts = article_text.get_text(strip=True)
    article_link = article.find(name="span",class_= "sitebit")
    links = article_link.find("a")["href"]
    article_list.append((texts,links))


points = []
# score = [point.get_text(strip=True) for point in news_score]
# points.append(score)
for subtext in news_score:
    score = subtext.get_text(strip=True) if subtext else "0 points"
    points.append(score)

final_data =[(article_list[i][0], article_list[i][1], points[i]) for i in range(len(article_list)-1)]

for text,link,point in final_data:
    print(f"texts = {text} \nlinks = '{link}'\nscores = {point} ")

