import threading


#   daemon not necessary to call join()


def print_something(something):
    print(something)


t = threading.Thread(target=print_something, args=('hello',))
t.daemon = True
t.start()
print('thread started')
