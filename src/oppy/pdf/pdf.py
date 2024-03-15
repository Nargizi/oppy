from __future__ import annotations

from oppy.ocr.tesseract import TESSERACT_DPI_TRESHOLD
from dataclasses import dataclass, field
from typing import List
import fitz  # PyMuPDF


@dataclass
class PDF:
    doc: fitz.Document
    dpi: int = field(default=TESSERACT_DPI_TRESHOLD)

    @classmethod
    def open(cls, url: str) -> PDF:
        return cls(fitz.open(url))

    def _extract_image(
        self, page: fitz.Page, dpi: int = TESSERACT_DPI_TRESHOLD
    ) -> fitz.Pixmap:
        return page.get_pixmap(dpi=dpi)

    def to_imgs(self) -> List[fitz.Pixmap]:
        return [self._extract_image(page) for page in self.doc]
