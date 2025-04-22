"""
Solution module for TDAH (Attention Deficit Hyperactivity Disorder).

This module provides personalized learning activities and tools
for students who struggle with attention, impulsivity, and organization.
"""

import streamlit as st
import random
from typing import Dict, Any

def generate_tdah_prompt(analysis_results: str, user_info: Dict[str, Any]) -> str:
    """
    Generates a custom prompt for the LLM to create a tailored solution
    for a student with TDAH.
    
    Args:
        analysis_results: Analysis of test results as string
        user_info: User information (age, name, class, etc.)
        
    Returns:
        A prompt string for the LLM
    """
    age = user_info.get("age", "unknown")
    class_level = user_info.get("classe", "unknown")
    name = user_info.get("nom", "l'élève")
    
    # Extract detailed results if available
    detailed_results = user_info.get("detailed_results", {})
    
    # Create detailed performance report
    performance_report = ""
    
    if detailed_results:
        # Compute category scores
        for category, data in detailed_results.items():
            score = data["score"]
            max_score = data["max"]
            performance_report += f"- {category.capitalize()}: {score}/{max_score}\n"
    
    # Create the prompt with detailed information about the student's difficulties
    prompt = f"""
    Tu es un assistant pédagogique spécialisé pour les élèves ayant un TDAH (Trouble du Déficit de l'Attention avec ou sans Hyperactivité).

    Informations sur l'élève:
    - Nom: {name}
    - Âge: {age} ans
    - Niveau scolaire: {class_level}
    
    Performance au test d'attention:
    {performance_report}
    
    Analyse des résultats:
    {analysis_results}
    
    Ta mission est de créer un plan d'apprentissage personnalisé qui aide cet élève à gérer son attention et son organisation. Le plan doit inclure exactement les sections suivantes:

    1. TROIS techniques visuelles pour aider à l'organisation et à la planification. Chaque technique doit être très concrète, pratique, et utiliser des objets ou des images colorés.

    2. DEUX jeux amusants qui améliorent la concentration et l'attention. Les jeux doivent être adaptés à un enfant de {age} ans et doivent pouvoir être joués avec du matériel simple.

    3. UN système de récompense et de motivation expliqué étape par étape, qui encourage l'enfant à rester concentré. Ce système doit être présenté comme un processus très visuel.

    4. TROIS messages d'encouragement spécifiques à l'attention et à l'organisation qui renforcent la confiance. Ces messages doivent être positifs, colorés, et adaptés à un enfant de {age} ans.

    Rends tout le contenu attractif et approprié pour un enfant de {age} ans. Utilise un langage simple, des émojis, et de nombreuses métaphores visuelles.
    
    IMPORTANT: Tu dois formater ta réponse EXACTEMENT selon la structure suivante, en gardant ces titres markdown précis:
    
    ## Techniques d'Organisation Visuelles
    
    [Trois techniques détaillées avec explications claires]
    
    ## Jeux pour Améliorer l'Attention
    
    [Deux jeux détaillés avec règles claires]
    
    ## Système de Récompense
    
    [Système de motivation pas à pas avec exemples]
    
    ## Messages d'Encouragement
    
    [Trois messages motivants numérotés]
    """
    
    return prompt

def parse_tdah_solution(llm_response: str) -> Dict[str, Any]:
    """
    Parses the LLM response into structured solution components.
    
    Args:
        llm_response: Raw response from the LLM
        
    Returns:
        Dictionary with parsed solution components
    """
    # Simple parsing based on markdown headers
    sections = {
        "organization_techniques": "",
        "attention_games": "",
        "reward_system": "",
        "encouraging_messages": ""
    }
    
    current_section = None
    
    lines = llm_response.split('\n')
    for i, line in enumerate(lines):
        # Check what section we're in
        if "## Techniques d'Organisation Visuelles" in line:
            current_section = "organization_techniques"
            continue
        elif "## Jeux pour Améliorer l'Attention" in line:
            current_section = "attention_games"
            continue
        elif "## Système de Récompense" in line:
            current_section = "reward_system"
            continue
        elif "## Messages d'Encouragement" in line:
            current_section = "encouraging_messages"
            continue
        
        # Add the line to the current section if we're in a section
        if current_section and line.strip():
            sections[current_section] += line + "\n"
    
    return sections

