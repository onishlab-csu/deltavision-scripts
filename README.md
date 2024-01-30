# deltavision-scripts
Scripts to work with deltavision files

## dv2tif.py

Use the mrc library to read the deltavision format, which is no longer an active company. The script transfers the deltavision header fields into the tiff metadata as well.

### required libraries

```
conda install -c conda-forge mrc tifffile
```

### usage

```
python dv2tiff.py dvfile.dv
```

That's all.
