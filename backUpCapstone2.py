from tabulate import tabulate
import os
import re
from colorama import Fore, Back, Style
import datetime

dataKaryawan = [{
    'IdKar': 'K001',
    'Nama': 'Yusrina',
    'Jabatan': 'Manajer',
    'Departemen': 'Marketing',  
    'SisaCuti': 10,
},
{
    'IdKar': 'K002',
    'Nama': 'Veny',
    'Jabatan': 'Administrasi',
    'Departemen': 'Marketing',
    'SisaCuti': 12,
},
{
    'IdKar': 'K003',
    'Nama': 'Niken',
    'Jabatan': 'Supervisor',
    'Departemen': 'Keuangan',
    'SisaCuti': 12,
},
{
    'IdKar': 'K004',
    'Nama': 'Rino',
    'Jabatan': 'Administrasi',
    'Departemen': 'Keuangan',
    'SisaCuti': 0,
},]

dataCuti = [
    {
        'IdCuti' : 'C001',
        'IdKar' : 'K001',
        'Nama' : 'Yusrina',
        'jumlahHari' : 2,
        'TanggalCuti' : '2023-01-01',
        'Keterangan' : 'ada keperluan keluarga'
    },
]

def templateNotifDataNotFound():
    #use colorama for color text
    print(Back.RED + Fore.WHITE + 'Data Tidak Ada' + Style.RESET_ALL)
    

def templateNotifWrongInput():
    #use colorama for color text
    print(Back.RED + Fore.WHITE + 'Pilihan yang anda Masukkan Salah' + Style.RESET_ALL)

def TemplateNotifWrongIdKar():
    print(Back.RED + Fore.WHITE + 'IdKar Tidak Ada' + Style.RESET_ALL)

def TemplateNotifInputWithNumber():
    print(Back.RED + Fore.WHITE + 'Nama yang anda masukkan mengandung angka' + Style.RESET_ALL)

def TemplateShowIdKarAndNama():
    table = [[karyawan["IdKar"], karyawan["Nama"]] for karyawan in dataKaryawan]
    print(tabulate(table, headers=('IdKar', 'Nama'), tablefmt="fancy_grid"))

def templateDataMustBeFilled():
    print(Back.RED + Fore.WHITE + 'Data Tidak Boleh Kosong' + Style.RESET_ALL)
    

    
#dajsdjsa
#laporan data karyawan
def laporanMenu():
        print('''
        ---------------------------------------
        Laporan Data Karyawan PT Power Telecom  :
        ---------------------------------------
        1. Laporan Seluruh Data Karyawan
        2. Laporan Data Karyawan By ID
        3. Filter Data Karyawan Berdasarkan Departemen
        4. Kembali ke Menu Utama
        ''')
        try:
            
            inputLaporan = int(input('Silahkan Pilih Sub Menu Laporan Data Karyawan (1-4): '))
        except ValueError:
            templateNotifWrongInput()
            
        
            


        if inputLaporan == 1:
            if len(dataKaryawan) == 0:
                templateNotifDataNotFound()
                laporanMenu()
            else:
                print('Laporan Seluruh Data Karyawan')
                print("---------------------------------------")
                print(tabulate(dataKaryawan, headers='keys', tablefmt='fancy_grid'))
                

        elif inputLaporan == 2:
            TemplateShowIdKarAndNama()

            Laporan2 = (input('Masukkan IdKar: ')).capitalize()
            print(f'Data Karyawan dengan IdKar: {Laporan2}')


            for i,j in enumerate (dataKaryawan) :
                if Laporan2 == j['IdKar'] :
                    for k in dataKaryawan:
                        if Laporan2 == k['IdKar']:
                            # print table  tabulate 
                            # print(tabulate(k, headers='keys', tablefmt='fancy_grid'))
                            print(tabulate([k.values()], headers=k.keys(), tablefmt='fancy_grid'))
                            # print('{}\t| {}  \t| {}\t| {}'.format(k['IdKar'],k['Nama'],k['Jabatan'],k['Departemen']))
                            laporanMenu()


                elif Laporan2 != j['IdKar'] and (i == len(dataKaryawan)-1):
                    templateNotifDataNotFound()
                    laporanMenu()            

        elif inputLaporan == 3:
            inputFilter = (input('Masukkan Departemen: ')).capitalize()
            print(f'Data Karyawan dengan Departemen: {inputFilter}')
            print("-----------------------------------------------------------------")
            print("IdKar\t| Nama\t\t| Jabatan\t| Departemen")
            print("-----------------------------------------------------------------")
            for i,j in enumerate(dataKaryawan) :
                if inputFilter == j['Departemen'] :
                    for k in dataKaryawan:
                        if inputFilter == k['Departemen']:
                            print('{}\t| {}  \t| {}\t| {}'.format(k['IdKar'],k['Nama'],k['Jabatan'],k['Departemen']))
                            # print(tabulate([k.values()], headers=k.keys, tablefmt='fancy_grid'))
                    
                    break

                elif inputFilter != j['Departemen'] and (i == len(dataKaryawan)-1):
                    templateNotifDataNotFound()
                    break
        elif inputLaporan == 4:
            return
        
        else:
            templateNotifWrongInput()
            laporanMenu()

