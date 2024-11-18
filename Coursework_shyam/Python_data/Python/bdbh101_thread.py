# SuperFastPython.com
# credit: https://superfastpython.com/threading-in-python/

# blocking IO provides an excellent use case for using threads in Python.
#
# Examples of blocking IO operations include:
#
# Reading or writing a file from the hard drive.
# Reading or writing to standard output, input or error (stdin, stdout, stderr).
# Printing a document.
# Reading or writing bytes on a socket connection with a server.
# Downloading or uploading a file.
# Querying a server.
# Querying a database.
# Taking a photo or recording a video.
# And so much more.
import numpy as np

def main():

    ### example of running a function with arguments in another thread
    from time import sleep
    from threading import Thread

    # a custom function that blocks for a moment
    def task(sleep_time, message):
        print('---NEW THREAD---: New thread started execution')
        # block for a moment
        sleep(sleep_time)
        # display a message
        print('---NEW THREAD---', message)


    # # create a thread
    # thread = Thread(target=task, args=(5, 'Thread completed its job'))
    # # thread.daemon = True
    # print("***MAIN THREAD***: Started a new thread")
    # # run the thread
    # thread.start()
    # print('***MAIN THREAD***: Main thread continues execution and computes the area of a square')
    # radius = 2
    # area = np.pi * radius**2
    # print("***MAIN THREAD***: Area of a circle", area)
    # print('***MAIN THREAD***: Waiting for new thread to complete before exiting program')
    #
    # # wait for the thread to finish
    # thread.join()
    #
    # print('All threads completed execution. Main thread is exiting!')


    # ### example of extending the Thread class
    # from time import sleep
    # from threading import Thread
    #
    # # custom thread class
    # class CustomThread(Thread):
    #     # override the run function
    #     def run(self):
    #         print('---NEW THREAD--- This is coming from another thread\n')
    #         # block for a moment
    #         sleep(5)
    #         # display a message
    #         print('---NEW THREAD--- Finished all activities in a thread')
    #
    # # create the thread
    # thread = CustomThread()
    # print('***MAIN THREAD***: Creating a new thread')
    # # start the thread
    # thread.start()
    # # wait for the thread to finish
    # print('***MAIN THREAD***: Waiting for the thread to finish')
    # thread.join()
    # print('***MAIN THREAD***: Program exiting!')


    # ### Example of Extending the Thread Class and Returning Values
    # # example of extending the Thread class and return values
    # from time import sleep
    # from threading import Thread
    #
    # # custom thread class
    # class CustomThread(Thread):
    #     # override the run function
    #     def run(self):
    #         # display a message
    #         print('---NEW THREAD--- Computing the area of a circle \n')
    #
    #         # block for a moment
    #         sleep(5)
    #
    #         radius = 5
    #         self.area = np.pi * radius**2
    #         # store return value
    #
    #
    # # create the thread
    # thread = CustomThread()
    # # start the thread
    # thread.start()
    # # wait for the thread to finish
    # print('***MAIN THREAD*** Waiting for the thread to finish')
    # thread.join()
    # # get the value returned from run
    # area_circle = thread.area
    # print(f'***MAIN THREAD*** Area of a circle computed in a thread: {area_circle}')

    # ### Thread Instance Attributes
    # # Query Thread Name
    # from threading import Thread
    # # create the thread
    # thread = Thread()
    # # report the thread name
    # print(thread.name)
    #
    # # Query Thread Daemon
    # # example of assessing whether a thread is a daemon
    # from threading import Thread
    # # create the thread
    # thread = Thread()
    # # report the daemon attribute
    # print(thread.daemon)
    # #
    # # Query Thread Identifier
    # # example of reporting the thread identifier
    # from threading import Thread
    # # create the thread
    # thread = Thread()
    # # report the thread identifier
    # print(thread.ident)
    # # start the thread
    # thread.start()
    # # report the thread identifier
    # print(thread.ident)
    #
    # # Query Thread Native Identifier
    # # example of reporting the native thread identifier
    # from threading import Thread
    # # create the thread
    # thread = Thread()
    # # report the native thread identifier
    # print(thread.native_id)
    # # start the thread
    # thread.start()
    # # report the native thread identifier
    # print(thread.native_id)
    #
    # # Query Thread Alive
    # # example of assessing whether a thread is alive
    # from threading import Thread
    # # create the thread
    # thread = Thread()
    # # report the thread is alive
    # print(thread.is_alive())
    #
    # from threading import Thread
    # from time import sleep
    # # create the thread
    # thread = Thread(target=lambda: sleep(1))
    # # report the thread is alive
    # print(thread.is_alive())
    # # start the thread
    # thread.start()
    # # report the thread is alive
    # print(thread.is_alive())
    # # wait for the thread to finish
    # thread.join()
    # # report the thread is alive
    # print(thread.is_alive())

    # ### configure thread attributes
    # # example of setting the thread name in the constructor
    # from threading import Thread
    # # create a thread with a custom name
    # thread = Thread(name='MyThread')
    # # report thread name
    # print(thread.name)
    #
    # # example of setting the thread name via the property
    # from threading import Thread
    # # create a thread
    # thread = Thread()
    # # set the name
    # thread.name = 'MyThread'
    # # report thread name
    # print(thread.name)
    #
    # # example of setting a thread to be a daemon via the constructor
    # from threading import Thread
    # # create a daemon thread
    # thread = Thread(daemon=True)
    # # report if the thread is a daemon
    # print(thread.daemon)
    #
    # # example of setting a thread to be a daemon via the property
    # from threading import Thread
    # # create a thread
    # thread = Thread()
    # # configure the thread to be a daemon
    # thread.daemon = True
    # # report if the thread is a daemon
    # print(thread.daemon)
    #
    # ### Main thread
    # # example of getting the current thread for the main thread
    # from threading import current_thread
    # # get the main thread
    # thread = current_thread()
    # # report properties for the main thread
    # print(f'name={thread.name}, daemon={thread.daemon}, id={thread.ident}')
    #
    # # example of getting the main thread
    # from threading import main_thread
    # # get the main thread
    # thread = main_thread()
    # # report properties for the main thread
    # print(f'name={thread.name}, daemon={thread.daemon}, id={thread.ident}')

    # ### Thread Utilities
    # # Number of Active Threads
    # # report the number of active threads
    # from threading import active_count
    # # get the number of active threads
    # count = active_count()
    # # report the number of active threads
    # print(count)
    #
    # # current thread
    # # retrieve the current thread within
    # from threading import Thread
    # from threading import current_thread
    #
    # # function to get the current thread
    # def task():
    #     # get the current thread
    #     thread = current_thread()
    #     # report the name
    #     print(thread.name)
    #
    # # create a thread
    # thread = Thread(target=task)
    # # start the thread
    # thread.start()
    # # wait for the thread to exit
    # thread.join()
    #
    # # current thread id
    # # report the id for the current thread
    # from threading import get_ident
    # # get the id for the current thread
    # identifier = get_ident()
    # # report the thread id
    # print(identifier)
    #
    # # enumerate active threads
    # # enumerate all active threads
    # import threading
    # # get a list of all active threads
    # threads = threading.enumerate()
    # # report the name of all active threads
    # for thread in threads:
    #     print(thread.name)

