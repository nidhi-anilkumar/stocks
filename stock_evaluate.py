import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'data'))
from data.download_data import download_data
download_data()
