import threading
from datetime import datetime
import random
from time import sleep

from replicator_sender import ReplicatorSender
from ReplicatorReceiver.Logger import Logger
from assets.helper import CODE


class Writer:
    global stop_threads

    def __init__(self):
        self.code = None
        self.value = None
        self.replicatorSender = ReplicatorSender()
        self.logger = Logger(r"C:\Users\Pantex\Documents\GitHub\RES-projekat-tim13\BazaPodataka\LOG\writerLogs.txt")

    def writer_send_data(self):
        while True:
            self.code = random.randint(0, 7)
            self.value = random.randrange(100, 1000, 3)  # Returns any random integer of specific length 3
            self.replicatorSender.repl_sender_receive(self.code, self.value)
            self.logger.LoggSentCodes(CODE(self.code), self.value, datetime.now().strftime("%d-%m-%y %H:%M:%S"),
                                      threading.current_thread().ident)
            print(f"Poslao THREAD ID-> {threading.current_thread().ident} : {CODE(self.code)} , VALUE:{self.value}")
            if self.stop_threads:
                break
            sleep(2)
