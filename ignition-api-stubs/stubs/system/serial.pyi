from typing import Any, List, Optional

from com.inductiveautomation.ignition.modules.serial.scripting import SerialScriptModule
from dev.coatl.helper.types import AnyStr

BIT_RATE_110: int
BIT_RATE_150: int
BIT_RATE_300: int
BIT_RATE_600: int
BIT_RATE_1200: int
BIT_RATE_2400: int
BIT_RATE_4800: int
BIT_RATE_9600: int
BIT_RATE_19200: int
BIT_RATE_38400: int
BIT_RATE_57600: int
BIT_RATE_115200: int
BIT_RATE_230400: int
BIT_RATE_460800: int
BIT_RATE_921600: int
DATA_BITS_5: int
DATA_BITS_6: int
DATA_BITS_7: int
DATA_BITS_8: int
DEFAULT_BIT_RATE: int
DEFAULT_DATA_BITS: int
DEFAULT_FLOW_CONTROL: int
DEFAULT_HANDSHAKE: int
DEFAULT_HARDWARE_FLOW_CONTROL: bool
DEFAULT_PARITY: int
DEFAULT_READ_TIMEOUT_MS: int
DEFAULT_STOP_BITS: int
DEFAULT_WRITE_TIMEOUT_MS: int
FLOW_CONTROL_CTS_ENABLED: int
FLOW_CONTROL_DISABLED: int
FLOW_CONTROL_DSR_ENABLED: int
FLOW_CONTROL_DTR_ENABLED: int
FLOW_CONTROL_RTS_ENABLED: int
FLOW_CONTROL_XONXOFF_IN_ENABLED: int
FLOW_CONTROL_XONXOFF_OUT_ENABLED: int
PARITY_EVEN: int
PARITY_ODD: int
PARITY_MARK: int
PARITY_SPACE: int
PARITY_NONE: int
STOP_BITS_1: int
STOP_BITS_2: int

def closeSerialPort(port: AnyStr) -> None: ...
def configureSerialPort(
    port: AnyStr,
    bitRate: Optional[int] = ...,
    dataBits: Optional[int] = ...,
    handshake: Optional[int] = ...,
    hardwareFlowControl: Optional[bool] = ...,
    parity: Optional[int] = ...,
    stopBits: Optional[int] = ...,
) -> SerialScriptModule.SerialConfigurator: ...
def openSerialPort(port: AnyStr) -> None: ...
def port(
    port: AnyStr,
    bitRate: Optional[int] = ...,
    dataBits: Optional[int] = ...,
    handshake: Optional[int] = ...,
    hardwareFlowControl: Optional[bool] = ...,
    parity: Optional[int] = ...,
    stopBits: Optional[int] = ...,
) -> SerialScriptModule.PortManager: ...
def readBytes(
    port: AnyStr, numberOfBytes: int, timeout: Optional[int] = ...
) -> List[Any]: ...
def readBytesAsString(
    port: AnyStr, numberOfBytes: int, timeout: int = ..., encoding: AnyStr = ...
) -> AnyStr: ...
def readLine(
    port: AnyStr, timeout: int = ..., encoding: AnyStr = ..., crlfRequired: bool = ...
) -> AnyStr: ...
def readUntil(
    port: AnyStr,
    delimiter: AnyStr,
    includeDelimiter: bool,
    timeout: Optional[int] = ...,
) -> AnyStr: ...
def sendBreak(port: AnyStr, millis: int) -> None: ...
def write(
    port: AnyStr, toWrite: AnyStr, timeout: int = ..., encoding: Optional[AnyStr] = ...
) -> None: ...
def writeBytes(port: AnyStr, toWrite: Any, timeout: Optional[int] = ...) -> None: ...
