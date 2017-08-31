import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
	print(name + " has started ...")
	tLock.acquire()
	print("Acquiring lock: " + str(name) + " ...")

	while repeat > 0:
		time.sleep(delay)
		print(name + ": " + str(time.ctime(time.time())))
		repeat -= 1
	
	print(name + " releasing lock ...")
	tLock.release()
	print(name + " completed ... ")

def Main():
	t1 = threading.Thread(target=timer, args=("1", 2, 5))
	t2 = threading.Thread(target=timer, args=("2", 1, 10))

	t1.start()
	t2.start()

	t1.join()
	t2.join()
	print("Main completed ...")

if __name__ == '__main__':
	Main()
