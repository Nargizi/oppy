from pathlib import Path 
import argparse
from oppy.utils.io import get_fs
from oppy.pdf.pdf import PDF

def extract_images(pdf_path: str, format: str, dir: str):
    pdf = PDF.open(pdf_path)
    for idx, img in enumerate(pdf.to_imgs()):
        img.save(Path(dir).joinpath(f"img{idx}.{format}"))
        

def process_pdfs(args):
    pdf_fs = get_fs(args.pdfs_path)
    out_fs = get_fs(args.output_dir)
    for pdf_path in pdf_fs.list_files(ext='pdf'):
        file_name = Path(pdf_path).stem
        out_fs.mkdir(file_name, exist_ok=True)
        extract_images(pdf_path, args.format,out_fs._join(file_name))


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="PDFImageExtractor",
        description="Script for extracting images from pdf files",
    )

    parser.add_argument("pdfs_path")
    parser.add_argument("output_dir")
    parser.add_argument(
        "-f", "--format", default="jpg", choices=["jpg", "png"]
    )  # option that takes a value
    parser.add_argument("-z", "--zoom", default=5)
    args = parser.parse_args()

    process_pdfs(args)


if __name__ == "__main__":
    main()
