from typing import List

from dev.coatl.helper.types import AnyNum, AnyStr

def demandPoll(deviceName: AnyStr, classList: List[int]) -> None: ...
def directOperateAnalog(
    deviceName: AnyStr, variation: int, index: int, value: AnyNum
) -> None: ...
def directOperateBinary(
    deviceName: AnyStr,
    index: int,
    tcc: int,
    opType: int,
    count: int,
    onTime: int,
    offTime: int,
) -> None: ...
def freezeAnalogs(deviceName: AnyStr, indexes: List[int]) -> None: ...
def freezeAtTimeAnalogs(
    deviceName: AnyStr, absoluteTime: int, intervalTime: int, indexes: List[int]
) -> None: ...
def freezeAtTimeCounters(
    deviceName: AnyStr, absoluteTime: int, intervalTime: int, indexes: List[int]
) -> None: ...
def freezeClearAnalogs(deviceName: AnyStr, indexes: List[int]) -> None: ...
def freezeClearCounters(deviceName: AnyStr, indexes: List[int]) -> None: ...
def freezeCounters(deviceName: AnyStr, indexes: List[int]) -> None: ...
def selectOperateAnalog(
    deviceName: AnyStr, variation: int, index: int, value: AnyNum
) -> None: ...
def selectOperateBinary(
    deviceName: AnyStr,
    index: int,
    tcc: int,
    opType: int,
    count: int,
    onTime: int,
    offTime: int,
) -> None: ...
def synchronizeTime(deviceName: AnyStr) -> None: ...
