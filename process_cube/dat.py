import os
from process_cube.header import Header
import numpy as np

def read_dat_file(filename, header: Header=None):
    if header is None:
        header_filename = os.path.splitext(filename)[0] + ".hdr"
        header = Header.read_header(header_filename)
    data = np.fromfile(filename, dtype=header.numpy_type)
    if header.interleave == "bsq":
        return data.reshape(header.bands, header.samples, header.lines).swapaxes(0,2)
    if header.interleave == "bil":
        return data.reshape(header.lines, header.bands, header.samples).swapaxes(1,2)
    else:
        raise NotImplementedError("Other interleaves not implemented: " + header.interleave)