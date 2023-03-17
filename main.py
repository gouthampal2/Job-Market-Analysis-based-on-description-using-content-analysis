import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas as pd

skill = input('Enter your Skill: ').strip()
place = input('Enter the location: ').strip()
no_of_pages = int(input('Enter the # of pages to scrape: '))

indeed_posts=[]


for page in range(no_of_pages):
    
    # Connecting to India Indeed
        url = 'https://uk.indeed.com/jobs?q=' + skill + \
            '&l=' + place + '&sort=date' +'&start='+ str(page * 10)
        
        # Get request to indeed with headers above (you don't need headers!)
        response = requests.get(url)
        html = response.text

        # Scrapping the Web (you can use 'html' or 'lxml')
        soup = BeautifulSoup(html, 'lxml')

        # Outer Most Entry Point of HTML:
        outer_most_point=soup.find('div',attrs={'id': 'mosaic-jobcards'})
        
 