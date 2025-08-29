__all__ = ["AbstractReadableInstantFieldProperty"]

from typing import TYPE_CHECKING, Optional, Union

from dev.coatl.helper.types import AnyStr
from java.lang import Object
from java.util import Locale

if TYPE_CHECKING:
    from org.joda.time import (
        DateTimeField,
        DateTimeFieldType,
        DurationField,
        Interval,
        ReadableInstant,
        ReadablePartial,
    )


class AbstractReadableInstantFieldProperty(Object):
    def __init__(self):
        # type: () -> None
        super(AbstractReadableInstantFieldProperty, self).__init__()

    def compareTo(self, arg):
        # type: (Union[ReadableInstant, ReadablePartial]) -> int
        pass

    def get(self):
        # type: () -> int
        pass

    def getAsShortText(self, arg=None):
        # type: (Optional[Locale]) -> AnyStr
        pass

    def getAsString(self):
        # type: () -> AnyStr
        pass

    def getAsText(self, locale=None):
        # type: (Optional[Locale]) -> AnyStr
        pass

    def getDifference(self, instant):
        # type: (ReadableInstant) -> int
        pass

    def getDifferenceAsLong(self, instant):
        # type: (ReadableInstant) -> long
        pass

    def getDurationField(self):
        # type: () -> DurationField
        pass

    def getField(self):
        # type: () -> DateTimeField
        pass

    def getFieldType(self):
        # type: () -> DateTimeFieldType
        pass

    def getLeapAmount(self):
        # type: () -> int
        pass

    def getLeapDurationField(self):
        # type: () -> DurationField
        pass

    def getMximumShortTextLength(self, locale):
        # type: (Locale) -> int
        pass

    def getMaximumTextLength(self, locale):
        # type: (Locale) -> int
        pass

    def getMaximumValue(self):
        # type: () -> int
        pass

    def getMaximumValueOverall(self):
        # type: () -> int
        pass

    def getMinimumValue(self):
        # type: () -> int
        pass

    def getMinimumValueOverall(self):
        # type: () -> int
        pass

    def getName(self):
        # type: () -> AnyStr
        pass

    def getRangeDurationField(self):
        # type: () -> DurationField
        pass

    def isLeap(self):
        # type: () -> bool
        pass

    def remainder(self):
        # type: () -> long
        pass

    def toInterval(self):
        # type: () -> Interval
        pass
