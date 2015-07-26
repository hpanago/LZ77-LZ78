#!/bin/bash

python lz78.py senior
ls -lh1 senior senior.lz78
python decompression78.py senior.lz78 
md5sum senior senior.decompressed78
