import streamlit as st

def show_sidebar():
    """Display sidebar with navigation options"""
    with st.sidebar:
        st.title("🧠 Smart-Aid")
        
        # Boutons de navigation
        if st.button("🏠 Accueil", key="nav_accueil"):
            st.session_state['page'] = 'accueil'
            st.rerun()
        
        if st.button("📋 Questionnaire", key="nav_questionnaire"):
            st.session_state['page'] = 'questionnaire'
            st.rerun()
        
        if st.button("🧩 Sélection des Tests", key="nav_test_selection"):
            st.session_state['page'] = 'test_selection'
            st.rerun()
        
        if st.button("🔢 Test de Mathématiques", key="nav_dyscalculie"):
            st.session_state['page'] = 'test_dyscalculie'
            st.rerun()
        
        if st.button("🎯 Test d'Attention", key="nav_tdah"):
            st.session_state['page'] = 'test_tdah'
            st.rerun()
        
        if 'dyscalculie_responses' in st.session_state and st.session_state['dyscalculie_responses']:
            if st.button("📊 Résultats Mathématiques", key="nav_res_dyscalculie"):
                st.session_state['page'] = 'resultats_dyscalculie'
                st.rerun()
        
        if 'tdah_responses' in st.session_state and st.session_state['tdah_responses']:
            if st.button("📈 Résultats Attention", key="nav_res_tdah"):
                st.session_state['page'] = 'resultats_tdah'
                st.rerun()
        
        st.markdown("---")
        st.markdown("### 🌟 Conseils")
        st.info("Prends ton temps pour répondre aux questions. Ce n'est pas une course ! 😊")