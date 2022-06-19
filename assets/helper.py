import enum
from dataclasses import dataclass


class CODE(enum.Enum):
    CODE_ANALOG = 0
    CODE_DIGITAL = 1
    CODE_CUSTOM = 2
    CODE_LIMITSET = 3
    CODE_SINGLENODE = 4
    CODE_MULTIPLENODE = 5
    CODE_CONSUMER = 6
    CODE_SOURCE = 7


@dataclass
class ReceiverProperty:
    Code: CODE
    ReceiverValue: int

    def __init__(self, code, receiverValue):
        self.Code = code
        self.ReceiverValue = receiverValue

