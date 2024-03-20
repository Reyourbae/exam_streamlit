import streamlit as st

#button
st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

#create chechbox
if st.checkbox("show/hide"):
    st.text("hai sahabat awan pintar")

#radio button
status = st.radio("pilih playlist:",('nlp','streamlit','python','flask'))
#enampilkan status
st.write("sahabat kelas awan pintar siap belajar",status)

#selection box
domain = st.selectbox("sahabat awan pintar siap belajar",
['NLP','Streamlit','python','flask','DS'])
st.write(f"Kelas awan pintar siap belajar", domain)

#multiselect
domain = st.multiselect("sahabat awan pintar siap belajar",
['NLP','Streamlit','python','flask','DS'])
st.write(f"Kelas awan pintar siap belajar", len(domain), 'Playlist')
