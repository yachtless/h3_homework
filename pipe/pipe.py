from multiprocessing import Process, Pipe
from time import sleep
from os import getpid


def ponger(receiver, sender, response):
    # we should 'ping' second process to initiate ping-pong exchange
    if response == 'ping':
        sender.send(f"{response}")

    while True:
        if receiver.poll(2):
            print(f"Process {getpid()} got message: {receiver.recv()}")
            sleep(2)
            sender.send(f"{response}")


if __name__ == "__main__":
    in_conn_1, out_conn_1 = Pipe()
    in_conn_2, out_conn_2 = Pipe()

    process_1 = Process(target=ponger, args=(in_conn_1, out_conn_2, 'ping')).start()
    process_2 = Process(target=ponger, args=(in_conn_2, out_conn_1, 'pong')).start()



