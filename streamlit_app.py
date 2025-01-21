import streamlit as st
import hashlib

# Fonction pour hasher les mots de passe
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Initialiser les utilisateurs si non existant
def initialize_users():
    if 'users' not in st.session_state:
        if 'persistent_users' not in st.session_state:
            st.session_state.persistent_users = {
                "admin@example.com": {
                    "password": hash_password("admin123"),
                    "is_logged_in": False
                }
            }
        st.session_state.users = st.session_state.persistent_users.copy()

# Initialiser les scores et les prix si non existants
def initialize_state():
    if 'scores' not in st.session_state:
        st.session_state.scores = {
            "Transport": 0,
            "Hébergement": 0,
            "Restauration": 0,
            "Activités": 0,
            "Autre": 0,
        }
    if 'prices' not in st.session_state:
        st.session_state.prices = {
            "Transport": 0,
            "Hébergement": 0,
            "Restauration": 0,
            "Activités": 0,
            "Autre": 0,
        }

# Vérifier l'état de connexion
def is_logged_in():
    for user, data in st.session_state.users.items():
        if data.get("is_logged_in", False):
            return user
    return None

# Interface d'inscription et de connexion combinées
def auth_page():
    st.markdown("# Connexion / Inscription")
    option = st.radio("Choisissez une option", ["Connexion", "Inscription"], key="auth_option")

    if option == "Connexion":
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Mot de passe", type="password", key="login_password")
        if st.button("Se connecter", key="login_button"):
            user_data = st.session_state.users.get(email)
            if not user_data:
                st.error("Utilisateur non trouvé. Veuillez vous inscrire.")
            elif user_data.get("password") != hash_password(password):
                st.error("Mot de passe incorrect.")
            else:
                user_data["is_logged_in"] = True
                st.success(f"Bienvenue {email} !")

    elif option == "Inscription":
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Mot de passe", type="password", key="signup_password")
        confirm_password = st.text_input("Confirmer le mot de passe", type="password", key="signup_confirm_password")
        if st.button("S'inscrire", key="signup_button"):
            if email in st.session_state.users:
                st.error("Cet email est déjà utilisé.")
            elif password != confirm_password:
                st.error("Les mots de passe ne correspondent pas.")
            elif len(password) < 6:
                st.error("Le mot de passe doit contenir au moins 6 caractères.")
            else:
                st.session_state.users[email] = {
                    "password": hash_password(password),
                    "is_logged_in": False
                }
                st.session_state.persistent_users[email] = {
                    "password": hash_password(password),
                    "is_logged_in": False
                }
                st.success("Inscription réussie ! Vous pouvez maintenant vous connecter.")

    if is_logged_in():
        if st.button("Se déconnecter", key="logout_button"):
            st.session_state.users[is_logged_in()]["is_logged_in"] = False
            st.success("Vous avez été déconnecté.")

# Initialiser les utilisateurs
initialize_users()
initialize_state()

# Vérifier l'état de connexion
logged_in_user = is_logged_in()

# Afficher l'email de l'utilisateur connecté
if logged_in_user:
    st.sidebar.markdown(f"### Connecté en tant que {logged_in_user}")

# Barre latérale pour la navigation
st.sidebar.markdown("## Menu")
menu = ["Connexion / Inscription", "Accueil", "Questionnaire", "Informations", "Analyse"]
if "page" not in st.session_state:
    st.session_state.page = "Accueil"
selection = st.sidebar.radio("", menu, index=menu.index(st.session_state.page))

