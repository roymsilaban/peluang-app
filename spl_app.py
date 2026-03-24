import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# =====================
# CUSTOM CSS
# =====================
st.markdown("""
<style>
    .title {
        text-align:center;
        color: white;
        padding:15px;
        border-radius:10px;
        background: linear-gradient(90deg, #007bff, #00c6ff);
        font-size:28px;
        font-weight:bold;
        margin-bottom:20px;
    }
    .box {
        padding:20px;
        border-radius:10px;
        background:#f8f9fa;
        border:1px solid #ddd;
        margin-bottom:20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Aplikasi Sistem Persamaan Linear (SPL)</div>", unsafe_allow_html=True)

st.write("Aplikasi ini menyelesaikan SPL 2 dan 3 variabel menggunakan metode eliminasi (numpy).")

# =====================
# PILIHAN JENIS SPL
# =====================
jenis = st.selectbox("Pilih Jenis SPL", ["SPL 2 Variabel", "SPL 3 Variabel"])

# =====================
# INPUT SPL 2 VARIABEL
# =====================
if jenis == "SPL 2 Variabel":
    st.markdown("<div class='box'>Masukkan koefisien persamaan:</div>", unsafe_allow_html=True)

    a11 = st.number_input("a11 (x)", value=1.0)
    a12 = st.number_input("a12 (y)", value=1.0)
    b1  = st.number_input("b1 (hasil)", value=2.0)

    a21 = st.number_input("a21 (x)", value=1.0)
    a22 = st.number_input("a22 (y)", value=2.0)
    b2  = st.number_input("b2 (hasil)", value=3.0)

    if st.button("Hitung SPL 2 Variabel"):
        A = np.array([[a11, a12],
                      [a21, a22]])
        B = np.array([b1, b2])

        try:
            hasil = np.linalg.solve(A, B)
            st.success(f"Solusi: x = {hasil[0]:.4f}, y = {hasil[1]:.4f}")
        except:
            st.error("SPL tidak memiliki solusi atau tidak unik!")

# =====================
# INPUT SPL 3 VARIABEL
# =====================
else:
    st.markdown("<div class='box'>Masukkan koefisien persamaan:</div>", unsafe_allow_html=True)

    a11 = st.number_input("a11 (x1)", value=1.0)
    a12 = st.number_input("a12 (x2)", value=1.0)
    a13 = st.number_input("a13 (x3)", value=1.0)
    b1  = st.number_input("b1", value=3.0)

    a21 = st.number_input("a21 (x1)", value=1.0)
    a22 = st.number_input("a22 (x2)", value=2.0)
    a23 = st.number_input("a23 (x3)", value=3.0)
    b2  = st.number_input("b2", value=6.0)

    a31 = st.number_input("a31 (x1)", value=2.0)
    a32 = st.number_input("a32 (x2)", value=3.0)
    a33 = st.number_input("a33 (x3)", value=4.0)
    b3  = st.number_input("b3", value=9.0)

    if st.button("Hitung SPL 3 Variabel"):
        A = np.array([[a11, a12, a13],
                      [a21, a22, a23],
                      [a31, a32, a33]])
        B = np.array([b1, b2, b3])

        try:
            hasil = np.linalg.solve(A, B)
            st.success(
                f"Solusi SPL:\n"
                f"x1 = {hasil[0]:.4f}\n"
                f"x2 = {hasil[1]:.4f}\n"
                f"x3 = {hasil[2]:.4f}"
            )
        except:
            st.error("SPL tidak memiliki solusi atau tidak unik!")
