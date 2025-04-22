import streamlit as st
import time
from PIL import Image
import io
import base64

def show_page():
    """Display the dysgraphie test page"""
    st.title("✍️ Test de Dépistage de la Dysgraphie 📝")
    
    # Initialize test state if not already done
    if 'dysgraphie_current_step' not in st.session_state:
        st.session_state['dysgraphie_current_step'] = 0  # 0=intro, 1-5=tests, 6=summary
    
    # Initialize results storage
    if 'dysgraphie_detailed_results' not in st.session_state or st.session_state['dysgraphie_detailed_results'] is None:
        st.session_state['dysgraphie_detailed_results'] = {
            "copie_texte": {"score": 0, "max": 3, "completed": False, "notes": "", "sample": None},
            "ecriture_spontanee": {"score": 0, "max": 3, "completed": False, "notes": "", "sample": None},
            "vitesse_endurance": {"score": 0, "max": 3, "completed": False, "notes": "", "word_count": 0},
            "graphisme_coordination": {"score": 0, "max": 3, "completed": False, "notes": "", "sample": None},
            "lisibilite_orthographe": {"score": 0, "max": 3, "completed": False, "notes": "", "sample": None}
        }
    
    # Form for user information
    col1, col2, col3 = st.columns(3)
    with col1:
        nom_prenom = st.text_input("Nom et Prénom de l'enfant", key="dysgraphie_nom", value="")
    with col2:
        age = st.number_input("Âge", min_value=2, max_value=18, value=8, key="dysgraphie_age")
    with col3:
        classe = st.text_input("Classe", value="", key="dysgraphie_classe")
    
    # Define step names
    step_names = [
        "Introduction",
        "Test de Copie de Texte", 
        "Test d'Écriture Spontanée",
        "Test de Vitesse et d'Endurance",
        "Test de Graphisme et Coordination Fine",
        "Test de Lisibilité et Orthographe",
        "Résumé des résultats"
    ]
    
    # Display progress
    if st.session_state['dysgraphie_current_step'] > 0:
        progress = st.session_state['dysgraphie_current_step'] / 6
        st.progress(progress)
        st.markdown(f"### Étape {st.session_state['dysgraphie_current_step']}/6: {step_names[st.session_state['dysgraphie_current_step']]}")
    
    # Display current step content
    if st.session_state['dysgraphie_current_step'] == 0:
        display_intro()
    elif st.session_state['dysgraphie_current_step'] == 1:
        display_copie_texte_test()
    elif st.session_state['dysgraphie_current_step'] == 2:
        display_ecriture_spontanee_test()
    elif st.session_state['dysgraphie_current_step'] == 3:
        display_vitesse_endurance_test()
    elif st.session_state['dysgraphie_current_step'] == 4:
        display_graphisme_coordination_test()
    elif st.session_state['dysgraphie_current_step'] == 5:
        display_lisibilite_orthographe_test()
    elif st.session_state['dysgraphie_current_step'] == 6:
        display_results_summary()
    
    # Navigation buttons if not at intro or final summary
    if 0 < st.session_state['dysgraphie_current_step'] < 6:
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.button("⬅️ Précédent", key="dysgraphie_prev_button"):
                st.session_state['dysgraphie_current_step'] -= 1
                st.rerun()
        
        with col3:
            if st.button("Suivant ➡️", key="dysgraphie_next_button"):
                # Mark current test as completed
                current_key = ""
                if st.session_state['dysgraphie_current_step'] == 1:
                    current_key = "copie_texte"
                elif st.session_state['dysgraphie_current_step'] == 2:
                    current_key = "ecriture_spontanee"
                elif st.session_state['dysgraphie_current_step'] == 3:
                    current_key = "vitesse_endurance"
                elif st.session_state['dysgraphie_current_step'] == 4:
                    current_key = "graphisme_coordination"
                elif st.session_state['dysgraphie_current_step'] == 5:
                    current_key = "lisibilite_orthographe"
                
                # Mark as completed
                if current_key:
                    st.session_state['dysgraphie_detailed_results'][current_key]["completed"] = True
                
                st.session_state['dysgraphie_current_step'] += 1
                st.rerun()

