import os
import platform
os.system('clear')
os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    __import__("MR-MAHIN").menu()
    
elif b == '32bit':
    print(" 32 BIT WILL AVAILABLE SOON ")
