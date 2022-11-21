from urllib.request import urlopen
from bs4 import BeautifulSoup

num = 10
url = "http://www.projecteuler.net/problem="+str(num)
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

for script in soup(["script","style"]):
    script.extract()

text = soup.get_text()

lines = (line.strip() for line in text.splitlines())

chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
text = ' '.join (chunk for chunk in chunks if chunk)
print(type(text))

printing = False
sol = ""
for char in text:
    if printing:
        sol+=char
    if char == "%":
        printing = True
    if char == "|":
        printing = False
print(sol)
