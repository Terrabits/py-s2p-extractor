# -*- mode: python ; coding: utf-8 -*-

# Fix to get skrf required data folder included
# see https://github.com/scikit-rf/scikit-rf/issues/276
import os
import skrf as rf
datas = [
  (os.path.join(os.path.dirname(rf.__file__), 'data/*'), 'skrf/data/')
]

block_cipher = None

# including MKL
# https://stackoverflow.com/a/40539073/1390788
mkl_dlls = [(r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_avx.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_avx2.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_avx512.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_core.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_intel_thread.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_p4.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_p4m.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_p4m3.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_rt.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_sequential.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_tbb_thread.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_vml_avx.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_vml_avx2.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_vml_avx512.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_vml_cmpt.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_vml_ia.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_vml_p4.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_vml_p4m.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_vml_p4m2.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\mkl_vml_p4m3.dll', '.'),
 (r'C:\Users\vm\AppData\Local\Programs\Python\Python37-32\lib\site-packages\numpy\DLLs\libiomp5md.dll', '.')]

a = Analysis(['s2p_extractor/bin/s2p_extractor.py'],
             pathex=['s2p_extractor/bin'],
             binaries=mkl_dlls,
             datas=datas,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='s2p-extractor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
