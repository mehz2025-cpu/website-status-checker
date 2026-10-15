#Website Status Checker
import requests
import threading
import queue

urls = []
threads = []
results = queue.Queue()

def start_checks():
    try:
        number_of_sites = int(input("How many websites do you want to check? "))
        if number_of_sites <= 0:
            print("Amount must be greater than 0!")
            return
    except ValueError:
        print("Enter a number!")
        return

    for i in range(number_of_sites):
        url = input(f"Please enter URL {i + 1}: ")
        if url.startswith("https://") or url.startswith("http://"):
            pass
        else:
            url = ("https://" + url)
        urls.append(url)
        t = threading.Thread(target=checker, args=(url,)) 
        threads.append(t)
        t.start()

def checker(url):
    try:
        response = requests.get(url, timeout=5)
        if 200 <= response.status_code < 300:
            results.put((url, "UP", response.status_code))
        else:
            results.put((url, "DOWN", response.status_code))

    except requests.RequestException as error:
        results.put((url, "ERROR", error))

def show_results():
    up = 0
    down = 0
    errors = 0
    for i in range(len(urls)):
        url, status, code = results.get()
        if status == "UP":
            print(f"{url} -> UP ({code})")
            up+=1
        elif status == "DOWN":
            print(f"{url} -> DOWN ({code})")
            down+=1
        else:
            print(f"{url} -> ERROR ({code})")
            errors+=1

    print("="*20)
    print(f"Total websites: {len(urls)}")
    print(f"Online: {up}")
    print(f"Offline: {down}")
    print(f"Errors: {errors}")
    print("="*20)

start_checks()

for thread in threads:
    thread.join()

show_results()