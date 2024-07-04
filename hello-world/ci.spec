# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

hook_path = os.path.abspath('./hooks')  # Directory where your custom hook is located

a = Analysis(['./app/__init__.py'],
             pathex=['./app'],
             binaries=[],
             runtime_hooks=[],
             hookspath=[hook_path],
             excludes=[],
             datas=[('./app/templates', 'templates')],
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
               name='app')
