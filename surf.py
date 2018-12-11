#!/usr/bin/env python

import urllib2
import html2text
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup
import re

'''
Get the source information for the url and place the information into
a BeautifulSoup object
@param url_name - string representation of the url
@return - BeautifulSoup object containing the source for the url
'''
def get_url_source(url_name):
    # open the url and read the source as text
    open_url = urllib2.urlopen(url_name)

    # send the read in information to be parsed for relative paths
    soup = BeautifulSoup(open_url.read())

    return soup

'''
@param url_name - string representation of the url
@param soup - BeautifulSoup Object
@return - list of relative path names converted to no longer be relative
by adding the name of the url_page they came from.
'''
def find_relative_paths(url_name, soup):
    relative_paths = []

    for url in soup.findAll('a'):
        path = urljoin(url_name, url.get('href'))

        # only keep the paths that are actually a part of this website
        if path.startswith(url_name) :
            relative_paths.append(urljoin(url_name, url.get('href')))

    return relative_paths

def find_url_source_info(url_name, soup, find_all, search_criteria):
    info = []

    for url in soup.findAll(find_all):
        path = url.get(search_criteria)

        #print path

        # remove empty strings and null strings
        if path is not None and path:
            info.append( path )

    return info

'''
@param relative_paths - list of relative paths from our original source page
@return - if exists the path to the forecasts page, otherwise return an empty string
'''
def find_forecast_url(relative_paths):
    forecasts = []
    # grab the forecasts path
    for url in relative_paths:
        if "forecast" in url and url not in forecasts:
            forecasts.append(url)

    forecast_url = ""
    if len(forecasts) >= 1:
        forecast_url = forecasts[0]

    return forecast_url

'''
@param url_name - string representation of the url
@param surf_loc - location that we wish to append to the url 
@return - url_name/surf_loc
'''
def add_surf_location(url_name, surf_loc):

    url_ends = url_name.ends_with('/')
    loc_starts = surf_loc.starts_with('/')

    if url_ends and loc_starts:
        return url_name[:-1] + surf_loc
    elif (url_ends and not loc_starts) or (not url_ends and loc_starts):
        return url_name + surf_loc
    else:
        return url_name + "/" + surf_loc

'''
Main Point of execution. Read the url and grab all information. We should slowly work
our way down to the forecasts for each individual location.
'''
def main():
    # starting url 
    surf_url = 'https://www.swellinfo.com'

    # get the web page source for swellinfo
    soup = get_url_source(surf_url)
    # find the forecast relative path url
    relative_paths = find_relative_paths(surf_url, soup)
    forecast_url = find_forecast_url(relative_paths)

    for i in relative_paths:
        print i

    # could not find the forecast page, so let's exit
    if not forecast_url:
        sys.exit()

    '''
    This will work to get the sub regions but there isn't a way to select it using
    beautiful soup. May need to be able to select a list item.
    '''

    '''
    # get all of the possible form values !!!
    data_region_forms = find_url_source_info(forecast_url, soup, 'li', 'data-region')

    # [abbreviated name fo the region, long/display name of the region]
    region_name_map = []

    # the data-regions are between tags of <li> ... </li>
    for url in soup.findAll('li'):

        # convert the result to a string for comparison of contains
        region = str(url)

        # for each data-region id, get try to get the long name for display or
        # for voice text comparison
        for data_region in data_region_forms:

            # is the id inside of this text?
            if data_region in region:

                # id was found, next get the <span> tags as that is where the long
                # and short name representations reside
                for t in url.findAll('span'):

                    # if this text contains the long-name string, get the name of the data
                    long_name = str(t)

                    if 'long-name' in long_name:
                        region_name_map.append([data_region, t.text])
    '''

if __name__ == "__main__":
    main()