# credit: https://www.w3resource.com/python-exercises/threading/index.php
def thread_exercises():

    # ### Write a Python program to create multiple threads and print their names.
    # import threading
    # def print_thread_names():
    #     print("Current thread name:", threading.current_thread().name)
    #
    # # Create multiple threads
    # threads = []
    # for i in range(7):
    #     thread = threading.Thread(target=print_thread_names)
    #     threads.append(thread)
    #     thread.start()
    #
    # # Wait for all threads to complete
    # for thread in threads:
    #     thread.join()



    # ### Write a Python program to download multiple files concurrently using threads.
    # import threading
    # import urllib.request
    # def download_file(url, filename):
    #     print(f"\nDownloading {filename} from {url}...")
    #     urllib.request.urlretrieve(url, filename)
    #     print(f"\n{filename} downloaded successfully.")
    #
    # # Create a list of files to download
    # files_to_download = [
    #     {"url": "https://en.wikipedia.org/wiki/British_logistics_in_the_Normandy_campaign", "filename": "wfile1.html"},
    #     {"url": "https://en.wikipedia.org/wiki/Graph_(abstract_data_type)", "filename": "Graph_abstract_data_type.html"},
    #     {"url": "https://example.com/", "filename": "example.html"}
    # ]
    #
    # # Create a list to store the threads
    # threads = []
    #
    # # Create a thread for each file and start the download
    # for file_info in files_to_download:
    #     thread = threading.Thread(
    #         target=download_file,
    #         args=(file_info["url"], file_info["filename"])
    #     )
    #     thread.start()
    #     threads.append(thread)
    #
    # # Wait for all threads to complete
    # for thread in threads:
    #     thread.join()


    # do other operations here and they will be executed in parallel




    print('End')

# Construct to not include whole program in other includes
if __name__ == "__main__":
   # main()
   thread_exercises()