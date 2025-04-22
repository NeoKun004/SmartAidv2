"""
Interactive math activities for students with dyscalculia.

This module contains various visual and interactive components
to help students with math difficulties.
"""

import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any, List

def display_number_line_activity() -> None:
    """Interactive number line visualization activity."""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #5D5FEF;">
        <h2 style="color: #5D5FEF; text-align: center;">📏 Ligne Numérique Interactive</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("Explore la position des nombres sur une ligne. Cet exercice t'aide à comprendre l'ordre et la valeur des nombres.")
    
    # Interactive number line
    max_num = st.slider("Choisis combien de nombres tu veux voir", 5, 20, 10)
    selected_num = st.slider("Sélectionne un nombre sur la ligne", 1, max_num, 5)
    
    # Visualize the number line
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown(f"### Nombre: {selected_num}")
    
    with col2:
        # Visual representation of numbers
        st.markdown("<div style='display: flex; flex-wrap: wrap;'>", unsafe_allow_html=True)
        
        for i in range(1, max_num + 1):
            if i == selected_num:
                st.markdown(f"""
                <div style="background-color: #FF6B6B; width: 40px; height: 40px; 
                     border-radius: 50%; margin: 5px; text-align: center; 
                     line-height: 40px; color: white; font-weight: bold;">
                    {i}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background-color: #4ECDC4; width: 40px; height: 40px; 
                     border-radius: 50%; margin: 5px; text-align: center; 
                     line-height: 40px; color: white;">
                    {i}
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Number ordering game
    st.markdown("### 🧩 Activité: Trouve l'ordre")
    
    # Generate a shuffled sequence if not already in session state
    if 'garden_sequence' not in st.session_state:
        sequence = list(range(1, 6))
        random.shuffle(sequence)
        st.session_state['garden_sequence'] = sequence
        st.session_state['garden_correct_order'] = []
    
    # Display instructions
    st.markdown("""
    Place les nombres dans l'ordre croissant (du plus petit au plus grand).
    Clique sur les nombres dans le bon ordre.
    """)
    
    # Display the shuffled numbers
    cols = st.columns(5)
    for i, num in enumerate(st.session_state['garden_sequence']):
        with cols[i]:
            if st.button(f"{num}", key=f"garden_num_{num}"):
                # Add to correct order if not already added
                if num not in st.session_state['garden_correct_order']:
                    st.session_state['garden_correct_order'].append(num)
                    st.rerun()
    
    # Display the current sequence
    st.markdown("### Ta séquence:")
    current_seq_str = " → ".join([str(num) for num in st.session_state['garden_correct_order']])
    st.markdown(f"### {current_seq_str}")
    
    # Check if correct
    if len(st.session_state['garden_correct_order']) == 5:
        if st.session_state['garden_correct_order'] == sorted(st.session_state['garden_sequence']):
            st.success("🎉 Bravo! Tu as mis les nombres dans le bon ordre!")
            st.balloons()
        else:
            st.error("Ce n'est pas tout à fait ça. Essaie encore!")
            
        # Reset button
        if st.button("Recommencer", key="garden_reset"):
            sequence = list(range(1, 6))
            random.shuffle(sequence)
            st.session_state['garden_sequence'] = sequence
            st.session_state['garden_correct_order'] = []
            st.rerun()

def display_calculator_activity() -> None:
    """Step-by-step visual calculator activity."""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #FF6B6B;">
        <h2 style="color: #FF6B6B; text-align: center;">🧮 Calculatrice Pas-à-Pas</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("Apprends à décomposer les calculs en étapes simples pour mieux comprendre les opérations.")
    
    # Operation selection
    operation = st.radio("Choisis une opération:", ["Addition", "Soustraction"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Premier nombre", min_value=1, max_value=99, value=27)
    
    with col2:
        num2 = st.number_input("Deuxième nombre", min_value=1, max_value=99, value=15)
    
    st.markdown("---")
    
    if operation == "Addition":
        st.markdown("#### Étapes pour additionner:")
        
        # Decompose numbers
        tens1, ones1 = divmod(num1, 10)
        tens2, ones2 = divmod(num2, 10)
        
        # Step 1: Decompose
        st.markdown(f"""
        **Étape 1:** Décompose les nombres en dizaines et unités:
        - {num1} = {tens1} dizaines + {ones1} unités
        - {num2} = {tens2} dizaines + {ones2} unités
        """)
        
        # Visual representation of decomposition
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**{num1}**")
            
            # Visualize tens
            for i in range(tens1):
                st.markdown(f"""
                <div style="display: inline-block; background-color: #4ECDC4; width: 50px; height: 20px; 
                     border-radius: 5px; margin: 2px; text-align: center; color: white;">
                    10
                </div>
                """, unsafe_allow_html=True)
            
            # Visualize ones
            for i in range(ones1):
                st.markdown(f"""
                <div style="display: inline-block; background-color: #5D5FEF; width: 20px; height: 20px; 
                     border-radius: 5px; margin: 2px; text-align: center; color: white;">
                    1
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"**{num2}**")
            
            # Visualize tens
            for i in range(tens2):
                st.markdown(f"""
                <div style="display: inline-block; background-color: #4ECDC4; width: 50px; height: 20px; 
                     border-radius: 5px; margin: 2px; text-align: center; color: white;">
                    10
                </div>
                """, unsafe_allow_html=True)
            
            # Visualize ones
            for i in range(ones2):
                st.markdown(f"""
                <div style="display: inline-block; background-color: #5D5FEF; width: 20px; height: 20px; 
                     border-radius: 5px; margin: 2px; text-align: center; color: white;">
                    1
                </div>
                """, unsafe_allow_html=True)
        
        # Step 2: Add tens
        sum_tens = tens1 + tens2
        st.markdown(f"""
        **Étape 2:** Additionne les dizaines:
        - {tens1} dizaines + {tens2} dizaines = {sum_tens} dizaines = {sum_tens * 10}
        """)
        
        # Step 3: Add ones
        sum_ones = ones1 + ones2
        carry = sum_ones // 10
        remaining_ones = sum_ones % 10
        
        if carry > 0:
            st.markdown(f"""
            **Étape 3:** Additionne les unités:
            - {ones1} unités + {ones2} unités = {sum_ones} unités
            - {sum_ones} unités = {carry} dizaine + {remaining_ones} unités
            """)
        else:
            st.markdown(f"""
            **Étape 3:** Additionne les unités:
            - {ones1} unités + {ones2} unités = {sum_ones} unités
            """)
        
        # Step 4: Combine
        result = num1 + num2
        
        if carry > 0:
            st.markdown(f"""
            **Étape 4:** Combine les résultats:
            - {sum_tens} dizaines + {carry} dizaine = {sum_tens + carry} dizaines = {(sum_tens + carry) * 10}
            - {(sum_tens + carry) * 10} + {remaining_ones} = {result}
            """)
        else:
            st.markdown(f"""
            **Étape 4:** Combine les résultats:
            - {sum_tens * 10} + {sum_ones} = {result}
            """)
        
        # Final result
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 10px; margin-top: 15px; text-align: center;">
            <p style="font-size: 1.5rem;">{num1} + {num2} = <strong style="color: #FF6B6B;">{result}</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    else:  # Subtraction
        st.markdown("#### Étapes pour soustraire:")
        
        # Check if need to borrow
        borrow_needed = False
        if num1 < num2:
            st.error("Le premier nombre doit être plus grand que le deuxième pour la soustraction!")
            return
        
        # Decompose numbers
        tens1, ones1 = divmod(num1, 10)
        tens2, ones2 = divmod(num2, 10)
        
        # Check if need to borrow
        borrow_needed = ones1 < ones2
        
        # Step 1: Decompose
        st.markdown(f"""
        **Étape 1:** Décompose les nombres en dizaines et unités:
        - {num1} = {tens1} dizaines + {ones1} unités
        - {num2} = {tens2} dizaines + {ones2} unités
        """)
        
        # Visual representation of decomposition
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**{num1}**")
            
            # Visualize tens
            for i in range(tens1):
                st.markdown(f"""
                <div style="display: inline-block; background-color: #4ECDC4; width: 50px; height: 20px; 
                     border-radius: 5px; margin: 2px; text-align: center; color: white;">
                    10
                </div>
                """, unsafe_allow_html=True)
            
            # Visualize ones
            for i in range(ones1):
                st.markdown(f"""
                <div style="display: inline-block; background-color: #5D5FEF; width: 20px; height: 20px; 
                     border-radius: 5px; margin: 2px; text-align: center; color: white;">
                    1
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"**{num2}**")
            
            # Visualize tens
            for i in range(tens2):
                st.markdown(f"""
                <div style="display: inline-block; background-color: #4ECDC4; width: 50px; height: 20px; 
                     border-radius: 5px; margin: 2px; text-align: center; color: white;">
                    10
                </div>
                """, unsafe_allow_html=True)
            
            # Visualize ones
            for i in range(ones2):
                st.markdown(f"""
                <div style="display: inline-block; background-color: #5D5FEF; width: 20px; height: 20px; 
                     border-radius: 5px; margin: 2px; text-align: center; color: white;">
                    1
                </div>
                """, unsafe_allow_html=True)
        
        # Step 2 and 3: Borrow if needed and subtract
        if borrow_needed:
            st.markdown(f"""
            **Étape 2:** Emprunt d'une dizaine:
            - On ne peut pas soustraire {ones2} de {ones1} directement
            - On emprunte 1 dizaine, donc {tens1} dizaines devient {tens1-1} dizaines
            - On ajoute 10 unités, donc {ones1} unités devient {ones1+10} unités
            """)
            
            # Step 3: Subtract
            diff_ones = ones1 + 10 - ones2
            diff_tens = tens1 - 1 - tens2
            
            st.markdown(f"""
            **Étape 3:** Soustrais les unités et les dizaines:
            - Unités: {ones1+10} - {ones2} = {diff_ones}
            - Dizaines: {tens1-1} - {tens2} = {diff_tens}
            """)
        else:
            # Step 2: Subtract directly
            diff_ones = ones1 - ones2
            diff_tens = tens1 - tens2
            
            st.markdown(f"""
            **Étape 2:** Soustrais les unités et les dizaines:
            - Unités: {ones1} - {ones2} = {diff_ones}
            - Dizaines: {tens1} - {tens2} = {diff_tens}
            """)
        
        # Step 3/4: Combine
        result = num1 - num2
        
        st.markdown(f"""
        **Étape {"4" if borrow_needed else "3"}:** Combine les résultats:
        - {diff_tens} dizaines = {diff_tens * 10}
        - {diff_tens * 10} + {diff_ones} = {result}
        """)
        
        # Final result
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 10px; margin-top: 15px; text-align: center;">
            <p style="font-size: 1.5rem;">{num1} - {num2} = <strong style="color: #FF6B6B;">{result}</strong></p>
        </div>
        """, unsafe_allow_html=True)

