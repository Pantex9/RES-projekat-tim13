from Reciever.Receiver import Send, ReplicatorReceiver
from assets.helper import ReceiverProperty, CODE
from multiprocessing.connection import wait
import queue
import threading
from time import sleep
from tracemalloc import start


class ReplicatorSender:
    def __init__(self):
        self.thread = None
        self.queue = []
        self.replicatorReceiver = ReplicatorReceiver()
        threading.Thread = start()

    def repl_sender_receive(self, code, value):
        # potrebna je struktura koja bi sacuvala vrednosti CODE i VALUE
        rp = ReceiverProperty(code, value)
        self.queue.append(rp)
        print(f"Primljeno od writera, KOD = {CODE(code)}, VREDNOST = {value}")
        print("Trenutno stanje QUEUE-a:")
        for rp in self.queue:
            print(f"Code[{CODE(rp.code)}] = {rp.value}")

    def repl_sender_send(self):
        receiverProp = queue[ReceiverProperty]
        mutex = threading.Lock()
        while (True):
            while (receiverProp <= 0):
                self = wait()

            rp = receiverProp
            self.queue.pop(rp)
            self.replicatorReceiver = Send(CODE(rp.code), rp.value)
            threading.Thread = sleep(1000)
