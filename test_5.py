# Evaulate the performance of problem_1.py
import pytest
import pandas as pd
import hw_webscraping as hw

def test_docstrings():
    assert hw.extract_nth_table.__doc__ != None, "The extract_nth_table function is missing a docstring."
    assert hw.extract_all_links.__doc__ != None, "The extract_all_links function is missing a docstring."
    assert hw.extract_table_rows.__doc__ != None, "The extract_table_rows function is missing a docstring."
    assert hw.extract_nth_bold_text.__doc__ != None, "The extract_nth_bold_text function is missing a docstring."

if __name__ == "__main__":
    test_docstrings()