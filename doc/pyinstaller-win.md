# Pyinstaller and Windows


## Directions

```shell
# start with clean package list
pip install --upgrade pip setuptools

cd path/to/py-s2p-extractor
pip install lib/numpy-1.17.4+mkl-cp37-cp37m-win32.whl # or similar
pip install -e .[dev]
pyinstaller s2p-extractor.spec
```

## Deprecation Warning

    c:\users\vm\appdata\local\programs\python\python37-32\lib\site-packages\PyInstaller\loader\pyimod03_importers.py:627: MatplotlibDeprecationWarning:
    The MATPLOTLIBDATA environment variable was deprecated in Matplotlib 3.1 and will be removed in 3.3.
    exec(bytecode, module.__dict__)

## References

- [download numpy+mkl wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
- [manually include mkl dlls with pyinstaller](https://stackoverflow.com/a/40539073/1390788)
- [resolve matplotlib gui lib type issues to 'agg'](https://github.com/ufoym/deepo/issues/17)
