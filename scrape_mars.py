# Load the dependencies
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import time


# Windows setup
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    full_mars_data={}
    url = "https://mars.nasa.gov/news/"
    time.sleep(15)
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    for x in range(1):
        html = browser.html
        soup = bs(html, 'html.parser')
        sitem_lists = soup.find("div", class_ ="list_text")
        sa_list2 = sitem_lists.find("a")
        news_title = sa_list2.text.strip()
        sb_list = sitem_lists.find("div", class_ ="article_teaser_body")
        news_p = sb_list.text.strip()
        
    # get the image
    url_jpl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    time.sleep(8)

    browser.visit(url_jpl)
    html = browser.html
    jpl_bs = bs(html, "html.parser")
    image_jpl = jpl_bs.find("a", {"id": "full_image", "data-fancybox-href": True}).get("data-fancybox-href")

    # take the image path (image_jpl) and add the begenning part to it.
    featured_image_url = ("https://www.jpl.nasa.gov" + image_jpl)

    url_tm = "https://twitter.com/marswxreport?lang=en"
    time.sleep(8)
    browser.visit(url_tm)
    html = browser.html
    twit_mars = bs(html, "html.parser")
    # find the first tweet and get all of its text that will ahve the weather
    twit_mars_full = twit_mars.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    # now we need to clean it up so that it is just the weather
    parsed = twit_mars_full.text.split("pic")
    mars_weather = parsed[0].strip()

    # Just the facts... mars facts
    url_mf = "https://space-facts.com/mars/"
    time.sleep(8)
    browser.visit(url_mf)

    # find the facts table about mars

    facts_mars_df = pd.read_html(url_mf)
    facts_mars_df1 = pd.DataFrame(facts_mars_df[0])

    facts_mars_df1.columns = ["FACT_TITLE","FACT"]
    facts_mars_df1_table = facts_mars_df1.set_index("FACT_TITLE")

    # facts_mars_df1_table.to_html("Mars_Facts.html")
    facts_mars_df1.to_html("Mars_Facts.html")

    ### get the 4 images ----------------------------------
    # get 1 of 4 images
    url_CHE = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    time.sleep(8)
    browser.visit(url_CHE)

    html = browser.html
    photos_CHE = bs(html, "html.parser")

    photos_CHE1 = photos_CHE.find("div", class_ ="downloads")

    photos_CHE2 = photos_CHE1.select("li")[1]
    photo_CHE = photos_CHE2.a["href"]

    # get 2 of 4 images
    url_SHE = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    time.sleep(8)
    browser.visit(url_SHE)

    html = browser.html
    photos_SHE = bs(html, "html.parser")

    photos_SHE1 = photos_SHE.find("div", class_ ="downloads")

    photos_SHE2 = photos_SHE1.select('li')[1]
    photo_SHE = photos_SHE2.a['href']

    # get 3 of 4 images
    url_SMHE = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    time.sleep(8)
    browser.visit(url_SMHE)

    html = browser.html
    photos_SMHE = bs(html, "html.parser")

    photos_SMHE1 = photos_SMHE.find("div", class_ ="downloads")

    photos_SMHE2 = photos_SMHE1.select('li')[1]
    photo_SMHE = photos_SMHE2.a['href']

    # get 4 of 4 images
    url_VMHE = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    time.sleep(8)
    browser.visit(url_VMHE)

    html = browser.html
    photos_VMHE = bs(html, "html.parser")

    photos_VMHE1 = photos_VMHE.find("div", class_ ="downloads")


    photos_VMHE2 = photos_VMHE1.select('li')[1]
    photo_VMHE = photos_VMHE2.a['href']


    # Make the python dictonary with the images

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": photo_CHE},
        {"title": "Cerberus Hemisphere", "img_url": photo_SHE},
        {"title": "Schiaparelli Hemisphere", "img_url": photo_SMHE},
        {"title": "Syrtis Major Hemisphere", "img_url": photo_VMHE},
    ]
    
    # return post
    # post = {"news_title": news_title}
    # posta = {"news_subline": news_p}
    # post2 = {"news_image": featured_image_url}
    # post3 = {"mars_weather": mars_weather}
    # post4 = {"mars_facts_table": Mars_Facts.html}
    # post5 = {"hemisphere_image_urls": hemisphere_image_urls}

    # load the full_mars_data dictionary with what we got
    full_mars_data["news_title"] = news_title
    full_mars_data["news_subline"] = news_p
    full_mars_data["news_image"] = featured_image_url
    full_mars_data["mars_weather"] = mars_weather
    # full_mars_data["mars_facts_table"] = Mars_Facts.html
    full_mars_data["photo_CHE"] = photo_CHE
    full_mars_data["photo_SHE"] = photo_SHE
    full_mars_data["photo_SMHE"] = photo_SMHE
    full_mars_data["photo_VMHE"] = photo_VMHE


    return full_mars_data

    browser.quit()
    return post

