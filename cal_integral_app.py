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
        background: linear-gradient(90deg, #00b09b, #96c93d);
        font-size:28px;
        font-weight:bold;
        margin-bottom:20px;
    }
    .box {
        padding:20px;
        border-radius:10px;
        background:#e7fff1;
        border:1px solid #00b782;
        margin-bottom:20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Kalkulator Integral</div>", unsafe_allow_html=True)

st.write("Masukkan fungsi seperti `x**2`, `sin(x)`, `exp(x)`, `1/x`.")


# ==========================
# INPUT
# ==========================
st.markdown("<div class='box'>Masukkan fungsi & pengaturan integral:</div>", unsafe_allow_html=True)

fungsi = st.text_input("Fungsi f(x):", value="x**2")

jenis = st.selectbox("Jenis Integral:", ["Integral Tak Tentu", "Integral Tentu"])

if jenis == "Integral Tentu":
    a = st.number_input("Batas bawah (a):", value=0.0)
    b = st.number_input("Batas atas (b):", value=2.0)

xmin = st.number_input("X minimum grafik:", value=-10.0)
xmax = st.number_input("X maksimum grafik:", value=10.0)
titik = st.slider("Jumlah titik grafik:", 50, 1000, 400)


# ==========================
# PROSES
# ==========================
if st.button("Hitung Integral"):
    try:
        x = sp.symbols("x")
        expr = sp.sympify(fungsi)

        # Integral tak tentu
        integral_tak_tentu = sp.integrate(expr, x)

        st.subheader("Integral Tak Tentu:")
        st.latex(sp.latex(integral_tak_tentu + sp.Symbol("C")))

        # Jika integral tentu
        if jenis == "Integral Tentu":
            nilai_integral = sp.integrate(expr, (x, a, b))
            st.subheader("Integral Tentu (a → b):")
            st.success(f"Hasil = {float(nilai_integral):.4f}")

        # =====================================
        # GRAFIK
        # =====================================
        st.subheader("Grafik Fungsi & Area Integral")

        f = sp.lambdify(x, expr, "numpy")

        X = np.linspace(xmin, xmax, titik)
        Y = f(X)

        fig, ax = plt.subplots()
        ax.plot(X, Y, linewidth=2, label="f(x)")
        ax.grid(True)

        if jenis == "Integral Tentu":
            # area shading
            X_area = np.linspace(a, b, 300)
            Y_area = f(X_area)
            ax.fill_between(X_area, Y_area, alpha=0.3, label="Area Integral")

        ax.set_title(f"Grafik Integral dari f(x) = {fungsi}")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
