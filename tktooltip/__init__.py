"""
TkToolTip
=========

Provides a tooltip (pop-up) widget for tkinter

Features:
---------
    - Normal tooltips
    - Functions tooltips
    - Delayed tooltips
    - Tracking tooltips
    - Theme-aware tooltips and fully customisable
"""

from .tooltip import ToolTip, ToolTipStatus

__all__ = [
    "ToolTip",
    "ToolTipStatus",
]
