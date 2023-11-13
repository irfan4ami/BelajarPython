data_in = input("Input Data: ")
data_out = input("Output Data: ")
try:
    with open(data_in, 'r') as file_input:
        isi_file = file_input.read()
        isi_file_modifikasi = isi_file.replace(';', ':')
        with open(data_out, 'w') as file_output:
            file_output.write(isi_file_modifikasi)

        print(f"Penggantian karakter ; ke : berhasil. Hasil disimpan di {data_out}")

except FileNotFoundError:
    print(f"File '{data_in}' tidak ditemukan.")

except Exception as e:
    print(f"Terjadi kesalahan: {(str(e))}")