def buatIdKar():
    if len(dataKaryawan) == 0:
        return 'K001'
    else:
        return 'K00' + str(len(dataKaryawan)+1)

#tambah data karyawan menu
def tambahMenu():
        print('''
        ---------------------------------------
        Tambah Data Karyawan :
        ---------------------------------------
        1. Tambah Data Karyawan
        2. Kembali ke Menu Utama
        ''')
        try:
            inputTambah = int(input('Silahkan Pilih Sub Menu Tambah Data Karyawan (1-2): '))
        except ValueError:
            templateNotifWrongInput()
            return tambahMenu()
        


        if inputTambah == 1:
            inputIdKar = buatIdKar()
            # inputNamaDepan = (input('Masukkan Nama Depan: ')).capitalize()
            # inputNamaBelakang = (input('Masukkan Nama Belakang: ')).capitalize()
            inputNama = (input('Masukan Nama : '))
            if inputNama == '':
                templateDataMustBeFilled()
                return tambahMenu()
                
            else:
                if re.search(r'\d', inputNama) is None:
                    tambahJabatan = (input('Masukkan Jabatan: ')).capitalize()
                    if tambahJabatan == '':
                        templateDataMustBeFilled()
                        return tambahMenu()
                    else:
                        tambahDepartemen = (input('Masukkan Departemen: ')).capitalize()
                        if tambahDepartemen == '':
                            templateDataMustBeFilled()
                            return tambahMenu()
                        else:
                            dataKaryawan.append({
                                'IdKar' : inputIdKar,
                                'Nama' : inputNama,
                                'Jabatan' : tambahJabatan,
                                'Departemen' : tambahDepartemen,
                                'SisaCuti' : 0
                            })
                            print(Fore.GREEN + 'Data Karyawan Berhasil Ditambahkan' + Style.RESET_ALL)
                            print("---------------------------------------")
                            #print only added data
                            print(tabulate(dataKaryawan[-1:], headers='keys', tablefmt='fancy_grid'))
                            return tambahMenu()
                else:
                    TemplateNotifInputWithNumber()
                    return tambahMenu()

                
                
                
                
    
            

