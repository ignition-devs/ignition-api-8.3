"""Kafka Functions.

The following functions allow you to poll and distribute data with a
Kafka system.
"""

from __future__ import print_function

__all__ = [
    "listConnectorInfo",
    "listTopicPartitions",
    "listTopics",
    "pollPartition",
    "pollTopic",
    "seekLatest",
    "sendRecord",
    "sendRecordAsync",
]

from typing import Any, Dict, List, Optional

from dev.coatl.helper.types import AnyStr


def listConnectorInfo():
    # type: () -> List[Dict[AnyStr, Any]]
    """Returns descriptions of all Kafka connectors in PyDictionary
    format.

    Returns:
        A list of descriptions of all Kafka connectors in PyDictionary
        format.
    """
    pass


def listTopicPartitions(
    connector,  # type: AnyStr
    topic,  # type: AnyStr
    groupId,  # type: AnyStr
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> List[Any]
    """Returns a list of records that match the filter.

    Args:
        connector: The name of the Kafka connector.
        topic: The name of the Kafka topic.
        groupId: The unique string of the consumer group the consumer
            belongs to.
        options: Custom options specific to the consumer, with key value
            string pairs. Optional

    Returns:
        A list of records that match the filter.
    """
    print(connector, topic, groupId, options)
    return []


def listTopics(connector):
    # type: (AnyStr) -> List[Any]
    """Returns a list of topics for the provided connector.

    Args:
        connector: The name of the Kafka connector.

    Returns:
        A list of topics for the provided connector.
    """
    print(connector)
    return []


def pollPartition(
    connector,  # type: AnyStr
    topic,  # type: AnyStr
    partition,  # type: int
    offset,  # type: AnyStr
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> List[Any]
    """Polls a specific partition of a topic.

    Args:
        connector: The name of the Kafka connector.
        topic: The name of the Kafka topic.
        partition: The partition to poll.
        offset: The position of offset to start the poll at.
        options: Custom options specific to the consumer, with key value
            string pairs. Optional

    Returns:
        A list of records polled from a specified partition.
    """
    print(connector, topic, partition, offset, options)
    return []


def pollTopic(
    connector,  # type: AnyStr
    topic,  # type: AnyStr
    groupId,  # type: AnyStr
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> List[Any]
    """Returns a list of records from the specified topic.

    Args:
        connector: The name of the Kafka connector.
        topic: The name of the Kafka topic.
        groupId: The unique string of the consumer group the consumer
            belongs to.
        options: Custom options specific to the consumer, with key value
            string pairs. Optional

    Returns:
        A list of records from the specified topic.
    """
    print(connector, topic, groupId, options)
    return []


def seekLatest(
    connector,  # type: AnyStr
    topic,  # type: AnyStr
    partition,  # type: int
    recordCount,  # type: int
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> List[Any]
    """Polls a specific partition of a topic.

    Args:
        connector: The name of the Kafka connector.
        topic: The name of the Kafka topic.
        partition: The partition to poll.
        recordCount: The number of records to return.
        options: Custom options specific to the consumer, with key value
            string pairs. Optional

    Returns:
        An N number of records from a specified topic, as a list.
    """
    print(connector, topic, partition, recordCount, options)
    return []


def sendRecord(
    connector,  # type: AnyStr
    topic,  # type: AnyStr
    key,  # type: AnyStr
    value,  # type: AnyStr
    partition=None,  # type: Optional[int]
    timestamp=None,  # type: Optional[long]
    headerKeys=None,  # type: Optional[List[Any]]
    headerValues=None,  # type: Optional[List[Any]]
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> Dict[AnyStr, Any]
    """Polls a specific partition of a topic.

    Args:
        connector: The name of the Kafka connector.
        topic: The name of the Kafka topic.
        key: The Kafka record key, used in identifying the record.
        value: The Kafka record key, used in identifying the record.
        partition: The partition to poll. Optional.
        timestamp: The record timestamp, in milliseconds. Optional.
        headerKeys: The header keys for the record. Optional.
        headerValues: The header values for the record. Optional.
        options: Custom options specific to the producer, with key value
            string pairs. Optional

    Returns:
        A PyDictionary representing metadata response in key value
        pairs.
    """
    print(
        connector,
        topic,
        key,
        value,
        partition,
        timestamp,
        headerKeys,
        headerValues,
        options,
    )
    return {
        "topic": topic,
        "partition": partition if partition is not None else 0,
        "offset": None,
        "timestamp": timestamp if timestamp is not None else 0,
    }


def sendRecordAsync(
    connector,  # type: AnyStr
    topic,  # type: AnyStr
    key,  # type: AnyStr
    value,  # type: AnyStr
    partition=None,  # type: Optional[int]
    timestamp=None,  # type: Optional[long]
    headerKeys=None,  # type: Optional[List[Any]]
    headerValues=None,  # type: Optional[List[Any]]
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> None
    """Sends a record to a specified topic asynchronously.

    If a metadata response is required, system.kafka.sendRecord can be
    used for blocking until a response is received.

    Args:
        connector: The name of the Kafka connector.
        topic: The name of the Kafka topic.
        key: The Kafka record key, used in identifying the record.
        value: The Kafka record key, used in identifying the record.
        partition: The partition to target. Optional.
        timestamp: The record timestamp, in milliseconds. Optional.
        headerKeys: The header keys for the record. Optional.
        headerValues: The header values for the record. Optional.
        options: Custom options specific to the producer, with key value
            string pairs. Optional
    """
    print(
        connector,
        topic,
        key,
        value,
        partition,
        timestamp,
        headerKeys,
        headerValues,
        options,
    )
