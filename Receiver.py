from array import array
from codecs import StreamWriter
import enum
from collections import namedtuple
import socket
import string
import struct
from collections import namedtuple
import threading
from xmlrpc.client import DateTime
'''
import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="milos",
    password="Grobarijug123",
    #database="mydatabase"
    )
except socket.error as e:
    print(str(e))
'''

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()




CODE = enum["CODE_ANALOG", "CODE_DIGITAL", "CODE_CUSTOM", "CODE_LIMITSET", "CODE_SINGLENODE", "CODE_MULTIPLENODE", "CODE_CONSUMER", "CODE_SOURCE"]

ReceiverProperty = struct(Code = CODE, ReceiverValue = int)

HistoricalCollection = struct(properties = ReceiverProperty[array])

CollectionDescription = struct( id = int, DataSet = int, Collection = HistoricalCollection)
'''
class FileItem:
    rp = ReceiverProperty.__new__
    dateTime = DateTime.__new__
'''
class Logger:
    fileName = string
    sw = StreamWriter
    def __init__(self, fileName):
        self.fileName = fileName

class Reader:
    fileName = string
    l = Logger
    def __init__(self, fileName):
        self.fileName = fileName
        l = Logger.__new__("@LOGGS\readerLogs")

class ReplicatorReceiver:
    reader1 = Reader
    reader2 = Reader
    reader3 = Reader
    reader4 = Reader
