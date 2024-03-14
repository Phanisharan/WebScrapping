import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

response = rq.get('https://www.bikewale.com/hero-bikes/')
#print(response) - To know whether the website we are Extracting can give a Success response i.e, is <Response [200]>.


soup = BeautifulSoup(response.content,'html.parser')
#print(soup) - To Check whether all the content of the website in the html format is printing r not.

name = soup.find_all('h3', class_ = 'o-jjpuv o-cVMLxW o-mHabQ o-fzpibK')
names = []
for i in name[0:30]:
    d = i.get_text()
    names.append(d)


price = soup.find_all('span', class_ = 'o-eZTujG o-byFsZJ o-bkmzIL o-bVSleT')
prices = []                             
for i in price[0:30]:
    d = i.get_text()
    prices.append(d)


feature = soup.find_all('div', class_ = 'o-bqHweY o-bVSleT o-bwCunT o-bfyaNx o-bNxxEB o-fzpihx')
features = []
for i in feature[0:30]:
    d = i.get_text()
    features.append(d)


rating = soup.find_all('p', class_ = 'o-frVjwE o-bdcqVx o-cKuOoN o-lIIwF o-eZTujG')
ratings = []
for i in rating[0:30]:
    d = i.get_text()
    ratings.append(d)


review = soup.find_all('span', class_ = 'o-bzsJdq o-fzpimR o-KxopV o-sTQWx o-dThPjR')
reviews = []
for i in review[0:30]:
    d = i.get_text()
    reviews.append(d)


image = soup.find_all('img', class_='o-bXKmQE o-cgkaRG o-cQfblS o-bNxxEB o-pGqQl o-wBtSi o-bwUciP o-btTZkL o-bfyaNx o-eAZqQI')
images = []
for i in image[0:30]:
    d = i['src']
    images.append(d)


min_length = min(len(names), len(prices), len(features), len(ratings),len(reviews),len(images))
names = names[:min_length]
prices = prices[:min_length]
features = features[:min_length]
ratings = ratings[:min_length]
reviews = reviews[:min_length]
images = images[:min_length]


#Structuring the website contents by using pandas
data = {'Bike Names' : names,
        'Prices' : prices,
        'Features' : features,
        'ratings' : ratings,
        'reviews' : reviews,
        'images'  : images
        }
df = pd.DataFrame(data)
df.to_csv('Bikes.csv') 
