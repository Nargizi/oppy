
import argparse
from pathlib import Path 
from typing import List

from oppy.utils.io import get_fs
from oppy.img.process import Image
from oppy.text.process import Texts, SplitWordProcessor, FrakturProcessor
from oppy.ocr.tesseract import ocr



def extract_text_from_image(image_path, lang) -> str:
    print(image_path)
    image = Image.read_image(image_path)
    (image.to_grayscale()
     .denoise())
    return ocr(image, lang)



def extract_text(args) -> Texts:
    fs = get_fs(args.images_dir)
    doc = Texts()
    doc.add_processor(SplitWordProcessor())
    if args.language == 'frk':
        doc.add_processor(FrakturProcessor())
    for image_path in sorted(fs.list_files(ext=args.format), 
                             key=lambda file_name: int(Path(file_name).stem[len("img"):]))[:20]:
        doc.texts.append(extract_text_from_image(image_path, args.language))
    return doc

    

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
    fs_out = get_fs(args.output_file)
    file_name = Path(args.images_dir).stem + ".txt"
    fs_out.touch(file_name)
    with fs_out.open(file_name, "w") as f:
        f.write(texts.process())



if __name__ == "__main__":
    main()
