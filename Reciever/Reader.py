from datetime import datetime
from assets.helper import ReceiverProperty, CODE
from ReplicatorReceiver.FileItem import FileItem
from ReplicatorReceiver.Logger import Logger

from codecs import StreamReader, StreamWriter


class CollectionFileItems:
    fileItems = [FileItem]


class Reader:
    def __init__(self, fileName):
        self.fileName = fileName
        self.l: Logger = Logger(r"C:\Users\Pantex\PycharmProjects\pythonProject\BazaPodataka\PracenjeAktivnosti")

    def WriteInFile(self, receiverProperty: ReceiverProperty):
        if receiverProperty.Code == CODE.CODE_DIGITAL:
            with StreamWriter(self.fileName, str(True)) as self.sw:
                self.sw.writelines(
                    str(datetime.now) + ";" + str(receiverProperty.Code) + ";" + str(receiverProperty.ReceiverValue))
                self.l.LoggStoredCodes(receiverProperty.Code, receiverProperty.ReceiverValue, datetime.now)
                return

        with StreamReader(self.fileName) as self.sr:
            while True:
                st = self.sr.readline()
                if st == "<EOF>" or st is None:
                    break
                else:
                    niz = st.split(";")
                    pom1 = datetime.strptime(niz[0], "%d/%m/%y %H:%M:%S.%f")
                    pom2 = CODE[niz[1]]
                    pom3 = int(niz[2])
                    it: FileItem = FileItem(dateTime=pom1, rp=ReceiverProperty(code=pom2, receiverValue=pom3))
                    if it.rp.Code == receiverProperty.Code:
                        difference = abs(it.rp.ReceiverValue - receiverProperty.ReceiverValue)
                        if difference < it.rp.ReceiverValue * 0.02:
                            return

        with StreamWriter(self.fileName, str(True)) as self.sw:
            self.sw.writelines(
                str(datetime.now) + ";" + str(receiverProperty.Code) + ";" + str(receiverProperty.ReceiverValue))
            self.l.LoggStoredCodes(receiverProperty.Code, receiverProperty.ReceiverValue, datetime.now)