def display_comparison_activity() -> None:
    """Number comparison activity."""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #FFD166;">
        <h2 style="color: #FFD166; text-align: center;">⚖️ Balance des Nombres</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Compare des objets et des nombres pour comprendre les relations "plus grand que", "plus petit que" et "égal à".
    """)
    
    # Number comparison activity
    st.markdown("### Compare les nombres:")
    
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        num1 = st.slider("Premier nombre", 1, 100, 35, key="balance_num1")
    
    with col3:
        num2 = st.slider("Deuxième nombre", 1, 100, 42, key="balance_num2")
    
    with col2:
        # Show comparison symbol based on values
        if num1 > num2:
            comparison = ">"
        elif num1 < num2:
            comparison = "<"
        else:
            comparison = "="
        
        st.markdown(f"""
        <div style="text-align: center; font-size: 2rem; margin-top: 30px;">
            {comparison}
        </div>
        """, unsafe_allow_html=True)
    
    # Visual representation of comparison
    st.markdown("### Représentation visuelle:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### {num1}")
        
        # Create bars to represent numbers
        for i in range(min(num1, 50)):  # Limit to 50 for display purposes
            width_percent = min(100, num1 * 2)
            st.markdown(f"""
            <div style="background-color: #4ECDC4; height: 10px; margin: 1px 0; width: {width_percent}%;">
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"### {num2}")
        
        # Create bars to represent numbers
        for i in range(min(num2, 50)):  # Limit to 50 for display purposes
            width_percent = min(100, num2 * 2)
            st.markdown(f"""
            <div style="background-color: #FF6B6B; height: 10px; margin: 1px 0; width: {width_percent}%;">
            </div>
            """, unsafe_allow_html=True)
    
    # Comparison quiz
    st.markdown("### Quiz de comparaison:")
    
    # Initialize quiz state if not already
    if 'comparison_quiz' not in st.session_state:
        # Generate 3 comparison questions
        questions = []
        for _ in range(3):
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            questions.append((a, b))
        
        st.session_state['comparison_quiz'] = questions
        st.session_state['comparison_answers'] = [""] * 3
        st.session_state['comparison_checked'] = False
    
    # Display questions
    for i, (a, b) in enumerate(st.session_state['comparison_quiz']):
        st.markdown(f"**Question {i+1}:** Quel symbole compare correctement {a} et {b}?")
        
        # Create columns for options
        cols = st.columns(3)
        
        with cols[0]:
            if st.button("<", key=f"less_{i}"):
                st.session_state['comparison_answers'][i] = "<"
                st.rerun()
        
        with cols[1]:
            if st.button("=", key=f"equal_{i}"):
                st.session_state['comparison_answers'][i] = "="
                st.rerun()
        
        with cols[2]:
            if st.button(">", key=f"greater_{i}"):
                st.session_state['comparison_answers'][i] = ">"
                st.rerun()
        
        # Show selected answer
        if st.session_state['comparison_answers'][i]:
            st.markdown(f"Ta réponse: **{a} {st.session_state['comparison_answers'][i]} {b}**")
    
    # Check answers button
    if st.button("Vérifier mes réponses", key="btn_check_comparison") or st.session_state['comparison_checked']:
        st.session_state['comparison_checked'] = True
        
        correct_count = 0
        for i, (a, b) in enumerate(st.session_state['comparison_quiz']):
            user_answer = st.session_state['comparison_answers'][i]
            
            if a < b and user_answer == "<":
                correct = True
            elif a > b and user_answer == ">":
                correct = True
            elif a == b and user_answer == "=":
                correct = True
            else:
                correct = False
            
            if correct:
                st.success(f"Question {i+1}: Correct! {a} {user_answer} {b}")
                correct_count += 1
            else:
                correct_answer = "<" if a < b else (">" if a > b else "=")
                st.error(f"Question {i+1}: Incorrect. La bonne réponse est: {a} {correct_answer} {b}")
        
        # Show final score
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 10px; margin-top: 15px; text-align: center;">
            <p style="font-size: 1.2rem;">Tu as obtenu <strong>{correct_count}/3</strong> bonnes réponses!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Reset button
        if st.button("Nouveau quiz", key="btn_new_comparison"):
            # Generate new questions
            questions = []
            for _ in range(3):
                a = random.randint(1, 50)
                b = random.randint(1, 50)
                questions.append((a, b))
            
            st.session_state['comparison_quiz'] = questions
            st.session_state['comparison_answers'] = [""] * 3
            st.session_state['comparison_checked'] = False
            st.rerun()

