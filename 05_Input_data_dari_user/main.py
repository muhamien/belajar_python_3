# Contoh penggunaan input untuk mendapatkan data dari pengguna
data = input("Masukkan data: ")

# Menampilkan data yang dimasukkan dan tipe datanya
print("Data yang dimasukkan:", data, ", Tipe data:", type(data))  # Output: Data yang dimasukkan: <data_input> , Tipe data: <class 'str'>

# Contoh casting dari input string ke integer
int_value = int(input("Masukkan angka: "))
print("String ke Integer:", int_value)  # Output: String ke Integer: <angka_input>

# Contoh casting dari input string ke boolean
bool_value = input("Masukkan nilai boolean (True/False): ").strip().lower() == 'true'
print("String ke Boolean:", bool_value)  # Output: String ke Boolean: <True/False>

# Contoh casting dari input string angka ke boolean
# Angka 0 akan dianggap False, sedangkan angka selain 0 akan dianggap True
number_input = int(input("Masukkan angka (0 untuk False, selain 0 untuk True): "))
bool_from_number = bool(number_input)
print("Angka ke Boolean:", bool_from_number)  # Output: Angka ke Boolean: <True/False>
