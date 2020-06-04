# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


# This work-around is required until
# pyinstaller releases this fix:
# https://github.com/pyinstaller/pyinstaller/commit/91481570517707fc70aa70dca9eb986c61eac35d#diff-dc99be50fd6e9451bec5c3e6c135c4b9
hiddenimports = ['pkg_resources.py2_warn']


hookspath = ['pyinstaller-hooks']


a = Analysis(['s2p_extractor/bin/s2p_extractor.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=hiddenimports,
             hookspath=hookspath,
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)


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
          runtime_tmpdir=None,
          console=True,
          icon='images/RS.ico')
