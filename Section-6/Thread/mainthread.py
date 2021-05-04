import threading

print("Current Thread:",threading.currentThread().getName())


if threading.currentThread() == threading.main_thread():
    print("Main Thread")

else:
    print("Some other Thread")