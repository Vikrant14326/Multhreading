import threading

def write_data():
    con.acquire()
    with open('report.txt', 'w') as file1:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for day in days:
            temp = input(f"Enter the temperature for {day}: ")
            file1.write(temp.strip() + "\n")
    con.notify_all()  # Notify all waiting threads
    con.release()

def max_temp():
    con.acquire()
    con.wait()  # Wait until data is written
    with open('report.txt', 'r') as file1:
        lines = file1.readlines()
        temps = [float(line.strip()) for line in lines]
        max_val = max(temps)
        print(f"Maximum temperature is: {max_val:.2f}")
    con.release()

def avg_temp():
    con.acquire()
    con.wait()  # Wait until data is written
    with open('report.txt', 'r') as file1:
        lines = file1.readlines()
        temps = [float(line.strip()) for line in lines]
        avg_val = sum(temps) / len(temps)
        print(f"Average temperature for week: {avg_val:.2f}")
    con.release()

# Condition variable
con = threading.Condition()

# Threads
t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)

# Start threads (readers first)
t2.start()
t3.start()
t1.start()

