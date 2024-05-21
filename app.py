import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

# Muat data
file_path = "netflix_titles.csv"
data = pd.read_csv(file_path, encoding='latin-1')

# Filter data untuk lima tahun terakhir
tahun_sekarang = pd.Timestamp.now().year
data_limpa_tahun_terakhir = data[data['release_year'] >= tahun_sekarang - 5]

# Judul utama untuk dashboard
st.title("Dashboard Netflix")

# Bagian visualisasi data
st.header("Raw Data")

# Tampilkan data mentah jika diinginkan
if st.checkbox("Tampilkan Data Mentah"):
    st.write(data_limpa_tahun_terakhir)

# Grafik batang jumlah judul yang dirilis dalam lima tahun terakhir
st.subheader("Jumlah Judul yang Dirilis dalam 5 Tahun Terakhir")
plt.figure(figsize=(10, 6))
sns.countplot(x='release_year', data=data_limpa_tahun_terakhir)
plt.xlabel("Tahun Rilis")
plt.ylabel("Jumlah Judul")
plt.title("Jumlah Judul yang Dirilis dalam 5 Tahun Terakhir")
plt.xticks(rotation=45)
st.pyplot()

# Grafik variasi jumlah judul yang dirilis setiap tahun dalam lima tahun terakhir
st.subheader("Variasi Jumlah Judul yang Dirilis Setiap Tahun dalam 5 Tahun Terakhir")
plt.figure(figsize=(10, 6))
sns.countplot(x='release_year', hue='type', data=data_limpa_tahun_terakhir)
plt.xlabel("Tahun Rilis")
plt.ylabel("Jumlah Judul")
plt.title("Variasi Jumlah Judul yang Dirilis Setiap Tahun dalam 5 Tahun Terakhir")
plt.legend(title='Tipe')
plt.xticks(rotation=45)
st.pyplot()


# Contoh: Distribusi rating dalam 5 tahun terakhir
st.subheader("Distribusi Rating dalam 5 Tahun Terakhir")
plt.figure(figsize=(10, 6))
sns.histplot(data=data_limpa_tahun_terakhir, x='rating', kde=True)
plt.xlabel("Rating")
plt.ylabel("Frekuensi")
plt.title("Distribusi Rating dalam 5 Tahun Terakhir")
plt.xticks(rotation=45)
st.pyplot()

# Grafik pie dari distribusi jenis konten dalam lima tahun terakhir
st.subheader("Distribusi Jenis Konten dalam 5 Tahun Terakhir")
jenis_konten = data_limpa_tahun_terakhir['type'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(jenis_konten, labels=jenis_konten.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Distribusi Jenis Konten dalam 5 Tahun Terakhir")
st.pyplot()
