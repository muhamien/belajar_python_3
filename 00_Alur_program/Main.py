import time

# Mencatat waktu mulai eksekusi program
start_time = time.time()

print("Hello")
print("World")
print("Hello World")

# Menghitung dan mencetak waktu eksekusi program dalam detik
print(time.time() - start_time, "detik")

# Untuk mengkompilasi file Python menjadi bytecode, kita dapat menggunakan
# modul py_compile. Berikut adalah langkah-langkahnya:
# 1. Buka terminal atau command prompt.
# 2. Jalankan perintah berikut untuk mengkompilasi file Python:
#    python -m py_compile Main.py
# Ini akan menghasilkan file bytecode dengan ekstensi .pyc di dalam direktori
# __pycache__.