#update data karyawan menu
def updateMenu():
    while True:
        
        print('''
        ---------------------------------------
        Update Data Karyawan :
        ---------------------------------------
        1. Update Data Karyawan (Semua Data)
        2. Update Data Karyawan Hanya Nama
        3. Update Data Karyawan Hanya Jabatan
        4. Update Data Karyawan Hanya Departemen
        5. Kembali ke Menu Utama
        ''')
        try:
            inputUpdate = int(input('Silahkan Pilih Sub Menu Update Data Karyawan (1-5): '))
        except ValueError:
            templateNotifWrongInput()
            continue
        


        if inputUpdate == 1:
            TemplateShowIdKarAndNama()

            inputIdKar = (input('Masukkan IdKar: ')).capitalize()
            if inputIdKar == '':
                TemplateNotifWrongIdKar()
                continue

            for k in dataKaryawan:
                if k['IdKar'] == inputIdKar:
                    # inputNamaDepan = (input('Masukkan Nama Depan: ')).capitalize()
                    # inputNamaBelakang = (input('Masukkan Nama Belakang: ')).capitalize()
                    inputNama = (input('Masukan Nama : '))
                    #validasi nama kosong
                    if inputNama == '':
                        templateDataMustBeFilled()
                        break
                    else:  
                        if re.search(r'\d', inputNama) is None:
                            tambahJabatan = (input('Masukkan Jabatan: ')).capitalize()
                            #validasi jabatan kosong
                            if tambahJabatan == '':
                                templateDataMustBeFilled()
                                return updateMenu()
                            else:
                                tambahDepartemen = (input('Masukkan Departemen: ')).capitalize()
                                if tambahDepartemen == '':
                                    templateDataMustBeFilled()
                                    return updateMenu()
                                else:
                                    k['Nama'] = inputNama
                                    k['Jabatan'] = tambahJabatan
                                    k['Departemen'] = tambahDepartemen
                                    
                                # k['SisaCuti'] = SisaCuti

                            break

                        
                    
                    #validasi input nama tidak boleh angka menggunakan regex

            else:
                TemplateNotifWrongIdKar()
                continue

        elif inputUpdate == 2:
            TemplateShowIdKarAndNama()

            inputIdKar = (input('Masukkan IdKar: ')).capitalize()
            if inputIdKar == '':
                TemplateNotifWrongIdKar()
                continue

            for k in dataKaryawan:
                if k['IdKar'] == inputIdKar:
                    # inputNamaDepan = (input('Masukkan Nama Depan: ')).capitalize()
                    # inputNamaBelakang = (input('Masukkan Nama Belakang: ')).capitalize()
                    inputNama = (input('Masukan Nama : '))
                    if inputNama == '':
                        templateDataMustBeFilled()
                        return updateMenu()
                    else:                    
                        if re.search(r'\d', inputNama) is None:
                            k['Nama'] = inputNama

                            print('Data Karyawan Berhasil Diupdate')
                            print("---------------------------------------")
                            #print only updated data
                            print(tabulate([k.values()], headers=k.keys(), tablefmt='fancy_grid'))

                            break
                        else:
                            TemplateNotifInputWithNumber()
                            break

            else:
                TemplateNotifWrongIdKar()
                continue

        elif inputUpdate == 3:
            TemplateShowIdKarAndNama()

            inputIdKar = (input('Masukkan IdKar: ')).capitalize()
            if inputIdKar == '':
                TemplateNotifWrongIdKar()
                continue

            for k in dataKaryawan:
                if k['IdKar'] == inputIdKar:
                    tambahJabatan = (input('Masukkan Jabatan: ')).capitalize()
                    if tambahJabatan == '':
                        templateDataMustBeFilled()
                        return updateMenu()
                    else:
                        k['Jabatan'] = tambahJabatan

                        print('Data Karyawan Berhasil Diupdate')
                        print("---------------------------------------")
                        #print only updated data
                        print(tabulate([k.values()], headers=k.keys(), tablefmt='fancy_grid'))

                        break

            else:
                TemplateNotifWrongIdKar()
                continue

        elif inputUpdate == 4:
            TemplateShowIdKarAndNama()

            inputIdKar = (input('Masukkan IdKar: ')).capitalize()
            if inputIdKar == '':
                TemplateNotifWrongIdKar()
                continue

            for k in dataKaryawan:
                if k['IdKar'] == inputIdKar:
                    tambahDepartemen = (input('Masukkan Departemen: ')).capitalize()
                    if tambahDepartemen == '':
                        templateDataMustBeFilled()
                        return updateMenu()
                    else:
                        
                        k['Departemen'] = tambahDepartemen

                        print('Data Karyawan Berhasil Diupdate')
                        print("---------------------------------------")
                        #print only updated data
                        print(tabulate([k.values()], headers=k.keys(), tablefmt='fancy_grid'))

                        break

            else:
                TemplateNotifWrongIdKar()
                continue

        elif inputUpdate == 5:
            break

        else:
            templateNotifWrongInput()
            updateMenu()





        

        
            

                    