def display_tdah_solution(solution_components: Dict[str, Any]) -> None:
    """
    Displays the TDAH solution components in the Streamlit UI.
    
    Args:
        solution_components: Parsed solution components from the LLM
    """
    # Setup nice, colorful containers for each section
    
    # Display Organization Techniques
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #4ECDC4;">
        <h3 style="color: #4ECDC4; text-align: center;">📋 Techniques d'Organisation Visuelles</h3>
    </div>
    """, unsafe_allow_html=True)
    
    organization_techniques = solution_components["organization_techniques"]
    if organization_techniques.strip():
        with st.container():
            st.markdown(organization_techniques)
    else:
        st.warning("Aucune technique d'organisation n'a été générée. Veuillez réessayer.")
    
    # Display Attention Games
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #5D5FEF;">
        <h3 style="color: #5D5FEF; text-align: center;">🎮 Jeux pour Améliorer l'Attention</h3>
    </div>
    """, unsafe_allow_html=True)
    
    attention_games = solution_components["attention_games"]
    if attention_games.strip():
        with st.container():
            st.markdown(attention_games)
    else:
        st.warning("Aucun jeu d'attention n'a été généré. Veuillez réessayer.")
    
    # Display Reward System
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #FF6B6B;">
        <h3 style="color: #FF6B6B; text-align: center;">🏆 Système de Récompense</h3>
    </div>
    """, unsafe_allow_html=True)
    
    reward_system = solution_components["reward_system"]
    if reward_system.strip():
        with st.container():
            st.markdown(reward_system)
    else:
        st.warning("Aucun système de récompense n'a été généré. Veuillez réessayer.")
    
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

def provide_tdah_solution(analysis_results: str, user_info: Dict[str, Any], llm_connector) -> None:
    """
    Main function to provide TDAH solutions.
    
    Args:
        analysis_results: Analysis of test results as string
        user_info: User information (age, name, class, etc.)
        llm_connector: Instance of the LLM connector
    """
    # Check if we already have solutions in session state to avoid re-generating
    if 'tdah_solution' not in st.session_state:
        try:
            # Generate prompt for the LLM
            prompt = generate_tdah_prompt(analysis_results, user_info)
            
            # Get system prompt
            system_prompt = "Tu es un assistant pédagogique spécialisé pour les enfants ayant des troubles d'attention et d'hyperactivité. Ton objectif est de créer du matériel d'apprentissage attrayant, coloré et efficace qui aide les enfants à améliorer leur concentration et leur organisation."
            
            # Get response from LLM
            with st.spinner("Création de solutions personnalisées en cours..."):
                llm_response = llm_connector.generate_response(
                    prompt=prompt,
                    system_prompt=system_prompt,
                    max_tokens=2000,  # Increased token limit for more detailed responses
                    temperature=0.7
                )
                
                # Parse the response
                solution_components = parse_tdah_solution(llm_response)
                
                # Store in session state
                st.session_state['tdah_solution'] = solution_components
                
        except Exception as e:
            st.error(f"Une erreur s'est produite lors de la génération des solutions: {str(e)}")
            
            # Provide a fallback solution if generation fails
            fallback_solution = {
                "organization_techniques": "### Technique 1: Tableau de Tâches Coloré\nCrée un tableau avec des post-it de couleurs différentes pour chaque type de tâche. Le vert pour les devoirs, le bleu pour les activités personnelles, etc.",
                "attention_games": "### Jeu 1: Le Détective des Détails\nObserve une image pendant 30 secondes, puis cache-la et essaie de te rappeler autant de détails que possible.",
                "reward_system": "### Système de Points\nChaque fois que tu termines une tâche sans te distraire, tu gagnes 2 points. Avec 10 points, tu peux choisir une récompense comme 15 minutes de jeu vidéo ou une collation spéciale.",
                "encouraging_messages": "1. Chaque petit pas est une grande victoire pour ton cerveau!\n2. Tu as le super-pouvoir de contrôler ton attention quand tu le décides!\n3. Les erreurs sont normales, c'est en essayant qu'on devient un champion de la concentration!"
            }
            st.session_state['tdah_solution'] = fallback_solution
    
    # Display tabs for different solution types
    tab1, tab2 = st.tabs(["📚 Conseils et exercices", "🎮 Activités interactives"])
    
    with tab1:
        # Display the solution
        display_tdah_solution(st.session_state['tdah_solution'])
        
    with tab2:
        # Display interactive attention activities
        display_interactive_tdah_activities()
        
def display_interactive_tdah_activities():
    """
    Display interactive activities for TDAH.
    """
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #5D5FEF;">
        <h3 style="color: #5D5FEF; text-align: center;">🎮 Activités Interactives pour l'Attention</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Menu pour choisir l'activité
    activity = st.selectbox(
        "Choisis une activité :",
        ["Chasse aux mots", "Jeu de la mémoire", "Trouve l'ordre"]
    )
    
    if activity == "Chasse aux mots":
        display_word_hunter_game()
    elif activity == "Jeu de la mémoire":
        display_memory_game()
    elif activity == "Trouve l'ordre":
        display_sequence_game()

def display_word_hunter_game():
    """Display the word hunting game for attention."""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #FF6B6B; text-align: center;">🔍 Chasse aux Mots</h3>
        <p style="text-align: center;">Clique sur tous les mots d'animaux qui apparaissent!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize game state
    if 'word_hunter_state' not in st.session_state:
        st.session_state['word_hunter_state'] = {
            'words': [],
            'animal_words': [],
            'score': 0,
            'clicks': [],
            'game_started': False,
            'game_over': False
        }
    
    # Game configuration
    if not st.session_state['word_hunter_state']['game_started']:
        # Lists of words
        animal_words = ["chat", "chien", "lion", "tigre", "oiseau", "poisson", "lapin", "souris", "écureuil", "éléphant"]
        other_words = ["table", "chaise", "voiture", "maison", "livre", "stylo", "école", "fenêtre", "porte", "jardin",
                      "soleil", "nuage", "rivière", "montagne", "arbre", "fleur", "télévision", "téléphone", "ordinateur", "ballon"]
        
        # Select random words
        selected_animals = random.sample(animal_words, 5)
        selected_others = random.sample(other_words, 10)
        all_words = selected_animals + selected_others
        random.shuffle(all_words)
        
        # Save to session state
        st.session_state['word_hunter_state']['words'] = all_words
        st.session_state['word_hunter_state']['animal_words'] = selected_animals
        st.session_state['word_hunter_state']['game_started'] = True
    
    # Display game
    if not st.session_state['word_hunter_state']['game_over']:
        # Create a grid of words
        cols = st.columns(3)
        for i, word in enumerate(st.session_state['word_hunter_state']['words']):
            col_idx = i % 3
            with cols[col_idx]:
                # Check if already clicked
                if i in st.session_state['word_hunter_state']['clicks']:
                    is_animal = word in st.session_state['word_hunter_state']['animal_words']
                    bg_color = "#4ECDC4" if is_animal else "#FF6B6B"
                    st.markdown(f"""
                    <div style="background-color: {bg_color}; padding: 10px; border-radius: 10px; margin: 5px; text-align: center; color: white;">
                        {word} {"✓" if is_animal else "✗"}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    if st.button(word, key=f"word_{i}"):
                        st.session_state['word_hunter_state']['clicks'].append(i)
                        if word in st.session_state['word_hunter_state']['animal_words']:
                            st.session_state['word_hunter_state']['score'] += 1
                        st.rerun()
    
        # Display score
        animal_count = len(st.session_state['word_hunter_state']['animal_words'])
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 10px; border-radius: 10px; margin-top: 15px; text-align: center;">
            <p style="font-size: 1.2rem;">Score: {st.session_state['word_hunter_state']['score']}/{animal_count} animaux trouvés</p>
        </div>
        """, unsafe_allow_html=True)
        
        # End game if all animals found or too many clicks
        if st.session_state['word_hunter_state']['score'] == animal_count or len(st.session_state['word_hunter_state']['clicks']) >= 10:
            st.session_state['word_hunter_state']['game_over'] = True
            st.rerun()
    
    else:
        # Game over screen
        final_score = st.session_state['word_hunter_state']['score']
        animal_count = len(st.session_state['word_hunter_state']['animal_words'])
        
        if final_score == animal_count:
            st.success(f"🎉 Bravo! Tu as trouvé tous les {animal_count} animaux!")
            st.balloons()
        else:
            st.warning(f"Tu as trouvé {final_score} animaux sur {animal_count}. Continue à t'entraîner!")
        
        # Show all correct answers
        st.markdown("### Les animaux à trouver étaient:")
        for animal in st.session_state['word_hunter_state']['animal_words']:
            st.markdown(f"- {animal}")
        
        # Restart button
        if st.button("Jouer à nouveau", key="restart_word_hunter"):
            del st.session_state['word_hunter_state']
            st.rerun()

def display_memory_game():
    """Display the memory/concentration game."""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #5D5FEF; text-align: center;">🧠 Jeu de la Mémoire</h3>
        <p style="text-align: center;">Observe les formes pendant 5 secondes, puis essaie de t'en souvenir!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize game state
    if 'memory_game_state' not in st.session_state:
        st.session_state['memory_game_state'] = {
            'phase': 'setup',  # setup, memorize, recall, results
            'shapes': [],
            'user_answers': [],
            'correct_answers': 0
        }
    
    # Game phases
    if st.session_state['memory_game_state']['phase'] == 'setup':
        # Game settings
        st.write("Choisis la difficulté du jeu:")
        difficulty = st.radio("Difficulté:", ["Facile (3 formes)", "Moyen (5 formes)", "Difficile (7 formes)"])
        
        if st.button("Commencer le jeu", key="start_memory_game"):
            # Determine number of shapes based on difficulty
            num_shapes = 3 if "Facile" in difficulty else (5 if "Moyen" in difficulty else 7)
            
            # Possible shapes and colors
            shapes = ["Cercle", "Carré", "Triangle", "Étoile", "Coeur", "Losange", "Rectangle"]
            colors = ["Rouge", "Bleu", "Vert", "Jaune", "Orange", "Violet", "Rose"]
            
            # Generate random shape-color combinations
            shape_combos = []
            for _ in range(num_shapes):
                shape = random.choice(shapes)
                color = random.choice(colors)
                shape_combos.append((shape, color))
            
            # Save to session state
            st.session_state['memory_game_state']['shapes'] = shape_combos
            st.session_state['memory_game_state']['phase'] = 'memorize'
            st.rerun()
    
    elif st.session_state['memory_game_state']['phase'] == 'memorize':
        # Display shapes to memorize
        st.markdown("### 👀 Mémorise ces formes et leurs couleurs:")
        
        # Display shapes in a grid
        cols = st.columns(3)
        for i, (shape, color) in enumerate(st.session_state['memory_game_state']['shapes']):
            col_idx = i % 3
            with cols[col_idx]:
                # Map shapes to emojis
                shape_emojis = {
                    "Cercle": "⭕", "Carré": "🟥", "Triangle": "🔺", 
                    "Étoile": "⭐", "Coeur": "❤️", "Losange": "🔶", "Rectangle": "🟪"
                }
                emoji = shape_emojis.get(shape, "📦")
                
                st.markdown(f"""
                <div style="padding: 10px; border-radius: 10px; margin: 5px; text-align: center; background-color: rgba(255,255,255,0.5);">
                    <p style="font-size: 2rem; margin: 0;">{emoji}</p>
                    <p style="margin: 0;">{shape} {color}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Countdown timer
        import time
        for countdown in range(5, 0, -1):
            st.markdown(f"""
            <div style="text-align: center; font-size: 1.5rem; margin-top: 20px;">
                Mémorise en {countdown} secondes...
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1)
            st.rerun()
        
        # Move to recall phase
        st.session_state['memory_game_state']['phase'] = 'recall'
        st.rerun()
    
    elif st.session_state['memory_game_state']['phase'] == 'recall':
        # Ask user to recall shapes and colors
        st.markdown("### 🤔 Quelles formes et couleurs as-tu mémorisé?")
        
        # Initialize user answers if empty
        shapes = ["Cercle", "Carré", "Triangle", "Étoile", "Coeur", "Losange", "Rectangle"]
        colors = ["Rouge", "Bleu", "Vert", "Jaune", "Orange", "Violet", "Rose"]
        
        if not st.session_state['memory_game_state']['user_answers']:
            for i in range(len(st.session_state['memory_game_state']['shapes'])):
                st.session_state['memory_game_state']['user_answers'].append({"shape": "", "color": ""})
        
        # Display input fields for each shape to recall
        for i in range(len(st.session_state['memory_game_state']['shapes'])):
            st.markdown(f"### Forme {i+1}:")
            col1, col2 = st.columns(2)
            
            with col1:
                shape = st.selectbox(f"Forme {i+1}", [""] + shapes, key=f"shape_{i}")
                st.session_state['memory_game_state']['user_answers'][i]["shape"] = shape
            
            with col2:
                color = st.selectbox(f"Couleur {i+1}", [""] + colors, key=f"color_{i}")
                st.session_state['memory_game_state']['user_answers'][i]["color"] = color
        
        # Submit button
        if st.button("Valider mes réponses", key="submit_memory"):
            # Count correct answers
            correct = 0
            for i, (actual_shape, actual_color) in enumerate(st.session_state['memory_game_state']['shapes']):
                user_shape = st.session_state['memory_game_state']['user_answers'][i]["shape"]
                user_color = st.session_state['memory_game_state']['user_answers'][i]["color"]
                
                if user_shape == actual_shape and user_color == actual_color:
                    correct += 1
            
            st.session_state['memory_game_state']['correct_answers'] = correct
            st.session_state['memory_game_state']['phase'] = 'results'
            st.rerun()
    
    elif st.session_state['memory_game_state']['phase'] == 'results':
        # Display results
        correct = st.session_state['memory_game_state']['correct_answers']
        total = len(st.session_state['memory_game_state']['shapes'])
        
        if correct == total:
            st.success(f"🎉 Parfait! Tu as trouvé toutes les {total} formes et leurs couleurs!")
            st.balloons()
        elif correct >= total / 2:
            st.success(f"👍 Bien joué! Tu as trouvé {correct} formes sur {total}!")
        else:
            st.warning(f"Tu as trouvé {correct} formes sur {total}. Continue à t'entraîner!")
        
        # Show correct answers vs user answers
        st.markdown("### Comparaison des réponses:")
        
        for i, (actual_shape, actual_color) in enumerate(st.session_state['memory_game_state']['shapes']):
            user_shape = st.session_state['memory_game_state']['user_answers'][i]["shape"]
            user_color = st.session_state['memory_game_state']['user_answers'][i]["color"]
            
            is_correct = (user_shape == actual_shape and user_color == actual_color)
            
            st.markdown(f"""
            <div style="background-color: {"rgba(78, 205, 196, 0.3)" if is_correct else "rgba(255, 107, 107, 0.3)"}; padding: 10px; border-radius: 10px; margin-bottom: 10px;">
                <h4>Forme {i+1}:</h4>
                <p>Réponse correcte: {actual_shape} {actual_color}</p>
                <p>Ta réponse: {user_shape} {user_color}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Restart button
        if st.button("Jouer à nouveau", key="restart_memory"):
            del st.session_state['memory_game_state']
            st.rerun()

def display_sequence_game():
    """Display the sequence ordering game."""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #4ECDC4; text-align: center;">📋 Trouve l'Ordre</h3>
        <p style="text-align: center;">Remets ces actions dans le bon ordre!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize game state
    if 'sequence_game_state' not in st.session_state:
        # Different sequence scenarios
        scenarios = [
            {
                "title": "Faire un gâteau",
                "steps": [
                    "Ajouter le sucre et la farine",
                    "Mélanger les ingrédients",
                    "Mettre le gâteau au four",
                    "Sortir le gâteau et le laisser refroidir"
                ]
            },
            {
                "title": "Se préparer pour l'école",
                "steps": [
                    "Se réveiller et sortir du lit",
                    "S'habiller",
                    "Prendre le petit déjeuner",
                    "Mettre son cartable et partir"
                ]
            },
            {
                "title": "Planter une graine",
                "steps": [
                    "Creuser un trou dans la terre",
                    "Placer la graine dans le trou",
                    "Recouvrir de terre",
                    "Arroser la graine"
                ]
            }
        ]
        
        # Choose random scenario
        scenario = random.choice(scenarios)
        steps = scenario["steps"].copy()
        random.shuffle(steps)
        
        st.session_state['sequence_game_state'] = {
            'title': scenario["title"],
            'correct_steps': scenario["steps"],
            'shuffled_steps': steps,
            'user_order': [],
            'game_complete': False
        }
    
    # Display game
    st.markdown(f"### {st.session_state['sequence_game_state']['title']}")
    
    # Instructions
    st.write("Clique sur les actions dans l'ordre correct :")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Display available steps
        for i, step in enumerate(st.session_state['sequence_game_state']['shuffled_steps']):
            if step not in st.session_state['sequence_game_state']['user_order']:
                if st.button(f"{step}", key=f"step_{i}"):
                    st.session_state['sequence_game_state']['user_order'].append(step)
                    
                    # Check if game is complete
                    if len(st.session_state['sequence_game_state']['user_order']) == len(st.session_state['sequence_game_state']['correct_steps']):
                        st.session_state['sequence_game_state']['game_complete'] = True
                    
                    st.rerun()
    
    with col2:
        # Display current order
        st.write("Ton ordre actuel :")
        for i, step in enumerate(st.session_state['sequence_game_state']['user_order']):
            st.markdown(f"{i+1}. {step}")
    
    # Game completion logic
    if st.session_state['sequence_game_state']['game_complete']:
        # Check if order is correct
        is_correct = st.session_state['sequence_game_state']['user_order'] == st.session_state['sequence_game_state']['correct_steps']
        
        if is_correct:
            st.success("🎉 Bravo! Tu as mis les étapes dans le bon ordre!")
            st.balloons()
        else:
            st.error("Ce n'est pas tout à fait le bon ordre. Essaie encore!")
            
            # Show correct order
            st.markdown("### Ordre correct :")
            for i, step in enumerate(st.session_state['sequence_game_state']['correct_steps']):
                st.markdown(f"{i+1}. {step}")
        
        # Restart button
        if st.button("Jouer avec une nouvelle séquence", key="restart_sequence"):
            del st.session_state['sequence_game_state']
            st.rerun()
    
    # Reset button
    if st.button("Recommencer cette séquence", key="reset_current_sequence"):
        st.session_state['sequence_game_state']['user_order'] = []
        st.session_state['sequence_game_state']['game_complete'] = False
        st.rerun()


def display_reaction_game():
    """Display a reaction time game to help with impulsivity."""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #FFD166; text-align: center;">🎯 Jeu de Temps de Réaction</h3>
        <p style="text-align: center;">Attends que la cible devienne verte avant de cliquer!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialisation du jeu
    if 'reaction_game_state' not in st.session_state:
        st.session_state['reaction_game_state'] = {
            'phase': 'waiting',  # waiting, ready, clicked
            'start_time': None,
            'click_time': None,
            'reaction_time': None,
            'attempts': [],
            'best_time': None
        }
    
    # Affichage selon la phase du jeu
    if st.session_state['reaction_game_state']['phase'] == 'waiting':
        # Bouton pour démarrer
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style="background-color: #FF6B6B; padding: 30px; border-radius: 15px; text-align: center; margin: 20px 0;">
                <h2 style="color: white; margin: 0;">ATTENDS...</h2>
                <p style="color: white; margin: 10px 0 0 0;">Prépare-toi à cliquer quand la cible devient VERTE</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🚦 Commencer le jeu", key="start_reaction_game"):
                # Générer un délai aléatoire entre 2 et 5 secondes
                import time
                import random
                
                st.session_state['reaction_game_state']['phase'] = 'ready'
                st.session_state['reaction_game_state']['start_time'] = time.time() + random.uniform(2, 5)
                st.rerun()
    
    elif st.session_state['reaction_game_state']['phase'] == 'ready':
        import time
        current_time = time.time()
        start_time = st.session_state['reaction_game_state']['start_time']
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # Si c'est le moment de cliquer
            if current_time >= start_time:
                st.markdown("""
                <div style="background-color: #4ECDC4; padding: 30px; border-radius: 15px; text-align: center; margin: 20px 0; cursor: pointer;">
                    <h2 style="color: white; margin: 0;">MAINTENANT!</h2>
                    <p style="color: white; margin: 10px 0 0 0;">Clique rapidement!</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Enregistrer le temps de début pour calculer le temps de réaction
                if not st.session_state['reaction_game_state'].get('green_time'):
                    st.session_state['reaction_game_state']['green_time'] = current_time
                
                if st.button("🎯 CLIQUE!", key="click_reaction"):
                    st.session_state['reaction_game_state']['click_time'] = time.time()
                    st.session_state['reaction_game_state']['phase'] = 'clicked'
                    
                    # Calculer le temps de réaction
                    green_time = st.session_state['reaction_game_state']['green_time']
                    click_time = st.session_state['reaction_game_state']['click_time']
                    reaction_time = round((click_time - green_time) * 1000) # en millisecondes
                    
                    st.session_state['reaction_game_state']['reaction_time'] = reaction_time
                    st.session_state['reaction_game_state']['attempts'].append(reaction_time)
                    
                    # Mettre à jour le meilleur temps
                    if st.session_state['reaction_game_state']['best_time'] is None or reaction_time < st.session_state['reaction_game_state']['best_time']:
                        st.session_state['reaction_game_state']['best_time'] = reaction_time
                    
                    st.rerun()
            else:
                # Afficher un message d'attente
                st.markdown("""
                <div style="background-color: #FF6B6B; padding: 30px; border-radius: 15px; text-align: center; margin: 20px 0;">
                    <h2 style="color: white; margin: 0;">ATTENDS...</h2>
                    <p style="color: white; margin: 10px 0 0 0;">Pas encore! Attends que la cible devienne verte</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Si l'utilisateur clique trop tôt
                if st.button("⚠️ Je veux cliquer maintenant", key="early_click"):
                    st.session_state['reaction_game_state']['phase'] = 'clicked'
                    st.session_state['reaction_game_state']['reaction_time'] = -1  # Trop tôt
                    st.rerun()
                
                # Auto-refresh pour vérifier le temps
                time.sleep(0.1)
                st.rerun()
    
    elif st.session_state['reaction_game_state']['phase'] == 'clicked':
        reaction_time = st.session_state['reaction_game_state']['reaction_time']
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if reaction_time == -1:
                # Trop tôt
                st.markdown("""
                <div style="background-color: #FF6B6B; padding: 30px; border-radius: 15px; text-align: center; margin: 20px 0;">
                    <h2 style="color: white; margin: 0;">TROP TÔT!</h2>
                    <p style="color: white; margin: 10px 0 0 0;">Tu as cliqué avant que la cible devienne verte. Essaie encore!</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                # Afficher le résultat
                if reaction_time < 300:
                    color = "#4ECDC4"
                    message = "EXCELLENT! Tu as des réflexes fulgurants!"
                elif reaction_time < 500:
                    color = "#5D5FEF"
                    message = "TRÈS BON! Tes réflexes sont au-dessus de la moyenne!"
                elif reaction_time < 800:
                    color = "#FFD166"
                    message = "BON! C'est un temps de réaction normal."
                else:
                    color = "#FF6B6B"
                    message = "Continue de t'entraîner, tu peux t'améliorer!"
                
                st.markdown(f"""
                <div style="background-color: {color}; padding: 30px; border-radius: 15px; text-align: center; margin: 20px 0;">
                    <h2 style="color: white; margin: 0;">{reaction_time} ms</h2>
                    <p style="color: white; margin: 10px 0 0 0;">{message}</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Afficher les statistiques
            if len(st.session_state['reaction_game_state']['attempts']) > 0 and st.session_state['reaction_game_state']['best_time'] is not None:
                valid_attempts = [t for t in st.session_state['reaction_game_state']['attempts'] if t > 0]
                if valid_attempts:
                    avg_time = round(sum(valid_attempts) / len(valid_attempts))
                    best_time = st.session_state['reaction_game_state']['best_time']
                    
                    st.markdown(f"""
                    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin: 20px 0; text-align: center;">
                        <h3 style="margin: 0;">Tes statistiques</h3>
                        <p>Meilleur temps: <strong>{best_time} ms</strong></p>
                        <p>Temps moyen: <strong>{avg_time} ms</strong></p>
                        <p>Nombre d'essais: <strong>{len(st.session_state['reaction_game_state']['attempts'])}</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Bouton pour rejouer
            if st.button("🔄 Rejouer", key="replay_reaction_game"):
                # Réinitialiser seulement certains éléments pour garder les statistiques
                st.session_state['reaction_game_state']['phase'] = 'waiting'
                st.session_state['reaction_game_state']['start_time'] = None
                st.session_state['reaction_game_state']['click_time'] = None
                st.session_state['reaction_game_state']['reaction_time'] = None
                if 'green_time' in st.session_state['reaction_game_state']:
                    del st.session_state['reaction_game_state']['green_time']
                st.rerun()
    
    # Bouton pour réinitialiser complètement
    if st.button("🔄 Réinitialiser toutes les statistiques", key="reset_reaction_game"):
        del st.session_state['reaction_game_state']
        st.rerun()