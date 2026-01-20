import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Calculatrice Pro %",
    page_icon="📊",
    layout="centered"
)

# Style CSS personnalisé pour améliorer l'apparence
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        border-left: 5px solid #007bff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Calculatrice de Pourcentages")
st.write("Sélectionnez le type de calcul dans le menu à gauche pour commencer.")

# Barre latérale pour la navigation
with st.sidebar:
    st.header("Configuration")
    choix = st.radio(
        "Quel calcul faire ?",
        ["Appliquer un Pourcentage", "Calculer un Ratio", "Hausse ou Baisse", "Évolution (%)"]
    )
    st.info("Cette application est gratuite et sécurisée.")

# --- LOGIQUE DE CALCUL ---

if choix == "Appliquer un Pourcentage":
    st.header("🧮 Appliquer un pourcentage")
    col1, col2 = st.columns(2)
    with col1:
        total = st.number_input("Montant Total (€, $, ...)", value=100.0, step=1.0)
    with col2:
        pct = st.number_input("Pourcentage à appliquer (%)", value=20.0, step=0.5)
    
    resultat = total * (pct / 100)
    
    st.markdown(f"""
    <div class="result-box">
        <p style='margin:0; color:gray;'>Le résultat est :</p>
        <h2 style='margin:0; color:#007bff;'>{resultat:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)

elif choix == "Calculer un Ratio":
    st.header("🔢 Calculer un ratio / part")
    valeur = st.number_input("Valeur partielle", value=25.0)
    total = st.number_input("Valeur totale", value=200.0)
    
    if total != 0:
        ratio = (valeur / total) * 100
        st.success(f"Cela représente **{ratio:.2f} %** du total.")
    else:
        st.error("Le total ne peut pas être zéro.")

elif choix == "Hausse ou Baisse":
    st.header("📉 Appliquer une hausse/baisse")
    valeur_i = st.number_input("Prix ou valeur initiale", value=50.0)
    pct_var = st.number_input("Pourcentage (%)", value=10.0)
    mode = st.selectbox("Action", ["Réduction (-)", "Augmentation (+)"])
    
    if mode == "Augmentation (+)":
        final = valeur_i * (1 + pct_var / 100)
        st.metric("Prix Final", f"{final:.2f}", f"+{pct_var}%")
    else:
        final = valeur_i * (1 - pct_var / 100)
        st.metric("Prix Final", f"{final:.2f}", f"-{pct_var}%", delta_color="inverse")

elif choix == "Évolution (%)":
    st.header("📈 Calculer une évolution")
    col1, col2 = st.columns(2)
    with col1:
        v_dep = st.number_input("Valeur de départ", value=100.0)
    with col2:
        v_fin = st.number_input("Valeur d'arrivée", value=125.0)
    
    if v_dep != 0:
        diff = ((v_fin - v_dep) / v_dep) * 100
        label = "Hausse" if diff > 0 else "Baisse"
        st.metric(label, f"{diff:.2f}%")
