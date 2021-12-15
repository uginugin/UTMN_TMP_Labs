from ctypes import *
from ctypes import wintypes as w
from time import process_time
from string import ascii_letters 
from random import choice

INVALID_HANDLE_VALUE = w.HANDLE(-1).value
GENERIC_ALL = 0x10000000
OPEN_ALWAYS = 4
FILE_ATTRIBUTE_NORMAL = 0x80

_k32 = WinDLL('kernel32',use_last_error=True)
_CreateFileA = _k32.CreateFileA
_WriteFile = _k32.WriteFile
_ReadFile = _k32.ReadFile
_CloseHandle = _k32.CloseHandle


def createfile_python(filename, text):
    time_start = process_time()
    with open(filename, 'w') as f:
        f.write(text)
    return f"Запись с помощью python заняла {process_time()-time_start}"


def readfile_python(filename):
    time_start = process_time()
    with open(filename, 'r') as f:
        data = f.read()
    return f"Чтение с помощью python заняло {process_time()-time_start}"


def CreateFile(file_name='',data=''):
    file_handler = _CreateFileA(file_name,GENERIC_ALL,0,None,OPEN_ALWAYS,FILE_ATTRIBUTE_NORMAL,None)
    written = w.DWORD()
    try:
        _WriteFile(file_handler,data,len(data)*2,byref(written),None)
    finally:
        _CloseHandle(file_handler)

def ReadAFile(file_name=''):
    file_handler = _CreateFileA(file_name,GENERIC_ALL,0,None,OPEN_ALWAYS,FILE_ATTRIBUTE_NORMAL,None)
    data = create_string_buffer(26000000)
    read = w.DWORD()
    try:
        _ReadFile(file_handler,byref(data),1024,byref(read),None)
    finally:
        _CloseHandle(file_handler)

def createfile_k32(filename, text):
    time_start = process_time()
    CreateFile(filename, text)
    return f"Запись с помощью ctypes заняла {process_time()-time_start}"


def readfile_k32(filename):
    time_start = process_time()
    ReadAFile(filename)
    return f"Чтение с помощью ctypes заняло {process_time()-time_start}"


if __name__ == '__main__':
    text = ''
    for i in range(1000000):
        text += ''.join(choice(ascii_letters)for i in range(12))+'\n'
    print(createfile_k32('k', text))
    print(readfile_k32('k'))
    print(createfile_python('py.txt', text))
    print(readfile_python('py.txt'))