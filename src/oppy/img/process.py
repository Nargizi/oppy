from __future__ import annotations
import cv2
from dataclasses import dataclass


@dataclass
class Image:
    image: cv2.Mat

    @classmethod
    def read_image(cls, image_path: str) -> Image:
        return cls(cv2.imread(image_path))
    
    def to_grayscale(self) -> Image:
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return self

    def blur(self) -> Image:
        self.image = cv2.GaussianBlur(self.image, (5, 5), 0)
        return self

    def denoise(self) -> Image:
        _, self.image = cv2.threshold(self.image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return self

    def denoise_adaptive(self) -> Image:
        self.image =  cv2.adaptiveThreshold(
            self.image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 19
        )
        return self

