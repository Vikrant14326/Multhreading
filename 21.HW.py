# File Handling Simulation (Dummy Code)
import threading
from time import sleep

e = threading.Event()
lock = threading.Lock()
chunk_count = 0  # Shared counter

def read_file():
    global chunk_count
    for i in range(5):  # Simulate 5 chunks (25 pages)
        with lock:
            chunk_count += 1
            print(f"Reading pages {(chunk_count - 1) * 5 + 1} to {chunk_count * 5} from file...")
            e.set()  # Signal write_file to proceed
        sleep(2)
        e.clear()  # Block writing until next read

def write_file():
    written_count = 0
    while written_count < 5:
        e.wait()  # Wait for read signal
        with lock:
            if written_count < chunk_count:
                written_count += 1
                print(f"Writing pages {(written_count - 1) * 5 + 1} to {written_count * 5} to file...")
                sleep(1)

t1 = threading.Thread(target=read_file)
t2 = threading.Thread(target=write_file)

t1.start()
t2.start()
