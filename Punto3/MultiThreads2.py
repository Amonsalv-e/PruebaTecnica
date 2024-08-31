import logging
from queue import PriorityQueue, Queue
import json
import os
import time
from threading import Thread
from pathlib import Path


logging.basicConfig(level=logging.INFO)

_logger = logging.getLogger(__name__)

global queue
queue = Queue()

folder = Path("/home/alejandro/Documentos/Prueba/Test_python/prueba_python")
file_name = "sample-03-00-json.json"
file_path_json = folder / file_name

with open(file_path_json, 'r') as file:
    data = json.load(file)

    def normalize_data(data_list):
        all_numbers = [int(num) for sublist in data_list for num in sublist.split()]
        max_value = max(all_numbers)
        normalized = [num / max_value for num in all_numbers]
        return normalized, sum(all_numbers) / len(all_numbers), sum(normalized) / len(normalized), len(all_numbers)

    def some_computation(counter, record):
        try:
            print("Started thread :{}".format(counter))
            time.sleep(2)

            if isinstance(record, dict) and "id" in record:
                normalized_data, original_avg, normalized_avg, data_size = normalize_data(record["data"])
                record["normalized_data"] = normalized_data
                record["original_avg"] = original_avg
                record["normalized_avg"] = normalized_avg
                record["data_size"] = data_size
                queue.put(record)
            else:
                print(f"Record {counter} does not have the expected format: {record}")
        except Exception as e:
            print(f"An error ocurred in thread {counter}: {e}")

    if __name__ == "__main__":
        threads = []
        max_threads = 4
        for key, value in data.items():
            if len(threads) >= max_threads:
                logging.info(f"A slot will open up in the thread")
                threads[0].join()
                threads.pop(0)

            t = Thread(target=some_computation, args=(key,value))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        while not queue.empty():
            record = queue.get()
            print(record)
