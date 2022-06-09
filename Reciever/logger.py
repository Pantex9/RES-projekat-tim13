

from codecs import StreamWriter
from dataclasses import dataclass
import string
import threading
from xmlrpc.client import DateTime


class Logger:
    
    sw=StreamWriter()
    filename=string
    dateTime=DateTime()

    def __init__(self,fileName):
        self.filename=fileName
        #mutex=Mutex()

    def LoggSentCodes(self,code,value,dateTime,writerId):
        my_mutex=threading.Lock()
        with StreamWriter(self._fileName, True) as self._sw:

                self._sw.writelines("\n{0:s} Writer id: {1:s} sent:   {2:s} Value:  {3:s}".format(dateTime, writerId, code, value))
                self._sw.Close()
    



    def LoggStoredCodes(self, code, value, dateTime):
        with StreamWriter(self._fileName, True) as self._sw:

            self._sw.writelines("\n{0:s} DATA STORED: {1:s}, Value:  {2:s}".format(dateTime, code, value))
            self._sw.Close()


    def LoggActivity(self, activity):
        with StreamWriter(self._fileName, True) as self._sw:

            self._sw.writelines("\n"+activity+" "+DateTime.Now)
            self._sw.Close()
