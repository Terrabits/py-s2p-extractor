# Pyinstaller and Windows

```shell
# start with clean package list
pip install --upgrade pip setuptools

cd path/to/py-s2p-extractor
pip install lib/numpy-1.17.4+mkl-cp37-cp37m-win32.whl # or similar
pip install -e .[dev]
pyinstaller s2p-extractor.spec
```

[numpy+mkl builds](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

## Deprecation Warning

    c:\users\vm\appdata\local\programs\python\python37-32\lib\site-packages\PyInstaller\loader\pyimod03_importers.py:627: MatplotlibDeprecationWarning:
    The MATPLOTLIBDATA environment variable was deprecated in Matplotlib 3.1 and will be removed in 3.3.
    exec(bytecode, module.__dict__)
