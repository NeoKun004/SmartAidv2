"""
Improved solution module for dyscalculia with structured recommendations
and direct navigation to interactive activities.
"""

import streamlit as st
from typing import Dict, Any, List

from .activities_manager import (
    generate_activities_prompt,
    parse_activities_response,
    display_activity_recommendations,
    display_selected_activity
)

def provide_improved_dyscalculia_solution(analysis_results: str, user_info: Dict[str, Any], llm_connector) -> None:
    """
    Provides an improved dyscalculia solution with direct navigation
    between structured recommendations and interactive activities.
    
    Args:
        analysis_results: Analysis of test results as string
        user_info: User information (age, name, class, etc.)
        llm_connector: Instance of the LLM connector
    """
    # Initialize session state for activity navigation if not already
    if 'current_activity' not in st.session_state:
        st.session_state['current_activity'] = None
    
    # Initialize recommended_activities with defaults FIRST
    # This prevents the NoneType error
    if 'recommended_activities' not in st.session_state or st.session_state['recommended_activities'] is None:
        st.session_state['recommended_activities'] = ["calculator", "number_line", "monster_game"]
        
        try:
            # Generate prompt for the LLM
            prompt = generate_activities_prompt(analysis_results, user_info)
            
            # Get system prompt
            system_prompt = "Tu es un assistant pédagogique spécialisé pour les enfants ayant des difficultés d'apprentissage. Ta mission est de recommander les activités les plus appropriées pour aider chaque enfant en fonction de ses besoins spécifiques."
            
            # Get response from LLM
            with st.spinner("Création de recommandations personnalisées..."):
                llm_response = llm_connector.generate_response(
                    prompt=prompt,
                    system_prompt=system_prompt,
                    max_tokens=500,
                    temperature=0.5
                )
                
                # Parse the structured recommendations
                temp_activities = parse_activities_response(llm_response)
                
                # Only update if we got valid activities
                if temp_activities is not None and len(temp_activities) > 0:
                    st.session_state['recommended_activities'] = temp_activities
                    
        except Exception as e:
            # Already have defaults, so just log error
            st.error(f"Une erreur s'est produite: {str(e)}")
    
    # Display solutions header
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #4ECDC4;">
        <h2 style="color: #4ECDC4; text-align: center;">💫 Solutions Personnalisées</h2>
        <p style="font-size: 1.2rem; text-align: center;">
            Voici des activités et des outils adaptés pour t'aider en mathématiques!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check if we're viewing a specific activity or showing recommendations
    if st.session_state['current_activity'] is None:
        # Show instructions
        st.info("👇 Clique sur 'Essayer' à côté d'une activité pour la commencer!")
        
        # Display activity recommendations - now guaranteed to be non-None
        display_activity_recommendations(st.session_state['recommended_activities'])
    else:
        # Display the selected activity
        display_selected_activity(st.session_state['current_activity'])