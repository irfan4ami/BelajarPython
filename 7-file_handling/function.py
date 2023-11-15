import os

def cek_file(nama_file):
    if os.path.exists(nama_file):
        a = True
    else:
        a = False
    return a


