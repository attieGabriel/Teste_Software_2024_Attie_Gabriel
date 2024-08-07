import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.example import add

def test_add(input_data):
    a, b = input_data
    assert add(a, b) == 3
