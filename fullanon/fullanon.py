#!/usr/bin/env python

import dicom
from PIL import Image

ds = dicom.read_file("/input/SCADXX0I.dcm")
for field_name in ds.dir("pat"):
    del ds[ds.data_element(field_name).tag]
ds.save_as("/output/Fred.dcm")
Image.fromarray(ds.pixel_array).convert('RGB').save("/output/Fred.png")
print(ds)
