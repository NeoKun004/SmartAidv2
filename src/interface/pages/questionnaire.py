import streamlit as st

def show_page():
    """Display the questionnaire page for screening neurodevelopmental disorders"""
    st.title("📋 Questionnaire de Dépistage des Troubles Neurodéveloppementaux")
    
    # Introduction stylisée
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #5D5FEF;">
        <h3 style="color: #5D5FEF; text-align: center;">👋 Bienvenue au questionnaire</h3>
        <p style="font-size: 1.1rem; text-align: center;">
            Ce questionnaire nous aidera à mieux comprendre les forces et les besoins de l'enfant.
            Vos réponses sont importantes pour nous permettre d'adapter les activités et les conseils.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Informations générales
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #FF6B6B; text-align: center;">📝 Informations générales</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        nom_prenom = st.text_input("Nom et Prénom de l'enfant", key="questionnaire_nom")
    with col2:
        age = st.number_input("Âge", min_value=2, max_value=18, value=6, key="questionnaire_age")
    with col3:
        classe = st.text_input("Classe", key="questionnaire_classe")
    
    # Correction : Initialiser les réponses correctement si non existantes ou si c'est None
    if 'questionnaire_responses' not in st.session_state or st.session_state['questionnaire_responses'] is None:
        st.session_state['questionnaire_responses'] = {
            "sphereA": {},
            "sphereB": {},
            "sphereC": {},
            "sphereD": {},
            "sphereE": {},
            "info": {}
        }
    
    # SPHÈRE A - Attention / Hyperactivité / Impulsivité
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #4ECDC4; text-align: center;">🧠 SPHÈRE A - Attention / Hyperactivité / Impulsivité</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Question 1
    st.markdown("**1. L'enfant a du mal à rester concentré longtemps, même sur une activité de loisir.**")
    col1, col2 = st.columns([3, 2])
    with col1:
        q1 = st.radio(
            "Réponse:", 
            ["OUI", "Rarement", "NON"], 
            key="q1_sphere_a",
            horizontal=True
        )
    with col2:
        q1_comment = st.text_input("Commentaire:", key="q1_comment_a")
    
    # Stocker les réponses
    st.session_state['questionnaire_responses']["sphereA"]["q1"] = {
        "answer": q1,
        "comment": q1_comment
    }
    
    # Question 2
    st.markdown("**2. Il oublie fréquemment certaines choses du quotidien (cahiers, clefs...) ou perd régulièrement ses affaires.**")
    col1, col2 = st.columns([3, 2])
    with col1:
        q2 = st.radio(
            "Réponse:", 
            ["OUI", "Rarement", "NON"], 
            key="q2_sphere_a",
            horizontal=True
        )
    with col2:
        q2_comment = st.text_input("Commentaire:", key="q2_comment_a")
    
    # Stocker les réponses
    st.session_state['questionnaire_responses']["sphereA"]["q2"] = {
        "answer": q2,
        "comment": q2_comment
    }
    
    # Question 3
    st.markdown("**3. Il est facilement distrait par ce qui se passe autour de lui.**")
    col1, col2 = st.columns([3, 2])
    with col1:
        q3 = st.radio(
            "Réponse:", 
            ["OUI", "Rarement", "NON"], 
            key="q3_sphere_a",
            horizontal=True
        )
    with col2:
        q3_comment = st.text_input("Commentaire:", key="q3_comment_a")
    
    # Stocker les réponses
    st.session_state['questionnaire_responses']["sphereA"]["q3"] = {
        "answer": q3,
        "comment": q3_comment
    }
    
    # Question 4
    st.markdown("**4. Il a des difficultés à attendre son tour (parole, jeux...).**")
    col1, col2 = st.columns([3, 2])
    with col1:
        q4 = st.radio(
            "Réponse:", 
            ["OUI", "Rarement", "NON"], 
            key="q4_sphere_a",
            horizontal=True
        )
    with col2:
        q4_comment = st.text_input("Commentaire:", key="q4_comment_a")
    
    # Stocker les réponses
    st.session_state['questionnaire_responses']["sphereA"]["q4"] = {
        "answer": q4,
        "comment": q4_comment
    }
    
    # Question 5
    st.markdown("**5. Il est souvent en mouvement (se lève en classe, bouge beaucoup à la maison).**")
    col1, col2 = st.columns([3, 2])
    with col1:
        q5 = st.radio(
            "Réponse:", 
            ["OUI", "Rarement", "NON"], 
            key="q5_sphere_a",
            horizontal=True
        )
    with col2:
        q5_comment = st.text_input("Commentaire:", key="q5_comment_a")
    
    # Stocker les réponses
    st.session_state['questionnaire_responses']["sphereA"]["q5"] = {
        "answer": q5,
        "comment": q5_comment
    }
    
    # SPHÈRE B - Langage Oral
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; margin-top: 30px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #5D5FEF; text-align: center;">🗣️ SPHÈRE B - Langage Oral</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Questions 6-9 (structure similaire)
    questions_b = [
        "6. L'enfant a des difficultés à comprendre le sens des conversations.",
        "7. Il montre des difficultés pour trouver les mots justes (manque du mot).",
        "8. Il a des difficultés à raconter une histoire de manière cohérente.",
        "9. Il se fait souvent reprendre pour la structure incorrecte de ses phrases."
    ]
    
    for i, question in enumerate(questions_b, 6):
        q_key = f"q{i}"
        st.markdown(f"**{question}**")
        col1, col2 = st.columns([3, 2])
        with col1:
            response = st.radio(
                "Réponse:", 
                ["OUI", "Rarement", "NON"], 
                key=f"{q_key}_sphere_b",
                horizontal=True
            )
        with col2:
            comment = st.text_input("Commentaire:", key=f"{q_key}_comment_b")
        
        # Stocker les réponses
        st.session_state['questionnaire_responses']["sphereB"][q_key] = {
            "answer": response,
            "comment": comment
        }
    
    # SPHÈRE C - Langage Écrit
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; margin-top: 30px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #FF6B6B; text-align: center;">📝 SPHÈRE C - Langage Écrit</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Questions 10-12
    questions_c = [
        "10. Il montre des difficultés à comprendre ce qu'il lit.",
        "11. Il fait beaucoup de fautes d'orthographe et écrit parfois un même mot de plusieurs manières.",
        "12. Il est lent dans la copie ou la prise de notes."
    ]
    
    for i, question in enumerate(questions_c, 10):
        q_key = f"q{i}"
        st.markdown(f"**{question}**")
        col1, col2 = st.columns([3, 2])
        with col1:
            response = st.radio(
                "Réponse:", 
                ["OUI", "Rarement", "NON"], 
                key=f"{q_key}_sphere_c",
                horizontal=True
            )
        with col2:
            comment = st.text_input("Commentaire:", key=f"{q_key}_comment_c")
        
        # Stocker les réponses
        st.session_state['questionnaire_responses']["sphereC"][q_key] = {
            "answer": response,
            "comment": comment
        }
    
    # SPHÈRE D - Motricité et Repérage Spatial
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; margin-top: 30px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #4ECDC4; text-align: center;">🤸 SPHÈRE D - Motricité et Repérage Spatial</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Questions 13-15
    questions_d = [
        "13. Il a du mal avec les activités nécessitant de la coordination (sport, utilisation d'outils comme les ciseaux, le compas...).",
        "14. Il est maladroit (se cogne souvent, renverse des objets).",
        "15. Il a des difficultés à se repérer dans l'espace (perte de repères dans un lieu connu)."
    ]
    
    for i, question in enumerate(questions_d, 13):
        q_key = f"q{i}"
        st.markdown(f"**{question}**")
        col1, col2 = st.columns([3, 2])
        with col1:
            response = st.radio(
                "Réponse:", 
                ["OUI", "Rarement", "NON"], 
                key=f"{q_key}_sphere_d",
                horizontal=True
            )
        with col2:
            comment = st.text_input("Commentaire:", key=f"{q_key}_comment_d")
        
        # Stocker les réponses
        st.session_state['questionnaire_responses']["sphereD"][q_key] = {
            "answer": response,
            "comment": comment
        }
    
    # SPHÈRE E - Fonctionnement Exécutif
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; margin-top: 30px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #5D5FEF; text-align: center;">🧩 SPHÈRE E - Fonctionnement Exécutif</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Questions 16-18
    questions_e = [
        "16. Il a du mal à suivre une consigne longue et ne retient que le début ou la fin.",
        "17. Il pose plusieurs fois les mêmes questions même après avoir reçu une réponse.",
        "18. Il a du mal à s'adapter à une nouvelle situation et persévère dans ses erreurs."
    ]
    
    for i, question in enumerate(questions_e, 16):
        q_key = f"q{i}"
        st.markdown(f"**{question}**")
        col1, col2 = st.columns([3, 2])
        with col1:
            response = st.radio(
                "Réponse:", 
                ["OUI", "Rarement", "NON"], 
                key=f"{q_key}_sphere_e",
                horizontal=True
            )
        with col2:
            comment = st.text_input("Commentaire:", key=f"{q_key}_comment_e")
        
        # Stocker les réponses
        st.session_state['questionnaire_responses']["sphereE"][q_key] = {
            "answer": response,
            "comment": comment
        }
    
    # Stocker les informations générales
    st.session_state['questionnaire_responses']['info'] = {
        "nom": nom_prenom,
        "age": age,
        "classe": classe
    }
    
    # Bouton de soumission
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-top: 30px; margin-bottom: 20px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <p style="font-size: 1.1rem;">
            Vos réponses nous aideront à personnaliser les tests et recommandations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✅ Continuer vers les tests", key="submit_questionnaire"):
            # Analyse rapide des réponses pour suggérer le test le plus approprié
            sphere_a_yes = sum(1 for q, data in st.session_state['questionnaire_responses']["sphereA"].items() if data["answer"] == "OUI")
            
            # Si plus de 2 "OUI" dans la sphère A, suggérer test TDAH
            if sphere_a_yes >= 2:
                st.session_state['suggested_test'] = 'tdah'
            else:
                st.session_state['suggested_test'] = 'dyscalculie'  # par défaut
            
            # Rediriger vers la page d'accueil des tests
            st.session_state['page'] = 'test_selection'
            st.rerun()