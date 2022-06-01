import random
from replicator_sender import ReplicatorSender


class Writer:

    def __init__(self, sender: ReplicatorSender):
        self.code = None
        self.value = None
        self.replicatorSender = sender

    def writer_send_data(self):
        self.code = random.randint(0, 7)
        self.value = random.randrange(100, 1000, 3)  # Returns any random integer of specific length 3
        self.replicatorSender.repl_sender_receive(self.code, self.value)
