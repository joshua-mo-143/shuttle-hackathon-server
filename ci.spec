# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

hook_path = os.path.abspath('./hooks')  # Directory where your custom hook is located

a = Analysis(['app.py'],
             pathex=['.'],
             binaries=[],
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
          [],
          exclude_binaries=True,
          name='shuttle_ai_poc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
	  icon=None,
	  onefile=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='shuttle_hackathon_server')
