from bs4 import BeautifulSoup

with open("website.html",encoding="utf-8") as html_file:
    content = html_file.read()

soup = BeautifulSoup(content, "html.parser")

selector = soup.find_all("p")
print(selector)

selector_css = soup.select_one(selector="#name")
print(selector_css)





