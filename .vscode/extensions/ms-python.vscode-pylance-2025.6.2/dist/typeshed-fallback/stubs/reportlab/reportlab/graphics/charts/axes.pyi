from _typeshed import Incomplete
from typing import Final

from reportlab.graphics.charts.textlabels import PMVLabel
from reportlab.graphics.widgetbase import Widget
from reportlab.lib.attrmap import *
from reportlab.lib.validators import Validator

__version__: Final[str]

class AxisLabelAnnotation:
    def __init__(self, v, **kwds) -> None: ...
    def __call__(self, axis): ...

class AxisLineAnnotation:
    def __init__(self, v, **kwds) -> None: ...
    def __call__(self, axis): ...

class AxisBackgroundAnnotation:
    def __init__(self, colors, **kwds) -> None: ...
    def __call__(self, axis): ...

class TickLU:
    accuracy: Incomplete
    T: Incomplete
    def __init__(self, *T, **kwds) -> None: ...
    def __contains__(self, t) -> bool: ...
    def __getitem__(self, t): ...

class _AxisG(Widget):
    def makeGrid(self, g, dim=None, parent=None, exclude=[]) -> None: ...
    def getGridDims(self, start=None, end=None): ...
    @property
    def isYAxis(self): ...
    @property
    def isXAxis(self): ...
    def addAnnotations(self, g, A=None) -> None: ...
    def draw(self): ...

class CALabel(PMVLabel):
    def __init__(self, **kw) -> None: ...

class CategoryAxis(_AxisG):
    visible: int
    visibleAxis: int
    visibleTicks: int
    visibleLabels: int
    visibleGrid: int
    drawGridLast: bool
    strokeWidth: int
    strokeColor: Incomplete
    strokeDashArray: Incomplete
    gridStrokeLineJoin: Incomplete
    gridStrokeLineCap: Incomplete
    gridStrokeMiterLimit: Incomplete
    gridStrokeWidth: float
    gridStrokeColor: Incomplete
    gridStrokeDashArray: Incomplete
    gridStart: Incomplete
    strokeLineJoin: Incomplete
    strokeLineCap: Incomplete
    strokeMiterLimit: Incomplete
    labels: Incomplete
    categoryNames: Incomplete
    joinAxis: Incomplete
    joinAxisPos: Incomplete
    joinAxisMode: Incomplete
    labelAxisMode: str
    reverseDirection: int
    style: str
    tickShift: int
    loPad: int
    hiPad: int
    loLLen: int
    hiLLen: int
    def __init__(self) -> None: ...
    def setPosition(self, x, y, length) -> None: ...
    def configure(self, multiSeries, barWidth=None) -> None: ...
    def scale(self, idx): ...
    def midScale(self, idx): ...

class _XTicks:
    @property
    def actualTickStrokeWidth(self): ...
    @property
    def actualTickStrokeColor(self): ...
    def makeTicks(self): ...

class _YTicks(_XTicks):
    def makeTicks(self): ...

class XCategoryAxis(_XTicks, CategoryAxis):
    tickUp: int
    tickDown: int
    def __init__(self) -> None: ...
    categoryNames: Incomplete
    def demo(self): ...
    def joinToAxis(self, yAxis, mode: str = "bottom", pos=None) -> None: ...
    def loScale(self, idx): ...
    def makeAxis(self): ...
    def makeTickLabels(self): ...

class YCategoryAxis(_YTicks, CategoryAxis):
    tickLeft: int
    tickRight: int
    def __init__(self) -> None: ...
    categoryNames: Incomplete
    def demo(self): ...
    def joinToAxis(self, xAxis, mode: str = "left", pos=None) -> None: ...
    def loScale(self, idx): ...
    def makeAxis(self): ...
    def makeTickLabels(self): ...

class TickLabeller:
    def __call__(self, axis, value): ...

class ValueAxis(_AxisG):
    def __init__(self, **kw) -> None: ...
    def setPosition(self, x, y, length) -> None: ...
    def configure(self, dataSeries) -> None: ...
    def makeTickLabels(self): ...
    def scale(self, value): ...

class XValueAxis(_XTicks, ValueAxis):
    tickUp: int
    tickDown: int
    joinAxis: Incomplete
    joinAxisMode: Incomplete
    joinAxisPos: Incomplete
    def __init__(self, **kw) -> None: ...
    def demo(self): ...
    def joinToAxis(self, yAxis, mode: str = "bottom", pos=None) -> None: ...
    def makeAxis(self): ...

def parseDayAndMonth(dmstr): ...

class _isListOfDaysAndMonths(Validator):
    def test(self, x): ...
    def normalize(self, x): ...

isListOfDaysAndMonths: Incomplete

class NormalDateXValueAxis(XValueAxis):
    bottomAxisLabelSlack: float
    niceMonth: int
    forceEndDate: int
    forceFirstDate: int
    forceDatesEachYear: Incomplete
    dailyFreq: int
    xLabelFormat: str
    dayOfWeekName: Incomplete
    monthName: Incomplete
    specialTickClear: int
    valueSteps: Incomplete
    def __init__(self, **kw) -> None: ...
    def configure(self, data) -> None: ...

class YValueAxis(_YTicks, ValueAxis):
    tickRight: int
    tickLeft: int
    joinAxis: Incomplete
    joinAxisMode: Incomplete
    joinAxisPos: Incomplete
    def __init__(self) -> None: ...
    def demo(self): ...
    def joinToAxis(self, xAxis, mode: str = "left", pos=None) -> None: ...
    def makeAxis(self): ...

class TimeValueAxis:
    labelTextFormat: Incomplete
    def __init__(self, *args, **kwds) -> None: ...
    def timeLabelTextFormatter(self, val): ...

class XTimeValueAxis(TimeValueAxis, XValueAxis):
    def __init__(self, *args, **kwds) -> None: ...

class AdjYValueAxis(YValueAxis):
    requiredRange: int
    leftAxisPercent: int
    leftAxisOrigShiftIPC: float
    leftAxisOrigShiftMin: int
    leftAxisSkipLL0: int
    valueSteps: Incomplete
    def __init__(self, **kw) -> None: ...

class LogValueAxis(ValueAxis): ...

class LogAxisTickLabeller(TickLabeller):
    def __call__(self, axis, value): ...

class LogAxisTickLabellerS(TickLabeller):
    def __call__(self, axis, value): ...

class LogAxisLabellingSetup:
    labels: Incomplete
    labelTextFormat: Incomplete
    def __init__(self) -> None: ...

class LogXValueAxis(LogValueAxis, LogAxisLabellingSetup, XValueAxis):
    def __init__(self) -> None: ...
    def scale(self, value): ...

class LogYValueAxis(LogValueAxis, LogAxisLabellingSetup, YValueAxis):
    def __init__(self) -> None: ...
    def scale(self, value): ...
