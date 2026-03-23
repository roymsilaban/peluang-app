import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

st.set_page_config(page_title="Aplikasi Statistika", layout="wide")

st.title("📊 Aplikasi Statistika Lengkap")

# ===============================
# INPUT DATA
# ===============================
st.header("Input Data")

input_data = st.text_area(
    "Masukkan data (pisahkan dengan koma)",
    "10, 20, 30, 40, 50, 60, 70, 80, 90"
)

if st.button("Proses Data"):
    try:
        data = list(map(float, input_data.split(",")))
        data.sort()

        st.success("Data berhasil diproses!")

        # ===============================
        # STATISTIKA DASAR
        # ===============================
        mean = np.mean(data)
        median = np.median(data)
        modus = stats.mode(data, keepdims=True)[0][0]
        minimum = np.min(data)
        maksimum = np.max(data)
        std_dev = np.std(data)
        varians = np.var(data)
        jangkauan = maksimum - minimum

        st.subheader("Hasil Perhitungan Statistika")

        col1, col2, col3 = st.columns(3)

        col1.metric("Mean", round(mean, 2))
        col2.metric("Median", round(median, 2))
        col3.metric("Modus", round(modus, 2))

        col1.metric("Minimum", minimum)
        col2.metric("Maksimum", maksimum)
        col3.metric("Jangkauan", jangkauan)

        col1.metric("Standar Deviasi", round(std_dev, 2))
        col2.metric("Varians (Ragam)", round(varians, 2))

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

        st.subheader("Tabel Distribusi Frekuensi")
        st.dataframe(df)

        # ===============================
        # HISTOGRAM (RAPI)
        # ===============================
        st.subheader("Histogram")

        fig, ax = plt.subplots()

        ax.hist(
            data,
            bins=k,
            edgecolor='black',
            rwidth=0.8
        )

        ax.set_title("Histogram Data")
        ax.set_xlabel("Nilai")
        ax.set_ylabel("Frekuensi")

        st.pyplot(fig)

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
        st.error("Pastikan input berupa angka yang dipisahkan koma.")