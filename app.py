import json
import threading
from os.path import getsize
from threading import Thread

import webscrapper as ws


def write_to_file(inform):
    with open('data.json', 'a') as outfile:
        for item in inform:
            outfile.write(json.dumps(item, indent=4))


def th1(x):
    info = ws.main_app(x)
    lock.acquire()
    write_to_file(info)
    print("t1 done")
    lock.release()


def th2(x):
    info = ws.main_app(x)
    lock.acquire()
    write_to_file(info)
    print("t2 done")
    lock.release()

def th3(x):
    info = ws.main_app(x)
    lock.acquire()
    write_to_file(info)
    print("t3 done")
    lock.release()

def th4(x):
    info = ws.main_app(x)
    lock.acquire()
    write_to_file(info)
    print("t4 done")
    lock.release()

def th5(x):
    info = ws.main_app(x)
    lock.acquire()
    write_to_file(info)
    print("t5 done")
    lock.release()

def th6(x):
    info = ws.main_app(x)
    lock.acquire()
    write_to_file(info)
    print("t6 done")
    lock.release()

def th7(x):
    info = ws.main_app(x)
    lock.acquire()
    write_to_file(info)
    print("t7 done")
    lock.release()

def th8(x):
    info = ws.main_app(x)
    lock.acquire()
    write_to_file(info)
    print("t8 done")
    lock.release()


if __name__ == '__main__':
    i = 1
    n_threads = 8
    lock = threading.Lock()
    while True:
        t1 = Thread(target=th1, args=(i,))
        t2 = Thread(target=th2, args=(i + 1,))
        t3 = Thread(target=th3, args=(i + 2,))
        t4 = Thread(target=th4, args=(i + 3,))
        t5 = Thread(target=th5, args=(i + 4,))
        t6 = Thread(target=th6, args=(i + 5,))
        t7 = Thread(target=th7, args=(i + 6,))
        t8 = Thread(target=th8, args=(i + 7,))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        size = getsize('data.json')
        print("velikost souboru je " + str((size * 0.000001)) + " MB")
        print(i)
        if size > 1000100100:
            break
        i += n_threads
