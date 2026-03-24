import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ==========================
# CSS TEMA ELEGAN
# ==========================
st.markdown("""
<style>
    .title {
        text-align:center;
        color:white;
        padding:15px;
        border-radius:10px;
        background: linear-gradient(90deg, #6a11cb, #2575fc);
        font-size:28px;
        font-weight:bold;
        margin-bottom:20px;
    }
    .box {
        padding:20px;
        border-radius:10px;
        background:#f0f4ff;
        border:1px solid #b4c9ff;
        margin-bottom:20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Aplikasi Plot Fungsi Matematika</div>", unsafe_allow_html=True)

st.write("Masukkan fungsi matematika seperti: `sin(x)`, `cos(x)`, `x**2 + 2*x`, `exp(x)`, dll.")

# ==========================
# INPUT FUNGSI
# ==========================
st.markdown("<div class='box'>Masukkan fungsi:</div>", unsafe_allow_html=True)

fungsi = st.text_input("Tuliskan fungsi (misal: x**2 + 3*x - 5):", value="x**2")

xmin = st.number_input("X minimum:", value=-10.0)
xmax = st.number_input("X maksimum:", value=10.0)
titik = st.slider("Jumlah titik grafik:", min_value=50, max_value=1000, value=400)

# ==========================
# TOMBOL PROSES
# ==========================
if st.button("Tampilkan Grafik"):
    try:
        x = sp.symbols("x")
        expr = sp.sympify(fungsi)     # konversi string → ekspresi matematika
        f = sp.lambdify(x, expr, "numpy")

        X = np.linspace(xmin, xmax, titik)
        Y = f(X)

        # ==========================
        # PLOT GRAFIK
        # ==========================
        fig, ax = plt.subplots()
        ax.plot(X, Y, linewidth=2)

        ax.set_title(f"Grafik Fungsi:  f(x) = {fungsi}")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid(True)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
