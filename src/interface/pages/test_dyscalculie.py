import streamlit as st
from src.utils.image_utils import dyscalc_b64

def show_page():
    """Display the dyscalculia test page"""
    st.title("🔢 Test de Dépistage de la Dyscalculie 🧮")
    
    # Ajouter des éléments visuels amusants
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #4ECDC4; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h3 style="color: #4ECDC4; text-align: center;">👋 Bienvenue au test de dyscalculie</h3>
            <div style="display: flex; justify-content: center; margin: 15px 0;">
                <img src="data:image/png;base64,{dyscalc_b64}" style="max-width: 90%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Formulaire d'informations générales
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #5D5FEF; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #5D5FEF; text-align: center;">👋 Informations générales</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        nom_prenom = st.text_input("Nom et Prénom de l'enfant", key="dyscalculie_nom")
    with col2:
        age = st.number_input("Âge", min_value=2, max_value=18, value=6, key="dyscalculie_age")
    with col3:
        classe = st.text_input("Classe", key="dyscalculie_classe")
    
    # Questions du test de dyscalculie
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #FF6B6B; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #FF6B6B; text-align: center;">📝 Questions</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Exemple de questions pour le test de dyscalculie
    st.markdown("### 🔢 Compréhension des nombres")
    q1 = st.number_input("1. Quel est le résultat de 5 + 3 ?", min_value=0, max_value=20, key="dyscalculie_q1")
    q2 = st.number_input("2. Quel est le résultat de 10 - 4 ?", min_value=0, max_value=20, key="dyscalculie_q2")
    
    st.markdown("### 🧩 Séquences et motifs")
    q3 = st.selectbox("3. Quelle est la suite logique ? 2, 4, 6, 8, ...", ["9", "10", "12", "14"], key="dyscalculie_q3")
    
    st.markdown("### 📏 Mesures et comparaisons")
    q4 = st.radio("4. Quel objet est le plus lourd ?", ["Une plume", "Une pomme", "Un livre", "Une voiture"], key="dyscalculie_q4")
    
    # Bouton pour soumettre le test
    if st.button("Terminer le test", key="btn_terminer_dyscalculie"):
        # Enregistrer les réponses
        st.session_state['dyscalculie_responses'] = {
            "nom": nom_prenom,
            "age": age,
            "classe": classe,
            "q1": q1,
            "q2": q2,
            "q3": q3,
            "q4": q4
        }
        # Rediriger vers la page des résultats
        st.session_state['page'] = 'resultats_dyscalculie'
        st.rerun()