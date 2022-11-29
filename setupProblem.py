from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
import os

for num in range(1,100):
    url = "http://www.projecteuler.net/problem="+str(num)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script","style"]):
        script.extract()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())

    chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
    text = ' '.join (chunk for chunk in chunks if chunk)

    Problem = re.findall(".*%(.*) Project Euler:",text)
    if len(Problem)>1:
        print("FAIL")
        print(text)
        exit()
    print(Problem[0])
    print("\n\n")
    numstring = str(num) if num >= 10 else "0"+str(num)
    print(numstring)
    if not os.path.exists("Problem"+numstring):
        os.system("mkdir Problem"+numstring)
        print("created folder")
    if not os.path.exists("Problem"+numstring+"/angabe.txt"):
        os.system("touch Problem"+numstring+"/angabe.txt")
        with open("Problem"+numstring+"/angabe.txt","w") as f:
            f.write(Problem[0])

