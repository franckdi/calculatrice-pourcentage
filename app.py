import streamlit as st
from fpdf import FPDF
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="Calculatrice Pro %", page_icon="📊", layout="centered")

# --- INITIALISATION DE L'HISTORIQUE ---
if 'historique' not in st.session_state:
    st.session_state['historique'] = []

# --- FONCTION GENERATION PDF RÉCAPITULATIF ---
def generate_history_pdf(historique):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Rapport de Calculs - Pourcentages", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"Document généré le : {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True)
    pdf.ln(5)
    
    # En-têtes de tableau
    pdf.set_fill_color(200, 220, 255)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(60, 10, "Type de calcul", 1, 0, 'C', True)
    pdf.cell(80, 10, "Détails", 1, 0, 'C', True)
    pdf.cell(50, 10, "Résultat", 1, 1, 'C', True)
    
    # Données
    pdf.set_font("Arial", size=10)
    for calcul in historique:
        pdf.cell(60, 10, str(calcul['type']), 1)
        pdf.cell(80, 10, str(calcul['details']), 1)
        pdf.cell(50, 10, str(calcul['resultat']), 1, 1)
        
    return pdf.output(dest='S').encode('latin-1')

# --- INTERFACE ---
st.title("📊 Calculatrice % avec Historique")

with st.sidebar:
    st.header("Options")
    choix = st.radio("Type de calcul", 
        ["Valeur d'un pourcentage", "Ratio (Part)", "Hausse ou Baisse", "Évolution (%)"])
    
    if st.button("🗑️ Effacer l'historique"):
        st.session_state['historique'] = []
        st.rerun()

st.subheader(f"📍 {choix}")

# --- FORMULAIRES DE CALCUL ---
col1, col2 = st.columns([2, 1])
with col1:
    if choix == "Valeur d'un pourcentage":
        total = st.number_input("Montant Total", value=0.0)
        pct = st.number_input("Pourcentage (%)", value=0.0)
        if st.button("Calculer"):
            res = total * (pct / 100)
            st.session_state['historique'].append({
                "type": "Valeur", "details": f"{pct}% de {total}", "resultat": f"{res:,.2f}"
            })

    elif choix == "Ratio (Part)":
        val = st.number_input("Valeur partielle", value=0.0)
        tot = st.number_input("Total", value=0.0)
        if st.button("Calculer"):
            if tot != 0:
                res = (val / tot) * 100
                st.session_state['historique'].append({
                    "type": "Ratio", "details": f"{val} sur {tot}", "resultat": f"{res:.2f}%"
                })

    elif choix == "Hausse ou Baisse":
        val_i = st.number_input("Valeur initiale", value=0.0)
        pct_v = st.number_input("Pourcentage (%)", value=0.0)
        mode = st.selectbox("Action", ["Réduction (-)", "Augmentation (+)"])
        if st.button("Calculer"):
            coeff = (1 + pct_v/100) if mode == "Augmentation (+)" else (1 - pct_v/100)
            res = val_i * coeff
            signe = "+" if mode == "Augmentation (+)" else "-"
            st.session_state['historique'].append({
                "type": "Hausse/Baisse", "details": f"{val_i} {signe} {pct_v}%", "resultat": f"{res:,.2f}"
            })

    elif choix == "Évolution (%)":
        v1 = st.number_input("Départ", value=0.0)
        v2 = st.number_input("Arrivée", value=0.0)
        if st.button("Calculer"):
            if v1 != 0:
                res = ((v2 - v1) / v1) * 100
                st.session_state['historique'].append({
                    "type": "Evolution", "details": f"De {v1} à {v2}", "resultat": f"{res:+.2f}%"
                })

# --- AFFICHAGE DE L'HISTORIQUE ET PDF ---
st.divider()
st.subheader("📜 Historique de la session")

if st.session_state['historique']:
    # Affichage tableau
    st.table(st.session_state['historique'])
    
    # Bouton PDF
    pdf_bytes = generate_history_pdf(st.session_state['historique'])
    st.download_button(
        label="📥 Télécharger le rapport complet (PDF)",
        data=pdf_bytes,
        file_name=f"rapport_calculs_{datetime.now().strftime('%d%m%Y')}.pdf",
        mime="application/pdf",
        use_container_width=True
    )
else:
    st.info("Aucun calcul dans l'historique pour le moment.")
