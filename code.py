import os, sys
os.system("git pull")
try:
    __import__("OBFHARD")
except Exception as e:
    exit(str(e))