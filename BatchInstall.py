#BatchInstall.py
#批安装python第三方库
import os
libs = {"numpy","matplotlib","pillow","sklearn","requests",\
		"beautifulsoup4","jieba","wheel","pyinstaller","django",\
		"flask","werobot","sympy","pandas","networkx",\
		"pyqt5","pyopengl","pypdf2","docopt","pygame"}	
try:
	for lib in libs:
		os.system("pip3 install " + lib)
	print("Successful installed ! ")
except:
	print("Failed somehow.")
	
"""	
Package         Version
--------------- ---------
altgraph        0.15
beautifulsoup4  4.6.0
bottle          0.12.13
certifi         2018.4.16
chardet         3.0.4
click           6.7
cycler          0.10.0
decorator       4.3.0
Django          2.0.5
docopt          0.6.2
et-xmlfile      1.0.1
Flask           1.0.2
future          0.16.0
idna            2.6
itsdangerous    0.24
jdcal           1.4
jieba           0.39
Jinja2          2.10
kiwisolver      1.0.1
macholib        1.9
MarkupSafe      1.0
matplotlib      2.2.2
mpmath          1.0.0
networkx        2.1
numpy           1.14.3
openpyxl        2.5.3
pefile          2017.11.5
Pillow          5.1.0
pip             10.0.1
pygame          1.9.3
PyInstaller     3.3.1
PyOpenGL        3.1.0
pyparsing       2.2.0
PyPDF2          1.26.0
pyperclip       1.6.0
pypiwin32       223
PyQt5           5.10.1
python-dateutil 2.7.3
pytz            2018.4
pywin32         223
requests        2.18.4
scikit-learn    0.19.1
selenium        3.12.0
Send2Trash      1.5.0
setuptools      28.8.0
sip             4.19.8
six             1.11.0
sklearn         0.0
sympy           1.1.1
UNKNOWN         0.0.0
urllib3         1.22
Werkzeug        0.14.1
WeRoBot         1.4.1
wheel           0.31.1
wordcloud       1.4.1
xmltodict       0.11.0
"""