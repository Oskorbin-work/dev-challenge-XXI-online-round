""" This code executes:
    a) tests
"""
# Import project Modules
from views import client
from settings import ENDPOINT

# ------------------------------------------------
def test_get_sheets_check_key_sheets():
    """
    test_get_sheets_check_key_sheets checks key Sheets in Sheets exist
    """
    print("\n" + test_get_sheets_check_key_sheets.__name__)
    res = client.get(ENDPOINT)
    assert res.get_json().get('Sheets') is not None, "Key \"Sheets\" isn't exist"
    print("Status OK –    checks key Sheets in Sheets exist")