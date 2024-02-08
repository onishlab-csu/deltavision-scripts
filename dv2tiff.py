#!/usr/bin/env python3
import sys
from mrc import DVFile
from tifffile import imwrite

# open with mrc.DVFile
with DVFile(sys.argv[1]) as dvfile:
    array = dvfile.asarray() # numpy array
    metadata = dvfile.hdr._asdict() # save header fields as metadata

# delete any "bytes" data, it is not transferable
for k in list(metadata.keys()):
    if isinstance(metadata[k], type(b'')): # "bytes type is not JSON serializable"
        del metadata[k]

# save tiff file
tif_filename = sys.argv[1].replace('.dv', '.tif')
imwrite(tif_filename, array, metadata=metadata)
print("wrote", tif_filename)
