import os
import sys


import numpy as np
import pandas as pd
import dill


from src.exception import CustomException
from src.logger import logging

def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        logging.info(f"Creating directory at: {dir_path}")
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            logging.info(f"Saving object to: {file_path}")
            dill.dump(obj, file_obj)
            
    except Exception as e:
        logging.error(f"Error saving object: {e}")
        raise CustomException(e, sys)