#!/usr/bin/env python3
import sys
from mrc import DVFile
from tifffile import imwrite

with DVFile(sys.argv[1]) as dvfile:
    array = dvfile.asarray()
    metadata = dvfile.hdr._asdict()

for k in list(metadata.keys()):
    if isinstance(metadata[k], type(b'')): # "bytes type is not JSON serializable"
        del metadata[k]

tif_filename = sys.argv[1].replace('.dv', '.tif')

imwrite(tif_filename, array, metadata=metadata)
print("wrote", tif_filename)
