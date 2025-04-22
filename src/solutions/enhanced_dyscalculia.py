"""
Enhanced solution module for dyscalculia with both LLM text content
and interactive visual components.
"""

import streamlit as st
from typing import Dict, Any
from src.solutions.dyscalculia import (
    generate_dyscalculia_prompt, 
    parse_dyscalculia_solution, 
    display_dyscalculia_solution
)
# Pour l'importation ci-dessous, il faudra s'assurer que cette fonction existe
from src.solutions.interactive_components import display_interactive_dyscalculia_solution

def provide_enhanced_dyscalculia_solution(analysis_results: str, user_info: Dict[str, Any], llm_connector) -> None:
    """
    Provides an enhanced dyscalculia solution with both text explanations from LLM
    and interactive visual components.
    
    Args:
        analysis_results: Analysis of test results as string
        user_info: User information (age, name, class, etc.)
        llm_connector: Instance of the LLM connector
    """
    # Display tabs to switch between text-based and interactive solutions
    tab1, tab2 = st.tabs(["📚 Exercices et conseils", "🎮 Activités interactives"])
    
    with tab1:
        # Check if we already have solutions in session state to avoid re-generating
        if 'dyscalculia_solution' not in st.session_state:
            try:
                # Generate prompt for the LLM
                prompt = generate_dyscalculia_prompt(analysis_results, user_info)
                
                # Get system prompt
                system_prompt = "Tu es un assistant pédagogique spécialisé pour les enfants ayant des troubles d'apprentissage. Ton objectif est de créer du matériel d'apprentissage attrayant, coloré et efficace qui aide les enfants à surmonter leurs difficultés spécifiques."
                
                # Get response from LLM
                with st.spinner("Création de solutions personnalisées en cours..."):
                    llm_response = llm_connector.generate_response(
                        prompt=prompt,
                        system_prompt=system_prompt,
                        max_tokens=2000,
                        temperature=0.7
                    )
                    
                    # Parse the response
                    solution_components = parse_dyscalculia_solution(llm_response)
                    
                    # Store in session state
                    st.session_state['dyscalculia_solution'] = solution_components
                    
            except Exception as e:
                st.error(f"Une erreur s'est produite lors de la génération des solutions: {str(e)}")
                
                # Provide a fallback solution if generation fails
                fallback_solution = {
                    "visual_exercises": "### Exercice Visuel 1: Les Tours de Nombres\nUtilise des blocs ou des Legos pour représenter les nombres. Chaque bloc vaut 1. Pour représenter 5, construis une tour de 5 blocs.",
                    "math_games": "### Jeu 1: La Chasse aux Trésors des Nombres\nCache des cartes avec des nombres dans la maison. L'enfant doit les trouver et les ranger dans l'ordre croissant.",
                    "calculator_helper": "### Comment calculer étape par étape\nPour additionner 24 + 18:\n1. Sépare les nombres: 24 = 20 + 4, 18 = 10 + 8\n2. Additionne les dizaines: 20 + 10 = 30\n3. Additionne les unités: 4 + 8 = 12\n4. Combine: 30 + 12 = 42",
                    "encouraging_messages": "1. Chaque problème que tu résous te rend plus fort en maths!\n2. Les erreurs sont normales, elles nous aident à apprendre!\n3. Les maths sont comme un jeu, parfois difficile mais toujours amusant quand on comprend!"
                }
                st.session_state['dyscalculia_solution'] = fallback_solution
        
        # Display the text-based solution from LLM
        display_dyscalculia_solution(st.session_state['dyscalculia_solution'])
    
    with tab2:
        # Display interactive components
        display_interactive_dyscalculia_solution()