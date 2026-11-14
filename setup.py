# setup.py
from setuptools import setup

APP = ['main.py']
DATA_FILES = ['rhythms_db.py']
OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'icon.png',
    'plist': {
        'CFBundleName': 'Rhythm Master',
        'CFBundleDisplayName': 'Rhythm Master',
        'CFBundleGetInfoString': "Application for practicing and learning musical rhythms",
        'CFBundleIdentifier': "com.music.rhythmmaster",
        'CFBundleVersion': "1.0.0",
        'CFBundleShortVersionString': "1.0.0",
        'NSHighResolutionCapable': True,
    },
    "includes": [
        "_math_integer",
        "practice_data",
        "rhythms_db",
        "AVFoundation",
        "Foundation",
        "AppKit",
    ],
    "packages": ["AVFoundation", "Foundation", "AppKit", "objc"]
}

setup(
    app=APP,
    name='Rhythm Master',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
