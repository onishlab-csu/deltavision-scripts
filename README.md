# deltavision-scripts
Scripts to work with deltavision files

## dv2tiff.py

Quick script by David to just open a dv file and save as tiff.

### details

Uses the [mrc](https://github.com/tlambert03/mrc) library to read the deltavision format, which is no longer an active company. The script transfers the deltavision header fields into the tiff metadata as well.

### required libraries

```
conda install -c conda-forge mrc tifffile
```

### usage

```
python dv2tiff.py dvfile.dv
```

That's all.
