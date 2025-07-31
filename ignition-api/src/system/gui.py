"""GUI Functions.

The following functions allow you to control windows and create popup
interfaces.
"""

from __future__ import print_function

__all__ = [
    "chooseColor",
    "convertPointToScreen",
    "getQuality",
    "openDiagnostics",
]

from typing import Tuple

from dev.coatl.helper.types import AnyStr
from java.awt import Color
from java.util import EventObject
from javax.swing import JComponent


def chooseColor(initialColor, dialogTitle="Choose Color"):
    # type: (Color, AnyStr) -> Color
    """Prompts the user to pick a color using the default color-chooser
    dialog box.

    Args:
        initialColor: A color to use as a starting point in the color
            choosing popup.
        dialogTitle: The title for the color choosing popup. Defaults to
            "Choose Color". Optional.

    Returns:
        The new color chosen by the user.
    """
    print(initialColor, dialogTitle)
    return Color()


def convertPointToScreen(x, y, event):
    # type: (int, int, EventObject) -> Tuple[int, int]
    """Converts a pair of coordinates that are relative to the upper-
    left corner of some component to be relative to the upper-left
    corner of the entire screen.

    Args:
        x: The X-coordinate, relative to the component that fired the
            event.
        y: The Y-coordinate, relative to the component that fired the
            event.
        event: An event object for a component event.

    Returns:
        A tuple of (x,y) in screen coordinates.
    """
    print(x, y, event)
    return x, y


def getQuality(component, propertyName):
    # type: (JComponent, AnyStr) -> int
    """Returns the data quality for the property of the given component
    as an integer.

    This function can be used to check the quality of a Tag binding on a
    component in the middle of the script so that alternative actions
    can be taken in the event of device disconnections.

    Args:
        component: The component whose property is being checked.
        propertyName: The name of the property as a string value.

    Returns:
        The data quality of the given property as an integer.
    """
    print(component, propertyName)
    return 192


def openDiagnostics():
    # type: () -> None
    """Opens the client runtime diagnostics window, which provides
    information regarding performance, logging, active threads,
    connection status, and the console.

    This provides an opportunity to open the diagnostics window in
    situations where the menu bar in the client is hidden, and the
    keyboard shortcut can not be used.
    """
    pass