def display_intro():
    """Display introduction to the dysgraphie test"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin: 20px 0; text-align: center;">
        <h2 style="color: #FF6B6B;">Bienvenue au Test de Dysgraphie!</h2>
        <p style="font-size: 1.2rem;">
            Ce test évalue les compétences d'écriture et la motricité fine.
            Il est composé de 5 petits exercices simples et interactifs.
        </p>
        <p style="font-size: 1.1rem;">
            <strong>Important:</strong> Un adulte doit être présent pour aider à administrer le test.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin: 20px 0;">
        <h3 style="color: #5D5FEF;">Comment ça marche?</h3>
        <ul style="font-size: 1.1rem;">
            <li>Tu auras besoin de papier et d'un crayon pour certains exercices</li>
            <li>Tu pourras télécharger tes exercices d'écriture pour les évaluer</li>
            <li>Un adulte notera tes performances après chaque exercice</li>
            <li>Prends ton temps et fais de ton mieux!</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Start button
    if st.button("📝 Commencer le test!", key="start_dysgraphie_test"):
        st.session_state['dysgraphie_current_step'] = 1
        st.rerun()

def display_copie_texte_test():
    """Display Text Copy Test"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #FF6B6B; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #FF6B6B; text-align: center;">📖 Test de Copie de Texte</h3>
        <p style="text-align: center;">
            L'enfant doit copier un texte en essayant d'écrire le plus lisiblement possible.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Instructions for the administrator
    with st.expander("📋 Instructions pour l'adulte"):
        st.markdown("""
        1. Donnez à l'enfant une feuille de papier et un crayon
        2. Demandez-lui de copier le texte ci-dessous en écrivant le plus lisiblement possible
        3. Observez comment l'enfant forme les lettres et organise son texte
        4. Une fois terminé, prenez une photo ou scannez le travail de l'enfant
        5. Téléversez l'image et remplissez l'évaluation ci-dessous
        """)
    
    # Display the text to copy
    st.markdown("### Texte à copier:")
    
    st.markdown("""
    <div style="background-color: rgba(255, 107, 107, 0.1); padding: 20px; border-radius: 10px; margin: 15px 0; text-align: center;">
        <p style="font-size: 1.2rem; line-height: 1.6;">
            "Le petit chat joue dans le jardin. Il saute sur l'herbe et court après un papillon."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Upload area for the copied text
    st.markdown("### Téléverser l'exercice complété:")
    uploaded_file = st.file_uploader("Téléversez une image de l'exercice d'écriture", type=["jpg", "jpeg", "png", "pdf"], key="copie_texte_upload")
    
    if uploaded_file is not None:
        # Display the uploaded image
        if uploaded_file.type.startswith('image'):
            st.image(uploaded_file, caption="Exercice de copie téléversé", width=400)
        elif uploaded_file.type == 'application/pdf':
            st.warning("Fichier PDF téléversé. Veuillez évaluer le PDF dans un lecteur externe.")
        
        # Store the uploaded file in session state
        st.session_state['dysgraphie_detailed_results']["copie_texte"]["sample"] = uploaded_file.getvalue()
    
    # Admin observation form
    with st.form("copie_texte_form"):
        st.markdown("### Évaluation (à remplir par l'adulte):")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Taille et forme des lettres:")
            letter_form = st.select_slider(
                "Les lettres sont formées:",
                options=["Très irrégulières", "Irrégulières", "Assez régulières", "Très régulières"],
                value="Assez régulières",
                key="copie_texte_letter_form"
            )
        
        with col2:
            st.markdown("#### Alignement sur la ligne:")
            alignment = st.select_slider(
                "Le texte est aligné:",
                options=["Pas du tout", "Peu", "Assez bien", "Très bien"],
                value="Assez bien",
                key="copie_texte_alignment"
            )
        
        st.markdown("#### Espacements entre les mots et les lettres:")
        spacing = st.select_slider(
            "Les espacements sont:",
            options=["Très irréguliers", "Irréguliers", "Assez réguliers", "Très réguliers"],
            value="Assez réguliers",
            key="copie_texte_spacing"
        )
        
        notes = st.text_area("Notes additionnelles:", key="copie_texte_notes", height=100)
        
        # Calculate score based on observations
        score = 0
        if letter_form in ["Assez régulières", "Très régulières"]:
            score += 1
        if alignment in ["Assez bien", "Très bien"]:
            score += 1
        if spacing in ["Assez réguliers", "Très réguliers"]:
            score += 1
        
        submit = st.form_submit_button("Enregistrer l'évaluation")
        
        if submit:
            # Save results to session state
            st.session_state['dysgraphie_detailed_results']["copie_texte"]["score"] = score
            st.session_state['dysgraphie_detailed_results']["copie_texte"]["notes"] = notes
            st.session_state['dysgraphie_detailed_results']["copie_texte"]["completed"] = True
            st.success("Évaluation enregistrée!")

def display_ecriture_spontanee_test():
    """Display Spontaneous Writing Test"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #5D5FEF; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #5D5FEF; text-align: center;">📝 Test d'Écriture Spontanée</h3>
        <p style="text-align: center;">
            L'enfant doit écrire une phrase qui décrit son activité préférée.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Instructions for the administrator
    with st.expander("📋 Instructions pour l'adulte"):
        st.markdown("""
        1. Donnez à l'enfant une feuille de papier et un crayon
        2. Demandez-lui d'écrire 2 ou 3 phrases qui décrivent son activité préférée
        3. Observez comment l'enfant organise ses idées et forme les lettres
        4. Une fois terminé, prenez une photo ou scannez le travail de l'enfant
        5. Téléversez l'image et remplissez l'évaluation ci-dessous
        """)
    
    # Display the instruction
    st.markdown("### Consigne:")
    
    st.markdown("""
    <div style="background-color: rgba(93, 95, 239, 0.1); padding: 20px; border-radius: 10px; margin: 15px 0; text-align: center;">
        <p style="font-size: 1.2rem; line-height: 1.6;">
            "Écris une phrase qui décrit ton activité préférée en 2 ou 3 phrases."
        </p>
        <p style="font-size: 1rem; font-style: italic;">
            Exemple: "J'aime jouer au foot avec mes amis. Nous courons sur le terrain et marquons des buts."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Upload area for the written text
    st.markdown("### Téléverser l'exercice complété:")
    uploaded_file = st.file_uploader("Téléversez une image de l'exercice d'écriture", type=["jpg", "jpeg", "png", "pdf"], key="ecriture_spontanee_upload")
    
    if uploaded_file is not None:
        # Display the uploaded image
        if uploaded_file.type.startswith('image'):
            st.image(uploaded_file, caption="Exercice d'écriture spontanée téléversé", width=400)
        elif uploaded_file.type == 'application/pdf':
            st.warning("Fichier PDF téléversé. Veuillez évaluer le PDF dans un lecteur externe.")
        
        # Store the uploaded file in session state
        st.session_state['dysgraphie_detailed_results']["ecriture_spontanee"]["sample"] = uploaded_file.getvalue()
    
    # Admin observation form
    with st.form("ecriture_spontanee_form"):
        st.markdown("### Évaluation (à remplir par l'adulte):")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Cohérence des phrases:")
            coherence = st.select_slider(
                "Les phrases sont cohérentes:",
                options=["Pas du tout", "Peu", "Assez", "Très"],
                value="Assez",
                key="ecriture_spontanee_coherence"
            )
        
        with col2:
            st.markdown("#### Organisation des mots sur la page:")
            organization = st.select_slider(
                "L'organisation est:",
                options=["Désordonnée", "Peu ordonnée", "Assez ordonnée", "Très ordonnée"],
                value="Assez ordonnée",
                key="ecriture_spontanee_organization"
            )
        
        st.markdown("#### Vitesse d'écriture et fatigue:")
        speed = st.select_slider(
            "L'enfant a écrit:",
            options=["Très lentement avec fatigue évidente", "Lentement avec signes de fatigue", "À vitesse normale, peu de fatigue", "Rapidement sans fatigue"],
            value="À vitesse normale, peu de fatigue",
            key="ecriture_spontanee_speed"
        )
        
        notes = st.text_area("Notes additionnelles:", key="ecriture_spontanee_notes", height=100)
        
        # Calculate score based on observations
        score = 0
        if coherence in ["Assez", "Très"]:
            score += 1
        if organization in ["Assez ordonnée", "Très ordonnée"]:
            score += 1
        if speed in ["À vitesse normale, peu de fatigue", "Rapidement sans fatigue"]:
            score += 1
        
        submit = st.form_submit_button("Enregistrer l'évaluation")
        
        if submit:
            # Save results to session state
            st.session_state['dysgraphie_detailed_results']["ecriture_spontanee"]["score"] = score
            st.session_state['dysgraphie_detailed_results']["ecriture_spontanee"]["notes"] = notes
            st.session_state['dysgraphie_detailed_results']["ecriture_spontanee"]["completed"] = True
            st.success("Évaluation enregistrée!")

def display_vitesse_endurance_test():
    """Display Speed and Endurance Test"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #4ECDC4; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #4ECDC4; text-align: center;">✍️⏳ Test de Vitesse et d'Endurance</h3>
        <p style="text-align: center;">
            L'enfant doit écrire le plus de mots possibles en recopiant une phrase pendant 2 minutes.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Instructions for the administrator
    with st.expander("📋 Instructions pour l'adulte"):
        st.markdown("""
        1. Donnez à l'enfant une feuille de papier et un crayon
        2. Demandez-lui d'écrire la phrase ci-dessous autant de fois que possible en 2 minutes
        3. Utilisez le minuteur ci-dessous pour chronométrer l'exercice
        4. Observez si l'écriture devient de plus en plus illisible ou irrégulière
        5. Comptez le nombre de mots écrits et téléversez une photo du résultat
        """)
    
    # Display the sentence to copy
    st.markdown("### Phrase à recopier:")
    
    st.markdown("""
    <div style="background-color: rgba(78, 205, 196, 0.1); padding: 20px; border-radius: 10px; margin: 15px 0; text-align: center;">
        <p style="font-size: 1.2rem; line-height: 1.6;">
            "Aujourd'hui, il fait beau et je vais à l'école."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Timer functionality
    if 'vitesse_timer_started' not in st.session_state:
        st.session_state['vitesse_timer_started'] = False
        st.session_state['vitesse_timer_end'] = None
    
    col1, col2 = st.columns(2)
    
    with col1:
        if not st.session_state['vitesse_timer_started']:
            if st.button("⏱️ Démarrer le chronomètre (2 minutes)", key="start_vitesse_timer"):
                st.session_state['vitesse_timer_started'] = True
                st.session_state['vitesse_timer_end'] = time.time() + 120  # 2 minutes
                st.rerun()
        else:
            remaining = st.session_state['vitesse_timer_end'] - time.time()
            if remaining <= 0:
                st.success("⌛ Temps écoulé! L'exercice est terminé.")
                st.session_state['vitesse_timer_started'] = False
            else:
                st.markdown(f"""
                <div style="background-color: rgba(255, 0, 0, 0.1); padding: 15px; border-radius: 10px; text-align: center; margin: 10px 0;">
                    <p style="font-size: 1.0rem; margin-bottom: 5px;">Temps restant</p>
                    <div style="font-size: 1.5rem; font-weight: bold; color: #FF0000;">{int(remaining // 60)}:{int(remaining % 60):02d}</div>
                </div>
                """, unsafe_allow_html=True)
                st.rerun()
    
    with col2:
        if st.session_state['vitesse_timer_started']:
            if st.button("⏹️ Arrêter le chronomètre", key="stop_vitesse_timer"):
                st.session_state['vitesse_timer_started'] = False
                st.rerun()
    
    # Upload area for the written text
    st.markdown("### Téléverser l'exercice complété:")
    uploaded_file = st.file_uploader("Téléversez une image de l'exercice d'écriture", type=["jpg", "jpeg", "png", "pdf"], key="vitesse_endurance_upload")
    
    if uploaded_file is not None:
        # Display the uploaded image
        if uploaded_file.type.startswith('image'):
            st.image(uploaded_file, caption="Exercice de vitesse et endurance téléversé", width=400)
        elif uploaded_file.type == 'application/pdf':
            st.warning("Fichier PDF téléversé. Veuillez évaluer le PDF dans un lecteur externe.")
        
        # Store the uploaded file in session state
        st.session_state['dysgraphie_detailed_results']["vitesse_endurance"]["sample"] = uploaded_file.getvalue()
    
    # Admin observation form
    with st.form("vitesse_endurance_form"):
        st.markdown("### Évaluation (à remplir par l'adulte):")
        
        col1, col2 = st.columns(2)
        with col1:
            word_count = st.number_input("Nombre de mots écrits:", min_value=0, value=0, step=1, key="vitesse_endurance_word_count")
        
        with col2:
            st.markdown("#### Qualité de l'écriture au fil du temps:")
            quality_change = st.select_slider(
                "L'écriture est devenue:",
                options=["Beaucoup plus illisible", "Plus illisible", "Légèrement détériorée", "Stable"],
                value="Légèrement détériorée",
                key="vitesse_endurance_quality"
            )
        
        fatigue_signs = st.multiselect(
            "Signes de fatigue observés:",
            ["Pression excessive sur le crayon", "Posture tendue", "Plaintes verbales", "Secouement de la main", "Ralentissement visible", "Aucun signe"],
            default=["Aucun signe"],
            key="vitesse_endurance_fatigue"
        )
        
        notes = st.text_area("Notes additionnelles:", key="vitesse_endurance_notes", height=100)
        
        # Calculate score based on observations
        score = 0
        
        # Score based on word count (adjust thresholds as needed)
        if word_count >= 40:
            score += 1
        elif word_count >= 25:
            score += 0.5
        
        # Score based on quality deterioration
        if quality_change in ["Légèrement détériorée", "Stable"]:
            score += 1
        
        # Score based on fatigue signs
        if "Aucun signe" in fatigue_signs or len(fatigue_signs) <= 1:
            score += 1
        
        # Round to nearest integer
        score = round(score)
        
        submit = st.form_submit_button("Enregistrer l'évaluation")
        
        if submit:
            # Save results to session state
            st.session_state['dysgraphie_detailed_results']["vitesse_endurance"]["score"] = score
            st.session_state['dysgraphie_detailed_results']["vitesse_endurance"]["notes"] = notes
            st.session_state['dysgraphie_detailed_results']["vitesse_endurance"]["word_count"] = word_count
            st.session_state['dysgraphie_detailed_results']["vitesse_endurance"]["completed"] = True
            st.success("Évaluation enregistrée!")

def display_graphisme_coordination_test():
    """Display Graphism and Fine Coordination Test"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #FFD166; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #FFD166; text-align: center;">🖍️ Test de Graphisme et Coordination Fine</h3>
        <p style="text-align: center;">
            L'enfant doit accomplir plusieurs exercices de motricité fine.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Instructions for the administrator
    with st.expander("📋 Instructions pour l'adulte"):
        st.markdown("""
        1. Imprimez les modèles d'exercices ci-dessous ou reproduisez-les sur une feuille
        2. Demandez à l'enfant de compléter les 3 exercices:
           - Relier les points pour tracer une étoile
           - Recopier les formes géométriques
           - Tracer une ligne entre deux points sans lever le crayon
        3. Observez comment l'enfant contrôle ses gestes et suit les lignes
        4. Téléversez une photo du résultat et remplissez l'évaluation
        """)
    
    # Display exercise templates to print
    st.markdown("### Exercices à réaliser:")
    
    # Display star points template
    st.markdown("#### 1. Relie les points pour tracer une étoile:")
    
    # Simple ASCII representation of star points
    st.markdown("""
    ```
         *
         
     *       *
       
    *         *
      
       *   *
    ```
    """)
    
    # Display geometric shapes template
    st.markdown("#### 2. Recopie ces formes géométriques:")
    
    st.markdown("""
    <div style="display: flex; justify-content: space-around; margin: 20px 0;">
        <div style="border: 2px solid black; width: 50px; height: 50px; display: inline-block;"></div>
        <div style="width: 0; height: 0; border-left: 25px solid transparent; border-right: 25px solid transparent; border-bottom: 50px solid black; display: inline-block;"></div>
        <div style="border: 2px solid black; width: 50px; height: 50px; border-radius: 50%; display: inline-block;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Display line tracing template
    st.markdown("#### 3. Trace une ligne entre ces deux points sans lever le crayon:")
    
    st.markdown("""
    <div style="margin: 20px 0; position: relative; height: 100px;">
        <div style="position: absolute; left: 10%; top: 50%; width: 10px; height: 10px; background-color: black; border-radius: 50%;"></div>
        <div style="position: absolute; right: 10%; top: 50%; width: 10px; height: 10px; background-color: black; border-radius: 50%;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Upload area for the completed exercises
    st.markdown("### Téléverser les exercices complétés:")
    uploaded_file = st.file_uploader("Téléversez une image des exercices réalisés", type=["jpg", "jpeg", "png", "pdf"], key="graphisme_upload")
    
    if uploaded_file is not None:
        # Display the uploaded image
        if uploaded_file.type.startswith('image'):
            st.image(uploaded_file, caption="Exercices de graphisme téléversés", width=400)
        elif uploaded_file.type == 'application/pdf':
            st.warning("Fichier PDF téléversé. Veuillez évaluer le PDF dans un lecteur externe.")
        
        # Store the uploaded file in session state
        st.session_state['dysgraphie_detailed_results']["graphisme_coordination"]["sample"] = uploaded_file.getvalue()
    
    # Admin observation form
    with st.form("graphisme_form"):
        st.markdown("### Évaluation (à remplir par l'adulte):")
        
        # Star exercise
        st.markdown("#### Exercice de l'étoile:")
        star_quality = st.select_slider(
            "Qualité du tracé:",
            options=["Très imprécis", "Imprécis", "Assez précis", "Très précis"],
            value="Assez précis",
            key="graphisme_star"
        )
        
        # Geometric shapes exercise
        st.markdown("#### Exercice des formes géométriques:")
        shapes_quality = st.select_slider(
            "Reproduction des formes:",
            options=["Très difficile", "Difficile", "Assez fidèle", "Très fidèle"],
            value="Assez fidèle",
            key="graphisme_shapes"
        )
        
        # Line tracing exercise
        st.markdown("#### Exercice de la ligne:")
        line_steadiness = st.select_slider(
            "Stabilité de la ligne:",
            options=["Très tremblante", "Tremblante", "Assez stable", "Très stable"],
            value="Assez stable",
            key="graphisme_line"
        )
        
        notes = st.text_area("Notes additionnelles:", key="graphisme_notes", height=100)
        
        # Calculate score based on observations
        score = 0
        
        if star_quality in ["Assez précis", "Très précis"]:
            score += 1
        
        if shapes_quality in ["Assez fidèle", "Très fidèle"]:
            score += 1
        
        if line_steadiness in ["Assez stable", "Très stable"]:
            score += 1
        
        submit = st.form_submit_button("Enregistrer l'évaluation")
        
        if submit:
            # Save results to session state
            st.session_state['dysgraphie_detailed_results']["graphisme_coordination"]["score"] = score
            st.session_state['dysgraphie_detailed_results']["graphisme_coordination"]["notes"] = notes
            st.session_state['dysgraphie_detailed_results']["graphisme_coordination"]["completed"] = True
            st.success("Évaluation enregistrée!")

def display_lisibilite_orthographe_test():
    """Display Legibility and Spelling Test"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; border: 3px solid #CC3366; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h3 style="color: #CC3366; text-align: center;">🔤 Test de Lisibilité et Orthographe</h3>
        <p style="text-align: center;">
            L'enfant doit écrire des mots en majuscules et minuscules, puis faire une courte dictée.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Instructions for the administrator
    with st.expander("📋 Instructions pour l'adulte"):
        st.markdown("""
        1. Donnez à l'enfant une feuille de papier et un crayon
        2. Demandez-lui d'écrire les mots indiqués en majuscules puis en minuscules
        3. Ensuite, dictez la phrase à l'enfant et demandez-lui de l'écrire
        4. Observez la formation des lettres et l'orthographe
        5. Téléversez une photo du résultat et remplissez l'évaluation
        """)
    
    # Display the words to write
    st.markdown("### Mots à écrire en majuscules et en minuscules:")
    
    st.markdown("""
    <div style="background-color: rgba(204, 51, 102, 0.1); padding: 20px; border-radius: 10px; margin: 15px 0; text-align: center;">
        <p style="font-size: 1.2rem; line-height: 1.6;">
            CHAT -- ÉCOLE -- POMME -- AMI
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display the dictation sentence
    st.markdown("### Phrase à dicter:")
    
    st.markdown("""
    <div style="background-color: rgba(204, 51, 102, 0.1); padding: 20px; border-radius: 10px; margin: 15px 0; text-align: center;">
        <p style="font-size: 1.2rem; line-height: 1.6;">
            "Le lapin saute dans le jardin et mange une carotte."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Upload area for the completed exercises
    st.markdown("### Téléverser les exercices complétés:")
    uploaded_file = st.file_uploader("Téléversez une image des exercices réalisés", type=["jpg", "jpeg", "png", "pdf"], key="lisibilite_upload")
    
    if uploaded_file is not None:
        # Display the uploaded image
        if uploaded_file.type.startswith('image'):
            st.image(uploaded_file, caption="Exercices de lisibilité téléversés", width=400)
        elif uploaded_file.type == 'application/pdf':
            st.warning("Fichier PDF téléversé. Veuillez évaluer le PDF dans un lecteur externe.")
        
        # Store the uploaded file in session state
        st.session_state['dysgraphie_detailed_results']["lisibilite_orthographe"]["sample"] = uploaded_file.getvalue()
    
    # Admin observation form
    with st.form("lisibilite_form"):
        st.markdown("### Évaluation (à remplir par l'adulte):")
        
        # Uppercase/lowercase quality
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Qualité des majuscules:")
            uppercase_quality = st.select_slider(
                "Formation des lettres:",
                options=["Très difficile", "Difficile", "Assez bonne", "Très bonne"],
                value="Assez bonne",
                key="lisibilite_uppercase"
            )
        
        with col2:
            st.markdown("#### Qualité des minuscules:")
            lowercase_quality = st.select_slider(
                "Formation des lettres:",
                options=["Très difficile", "Difficile", "Assez bonne", "Très bonne"],
                value="Assez bonne",
                key="lisibilite_lowercase"
            )
        
        # Spelling quality
        st.markdown("#### Qualité de l'orthographe dans la dictée:")
        spelling_quality = st.select_slider(
            "Orthographe:",
            options=["Nombreuses erreurs", "Quelques erreurs", "Peu d'erreurs", "Pas d'erreurs"],
            value="Peu d'erreurs",
            key="lisibilite_spelling"
        )
        
        notes = st.text_area("Notes additionnelles:", key="lisibilite_notes", height=100)
        
        # Calculate score based on observations
        score = 0
        
        if uppercase_quality in ["Assez bonne", "Très bonne"]:
            score += 1
        
        if lowercase_quality in ["Assez bonne", "Très bonne"]:
            score += 1
        
        if spelling_quality in ["Peu d'erreurs", "Pas d'erreurs"]:
            score += 1
        
        submit = st.form_submit_button("Enregistrer l'évaluation")
        
        if submit:
            # Save results to session state
            st.session_state['dysgraphie_detailed_results']["lisibilite_orthographe"]["score"] = score
            st.session_state['dysgraphie_detailed_results']["lisibilite_orthographe"]["notes"] = notes
            st.session_state['dysgraphie_detailed_results']["lisibilite_orthographe"]["completed"] = True
            st.success("Évaluation enregistrée!")

def display_results_summary():
    """Display a summary of test results and redirect to the detailed results page"""
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.7); padding: 20px; border-radius: 15px; margin: 20px 0; text-align: center;">
        <h2 style="color: #4CAF50;">Test Terminé!</h2>
        <p style="font-size: 1.2rem;">
            Tous les exercices ont été complétés. Les résultats sont en cours de traitement.
        </p>
        <div style="margin: 20px 0;">
            <div class="loader" style="border: 16px solid #f3f3f3; border-radius: 50%; border-top: 16px solid #3498db; width: 80px; height: 80px; animation: spin 2s linear infinite; margin: 0 auto;"></div>
        </div>
        <p style="font-style: italic;">
            Veuillez patienter pendant que nous analysons les résultats...
        </p>
    </div>
    
    <style>
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Calculate total score
    detailed_results = st.session_state['dysgraphie_detailed_results']
    total_score = sum(data["score"] for data in detailed_results.values())
    max_score = sum(data["max"] for data in detailed_results.values())
    
    # Store information for the results page
    st.session_state['dysgraphie_responses'] = {
        "nom": st.session_state.get("dysgraphie_nom", ""),
        "age": st.session_state.get("dysgraphie_age", 8),
        "classe": st.session_state.get("dysgraphie_classe", ""),
        "detailed_results": detailed_results
    }
    
    # Redirect to results page after a short delay
    import time
    time.sleep(2)  # Simulate processing time
    
    # Redirect to results page when it's available (for now, go back to home)
    st.session_state['page'] = "resultats_dysgraphie" if "resultats_dysgraphie" in st.session_state['page'] else "accueil"
    st.rerun()