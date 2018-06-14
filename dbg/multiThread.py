
import time
import threading
import ptvsd
print(ptvsd.__version__)
def one():
    while True:
        print("Do in one")
        time.sleep(1)

def two():
    while True:
        print("Do in two")
        time.sleep(1)

def three():
    while True:
        print("Do in 3")
        time.sleep(1)

workers = []
worker = threading.Thread(target=one)
worker.start()
workers.append(worker)

worker = threading.Thread(target=two)
worker.start()
workers.append(worker)

worker = threading.Thread(target=three)
worker.start()
workers.append(worker)

worker.join()
