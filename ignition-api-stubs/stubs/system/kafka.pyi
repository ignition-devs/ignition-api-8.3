from typing import Any, Dict, List, Optional

from dev.coatl.helper.types import AnyStr

def listConnectorInfo() -> List[Dict[AnyStr, Any]]: ...
def listTopicPartitions(
    connector: AnyStr,
    topic: AnyStr,
    groupId: AnyStr,
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> List[Any]: ...
def listTopics(connector: AnyStr) -> List[Any]: ...
def pollPartition(
    connector: AnyStr,
    topic: AnyStr,
    partition: int,
    offset: AnyStr,
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> List[Any]: ...
def pollTopic(
    connector: AnyStr,
    topic: AnyStr,
    groupId: AnyStr,
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> List[Any]: ...
def seekLatest(
    connector: AnyStr,
    topic: AnyStr,
    partition: int,
    recordCount: int,
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> List[Any]: ...
def sendRecord(
    connector: AnyStr,
    topic: AnyStr,
    key: AnyStr,
    value: AnyStr,
    partition: Optional[int] = ...,
    timestamp: Optional[long] = ...,
    headerKeys: Optional[List[Any]] = ...,
    headerValues: Optional[List[Any]] = ...,
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> Dict[AnyStr, Any]: ...
def sendRecordAsync(
    connector: AnyStr,
    topic: AnyStr,
    key: AnyStr,
    value: AnyStr,
    partition: Optional[int] = ...,
    timestamp: Optional[long] = ...,
    headerKeys: Optional[List[Any]] = ...,
    headerValues: Optional[List[Any]] = ...,
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> None: ...
