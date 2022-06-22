import os
from datetime import datetime
from assets.helper import CODE, DeltaCD
from ReplicatorReceiver.Logger import Logger


class CollectionFileItems:
    fileItems = []


class Reader:
    def __init__(self, fileName):
        self.currentVal = 1
        self.fileName = fileName
        self.l: Logger = Logger(r"C:\Users\Pantex\PycharmProjects\pythonProject\BazaPodataka\LOG\readerLogs.txt")
        self.niz = []

    @staticmethod
    def write_in_file_pr(file_path, content):
        with open(file_path, 'a') as file:
            file.write(content)

    def write_in_file2(self, delta_cd: DeltaCD):
        for item in delta_cd.update:
            # Updatuj trenutnu vrednost i loguj ako treba?
            new_value = item.ReceiverValue
            self.currentVal = new_value
        for item in delta_cd.add:
            # Upisi u bazu podataka i loguj ako treba?
            new_rp = item
            # f = open(self.fileName, "a")
            dateTime = datetime.now().strftime("%d-%m-%y %H:%M:%S")
            self.write_in_file_pr(self.fileName, f"{dateTime};{new_rp.Code.name};{new_rp.ReceiverValue}\n")
            self.l.LoggStoredCodes(new_rp.Code, new_rp.ReceiverValue, dateTime)
            self.currentVal = new_rp.ReceiverValue
            # f.close()

    def read_from_file(self, code, fromDate, toDate):
        fromDate = datetime.strptime(fromDate, "%d-%m-%y %H:%M:%S")
        toDate = datetime.strptime(toDate, "%d-%m-%y %H:%M:%S")
        f = open(self.fileName, "r")
        while True:
            st = f.readline()
            if not st or os.stat(self.fileName).st_size == 0:
                for item in CollectionFileItems.fileItems:
                    print(item)
                CollectionFileItems.fileItems.clear()
                break
            else:
                self.niz = st.split(';')
                pom1 = datetime.strptime(self.niz[0], "%d-%m-%y %H:%M:%S")
                pom2 = self.niz[1]
                pom3 = int(self.niz[2])
                if CODE[pom2] == CODE[code]:
                    if fromDate.hour <= pom1.hour <= toDate.hour:
                        if fromDate.minute <= pom1.minute <= toDate.minute:
                            if fromDate.second <= pom1.second <= toDate.second:
                                CollectionFileItems.fileItems.append(pom3)

    def read_from_file2(self, code):
        f = open(self.fileName, "r")
        while True:
            st = f.readline()
            if not st or os.stat(self.fileName).st_size == 0:
                for item in range(0, len(CollectionFileItems.fileItems)):
                    if item == (len(CollectionFileItems.fileItems) - 1):
                        print(CollectionFileItems.fileItems[item])
                        CollectionFileItems.fileItems.clear()
                break
            else:
                self.niz = st.split(';')
                pom1 = datetime.strptime(self.niz[0], "%d-%m-%y %H:%M:%S")
                pom2 = self.niz[1]
                pom3 = int(self.niz[2])
                if CODE[pom2] == CODE[code]:
                    CollectionFileItems.fileItems.append(pom3)