def display_monster_game() -> None:
    """Monster capture math game."""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #FF6B6B;">
        <h2 style="color: #FF6B6B; text-align: center;">👹 La Chasse aux Monstres</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Attrape les monstres en résolvant des opérations mathématiques! Chaque bonne réponse te permet de capturer un monstre.
    """)
    
    # Initialize game state if not already
    if 'monster_game' not in st.session_state:
        # Generate math problems grid
        grid = []
        for i in range(3):  # Simplified to 3x3 grid
            row = []
            for j in range(3):
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                operation = random.choice(['+', '-', '×'])
                
                if operation == '+':
                    result = a + b
                    problem = f"{a} + {b}"
                elif operation == '-':
                    # Ensure a >= b for subtraction
                    if a < b:
                        a, b = b, a
                    result = a - b
                    problem = f"{a} - {b}"
                else:  # multiplication
                    # Keep numbers small for multiplication
                    a = random.randint(1, 5)
                    b = random.randint(1, 5)
                    result = a * b
                    problem = f"{a} × {b}"
                
                row.append({
                    'problem': problem,
                    'result': result,
                    'solved': False
                })
            grid.append(row)
        
        st.session_state['monster_game'] = {
            'grid': grid,
            'score': 0,
            'total': 9,  # 3x3 grid
            'current_problem': None
        }
    
    # Display score
    st.markdown(f"""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 10px; margin: 15px 0; text-align: center;">
        <p style="font-size: 1.2rem;">Monstres capturés: <strong>{st.session_state['monster_game']['score']}/{st.session_state['monster_game']['total']}</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Current problem display
    if st.session_state['monster_game']['current_problem'] is not None:
        row, col = st.session_state['monster_game']['current_problem']
        problem = st.session_state['monster_game']['grid'][row][col]
        
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 10px; margin: 15px 0; text-align: center;">
            <h3 style="font-size: 1.5rem;">Résous: {problem['problem']} = ?</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Answer input
        answer = st.number_input("Ta réponse:", key="monster_answer", step=1)
        
        # Check answer button
        if st.button("Vérifier", key="btn_check_monster"):
            if answer == problem['result']:
                st.success("🎉 Correct! Tu as capturé un monstre!")
                st.session_state['monster_game']['grid'][row][col]['solved'] = True
                st.session_state['monster_game']['score'] += 1
                st.session_state['monster_game']['current_problem'] = None
            else:
                st.error(f"Ce n'est pas la bonne réponse. {problem['problem']} = {problem['result']}")
                st.session_state['monster_game']['current_problem'] = None
            
            st.rerun()
    
    # Display the grid
    st.markdown("### Grille de monstres:")
    
    # Display grid as table
    for i, row in enumerate(st.session_state['monster_game']['grid']):
        cols = st.columns(3)  # Simplified to 3x3 grid
        for j, cell in enumerate(row):
            with cols[j]:
                if cell['solved']:
                    # Already solved - show captured monster
                    st.markdown(f"""
                    <div style="background-color: #4ECDC4; border-radius: 10px; padding: 10px; margin: 5px; text-align: center; height: 60px;">
                        <p style="margin: 0;">✅</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    # Not solved yet - show clickable cell
                    monster_key = f"monster_{i}_{j}"
                    if st.button("👹", key=monster_key):
                        st.session_state['monster_game']['current_problem'] = (i, j)
                        st.rerun()
    
    # Check if all monsters captured
    if st.session_state['monster_game']['score'] == st.session_state['monster_game']['total']:
        st.success("🎉 Félicitations! Tu as capturé tous les monstres!")
        st.balloons()
        
        # Reset button
        if st.button("Nouvelle partie", key="btn_new_monster"):
            del st.session_state['monster_game']
            st.rerun()