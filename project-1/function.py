import uuid
import json
import sys
import os
import requests

def color(color="default", text=""):
    array_color = {
        'default': '0',
        'grey': '1;30',
        'red': '1;31',
        'green': '1;32',
        'yellow': '1;33',
        'blue': '1;34',
        'purple': '1;35',
        'nevy': '1;36',
        'white': '1;0',
    }
    
    return f"\033[{array_color.get(color, '0')}m{text}\033[0m"

def gen_uuid():
    return str(uuid.uuid4())

def save(data, filename):
    with open(filename, 'a') as file:
        file.write(data)

def sarep(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

def cek_file(nama_file):
    if os.path.exists(nama_file):
        a = True
    else:
        a = False
    return a


def retrieve_text(file_path, start, end):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        start -= 1 
        return ''.join(lines[start:end])
    
def get_file_token(file_name: str):
    with open(file_name, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines



def menu():
    print(color('green', "\n" * 2))
    print(color('green', "=" * 64))
    print(color('purple', "MENU") + color('green', "   **SHELL ASIA INDONESIA**"))
    print(color('green', "=" * 64))
    print(color('red', "[1]") + color('red', " Create "))
    print(color('blue', "[2]") + color('green', " Login "))
    print(color('blue', "[3]") + color('green', " Check "))
    print(color('red', "[4]") + color('red', " Logout"))
    print(color('red', "[5]") + color('red', " REGIST AKUN"))
    print(color('red', "[6]") + color('red', " REGIST AKUN"))
    print(color('red', "[7]") + color('red', " REGIST AKUN"))
    print(color('green', "=" * 64))
    pilih_menu = int(input(color('yellow', "PILIH : ")))

    if pilih_menu == 1:
        off()
    if pilih_menu == 2:
        login()
    if pilih_menu == 3:
        check()
    if pilih_menu == 4:
        off()
    if pilih_menu == 5:
        off()
    if pilih_menu == 6:
        off()
    if pilih_menu == 7:
        off()
    if pilih_menu >= 8:
        releases() 

    

def off():
    print(color('red', "FITUR OFF"))

def on():
    print(color('green', "FITUR ONLINE"))

def releases():
    print(color('red', "FITUR BELUM RELEASE"))


def get_token(nomor, device_id):
    url = "https://apac2-auth-api.capillarytech.com/auth/v1/token/generate"
    body = {"brand": "SHELLINDONESIALIVE", "mobile": nomor, "deviceId": device_id}
    headers = {
        "Host": "apac2-auth-api.capillarytech.com",
        "Content-Type": "application/json",
        "User-Agent": "ShellGoPlus%20Production/36 CFNetwork/1404.0.5 Darwin/22.3.0"
    }
    response = requests.post(url, json=body, headers=headers)

    return response.text

def generate_otp(nomor, device_id, session_id):
    url = "https://apac2-auth-api.capillarytech.com/auth/v1/otp/generate"
    body = {"deviceId": device_id, "sessionId": session_id, "mobile": nomor, "brand": "SHELLINDONESIALIVE"}
    headers = {
        "Host": "apac2-auth-api.capillarytech.com",
        "Content-Type": "application/json",
        "User-Agent": "ShellGoPlus%20Production/36 CFNetwork/1404.0.5 Darwin/22.3.0"
    }
    response = requests.post(url, json=body, headers=headers)
    
    return response.text

def verif_otp(nomor, device_id, session_id, otp):
    url = "https://apac2-auth-api.capillarytech.com/auth/v1/otp/validate"
    body = {"brand": "SHELLINDONESIALIVE","sessionId": session_id, "deviceId": device_id, "mobile": nomor, "otp": otp}
    headers = {
        "Host": "apac2-auth-api.capillarytech.com",
        "Content-Type": "application/json",
        "User-Agent": "ShellGoPlus%20Production/36 CFNetwork/1404.0.5 Darwin/22.3.0"
    }
    response = requests.post(url, json=body, headers=headers)
    return response.text


def cek_akun(nomor, device_id, token):
    url = "https://apac2-auth-api.capillarytech.com/mobile/v2/api/customer/get"
    headers = {
        "Host": "apac2-auth-api.capillarytech.com",
        "Content-Type": "application/json",
        "cap_mobile": nomor,
        "cap_authorization": token,
        "cap_device_Id": device_id,
        "cap_brand": "SHELLINDONESIALIVE",
        "User-Agent": "ShellGoPlus%20Production/36 CFNetwork/1404.0.5 Darwin/22.3.0"
    }
    response = requests.get(url, headers=headers)
    return response.text






def login():
    device_id = gen_uuid()
    print(color('green', "=" * 64))
    nomor = input(color('green', "\nNOMOR : +62"))
    nomor = "62" + nomor
    noken = get_token(nomor, device_id) ### GET TOKEN
    js_noken = json.loads(noken)
    success = js_noken["status"]["success"]
    if success != True:
            print(color('purple', f"\n\n{noken} get_token")) 
            sys.exit(1)
    if success == True:
            session_id = js_noken["user"]["sessionId"]
    ngotp = generate_otp(nomor, device_id, session_id) ### GET OTP
    js_ngotp = json.loads(ngotp)
    success = js_ngotp["status"]["success"]
    if success != True:
            print(color('purple', f"\n\n{ngotp} generate_otp"))
            sys.exit(1)
    if success == True:
            otp = input(color('green', "OTP   : "))
    meriv = verif_otp(nomor, device_id, session_id, otp) ### MERIF OTP
    js_meriv = json.loads(meriv)
    success = js_meriv["status"]["success"]
    print(color('green', "OTP VALID"))
    if success != True:
            print(color('purple', f"\n\n{meriv} verif_otp"))
            sys.exit(1)
    if success == True:
            token = js_meriv["auth"]["token"]
    cek = cek_akun(nomor, device_id, token) ### CEK AKUN
    js_cek = json.loads(cek)
    success = js_cek["status"]["success"]
    if success != "true":
            print(color('purple', f"\n\n{cek} cek_akun "))
            sys.exit(1)
    if success == "true":
            firstname = js_cek["customers"]["customer"][0]["firstname"]
            lastname = js_cek["customers"]["customer"][0]["lastname"]
            mobile = js_cek["customers"]["customer"][0]["mobile"]
            points = js_cek["customers"]["customer"][0]["loyalty_points"]
            dibuat = js_cek["customers"]["customer"][0]["registered_on"]
    print(color('green', f"NAMA   : ") + color('nevy', f"{firstname} {lastname}"))
    print(color('green', f"NOMOR  : ") + color('nevy', f"{mobile}"))
    print(color('green', f"POINTS : ") + color('nevy', f"{points}"))
    print(color('green', f"DIBUAT : ") + color('nevy', f"{dibuat}"))
    save(f"{mobile}\n", f"akunshell.txt")
    sarep(f"{nomor}:{device_id}:{token}", f"token/{nomor}.txt")
    print(color('green', f"AKUN TERSIMPAN DI FILE akunshell.txt"))
    print(color('green', "=" * 64))





def check():
    
    print(color('green', "=" * 64))
    files = input(color('green', "Input File : "))
    if cek_file(files) != True:
            print(color('red', "File Not Found"))
            check()
    if cek_file(files) == True:
        with open(files, 'r') as file:
                lines = file.readlines()
                data_list = [line.strip() for line in lines]
                no = 1
        for i, data in enumerate(data_list):
                print(f'[{no}] {data}')
                no += 1
                
    start = input(color('green', "\nStart : "))
    end = input(color('green', "End   : "))
    print(color('green', "=" * 64))
    result = retrieve_text(files, int(start), int(end))
    list_akun = result.strip().split('\n')

    akun = 1
    for data_akun in list_akun:
            if not data_akun:
                continue
    
            file_akun = get_file_token(f"token/{data_akun.split(':')[0]}.txt")
            pecah = file_akun[0].split(':')
            nomor = pecah[0].strip()
            device_id = pecah[1].strip()
            token = pecah[2].strip()
            cek = cek_akun(nomor, device_id, token) ### CEK AKUN
            js_cek = json.loads(cek)
            success = js_cek["status"]["success"]
            if success == "true":
#            print(color('purple', f"\n\n{cek} cek_akun "))
#            sys.exit(1)
                firstname = js_cek["customers"]["customer"][0]["firstname"]
                lastname = js_cek["customers"]["customer"][0]["lastname"]
                mobile = js_cek["customers"]["customer"][0]["mobile"]
                points = js_cek["customers"]["customer"][0]["loyalty_points"]
                dibuat = js_cek["customers"]["customer"][0]["registered_on"]
                
                print(color('yellow', f"AKUN KE: ") + color('yellow', f"{akun}"))
                print(color('green', f"NAMA   : ") + color('nevy', f"{firstname} {lastname}"))
                print(color('green', f"NOMOR  : ") + color('nevy', f"{mobile}"))
                print(color('green', f"POINTS : ") + color('nevy', f"{points}"))
                print(color('green', f"DIBUAT : ") + color('nevy', f"{dibuat}"))
                print(color('green', "=" * 64))
                akun += 1

def gen_uuid2():
    return str(uuid.uuid4())
