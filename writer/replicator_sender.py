from assets.helper import ReceiverProperty, CODE


class ReplicatorSender:
    def __init__(self):
        self.thread = None
        self.queue = []

    def repl_sender_receive(self, code, value):
        # potrebna je struktura koja bi sacuvala vrednosti CODE i VALUE
        rp = ReceiverProperty(code, value)
        self.queue.append(rp)
        print(f"Primljeno od writera, KOD = {CODE(code)}, VREDNOST = {value}")
        print("Trenutno stanje QUEUE-a:")
        for rp in self.queue:
            print(f"Code[{CODE(rp.code)}] = {rp.value}")
