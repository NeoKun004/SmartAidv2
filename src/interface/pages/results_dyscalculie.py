import streamlit as st
from src.utils.image_utils import dyscalc_b64
from src.utils.score_utils import check_answers_and_provide_solutions
from src.utils.llm_utils import analyze_results_with_ai
from src.solutions import provide_improved_dyscalculia_solution
from src.llm_connector import get_llm_connector

def show_page():
    """Display the dyscalculia results page"""
    responses = st.session_state['dyscalculie_responses']
    
    st.title(f"🎯 Résultats du test de mathématiques")
    
    # Vérifier les réponses et obtenir les solutions si nécessaire
    correct_answers, total_questions, solutions = check_answers_and_provide_solutions("dyscalculie", responses)
    
    # Analyse des résultats avec le LLM
    if 'dyscalculia_analysis' not in st.session_state:
        with st.spinner("Analyse des résultats en cours..."):
            st.session_state['dyscalculia_analysis'] = analyze_results_with_ai("dyscalculie", responses)
    
    analysis = st.session_state['dyscalculia_analysis']
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #4ECDC4;">
            <h3 style="color: #4ECDC4; text-align: center;">🏆 Félicitations pour avoir terminé le test!</h3>
            <div style="display: flex; justify-content: center; margin: 15px 0;">
                <img src="data:image/png;base64,{dyscalc_b64}" style="max-width: 90%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Afficher le score
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #5D5FEF;">
            <h3 style="color: #5D5FEF; text-align: center;">📊 Ton score</h3>
            <p style="font-size: 1.5rem; text-align: center; color: #333;">
                Tu as obtenu <span style="font-weight: bold; color: #FF6B6B;">{correct_answers}/{total_questions}</span> bonnes réponses!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Afficher l'analyse
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #FF6B6B;">
            <h3 style="color: #FF6B6B; text-align: center;">📊 Analyse personnalisée</h3>
            <p style="font-size: 1.1rem; line-height: 1.6; color: #333; white-space: pre-line;">
                {analysis}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Appel à notre module de solution amélioré pour dyscalculie
    llm_connector = get_llm_connector()
    provide_improved_dyscalculia_solution(analysis, responses, llm_connector)
    
    # Bouton pour revenir à l'accueil
    if st.button("Retour à l'accueil", key="btn_retour_dyscalculie"):
        st.session_state['page'] = 'accueil'
        st.rerun()