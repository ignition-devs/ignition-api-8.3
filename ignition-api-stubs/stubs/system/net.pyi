from typing import Any, Callable, List, Optional

from com.inductiveautomation.ignition.common.script.builtin.http import JythonHttpClient
from dev.coatl.helper.types import AnyStr

def getHostName() -> AnyStr: ...
def getIpAddress() -> AnyStr: ...
def getRemoteServers(runningOnly: Optional[bool] = ...) -> List[AnyStr]: ...
def httpClient(
    timeout: int = ...,
    bypass_cert_validation: bool = ...,
    username: Optional[AnyStr] = ...,
    password: Optional[AnyStr] = ...,
    proxy: Optional[AnyStr] = ...,
    cookie_policy: AnyStr = ...,
    redirect_policy: AnyStr = ...,
    version: AnyStr = ...,
    customizer: Optional[Callable[..., Any]] = ...,
) -> JythonHttpClient: ...
def sendEmail(
    smtp: Optional[AnyStr] = ...,
    fromAddr: AnyStr = ...,
    subject: Optional[AnyStr] = ...,
    body: Optional[AnyStr] = ...,
    html: bool = ...,
    to: Optional[List[AnyStr]] = ...,
    attachmentNames: Optional[List[object]] = ...,
    attachmentData: Optional[List[object]] = ...,
    timeout: int = ...,
    username: Optional[AnyStr] = ...,
    password: Optional[AnyStr] = ...,
    priority: AnyStr = ...,
    smtpProfile: Optional[AnyStr] = ...,
    cc: Optional[List[AnyStr]] = ...,
    bcc: Optional[List[AnyStr]] = ...,
    retries: int = ...,
    replyTo: Optional[List[AnyStr]] = ...,
) -> None: ...
