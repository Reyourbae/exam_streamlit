import streamlit as st
import pandas as pd
import numpy as np

#array
a = np.array([1, 2, 3, 4])
b = np.array([(1.1,1.2,1.3),(2.1,2.2,2.3)], dtype=float)

#data series
u = pd.Series([1, 2, 3, 4, 5, 6, 7])

#cara mengambil data dari github
dataset = pd.read_csv("https://raw.githubusercontent.com/Reyourbae/2106019_MuhammadRaihan_B/main/customer_churn_dataset.csv")

#data dictionary
profil = {
    'nama': 'Muhammad Raihan',
    'umur': '21',
    'pemrograman': ['python', 'streamlit', 'HTML'],
    'favorit': {
        'makanan': 'Nasi Goreng',
        'Hobi': 'Motoran',
    }
}


#json
st.text("Ini adalah cara menampilkan data json")
st.json(profil)

#metrik
st.text("Ini adalah data matric")
st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")


#dataframe
st.text("Ini Adalah Data Frame")
st.dataframe(b)
st.dataframe(u)
st.dataframe(dataset)

#tabel
st.text("Ini adalah Data Table")
st.table(a)
st.table(dataset)