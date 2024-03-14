#Import sections
import requests
import pandas #pandas is used for structing the data
from bs4 import BeautifulSoup #Beautifulsoup is used for scrappping the data 

response = requests.get("https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_4_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_4_0_na_na_na&as-pos=4&as-type=TRENDING&suggestionId=laptops&requestId=3659388c-3384-43ac-bfb7-e42a80a426b9&as-backfill=on")
#print(response)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)

names = soup.find_all('div', class_ = "_4rR01T") #we have to keep underscore(_)after class we can keep class r id if there, if not no need just we can keep tag names
name = []
for i in names[0:12]:
    d = i.get_text()
    name.append(d)

prices = soup.find_all('div', class_ = "_30jeq3 _1_WHN1")
price = []
for i in prices[0:12]:
    d = i.get_text()
    price.append(d)

ratings = soup.find_all('div', class_ = "_3LWZlK")
rate = []
for i in ratings[0:12]:
    d = i.get_text()
    rate.append(float(d))

reviews = soup.find_all('div', class_ = "gUuXy-")
review = []
for i in reviews[0:12]:
    d = i.get_text()
    review.append(d)

reviews = soup.find_all('div', class_ = "gUuXy-")
review = []
for i in reviews[0:12]:
    d = i.get_text()
    review.append(d)

features = soup.find_all('li', class_ = "rgWa7D")
feature = []
for i in features[0:12]:
    d = i.get_text()
    feature.append(d)

links = soup.find_all('a', class_ = "_1fQZEK")
link = []
for i in links[0:12]:
    d = "https://www.flipkart.com" + i['href']
    link.append(d)
#print(link) #scrabbing links

images = soup.find_all('img', class_ = "_396cs4")
image = []
for i in images[0:12]:
    d = i['src']
    image.append(d)

images = soup.find_all('img', class_ = "_396cs4")
image = []
for i in images[0:12]:
    d = i['src']
    #d = i.div.img['src'] #if there is one class for div, but not for others we have to use to this 
    image.append(d)

''' pandas '''

df = pandas.DataFrame() #pandas is a library used for dataanalyises ; data frame is a normally like a atable 
#print(df)
data = {'Names' : name, #if we got errors like index outdate error we have to write in "Names":name.pandas,Series(), (or) "Names":pandas.Series(names), 
      "Prices" : price,
      "Ratings" : rate,
      "Features" : feature,
      'Reviews' : review,
      "Images" : image,
      "Links" : link
      }
#print(data)

df = pandas.DataFrame(data) #put give us an output in table format
#print(df)

df.to_csv("Flipkart.csv") #to get the data in spreadsheet

