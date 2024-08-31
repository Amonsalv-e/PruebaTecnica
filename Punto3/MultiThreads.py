import logging
import threading
from threading import Thread
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def even():
    for i in range(200):
        if i % 2 == 0:
            logging.info(f"Even : {i}")
            time.sleep(0.5)

def over():
    for i in range(200):
        if i % 2 != 0:
            logging.info(f"Over : {i}")
            time.sleep(0.5)

even_thread = Thread(target=even)
over_thread = Thread(target=over)

even_thread.start()
over_thread.start()

even_thread.join()
over_thread.join()

logging.info(f"Finish print numbers even and over")