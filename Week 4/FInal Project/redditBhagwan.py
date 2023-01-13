import requests
from bs4 import BeautifulSoup
import csv

class Reddit:
    def __init__(self, url):
        self.url = url
        self.subreddit = ""
        self.title = ""
        self.upvotes =""
        self.comments =""      
        self.content =""
        self.media  = ""
    
    def scrape(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        page = requests.get(self.url,headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        Name = soup.find('span', class_='_2wzi-W7JiZ7A6U6aFvfvSR')#for name
        self.subreddit = Name.text if Name else None 
        
        Title= soup.find('h1', class_='_eYtD2XCVieq6emjKBH3m')#for title
        self.title = Title.text if Title else None 
        
        upvotes = soup.find('div', class_='_23h0-EcaBUorIHC-JZyh6J')#for upvotes
        self.upvotes = int(upvotes.text) if upvotes else None
         
        comments = soup.find('span', class_='FHCV02u6Cp2zYL0fhQPsO')#for comments
        self.comments = comments.text if comments else None 
        
        content = soup.find('div', class_='_3AStxql1mQsrZuUIFP9xSg s1y8gf4b-0 gXUyBJ')#for content
        self.content = content.text  if content else None 
            
        urlmedia = soup.find('img', class_='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax')#for photo
        self.media = urlmedia.get('src') if urlmedia else None

    def to_csv(self, filename):
     with open(filename, 'a') as file:
            file.write("Name:"+f"{self.subreddit}\n")
            file.write("Title:"+f"{self.title}\n")
            file.write("Upvotes:"+f"{self.upvotes}\n")
            file.write("Comments:"+f"{self.comments}\n")
            file.write("Picture:"+f"{self.media}\n")

link = Reddit('https://www.reddit.com/r/Nepal/comments/u73zol/beautiful_tea_garden_as_seen_in_illam/')
link.scrape() #scraping data
link.to_csv('redditgahana.csv')