import sys
import threading
import time
from writer import Writer
from ReplicatorReceiver.Logger import Logger


class NevalidanUnos(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message is None:
            return "Nevalidan unos."
        return self.message


def main():
    writer = Writer()
    threads = []
    l: Logger = Logger(r"C:\Users\Pantex\PycharmProjects\pythonProject\BazaPodataka\LOG\UILogs.txt")
    ret: int

    while True:
        print("Pritisni dugme za Meni")
        if len(threads) == 0:
            print("Nema upaljenih writera.")
        input()

        ret = Meni()
        if ret == 1:
            threads.append(threading.Thread(target=writer.writer_send_data))
            threads[len(threads) - 1].start()
            print(f"Upaljeno {len(threads)}  writera")
            l.LoggActivity(f"Upaljen novi writer.Trenutno writera -> {len(threads)}  ")
        elif ret == 2:
            threads[len(threads) - 1].join()
            threads.pop(len(threads) - 1)
            print(f"Upaljeno {len(threads)} writera")
            l.LoggActivity(f"Ugasen jedan writer.Trenutno writera -> {len(threads)} ")
        elif ret == 3:
            continue
        elif ret == 4:
            break
        else:
            print("Nepostojeca komanda")

    for t in threads:
        t.join()

    print("Gasenje")
    sys.exit()


def Meni():
    while True:
        print("1.Upali writera")
        print("2.Ugasi writera")
        print("3.Odustani")
        print("4.Ugasi klijenta")
        br = input()
        try:
            br = int(br)
            if br <= 0 or br > 4:
                raise NevalidanUnos("Pogresan unos!")

            return br
        except NevalidanUnos as e:
            print(e)
            return None
        except Exception:
            print("Unesite broj.")
            return None


if __name__ == "__main__":
    main()