def hapusMenu():
    while True:
        print('''
        ---------------------------------------
        Hapus Data Karyawan :
        ---------------------------------------
        1. Hapus Data Karyawan
        2. Kembali ke Menu Utama
        ''')
        try:
            
            inputHapus = int(input('Silahkan Pilih Sub Menu Hapus Data Karyawan (1-2): '))
        except ValueError:
            templateNotifWrongInput()
            continue
            

        if inputHapus == 1:
            TemplateShowIdKarAndNama()

            inputIdKar = (input('Masukkan IdKar: ')).capitalize()
            if inputIdKar == '':
                TemplateNotifWrongIdKar()
                continue
            elif inputIdKar in [i['IdKar'] for i in dataKaryawan]:
                print('Apakah anda ingin menghapus data karyawan?')
                inputHapus2 = input('Y/n: ')
                if inputHapus2 == 'Y':
                    for key in dataKaryawan:
                        if inputIdKar == key['IdKar']:
                            dataKaryawan.remove(key)
                            print(Fore.GREEN + 'Data Karyawan Berhasil Dihapus' + Style.RESET_ALL)
                            print("---------------------------------------")
                            print(tabulate(dataKaryawan, headers='keys', tablefmt='fancy_grid'))
                            return hapusMenu()
                elif inputHapus2 == 'n':
                    return hapusMenu()
                else:
                    print('Pilihan yang anda Masukkan Salah')
                    continue
            elif inputIdKar not in [i['IdKar'] for i in dataKaryawan]:
                TemplateNotifWrongIdKar()
                continue
        elif inputHapus == 2:
            break
        else:
            templateNotifWrongInput()
            continue
    
def clearCli():
        print('''
        ---------------------------------------
        Clear Cli :
        ---------------------------------------
        1. Clear Cli
        2. Kembali ke Menu Utama
        ''')
        try:
            inputClear = int(input('Silahkan Pilih Sub Menu Clear Cli (1-2): '))
        except ValueError:
            templateNotifWrongInput()
            return clearCli()

            if inputClear == 1:
                os.system('clear')
                print(Fore.GREEN + 'Cli Berhasil Diclear' + Style.RESET_ALL)
                return
            elif inputClear == 2:
                return                
            


        
    
def clearAll():
        print('''
        ---------------------------------------
        Clear All Data Karyawan :
        ---------------------------------------
        1. Clear All Data Karyawan
        2. Clear All Data Cuti
        3. Kembali ke Menu Utama
        ''')

        try:
            inputClearAll = int(input('Silahkan Pilih Sub Menu Clear All Data Karyawan (1-3): '))
        except:
            templateNotifWrongInput()
            return clearAll()
        if inputClearAll == 1:
            try:
                inputValidasi = input('Apakah anda ingin menghapus data karyawan? Y/n: ')
            except:
                templateNotifWrongInput()
                return clearAll()
            # inputValidasi = input('Apakah anda ingin menghapus data karyawan? Y/n: ')
            if inputValidasi == 'Y':
                dataKaryawan.clear()
                print(Fore.GREEN + 'Data Karyawan Berhasil Diclear' + Style.RESET_ALL)
                return
            elif inputValidasi == 'n':
                clearAll()
            
        elif inputClearAll == 2:
            dataCuti.clear()
            inputValidasi = input('Apakah anda ingin menghapus data karyawan? Y/n: ')
            if inputValidasi == 'Y':
                dataKaryawan.clear()
                print(Fore.GREEN + 'Data Karyawan Berhasil Diclear' + Style.RESET_ALL)
                return
            elif inputValidasi == 'n':
                return clearAll()
            # print('Data Cuti Berhasil Diclear')
            
        # elif inputClearAll == 2:
        #     break
        elif inputClearAll == 3:
            return
        else:
            templateNotifWrongInput()
            return clearAll()


