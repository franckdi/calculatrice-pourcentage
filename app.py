import streamlit as st
from fpdf import FPDF
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="Calculatrice Pro %", page_icon="📊")

# --- FONCTION GENERATION PDF ---
def create_pdf(titre, detail, resultat):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Rapport de Calcul - Pourcentages", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Date : {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt=f"Type de calcul : {titre}", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Détails : {detail}")
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, txt=f"RESULTAT FINAL : {resultat}", ln=True)
    return pdf.output(dest='S').encode('latin-1')

# --- INTERFACE ---
st.title("📊 Calculatrice avec Export PDF")

choix = st.sidebar.selectbox("Calcul à effectuer", 
    ["Appliquer un Pourcentage", "Calculer un Ratio", "Hausse ou Baisse", "Évolution (%)"])

# Initialisation des variables pour le PDF
titre_pdf = choix
detail_pdf = ""
res_pdf = ""

if choix == "Appliquer un Pourcentage":
    total = st.number_input("Montant Total", value=100.0)
    pct = st.number_input("Pourcentage (%)", value=20.0)
    res = total * (pct / 100)
    detail_pdf = f"Calcul de {pct}% sur un montant de {total}."
    res_pdf = f"{res}"
    st.success(f"Résultat : {res}")

elif choix == "Calculer un Ratio":
    val = st.number_input("Valeur partielle", value=25.0)
    tot = st.number_input("Total", value=100.0)
    res = (val / tot) * 100
    detail_pdf = f"Part de {val} par rapport à {tot}."
    res_pdf = f"{res:.2f}%"
    st.success(f"Ratio : {res:.2f}%")

# (Les autres blocs Hausse/Baisse et Evolution suivent la même logique...)

st.divider()

# --- BOUTON DE TÉLÉCHARGEMENT ---
if res_pdf:
    pdf_data = create_pdf(titre_pdf, detail_pdf, res_pdf)
    st.download_button(
        label="📥 Télécharger le résultat en PDF",
        data=pdf_data,
        file_name="calcul_pourcentage.pdf",
        mime="application/pdf"
    )
