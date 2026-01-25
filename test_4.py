from hw_webscraping import extract_nth_bold_text

def test_extract_nth_bold_text():
    """Test that the text from the fifth <b> tag is correctly extracted."""
    filepath = './data/sample_page.html'
    
    # Get the result from student's function
    result = extract_nth_bold_text(filepath, 5)
    
    # Verify it's a string
    assert isinstance(result, str), "Function should return a string"
    
    # The fifth <b> tag should contain "programming"
    # Order of <b> tags in HTML:
    # 1. "Web Scraping"
    # 2. "multiple tables"
    # 3. "various HTML elements"
    # 4. "statistics"
    # 5. "programming"
    # 6. "domain expertise"
    # 7. "January 2026"
    
    expected_text = "programming"
    assert result == expected_text, f"Expected '{expected_text}', but got '{result}'"
    
    # Verify that whitespace has been stripped
    assert result == result.strip(), "Text should have leading/trailing whitespace removed"
    
    # Verify the result is not empty
    assert len(result) > 0, "Result should not be an empty string"
    
    print("✓ All tests passed for extract_nth_bold_text!")

if __name__ == "__main__":
    test_extract_nth_bold_text()