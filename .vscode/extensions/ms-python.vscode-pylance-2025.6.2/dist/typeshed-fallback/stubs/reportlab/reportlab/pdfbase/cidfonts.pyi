from _typeshed import Incomplete
from typing import Final

from reportlab.pdfbase import pdfmetrics

__version__: Final[str]
DISABLE_CMAP: bool

def findCMapFile(name): ...
def structToPDF(structure): ...

class CIDEncoding(pdfmetrics.Encoding):
    name: Incomplete
    source: Incomplete
    def __init__(self, name, useCache: int = 1) -> None: ...
    def parseCMAPFile(self, name) -> None: ...
    def translate(self, text): ...
    def fastSave(self, directory) -> None: ...
    def fastLoad(self, directory) -> None: ...
    def getData(self): ...

class CIDTypeFace(pdfmetrics.TypeFace):
    def __init__(self, name) -> None: ...
    def getCharWidth(self, characterId): ...

class CIDFont(pdfmetrics.Font):
    faceName: Incomplete
    face: Incomplete
    encodingName: Incomplete
    encoding: Incomplete
    fontName: Incomplete
    name: Incomplete
    isVertical: Incomplete
    substitutionFonts: Incomplete
    def __init__(self, face, encoding) -> None: ...
    def formatForPdf(self, text): ...
    def stringWidth(self, text, size, encoding=None): ...
    def addObjects(self, doc) -> None: ...

class UnicodeCIDFont(CIDFont):
    language: Incomplete
    name: Incomplete
    vertical: Incomplete
    isHalfWidth: Incomplete
    unicodeWidths: Incomplete
    def __init__(self, face, isVertical: bool = False, isHalfWidth: bool = False) -> None: ...
    def formatForPdf(self, text): ...
    def stringWidth(self, text, size, encoding=None): ...

def precalculate(cmapdir) -> None: ...
def test() -> None: ...
