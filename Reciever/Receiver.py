from assets.helper import CODE, ReceiverProperty
from threading import Thread
from time import sleep
from tracemalloc import start
from Reader import Reader


class HistoricalCollection:
    properties: ReceiverProperty = []


class CollectionDescription:
    Id: int
    DataSet: int

    def __init__(self, id, dataSet):
        self.Id = id
        self.DataSet = dataSet
        self.Collection = HistoricalCollection
        self.Collection.properties = [100]


class ReplicatorReceiver:
    def __init__(self):
        self.collectionDescription1 = CollectionDescription(1, 1)
        self.collectionDescription2 = CollectionDescription(2, 2)
        self.collectionDescription3 = CollectionDescription(3, 3)
        self.collectionDescription4 = CollectionDescription(4, 4)

        self.collection1Count = 0
        self.collection2Count = 0
        self.collection3Count = 0
        self.collection4Count = 0

        self.reader1 = Reader(r"C:\Users\Pantex\PycharmProjects\pythonProject\BazaPodataka\DataSet\database1.txt")
        self.reader2 = Reader(r"C:\Users\Pantex\PycharmProjects\pythonProject\BazaPodataka\DataSet\database2.txt")
        self.reader3 = Reader(r"C:\Users\Pantex\PycharmProjects\pythonProject\BazaPodataka\DataSet\database3.txt")
        self.reader4 = Reader(r"C:\Users\Pantex\PycharmProjects\pythonProject\BazaPodataka\DataSet\database4.txt")

        self.thread = Thread.__new__(self.ReadersRead)
        start()

    def Send(self, code: str, value: int):
        c: CODE = CODE[code]
        rp: ReceiverProperty = ReceiverProperty(c, value)

        if c == CODE.CODE_ANALOG or c == CODE.CODE_DIGITAL:

            self.collectionDescription1.Collection.properties[self.collection1Count] = rp
            self.collection1Count += 1
        elif c == CODE.CODE_CUSTOM or c == CODE.CODE_LIMITSET:
            self.collectionDescription2.Collection.properties[self.collection2Count] = rp
            self.collection2Count += 1
        elif c == CODE.CODE_SINGLENODE or c == CODE.CODE_MULTIPLENODE:
            self.collectionDescription3.Collection.properties[self.collection3Count] = rp
            self.collection3Count += 1
        elif c == CODE.CODE_CONSUMER or c == CODE.CODE_SOURCE:
            self.collectionDescription4.Collection.properties[self.collection4Count] = rp
            self.collection4Count += 1

    @staticmethod
    def RemoveFirst(param: [ReceiverProperty]):
        l: list[ReceiverProperty] = param
        del l[0]
        return l

    def ReadersRead(self):
        while True:
            if self.collection1Count > 0:
                self.reader1.WriteInFile(self.collectionDescription1.Collection.properties[0])
                self.collectionDescription1.Collection.properties = self.RemoveFirst(
                    self.collectionDescription1.Collection.properties)
                self.collection1Count -= 1

            if self.collection2Count > 0:
                self.reader2.WriteInFile(self.collectionDescription2.Collection.properties[0])
                self.collectionDescription2.Collection.properties = self.RemoveFirst(
                    self.collectionDescription2.Collection.properties)
                self.collection2Count -= 1

            if self.collection3Count > 0:
                self.reader3.WriteInFile(self.collectionDescription3.Collection.properties[0])
                self.collectionDescription3.Collection.properties = self.RemoveFirst(
                    self.collectionDescription3.Collection.properties)
                self.collection3Count -= 1

            if self.collection4Count > 0:
                self.reader4.WriteInFile(self.collectionDescription4.Collection.properties[0])
                self.collectionDescription4.Collection.properties = self.RemoveFirst(
                    self.collectionDescription4.Collection.properties)
                self.collection4Count -= 1

            sleep(1000)
