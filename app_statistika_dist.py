import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

st.set_page_config(page_title="Aplikasi Statistika", layout="wide")

# ===============================
# CUSTOM CSS (BIAR ELEGAN)
# ===============================
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.main-title {
    font-size:220px;
    font-weight:bold;
    color:#2c3e50;
    text-align:center;
}
.card {
    padding:20px;
    border-radius:15px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color:white;
    text-align:center;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
.section {
    background-color:white;
    padding:20px;
    border-radius:15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">📊 APLIKASI STATISTIKA TABEL DISTRIBUSI</p>', unsafe_allow_html=True)

# ===============================
# INPUT DATA
# ===============================
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("📥 Input Data")

    input_data = st.text_area(
        "Masukkan data (pisahkan dengan koma)",
        "10, 20, 30, 40, 50, 60, 70, 80, 90"
    )

    st.markdown('</div>', unsafe_allow_html=True)

if st.button("🚀 Proses Data"):
    try:
        data = list(map(float, input_data.split(",")))
        data.sort()

        # ===============================
        # STATISTIKA
        # ===============================
        mean = np.mean(data)
        median = np.median(data)
        modus = stats.mode(data, keepdims=True)[0][0]
        minimum = np.min(data)
        maksimum = np.max(data)
        std_dev = np.std(data)
        varians = np.var(data)
        jangkauan = maksimum - minimum

        st.subheader("📊 Hasil Statistika")

        col1, col2, col3, col4 = st.columns(4)

        col1.markdown(f'<div class="card">Mean<br><h2>{mean:.2f}</h2></div>', unsafe_allow_html=True)
        col2.markdown(f'<div class="card">Median<br><h2>{median:.2f}</h2></div>', unsafe_allow_html=True)
        col3.markdown(f'<div class="card">Modus<br><h2>{modus:.2f}</h2></div>', unsafe_allow_html=True)
        col4.markdown(f'<div class="card">Jangkauan<br><h2>{jangkauan:.2f}</h2></div>', unsafe_allow_html=True)

        col5, col6, col7, col8 = st.columns(4)

        col5.markdown(f'<div class="card">Min<br><h2>{minimum:.2f}</h2></div>', unsafe_allow_html=True)
        col6.markdown(f'<div class="card">Max<br><h2>{maksimum:.2f}</h2></div>', unsafe_allow_html=True)
        col7.markdown(f'<div class="card">Std Dev<br><h2>{std_dev:.2f}</h2></div>', unsafe_allow_html=True)
        col8.markdown(f'<div class="card">Varians<br><h2>{varians:.2f}</h2></div>', unsafe_allow_html=True)

        # ===============================
        # DISTRIBUSI FREKUENSI
        # ===============================
        n = len(data)
        k = int(1 + 3.3 * np.log10(n))
        min_data = min(data)
        max_data = max(data)
        range_data = max_data - min_data
        panjang_kelas = int(np.ceil(range_data / k))

        kelas = []
        frekuensi = []
        batas_bawah = min_data

        for i in range(k):
            batas_atas = batas_bawah + panjang_kelas
            count = sum(batas_bawah <= x < batas_atas for x in data)

            kelas.append(f"{int(batas_bawah)} - {int(batas_atas)}")
            frekuensi.append(count)

            batas_bawah = batas_atas

        df = pd.DataFrame({
            "Range Data": kelas,
            "Frekuensi": frekuensi
        })

        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("📋 Tabel Distribusi Frekuensi")
        st.dataframe(df)
        st.markdown('</div>', unsafe_allow_html=True)

        # ===============================
        # HISTOGRAM
        # ===============================
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("📉 Histogram")

        fig, ax = plt.subplots()
        ax.hist(data, bins=k, edgecolor='black', rwidth=0.8)
        ax.set_title("Histogram Data")
        ax.set_xlabel("Nilai")
        ax.set_ylabel("Frekuensi")

        st.pyplot(fig)
        st.markdown('</div>', unsafe_allow_html=True)

        # ===============================
        # LINE CHART
        # ===============================
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("📈 Grafik Garis")

        fig2, ax2 = plt.subplots()
        ax2.plot(data, marker='o')
        ax2.set_title("Grafik Garis")
        ax2.set_xlabel("Index")
        ax2.set_ylabel("Nilai")

        st.pyplot(fig2)
        st.markdown('</div>', unsafe_allow_html=True)

    except:
        st.error("⚠️ Pastikan input berupa angka yang dipisahkan koma.")
