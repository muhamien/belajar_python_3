
# Contoh penggunaan casting tipe data di Python

# 1. Casting dari Integer ke Float
integer_value = 10
float_value = float(integer_value)
print("Integer ke Float:", float_value)  # Output: 10.0

# ==================================================

# Contoh yang salah: Menggunakan string yang tidak dapat dikonversi ke float
try:
    invalid_float = float("abc")
except ValueError as e:
    print("Error saat mengonversi string 'abc' ke float:", e)

# ==================================================

# 2. Casting dari Float ke Integer
float_value = 10.5
integer_value = int(float_value)
print("Float ke Integer:", integer_value)  # Output: 10

# ==================================================

# Contoh yang salah: Menggunakan string yang tidak dapat dikonversi ke integer
try:
    invalid_integer = int("10.5")
except ValueError as e:
    print("Error saat mengonversi string '10.5' ke integer:", e)

# ==================================================

# 3. Casting dari Integer ke String
integer_value = 10
string_value = str(integer_value)
print("Integer ke String:", string_value)  # Output: "10"

# ==================================================

# 4. Casting dari String ke Integer
string_value = "10"
integer_value = int(string_value)
print("String ke Integer:", integer_value)  # Output: 10

# ==================================================

# Contoh yang salah: Menggunakan string yang tidak dapat dikonversi ke integer
try:
    invalid_integer = int("abc")
except ValueError as e:
    print("Error saat mengonversi string 'abc' ke integer:", e)

# ==================================================

# 5. Casting dari String ke Float
string_value = "10.5"
float_value = float(string_value)
print("String ke Float:", float_value)  # Output: 10.5

# ==================================================

# Contoh yang salah: Menggunakan string yang tidak dapat dikonversi ke float
try:
    invalid_float = float("abc")
except ValueError as e:
    print("Error saat mengonversi string 'abc' ke float:", e)

# ==================================================

# 6. Casting dari List ke Tuple
list_value = [1, 2, 3]
tuple_value = tuple(list_value)
print("List ke Tuple:", tuple_value)  # Output: (1, 2, 3)

# ==================================================

# 7. Casting dari Tuple ke List
tuple_value = (1, 2, 3)
list_value = list(tuple_value)
print("Tuple ke List:", list_value)  # Output: [1, 2, 3]

# ==================================================

# 8. Casting dari List ke Set
list_value = [1, 2, 3, 3]
set_value = set(list_value)
print("List ke Set:", set_value)  # Output: {1, 2, 3}

# ==================================================

# 9. Casting dari Set ke List
set_value = {1, 2, 3}
list_value = list(set_value)
print("Set ke List:", list_value)  # Output: [1, 2, 3]

# ==================================================

# 10. Casting dari Dictionary ke List (mengambil kunci)
dict_value = {"nama": "John", "umur": 30}
list_keys = list(dict_value.keys())
list_values = list(dict_value.values())
print("Dictionary ke List (Keys):", list_keys)  # Output: ["nama", "umur"]

# Casting dari Dictionary ke List (mengambil nilai)
list_values = list(dict_value.values())
print("Dictionary ke List (Values):", list_values)  # Output: ["John", 30]

# ==================================================
