# [Web Scraping](https://realpython.com/python-web-scraping-practical-introduction/)

## Resources 
- [Web Scraping with Python in 4 minutes](https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460)
- [Web Scraping wiki](https://en.wikipedia.org/wiki/Web_scraping)
- [Video tutorial that tracks Amazon prices](https://www.youtube.com/watch?v=Bg9r_yLk7VY)

It sounds like I'll also need to create a blog on API integration in Python as well, which you can find [here](./api-integration.md)

Web scraping is the process of collecting and parsing raw data from the web using an automated process.
- Some websites forbid users from scraping their data with automated tools because,
  - the site has a good reason to protect its data. Google maps doesn't let you request too many results too quickly
  - making too many requests to a sites server may use up bandwidth, slowing down the site for other users and potentially overloading the server
- You should always check your target website's acceptable use policy to see if accessing the site with automated tools is a violation of its terms of use. 
## Legally it's a gray area to scrape without permission, click **[here](https://en.wikipedia.org/wiki/Web_scraping#Legal_issues)** for more details on where scraping could be deemed illegal

To me, web scraping sounds a lot like just making an API call, doesn't it? This article from [parsehub.com](https://www.parsehub.com/blog/web-scraping-vs-api/#:~:text=Web%20scraping%20allows%20you%20to,the%20data%20you'd%20want.&text=In%20these%20scenarios%2C%20web%20scraping,is%20available%20on%20a%20website.) was helpful to sort out the difference. I'll highlight some of my key takeaways below.

- The goal of web scraping and APIs is to access web data
- Web scraping is used via automated scraping software, APIs give you direct access to the data you'd want
  - you might be in a situation where there isn't an API to access data you want, or access to the API might be too limited or expensive
  - this is when you can use web scraping **as long as it is available on a particular website**
  - an example is Amazon, you could use a web scraper to extract product data as they don't provide an API for you to access the data

## Web Scraping in 4 minutes

Important notes on web scraping:
- Read through the website's terms and conditions to understand how you can legally use the data. Most sites prohibit you from using the dta for commercial purposes. 
- Make sure you are not downloading data at too rapid a rate because this may break the website. You may potentially be blocked from the site as well.

First thing to do is figure out where to locate links to the files we want to download. 
- Open dev tools
- Click the "Element on hover" arrow 
- Hover over what you want to extract and get the HTML element

### Inside your editor
Import the following libraries:
  - import requests
  - import urllib.request
  - import time
  - from bs4 import BeautifulSoup

Set the url to the website and access the site with `requests` library (the url below is the one used in the article)
```
url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
```

It looks like the author of this article is using Jupyter notebook, when she runs `response`, she gets output of `<Response [200]>`

Next, parse the html with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) that gives us a nested data structure. 

Call it within a variable
```
soup = BeautifulSoup(response.text, “html.parser”)
```

Use the method `.findAll` to locate `<a>` elements
```
soup.findAll('a')
```

`.findAll` will return every line of code that has an `<a>` tag from that url

Next, extract the actual link that you want using syntax like:
```
one_a_tag = soup.findAll(‘a’)[38]
link = one_a_tag[‘href’]
```

The full url may not be displayed in the output from the above code, try clicking on the link it provides to get the full url

You can use `urllib.request` library to download this file path to your computer by using `request.urlretrieve`. Give it two parameters; file url and filename. The author of this article used:
```
“turnstile_180922.txt”, 
“turnstile_180901”, etc.

download_url = 'http://web.mta.info/developers/'+ link
urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
```
Finally, use the `.sleep` method and pass in a number (in seconds) to set a timeout for our request so that we aren't flagged as a spammer.
```
time.sleep(1)
```
Download the rest of the data set files with a `for` loop.

Code used in '4 minute' article
```
# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
line_count = 1 #variable to track what line you are on
for one_a_tag in soup.findAll('a'):  #'a' tags are for links
    if line_count >= 36: #code for text files starts at line 36
        link = one_a_tag['href']
        download_url = 'http://web.mta.info/developers/'+ link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
        time.sleep(1) #pause the code for a sec
    #add 1 for next line
    line_count +=1
```
You can find the authors Jupyter Notebook for this [here](https://github.com/julia-git/webscraping_ny_mta)


[Table of Contents](../index.md)
