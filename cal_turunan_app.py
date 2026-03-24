import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

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
        background: linear-gradient(90deg, #ff512f, #dd2476);
        font-size:28px;
        font-weight:bold;
        margin-bottom:20px;
    }
    .box {
        padding:20px;
        border-radius:10px;
        background:#ffeef5;
        border:1px solid #ff99c8;
        margin-bottom:20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Kalkulator Turunan (Derivative Calculator)</div>", unsafe_allow_html=True)

st.write("Masukkan fungsi seperti `x**3 + 2*x`, `sin(x)`, `exp(x)`, `log(x)`.")

# ==========================
# INPUT & PENGATURAN
# ==========================
st.markdown("<div class='box'>Masukkan fungsi dan pengaturan:</div>", unsafe_allow_html=True)

fungsi = st.text_input("Fungsi f(x):", value="x**3 + 2*x")
orde = st.selectbox("Pilih Turunan ke:", [1, 2, 3])

xmin = st.number_input("X minimum:", value=-10.0)
xmax = st.number_input("X maksimum:", value=10.0)
titik = st.slider("Jumlah titik grafik:", 50, 1000, 400)

# ==========================
# TOMBOL PROSES
# ==========================
if st.button("Hitung Turunan & Tampilkan Grafik"):
    try:
        x = sp.symbols("x")
        expr = sp.sympify(fungsi)

        # Hitung turunan
        turunan = sp.diff(expr, x, orde)

        st.success(f"Turunan ke-{orde}:")
        st.latex(sp.latex(turunan))

        # Konversi ke fungsi numpy
        f = sp.lambdify(x, expr, "numpy")
        f_turunan = sp.lambdify(x, turunan, "numpy")

        X = np.linspace(xmin, xmax, titik)
        Y = f(X)
        Y_d = f_turunan(X)

        # ==========================
        # PLOT GRAFIK
        # ==========================
        fig, ax = plt.subplots()
        
        ax.plot(X, Y, label="f(x)", linewidth=2)
        ax.plot(X, Y_d, label=f"Turunan ke-{orde}", linewidth=2)

        ax.set_title(f"Grafik Fungsi & Turunan ke-{orde}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
