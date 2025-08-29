__all__ = ["Creator", "Deleter", "Fetcher", "Page", "Reader", "Resource", "Updater"]

from typing import Any, List, Optional

from com.google.common.util.concurrent import ListenableFuture
from com.twilio.http import TwilioRestClient
from dev.coatl.helper.types import AnyStr
from java.lang import Object


class Creator(Object):
    def __init__(self):
        # type: () -> None
        super(Creator, self).__init__()

    def create(self, client=None):
        # type: (Optional[TwilioRestClient]) -> Resource
        pass

    def createAsync(self, client=None):
        # type: (Optional[TwilioRestClient]) -> ListenableFuture
        pass


class Deleter(Object):
    def __init__(self):
        # type: () -> None
        super(Deleter, self).__init__()

    def delete(self, client=None):
        # type: (Optional[TwilioRestClient]) -> bool
        pass

    def deleteAsync(self, client=None):
        # type: (Optional[TwilioRestClient]) -> ListenableFuture
        pass


class Fetcher(Object):
    def __init__(self):
        # type: () -> None
        super(Fetcher, self).__init__()

    def fetch(self, client=None):
        # type: (Optional[TwilioRestClient]) -> Resource
        pass

    def fetchAsync(self, client=None):
        # type: (Optional[TwilioRestClient]) -> ListenableFuture
        pass


class Page(Object):
    def __init__(self):
        # type: () -> None
        super(Page, self).__init__()

    @staticmethod
    def fromJson(*args):
        # type: (*Any) -> Page
        pass

    def getFirstPageUrl(self, domain, region):
        # type: (AnyStr, AnyStr) -> AnyStr
        pass

    def getNextPageUrl(self, domain, region):
        # type: (AnyStr, AnyStr) -> AnyStr
        pass

    def getPageSize(self):
        # type: () -> int
        pass

    def getPreviousPageUrl(self, domain, region):
        # type: (AnyStr, AnyStr) -> AnyStr
        pass

    def getRecords(self):
        # type: () -> List[Any]
        pass

    def getUrl(self, domain, region):
        # type: (AnyStr, AnyStr) -> AnyStr
        pass

    def hasNextPage(self):
        # type: () -> bool
        pass


class Reader(Object):
    def __init__(self):
        # type: () -> None
        super(Reader, self).__init__()

    def firstPage(self, client=None):
        # type: (Optional[TwilioRestClient]) -> Page
        pass

    def getLimit(self):
        # type: () -> long
        pass

    def getPage(self, targetUrl, client=None):
        # type: (AnyStr, Optional[TwilioRestClient]) -> Page
        pass

    def getPageSize(self):
        # type: () -> int
        pass

    def limit(self, limit):
        # type: (long) -> Reader
        pass

    def nextPage(self, page, client=None):
        # type: (Page, Optional[TwilioRestClient]) -> Page
        pass

    def pageSize(self, pageSize):
        # type: (int) -> Reader
        pass

    def previousPage(self, page, client=None):
        # type: (Page, Optional[TwilioRestClient]) -> Page
        pass

    def read(self, client=None):
        # type: (Optional[TwilioRestClient]) -> List[Resource]
        pass

    def readAsync(self, client=None):
        # type: (Optional[TwilioRestClient]) -> ListenableFuture
        pass


class Resource(Object):
    def __init__(self):
        # type: () -> None
        super(Resource, self).__init__()


class Updater(Object):
    def __init__(self):
        # type: () -> None
        super(Updater, self).__init__()

    def update(self, client=None):
        # type: (Optional[TwilioRestClient]) -> Resource
        pass

    def updateAsync(self, client=None):
        # type: (Optional[TwilioRestClient]) -> ListenableFuture
        pass
