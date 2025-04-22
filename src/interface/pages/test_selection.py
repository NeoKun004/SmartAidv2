import streamlit as st
from src.utils.image_utils import dyscalc_b64, dtha_b64, dyslexie_b64

def show_page():
    """Display the test selection page after questionnaire"""
    st.title("🔍 Sélection des Tests")
    
    # Récupérer les informations du questionnaire avec vérifications
    nom = "l'enfant"
    age = ""
    
    if 'questionnaire_responses' in st.session_state and st.session_state['questionnaire_responses'] is not None:
        if 'info' in st.session_state['questionnaire_responses']:
            nom = st.session_state['questionnaire_responses']['info'].get('nom', 'l\'enfant')
            age = st.session_state['questionnaire_responses']['info'].get('age', '')
    
    # Afficher un message de bienvenue personnalisé
    st.markdown(f"""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h2 style="color: #5D5FEF; text-align: center;">Merci d'avoir complété le questionnaire!</h2>
        <p style="font-size: 1.2rem; text-align: center;">
            Maintenant, {nom} peut choisir un test à réaliser.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Obtenir le test suggéré
    suggested_test = st.session_state.get('suggested_test', None)
    
    # Afficher une suggestion basée sur le questionnaire si disponible
    if suggested_test:
        if suggested_test == 'tdah':
            suggestion_text = "D'après vos réponses au questionnaire, nous recommandons de commencer par le test d'attention."
            highlight_tdah = "border: 5px solid #FFD166; box-shadow: 0 0 15px rgba(255, 209, 102, 0.5);"
            highlight_dyscalculie = ""
            highlight_dyslexie = ""
        elif suggested_test == 'dyscalculie':
            suggestion_text = "D'après vos réponses au questionnaire, nous recommandons de commencer par le test de mathématiques."
            highlight_dyscalculie = "border: 5px solid #FFD166; box-shadow: 0 0 15px rgba(255, 209, 102, 0.5);"
            highlight_tdah = ""
            highlight_dyslexie = ""
        elif suggested_test == 'dyslexie':
            suggestion_text = "D'après vos réponses au questionnaire, nous recommandons de commencer par le test de lecture."
            highlight_dyslexie = "border: 5px solid #FFD166; box-shadow: 0 0 15px rgba(255, 209, 102, 0.5);"
            highlight_tdah = ""
            highlight_dyscalculie = ""
        else:
            highlight_tdah = ""
            highlight_dyscalculie = ""
            highlight_dyslexie = ""
            suggestion_text = "D'après vos réponses au questionnaire, nous recommandons de choisir un test adapté à vos besoins."
        
        st.markdown(f"""
        <div style="background-color: rgba(255, 209, 102, 0.2); padding: 15px; border-radius: 15px; margin-bottom: 20px; border: 2px solid #FFD166;">
            <p style="font-size: 1.1rem; text-align: center;">
                💡 {suggestion_text}
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        highlight_tdah = ""
        highlight_dyscalculie = ""
        highlight_dyslexie = ""
    
    # Afficher les options de test en trois colonnes
    col1, col2, col3 = st.columns(3, gap="small")
    
    with col1:
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin: 10px 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1); {highlight_dyscalculie}">
            <h2 style="color: #FF6B6B; text-align: center;">
                <span style="font-size: 32px;">🧮</span> 
                Test de Mathématiques
            </h2>
            <p style="font-size: 1.1rem; text-align: center; margin: 10px 0;">
                Évalue les compétences en mathématiques avec des exercices amusants !
            </p>
            <div style="display: flex; justify-content: center; margin: 10px 0;">
                <img src="data:image/png;base64,{dyscalc_b64}" style="max-width: 90%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Commencer le test de Mathématiques", key="btn_dyscalculie"):
            # Sauvegarder les infos du questionnaire
            if 'questionnaire_responses' in st.session_state and st.session_state['questionnaire_responses'] is not None:
                if 'info' in st.session_state['questionnaire_responses']:
                    info = st.session_state['questionnaire_responses']['info']
                    st.session_state['dyscalculie_nom'] = info.get('nom', '')
                    st.session_state['dyscalculie_age'] = info.get('age', 6)
                    st.session_state['dyscalculie_classe'] = info.get('classe', '')
            
            st.session_state['page'] = 'test_dyscalculie'
            st.rerun()
    
    with col2:
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin: 10px 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1); {highlight_tdah}">
            <h2 style="color: #5D5FEF; text-align: center;">
                <span style="font-size: 32px;">🧠</span> 
                Test d'Attention
            </h2>
            <p style="font-size: 1.1rem; text-align: center; margin: 10px 0;">
                Teste la concentration et la mémoire avec des défis captivants !
            </p>
            <div style="display: flex; justify-content: center; margin: 10px 0;">
                <img src="data:image/png;base64,{dtha_b64}" style="max-width: 90%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Commencer le test d'Attention", key="btn_tdah"):
            # Sauvegarder les infos du questionnaire
            if 'questionnaire_responses' in st.session_state and st.session_state['questionnaire_responses'] is not None:
                if 'info' in st.session_state['questionnaire_responses']:
                    info = st.session_state['questionnaire_responses']['info']
                    st.session_state['tdah_nom'] = info.get('nom', '')
                    st.session_state['tdah_age'] = info.get('age', 6)
                    st.session_state['tdah_classe'] = info.get('classe', '')
            
            st.session_state['page'] = 'test_tdah'
            st.rerun()
    
    with col3:
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin: 10px 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1); {highlight_dyslexie}">
            <h2 style="color: #CC3366; text-align: center;">
                <span style="font-size: 32px;">📚</span> 
                Test de Lecture
            </h2>
            <p style="font-size: 1.1rem; text-align: center; margin: 10px 0;">
                Évalue les compétences en lecture et traitement des sons !
            </p>
            <div style="display: flex; justify-content: center; margin: 10px 0;">
                <img src="data:image/png;base64,{dyslexie_b64}" style="max-width: 90%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Commencer le test de Lecture", key="btn_dyslexie"):
            # Set default values for the dyslexia test
            st.session_state['dyslexie_nom'] = 'Khalil Baccouche'
            st.session_state['dyslexie_age'] = 8
            st.session_state['dyslexie_classe'] = 'CE2'
            
            # Navigate to the test
            st.session_state['page'] = 'test_dyslexie'
            st.rerun()
    
    # Return to home button
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🏠 Retour à l'accueil", key="return_home", use_container_width=True):
            st.session_state['page'] = "accueil"
            st.rerun()