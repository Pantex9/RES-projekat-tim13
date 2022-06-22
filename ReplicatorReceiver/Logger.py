from codecs import StreamWriter
import string
import threading
from datetime import datetime
from assets.helper import CODE


class Logger:
    def __init__(self, fileName):
        self.fileName = fileName
        self.dateTime = datetime.now().strftime("%d-%m-%y %H:%M:%S")

    @staticmethod
    def write_in_file(file_path, content):
        with open(file_path, 'a') as file:
            file.write(content)

    def LoggSentCodes(self, code: CODE, value: int, dateTime, writerId: int):
        threading.Lock()
        try:
            self.write_in_file(self.fileName, f"\n{dateTime} Writer id: {writerId} sent:   {code.name} Value:  {value}")
            if value < 0 and writerId < 0:
                raise Exception("Greska pri upisu u fajl. Int vrednosti moraju biti POZITIVNE")
            if value < 0 or writerId < 0:
                raise Exception("Greska pri upisu u fajl. Int vrednost mora biti POZITIVNA")

        except Exception as e:
            print(e)

    def LoggStoredCodes(self, code: CODE, value: int, dateTime):
        try:
            self.write_in_file(self.fileName, f"\n{dateTime} DATA STORED: {code.name}, Value:  {value}")
            if value < 0:
                raise Exception("Greska pri upisu u fajl. Value mora biti pozitivan")
        except Exception as e:
            print(e)

    def LoggActivity(self, activity: str, dateTime):
        try:
            self.write_in_file(self.fileName, f"\n {activity} ; {dateTime}")
            if activity == "":
                raise Exception("Greska pri upisu u fajl. Niste uneli nista")
        except Exception as e:
            print(e)
