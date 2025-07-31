"""Event Stream Functions.

The following functions allow you to get and run event stream
information.
"""

from __future__ import print_function

__all__ = [
    "getDiagnostics",
    "listEventStreams",
    "publishEvent",
]

from typing import Any, Dict, Optional

from dev.coatl.helper.types import AnyStr


def getDiagnostics(project, path):
    # type: (AnyStr, AnyStr) -> None
    """Retrieves diagnostics for an event stream.

    Args:
        project: The project the event stream belongs to.
        path: The paths to the event stream resource.
    """
    print(project, path)


def listEventStreams(project):
    # type: (AnyStr) -> None
    """Lists all event streams in a project.

    Args:
        project: The project the event stream(s) belong to.
    """
    print(project)


def publishEvent(
    project,  # type: AnyStr
    path,  # type: AnyStr
    message,  # type: AnyStr
    acknowledge,  # type: bool
    gatewayId=None,  # type: Optional[AnyStr]
):
    # type: (...) -> Dict[AnyStr, Any]
    """Publishes a message to a Gateway Event Source.

    You can publish a message to the local Gateway, or a remote Gateway.

    Args:
        project: The project the event stream(s) belong to.
        path: The path to the event stream resource.
        message: The string message to send.
        acknowledge: If True, further messages will be blocked until the
            receiving Gateway Event Listener source finishes processing
            the message. If False, further messages will be blocked
            until the Gateway Event Listener source receives the
            message.
        gatewayId: The Gateway ID of the remote Gateway you want to send
            the message to. Not specifying a remote Gateway will send
            the message to the specified event stream path and project
            on the local Gateway. Optional.

    Returns:
        A dictionary of key and value status pairs resulting from
        publishing the specified event stream.
    """
    print(project, path, message, acknowledge, gatewayId)
    return {"errorMessage": None, "stage": None, "status": None}
