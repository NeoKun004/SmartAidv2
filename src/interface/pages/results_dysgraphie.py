# File path: src/interface/pages/results_dysgraphie.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from src.utils.llm_utils import analyze_results_with_ai
from src.llm_connector import get_llm_connector

def show_page():
    """Display the dysgraphie test results page"""
    st.title("📊 Résultats du Test de Dysgraphie ✍️")
    
    # Check if test results exist
    if 'dysgraphie_responses' not in st.session_state:
        st.error("⚠️ Aucun résultat de test disponible. Veuillez d'abord passer le test.")
        
        # Return to home button
        if st.button("🏠 Retourner à l'accueil", key="home_return_dysgraphie"):
            st.session_state['page'] = "accueil"
            st.rerun()
            
        return
    
    # User info display
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"👤 Nom: {st.session_state.get('dysgraphie_nom', 'Non spécifié')}")
    with col2:
        st.info(f"🎂 Age: {st.session_state.get('dysgraphie_age', 'Non spécifié')}")
    with col3:
        st.info(f"🏫 Classe: {st.session_state.get('dysgraphie_classe', 'Non spécifiée')}")
    
    # Extract scores from session state
    results = st.session_state['dysgraphie_responses'].get('detailed_results', {})
    
    # Calculate total score and percentage
    total_score = sum(test_data["score"] for test_data in results.values())
    max_score = sum(test_data["max"] for test_data in results.values())
    percentage = round((total_score / max_score) * 100) if max_score > 0 else 0
    
    # Display overall result
    st.markdown("""
    <div style="background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="text-align: center; color: #333;">Résultat Global</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Create a gauge chart for the overall score
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=percentage,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Score Global", 'font': {'size': 24}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "royalblue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 30], 'color': 'red'},
                    {'range': [30, 70], 'color': 'orange'},
                    {'range': [70, 100], 'color': 'green'},
                ],
            }
        ))
        
        fig.update_layout(
            height=300,
            margin=dict(l=10, r=10, t=50, b=10),
            font=dict(family="Arial", size=12)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        risk_level = ""
        recommendations = ""
        
        if percentage < 30:
            risk_level = "Élevé"
            color = "red"
            recommendations = "Une évaluation approfondie par un professionnel spécialisé est fortement recommandée."
        elif percentage < 70:
            risk_level = "Modéré"
            color = "orange"
            recommendations = "Certains signes suggèrent des difficultés en écriture. Une évaluation professionnelle pourrait être bénéfique."
        else:
            risk_level = "Faible"
            color = "green"
            recommendations = "Peu de signes de dysgraphie détectés. Continuez à encourager les activités d'écriture!"
        
        st.markdown(f"""
        <div style="background-color: {color}25; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h3 style="color: {color};">Niveau de risque de dysgraphie: {risk_level}</h3>
            <p style="font-size: 1.1rem;">{recommendations}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px; margin-top: 20px;">
            <p style="font-size: 1.0rem;"><b>Score total:</b> {total_score}/{max_score} points ({percentage}%)</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Detailed results section
    st.markdown("""
    <div style="background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
        <h2 style="text-align: center; color: #333;">Résultats Détaillés</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Prepare data for the radar chart
    categories = []
    scores = []
    max_scores = []
    percentages = []
    
    test_names = {
        "copie_texte": "Copie de Texte",
        "ecriture_spontanee": "Écriture Spontanée",
        "vitesse_endurance": "Vitesse et Endurance",
        "graphisme_coordination": "Graphisme et Coordination",
        "lisibilite_orthographe": "Lisibilité et Orthographe"
    }
    
    for test_key, test_data in results.items():
        categories.append(test_names.get(test_key, test_key))
        scores.append(test_data["score"])
        max_scores.append(test_data["max"])
        if test_data["max"] > 0:
            percentages.append((test_data["score"] / test_data["max"]) * 100)
        else:
            percentages.append(0)
    
    # Create a radar chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=percentages,
        theta=categories,
        fill='toself',
        name='Score (%)',
        line_color='rgb(60, 110, 220)',
        fillcolor='rgba(60, 110, 220, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Display detailed scores in a table
    detailed_data = []
    for i, cat in enumerate(categories):
        detailed_data.append({
            "Test": cat,
            "Score": f"{scores[i]}/{max_scores[i]}",
            "Pourcentage": f"{round(percentages[i])}%"
        })
    
    detailed_df = pd.DataFrame(detailed_data)
    st.table(detailed_df)
    
    # Specific observations section
    st.markdown("""
    <div style="background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
        <h2 style="text-align: center; color: #333;">Observations Spécifiques</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Display observations based on test results
    st.markdown("""
    <div style="background-color: rgba(255, 82, 82, 0.1); padding: 20px; border-radius: 10px; margin: 15px 0;">
        <h3 style="color: #ff5252;">Difficultés Identifiées</h3>
        
        <h4 style="margin-top: 15px;">Formation des lettres</h4>
        <p>Des difficultés dans la formation régulière et cohérente des lettres ont été observées, un signe caractéristique de la dysgraphie.</p>
        
        <h4 style="margin-top: 15px;">Organisation spatiale</h4>
        <p>L'organisation spatiale sur la page présente des irrégularités, notamment dans l'alignement et les espacements.</p>
        
        <h4 style="margin-top: 15px;">Motricité fine</h4>
        <p>Le contrôle du crayon et la coordination fine montrent des signes de difficulté, affectant la précision des tracés.</p>
        
        <h4 style="margin-top: 15px;">Vitesse et endurance</h4>
        <p>L'écriture devient de plus en plus irrégulière avec le temps, indiquant une fatigue et une difficulté à maintenir l'effort.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Recommendations section
    st.markdown("""
    <div style="background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
        <h2 style="text-align: center; color: #333;">Recommandations</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Get the LLM connector for solutions (will be used later when solution module is available)
    llm_connector = get_llm_connector()
    
    # Placeholder for solution module call (to be implemented later)
    # This will be replaced with a call like:
    # provide_dysgraphie_solution(analysis, st.session_state['dysgraphie_responses'], llm_connector)
    
    # For now, display default recommendations
    st.markdown("""
    <div style="background-color: rgba(0, 150, 199, 0.1); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #0096c7;">Recommandations Générales</h3>
        
        <h4 style="margin-top: 15px;">1. Évaluation professionnelle</h4>
        <p>Il est recommandé de consulter un ergothérapeute pour une évaluation complète et un plan d'intervention personnalisé.</p>
        
        <h4 style="margin-top: 15px;">2. Exercices de motricité fine</h4>
        <p>Pratiquer quotidiennement des activités de motricité fine comme le découpage, le modelage, les jeux de construction.</p>
        
        <h4 style="margin-top: 15px;">3. Approche multisensorielle</h4>
        <p>Utiliser des approches multisensorielles (toucher, voir, entendre) pour renforcer l'apprentissage de l'écriture.</p>
        
        <h4 style="margin-top: 15px;">4. Adaptations matérielles</h4>
        <p>Proposer des outils adaptés comme des grips pour crayons, des papiers à lignage spécial, ou des guides d'écriture.</p>
        
        <h4 style="margin-top: 15px;">5. Renforcement positif</h4>
        <p>Encourager l'enfant et valoriser ses efforts plutôt que le résultat final de son écriture.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Placeholder for AI-driven solutions (to be implemented when you provide the solution file)
    st.markdown("""
    <div style="background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
        <h2 style="text-align: center; color: #333;">Outils et Activités Intelligents</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Placeholder introduction text for future AI-driven solutions
    st.markdown("""
    <div style="background-color: rgba(93, 95, 239, 0.1); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #5D5FEF; text-align: center;">Solutions IA adaptées</h3>
        <p style="font-size: 1.1rem; text-align: center;">
            Des outils d'intelligence artificielle spécialement conçus pour soutenir 
            les enfants ayant des difficultés d'écriture seront disponibles prochainement.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Refaire le test", key="retake_dysgraphie_test"):
            # Reset test results
            if 'dysgraphie_detailed_results' in st.session_state:
                del st.session_state['dysgraphie_detailed_results']
            if 'dysgraphie_current_step' in st.session_state:
                del st.session_state['dysgraphie_current_step']
            if 'dysgraphie_responses' in st.session_state:
                del st.session_state['dysgraphie_responses']
            
            # Navigate to test page
            st.session_state['page'] = "test_dysgraphie"
            st.rerun()
    
    with col2:
        if st.button("📝 Imprimer les résultats", key="print_dysgraphie_results"):
            st.info("Préparation du PDF pour impression... Cette fonctionnalité sera disponible prochainement.")
    
    with col3:
        if st.button("🏠 Retour à l'accueil", key="home_dysgraphie_results"):
            st.session_state['page'] = "accueil"
            st.rerun()