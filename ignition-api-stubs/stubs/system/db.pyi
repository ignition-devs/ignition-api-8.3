from typing import Any, Dict, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.script.builtin import (
    DatasetUtilities,
    SProcCall,
)
from dev.coatl.helper.types import AnyStr

BIT: int
REAL: int
LONGVARCHAR: int
LONGVARBINARY: int
TINYINT: int
DOUBLE: int
DATE: int
NULL: int
SMALLINT: int
NUMERIC: int
TIME: int
ROWID: int
INTEGER: int
DECIMAL: int
TIMESTAMP: int
CLOB: int
BIGINT: int
CHAR: int
BINARY: int
NCLOB: int
FLOAT: int
VARCHAR: int
VARBINARY: int
BLOB: int
NCHAR: int
NVARCHAR: int
LONGNVARCHAR: int
BOOLEAN: int
ORACLE_CURSOR: int
DISTINCT: int
STRUCT: int
REF: int
JAVA_OBJECT: int
SQLXML: int
ARRAY: int
DATALINK: int
OTHER: int
READ_COMMITTED: int
READ_UNCOMMITTED: int
REPEATABLE_READ: int
SERIALIZABLE: int

def addDatasource(
    jdbcDriver: AnyStr,
    name: AnyStr,
    description: AnyStr = ...,
    connectUrl: Optional[AnyStr] = ...,
    username: Optional[AnyStr] = ...,
    password: Optional[AnyStr] = ...,
    props: Optional[AnyStr] = ...,
    validationQuery: Optional[AnyStr] = ...,
    maxConnections: int = ...,
) -> None: ...
def beginNamedQueryTransaction(*args: Any, **kwargs: Any) -> AnyStr: ...
def beginTransaction(
    database: Optional[AnyStr] = ...,
    isolationLevel: Optional[int] = ...,
    timeout: Optional[int] = ...,
) -> AnyStr: ...
def clearQueryCache(
    project: Optional[AnyStr] = ..., path: Optional[AnyStr] = ...
) -> None: ...
def closeTransaction(tx: AnyStr) -> None: ...
def commitTransaction(tx: AnyStr) -> None: ...
def createSProcCall(
    procedureName: AnyStr,
    database: AnyStr = ...,
    tx: Optional[AnyStr] = ...,
    skipAudit: bool = ...,
) -> SProcCall: ...
def execSProcCall(callContext: SProcCall) -> None: ...
def execUpdate(
    path: AnyStr,
    parameters: Optional[Dict[AnyStr, Any]] = ...,
    tx: Optional[AnyStr] = ...,
    getKey: bool = ...,
    project: Optional[AnyStr] = ...,
) -> int: ...
def execUpdateAsync(
    path: AnyStr,
    parameters: Optional[Dict[AnyStr, Any]] = ...,
    project: Optional[AnyStr] = ...,
) -> bool: ...
def getConnectionInfo(name: Optional[AnyStr] = ...) -> BasicDataset: ...
def getConnections() -> BasicDataset: ...
def removeDatasource(name: AnyStr) -> None: ...
def rollbackTransaction(tx: AnyStr) -> None: ...
def runPrepQuery(
    query: AnyStr, args: List[Any], database: AnyStr = ..., tx: Optional[AnyStr] = ...
) -> DatasetUtilities.PyDataSet: ...
def runPrepUpdate(
    query: AnyStr,
    args: List[Any],
    database: AnyStr = ...,
    tx: Optional[AnyStr] = ...,
    getKey: bool = ...,
    skipAudit: bool = ...,
) -> int: ...
def runSFNamedQuery(*args: Any, **kwargs: Any) -> bool: ...
def runSFUpdateQuery(query: AnyStr, datasources: List[AnyStr]) -> bool: ...
def setDatasourceConnectURL(name: AnyStr, connectUrl: AnyStr) -> None: ...
def setDatasourceEnabled(name: AnyStr, enabled: bool) -> None: ...
def setDatasourceMaxConnections(name: AnyStr, maxConnections: int) -> None: ...
