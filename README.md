[![](https://img.shields.io/pypi/pyversions/touch.svg?longCache=True)](https://pypi.org/pypi/touch/)
[![](https://img.shields.io/pypi/v/touch.svg?maxAge=3600)](https://pypi.org/pypi/touch/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/touch.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/touch.py/)

#### Install
```bash
$ [sudo] pip install touch
```

#### Functions
function|description
-|-
`touch.touch(path)`|mkdir + touch path(s)

#### Examples
```python
>>> import touch
>>> touch.touch("path/to/file")
>>> touch.touch(["path/to/file1","path/to/file2"])
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>