import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data1_dir= os.path.dirname(os.path.realpath(file))
data1 =  pd.read_csv(f"{data1_dir}/main_data1.csv")

data2_dir= os.path.dirname(os.path.realpath(file))
data2 =  pd.read_csv(f"{data2_dir}/main_data2.csv")


st.title("Analisis Penyewaan Sepeda")

st.markdown("""
Pada dashboard ini akan menampilkan hasil analisis dari Bike Sharing Dataset. Analisis dari data penyewaan sepeda ini bertujuan untuk melihat pengaruh cuaca terhadap penyewaan sepeda, pengaruh hari kerja dan hari libur terhadap penyewaan sepeda, serta memperlihatkan pola penyewaan per jam. 
Melalui analisis ini, kita dapat memahami faktor-faktor yang mempengaruhi penyewaan sepeda dan pola penggunaan sepeda di berbagai waktu.
""")

st.header("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")

dampak_cuaca = data2.groupby(by="weathersit")["cnt"].mean().reset_index()
dampak_cuaca.rename(columns={
    "cnt": "rata2_penyewaan"
}, inplace=True)

plt.figure(figsize=(10, 7))
sns.barplot(
    y="rata2_penyewaan", 
    x="weathersit",
    data=dampak_cuaca.sort_values(by="rata2_penyewaan", ascending=False),
    palette=["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"],
    dodge=False
)
plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca", loc="center", fontsize=15)
plt.ylabel("Rata-rata Jumlah Penyewaan")
plt.xlabel("Jenis Cuaca")
plt.xticks(ticks=[0, 1, 2, 3], labels=['Cerah', 'Mendung', 'Hujan Ringan', 'Hujan Berat'])
st.pyplot(plt)  

st.markdown("""
Berdasarkan visualisasi di atas mengenai rata-rata penyewaan sepeda berdasarkan cuaca, dapat 
disimpulkan bahwa penyewaan sepeda dipengaruhi oleh cuaca. Sesuai hasil yang didapat bahwa cuaca 
cerah memiliki jumlah penyewaan tertinggi, disusul dengan cuaca mendung, dan jumlah terendah 
berada di cuaca hujan berat.
""")

st.header("Rata-rata Penyewaan Sepeda Berdasarkan Hari Kerja dan Hari Libur")

dampak_libur = data1.groupby('holiday')['cnt'].mean().reset_index()
dampak_libur["holiday"] = dampak_libur["holiday"].map({0: "Hari Kerja", 1: "Hari Libur"})
data_libur = dampak_libur.rename(columns={"cnt": "rata2_penyewaan"})

plt.figure(figsize=(10, 6))

sns.barplot(
    y="rata2_penyewaan", 
    x="holiday",
    data=data_libur.sort_values(by="rata2_penyewaan", ascending=False),
    palette=["#72BCD4", "#D3D3D3", "#D3D3D3"]
)
plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Hari Kerja dan Hari Libur", loc="center", fontsize=15)
plt.ylabel("Rata-rata Jumlah Penyewaan")
plt.xlabel("Tipe Hari")
plt.tick_params(axis='x', labelsize=12)
st.pyplot(plt)  
st.markdown("""
Berdasarkan visualisasi di atas mengenai rata-rata penyewaan sepeda berdasarkan hari kerja dan hari libur, dapat disimpulkan 
bahwa penyewaan sepeda dipengaruhi oleh hari kerja dan hari libur walaupun tidak jauh berbeda. Hari kerja memiliki jumlah 
rata-rata yang lebih tinggi dibanding hari libur yang memiliki rata-rata sekitar 4000 lebih.
""")

st.header("Total Penyewaan Sepeda per Jam dalam Satu Hari")

total_jam = data2.groupby("hr")["cnt"].sum().reset_index()
plt.figure(figsize=(10, 5))
plt.plot(
    total_jam["hr"],
    total_jam["cnt"],
    marker='o', 
    linewidth=2,
    color="#72BCD4"
)
plt.title("Total Penyewaan Sepeda per Jam dalam Satu Hari", loc="center", fontsize=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("Jam")
plt.ylabel("Total Penyewaan Sepeda")
st.pyplot(plt) 
st.markdown("""
Berdasarkan visualisasi di atas mengenai total penyewaan sepeda per jam dalam satu hari, terlihat bahwa waktu yang paling tinggi 
pada saat pagi dan sore hari. Pada waktu menjelang siang dan tengah tren penyewaan sepeda menurun.
""")

