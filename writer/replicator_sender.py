
import queue
import threading
from time import sleep
from tracemalloc import start
from Receiver.Receiver import ReplicatorReceiver
from assets.helper import CODE, ReceiverProperty


class ReplicatorSender:
    def __init__(self):
        self.thread = threading.Thread(target=self.repl_sender_send)
        self.queue = []
        self.replicatorReceiver = ReplicatorReceiver
        start()

    def repl_sender_receive(self, code, value):
        # potrebna je struktura koja bi sacuvala vrednosti CODE i VALUE
        rp = ReceiverProperty(code, value)
        self.queue.append(rp)
        print(f"Primljeno od writera, KOD = {CODE(code)}, VREDNOST = {value}")
        print("Trenutno stanje QUEUE-a:")
        for rp in self.queue:
            print(f"Code[{CODE(rp.Code)}] = {rp.ReceiverValue}")

    def repl_sender_send(self):
        threading.Lock()
        while True:
            while len(self.queue) <= 0:
                self.thread.join()

            rp: ReceiverProperty = self.queue.pop()
            self.replicatorReceiver.Send(str(CODE(rp.Code)), rp.ReceiverValue)
            sleep(1000)
