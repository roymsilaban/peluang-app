import streamlit as st
import numpy as np

st.title("🧮 APLIKASI PERHITUNGAN MATRIKS (2x2 & 3x3)")

# Pilih ordo matriks
ordo = st.selectbox("Pilih Ordo Matriks", ["2x2", "3x3"])

# Tentukan ukuran
n = 2 if ordo == "2x2" else 3

st.subheader("Input Matriks A")
A = []
for i in range(n):
    row = []
    cols = st.columns(n)
    for j in range(n):
        val = cols[j].number_input(f"A[{i+1},{j+1}]", key=f"A{i}{j}")
        row.append(val)
    A.append(row)

st.subheader("Input Matriks B")
B = []
for i in range(n):
    row = []
    cols = st.columns(n)
    for j in range(n):
        val = cols[j].number_input(f"B[{i+1},{j+1}]", key=f"B{i}{j}")
        row.append(val)
    B.append(row)

A = np.array(A)
B = np.array(B)

# Pilih operasi
operasi = st.selectbox("Pilih Operasi", [
    "Penjumlahan",
    "Pengurangan",
    "Perkalian",
    "Determinan A",
    "Determinan B",
    "Invers A",
    "Invers B"
])

if st.button("Hitung"):

    try:
        if operasi == "Penjumlahan":
            hasil = A + B
            st.write("Hasil A + B:")
            st.write(hasil)

        elif operasi == "Pengurangan":
            hasil = A - B
            st.write("Hasil A - B:")
            st.write(hasil)

        elif operasi == "Perkalian":
            hasil = np.dot(A, B)
            st.write("Hasil A x B:")
            st.write(hasil)

        elif operasi == "Determinan A":
            det = np.linalg.det(A)
            st.write("Determinan Matriks A:", det)

        elif operasi == "Determinan B":
            det = np.linalg.det(B)
            st.write("Determinan Matriks B:", det)

        elif operasi == "Invers A":
            inv = np.linalg.inv(A)
            st.write("Invers Matriks A:")
            st.write(inv)

        elif operasi == "Invers B":
            inv = np.linalg.inv(B)
            st.write("Invers Matriks B:")
            st.write(inv)

    except Exception as e:
        st.error("Terjadi kesalahan! (Mungkin matriks tidak memiliki invers)")