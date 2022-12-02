"""

Several options

Concurrency with Futures 

Concurrency with asyncio

Thread and lock

ThreadPool

https://leetcode.com/problems/web-crawler-multithreaded/discuss/790522/Short-and-Simple-Python
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
# from concurrent.asyncio import 

from multiprocessing.pool import ThreadPool

# threading keys: CPU-bound on CPython interpretor run 1 thread at once - due to GIL; use multiprocessing module instead
# I/O bound apps can take advantage of multi-threading



# 1.1. Concurrency with Futures: as_completed (limited by GIL so not really making downloads in parallel BUT PYTHON I/O bound benefit from multi threads!
def download_many(cc_list):


	with ThreadPoolExecutor(max_workers=4) as executor:
		to_do = []
		for cc in sorted(cc_list):
			future = executor.submit(download_one_callable, cc)
			to_do.append(future)

	results = []
	for future in as_completed(to_do):
		res = future.result()
		results.append(res)

	return len(results)

	# 1.2. Concurrency with Futures: ThreadPoolExecutor.map (like in the mfactcheck)
	# but as_completed is more flexible than map: can use different callables; can even combine ProcessPoolExecutor and ThreadPoolExecutor

	# Python 3 : threading replace initial threads module
	# lower level: thread, lock, semaphore; -> higher level futures.ThreadPoolExecutor


	# 2. Concurency with asyncio


	# #33####################### Going back to the basics. threading module

import threading
import logging
import time

def thread_function(name):
	logging.info(f"Thread start {name}")
	time.sleep(2)
	logging.info(f"Thread {name} finishing.")


def main():
	
	format = "%(asctime)s:%(message)s"
	logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

	logging.info("Main: before creating thread")
	# do list
	threads = []

	for i in range(3):
		logging.info(f"Main: before createe and running thread {i}.")
		x = threading.Thread(target=thread_function, args = (i,))
		threads.append(x)
		x.start()
		# logging.info("Main: wait for the thread to finish.")
	# x.join() # this finishes thread frist this returns and thread finishes
	# tell one thread to wait while another finishes
	# daemon threads finish at the exit of the program

	for i, thread in enumerate(threads):
		logging.info(f"before join thread {i}")
		thread.join()
		logging.info(f"after join thread {i}") # order donee by the OS hard to predict

		# must join the threads
		# use the ThreadPoolExecutor context manager to do this for you.
		# ThreadPoolExecutor with map can be hard to debug, 

		# Race conditions: when two threads acceess the same resource

		# Solution: lock

		# mutex (mutuall excludion) called in other languages;
		# 
		# Deadlock: must release lock before acquire again
		# to help with That: context managers and RLock in Python



		# Producer - Consumer: prod get message to add to pipeline; consumer take mess from pipeline

		# Can use Quueue form ultiple evetns
		# cans use therading.Event
		# queue.Queue (give it a size) - has locks implemented

		# threading.Condition; wait(); notify()
		

	logging.info("Main: all done.") # as part of the _shutdown of the python p



if __name__ == '__main__':
	main()
