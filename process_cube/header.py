from io import StringIO
from dataclasses import dataclass
import numpy as np

@dataclass
class Header:
    samples: int
    lines: int
    bands: int
    data_type: int
    interleave: str

    @classmethod
    def read_header(cls, filename):
        with open(filename) as f:
            return cls.parse_header(f)

    @classmethod
    def parse_header(cls, file: StringIO):
        sections = {}
        for line in file.readlines():
            split = line.split("=")
            if len(split) != 2:
                continue
            header, value = map(lambda s: s.strip(), split)

            if header in ["samples", 'lines', "bands", "data type"]:
                sections[header.replace(" ", "_")] = int(value)
            if header == "interleave":
                sections[header] = value
        return cls(**sections)

    @property
    def numpy_type(self,):
        if self.data_type == 1:
            return np.uint8
        if self.data_type == 2:
            return np.short
        if self.data_type == 3:
            return np.uint
        if self.data_type == 4:
            return np.float32
