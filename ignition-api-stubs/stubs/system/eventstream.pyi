from typing import Any, Dict, Optional

from dev.coatl.helper.types import AnyStr

def getDiagnostics(project: AnyStr, path: AnyStr) -> None: ...
def listEventStreams(project: AnyStr) -> None: ...
def publishEvent(
    project: AnyStr,
    path: AnyStr,
    message: AnyStr,
    acknowledge: bool,
    gatewayId: Optional[AnyStr] = ...,
) -> Dict[AnyStr, Any]: ...
