import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_object = None

    def __enter__(self) -> "CleanUpFile":
        self.file_object = open(self.filename, "a")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.filename:
            self.file_object.close()
            os.remove(self.filename)
