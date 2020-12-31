import os
import re
import glob

class FileFinder:
    path: str

    def __init__(self, basepath: str):
        self.path = basepath

    def find(self, files: list):
        if not isinstance(files,list):
            raise TypeError("files argument requires a list")

        found = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                for match in files:
                    if match == file:
                        found.append(os.path.join(dirpath,file))
        return found

    def search(self,files: list):
        if not isinstance(files,list):
            raise TypeError("files argument requires a list")

        found = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                for pattern in files:
                    if re.search(pattern,file):
                        found.append(os.path.join(dirpath,file))
        return found

    def glob(self, files: list):
        if not isinstance(files,list):
            raise TypeError("files argument requires a list")

        found = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for pattern in files:
                fullpathglob = os.path.join(dirpath,pattern)
                match = glob.glob(fullpathglob)
                if len(match) > 0:
                    found.extend(match)
        return found