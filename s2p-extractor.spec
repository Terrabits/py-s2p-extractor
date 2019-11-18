# -*- mode: python ; coding: utf-8 -*-

# Fix to get skrf required data folder included
# see https://github.com/scikit-rf/scikit-rf/issues/276
import os
import skrf as rf
datas = [
  (os.path.join(os.path.dirname(rf.__file__), 'data/*'), 'skrf/data/')
]

block_cipher = None


a = Analysis(['s2p_extractor/bin/s2p_extractor.py'],
             pathex=['s2p_extractor/bin'],
             binaries=[],
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
          name='s2p_extractor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
