import streamlit as st
import math

st.title("📊 Aplikasi Permutasi & Kombinasi")

n = st.number_input("Masukkan nilai n", min_value=0, step=1)
r = st.number_input("Masukkan nilai r", min_value=0, step=1)

if st.button("Hitung"):
    if r > n:
        st.error("r tidak boleh lebih besar dari n")
    else:
        p = math.factorial(n) // math.factorial(n - r)
        c = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

        st.success(f"Permutasi = {p}")
        st.info(f"Kombinasi = {c}")