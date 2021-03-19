#Pertemuan pertama sintax dasar python

#penulisan variable
# di php => $
# vasriable di js => let, var, const
# java const
# python => nama_variable

# variable
# - type data
#   - int => angka
#   - string => input " " biasanya berupa huruf,
#               karakter angka
#   - bool => False or True
#   - array => di python > list = []
#   - object => di python > dict (dictionary) {}
# pengkondisian
# perulangan
# array
# penulisan sintax python => pep8

# type data int
# a = 3
# b = 2
# hasil = a + b
# print(hasil)
# # inputan
# a = int(input('input nilai a : '))
# b = int(input('input nilai b : '))
#
# hasil = a + b
# print(hasil)


# data = [1,2,3,4,5,6,7]
# # list/ array = [0, 1, 2, 3]
data = ['kopi', 'susu', 'teh', 'coklat']#list
cari = input('cari produk : ')#string
ketemu = False #bolean
for i in range(0,len(data)): #perulangan
    # print(i)
    if data[i] == cari:#pengkondisian
        print('produk ditemukan ', cari)
        ketemu = True
# print('berhenti')
    break
if not ketemu:
    print('data kosong')

#type dictionary atu type data dict
#adalah type data yang menyimpan nilai kunci

# mahasiswa = {
#     'nim' : 12235,
#     'nama' : 'asad mau',
#     'alamat' : 'jember'
# }
#
# print('cari mahasiswa dengan :', mahasiswa['nim'])