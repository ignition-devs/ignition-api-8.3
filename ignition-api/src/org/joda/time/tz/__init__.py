__all__ = ["NameProvider", "Provider"]

from typing import TYPE_CHECKING, Iterable

from dev.coatl.helper.types import AnyStr
from java.util import Locale

if TYPE_CHECKING:
    from org.joda.time import DateTimeZone


class NameProvider(object):
    def getName(self, locale, id_, nameKey):
        # type: (Locale, AnyStr, AnyStr) -> AnyStr
        raise NotImplementedError

    def getShortName(self, locale, id_, nameKey):
        # type: (Locale, AnyStr, AnyStr) -> AnyStr
        raise NotImplementedError


class Provider(object):
    def getAvailableIDs(self):
        # type: () -> Iterable[AnyStr]
        raise NotImplementedError

    def getZone(self, id_):
        # type: (AnyStr) -> DateTimeZone
        raise NotImplementedError
