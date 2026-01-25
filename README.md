# Homework: Web Scraping

In this assignment, you will have the opportunity to practice with web scraping techniques using both Pandas and BeautifulSoup. In the file `hw_webscraping.py`, create 4 different functions to extract data from HTML pages. You will be asked to demonstrate that you can do the following:

* Extract tables from HTML using Pandas
* Parse HTML documents with BeautifulSoup
* Extract links from web pages
* Find and extract specific HTML elements and their text content

## Instructions

For this assignment, you will work with the sample HTML file provided in the `./data/` folder called `sample_page.html`. This file contains multiple tables, links, and formatted text that you will practice scraping.

In each function, you need to include a docstring. A docstring helps users to understand how a function works. Include a docstring using triple-quotation marks. Look back at the last homework assignments as a reminder of how to apply docstrings. 

### Function 1: `extract_nth_table(url)`

* Use `pd.read_html()` to read all tables from the given URL or file path
* Return the **n-th table** (index 2) as a pandas DataFrame
* **Input:** `url` - string, the path to the HTML file or URL
* **Output:** pandas DataFrame containing the third table

**Hints:**
- `pd.read_html()` returns a list of all tables found on the page
- Remember that Python uses zero-based indexing
- You are not allowed to modify the HTML file

### Function 2: `extract_all_links(filepath)`

* Use BeautifulSoup to parse the HTML file
* Find all anchor tags (`<a>`)
* Extract the `href` attribute from each link
* Return a list of all URLs/hrefs found
* **Input:** `filepath` - string, the path to the HTML file
* **Output:** list of strings, where each string is an href value

**Hints:**
- Use `soup.find_all('a')` to find all anchor tags
- Use the `.get('href')` method or `['href']` to access the href attribute
- Make sure to open and read the file with the appropriate encoding

### Function 3: `extract_table_rows(filepath)`

* Use BeautifulSoup to parse the HTML file
* Find all table row tags (`<tr>`)
* Return the list of all `<tr>` tag objects
* **Input:** `filepath` - string, the path to the HTML file
* **Output:** list of BeautifulSoup Tag objects

**Hints:**
- Use `soup.find_all('tr')` to find all table row tags
- Return the actual tag objects, not just the text content

### Function 4: `extract_nth_bold_text(filepath, n)`

* Use BeautifulSoup to parse the HTML file
* Find all bold tags (`<b>`)
* Extract the text content from the **n-th** `<b>` tag (index 4)
* Return the text as a string, with leading/trailing whitespace removed
* **Input:** `filepath` - string, the path to the HTML file
* **Output:** string, the text content of the n-th bold tag

**Hints:**
- Use `soup.find_all('b')` to find all bold tags
- Use `.text` or `.get_text()` to extract text content
- Use `.strip()` to remove extra whitespace
- Remember zero-based indexing: the n-th element is at index 4

## Testing Your Code

You can test your functions by running the test files:

```bash
python test_1.py
python test_2.py
python test_3.py
python test_4.py
```

All tests should pass when your functions are implemented correctly.

## Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Function 1 | 4 | Correctly extracts the third table using pd.read_html() |
| Function 2 | 4 | Correctly extracts all links using BeautifulSoup |
| Function 3 | 4 | Correctly finds and returns all `<tr>` tags |
| Function 4 | 4 | Correctly extracts text from the fifth `<b>` tag |
| Docstrings | 4 | Each function has a complete and accurate docstring |

**Total: 20 points**

## Submission

Commit and push your completed `hw_webscraping.py` file to your GitHub repository. The autograder will run automatically when you push your code.

## Resources

- [Pandas read_html documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html)
- [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Python requests library](https://requests.readthedocs.io/)

-----

This assignment was built with the assistance of AI