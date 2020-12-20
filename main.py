# Nama  : Agung Mubarok
# NIM   : 0110120196
# Kelas : Sistem Informasi - 05

def hitung_kemunculan(s):
  # Membuat variabel data_dict yang akan menampung array kosong
  data_dict = {}
  # Jika pembatas tidak diberikan secara spesifik, maka spasi akan dijadikan pembatas default
  spasi = s.split()
  # Membuat perulangan i di dalam elemen variabel spasi
  for i in spasi:
    # Variabel data_dict yang berisi array kosong di isi dengan string i sama dengan variabel spasi yang menghitung string i
    data_dict[str(i)] = spasi.count(str(i))
  # Mengembalikan nilai data_dict
  return data_dict

# ==========================================================
# ==========================================================

def urut_unik(s):
  # Jika pembatas tidak diberikan secara spesifik, maka spasi akan dijadikan pembatas default
  spasi = s.split()
  #Memasukan data list menjadi dictionary sebagai key agar tidak ada duplikasi lalu merubah ke list kembali 
  myList = list(dict.fromkeys(spasi))
  #Mengurutkan data
  myList.sort()
  # Mengembalikan nilai myList
  return myList

  #referensi: https://www.w3schools.com/python/python_howto_remove_duplicates.asp

# ==========================================================
# ==========================================================

def read(filename):
  # Membuat variabel result yang akan menampung array kosong
  result = {}
  # Variabel f untuk membuka file dan merepresentasikan isi filename dengan fungsi open()
  f = open(filename)
  # Membuat perulangan dimana i berada di variabel f
  for i in f:
    # Membuat fungsi split untuk menambahkan data ke array string menggunakan pemisah yang didefinisikan
    split = i.split()
    # Variabel result yang berisi array kosong di isi dengan variabel split dengan index 0 sama dengan variabel split index 1
    result[split[0]] = split[1]
  # Jika pengolahan file sudah selesai
  f.close()
  # Mengembalikan nilai result
  return result

# ==========================================================
# ==========================================================

# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = hitung_kemunculan("pisang jambu apel jambu pisang jeruk")
  print(f"hitung_kemunculan('pisang jambu apel jambu pisang jeruk') = {r} \n(solusi: {{'pisang': 2, 'jambu': 2, 'apel': 1, 'jeruk': 1}})")
  print()
  r = urut_unik("pisang jambu apel jambu pisang jeruk")
  print(f"urut_unik('pisang jambu apel jambu pisang jeruk') = {r} \n(solusi: ['apel', 'jambu', 'jeruk', 'pisang'])")
  print()
  r = urut_unik('kecapi melon kecapi kecapi kecapi')
  print(f"urut_unik('kecapi melon kecapi kecapi kecapi') = {r} \n(solusi: ['kecapi', 'melon'])")
  print()
  r = read('data1.txt')
  print(f"read('data1.txt') = {r} \n(solusi: {{'101': 'Teddy-Bear', '102': 'Kelereng', '201': 'Laptop', '202': 'Smartphone', '203': 'Speaker', '301': 'Avanza', '302': 'Supra-X', '401': 'Topi', '402': 'Jaket', '403': 'Scarf'}}")
  print()
  r = read('data2.txt')
  print(f"read('nilai2.txt') = {r} \n(solusi: {{'711': 'Malaysia', '712': 'Singapura', '713': 'Indonesia', '814': 'USA', '815': 'Canada'}}")
  print()

if __name__ == '__main__':
  test()