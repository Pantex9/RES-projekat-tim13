from array import array
import code
import math
import struct
from datetime import date, datetime

from pymysql import NULL
from FileItem import FileItem
from Logger import Logger
import string
import FileItem
from Receiver import ReceiverProperty
from assets.helper import CODE
from assets.helper import ReceiverProperty
from codecs import StreamReader, StreamWriter

CollectionFileItems = struct(fileItems = FileItem[array])

class Reader:
    fileName = string
    l = Logger
    def __init__(self, fileName):
        self.fileName = fileName
        l = Logger.__new__("@BazaPodataka\readerLogs")

    def WriteInFile(self, receiverProperty = ReceiverProperty):
        str = string
        niz = string[array]
        difference = int

        if(receiverProperty.Code == CODE.CODE_DIGITAL):
            with StreamWriter(self.fileName, True) as self.sw:
                 self.sw.writelines()#
                 self.l.LoggStoredCodes(receiverProperty.code, receiverProperty.value, datetime.now)
                 return

        with StreamReader(self.fileName) as self.sr:
            while(True):
                str = self.sr.readline()
                if(str == "<EOF>" or str == NULL):
                    break
                else:
                    niz = str.split(';')
                    pom1 = datetime
                    pom1 = datetime.strptime(niz[0])
                    pom2 = CODE
                    #CODE.
                    pom3 = int
                    pom3 = int(niz[2])
                    it = FileItem(datetime = pom1, rp = ReceiverProperty(code = pom2, value = pom3)) #
                    if(it.rp == receiverProperty.code):#
                        difference = abs(it.rp - receiverProperty.value) #
                        if(difference < it.rp * 0.02):
                            return
        
        with StreamWriter(self.fileName, True) as self.sw:
            self.sw.writelines() #
            self.l.LoggStoredCodes(receiverProperty.code, receiverProperty.value, datetime.now)