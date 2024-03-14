# My Web Scraping Project

This project utilizes Python with BeautifulSoup and Pandas to scrape data from the Multiple websites.

## Description

I have implemented a web scraping script using Python's BeautifulSoup library to extract data from the different websites.
The scraped data includes [describe the data you scraped, e.g., names, models, prices, specifications, images, links]. 
The extracted data is then processed and analyzed using Pandas for further insights.

## Requirements

- Python 3.x
- BeautifulSoup
- Pandas

## Usage

To use the web scraping script:

1. Import the necessary libraries:
   ```python
   import pandas as pd
   import requests as rq
   from bs4 import BeautifulSoup
   ```
### Choose a Website you want to scrape here is the Website that i used for Scrapping

![Screenshot 2024-03-14 183824](https://github.com/Phanisharan/WebScrapping/assets/143081814/3993f4d1-c094-4871-9f49-a15295c1cbd4)

2. Send a GET request to the BikeWale website:
   ```python
   response = rq.get('https://www.bikewale.com/hero-bikes/')
   ```
### Make Sure to Print the response for the Site you are using for Scrapping if you get <Response 200> then you can Extract the contents in the site if not go for the another site 

3. Parse the HTML content of the response:
   ```python
   soup = BeautifulSoup(response.content, 'html.parser')
   ```

4. Extract bike information using BeautifulSoup:

   - Bike names:
     ```python
     name = soup.find_all('h3', class_='o-jjpuv o-cVMLxW o-mHabQ o-fzpibK')
     ```

   - Bike prices:
     ```python
     price = soup.find_all('span', class_='o-eZTujG o-byFsZJ o-bkmzIL o-bVSleT')
     ```

   - Bike features:
     ```python
     feature = soup.find_all('div', class_='o-bqHweY o-bVSleT o-bwCunT o-bfyaNx o-bNxxEB o-fzpihx')
     ```

   - Bike ratings:
     ```python
     rating = soup.find_all('p', class_='o-frVjwE o-bdcqVx o-cKuOoN o-lIIwF o-eZTujG')
     ```

   - Bike reviews:
     ```python
     review = soup.find_all('span', class_='o-bzsJdq o-fzpimR o-KxopV o-sTQWx o-dThPjR')
     ```

   - Bike images (example photo of the website):
     ```python
     image = soup.find_all('img', class_='o-bXKmQE o-cgkaRG o-cQfblS o-bNxxEB o-pGqQl o-wBtSi o-bwUciP o-btTZkL o-bfyaNx o-eAZqQI')
     ```

5. Structuring the extracted data into a DataFrame using pandas:
   ```python
   data = {'Bike Names': names,
           'Prices': prices,
           'Features': features,
           'Ratings': ratings,
           'Reviews': reviews,
           'Images': images}
   df = pd.DataFrame(data)
   ```

6. Exporting the DataFrame to a CSV file:
   ```python
   df.to_csv('Bikes.csv')
   ```
### Here is the Final output how you get the information in a website with a Structed format in using pandas 

![Screenshot 2024-03-14 184352](https://github.com/Phanisharan/WebScrapping/assets/143081814/e9a4a6c1-ce5d-47fd-865f-8de9feace80c)


### Note:
    - Make sure to replace the URL in the `rq.get()` function with the appropriate one for the specific Website you want to scrape.
    - Extract the website only those Who gives the response as 200

Feel free to explore the extracted data and analyze it further using the structured DataFrame.

### Here are the Few sites you can use : Flipkart, Bikewale, ibmd, ebay, walmart etc.




