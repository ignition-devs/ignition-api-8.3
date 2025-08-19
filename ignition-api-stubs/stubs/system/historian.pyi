from typing import Any, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import BasicQualifiedValue
from dev.coatl.helper.types import AnyStr
from java.util import Date

def browse(rootPath: AnyStr, *args: Any, **kwargs: Any) -> Results: ...
def deleteAnnotations(
    paths: List[AnyStr], storageIds: List[AnyStr]
) -> List[BasicQualifiedValue]: ...
def queryAggregatedPoints(
    paths: List[AnyStr],
    startTime: Optional[Date] = ...,
    endTime: Optional[Date] = ...,
    aggregates: Optional[List[AnyStr]] = ...,
    fillModes: Optional[List[AnyStr]] = ...,
    columnNames: Optional[List[AnyStr]] = ...,
    returnFormat: str = ...,
    returnSize: int = ...,
    includeBounds: bool = ...,
    excludeObservations: bool = ...,
) -> BasicDataset: ...
def queryAnnotations(
    paths: List[AnyStr],
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    allowedTypes: Optional[List[AnyStr]] = ...,
) -> Results: ...
def queryMetadata(
    paths: List[AnyStr], startDate: Optional[Date] = ..., endDate: Optional[Date] = ...
) -> Results: ...
def queryRawPoints(
    paths: List[AnyStr],
    startTime: Optional[Date] = ...,
    endTime: Optional[Date] = ...,
    columnNames: Optional[List[AnyStr]] = ...,
    returnFormat: str = ...,
    returnSize: int = ...,
    includeBounds: bool = ...,
    excludeObservations: bool = ...,
) -> BasicDataset: ...
def storeAnnotations(*args: Any, **kwargs: Any) -> List[BasicQualifiedValue]: ...
def storeDataPoints(*args: Any, **kwargs: Any) -> List[BasicQualifiedValue]: ...
def storeMetadata(*args: Any, **kwargs: Any) -> List[BasicQualifiedValue]: ...
def updateRegisteredNodePath(
    previousPath: AnyStr, currentPath: AnyStr
) -> List[BasicQualifiedValue]: ...
