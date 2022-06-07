from array import array
import enum
from collections import namedtuple
import string
import struct
from collections import namedtuple
import threading
from time import sleep
from typing import Collection
from Logger import Logger
from Reader import Reader
from assets.helper import CODE

#CODE = Enum["CODE_ANALOG", "CODE_DIGITAL", "CODE_CUSTOM", "CODE_LIMITSET", "CODE_SINGLENODE", "CODE_MULTIPLENODE", "CODE_CONSUMER", "CODE_SOURCE"]

ReceiverProperty = struct(Code = CODE, ReceiverValue = int)

HistoricalCollection = struct(properties = ReceiverProperty[array])

CollectionDescription = struct( id = int, DataSet = int, Collection = HistoricalCollection,  properties = ReceiverProperty[100])

class ReplicatorReceiver:
    reader1 = Reader
    reader2 = Reader
    reader3 = Reader
    reader4 = Reader

    collectionDescription1 = CollectionDescription(1,1)
    collectionDescription2 = CollectionDescription(2,2)
    collectionDescription3 = CollectionDescription(3,3)
    collectionDescription4 = CollectionDescription(4,4)

    collection1Count = 0
    collection2Count = 0
    collection3Count = 0
    collection4Count = 0

    thread = threading.Thread

def Send(self, code, value):
    c = CODE
    self.code = string(c)
    rp = ReceiverProperty(c, value)

    if(c == CODE.CODE_ANALOG or c == CODE.CODE_DIGITAL):
      # ReplicatorReceiver.collectionDescription1
       ReplicatorReceiver.collection1Count += 1

    elif(c == CODE.CODE_CUSTOM or c == CODE.CODE_LIMITSET):
        ReplicatorReceiver.collection2Count += 1
    elif(c == CODE.CODE_SINGLENODE or c == CODE.CODE_MULTIPLENODE):
        ReplicatorReceiver.collection3Count += 1
    elif(c == CODE.CODE_CONSUMER or c == CODE.CODE_SOURCE):
        ReplicatorReceiver.collection4Count += 1

def ReadersRead(self):
    while(True):
        if(ReplicatorReceiver.collection1Count > 0):
            ReplicatorReceiver.collection1Count -=1

        if(ReplicatorReceiver.collection2Count > 0):
            ReplicatorReceiver.collection2Count -=1
        
        if(ReplicatorReceiver.collection3Count > 0):
            ReplicatorReceiver.collection3Count -=1
        
        if(ReplicatorReceiver.collection4Count > 0):
            ReplicatorReceiver.collection4Count -=1

        threading.Thread = sleep(1000)