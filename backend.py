import nltk
import aiohttp
import asyncio
import bs4
from random import shuffle
from nltk.corpus import words
import time
import sqlite3
connection = sqlite3.connect('ac8r2z.db')     #CHANGE HERE FOR DIFFERENT FILES
c=connection.cursor()

w = words.words()
word_list= []
for i in w:
    if i[0]=='c' or i[0]=='C':     #CHANGE HERE FOR DIFFERENT LETTERS
        if len(i)<2:
            pass
        else:
            if i[1] in "rstuvwxyz":    #CHANGE HERE FOR DEFFERENT LETTERS[1]
                word_list.append(i)
    elif i[0]=='a' or i[0]=='A':     #CHANGE HERE FOR DIFFERENT LETTERS
        if len(i)<2:
            pass
        else:
            if i[1] in "rstuvwxyz":    #CHANGE HERE FOR DEFFERENT LETTERS[1]
                word_list.append(i)
length = len(word_list)

print(f"WORD LIST CREATED OF {len(word_list)} WORDS")
time.sleep(1)
print("STARTING WEBSCRAPING NOW")

async def fetch(session, word):
    url = f'https://www.wordnik.com/words/{word.lower()}'
    async with session.get(url) as response:
        return word, await response.text()

async def fetch_all_words(words):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, word) for word in words]
        return await asyncio.gather(*tasks)

def parse_html(word, html):
    soup = bs4.BeautifulSoup(html, 'lxml')
    lis = soup.find_all('div', class_='guts active')
    if not lis:
        return word, "no meaning"

    total = lis[0].find_all('li')
    rang = len(total)
    
    if rang == 0:
        return word, "no meaning"
    elif rang > 3:
        definitions = [total[i].getText().split("   ") for i in range(3)]
    else:
        definitions = [total[i].getText().split("   ") for i in range(rang)]

    return word, definitions,

async def main():
    c.execute("""CREATE TABLE dictionary(
           word text,
           pos text,
           def text
    )""")
    connection.commit()
    trash=[]
    count=0
    for i in range(0,length,10):
        if i+10>length:
            words_to_fetch = word_list[i:length]
        else:
            words_to_fetch = word_list[i:10+i]
        htmls = await fetch_all_words(words_to_fetch)
        for word, html in htmls:
            word, definitions = parse_html(word, html)
            # print(word)
            if definitions == "no meaning":
                trash.append(word)
            else:
                for defi in definitions:
                    # print(defi)
                    if len(defi)==2:
                        item = (word, defi[0],defi[1])
                        c.execute("INSERT INTO dictionary VALUES (?,?,?)",item)
                        count+=1
                    elif len(defi)==1:
                        item = (word,'---',defi[0])
                        c.execute("INSERT INTO dictionary VALUES (?,?,?)",item)
                        count+=1
                    else:
                        trash.append(word)

        print(f"{i+10} words done")
        connection.commit()
    print("TASK COMPLETED!!!")
    print(f"WORDS TRASHED = {len(trash)}\nWORDS ADDED = {count}")
    connection.close()

if __name__ == "__main__":
    asyncio.run(main())
