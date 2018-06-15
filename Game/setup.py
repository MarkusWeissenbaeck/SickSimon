# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:53:14 2018

@author: Weissenbäck
"""
import sys
import os
sys.path.append(os.environ['PATH'])
import cx_Freeze

executables = [cx_Freeze.Executable("sick_sime.py",base="Win32GUI")]

os.environ['TCL_LIBRARY'] = r'C:\ProgramData\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\ProgramData\Anaconda3\tcl\tk8.6'

cx_Freeze.setup(
        name = "sick_Simon",
        options = {"build_exe": 
            {"packages":["pygame"],"include_files":["data/"], "includes":['numpy.core._methods', 'numpy.lib.format','tkinter']}},
        executables = executables,
        version="1.0.0"
        )
    

    
''' 
__version__ = "1.1.0"

include_files = ['logging.ini', 'config.ini', 'running.png']
excludes = ["tkinter"]
packages = ["os", "idna", "requests","json","base64","pyodbc"]

setup(
    name = "appname",
    description='App Description',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("b2b_conn.py",base="Win32GUI")]
)`
'''
'''
import sys
import os
sys.path.append(os.environ['PATH'])
from distutils.core import setup
import py2exe
setup(windows=['sick_sime.py'])
'''