def buatIdCuti():

    if len(dataCuti) == 0:
        return 'C001'
    else:
        return 'C00' + str(len(dataCuti)+1)

def sistemCuti():
    while True:
        print('''
        ---------------------------------------
        Sistem Cuti Karyawan :
        ---------------------------------------
        1. Sistem Cuti Karyawan
        2. Laporan Data Cuti
        3. Update Data Cuti
        4. Kembali ke Menu Utama
        ''')
        # TemplateShowIdKarAndNama()
        try:
                inputCuti = int(input('Silahkan Pilih Sub Menu Sistem Cuti Karyawan (1-4): '))
        except ValueError:
            templateNotifWrongInput()

            

        # inputCuti = int(input('Silahkan Pilih Sub Menu Sistem Cuti Karyawan (1-4: '))

        if inputCuti == 1:
            TemplateShowIdKarAndNama()
            inputIdKar = (input('Masukkan IdKar: ')).capitalize()
            if inputIdKar == '':
                TemplateNotifWrongIdKar()
                continue
            elif inputIdKar in [i['IdKar'] for i in dataKaryawan]:
                # print('IdKar Sudah Ada')
                print('Apakah anda ingin input pengajuan cuti?')
                inputCuti2 = input('Y/n: ')
                if inputCuti2 == 'Y':
                    for key in dataKaryawan:
                        if inputIdKar == key['IdKar']:
                            inputJumlahHari = int(input('Masukkan Jumlah Hari: '))
                            if inputJumlahHari > key['SisaCuti']:
                                print(Back.RED + Fore.WHITE + 'Jumlah Hari Tidak Boleh Lebih Dari Sisa Cuti' + Style.RESET_ALL)
                                continue
                            elif inputJumlahHari <= 0:
                                print('Jumlah Hari Tidak Boleh 0 atau Kurang Dari 0')
                                continue
                            elif inputJumlahHari <= key['SisaCuti']:
                                print('contoh inputan yang benar "2023-12-12"')
                                inputTanggalCuti = (input('Masukkan Tanggal Cuti Y/M/D: '))
                                #validasi tanggal cuti kosong
                                if inputTanggalCuti == '':
                                    templateDataMustBeFilled()
                                    continue
                                else:
                                    #validasi tanggal cuti harus angka datetime
                                    try:
                                        datetime.datetime.strptime(inputTanggalCuti, '%Y-%m-%d')
                                    except ValueError:
                                        print(Back.RED + Fore.WHITE + 'Format Tanggal Cuti Salah' + Style.RESET_ALL)
                                        continue
                                    inputKeterangan = (input('Masukkan Keterangan: '))
                                    dataCuti.append({
                                        'IdCuti' : buatIdCuti(),
                                        'IdKar' : inputIdKar,
                                        'Nama' : key['Nama'],
                                        'jumlahHari' : inputJumlahHari,
                                        'TanggalCuti' : inputTanggalCuti,
                                        'Keterangan' : inputKeterangan
                                    })
                                    penguranganCuti = key['SisaCuti'] - inputJumlahHari  
                                    key['SisaCuti'] = penguranganCuti      

                                    print(Fore.GREEN + 'Data Cuti Berhasil Ditambahkan' + Style.RESET_ALL )
                                    print("---------------------------------------")
                                    #print only added data
                                    print(tabulate(dataCuti[-1:], headers='keys', tablefmt='fancy_grid'))
                                    break
                                
                elif inputCuti2 == 'n':
                    sistemCuti()
                    
                else:
                    templateNotifWrongInput()
                    continue
            elif inputIdKar not in [i['IdKar'] for i in dataKaryawan]:
                TemplateNotifWrongIdKar()
                continue
        elif inputCuti == 2:
            print('Laporan Data Cuti')
            print("---------------------------------------")
            print(tabulate(dataCuti, headers='keys', tablefmt='fancy_grid'))
            continue
        elif inputCuti == 3:
            print('Update Data Cuti')
            print("---------------------------------------")
            table = [[karyawan["IdKar"], karyawan["Nama"], karyawan['SisaCuti']] for karyawan in dataKaryawan]
            # print(tabulate(table, headers=('IdKar', 'Nama'), tablefmt="fancy_grid"))

            print(tabulate(table, headers=('IdKar', 'Nama', 'Sisa Cuti'), tablefmt="fancy_grid"))

            inputIdKar = (input('Masukkan IdKar: ')).capitalize()
            try:

                if inputIdKar == '':
                    TemplateNotifWrongIdKar()
                    continue
                elif inputIdKar in [i['IdKar'] for i in dataKaryawan]:
                    inputValidasi = input('Apakah anda ingin mengupdate data cuti? Y/n: ')
                    if inputValidasi == 'Y':
                        for key in dataKaryawan:
                            if inputIdKar == key['IdKar']:
                                inputJumlahHari = input('Masukkan Jumlah Hari: ')
                                if inputJumlahHari == '':
                                    print(Fore.RED + 'Jumlah Hari Tidak Boleh Kosong' + Style.RESET_ALL)
                                    continue
                                elif inputJumlahHari.isalpha():
                                    print(Fore.RED + 'Jumlah Hari Harus Angka' + Style.RESET_ALL)
                                    continue
                                else: 
                                    key['SisaCuti'] = inputJumlahHari
                                    print(Fore.GREEN + 'Data Cuti Berhasil Diupdate' + Style.RESET_ALL)
                                    print("---------------------------------------")
                                    #print only updated data IdKar, Nama, Jabatan, Departemen
                                    print(tabulate([key], headers='keys', tablefmt='fancy_grid'))
                                    break
                    elif inputValidasi == 'n':
                        sistemCuti()
                    else:
                        templateNotifWrongInput()
                        continue
                elif inputIdKar not in [i['IdKar'] for i in dataKaryawan]:
                    TemplateNotifWrongIdKar()
                    continue
            except ValueError:
                templateNotifWrongInput()
                continue
        elif inputCuti == 4:
            break
                            


                            

     

                    

                    
        


    



#create initial for launch program with while

while True:
    print('''
    ---------------------------------------------------------
    Selamat Datang di Program Data Karyawan PT Power Telecom :
    ---------------------------------------------------------
    1. Laporan Data Karyawan
    2. Tambah Data Karyawan
    3. Update Data Karyawan
    4. Hapus Data Karyawan
    5. Sistem Cuti Karyawan
    6. Clear Cli
    7. Clear All Data
    8. Exit
    
    ''')
    try:
        inputMenu = int(input('Silahkan Pilih Menu (1-8): '))   
    except ValueError:
        templateNotifWrongInput()
        continue
    
    if inputMenu == 1:
        laporanMenu()
    elif inputMenu == 2:
        tambahMenu()
    elif inputMenu == 3:
        updateMenu()
    elif inputMenu == 4:
        hapusMenu()
    elif inputMenu == 5:
        sistemCuti()   
    elif inputMenu == 6:
        clearCli()
    elif inputMenu == 7:
        clearAll()
    elif inputMenu == 8:
        exit()
    else:
        templateNotifWrongInput()
        continue
        
