import threading
from time import sleep
from ReplicatorReceiver.Receiver import ReplicatorReceiver
from assets.helper import CODE, ReceiverProperty


class ReplicatorSender:
    def __init__(self):
        self.thread = threading.Thread(target=self.repl_sender_send)
        self.e = threading.Event()
        self.queue = []
        self.replicatorReceiver = ReplicatorReceiver()
        self.thread.start()

    def repl_sender_receive(self, code, value):
        # potrebna je struktura koja bi sacuvala vrednosti CODE i VALUE
        rp = ReceiverProperty(code, value)
        self.queue.append(rp)
        self.e.set()


    def repl_sender_send(self):
        threading.Lock()
        while True:
            while len(self.queue) <= 0:
                self.e.wait()

            rp: ReceiverProperty = self.queue.pop()
            self.replicatorReceiver.Send(CODE(rp.Code), rp.ReceiverValue)
            sleep(1)