# Contenu des sections
if selection == "Accueil":
    st.markdown("# 💡 TouriSieve")
    st.write("➡️ __L'objectif de cette application est de vous aider, en tant que tour-opérateur, à adopter un tourisme plus durable.__")

    st.write("🌍 Selon l’Organisation mondiale du tourisme (OMT), un __tourisme durable__ tient pleinement compte de ses impacts économiques, sociaux et environnementaux, répondant aux besoins actuels et futurs des visiteurs, des professionnels, de l'environnement, et des communautés d'accueil.")
    
    st.write("📄 Pour avancer dans cette démarche, vous avez ici accès à un __questionnaire conçu spécifiquement pour identifier des pistes d’amélioration dans vos activités.__ Celui-ci s'appuie sur la chaîne de valeur du tourisme, décomposée en cinq grands piliers : Transport, Hébergement, Restauration, Activités, et Autres services. En abordant ces différents aspects, notre approche vous permet d’évaluer l'impact de chaque maillon de votre chaîne sur les économies locales et les communautés.")
    
    st.write("📊 À l'issue du questionnaire, __vous recevrez une estimation des retombées économiques de vos activités sur les communautés locales__. Une retombée économique désigne tout revenu généré par le tourisme qui reste dans l'économie locale plutôt que d’être rapatrié à l’étranger. Ce principe garantit que les bénéfices du tourisme sont redistribués auprès des communautés locales, contribuant ainsi à un développement économique inclusif et durable.")
    
    st.write("🥳 Grâce à cette application, vous serez en mesure de renforcer les effets positifs de vos activités sur l'économie locale et d’adopter des pratiques toujours plus responsables et durables. Engageons-nous ensemble pour un tourisme qui profite à tous et respecte l’avenir.")

elif selection == "Connexion / Inscription":
    auth_page()

