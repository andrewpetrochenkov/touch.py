#!/usr/bin/env python
import os
from touch import touch

path = "~/testtest"
fullpath = path.replace("~", os.environ["HOME"])
touch("~/testtest")  # fullpath
os.unlink(fullpath)
