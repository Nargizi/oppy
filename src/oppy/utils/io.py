from typing import List

from fsspec.core import url_to_fs
from fsspec.implementations.dirfs import DirFileSystem


class DataFileSystem(DirFileSystem):

    def list_files(self, path: str = "", ext: str = "") -> List[str]:
        return [self._join(file['name']) for file in self.listdir(path) if file['type'] == 'file' and file['name'].endswith(ext)]

    def list_dirs(self, path: str = "") -> List[str]:
        return [dir['name'] for dir in self.listdir(path) if dir['type'] == 'directory']


def get_fs(path: str) -> DataFileSystem:
    return DataFileSystem(*url_to_fs(path)[::-1])
