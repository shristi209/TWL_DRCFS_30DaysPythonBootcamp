#Final Project of Reddit Scraping is here

Lets go with the following steps:
#Step 1: 
import requests, bs4 and csv.
These lines of code are using the Python requests library to send HTTP requests to a web page, the BeautifulSoup library to parse the HTML of the web page, and the csv library to read and write CSV files.

#Step 2:
Python class named Reddit that is used to scrape data from a given subreddit page, specifically the subreddit name, title, number of upvotes, number of comments, content and media from a page and write it to a csv file. 

#Step 3:
The scrape method within the Reddit class is used to scrape data from a subreddit page and store it in the class's attributes. This steps involves sending an HTTP GET request to the subreddit page specified by the self.url attribute, along with headers variable. Also, BeautifulSoup is used to parse the Html content of the page and create a soup object. find() is used to search for the first HTML element that matches the specified class, and assigns it to the variable. In each case, it then checks whether the variable is None or not using an if statement. If the variable is not None, it means the element with the specified class was found on the page, so it uses the appropriate attribute of the variable to get the text of the element or the attribute of the element and assigns it to the corresponding class attribute like self.subreddit, self.title, self.upvotes, self.comments, self.content, and self.media.

#Step 4:
This code defines the to_csv method within the Reddit class which is used to write the scraped data to a CSV file with the given filename.

#step 5:
This code creates an instance of the Reddit class and assigns it to the variable link. It pass the url 'https://www.reddit.com/r/Nepal/comments/u73zol/beautiful_tea_garden_as_seen_in_illam/' as an argument to the class's constructor method, which is then stored in the self.url attribute of the class instance.
It then calls the scrape method on the link object, which is used to access the data from the subreddit page and store it in the class's attributes.
Finally, it calls the to_csv method on the link object, passing the string 'redditgahana.csv' as an argument. This tells the method to write the scraped data to a file named 'redditgahana.csv' in the current working directory.
This code will scrape the data from the specified subreddit page and write it to a file named 'redditgahana.csv' in the current working directory. However, since the method 'to_csv' is not written to write the data in a csv format, it will not be easily processable by spreadsheet software.
