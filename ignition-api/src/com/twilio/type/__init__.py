from __future__ import print_function

__all__ = ["PhoneNumber"]

from dev.coatl.helper.types import AnyStr
from java.lang import Object


class PhoneNumber(Object):
    def __init__(self, number):
        # type: (AnyStr) -> None
        super(PhoneNumber, self).__init__()
        print(number)

    def getEndPoint(self):
        # type: () -> AnyStr
        pass
