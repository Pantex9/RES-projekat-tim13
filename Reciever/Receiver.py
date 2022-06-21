import threading
from time import sleep

from assets.helper import CODE, ReceiverProperty, DeltaCD
from ReplicatorReceiver.Reader import Reader


class HistoricalCollection:
    def __init__(self):
        self.properties = []


class CollectionDescription:
    def __init__(self, cd_id, dataset):
        self.id = cd_id
        self.dataSet = dataset
        self.Collection = HistoricalCollection()


class ReplicatorReceiver:
    def __init__(self):
        self.collectionDescription1 = CollectionDescription(1, 1)
        self.collectionDescription2 = CollectionDescription(2, 2)
        self.collectionDescription3 = CollectionDescription(3, 3)
        self.collectionDescription4 = CollectionDescription(4, 4)

        self.delta_cd1 = DeltaCD(1)
        self.delta_cd2 = DeltaCD(2)
        self.delta_cd3 = DeltaCD(3)
        self.delta_cd4 = DeltaCD(4)

        self.reader1 = Reader("C:\\Users\\Pantex\\PycharmProjects\\pythonProject\\BazaPodataka\\DataSet\\database1.txt")
        self.reader2 = Reader("C:\\Users\\Pantex\\PycharmProjects\\pythonProject\\BazaPodataka\\DataSet\\database2.txt")
        self.reader3 = Reader("C:\\Users\\Pantex\\PycharmProjects\\pythonProject\\BazaPodataka\\DataSet\\database3.txt")
        self.reader4 = Reader("C:\\Users\\Pantex\\PycharmProjects\\pythonProject\\BazaPodataka\\DataSet\\database4.txt")

        self.thread = threading.Thread(target=self.ReadersRead)
        self.thread.start()

    def Send(self, code: CODE, value):
        c = code
        rp = ReceiverProperty(c, value)

        if c == CODE.CODE_ANALOG or c == CODE.CODE_DIGITAL:
            self.collectionDescription1.Collection.properties.append(rp)

        elif c == CODE.CODE_CUSTOM or c == CODE.CODE_LIMITSET:
            self.collectionDescription2.Collection.properties.append(rp)

        elif c == CODE.CODE_SINGLENODE or c == CODE.CODE_MULTIPLENODE:
            self.collectionDescription3.Collection.properties.append(rp)

        elif c == CODE.CODE_CONSUMER or c == CODE.CODE_SOURCE:
            self.collectionDescription4.Collection.properties.append(rp)

    def ReadersRead(self):
        while True:
            # CD1
            if not self.check_if_empty(self.collectionDescription1.Collection.properties):
                value = self.collectionDescription1.Collection.properties[0]
                self.process_receiver_property(value=value, reader=self.reader1, delta_cd=self.delta_cd1)
                self.collectionDescription1.Collection.properties.pop(0)
            # CD2
            # promenio sam ovo u IF umesto ELIF, da i ovo proveri u svakom prolazu kroz petlju
            if not self.check_if_empty(self.collectionDescription2.Collection.properties):
                value = self.collectionDescription2.Collection.properties[0]
                self.process_receiver_property(value=value, reader=self.reader2, delta_cd=self.delta_cd2)
                self.collectionDescription2.Collection.properties.pop(0)

            # CD3
            if not self.check_if_empty(self.collectionDescription3.Collection.properties):
                value = self.collectionDescription3.Collection.properties[0]
                self.process_receiver_property(value=value, reader=self.reader3, delta_cd=self.delta_cd3)
                self.collectionDescription3.Collection.properties.pop(0)

            # CD4
            if not self.check_if_empty(self.collectionDescription4.Collection.properties):
                value = self.collectionDescription4.Collection.properties[0]
                self.process_receiver_property(value=value, reader=self.reader4, delta_cd=self.delta_cd4)
                self.collectionDescription4.Collection.properties.pop(0)

            sleep(1)

    # proveravam da li je lista propertija prazna
    def check_if_empty(self, properties_list):
        if len(properties_list) > 0:
            return False
        return True

    # metoda za spremanje za upis u bazu podataka
    def ready_for_db(self, value: ReceiverProperty, reader: Reader, delta_cd: DeltaCD):
        # dodajem receiver property u ADD listu, koja ce da se doda u BP u Reader komponenti
        delta_cd.add.append(value)
        # ispisujem trenutnu zbirnu duzinu deltaCD komponente
        print(f"DeltaCD {delta_cd.id} len = {len(delta_cd.add) + len(delta_cd.update)}")
        if self.check_delta_size(delta_cd):
            reader.write_in_file2(delta_cd)
            self.clear_delta_cd(delta_cd)

    # metoda za spremanje za update only, bez upisa u bazu podataka
    def ready_for_update_only(self, value: ReceiverProperty, reader: Reader, delta_cd: DeltaCD):
        # dodajem rp u UPDATE listu, koja ce da odradi samo update vrednosti currentVal u Reader komponenti
        delta_cd.update.append(value)
        # ispisujem trenutnu zbirnu duzinu deltaCD komponente
        print(f"DeltaCD {delta_cd.id} len = {len(delta_cd.add) + len(delta_cd.update)}")
        if self.check_delta_size(delta_cd):
            reader.write_in_file2(delta_cd)
            self.clear_delta_cd(delta_cd)

    # metoda koja prazni obe liste DeltaCD komponente
    def clear_delta_cd(self, delta_cd: DeltaCD):
        delta_cd.add.clear()
        delta_cd.update.clear()

    # metoda koja obradjuje reciever property uzet iz datog cd-a za dati reader i dati delta_cd
    def process_receiver_property(self, value: ReceiverProperty, reader: Reader, delta_cd: DeltaCD):
        # Ako je CODE.CODE_DIGITAL, svakako treba upisati u bazu podataka
        if self.check_code_digital(value):
            self.ready_for_db(value, reader, delta_cd)

        # Ako je tacno, potrebno je upisati u bazu podataka
        elif self.deadband(reader.currentVal, value.ReceiverValue):
            self.ready_for_db(value, reader, delta_cd)

        # Ako nije tacno, onda je potrebno samo updatovati vrednost
        else:
            self.ready_for_update_only(value, reader, delta_cd)

    # Proverava duzinu delta_cd komponente, da li je add.count() + update.count() > 10
    def check_delta_size(self, delta_cd: DeltaCD):
        size = len(delta_cd.add) + len(delta_cd.update)
        if size >= 10:
            return True
        return False

    # Proverava da li je kod == CODE_DIGITAL
    def check_code_digital(self, rp: ReceiverProperty):
        if rp.Code == CODE.CODE_DIGITAL:
            return True
        return False

    # Vraca 2% od vrednosti val
    def two_percent(self, val):
        return val * 2 / 100

    # Vraca True ako je razlika nove i stare vrednosti VECA od 2%
    # U suprotnom vraca False
    def deadband(self, old_val, new_val):
        if abs(old_val - new_val) > self.two_percent(old_val):
            return True
        return False