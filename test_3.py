from hw_webscraping import extract_table_rows
from bs4 import BeautifulSoup

def test_extract_table_rows():
    """Test that all table rows are correctly extracted."""
    filepath = './data/sample_page.html'
    
    # Get the result from student's function
    result = extract_table_rows(filepath)
    
    # Verify it's a list
    assert isinstance(result, list), "Function should return a list"
    
    # Check that we have the correct number of <tr> tags
    # Table 1: 4 rows (1 header + 3 data)
    # Table 2: 5 rows (1 header + 4 data)
    # Table 3: 6 rows (1 header + 5 data)
    # Total: 15 rows
    assert len(result) == 15, f"Expected 15 <tr> tags, but got {len(result)}"
    
    # Verify that each element is a BeautifulSoup Tag object
    for item in result:
        assert hasattr(item, 'name'), "Each item should be a BeautifulSoup Tag object"
        assert item.name == 'tr', f"Expected tag name 'tr', but got '{item.name}'"
    
    # Check that the first row contains the expected content
    first_row_text = result[0].get_text()
    assert 'Language' in first_row_text and 'Year Created' in first_row_text, \
        "First row should contain headers from Table 1"
    
    # Check a specific data row
    # The 5th row should be "JavaScript, 1995, Brendan Eich"
    fifth_row = result[3]  # Index 3 because of zero-based indexing
    cells = fifth_row.find_all(['td', 'th'])
    assert len(cells) >= 3, "Fifth row should have at least 3 cells"
    assert 'JavaScript' in cells[0].get_text(), "Fifth row should contain JavaScript"
    
    print("✓ All tests passed for extract_table_rows!")

if __name__ == "__main__":
    test_extract_table_rows()