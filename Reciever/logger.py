
from codecs import StreamWriter
import string
import threading
from datetime import datetime
from assets.helper import CODE


class Logger:
    def __init__(self, fileName):
        self.fileName = fileName

    def LoggSentCodes(self, code: CODE, value: int, dateTime: datetime, writerId: int):
        threading.Lock()
        f = open(self.fileName, "a")
        f.write(f"\n{dateTime} Writer id: {writerId} sent:   {code} Value:  {value}")
        f.close()

    def LoggStoredCodes(self, code=CODE, value=int, dateTime=datetime):
        f = open(self.fileName, "a")
        f.write(f"\n{dateTime} DATA STORED: {code}, Value:  {value}")
        f.close()

    def LoggActivity(self, activity: string):
        f = open(self.fileName, "a")
        f.write(f"\n {activity} ; {str(datetime.now)}")
        f.close()
