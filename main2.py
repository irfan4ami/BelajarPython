nama_file_input = input("Input Data: ")
nama_file_output = input("Output Data: ")
try:
    with open(nama_file_input, 'r') as file_input:
        isi_file = file_input.read()
        isi_file_modifikasi = isi_file.replace(';', ':')
        with open(nama_file_output, 'w') as file_output:
            file_output.write(isi_file_modifikasi)

        print("Penggantian karakter ; ke : berhasil. Hasil disimpan di '{}'.".format(nama_file_output))

except FileNotFoundError:
    print("File '{}' tidak ditemukan.".format(nama_file_input))

except Exception as e:
    print("Terjadi kesalahan: {}".format(str(e)))
