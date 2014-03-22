# -*- mode: python -*-
a = Analysis(['exec.py'],
             pathex=['C:\\Apps\\google-python-exercises\\pranky\\PyInstaller-2.1\\exec'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='exec.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
