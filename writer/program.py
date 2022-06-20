import sys
import threading
from writer import Writer
from Reciever.logger import Logger
from replicator_sender import ReplicatorSender


def main():
    writer = Writer
    threads = []
    l: Logger = Logger(r"C:\Users\Pantex\PycharmProjects\pythonProject\BazaPodataka\LOG\UILogs.txt")
    send: ReplicatorSender = ReplicatorSender()
    ret: int

    while True:
        print("Pritisni dugme za Meni")
        if len(threads) == 0:
            print("Nema upaljenih writera.")
        input()
        ret = Meni()
        if ret == 1:
            #start_new_thread(writer(send, l).writer_send_data(), ())
            thread = threading.Thread(target=writer(send, l).writer_send_data())
            thread.start()
            #new_thread = Thread()
            #threads.append(new_thread)
           # threads(threads.count - 1) = start()
            print(f"Upaljeno {len(threads)}  writera")
            print(f"Upaljen novi writer.Trenutno writera {len(threads)} ")
        elif ret == 2:
            print(f"Upaljeno {len(threads)} writera")
            print(f"Ugasen jedan writer.Trenutno writera -> {len(threads)}")
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
    br: int
    while True:
        print("1.Upali writera")
        print("2.Ugasi writera")
        print("3. Odustani")
        print("4.Ugasi klijenta")
        try:
            br = int(input())
            return br
        except:
            print("Pogresan unos!")


if __name__ == "__main__":
    main()
