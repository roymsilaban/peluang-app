import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

st.set_page_config(page_title="Aplikasi Statistika", layout="wide")

st.title("📊 APLIKASI STATISTIKA DENGAN STREAMLIT")

# ===============================
# INPUT DATA
# ===============================
st.header("Input Data")

input_data = st.text_area(
    "Masukkan data (pisahkan dengan koma)",
    "10, 20, 30, 40, 50"
)

if st.button("Proses Data"):
    try:
        # Konversi ke list angka
        data = list(map(float, input_data.split(",")))
        df = pd.DataFrame(data, columns=["Data"])

        st.success("Data berhasil diproses!")

        # ===============================
        # TABEL DATA
        # ===============================
        st.subheader("Tabel Data")
        st.dataframe(df)

        # ===============================
        # STATISTIKA
        # ===============================
        st.subheader("Hasil Perhitungan Statistika")

        mean = np.mean(data)
        median = np.median(data)
        modus = stats.mode(data, keepdims=True)[0][0]
        minimum = np.min(data)
        maksimum = np.max(data)
        std_dev = np.std(data)

        col1, col2, col3 = st.columns(3)

        col1.metric("Mean", round(mean, 2))
        col2.metric("Median", round(median, 2))
        col3.metric("Modus", round(modus, 2))

        col1.metric("Minimum", minimum)
        col2.metric("Maksimum", maksimum)
        col3.metric("Standar Deviasi", round(std_dev, 2))

        # ===============================
        # HISTOGRAM
        # ===============================
        st.subheader("Histogram")

        fig1, ax1 = plt.subplots()
        ax1.hist(data, bins=5)
        ax1.set_title("Histogram Data")
        ax1.set_xlabel("Nilai")
        ax1.set_ylabel("Frekuensi")

        st.pyplot(fig1)

        # ===============================
        # LINE CHART
        # ===============================
        st.subheader("Grafik Garis")

        fig2, ax2 = plt.subplots()
        ax2.plot(data, marker='o')
        ax2.set_title("Grafik Garis")
        ax2.set_xlabel("Index")
        ax2.set_ylabel("Nilai")

        st.pyplot(fig2)

    except:
        st.error("Terjadi kesalahan! Pastikan input berupa angka yang dipisahkan koma.")