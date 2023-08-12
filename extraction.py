import requests
from bs4 import BeautifulSoup
import pandas as pd

try:
    source = requests.get("https://www.pakwheels.com/used-cars/search/-/mk_honda/md_accord/")
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text,"html.parser")
    
    cars = soup.find('ul', class_="list-unstyled search-results search-results-mid next-prev car-search-results")
    #cars = soup.find('div',id ='main-container').find_all('ul', class_="list-unstyled")
    for car in cars:
        cars1 = cars.find_all('li', data-listing-id==7530019)
        print(len(cars1))
    """
    for car in cars:
        print(len(car))
    """
        
    
    
except Exception as e:
    print(e)
    

