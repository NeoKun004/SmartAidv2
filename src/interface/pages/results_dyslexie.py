import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from src.utils.llm_utils import generate_dyslexie_recommendations
from src.solutions.dyslexie import provide_dyslexie_solution

def show_page():
    """Display the dyslexia test results page"""
    st.title("📊 Résultats du Test de Dyslexie 📝")
    
    # Check if test results exist
    if 'dyslexie_detailed_results' not in st.session_state:
        st.error("⚠️ Aucun résultat de test disponible. Veuillez d'abord passer le test.")
        
        # Return to home button
        if st.button("🏠 Retourner à l'accueil", key="home_return_dyslexie"):
            st.session_state['page'] = "accueil"
            st.rerun()
            
        return
    
    # User info display
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"👤 Nom: {st.session_state.get('dyslexie_nom', 'Khalil Baccouche')}")
    with col2:
        st.info(f"🎂 Age: {st.session_state.get('dyslexie_age', 8)}")
    with col3:
        st.info(f"🏫 Classe: {st.session_state.get('dyslexie_classe', 'CE2')}")
    
    # Extract scores from session state
    results = st.session_state['dyslexie_detailed_results']
    
    # Calculate total score and percentage
    total_score = sum(test_data["score"] for test_data in results.values())
    max_score = sum(test_data["max"] for test_data in results.values())
    percentage = round((total_score / max_score) * 100)
    
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
            recommendations = "Une évaluation approfondie par un orthophoniste est fortement recommandée."
        elif percentage < 70:
            risk_level = "Modéré"
            color = "orange"
            recommendations = "Certains signes suggèrent des difficultés en lecture. Une évaluation professionnelle pourrait être bénéfique."
        else:
            risk_level = "Faible"
            color = "green"
            recommendations = "Peu de signes de dyslexie détectés. Continuez à encourager la lecture!"
        
        st.markdown(f"""
        <div style="background-color: {color}25; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">
            <h3 style="color: {color};">Niveau de risque de dyslexie: {risk_level}</h3>
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
        "denomination_rapide": "Dénomination Rapide",
        "pseudo_mots": "Décodage Pseudo-Mots",
        "suppression_phonemique": "Suppression Phonémique",
        "fluidite_lecture": "Fluidité de Lecture",
        "memoire_sons": "Mémoire des Sons",
        "confusion_lettres": "Confusion de Lettres"
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
    
    # Fixed: HTML rendering for observations section
    st.markdown("""
    <div style="background-color: rgba(255, 82, 82, 0.1); padding: 20px; border-radius: 10px; margin: 15px 0;">
        <h3 style="color: #ff5252;">Difficultés Identifiées</h3>
        
        <h4 style="margin-top: 15px;">Vitesse de traitement</h4>
        <p>Lucas présente une lenteur significative dans la reconnaissance des lettres et la lecture, ce qui est un signe caractéristique de la dyslexie.</p>
        
        <h4 style="margin-top: 15px;">Décodage phonologique</h4>
        <p>Il montre des difficultés importantes à lire des mots nouveaux en s'appuyant sur les sons, avec des erreurs de substitution et d'omission.</p>
        
        <h4 style="margin-top: 15px;">Manipulation phonémique</h4>
        <p>Lucas a du mal à manipuler mentalement les sons dans les mots, ce qui révèle une faiblesse de la conscience phonologique.</p>
        
        <h4 style="margin-top: 15px;">Mémoire de travail phonologique</h4>
        <p>Les erreurs dans la répétition des séquences de lettres indiquent des difficultés de mémoire à court terme pour les sons.</p>
        
        <h4 style="margin-top: 15px;">Confusions visuelles</h4>
        <p>Des confusions entre lettres similaires (b/d) sont observées, ce qui est typique de la dyslexie.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Recommendations section
    st.markdown("""
    <div style="background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
        <h2 style="text-align: center; color: #333;">Recommandations</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Fixed: HTML rendering for recommendations
    st.markdown("""
    <div style="background-color: rgba(0, 150, 199, 0.1); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #0096c7;">Recommandations pour Lucas</h3>
        
        <h4 style="margin-top: 15px;">1. Évaluation professionnelle</h4>
        <p>Il est fortement recommandé de consulter un orthophoniste pour une évaluation complète et un diagnostic précis de dyslexie.</p>
        
        <h4 style="margin-top: 15px;">2. Entraînement phonologique quotidien</h4>
        <p>Pratiquer quotidiennement des exercices de conscience phonologique pour renforcer la perception et la manipulation des sons.</p>
        
        <h4 style="margin-top: 15px;">3. Méthode multisensorielle</h4>
        <p>Utiliser des approches multisensorielles (visuelle, auditive, tactile) pour faciliter l'apprentissage de la lecture.</p>
        
        <h4 style="margin-top: 15px;">4. Lecture guidée régulière</h4>
        <p>Mettre en place des sessions quotidiennes de lecture guidée de 10-15 minutes avec un adulte.</p>
        
        <h4 style="margin-top: 15px;">5. Aménagements scolaires</h4>
        <p>Discuter avec l'enseignant pour mettre en place des adaptations: temps supplémentaire, textes adaptés, lecture à voix haute des consignes.</p>
        
        <h4 style="margin-top: 15px;">6. Renforcement de la mémoire de travail</h4>
        <p>Pratiquer des jeux de mémoire verbale quotidiennement pour améliorer la rétention des sons et des lettres.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive solutions section - Updated introduction for new AI-driven approach
    st.markdown("""
    <div style="background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
        <h2 style="text-align: center; color: #333;">Outils et Activités Intelligents</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Updated introduction text for the new AI-driven solutions
    st.markdown("""
    <div style="background-color: rgba(93, 95, 239, 0.1); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="color: #5D5FEF; text-align: center;">Solutions IA adaptées pour Lucas</h3>
        <p style="font-size: 1.1rem; text-align: center;">
            Découvrez nos outils d'intelligence artificielle spécialement conçus pour soutenir 
            les enfants dyslexiques dans leur apprentissage de la lecture.
        </p>
        <p style="font-size: 1.0rem; text-align: center;">
            Ces outils interactifs s'adaptent aux besoins spécifiques de Lucas et évoluent avec ses progrès.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get interactive solutions
    provide_dyslexie_solution(percentage)
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Refaire le test", key="retake_dyslexie_test"):
            # Reset test results
            if 'dyslexie_detailed_results' in st.session_state:
                del st.session_state['dyslexie_detailed_results']
            if 'dyslexie_current_step' in st.session_state:
                del st.session_state['dyslexie_current_step']
            if 'dyslexie_recommendations' in st.session_state:
                del st.session_state['dyslexie_recommendations']
            
            # Navigate to test page
            st.session_state['page'] = "test_dyslexie"
            st.rerun()
    
    with col2:
        if st.button("📝 Imprimer les résultats", key="print_dyslexie_results"):
            st.info("Préparation du PDF pour impression... Cette fonctionnalité sera disponible prochainement.")
    
    with col3:
        if st.button("🏠 Retour à l'accueil", key="home_dyslexie_results"):
            st.session_state['page'] = "accueil"
            st.rerun()