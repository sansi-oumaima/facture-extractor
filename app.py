import streamlit as st
from extract import extract_text_from_file, parse_invoice_data
import json

st.title("🧾 Extracteur de Factures Marocaines (Ar/Fr)")
uploaded_file = st.file_uploader("Téléversez une facture", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    with open("temp_file", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    text = extract_text_from_file("temp_file")
    st.text_area("Texte extrait :", text, height=300)
    
    data = parse_invoice_data(text)
    st.write("📊 Données extraites :")
    st.json(data)

if st.button("📥 Télécharger JSON"):
    st.download_button("Télécharger", json.dumps(data, indent=2), file_name="facture.json")
