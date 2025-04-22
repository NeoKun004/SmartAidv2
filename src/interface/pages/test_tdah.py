import streamlit as st
import time
import random
from src.utils.image_utils import dtha_b64

def show_page():
    """Display the TDAH test page with comprehensive attention tests"""
    st.title("🎯 Test d'Attention et de Concentration 🧠")
    
    # Ajouter des éléments visuels amusants
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #5D5FEF; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h3 style="color: #5D5FEF; text-align: center;">👋 Bienvenue au test d'attention</h3>
            <div style="display: flex; justify-content: center; margin: 15px 0;">
                <img src="data:image/png;base64,{dtha_b64}" style="max-width: 90%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Formulaire d'informations générales
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #5D5FEF; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #5D5FEF; text-align: center;">👋 Informations générales</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        nom_prenom = st.text_input("Nom et Prénom de l'enfant", key="tdah_nom")
    with col2:
        age = st.number_input("Âge", min_value=2, max_value=18, value=6, key="tdah_age")
    with col3:
        classe = st.text_input("Classe", key="tdah_classe")
    
    # Instructions générales pour le test
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #FF6B6B; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <p style="font-size: 1.2rem; text-align: center; color: #333;">
            Ce test va évaluer ta concentration et ton attention à travers 6 activités amusantes. 
            <span style="font-weight: bold; color: #FF6B6B;">Amuse-toi bien ! 🎮</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialiser l'étape actuelle du test si ce n'est pas déjà fait
    if 'tdah_current_step' not in st.session_state:
        st.session_state['tdah_current_step'] = 0  # 0=intro, 1-6=tests, 7=résumé
    
    # Initialize results in session state
    if 'tdah_detailed_results' not in st.session_state:
        st.session_state['tdah_detailed_results'] = {
            "memorisation": {"score": 0, "max": 3, "completed": False},
            "attention": {"score": 0, "max": 4, "completed": False},
            "impulsivite": {"score": 0, "max": 1, "completed": False},
            "memoire": {"score": 0, "max": 1, "completed": False},
            "organisation": {"score": 0, "max": 1, "completed": False},
            "flexibilite": {"score": 0, "max": 2, "completed": False}
        }
    
    # Définir les noms des étapes
    step_names = [
        "Introduction",
        "Test de Mémorisation", 
        "Test d'Attention",
        "Test d'Impulsivité",
        "Test de Mémoire",
        "Test d'Organisation",
        "Test de Flexibilité",
        "Résumé des résultats"
    ]
    
    # Afficher la barre de progression
    if st.session_state['tdah_current_step'] > 0:
        progress = st.session_state['tdah_current_step'] / 7  # 7 étapes au total après l'intro
        st.progress(progress)
        st.markdown(f"### Étape {st.session_state['tdah_current_step']}/7: {step_names[st.session_state['tdah_current_step']]}")
    
    # Afficher l'étape actuelle
    if st.session_state['tdah_current_step'] == 0:
        # Page d'introduction
        st.markdown("""
        <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin: 20px 0; text-align: center;">
            <h2 style="color: #4ECDC4;">Bienvenue au Test d'Attention!</h2>
            <p style="font-size: 1.2rem;">
                Tu vas participer à 6 activités différentes pour tester ton attention et ta concentration.
                Prends ton temps et réponds du mieux que tu peux!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📝 Commencer le test!", key="start_test"):
            st.session_state['tdah_current_step'] = 1
            st.rerun()
            
    elif st.session_state['tdah_current_step'] == 1:
        # Test 1: Mémorisation d'histoire
        display_memorisation_test()
        
    elif st.session_state['tdah_current_step'] == 2:
        # Test 2: Attention Soutenue
        display_attention_test()
        
    elif st.session_state['tdah_current_step'] == 3:
        # Test 3: Impulsivité
        display_impulsivity_test()
        
    elif st.session_state['tdah_current_step'] == 4:
        # Test 4: Mémoire de Travail
        display_memory_test()
        
    elif st.session_state['tdah_current_step'] == 5:
        # Test 5: Organisation
        display_organization_test()
        
    elif st.session_state['tdah_current_step'] == 6:
        # Test 6: Flexibilité Cognitive
        display_flexibility_test()
    
    elif st.session_state['tdah_current_step'] == 7:
        # Page récapitulative des résultats
        display_results_summary()
    
    # Navigation buttons (si on n'est pas à l'intro ou au résumé final)
    if 0 < st.session_state['tdah_current_step'] < 7:
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.button("⬅️ Précédent", key="prev_button"):
                st.session_state['tdah_current_step'] -= 1
                st.rerun()
        
        with col3:
            if st.button("Suivant ➡️", key="next_button"):
                # Vérifier si le test actuel est complété avant d'avancer
                current_key = ""
                if st.session_state['tdah_current_step'] == 1:
                    current_key = "memorisation"
                elif st.session_state['tdah_current_step'] == 2:
                    current_key = "attention"
                elif st.session_state['tdah_current_step'] == 3:
                    current_key = "impulsivite"
                elif st.session_state['tdah_current_step'] == 4:
                    current_key = "memoire"
                elif st.session_state['tdah_current_step'] == 5:
                    current_key = "organisation"
                elif st.session_state['tdah_current_step'] == 6:
                    current_key = "flexibilite"
                
                # Si le test actuel n'est pas complété, afficher un avertissement
                if current_key in st.session_state['tdah_detailed_results'] and not st.session_state['tdah_detailed_results'][current_key]["completed"]:
                    st.warning("Termine ce test avant de passer au suivant!")
                else:
                    st.session_state['tdah_current_step'] += 1
                    st.rerun()

# Fonctions pour afficher chaque test
def display_memorisation_test():
    """Test de mémorisation"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #4ECDC4; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #4ECDC4; text-align: center;">📚 Test de Mémorisation</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Lis attentivement cette histoire courte :")
    st.info("""
    Pierre et Marie sont allés au parc. Pierre portait un t-shirt bleu et Marie une robe rouge. 
    Ils ont joué au ballon pendant 30 minutes, puis ils ont mangé une glace. 
    Pierre a choisi une glace à la vanille et Marie une glace au chocolat.
    """)
    
    # Ajouter des icônes et des couleurs aux questions
    q1 = st.text_input("1️⃣ De quelle couleur était le t-shirt de Pierre ? 👕", key="tdah_mem_q1")
    q2 = st.text_input("2️⃣ Combien de temps ont-ils joué au ballon ? ⚽", key="tdah_mem_q2")
    q3 = st.text_input("3️⃣ Quel parfum de glace a choisi Marie ? 🍦", key="tdah_mem_q3")
    
    # Bouton pour valider ce test spécifique
    if st.button("✅ Valider mes réponses", key="submit_memorisation"):
        score = 0
        if q1.lower() == "bleu":
            score += 1
        if "30" in q2 or "trente" in q2.lower():
            score += 1
        if "chocolat" in q3.lower():
            score += 1
        
        st.session_state['tdah_detailed_results']["memorisation"]["score"] = score
        st.session_state['tdah_detailed_results']["memorisation"]["completed"] = True
        
        # Afficher le résultat
        st.success(f"Tu as obtenu {score}/3 bonnes réponses pour ce test!")
        
        # Bouton pour passer au test suivant
        if st.button("▶️ Passer au test suivant", key="next_after_memorisation"):
            st.session_state['tdah_current_step'] += 1
            st.rerun()

def display_attention_test():
    """Test d'attention soutenue"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #4ECDC4; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #4ECDC4; text-align: center;">👁️ Test d'Attention Soutenue</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Appuie sur le bouton quand tu vois la lettre 'A' dans la séquence suivante :")
    
    # Définir la séquence de lettres
    sequence = ["D", "A", "B", "C", "A", "M", "A", "Z", "A", "T"]
    
    # Initialisation des clics si non existant
    if 'attention_clicks' not in st.session_state:
        st.session_state['attention_clicks'] = []
    
    # Afficher la séquence avec des boutons
    cols = st.columns(10)
    for i, letter in enumerate(sequence):
        with cols[i]:
            # Si déjà cliqué, afficher différemment
            if i in st.session_state['attention_clicks']:
                if letter == "A":
                    st.markdown(f"""
                    <div style="background-color: #4ECDC4; padding: 10px; border-radius: 10px; margin: 5px; text-align: center; color: white; font-weight: bold;">
                        {letter} ✓
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background-color: #FF6B6B; padding: 10px; border-radius: 10px; margin: 5px; text-align: center; color: white; font-weight: bold;">
                        {letter} ✗
                    </div>
                    """, unsafe_allow_html=True)
            else:
                if st.button(letter, key=f"letter_{i}"):
                    st.session_state['attention_clicks'].append(i)
                    if letter == "A":
                        st.success("Bien joué!")
                    else:
                        st.error("Ce n'est pas un A!")
                    st.rerun()
    
    # Calculer le score d'attention
    correct_a_indices = [i for i, letter in enumerate(sequence) if letter == "A"]
    clicked_a_indices = [i for i in st.session_state['attention_clicks'] if sequence[i] == "A"]
    wrong_clicks = [i for i in st.session_state['attention_clicks'] if sequence[i] != "A"]
    
    attention_score = len(clicked_a_indices)
    max_attention_score = len(correct_a_indices)
    
    # Bouton pour valider ce test
    if st.button("✅ Valider mes réponses", key="submit_attention"):
        st.session_state['tdah_detailed_results']["attention"]["score"] = attention_score
        st.session_state['tdah_detailed_results']["attention"]["completed"] = True
        
        # Afficher le résultat
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin: 15px 0; text-align: center;">
            <h3 style="color: {'#4ECDC4' if attention_score >= max_attention_score/2 else '#FF6B6B'};">
                Tu as trouvé {attention_score}/{max_attention_score} lettres A
            </h3>
            <p>Tu as fait {len(wrong_clicks)} erreur(s) en cliquant sur d'autres lettres.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Bouton pour passer au test suivant
        if st.button("▶️ Passer au test suivant", key="next_after_attention"):
            # Réinitialiser les clics pour la prochaine fois
            st.session_state['attention_clicks'] = []
            st.session_state['tdah_current_step'] += 1
            st.rerun()
    
    # Bouton pour réinitialiser le test
    if st.button("🔄 Recommencer ce test", key="reset_attention"):
        st.session_state['attention_clicks'] = []
        st.rerun()

def display_impulsivity_test():
    """Test d'impulsivité"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #4ECDC4; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #4ECDC4; text-align: center;">⏱️ Test d'Impulsivité</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Lis bien la consigne et attends 5 secondes avant de répondre :")
    st.info("Quel est le nom de la capitale de la Tunisie ?")
    
    # Initialiser le timer et la réponse
    if 'impulsivity_timer_started' not in st.session_state:
        st.session_state['impulsivity_timer_started'] = time.time()
        st.session_state['impulsivity_answered'] = False
        st.session_state['impulsivity_time_elapsed'] = 0
    
    # Calculer le temps écoulé
    current_time = time.time()
    elapsed_time = current_time - st.session_state['impulsivity_timer_started']
    st.session_state['impulsivity_time_elapsed'] = elapsed_time
    
    # Afficher un compte à rebours
    if elapsed_time < 5:
        st.write(f"Attends encore {5 - int(elapsed_time)} secondes...")
        st.progress(min(elapsed_time / 5, 1.0))
    else:
        st.success("Tu peux maintenant répondre!")
    
    # Champ de réponse
    answer = st.text_input("Ta réponse :", key="impulsivity_answer", disabled=elapsed_time < 5)
    
    # Bouton pour valider ce test
    if st.button("✅ Valider ma réponse", key="submit_impulsivity"):
        # Vérifier si l'élève a attendu 5 secondes
        waited_enough = elapsed_time >= 5
        
        st.session_state['tdah_detailed_results']["impulsivite"]["score"] = 1 if waited_enough else 0
        st.session_state['tdah_detailed_results']["impulsivite"]["completed"] = True
        
        if waited_enough:
            st.success("Bravo pour avoir attendu le temps nécessaire! Tu as bien contrôlé ton impulsivité.")
        else:
            st.error("Tu as essayé de répondre trop vite. C'est important d'attendre et de réfléchir avant d'agir!")
        
        # Bouton pour passer au test suivant
        if st.button("▶️ Passer au test suivant", key="next_after_impulsivity"):
            # Réinitialiser le test pour la prochaine fois
            if 'impulsivity_timer_started' in st.session_state:
                del st.session_state['impulsivity_timer_started']
            if 'impulsivity_answered' in st.session_state:
                del st.session_state['impulsivity_answered']
            if 'impulsivity_time_elapsed' in st.session_state:
                del st.session_state['impulsivity_time_elapsed']
                
            st.session_state['tdah_current_step'] += 1
            st.rerun()
    
    # Bouton pour réinitialiser le test
    if st.button("🔄 Recommencer ce test", key="reset_impulsivity"):
        if 'impulsivity_timer_started' in st.session_state:
            del st.session_state['impulsivity_timer_started']
        if 'impulsivity_answered' in st.session_state:
            del st.session_state['impulsivity_answered']
        if 'impulsivity_time_elapsed' in st.session_state:
            del st.session_state['impulsivity_time_elapsed']
        st.rerun()

def display_memory_test():
    """Test de mémoire de travail"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #4ECDC4; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #4ECDC4; text-align: center;">🧠 Test de Mémoire de Travail</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Mémorise cette suite de chiffres, puis répète-la dans l'ordre inverse :")
    
    # Séquence à mémoriser
    sequence = "4 - 9 - 2 - 7"
    st.info(f"Séquence : {sequence}")
    
    # Réponse attendue
    expected_inverse = "7 - 2 - 9 - 4"
    
    # Champ de réponse
    inverse_answer = st.text_input("Entre la séquence dans l'ordre inverse :", 
                                  placeholder="Par exemple: 7 - 2 - 9 - 4", 
                                  key="memory_inverse")
    
    # Bouton pour valider ce test
    if st.button("✅ Vérifier ma réponse", key="submit_memory"):
        is_correct = inverse_answer.strip() == expected_inverse
        score = 1 if is_correct else 0
        
        st.session_state['tdah_detailed_results']["memoire"]["score"] = score
        st.session_state['tdah_detailed_results']["memoire"]["completed"] = True
        
        if is_correct:
            st.success("Correct! Tu as bien mémorisé et inversé la séquence!")
        else:
            st.error(f"Ce n'est pas tout à fait ça. La bonne réponse était : {expected_inverse}")
        
        # Bouton pour passer au test suivant
        if st.button("▶️ Passer au test suivant", key="next_after_memory"):
            st.session_state['tdah_current_step'] += 1
            st.rerun()

def display_organization_test():
    """Test d'organisation"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #4ECDC4; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #4ECDC4; text-align: center;">📋 Test d'Organisation</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Mets ces actions dans le bon ordre pour faire un gâteau :")
    
    # Liste des étapes
    steps = {
        "A": "Mettre le gâteau au four",
        "B": "Mélanger les ingrédients",
        "C": "Servir le gâteau",
        "D": "Ajouter le sucre et la farine"
    }
    
    # Initialiser l'ordre sélectionné
    if 'organization_order' not in st.session_state:
        st.session_state['organization_order'] = []
    
    # Afficher les options disponibles
    st.write("Clique sur les actions dans l'ordre correct :")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Options disponibles :")
        for key, step in steps.items():
            if key not in st.session_state['organization_order']:
                if st.button(f"{key} - {step}", key=f"org_step_{key}"):
                    st.session_state['organization_order'].append(key)
                    st.rerun()
    
    with col2:
        st.write("### Ton ordre actuel :")
        if st.session_state['organization_order']:
            for i, step_key in enumerate(st.session_state['organization_order']):
                st.markdown(f"""
                <div style="background-color: rgba(78, 205, 196, 0.3); padding: 10px; border-radius: 10px; margin-bottom: 5px;">
                    {i+1}. {steps[step_key]}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("Aucune étape sélectionnée")
    
    # Vérifier l'ordre
    correct_order = ["D", "B", "A", "C"]
    
    # Bouton pour valider ce test
    if len(st.session_state['organization_order']) == 4:
        if st.button("✅ Valider mon ordre", key="submit_organization"):
            is_correct = st.session_state['organization_order'] == correct_order
            score = 1 if is_correct else 0
            
            st.session_state['tdah_detailed_results']["organisation"]["score"] = score
            st.session_state['tdah_detailed_results']["organisation"]["completed"] = True
            
            if is_correct:
                st.success("Bravo! Tu as mis les étapes dans le bon ordre!")
            else:
                st.error("Ce n'est pas le bon ordre. Voici l'ordre correct :")
                for i, key in enumerate(correct_order):
                    st.markdown(f"{i+1}. {steps[key]}")
            
            # Bouton pour passer au test suivant
            if st.button("▶️ Passer au test suivant", key="next_after_organization"):
                st.session_state['organization_order'] = []
                st.session_state['tdah_current_step'] += 1
                st.rerun()
    
    # Bouton pour réinitialiser
    if st.button("🔄 Recommencer", key="reset_organization"):
        st.session_state['organization_order'] = []
        st.rerun()

def display_flexibility_test():
    """Test de flexibilité cognitive"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #4ECDC4; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #4ECDC4; text-align: center;">🔄 Test de Flexibilité Cognitive</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("Ce test évalue ta capacité à changer de stratégie.")
    
    # Initialiser les étapes du test
    if 'flexibility_step' not in st.session_state:
        st.session_state['flexibility_step'] = 1
        st.session_state['flexibility_score'] = 0
    
    # Première partie : mot commençant par P
    if st.session_state['flexibility_step'] == 1:
        st.write("1️⃣ Donne un mot qui commence par la lettre 'P'.")
        word_p_start = st.text_input("Ton mot :", key="flex_p_start")
        
        if st.button("✅ Valider", key="validate_p_start"):
            if word_p_start and word_p_start.lower().startswith('p'):
                st.session_state['flexibility_score'] += 1
                st.success(f"Bravo! '{word_p_start}' commence bien par P.")
                st.session_state['flexibility_step'] = 2
                st.rerun()
            else:
                st.error("Ce mot ne commence pas par P. Essaie encore!")
    
    # Deuxième partie : mot finissant par P
    elif st.session_state['flexibility_step'] == 2:
        st.write("2️⃣ Maintenant, donne un mot qui finit par la lettre 'P'.")
        st.info("C'est un changement de règle! Tu dois t'adapter.")
        word_p_end = st.text_input("Ton mot :", key="flex_p_end")
        
        if st.button("✅ Valider", key="validate_p_end"):
            if word_p_end and word_p_end.lower().endswith('p'):
                st.session_state['flexibility_score'] += 1
                st.success(f"Excellent! '{word_p_end}' finit bien par P.")
                st.session_state['flexibility_step'] = 3
                st.rerun()
            else:
                st.error("Ce mot ne finit pas par P. Essaie encore!")
    
    # Affichage du résultat final
    elif st.session_state['flexibility_step'] == 3:
        score = st.session_state['flexibility_score']
        
        # Enregistrer le score
        st.session_state['tdah_detailed_results']["flexibilite"]["score"] = score
        st.session_state['tdah_detailed_results']["flexibilite"]["completed"] = True
        
        st.markdown(f"""
        <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin: 15px 0; text-align: center;">
            <h3 style="color: {'#4ECDC4' if score == 2 else '#FF6B6B'};">
                Tu as obtenu {score}/2 points au test de flexibilité!
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        if score == 2:
            st.success("Excellent! Tu as montré une très bonne capacité d'adaptation aux changements de règles.")
        elif score == 1:
            st.info("Tu as réussi une partie du test. Avec de l'entraînement, tu pourras améliorer ta flexibilité mentale.")
        else:
            st.warning("Ce test était difficile! Ne t'inquiète pas, la flexibilité mentale s'améliore avec la pratique.")
        
        # Bouton pour passer au résumé
        if st.button("📊 Voir le résumé de tous les tests", key="next_after_flexibility"):
            st.session_state['tdah_current_step'] = 7
            st.rerun()
    
    # Bouton pour réinitialiser
    if st.button("🔄 Recommencer ce test", key="reset_flexibility"):
        st.session_state['flexibility_step'] = 1
        st.session_state['flexibility_score'] = 0
        st.rerun()

def display_results_summary():
    """Affiche un résumé des résultats avant la soumission finale"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border: 3px solid #FF6B6B;">
        <h3 style="color: #FF6B6B; text-align: center;">🎯 Résumé de tes résultats</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Calcul du score total
    total_score = sum([st.session_state['tdah_detailed_results'][key]["score"] for key in st.session_state['tdah_detailed_results']])
    max_score = sum([st.session_state['tdah_detailed_results'][key]["max"] for key in st.session_state['tdah_detailed_results']])
    
    # Afficher le score total
    st.markdown(f"""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin-bottom: 20px; text-align: center;">
        <h2 style="color: #5D5FEF;">Score total: {total_score}/{max_score}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Afficher les scores par catégorie
    for category, data in st.session_state['tdah_detailed_results'].items():
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
    
    # Bouton pour terminer et voir l'analyse complète
    if st.button("🏁 Terminer le test et voir mon analyse personnalisée", key="finish_test"):
        # Enregistrer les réponses pour la page de résultats
        st.session_state['tdah_responses'] = {
            "nom": st.session_state.get("tdah_nom", ""),
            "age": st.session_state.get("tdah_age", 6),
            "classe": st.session_state.get("tdah_classe", ""),
            "detailed_results": st.session_state['tdah_detailed_results']
        }
        
        # Réinitialiser l'étape pour la prochaine fois
        st.session_state['tdah_current_step'] = 0
        
        # Rediriger vers la page des résultats
        st.session_state['page'] = 'resultats_tdah'
        st.rerun()