"""
Activities manager for dyscalculia and other learning disabilities.

This module manages the available interactive activities and handles
selecting appropriate activities based on identified difficulties.
"""

import streamlit as st
import json
import re
from typing import Dict, Any, List

# Import the activity display functions
from .interactive_components import (
    display_number_line_activity,
    display_calculator_activity, 
    display_comparison_activity,
    display_monster_game
)

# Define our available interactive activities with their mappings to difficulty types
AVAILABLE_ACTIVITIES = {
    "number_line": {
        "title": "Ligne Numérique Interactive",
        "description": "Visualise les nombres et leur ordre pour mieux comprendre les séquences numériques.",
        "difficulty_types": ["reconnaissance_nombres", "suites"],
        "display_function": display_number_line_activity
    },
    "calculator": {
        "title": "Calculatrice Pas-à-Pas",
        "description": "Décompose les calculs en étapes simples pour maîtriser les opérations de base.",
        "difficulty_types": ["calcul", "operations"],
        "display_function": display_calculator_activity
    },
    "comparison": {
        "title": "Balance des Nombres",
        "description": "Compare différentes quantités pour mieux comprendre les relations entre les nombres.",
        "difficulty_types": ["comparaison", "estimation"],
        "display_function": display_comparison_activity
    },
    "monster_game": {
        "title": "La Chasse aux Monstres",
        "description": "Capture des monstres en résolvant des opérations mathématiques!",
        "difficulty_types": ["calcul", "general"],  # Good for everyone
        "display_function": display_monster_game
    }
}

def identify_difficulties(user_info: Dict[str, Any]) -> List[str]:
    """
    Identify specific difficulties based on test responses.
    
    Args:
        user_info: Dictionary with user information and test responses
        
    Returns:
        List of identified difficulty types
    """
    difficulties = []
    
    # Check for numerical recognition issues
    if user_info.get("q1") != 8 or user_info.get("q3") != "10":
        difficulties.append("reconnaissance_nombres")
    
    # Check for calculation issues
    if user_info.get("q1") != 8 or user_info.get("q2") != 6:
        difficulties.append("calcul")
    
    # Check for sequence/pattern issues
    if user_info.get("q3") != "10":
        difficulties.append("suites")
    
    # Check for comparison/measurement issues
    if user_info.get("q4") != "Une voiture":
        difficulties.append("comparaison")
    
    # If no specific difficulties identified, mark as general
    if not difficulties:
        difficulties.append("general")
    
    return difficulties

def generate_activities_prompt(analysis_results: str, user_info: Dict[str, Any]) -> str:
    """
    Generates a prompt for the LLM to select appropriate activities.
    
    Args:
        analysis_results: Analysis of test results as string
        user_info: User information (age, name, class, etc.)
        
    Returns:
        A structured prompt for the LLM
    """
    # Identify difficulties from test results
    difficulties = identify_difficulties(user_info)
    difficulties_str = ", ".join(difficulties)
    
    # Format activity data for prompt
    activity_info = []
    for activity_id, activity in AVAILABLE_ACTIVITIES.items():
        activity_info.append({
            "id": activity_id,
            "title": activity["title"],
            "description": activity["description"],
            "target_difficulties": activity["difficulty_types"]
        })
    
    # Create the prompt
    prompt = f"""
    Tu es un assistant pédagogique spécialisé pour les élèves ayant des difficultés en mathématiques.
    
    Informations sur l'élève:
    - Nom: {user_info.get('nom', 'Student')}
    - Âge: {user_info.get('age', 'unknown')} ans
    - Classe: {user_info.get('classe', 'unknown')}
    - Difficultés identifiées: {difficulties_str}
    
    Analyse des résultats:
    {analysis_results}
    
    Voici la liste des activités disponibles:
    {json.dumps(activity_info, indent=2, ensure_ascii=False)}
    
    Ta mission est de sélectionner les 2-3 activités les plus appropriées pour cet élève,
    en fonction de ses difficultés spécifiques identifiées durant le test.
    
    Réponds UNIQUEMENT avec un tableau JSON contenant les IDs des activités recommandées:
    
    ```json
    ["activity_id1", "activity_id2", "activity_id3"]
    ```
    
    N'inclus aucun autre texte, juste le tableau JSON.
    """
    
    return prompt

def parse_activities_response(llm_response: str) -> List[str]:
    """
    Parses the LLM response to extract recommended activity IDs.
    
    Args:
        llm_response: Raw response from the LLM
        
    Returns:
        List of activity IDs
    """
    # Log the raw response for debugging
    print(f"Raw LLM response: {llm_response}")
    
    # Try to extract JSON from the response
    json_match = re.search(r'```json\s*(.*?)\s*```', llm_response, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
        print(f"Extracted JSON: {json_str}")
    else:
        # If no JSON code block, try to find array directly
        json_match = re.search(r'\[\s*".*"\s*\]', llm_response, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
            print(f"Extracted array: {json_str}")
        else:
            # Fallback to using the whole response
            json_str = llm_response
            print(f"Using whole response as JSON: {json_str}")
    
    try:
        # Parse the JSON
        activity_ids = json.loads(json_str)
        print(f"Parsed activity IDs: {activity_ids}")
        
        # Validate activity IDs
        valid_ids = []
        for activity_id in activity_ids:
            if activity_id in AVAILABLE_ACTIVITIES:
                valid_ids.append(activity_id)
        
        print(f"Valid activity IDs: {valid_ids}")
        
        # Ensure we have at least one valid activity
        if not valid_ids:
            print("No valid activity IDs found, using defaults")
            valid_ids = ["calculator", "monster_game", "number_line"]  # Default activities
        
        return valid_ids
    
    except (json.JSONDecodeError, TypeError) as e:
        # Log the error
        print(f"Error parsing JSON: {str(e)}")
        
        # Provide fallback recommendations
        return ["calculator", "monster_game", "number_line"]  # Default activities

def display_activity_recommendations(recommended_activities: List[str]) -> None:
    """
    Displays the recommended activities with buttons to try them.
    
    Args:
        recommended_activities: List of recommended activity IDs
    """
    # Display recommendations with navigation buttons
    for i, activity_id in enumerate(recommended_activities):
        activity = AVAILABLE_ACTIVITIES.get(activity_id)
        if not activity:
            continue
            
        title = activity["title"]
        description = activity["description"]
        
        # Create a unique key for the button
        button_key = f"btn_activity_{i}_{activity_id}"
        
        # Display the recommendation in a nice container
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 10px; margin-bottom: 10px;">
                <h3 style="margin-top: 0; color: #5D5FEF;">{title}</h3>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Create a button that sets the current activity
            if st.button("Essayer", key=button_key):
                st.session_state['current_activity'] = activity_id
                st.rerun()

def display_selected_activity(activity_id: str) -> None:
    """
    Displays the selected activity and provides a back button.
    
    Args:
        activity_id: ID of the activity to display
    """
    # Get the activity info
    activity = AVAILABLE_ACTIVITIES.get(activity_id)
    if not activity:
        st.error(f"Activité '{activity_id}' non trouvée.")
        return
    
    # Call the display function for this activity
    display_func = activity["display_function"]
    display_func()
    
    # Add a back button
    if st.button("← Retour aux recommandations", key="btn_back_from_activity"):
        st.session_state['current_activity'] = None
        st.rerun()