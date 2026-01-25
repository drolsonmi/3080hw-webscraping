from hw_webscraping import extract_all_links

def test_extract_all_links():
    """Test that all links are correctly extracted."""
    filepath = './data/sample_page.html'
    
    # Get the result from student's function
    result = extract_all_links(filepath)
    
    # Verify it's a list
    assert isinstance(result, list), "Function should return a list"
    
    # Check that we have the correct number of links (8 total in the HTML)
    assert len(result) == 8, f"Expected 8 links, but got {len(result)}"
    
    # Expected links in order
    expected_links = [
        'https://pandas.pydata.org/',
        'https://www.crummy.com/software/BeautifulSoup/',
        'https://www.python.org/',
        '/data/dataset1.csv',
        '/data/dataset2.csv',
        'https://github.com/',
        'https://stackoverflow.com/',
        'https://www.kaggle.com/'
    ]
    
    # Check that all expected links are present
    for expected_link in expected_links:
        assert expected_link in result, f"Expected to find link '{expected_link}' in results"
    
    # Verify the order is correct
    assert result == expected_links, f"Links are not in the expected order"
    
    print("✓ All tests passed for extract_all_links!")

if __name__ == "__main__":
    test_extract_all_links()