import streamlit as st
from src.utils.image_utils import dtha_b64
from src.utils.score_utils import check_answers_and_provide_solutions
from src.utils.llm_utils import analyze_results_with_ai
from src.solutions.tdah import (
    provide_tdah_solution, 
    display_word_hunter_game, 
    display_memory_game, 
    display_sequence_game,
    display_reaction_game
)
from src.llm_connector import get_llm_connector

def show_page():
    """Display the TDAH results page with comprehensive analysis and interactive activities"""
    responses = st.session_state['tdah_responses']
    
    # Vérifier si nous affichons une activité spécifique
    if 'current_tdah_activity' not in st.session_state:
        st.session_state['current_tdah_activity'] = None
    
    # Si une activité est sélectionnée, l'afficher
    if st.session_state['current_tdah_activity']:
        activity = st.session_state['current_tdah_activity']
        
        # Afficher un bouton de retour
        if st.button("← Retour aux résultats", key="back_to_results"):
            st.session_state['current_tdah_activity'] = None
            st.rerun()
        
        # Afficher l'activité sélectionnée
        if activity == "word_hunter":
            display_word_hunter_game()
        elif activity == "memory_game":
            display_memory_game()
        elif activity == "sequence_game":
            display_sequence_game()
        elif activity == "reaction_game":
            display_reaction_game()
        
        return  # Sortir de la fonction si on affiche une activité
    
    # Sinon, afficher la page de résultats normale
    st.title(f"🎯 Résultats du test d'attention")
    
    # Récupérer les résultats détaillés
    detailed_results = responses.get('detailed_results', {})
    
    # Calculer les scores
    total_score = sum([detailed_results[key]["score"] for key in detailed_results])
    max_score = sum([detailed_results[key]["max"] for key in detailed_results])
    
    # Vérifier les réponses et obtenir les solutions
    correct_answers, total_questions, solutions = check_answers_and_provide_solutions("tdah", responses)
    
    # Analyse des résultats avec le LLM
    if 'tdah_analysis' not in st.session_state:
        with st.spinner("Analyse des résultats en cours..."):
            st.session_state['tdah_analysis'] = analyze_results_with_ai("tdah", responses)
    
    # Récupérer l'analyse
    analysis = st.session_state['tdah_analysis']

    # Si l'analyse est vide ou None, utiliser une analyse de secours
    if not analysis or analysis.strip() == "":
        analysis = """Tu montres de bons résultats en mémorisation et en flexibilité cognitive! 🌟 

Tu as bien retenu les détails de l'histoire et tu as pu t'adapter à de nouvelles consignes. C'est super!

J'ai remarqué que tu pourrais améliorer ton attention soutenue et ton organisation. Ce sont des compétences que tout le monde peut développer avec un peu de pratique.

Voici quelques jeux amusants pour t'aider:
- Joue à "Où est Charlie?" pour entraîner ton attention
- Essaie des jeux de mémoire avec des cartes
- Utilise un tableau coloré pour organiser tes tâches quotidiennes

N'oublie pas: chaque petit effort compte! Ton cerveau est comme un muscle qui devient plus fort à chaque entraînement. Continue comme ça, je suis sûr que tu vas faire des progrès formidables! 🚀"""
        st.session_state['tdah_analysis'] = analysis
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #5D5FEF;">
            <h3 style="color: #5D5FEF; text-align: center;">🏆 Félicitations pour avoir terminé le test!</h3>
            <div style="display: flex; justify-content: center; margin: 15px 0;">
                <img src="data:image/png;base64,{dtha_b64}" style="max-width: 90%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Afficher le score global
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #5D5FEF;">
            <h3 style="color: #5D5FEF; text-align: center;">📊 Ton score global</h3>
            <p style="font-size: 1.5rem; text-align: center; color: #333;">
                Tu as obtenu <span style="font-weight: bold; color: #FF6B6B;">{total_score}/{max_score}</span> points au total!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Afficher les scores par catégorie
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #4ECDC4;">
            <h3 style="color: #4ECDC4; text-align: center;">📊 Tes résultats par catégorie</h3>
        </div>
        """, unsafe_allow_html=True)
        
        for category, data in detailed_results.items():
            category_name = {
                "memorisation": "📚 Mémorisation",
                "attention": "👁️ Attention Soutenue",
                "impulsivite": "⏱️ Contrôle de l'Impulsivité",
                "memoire": "🧠 Mémoire de Travail",
                "organisation": "📋 Organisation",
                "flexibilite": "🔄 Flexibilité Cognitive"
            }.get(category, category)
            
            score = data["score"]
            max_possible = data["max"]
            
            # Couleur selon le score
            color = "#4ECDC4" if score >= max_possible/2 else "#FF6B6B"
            
            st.markdown(f"""
            <div style="background-color: rgba(255,255,255,0.5); padding: 10px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid {color};">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 1.1rem;">{category_name}</span>
                    <span style="font-weight: bold; color: {color};">{score}/{max_possible}</span>
                </div>
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
    
    # Appel à notre module de solution pour TDAH
    llm_connector = get_llm_connector()
    provide_tdah_solution(analysis, responses, llm_connector)
    
    # Ajouter des activités interactives recommandées
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #4ECDC4;">
        <h3 style="color: #4ECDC4; text-align: center;">🎮 Activités recommandées</h3>
        <p style="text-align: center; font-size: 1.1rem;">
            Choisis une activité pour t'entraîner tout en t'amusant!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Créer des cartes pour chaque activité recommandée
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #4ECDC4;">
            <h4 style="color: #4ECDC4; text-align: center;">🔍 Chasse aux Mots</h4>
            <p>Améliore ton attention en trouvant rapidement les mots d'une catégorie spécifique.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 Jouer maintenant", key="play_word_hunter"):
            # Sauvegarder l'activité dans la session state
            st.session_state['current_tdah_activity'] = "word_hunter"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #5D5FEF;">
            <h4 style="color: #5D5FEF; text-align: center;">🧠 Jeu de la Mémoire</h4>
            <p>Entraîne ta mémoire en te souvenant des formes et couleurs.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 Jouer maintenant", key="play_memory_game"):
            st.session_state['current_tdah_activity'] = "memory_game"
            st.rerun()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #FF6B6B;">
            <h4 style="color: #FF6B6B; text-align: center;">📋 Trouve l'Ordre</h4>
            <p>Améliore ton organisation en remettant des actions dans le bon ordre.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 Jouer maintenant", key="play_sequence_game"):
            st.session_state['current_tdah_activity'] = "sequence_game"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #FFD166;">
            <h4 style="color: #FFD166; text-align: center;">🎯 Temps de Réaction</h4>
            <p>Entraîne ton impulsivité en améliorant ton temps de réaction.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎮 Jouer maintenant", key="play_reaction_game"):
            st.session_state['current_tdah_activity'] = "reaction_game"
            st.rerun()
    
    # Bouton pour revenir à l'accueil
    if st.button("🏠 Retour à l'accueil", key="btn_retour_tdah"):
        st.session_state['page'] = 'accueil'
        st.rerun()