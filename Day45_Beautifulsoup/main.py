from bs4 import BeautifulSoup

with open("website.html",encoding="utf-8") as html_file:
    content = html_file.read()

soup = BeautifulSoup(content, "html.parser")

print(soup)

