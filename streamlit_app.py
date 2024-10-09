import streamlit as st

# Initialiser les scores pour chaque section
if 'scores' not in st.session_state:
    st.session_state.scores = {
        "Transport": 0,
        "Hébergement": 0,
        "Restauration": 0,
        "Activités": 0,
        "Autre": 0,
    }

# Sidebar navigation
st.sidebar.title("💡 TouriSieve")

# Liste des pages
pages = {
    "Accueil": "Accueil",
    "Transport": "Transport",
    "Hébergement": "Hébergement",
    "Restauration": "Restauration",
    "Activités": "Activités",
    "Autre": "Autre",
}

# Afficher les boutons dans la sidebar
selection = st.sidebar.radio("", list(pages.keys()))

# Afficher le contenu de la page sélectionnée
if selection == "Accueil":
    st.title("💡 TouriSieve")
    st.write("Cette application a pour objectif d'analyser si votre activité touristique bénéficie réellement à la localité.")
    st.write("Écrire définitions et explication du concept")

elif selection == "Transport":
    st.title("✈️ Transport")

    # Première question
    question1 = st.radio(
        "Compagnies aériennes, ferroviaires ou de ferry étrangères opérant des liaisons internes ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="transport_q1"
    )
    if question1 == "Oui":
        st.session_state.scores["Transport"] += 25

    # Deuxième question
    question2 = st.radio(
        "Véhicules, vélos ou bus importés pour les navettes et les liaisons ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="transport_q2"
    )
    if question2 == "Oui":
        st.session_state.scores["Transport"] += 25

    # Troisième question
    question3 = st.radio(
        "Location de véhicules via des entreprises étrangères ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="transport_q3"
    )
    if question3 == "Oui":
        st.session_state.scores["Transport"] += 25

    # Quatrième question
    question4 = st.radio(
        "Emploi et formation de chauffeurs étrangers ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="transport_q4"
    )
    if question4 == "Oui":
        st.session_state.scores["Transport"] += 25

    st.header(f"Score pour la section Transport : {st.session_state.scores['Transport']}%")

elif selection == "Hébergement":
    st.title("🏘️ Hébergement")

    # Première question
    question1 = st.radio(
        "Hébergements gérés par des chaînes internationales ou des étrangers ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="hebergement_q1"
    )
    if question1 == "Oui":
        st.session_state.scores["Hébergement"] += 25

    # Deuxième question
    question2 = st.radio(
        "Utilisation de meubles, décorations et linge importés ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="hebergement_q2"
    )
    if question2 == "Oui":
        st.session_state.scores["Hébergement"] += 25

    # Troisième question
    question3 = st.radio(
        "Externalisation de l’entretien du linge et des services via des entreprises étrangères ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="hebergement_q3"
    )
    if question3 == "Oui":
        st.session_state.scores["Hébergement"] += 25

    # Quatrième question
    question4 = st.radio(
        "Formation des employés réalisée par des étrangers ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="hebergement_q4"
    )
    if question4 == "Oui":
        st.session_state.scores["Hébergement"] += 25

    st.header(f"Score pour la section Hébergement : {st.session_state.scores['Hébergement']}%")

elif selection == "Restauration":
    st.title("🍝 Restauration")

    # Première question
    question1 = st.radio(
        "Utilisation de produits alimentaires et boissons importés dans les menus ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="restauration_q1"
    )
    if question1 == "Oui":
        st.session_state.scores["Restauration"] += 25

    # Deuxième question
    question2 = st.radio(
        "Employés internationaux dans la restauration ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="restauration_q2"
    )
    if question2 == "Oui":
        st.session_state.scores["Restauration"] += 25

    # Troisième question
    question3 = st.radio(
        "Formation du personnel réalisée par des étrangers ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="restauration_q3"
    )
    if question3 == "Oui":
        st.session_state.scores["Restauration"] += 25

    # Quatrième question
    question4 = st.radio(
        "Équipement de restauration (meubles, vaisselles) importé ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="restauration_q4"
    )
    if question4 == "Oui":
        st.session_state.scores["Restauration"] += 25

    st.header(f"Score pour la section Restauration : {st.session_state.scores['Restauration']}%")

elif selection == "Activités":
    st.title("🤿 Activités")

    # Première question
    question1 = st.radio(
        "Recrutement de guides et interprètes via une entreprise étrangère ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="activites_q1"
    )
    if question1 == "Oui":
        st.session_state.scores["Activités"] += 25

    # Deuxième question
    question2 = st.radio(
        "Employés internationaux pour les activités ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="activites_q2"
    )
    if question2 == "Oui":
        st.session_state.scores["Activités"] += 25

    # Troisième question
    question3 = st.radio(
        "Les équipements nécessaires aux activités sont-ils importés ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="activites_q3"
    )
    if question3 == "Oui":
        st.session_state.scores["Activités"] += 25

    # Quatrième question
    question4 = st.radio(
        "La promotion et la maintenance du site visité sont-elles gérées par des acteurs étrangers ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="activites_q4"
    )
    if question4 == "Oui":
        st.session_state.scores["Activités"] += 25

    st.header(f"Score pour la section Activités : {st.session_state.scores['Activités']}%")

elif selection == "Autre":
    st.title("📄Autre")

    # Première question
    question1 = st.radio(
        "Souscription à des assurances ou services fournis par des compagnies étrangères ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="autre_q1"
    )
    if question1 == "Oui":
        st.session_state.scores["Autre"] += 33.33

    # Deuxième question
    question2 = st.radio(
        "Plateformes de réservation ou outils de planification étrangers ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="autre_q2"
    )
    if question2 == "Oui":
        st.session_state.scores["Autre"] += 33.33

    # Troisième question
    question3 = st.radio(
        "Frais bancaires lors de transactions financières ?", 
        ("Oui", "Non", "Je ne sais pas"), 
        index=2,
        key="autre_q3"
    )
    if question3 == "Oui":
        st.session_state.scores["Autre"] += 33.33

    st.header(f"Score pour la section Autre : {st.session_state.scores['Autre']}%")

# Calculer le score global après chaque section
global_score = sum(st.session_state.scores.values()) / len(st.session_state.scores)

# Afficher le score global mis à jour
st.sidebar.header(f"Score général : {global_score:.2f}%")


st.write("pour Paul perso : prochaine modifs à faire : changer fonctionnement comptage chaque sous partie + transport")