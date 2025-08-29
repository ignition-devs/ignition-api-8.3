from java.lang import Runnable
from java.util.concurrent import Executor

class ListenableFuture:
    def addListener(self, listener: Runnable, executor: Executor) -> None: ...
