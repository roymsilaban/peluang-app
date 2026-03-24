import streamlit as st
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
        background: linear-gradient(90deg, #8e2de2, #4a00e0);
        font-size:28px;
        font-weight:bold;
        margin-bottom:20px;
    }
    .box {
        padding:20px;
        border-radius:10px;
        background:#f3e8ff;
        border:1px solid #c59fff;
        margin-bottom:20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Aplikasi Aljabar: Simplifikasi, Faktor, dan Penyelesaian</div>", unsafe_allow_html=True)

st.write("Masukkan ekspresi atau persamaan aljabar, misalnya: `x^2 + 2*x + 1`, `sin(x) + sin(x)` atau `x^2 - 9 = 0`.")

# ==========================
# MENU OPERASI
# ==========================
opsi = st.selectbox(
    "Pilih Operasi Aljabar:",
    ["Penyederhanaan (Simplify)", 
     "Faktorisasi (Factor)",
     "Penyelesaian Persamaan",
     "Faktorisasi Persamaan Kuadrat"]
)

st.markdown("<div class='box'>Input Ekspresi atau Persamaan:</div>", unsafe_allow_html=True)

user_input = st.text_input("Masukkan ekspresi atau persamaan:", value="x^2 + 2*x + 1")

x = sp.symbols("x")


# ==========================
# PROSES OPERASI
# ==========================
if st.button("Proses"):
    try:
        # Ubah ^ menjadi **
        ekspresi = user_input.replace("^", "**")

        if opsi == "Penyederhanaan (Simplify)":
            hasil = sp.simplify(ekspresi)
            st.subheader("Hasil Penyederhanaan:")
            st.latex(sp.latex(hasil))

        elif opsi == "Faktorisasi (Factor)":
            expr = sp.sympify(ekspresi)
            hasil = sp.factor(expr)
            st.subheader("Hasil Faktor:")
            st.latex(sp.latex(hasil))

        elif opsi == "Penyelesaian Persamaan":
            bagian = ekspresi.split("=")
            kiri = sp.sympify(bagian[0])
            kanan = sp.sympify(bagian[1])
            solusi = sp.solve(sp.Eq(kiri, kanan), x)

            st.subheader("Solusi Persamaan:")
            if solusi:
                for s in solusi:
                    st.latex(f"x = {sp.latex(s)}")
            else:
                st.warning("Tidak ada solusi atau solusi kompleks.")

        elif opsi == "Faktorisasi Persamaan Kuadrat":
            expr = sp.sympify(ekspresi)
            faktor = sp.factor(expr)

            st.subheader("Hasil Faktorisasi:")
            st.latex(sp.latex(faktor))

            akar = sp.solve(expr, x)
            st.subheader("Akar-Akar Persamaan:")
            for a in akar:
                st.latex(f"x = {sp.latex(a)}")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
