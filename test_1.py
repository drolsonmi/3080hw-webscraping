import pandas as pd
from hw_webscraping import extract_nth_table

def test_extract_nth_table():
    """Test that the third table is correctly extracted."""
    filepath = './data/sample_page.html'
    
    # Get the result from student's function
    result = extract_nth_table(filepath, 3)
    
    # Verify it's a DataFrame
    assert isinstance(result, pd.DataFrame), "Function should return a pandas DataFrame"
    
    # Check the shape of the DataFrame (should be 5 rows x 5 columns for Student Grades table)
    assert result.shape == (5, 5), f"Expected shape (5, 5), but got {result.shape}"
    
    # Check that the correct columns are present
    expected_columns = ['Student ID', 'Name', 'Assignment 1', 'Assignment 2', 'Final Grade']
    assert list(result.columns) == expected_columns, f"Expected columns {expected_columns}, but got {list(result.columns)}"
    
    # Check some specific values
    assert result.iloc[0, 0] == 1 or result.iloc[0, 0] == '001', "First student ID should be 001"
    assert result.iloc[0, 1] == 'Alice Johnson', "First student name should be Alice Johnson"
    assert result.iloc[1, 4] == 'B+', "Second student's final grade should be B+"
    
    print(f"✓ All tests passed for extracting table 3!")

if __name__ == "__main__":
    test_extract_nth_table()