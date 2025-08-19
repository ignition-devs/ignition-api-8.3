from typing import Any, Dict, List, Optional

__all__ = ["QueryResults"]

from com.inductiveautomation.ignition.common import BasicDataset
from dev.coatl.helper.types import AnyStr
from java.lang import Object
from java.util import AbstractList


class QueryResults(AbstractList):
    class Row(Object):
        def getKeys(self):
            # type: () -> List[AnyStr]
            pass

        def getKeyValue(self, aKey):
            # type: (AnyStr) -> Object
            pass

    def __init__(self, dataset, parent=None, parentRow=None):
        # type: (BasicDataset, Optional[Any], Optional[int]) -> None
        super(QueryResults, self).__init__()
        print(dataset, parent, parentRow)

    def addNestedQueryResults(self, key, results):
        # type: (AnyStr, QueryResults) -> None
        print(key, results)

    def get(self, index):
        # type: (int) -> QueryResults.Row
        pass

    def getCoreResults(self):
        # type: () -> BasicDataset
        pass

    def getNestedQueryResults(self):
        # type: () -> Dict[AnyStr, List[QueryResults]]
        pass

    def lookup(self, rowIndex, keyName):
        # type: (int, AnyStr) -> Object
        pass

    def size(self):
        # type: () -> int
        pass
