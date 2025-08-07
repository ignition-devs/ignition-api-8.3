"""Historian Functions.

The following functions give you access to interact with the Historian
system.
"""

from __future__ import print_function

__all__ = [
    "browse",
    "convertToQualifiedPath",
    "deleteAnnotations",
    "queryAnnotations",
    "queryMetadata",
    "queryValues",
    "storeAnnotations",
    "storeDataPoints",
    "updateRegisteredNodePath",
]

from typing import Any, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import BasicQualifiedValue
from dev.coatl.helper.types import AnyStr
from java.util import Date


def browse(rootPath, *args, **kwargs):
    # type: (AnyStr, *Any, **Any) -> Results
    """Returns a list of browse results for the specified Historian."""
    print(rootPath, args, kwargs)
    return Results()


def convertToQualifiedPath(stringPath, isHistorical):
    # type: (AnyStr, bool) -> AnyStr
    """Converts a string path into a qualified path to use for storing
    or querying.

    Args:
        stringPath: The original string to be converted into a qualified
            path.
        isHistorical: Designates whether the string represents a tag or
            a historical path. If not specified, the path is assumed to
            be of a tag.

    Returns:
        A string of the qualified path that can be used for storage and
        queries.
    """
    print(stringPath, isHistorical)
    return ""


def deleteAnnotations(paths, storageIds):
    # type: (List[AnyStr], List[AnyStr]) -> List[BasicQualifiedValue]
    """Deletes desired annotations from the specified Historian.

    Args:
        paths: A list of historical paths associated with the
            annotations.
        storageIds: A list of annotation storage IDs to be used for
            deleting.

    Returns:
        A list of qualified values. The quality code will indicate
        success or failure, and if successful, the storage ID of the
        annotation will have been deleted.
    """
    print(paths, storageIds)
    return [BasicQualifiedValue() for _ in paths]


def queryAnnotations(
    paths,  # type: List[AnyStr]
    startDate=None,  # type: Optional[Date]
    endDate=None,  # type: Optional[Date]
    allowedTypes=None,  # type: Optional[List[AnyStr]]
):
    # type: (...) -> Results
    """Queries user stored annotations from the Tag history system for a
    set of paths, for a given time range.

    Args:
        paths: A list of historical paths to query annotations for.
        startDate: A start time to query annotations for.
        endDate: An end time to query annotations for. Optional.
        allowedTypes: A list of string types to query annotations for.
            Optional.

    Returns:
        A Results object that contains a list of query results.
    """
    print(paths, startDate, endDate, allowedTypes)
    return Results()


def queryMetadata(paths, startDate=None, endDate=None):
    # type: (List[AnyStr], Optional[Date], Optional[Date]) -> Results
    """Queries metadata for the specified Historian.

    Args:
        paths: A list of historical paths to query metadata for.
        startDate: A start time to query metadata for. This parameter is
            optional, unless an end time is specified.
        endDate: An end time to query metadata for. If specifying an end
            time, a start time must be provided. Optional.

    Returns:
        A Results object that contains a list of query results.
    """
    print(paths, startDate, endDate)
    return Results()


def queryValues(definitions, filter):
    # type: (List[Any], Any) -> BasicDataset
    """Queries values for the specified Historian.

    Args:
        definitions: A list of historical paths to query values for.
        filter: Filters to include/exclude value data within the
            returned query results, such as quality and timestamp.

    Returns:
        A dataset representing the historian values for the specified
        historical paths.
    """
    print(definitions, filter)
    return BasicDataset()


def storeAnnotations(*args, **kwargs):
    # type: (*Any, **Any) -> List[BasicQualifiedValue]
    """Store a list of annotations to the specified Historian.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        A list of qualified values. The quality code will indicate
        success or failure.
    """
    print(args, kwargs)
    return [BasicQualifiedValue()]


def storeDataPoints(*args, **kwargs):
    # type: (*Any, **Any) -> List[BasicQualifiedValue]
    """Store a list of data points to the specified Historian.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        A list of qualified values. The quality code will indicate
        success or failure.
    """
    print(args, kwargs)
    return [BasicQualifiedValue()]


def storeMetadata(*args, **kwargs):
    # type: (*Any, **Any) -> List[BasicQualifiedValue]
    """Store a list of metadata to the specified Historian.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        A list of qualified values. The quality code will indicate
        success or failure.
    """
    print(args, kwargs)
    return [BasicQualifiedValue()]


def updateRegisteredNodePath(previousPath, currentPath):
    # type: (AnyStr, AnyStr) -> List[BasicQualifiedValue]
    """Updates the existing historical path for a stored historian node
    to the newly specific path.

    Args:
        previousPath: The previous path for the historian node.
        currentPath: The new current path for the historian node. If
            null, then the historian node will be retired.

    Returns:
        A list of qualified values. The quality code will indicate
        success or failure, and if successful, the path will be updated.
    """
    print(previousPath, currentPath)
    return [BasicQualifiedValue()]
