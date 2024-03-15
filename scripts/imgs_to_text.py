# import os
# from typing import List
# import pytesseract

# import cv2

import argparse
from pathlib import Path 
from typing import List

from oppy.utils.io import get_fs
from oppy.img.process import Image
from oppy.ocr.tesseract import ocr



def extract_text_from_image(image_path, lang) -> str:
    print(image_path)
    image = Image.read_image(image_path)
    (image.to_grayscale()
     .denoise_adaptive())
    return ocr(image, lang)



def extract_text(args) -> List[str]:
    fs = get_fs(args.images_dir)
    for pdf_dir in fs.list_dirs():
        for image_path in sorted(fs.list_files(pdf_dir, args.format), 
                            key=lambda file_name: int(Path(file_name).stem[len("img"):])):
            print(extract_text_from_image(image_path, args.language))
            break
        break
    

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="OCR", description="Script for extracting text from jpeg files"
    )

    parser.add_argument("images_dir")
    parser.add_argument("language")
    parser.add_argument("output_file")
    parser.add_argument(
        "-f", "--format", default="jpg", choices=["jpg", "png"]
    )
    parser.add_argument("-b", "--blur", action="store_true")
    parser.add_argument("-d", "--denoise", action="store_true")
    parser.add_argument("-a", "--adaptive_denoise", action="store_true")
    args = parser.parse_args()

    texts = extract_text(args)
    # with open(args.output_file, "w") as f:
    #     for text in texts:
    #         f.write(text)


if __name__ == "__main__":
    main()
