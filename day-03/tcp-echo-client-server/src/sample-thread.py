from threading import Thread, current_thread

def aThread():
    print "Thread"
    return

threads = []
for i in range(5):
    t = Thread(target=aThread)
    threads.append(t)
    t.start()