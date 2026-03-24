import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# CUSTOM CSS (UI Warna & Menarik)
# ===============================
st.markdown("""
<style>
body {
    background-color: #F0F8FF;
}
.title {
    color: #003366;
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}
.box {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">Aplikasi Penghitung Akar Persamaan Kuadrat</p>', unsafe_allow_html=True)

st.markdown('<div class="box">', unsafe_allow_html=True)

st.write("Masukkan nilai koefisien dari persamaan kuadrat:")
a = st.number_input("a", value=1.0)
b = st.number_input("b", value=0.0)
c = st.number_input("c", value=0.0)

# ===============================
# Hitung diskriminan & akar
# ===============================
if st.button("Hitung Akar"):
    D = b**2 - 4*a*c

    st.subheader("Hasil Perhitungan")

    if D > 0:
        x1 = (-b + np.sqrt(D)) / (2*a)
        x2 = (-b - np.sqrt(D)) / (2*a)
        st.success(f"Dua akar berbeda: x₁ = {x1:.4f}, x₂ = {x2:.4f}")
    elif D == 0:
        x = -b / (2*a)
        st.info(f"Akar kembar: x = {x:.4f}")
    else:
        real = -b / (2*a)
        imag = np.sqrt(-D) / (2*a)
        st.warning(f"Akar kompleks: {real:.4f} ± {imag:.4f}i")

st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# Grafik Parabola
# ===============================
st.subheader("📈 Grafik Parabola")

x_vals = np.linspace(-20, 20, 400)
y_vals = a * x_vals**2 + b * x_vals + c

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_title("Grafik Persamaan Kuadrat")
ax.set_xlabel("x")
ax.set_ylabel("y")
st.pyplot(fig)
