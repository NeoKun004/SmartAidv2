"""
Solution module for dyscalculia (math learning disability).

This module provides personalized learning activities and tools
for students who struggle with mathematics.
"""

import streamlit as st
from typing import Dict, Any

def generate_dyscalculia_prompt(analysis_results: str, user_info: Dict[str, Any]) -> str:
    """
    Generates a custom prompt for the LLM to create a tailored solution
    for a student with dyscalculia.
    
    Args:
        analysis_results: Analysis of test results as string
        user_info: User information (age, name, class, etc.)
        
    Returns:
        A prompt string for the LLM
    """
    age = user_info.get("age", "unknown")
    class_level = user_info.get("classe", "unknown")
    name = user_info.get("nom", "l'élève")
    
    # Extract test performance if available
    test_performance = ""
    if user_info.get("q1") is not None:
        test_performance += f"- Question 1 (Addition 5+3): {user_info['q1']} (réponse correcte: 8)\n"
    if user_info.get("q2") is not None:
        test_performance += f"- Question 2 (Soustraction 10-4): {user_info['q2']} (réponse correcte: 6)\n"
    if user_info.get("q3") is not None:
        test_performance += f"- Question 3 (Suite logique): {user_info['q3']} (réponse correcte: 10)\n"
    if user_info.get("q4") is not None:
        test_performance += f"- Question 4 (Comparaison): {user_info['q4']} (réponse correcte: Une voiture)\n"
    
    # Create the prompt with detailed information about the student's difficulties
    prompt = f"""
    Tu es un assistant pédagogique spécialisé pour les élèves ayant une dyscalculie (trouble d'apprentissage des mathématiques).

    Informations sur l'élève:
    - Nom: {name}
    - Âge: {age} ans
    - Niveau scolaire: {class_level}
    
    Performance au test de dyscalculie:
    {test_performance}
    
    Analyse des résultats:
    {analysis_results}
    
    Ta mission est de créer un plan d'apprentissage personnalisé qui répond aux besoins spécifiques de cet élève. Le plan doit inclure exactement les sections suivantes:

    1. TROIS exercices visuels de mathématiques qui aident à la compréhension des nombres. Chaque exercice doit être très concret, pratique, et utiliser des objets ou des images que l'enfant peut manipuler.

    2. DEUX jeux amusants qui améliorent le raisonnement mathématique et rendent les mathématiques ludiques. Les jeux doivent être adaptés à un enfant de {age} ans et doivent pouvoir être joués avec du matériel simple (papier, crayons, dés, jetons).

    3. UN outil de "Calculatrice Assistée" expliqué étape par étape, qui montre comment décomposer les calculs pour les rendre plus faciles. Cette méthode doit être présentée comme un processus très visuel.

    4. TROIS messages d'encouragement spécifiques aux mathématiques qui renforcent la confiance. Ces messages doivent être positifs, colorés, et adaptés à un enfant de {age} ans.

    Rends tout le contenu attractif et approprié pour un enfant de {age} ans. Utilise un langage simple, des émojis, et de nombreuses métaphores visuelles.
    
    IMPORTANT: Tu dois formater ta réponse EXACTEMENT selon la structure suivante, en gardant ces titres markdown précis:
    
    ## Exercices Visuels de Mathématiques
    
    [Trois exercices détaillés avec explications claires]
    
    ## Jeux Mathématiques Amusants
    
    [Deux jeux détaillés avec règles claires]
    
    ## Calculatrice Assistée
    
    [Méthode de calcul pas à pas avec exemples]
    
    ## Messages d'Encouragement
    
    [Trois messages motivants numérotés]
    """
    
    return prompt

def parse_dyscalculia_solution(llm_response: str) -> Dict[str, Any]:
    """
    Parses the LLM response into structured solution components.
    
    Args:
        llm_response: Raw response from the LLM
        
    Returns:
        Dictionary with parsed solution components
    """
    # Simple parsing based on markdown headers
    sections = {
        "visual_exercises": "",
        "math_games": "",
        "calculator_helper": "",
        "encouraging_messages": ""
    }
    
    current_section = None
    
    lines = llm_response.split('\n')
    for i, line in enumerate(lines):
        # Check what section we're in
        if "## Exercices Visuels de Mathématiques" in line:
            current_section = "visual_exercises"
            continue
        elif "## Jeux Mathématiques Amusants" in line:
            current_section = "math_games"
            continue
        elif "## Calculatrice Assistée" in line:
            current_section = "calculator_helper"
            continue
        elif "## Messages d'Encouragement" in line:
            current_section = "encouraging_messages"
            continue
        
        # Add the line to the current section if we're in a section
        if current_section and line.strip():
            sections[current_section] += line + "\n"
    
    return sections

def display_dyscalculia_solution(solution_components: Dict[str, Any]) -> None:
    """
    Displays the dyscalculia solution components in the Streamlit UI.
    
    Args:
        solution_components: Parsed solution components from the LLM
    """
    # Setup nice, colorful containers for each section
    
    # Display Visual Math Exercises
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #4ECDC4;">
        <h3 style="color: #4ECDC4; text-align: center;">🧮 Exercices Visuels de Mathématiques</h3>
    </div>
    """, unsafe_allow_html=True)
    
    visual_exercises = solution_components["visual_exercises"]
    if visual_exercises.strip():
        with st.container():
            st.markdown(visual_exercises)
    else:
        st.warning("Aucun exercice visuel n'a été généré. Veuillez réessayer.")
    
    # Display Fun Math Games
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #5D5FEF;">
        <h3 style="color: #5D5FEF; text-align: center;">🎮 Jeux Mathématiques Amusants</h3>
    </div>
    """, unsafe_allow_html=True)
    
    math_games = solution_components["math_games"]
    if math_games.strip():
        with st.container():
            st.markdown(math_games)
    else:
        st.warning("Aucun jeu mathématique n'a été généré. Veuillez réessayer.")
    
    # Display Calculator Helper
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #FF6B6B;">
        <h3 style="color: #FF6B6B; text-align: center;">🔢 Calculatrice Assistée</h3>
    </div>
    """, unsafe_allow_html=True)
    
    calculator_helper = solution_components["calculator_helper"]
    if calculator_helper.strip():
        with st.container():
            st.markdown(calculator_helper)
    else:
        st.warning("Aucune assistance calculatrice n'a été générée. Veuillez réessayer.")
    
    # Display Encouraging Messages
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #FFD166;">
        <h3 style="color: #FFD166; text-align: center;">⭐ Messages d'Encouragement</h3>
    </div>
    """, unsafe_allow_html=True)
    
    encouraging_messages = solution_components["encouraging_messages"]
    if encouraging_messages.strip():
        with st.container():
            st.markdown(encouraging_messages)
    else:
        st.warning("Aucun message d'encouragement n'a été généré. Veuillez réessayer.")

def provide_dyscalculia_solution(analysis_results: str, user_info: Dict[str, Any], llm_connector) -> None:
    """
    Main function to provide dyscalculia solutions.
    
    Args:
        analysis_results: Analysis of test results as string
        user_info: User information (age, name, class, etc.)
        llm_connector: Instance of the LLM connector
    """
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
                    max_tokens=2000,  # Increased token limit for more detailed responses
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
    
    # Display the solution
    display_dyscalculia_solution(st.session_state['dyscalculia_solution'])