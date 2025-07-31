from __future__ import print_function

__all__ = [
    "ClientDatasetUtilities",
    "ClientPrintUtilities",
    "ClientSystemUtilities",
    "INavUtilities",
    "NavUtilities",
    "VisionUtilities",
    "WindowUtilities",
]

from typing import Any, Dict, List, Optional, Tuple, Union

from com.inductiveautomation.factorypmi.application import FPMIApp, FPMIWindow
from com.inductiveautomation.factorypmi.application.script import PyComponentWrapper
from com.inductiveautomation.ignition.common.i18n.keyboard import KeyboardLayout
from com.inductiveautomation.ignition.common.model.values import QualityCode
from dev.coatl.helper.types import AnyStr
from java.awt import Color, Component, Graphics
from java.awt.event import ActionEvent, ComponentEvent, MouseEvent
from java.awt.image import BufferedImage
from java.awt.print import PageFormat
from java.lang import Number, Object
from java.util import EventObject, Locale
from javax.swing import JComponent, JFrame, JPopupMenu
from org.python.core import PyObject, PySequence, PyTuple


class INavUtilities(object):
    """Parent interface to coordinate the functions between NavUtilities
    and NavUtilitiesDispatcher.
    """

    def centerWindow(self, arg):
        # type: (Union[FPMIWindow, AnyStr]) -> None
        raise NotImplementedError

    def closeParentWindow(self, event):
        # type: (EventObject) -> None
        raise NotImplementedError

    def closeWindow(self, arg):
        # type: (Union[FPMIWindow, AnyStr]) -> None
        raise NotImplementedError

    def getCurrentWindow(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def goBack(self):
        # type: () -> PyObject
        raise NotImplementedError

    def goForward(self):
        # type: () -> PyObject
        raise NotImplementedError

    def goHome(self):
        # type: () -> PyObject
        raise NotImplementedError

    def openWindow(self, path, params=None):
        # type: (AnyStr, Optional[Dict[AnyStr, Any]]) -> PyObject
        raise NotImplementedError

    def openWindowImpl(self, path, params, openAdditional):
        # type: (AnyStr, Dict[AnyStr, Any], bool) -> PyObject
        raise NotImplementedError

    def openWindowInstance(self, path, params=None):
        # type: (AnyStr, Optional[Dict[AnyStr, Any]]) -> PyObject
        raise NotImplementedError

    def swapTo(self, name, params):
        # type: (AnyStr, Dict[AnyStr, Any]) -> PyObject
        raise NotImplementedError

    def swapWindow(self, *args):
        # type: (*Any) -> PyObject
        raise NotImplementedError


class ClientDatasetUtilities(Object):
    def __init__(self, app):
        # type: (FPMIApp) -> None
        super(ClientDatasetUtilities, self).__init__()
        print(app)


class ClientSystemUtilities(Object):
    def __init__(self):
        # type: () -> None
        super(ClientSystemUtilities, self).__init__()


class NavUtilities(INavUtilities):
    def centerWindow(self, arg):
        # type: (Union[FPMIWindow, AnyStr]) -> None
        pass

    def closeParentWindow(self, event):
        # type: (EventObject) -> None
        pass

    def closeWindow(self, arg):
        # type: (Union[FPMIWindow, AnyStr]) -> None
        pass

    def getCurrentWindow(self):
        # type: () -> AnyStr
        pass

    def goBack(self):
        # type: () -> PyObject
        pass

    def goForward(self):
        # type: () -> PyObject
        pass

    def goHome(self):
        # type: () -> PyObject
        pass

    def openWindow(self, path, params=None):
        # type: (AnyStr, Optional[Dict[AnyStr, Any]]) -> PyObject
        pass

    def openWindowImpl(self, path, params, openAdditional):
        # type: (AnyStr, Dict[AnyStr, Any], bool) -> PyObject
        pass

    def openWindowInstance(self, path, params=None):
        # type: (AnyStr, Optional[Dict[AnyStr, Any]]) -> PyObject
        pass

    def swapTo(self, name, params):
        # type: (AnyStr, Dict[AnyStr, Any]) -> PyObject
        pass

    def swapWindow(self, *args):
        # type: (*Any) -> PyObject
        pass


class ClientPrintUtilities(Object):

    class ComponentPrinter(Object):
        def __init__(self, c, fit, zoom):
            # type: (Component, bool, float) -> None
            super(ClientPrintUtilities.ComponentPrinter, self).__init__()
            print(c, fit, zoom)

        def print(self, g, pageFormat, pageIndex):
            # type: (Graphics, PageFormat, int) -> int
            pass

    class JythonPrintJob(Object):
        def __init__(self, c):
            # type: (Component) -> None
            super(ClientPrintUtilities.JythonPrintJob, self).__init__()
            print(c)

        def getBottomMargin(self):
            # type: () -> float
            pass

        def getLeftMargin(self):
            # type: () -> float
            pass

        def getOrientation(self):
            # type: () -> int
            pass

        def getPageHeight(self):
            # type: () -> float
            pass

        def getPageWidth(self):
            # type: () -> float
            pass

        def getPrinterName(self):
            # type: () -> AnyStr
            pass

        def getRightMargin(self):
            # type: () -> float
            pass

        def getTopMargin(self):
            # type: () -> float
            pass

        def getZoomFactor(self):
            # type: () -> float
            pass

        def isFitToPage(self):
            # type: () -> bool
            return True

        def isShowPrintDialog(self):
            # type: () -> bool
            return True

        def setBottomMargin(self, bottomMargin):
            # type: (float) -> None
            pass

        def setFitToPage(self, fitToPage):
            # type: (bool) -> None
            pass

        def setLeftMargin(self, leftMargin):
            # type: (float) -> None
            pass

        def setMargins(self, m):
            # type: (float) -> None
            pass

        def setOrientation(self, orientation):
            # type: (int) -> None
            pass

        def setPageHeight(self, pageHeight):
            # type: (float) -> None
            pass

        def setPageWidth(self, pageWidth):
            # type: (float) -> None
            pass

        def setPrinterName(self, printerName):
            # type: (AnyStr) -> None
            pass

        def setRightMargin(self, rightMargin):
            # type: (float) -> None
            pass

        def setShowPrintDialog(self, showPrintDialog):
            # type: (bool) -> None
            pass

        def setZoomFactor(self, zoomFactor):
            # type: (float) -> None
            pass

    def __init__(self, app):
        # type: (Any) -> None
        super(ClientPrintUtilities, self).__init__()
        print(self, app)

    def createImage(self, c):
        # type: (Component) -> BufferedImage
        print(self, c)
        width = height = imageType = 1
        return BufferedImage(width, height, imageType)

    def createPrintJob(self, c):
        # type: (Component) -> ClientPrintUtilities.JythonPrintJob
        pass

    def printToImage(self, c, fileName=None):
        # type: (Component, Optional[str]) -> None
        pass


class VisionUtilities(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(VisionUtilities, self).__init__()
        print(self, args)

    def beep(self):
        # type: () -> None
        pass

    def centerWindow(self, win):
        # type: (PyObject) -> None
        pass

    def close(self):
        # type: () -> None
        pass

    def closeDesktop(self, handle):
        # type: (AnyStr) -> None
        pass

    def closeParentWindow(self, event):
        # type: (EventObject) -> None
        pass

    def closeWindow(self, win):
        # type: (PyObject) -> None
        pass

    def color(self, *args, **kwargs):
        # type: (*Any, **Any) -> Color
        pass

    def createImage(self, c):
        # type: (Component) -> BufferedImage
        pass

    def createPopupMenu(self, keys, functions):
        # type: (PySequence, PySequence) -> JPopupMenu
        pass

    def createPrintJob(self, c):
        # type: (Component) -> ClientPrintUtilities.JythonPrintJob
        pass

    def desktop(self, arg=None):
        # type: (Union[int, AnyStr, None]) -> VisionUtilities
        pass

    def exit(self):
        # type: () -> None
        pass

    def exportCSV(self, *args, **kwargs):
        # type: (*Any, **Any) -> AnyStr
        pass

    def exportExcel(self, *args, **kwargs):
        # type: (*Any, **Any) -> AnyStr
        pass

    def exportHTML(self, *args, **kwargs):
        # type: (*Any, **Any) -> AnyStr
        pass

    def findWindow(self, path):
        # type: (AnyStr) -> List[PyComponentWrapper]
        pass

    def getAvailableLocales(self):
        # type: () -> List[AnyStr]
        pass

    def getAvailableTerms(self):
        # type: () -> List[AnyStr]
        pass

    def getClientId(self):
        # type: () -> AnyStr
        pass

    def getConnectionMode(self):
        # type: () -> int
        pass

    def getConnectTimeout(self):
        # type: () -> int
        pass

    def getCurrentDesktop(self):
        # type: () -> AnyStr
        pass

    def getCurrentWindow(self):
        # type: () -> AnyStr
        pass

    def getDesktopHandles(self):
        # type: () -> List[Any]
        pass

    def getEdition(self):
        # type: () -> AnyStr
        pass

    def getExternalIpAddress(self):
        # type: () -> AnyStr
        pass

    def getGatewayAddress(self):
        # type: () -> AnyStr
        pass

    def getHandle(self):
        # type: () -> AnyStr
        pass

    def getInactivitySeconds(self):
        # type: () -> int
        return 300

    def getKeyboardLayouts(self):
        # type: () -> List[KeyboardLayout]
        pass

    def getLocale(self):
        # type: () -> AnyStr
        pass

    def getOpenedWindowNames(self):
        # type: () -> PyTuple
        pass

    def getOpenedWindows(self):
        # type: () -> PyTuple
        pass

    def getParentWindow(self, event):
        # type: (EventObject) -> PyObject
        pass

    def getReadTimeout(self):
        # type: () -> int
        pass

    def getRoles(self):
        # type: () -> List[AnyStr]
        pass

    def getScreenIndex(self):
        # type: () -> int
        pass

    def getScreens(self):
        # type: () -> PySequence
        pass

    def getSibling(self, event, name):
        # type: (EventObject, AnyStr) -> PyObject
        pass

    def getSystemFlags(self):
        # type: () -> int
        pass

    def getUsername(self):
        # type: () -> AnyStr
        pass

    def getUserRoles(self, *args, **kwargs):
        # type: (*Any, **Any) -> List[AnyStr]
        pass

    def getWindow(self, name):
        # type: (AnyStr) -> PyObject
        pass

    def getWindowNames(self):
        # type: () -> PyTuple
        pass

    def goBack(self):
        # type: () -> PyObject
        pass

    def goForward(self):
        # type: () -> PyObject
        pass

    def goHome(self):
        # type: () -> PyObject
        pass

    def invokeLater(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def isOverlaysEnabled(self):
        # type: () -> bool
        return True

    def isScreenLocked(self):
        # type: () -> bool
        return True

    def isTouchscreenMode(self):
        # type: () -> bool
        return True

    def lockScreen(self, obscure=False):
        # type: (bool) -> None
        pass

    def logout(self):
        # type: () -> None
        pass

    def openDesktop(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> JFrame
        pass

    def openFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> AnyStr
        pass

    def openFiles(self, *args, **kwargs):
        # type: (*Any, **Any) -> List[AnyStr]
        pass

    def openURL(self, url):
        # type: (AnyStr) -> None
        pass

    def openWindow(self, path, params=None):
        # type: (AnyStr, Optional[Dict[AnyStr, Any]]) -> PyObject
        pass

    def openWindowInstance(self, path, params=None):
        # type: (AnyStr, Optional[Dict[AnyStr, Any]]) -> PyObject
        pass

    def playSoundClip(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def printToImage(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def refreshBinding(self, comp, propName):
        # type: (JComponent, AnyStr) -> bool
        return True

    def retarget(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def saveFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> AnyStr
        pass

    def setConnectionMode(self, mode):
        # type: (int) -> None
        pass

    def setConnectTimeout(self, timeout):
        # type: (int) -> None
        pass

    def setLocale(self, locale):
        # type: (Union[AnyStr, Locale]) -> None
        pass

    def setOverlaysEnabled(self, b):
        # type: (bool) -> None
        pass

    def setReadTimeout(self, timeout):
        # type: (int) -> None
        pass

    def setScreenIndex(self, index):
        # type: (int) -> None
        pass

    def setTouchscreenMode(self, b):
        # type: (bool) -> None
        pass

    def showColorInput(self, *args, **kwargs):
        # type: (*Any, **Any) -> Color
        pass

    def showConfirm(self, *args, **kwargs):
        # type: (*Any, **Any) -> bool
        print(args, kwargs)
        return True

    def showDiagnostics(self):
        # type: () -> None
        pass

    def showError(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def showInput(self, *args, **kwargs):
        # type: (*Any, **Any) -> Optional[AnyStr]
        pass

    def showMessage(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def showNumericKeyPad(self, *args, **kwargs):
        # type: (*Any, **Any) -> Number
        pass

    def showPasswordInput(self, *args, **kwargs):
        # type: (*Any, **Any) -> Optional[AnyStr]
        pass

    def showTouchscreenKeyboard(self, *args, **kwargs):
        # type: (*Any, **Any) -> AnyStr
        pass

    def showWarning(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    def swapTo(self, name, params=None):
        # type: (AnyStr, Optional[Dict[AnyStr, Any]]) -> PyObject
        pass

    def swapWindow(self, *args):
        # type: (*Any) -> PyObject
        pass

    def switchUser(self, *args, **kwargs):
        # type: (*Any, **Any) -> bool
        print(args, kwargs)
        return True

    def transform(self, *args, **kwargs):
        # type: (*Any, **AnyStr) -> PyObject
        pass

    def unlockScreen(self):
        # type: () -> None
        pass

    def updateProject(self):
        # type: () -> None
        pass

    def validateUser(self, *args, **kwargs):
        # type: (*Any, **Any) -> bool
        print(args, kwargs)
        return True


class WindowUtilities(Object):
    """These are the scripting functions mounted at system.gui.*.

    Changes to this class must be made carefully, as some of the true
    implementations actually reside in the subclass,
    WindowUtilitiesForDesktop.
    """

    class JyPopupMenu(JPopupMenu):
        def actionPerformed(self, e):
            # type: (ActionEvent) -> None
            pass

        def addJyFunction(self, name, fun):
            # type: (AnyStr, PyObject) -> None
            pass

        def show(self, me, *args):
            # type: (Union[ComponentEvent, MouseEvent], *int) -> None
            pass

    class PopupContext(Object):
        def endPopup(self):
            # type: () -> None
            pass

        def startPopup(self):
            # type: () -> None
            pass

    ACCL_NONE = 0
    ACCL_CONSTANT = 1
    ACCL_FAST_TO_SLOW = 2
    ACCL_SLOW_TO_FAST = 3
    ACCL_EASE = 4
    COORD_DESIGNER = 1
    COORD_SCREEN = 0

    def chooseColor(self, initialColor, dialogTitle="Choose Color"):
        # type: (Color, Optional[AnyStr]) -> Color
        pass

    def closeDesktop(self, handle):
        # type: (AnyStr) -> None
        pass

    @staticmethod
    def color(*args):
        # type: (*Any) -> Color
        pass

    def confirm(
        self,
        message,  # type: AnyStr
        title="Confirm",  # type: AnyStr
        allowCancel=False,  # type: bool
    ):
        # type: (...) -> Optional[bool]
        pass

    @staticmethod
    def convertPointToScreen(x, y, event):
        # type: (int, int, EventObject) -> Tuple[int, int]
        pass

    @staticmethod
    def createPopupContext():
        # type: () -> WindowUtilities.PopupContext
        pass

    @staticmethod
    def createPopupMenu(key, functions):
        # type: (PySequence, PySequence) -> JPopupMenu
        pass

    def desktop(self, arg):
        # type: (Union[int, AnyStr]) -> WindowUtilities
        pass

    def errorBox(self, message, title="Error"):
        # type: (AnyStr, Optional[AnyStr]) -> None
        pass

    @staticmethod
    def find(component):
        # type: (JComponent) -> WindowUtilities
        pass

    def findWindow(self, path):
        # type: (AnyStr) -> List[PyComponentWrapper]
        pass

    def getCurrentDesktop(self):
        # type: () -> AnyStr
        pass

    def getDesktopHandles(self):
        # type: () -> PySequence
        pass

    def getOpenedWindowNames(self):
        # type: () -> PyTuple
        pass

    def getOpenedWindows(self):
        # type: () -> PyTuple
        pass

    @staticmethod
    def getParentWindow(event):
        # type: (EventObject) -> PyObject
        pass

    def getQuality(self, comp, propertyName):
        # type: (JComponent, AnyStr) -> QualityCode
        pass

    def getScreenIndex(self):
        # type: () -> int
        pass

    @staticmethod
    def getScreens():
        # type: () -> PySequence
        pass

    @staticmethod
    def getSibling(event, name):
        # type: (EventObject, AnyStr) -> PyObject
        pass

    def getWindow(self, name):
        # type: (AnyStr) -> PyObject
        pass

    def getWindowNames(self):
        # type: () -> PyTuple
        pass

    def inputBox(self, message, defaultTxt=""):
        # type: (AnyStr, AnyStr) -> Optional[AnyStr]
        pass

    def isTouchscreenModeEnabled(self):
        # type: () -> bool
        return True

    def messageBox(self, message, title="Information"):
        # type: (AnyStr, AnyStr) -> None
        pass

    def openDesktop(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> JFrame
        pass

    def openDiagnostics(self):
        # type: () -> None
        pass

    def passwordBox(
        self,
        message,  # type:AnyStr
        title="Password",  # type: AnyStr
        echoChar="*",  # type: AnyStr
    ):
        # type: (...) -> Optional[AnyStr]
        pass

    def setTouchScreenModeEnabled(self, b):
        # type: (bool) -> None
        pass

    def showNumericKeyPad(
        self,
        initialValue,  # type: Number
        fontSize=None,  # type: Optional[int]
        usePasswordMode=False,  # type: bool
    ):
        # type: (...) -> Number
        pass

    def showTouchscreenKeyboard(self, initialText, fontSize=None, password=None):
        # type: (AnyStr, Optional[int], Optional[bool]) -> AnyStr
        pass

    def transform(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> PyObject
        pass

    def warningBox(self, message, title="Warning"):
        # type: (AnyStr, AnyStr) -> None
        pass
