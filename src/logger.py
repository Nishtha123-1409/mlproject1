import logging
'''
logging.py is used to record what your program is doing while it runs.

Not errors only — everything important:

when the program starts

which step is running

what data shape came in

where it failed

why it failed

Think of it as the black box of an airplane 
'''
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y__%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] %(levelname)s %(lineno)d %(name)s - %(message)s',
    level=logging.INFO
)

