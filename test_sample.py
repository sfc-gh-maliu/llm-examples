from streamlit.testing.v1 import AppTest
import os 
import glob 
def test_smoke():
    python_files = glob.glob("*.py") + glob.glob("pages/*.py") 
    for file in python_files:
        if file == 'run_test.py':
            continue
        file_path  = os.path.abspath(file)
        at = AppTest.from_file(file_path, default_timeout = 100).run()
        assert not at.exception
