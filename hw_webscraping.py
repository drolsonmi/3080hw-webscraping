import pandas as pd
from bs4 import BeautifulSoup


def extract_third_table(url):
    """
    Extract the third table from an HTML page using pandas.
    
    Input: url - string, path to HTML file or URL
    Output: pandas DataFrame containing the third table
    """
    # Your code here
    pass


def extract_all_links(filepath):
    """
    Extract all hyperlinks (href attributes) from an HTML file using BeautifulSoup.
    
    Input: filepath - string, path to the HTML file
    Output: list of strings, each string is an href value
    """
    # Your code here
    pass


def extract_table_rows(filepath):
    """
    Find and return all table row (<tr>) tags from an HTML file using BeautifulSoup.
    
    Input: filepath - string, path to the HTML file
    Output: list of BeautifulSoup Tag objects representing <tr> tags
    """
    # Your code here
    pass


def extract_fifth_bold_text(filepath):
    """
    Extract the text content from the fifth <b> tag in an HTML file.
    
    Input: filepath - string, path to the HTML file
    Output: string, the text content of the fifth bold tag (whitespace stripped)
    """
    # Your code here
    pass

## Any code below this line will not be evaluated ##
