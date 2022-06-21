import os
from datetime import datetime
from assets.helper import ReceiverProperty, CODE, DeltaCD
from ReplicatorReceiver.FileItem import FileItem
from ReplicatorReceiver.Logger import Logger


class CollectionFileItems:
    fileItems = [FileItem]


class Reader:
    def __init__(self, fileName):
        self.currentVal = 1
        self.fileName = fileName
        self.l: Logger = Logger(r"C:\Users\Pantex\PycharmProjects\pythonProject\BazaPodataka\LOG\readerLogs.txt")
        self.niz = []
        self.dateTime = datetime.now().strftime("%d-%m-%y %H:%M:%S")

    def write_in_file2(self, delta_cd: DeltaCD):
        for item in delta_cd.update:
            # Updatuj trenutnu vrednost i loguj ako treba?
            new_value = item.ReceiverValue
            self.currentVal = new_value
        for item in delta_cd.add:
            # Upisi u bazu podataka i loguj ako treba?
            new_rp = item
            f = open(self.fileName, "a")
            f.write(f"\n{self.dateTime}  ;  {new_rp.Code}  ; {new_rp.ReceiverValue}")
            self.l.LoggStoredCodes(new_rp.Code, new_rp.ReceiverValue, self.dateTime)
            self.currentVal = new_rp.ReceiverValue
            f.close()