elif selection == "Questionnaire":
    st.markdown("# 📝 Questionnaire")

    if 'total_impact_values' not in st.session_state:
        st.session_state.total_impact_values = {
            "Transport": 0,
            "Hébergement": 0,
            "Restauration": 0,
            "Activités": 0,
            "Autre": 0
        }

    if 'prices' not in st.session_state:
        st.session_state.prices = {
            "Transport": 0,
            "Hébergement": 0,
            "Restauration": 0,
            "Activités": 0,
            "Autre": 0
        }


    with st.expander("Transport"):
        st.session_state.prices["Transport"] = st.number_input("Renseigner le prix (en €) pour la section Transport :", min_value=0, key="price_transport")

        weights = {
            "q1": 0.10,
            "q2": 0.20,
            "q3": 0.15,
            "q4": 0.15,
            "q5": 0.15,
            "q6": 0.15,
            "q7": 0.10
        }

        impacts = {
            "q1": {"Oui": 0.75, "Non": 0.20, "Je ne sais pas": 0.0},
            "q2": {"Oui": 0.60, "Non": 0.30, "Je ne sais pas": 0.0},
            "q3": {"Oui": 1.00, "Non": 0.20, "Je ne sais pas": 0.0},
            "q4": {"Oui": 0.65, "Non": 0.35, "Je ne sais pas": 0.0},
            "q5": {"Oui": 0.10, "Non": 0.00, "Je ne sais pas": 0.0},
            "q6": {"Oui": 0.70, "Non": 0.30, "Je ne sais pas": 0.0},
            "q7": {"Oui": 0.60, "Non": 0.20, "Je ne sais pas": 0.0}
        }

        questions = {
            "q1": "Les véhicules utilisés pour le transport touristique (bus, trains, avions, navettes) sont-ils fabriqués ou assemblés localement ?",
            "q2": "Les compagnies qui assurent les liaisons internes (bus, train, avion) sont-elles majoritairement locales ?",
            "q3": "Les chauffeurs et le personnel opérant les services de transport touristique sont-ils majoritairement locaux ?",
            "q4": "L'entretien et la maintenance des transports touristiques se font-ils localement ?",
            "q5": "Les entreprises de transport et leurs salariés paient-ils leurs impôts localement ?",
            "q6": "Les véhicules de transport touristique sont-ils principalement achetés et entretenus localement ?",
            "q7": "Existe-t-il des taxes locales spécifiques sur les transports touristiques et des mesures de compensation des impacts environnementaux ?"
        }

        total_impact = 0
        for q, weight in weights.items():
            response = st.radio(questions[q], ["Oui", "Non", "Je ne sais pas"], index=2, key=f"transport_{q}")
            total_impact += impacts[q][response] * weight

        total_impact_percentage = total_impact * 100
        total_impact_value = st.session_state.prices["Transport"] * total_impact
        st.session_state.total_impact_values["Transport"] = total_impact_value
        
        st.write(f"### Résultat pour Transport")
        st.write(f"- **Retombées économiques locales :** {total_impact_percentage:.2f}%")
        st.write(f"- **Montant des retombées économiques :** {total_impact_value:.2f} €")

    with st.expander("Hébergement"):
        st.session_state.prices["Hébergement"] = st.number_input("Renseigner le prix (en €) pour la section Hébergement :", min_value=0, key="price_hebergement")

        weights = {
            "q1": 0.30,
            "q2": 0.15,
            "q3": 0.15,
            "q4": 0.10,
            "q5": 0.20,
            "q6": 0.10
    }

        impacts = {
            "q1": {"Oui": 1.00, "Non": 0.50, "Je ne sais pas": 0.0},
            "q2": {"Oui": 1.00, "Non": 0.15, "Je ne sais pas": 0.0},
            "q3": {"Oui": 1.00, "Non": 0.15, "Je ne sais pas": 0.0},
            "q4": {"Oui": 0.25, "Non": 0.00, "Je ne sais pas": 0.0},
            "q5": {"Oui": 1.00, "Non": 0.20, "Je ne sais pas": 0.0},
            "q6": {"Oui": 0.25, "Non": 0.00, "Je ne sais pas": 0.0}
    }

        questions = {
            "q1": "Les hébergements touristiques (hôtels, maisons d’hôtes, campings, etc) sont-ils majoritairement possédés et opérés par des acteurs locaux ?",
            "q2": "Les hébergements proposent-ils des produits alimentaires locaux dans le cas où des repas seraient inclus (ex : petit déjeuner) ?",
            "q3": "Les hébergements touristiques payent-ils des taxes locales importantes (ex: taxe de séjour) sans bénéficier d'exonérations ou de structures fiscales avantageuses ?",
            "q4": "Les meubles, décorations et linges utilisés dans les hébergements proviennent-ils majoritairement d’entreprises locales ?",
            "q5": "Les employés des hébergements sont-ils majoritairement locaux ?",
            "q6": "Les hébergements touristiques utilisent-ils principalement des plateformes internationales comme Booking.com ou Expedia ?"
    }

        total_impact = 0
        for q, weight in weights.items():
            response = st.radio(questions[q], ["Oui", "Non", "Je ne sais pas"], index=2, key=f"hebergement_{q}")
            total_impact += impacts[q][response] * weight

        total_impact_percentage = total_impact * 100
        total_impact_value = st.session_state.prices["Hébergement"] * total_impact
        st.session_state.total_impact_values["Hébergement"] = total_impact_value

        st.write(f"### Résultat pour Hébergement")
        st.write(f"- **Retombées économiques locales :** {total_impact_percentage:.2f}%")
        st.write(f"- **Montant des retombées économiques :** {total_impact_value:.2f} €")

    with st.expander("Restauration"):
        st.session_state.prices["Restauration"] = st.number_input("Renseigner le prix (en €) pour la section Restauration :", min_value=0, key="price_restauration")

        weights = {
            "q1": 0.30,
            "q2": 0.40,
            "q3": 0.20,
            "q4": 0.10
    }

        impacts = {
            "q1": {"Oui": 0.85, "Non": 0.30, "Je ne sais pas": 0.0},
            "q2": {"Oui": 1.00, "Non": 0.03, "Je ne sais pas": 0.0},
            "q3": {"Oui": 0.70, "Non": 0.30, "Je ne sais pas": 0.0},
            "q4": {"Oui": 0.90, "Non": 0.00, "Je ne sais pas": 0.0}
    }

        questions = {
            "q1": "Les restaurants sont-ils principalement détenus et gérés par des acteurs locaux ?",
            "q2": "Les restaurants s’approvisionnent-ils majoritairement en produits locaux (aliments, boissons et fournitures non alimentaires) ?",
            "q3": "Les employés des restaurants sont-ils majoritairement locaux ?",
            "q4": "Les restaurants valorisent-ils activement la cuisine locale à travers des plats typiques et des expériences culinaires avec des guides locaux ?"
    }

        total_impact = 0
        for q, weight in weights.items():
            response = st.radio(questions[q], ["Oui", "Non", "Je ne sais pas"], index=2, key=f"restauration_{q}")
            total_impact += impacts[q][response] * weight

        total_impact_percentage = total_impact * 100
        total_impact_value = st.session_state.prices["Restauration"] * total_impact
        st.session_state.total_impact_values["Restauration"] = total_impact_value

        st.write(f"### Résultat pour Restauration")
        st.write(f"- **Retombées économiques locales :** {total_impact_percentage:.2f}%")
        st.write(f"- **Montant des retombées économiques :** {total_impact_value:.2f} €")

    with st.expander("Activités"):
        st.write("Section en cours de développement.")

    with st.expander("Autre"):
        st.session_state.prices["Autre"] = st.number_input("Renseigner le prix (en €) pour la section Autre :", min_value=0, key="price_autre")

        weights = {
            "q1": 0.25,
            "q2": 0.20,
            "q3": 0.15,
            "q4": 0.20,
            "q5": 0.10,
            "q6": 0.10
    }

        impacts = {
            "q1": {"Oui": 0.75, "Non": 0.35, "Je ne sais pas": 0.0},
            "q2": {"Oui": 0.65, "Non": 0.40, "Je ne sais pas": 0.0},
            "q3": {"Oui": 0.80, "Non": 0.25, "Je ne sais pas": 0.0},
            "q4": {"Oui": 0.65, "Non": 0.40, "Je ne sais pas": 0.0},
            "q5": {"Oui": 0.70, "Non": 0.25, "Je ne sais pas": 0.0},
            "q6": {"Oui": 0.55, "Non": 0.15, "Je ne sais pas": 0.0}
    }

        questions = {
            "q1": "Les boutiques de souvenirs vendent-elles principalement des produits fabriqués localement ?",
            "q2": "Les magasins de souvenirs sont-ils principalement des franchises locales ?",
            "q3": "Les services de guide général (ex. : visites de ville) sont-ils majoritairement fournis par des guides locaux ?",
            "q4": "Les spas et centres de bien-être sont-ils principalement gérés par des locaux ?",
            "q5": "Les produits de bien-être (huiles, crèmes) utilisés sont-ils principalement fabriqués localement ?",
            "q6": "Les transactions touristiques (change, retraits) sont-elles majoritairement effectuées dans des banques locales ?"
    }

        total_impact = 0
        for q, weight in weights.items():
            response = st.radio(questions[q], ["Oui", "Non", "Je ne sais pas"], index=2, key=f"autre_{q}")
            total_impact += impacts[q][response] * weight

        total_impact_percentage = total_impact * 100
        total_impact_value = st.session_state.prices["Autre"] * total_impact
        st.session_state.total_impact_values["Autre"] = total_impact_value

        st.write(f"### Résultat pour Autre")
        st.write(f"- **Retombées économiques locales :** {total_impact_percentage:.2f}%")
        st.write(f"- **Montant des retombées économiques :** {total_impact_value:.2f} €")

 # Résultats globaux
    total_sejour = sum(st.session_state.prices.values())
    total_retombes = sum(st.session_state.total_impact_values.values())
    total_retombes_percentage = (total_retombes / total_sejour * 100) if total_sejour != 0 else 0

    st.write("## Résultat global")
    st.write(f"**Montant total du séjour :** {total_sejour:.2f} €")
    st.write(f"**Retombées économiques locales totales :** {total_retombes_percentage:.2f}%")
    st.write(f"**Montant des retombées économiques locales :** {total_retombes:.2f} €")

elif selection == "Informations":
    st.markdown("# ℹ️ Informations")
    st.write("Section informations en cours de développement.")

elif selection == "Analyse":
    st.markdown("# 📊 Analyse")
    st.write("Section analyse en cours de développement.")
