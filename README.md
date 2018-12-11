# SurfForecastScraper

A python based web scraper to grab the surf forecast from [Swellinfo](https://www.swellinfo.com).
The intention is to move this over to Amazon's Alexa inside of a skill. I would like 
to be able to ask Alexa [in my house] what the surf forecast for the area is, so that 
I can make a decision before I try to go surfing. 

This would be easy enough to just program my current location into the Alexa skill, and
query only the information from that page. I decided that I wanted to expand upon the 
specific use case, and I would like to create a generic Alexa skill to let me query
multiple surf locations for their forecast. 

> **Disclaimer** I do NOT pretend to be the creator of the surf forecasts. All rights of any surf forecast belong to [Swellinfo](https://www.swellinfo.com) and their team of forecasters.


## TO DO ##
- Currently grab the first level from the website. I need to get the next level down which should include the areas and subareas for forecasts. 
- Make the first function a little bit more generic for searching.

**NOTE: looks like this implementation will not go anywhere. I keep getting flagged as a bot for my requests and I cannot execute their javascript code. I need to move to selenium for python 3.x. **


## Software Versions ##
- Python version
- BeautifulSoup Version
