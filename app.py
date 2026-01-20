import streamlit as st

st.set_page_config(page_title="Calculatrice %", page_icon="🧮")

st.title("🧮 Calculatrice de Pourcentages")
st.write("Outil simple pour tous vos calculs quotidiens.")

menu = ["Valeur d'un pourcentage", "Ratio (Part)", "Augmentation / Réduction", "Taux de variation"]
choix = st.sidebar.selectbox("Choisissez le type de calcul", menu)

st.divider()

if choix == "Valeur d'un pourcentage":
    st.subheader("Calculer x% d'un montant")
    total = st.number_input("Montant total", value=100.0)
    pct = st.number_input("Pourcentage (%)", value=20.0)
    res = total * (pct / 100)
    st.info(f"Résultat : **{res}**")

elif choix == "Ratio (Part)":
    st.subheader("Quel pourcentage représente cette valeur ?")
    valeur = st.number_input("Valeur partielle", value=15.0)
    total = st.number_input("Total", value=60.0)
    if total != 0:
        res = (valeur / total) * 100
        st.info(f"Résultat : **{res:.2f}%**")

elif choix == "Augmentation / Réduction":
    st.subheader("Appliquer une hausse ou une baisse")
    val = st.number_input("Valeur initiale", value=80.0)
    pct = st.number_input("Pourcentage (%)", value=30.0)
    type_op = st.radio("Type d'opération", ["Réduction (-)", "Augmentation (+)"])
    if type_op == "Augmentation (+)":
        res = val * (1 + pct / 100)
    else:
        res = val * (1 - pct / 100)
    st.info(f"Prix final : **{res:.2f}**")

elif choix == "Taux de variation":
    st.subheader("Calculer l'évolution entre deux chiffres")
    v1 = st.number_input("Valeur de départ", value=100.0)
    v2 = st.number_input("Valeur finale", value=150.0)
    if v1 != 0:
        var = ((v2 - v1) / v1) * 100
        st.info(f"Variation : **{'+' if var > 0 else ''}{var:.2f}%**")
