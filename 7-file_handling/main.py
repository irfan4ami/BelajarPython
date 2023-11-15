import function
import os


file = input("\n\ninput file : ")
cek_file = function.cek_file(file)

if cek_file == True:
    print(f"\nFILE ADA")
    os.remove(file) #MENGHAPUS FILE
    print(f"DAN SUDAH DI HAPUS")
elif cek_file == False:
    print(f"\nFILE TIDAK ADA")
    with open(file, 'a') as filenya:
        filenya.write('test\n')
        filenya.write('test\n')
        filenya.write('test\n')
    print(f"DAN SUDAH DI BUAT {file}")
else:        
    print(f"\nERROR TAK TERDUGA")

