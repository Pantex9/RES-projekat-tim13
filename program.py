from datetime import datetime
import sys
import threading
import time
import os
from assets.helper import CODE
from replicator_sender import ReplicatorSender
from writer import Writer
from ReplicatorReceiver.Logger import Logger
from ReplicatorReceiver.Receiver import ReplicatorReceiver


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
    l: Logger = Logger(r"C:\Users\Pantex\Documents\GitHub\RES-projekat-tim13\BazaPodataka\LOG\UILogs.txt")
    data = ReplicatorReceiver()
    ret: int

    while True:
        print("Pritisni dugme za Meni")
        if len(threads) == 0:
            print("Nema upaljenih writera.")
        input()

        ret = Meni()
        if ret == 1:
            writer.stop_threads = False
            threads.append(threading.Thread(target=writer.writer_send_data))
            threads[len(threads) - 1].start()
            dateTime = datetime.now().strftime("%d-%m-%y %H:%M:%S")
            print(f"Upaljeno {len(threads)}  writera")
            l.LoggActivity(f"Upaljen novi writer.Trenutno writera -> {len(threads)}  ", dateTime)
        elif ret == 2:
            writer.stop_threads = True
            time.sleep(1)
            threads[len(threads) - 1].join()
            threads.clear()
            dateTime = datetime.now().strftime("%d-%m-%y %H:%M:%S")
            l.LoggActivity(f"Ugaseni writeri.", dateTime)
        elif ret == 3:
            br = iscitavanje_po_vr_intervalu()
            code1 = br[0]
            odDatuma1 = br[1]
            doDatuma1 = br[2]
            data.send_to_read(code1, odDatuma1, doDatuma1)
        elif ret == 4:
            code2 = iscitavanje_poslednje_vrednosti()
            data.send_to_read2(code2)
        elif ret == 5:
            continue
        elif ret == 6:
            break
        else:
            print("Nepostojeca komanda")

    print("Gasenje")
    sys.exit()



def iscitavanje_poslednje_vrednosti():
    print("CODE_ANALOG, CODE_DIGITAL, CODE_CUSTOM,"
          "CODE_LIMITSET, CODE_SINGLENODE, CODE_MULTIPLENODE, CODE_CONSUMER, CODE_SOURCE")
    print("Unesite neku od vrednosti iznad koje zelite da iscitate:")
    code = input()
    return code


def iscitavanje_po_vr_intervalu():
    while True:
        print("CODE_ANALOG, CODE_DIGITAL, CODE_CUSTOM,"
              " CODE_LIMITSET, CODE_SINGLENODE, CODE_MULTIPLENODE, CODE_CONSUMER, CODE_SOURCE")
        print("Unesite neku od vrednosti iznad koje zelite da iscitate:")
        code = input()
        print("Unesite od kog datuma zelite da iscitate")
        odDatuma = input()
        print("Unesite do kog datuma zelite da iscitate")
        doDatuma = input()
        pom = [code, odDatuma, doDatuma]
        return pom


def Meni():
    while True:
        print("1.Upali writera")
        print("2.Ugasi writere")
        print("3.Citanje vrednosti readera po vremenskom intervalu za trazeni kod")
        print("4.Dobavljanje poslednje vrenosti izabranog koda")
        print("5.Odustani")
        print("6.Ugasi klijenta")
        br = input()
        try:
            br = int(br)
            if br <= 0 or br > 6:
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
