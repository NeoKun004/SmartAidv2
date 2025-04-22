import streamlit as st
import os
import base64
import random

def provide_dyslexie_solution(risk_score):
    """
    Provide interactive solutions for dyslexia based on test results.
    
    Args:
        risk_score (int): The risk score from the dyslexia test (0-100)
    """
    # Track which tab is selected
    if 'dyslexie_selected_tab' not in st.session_state:
        st.session_state['dyslexie_selected_tab'] = 0
    
    # Define the solution tabs with on_change callback to track selection
    tab_names = [
        "📖 Assistant de Lecture IA", 
        "🎙️ Synthèse Vocale", 
        "📊 Générateur d'Exercices", 
        "🎵 Transformation Vocale"
    ]
    
    # Create tab objects
    tabs = st.tabs(tab_names)
    
    # Track which tab is currently active for audio autoplay
    current_tab_index = st.session_state['dyslexie_selected_tab']
    
    # Tab 1: Assistant de Lecture IA
    with tabs[0]:
        if current_tab_index == 0:
            st.session_state['dyslexie_selected_tab'] = 0
        
        st.markdown("""
        <div style="background-color: #f0f7ff; padding: 20px; border-radius: 10px; border-left: 5px solid #3a86ff;">
            <h3 style="color: #3a86ff;">📖 Assistant de Lecture IA</h3>
            <p style="font-size: 1.1rem;">
                L'IA adapte la présentation du texte pour aider les élèves à mieux lire.
            </p>
            <h4>Fonctions principales:</h4>
            <ul>
                <li>Découpage des mots en syllabes</li>
                <li>Mise en couleur des lettres ou syllabes difficiles</li>
                <li>Agrandissement des espaces entre les lettres</li>
                <li>Génération de résumés pour simplifier la compréhension</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Audio playback
        audio_file = "/home/ubuntu/side/SmartAid/assets/audio/solutions/dyslexie/ex1.mp3"
        display_audio_with_autoplay(audio_file, "lecture_ia", autoplay=(current_tab_index == 0))
        
        # Example of text transformation
        st.markdown("### Exemple d'utilisation:", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background-color: rgba(58, 134, 255, 0.1); padding: 15px; border-radius: 10px; margin: 15px 0;">
            <h4 style="color: #3a86ff;">Texte normal:</h4>
            <p style="font-size: 1.2rem;">Le petit garçon joue dans le parc.</p>
            
            <h4 style="color: #3a86ff; margin-top: 20px;">Texte transformé par l'IA:</h4>
            <p style="font-size: 1.2rem; font-weight: bold;">Le pe-tit gar-çon joue dans le parc.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive example
        st.markdown("### Essaie avec ton propre texte:", unsafe_allow_html=True)
        
        user_text = st.text_area("Entre une phrase simple:", value="La petite fille mange une pomme.", height=100)
        
        if st.button("Transformer le texte", key="transform_text"):
            # Simple syllable separation logic
            words = user_text.split()
            transformed_words = []
            
            for word in words:
                if len(word) > 3:
                    # Very simple syllable separation (not linguistically accurate)
                    middle = len(word) // 2
                    transformed = word[:middle] + "-" + word[middle:]
                    transformed_words.append(transformed)
                else:
                    transformed_words.append(word)
            
            transformed_text = " ".join(transformed_words)
            
            st.markdown(f"""
            <div style="background-color: rgba(58, 134, 255, 0.1); padding: 15px; border-radius: 10px; margin: 15px 0;">
                <h4 style="color: #3a86ff;">Texte transformé:</h4>
                <p style="font-size: 1.3rem; font-weight: bold;">{transformed_text}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Tab 2: Synthèse Vocale et Reconnaissance de la Lecture
    with tabs[1]:
        if current_tab_index == 1:
            st.session_state['dyslexie_selected_tab'] = 1
            
        st.markdown("""
        <div style="background-color: #fff0f7; padding: 20px; border-radius: 10px; border-left: 5px solid #ff3a86;">
            <h3 style="color: #ff3a86;">🎙️ Synthèse Vocale et Reconnaissance de la Lecture</h3>
            <p style="font-size: 1.1rem;">
                L'IA écoute l'enfant lire et l'aide à améliorer sa prononciation et sa compréhension.
            </p>
            <h4>Comment ça fonctionne:</h4>
            <ul>
                <li>L'enfant lit un texte à voix haute</li>
                <li>L'IA analyse la prononciation et détecte les erreurs</li>
                <li>L'IA propose une correction vocale et des exercices personnalisés</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Audio playback
        audio_file = "/home/ubuntu/side/SmartAid/assets/audio/solutions/dyslexie/ex2.mp3"
        display_audio_with_autoplay(audio_file, "vocal_recognition", autoplay=(current_tab_index == 1))
        
        # Example
        st.markdown("### Exemple d'utilisation:", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background-color: rgba(255, 58, 134, 0.1); padding: 15px; border-radius: 10px; margin: 15px 0;">
            <p style="font-size: 1.1rem;"><b>👦 L'élève lit :</b> "Le chat grimpe sur le sofa."</p>
            <p style="font-size: 1.1rem;"><b>🤖 L'IA détecte que l'élève dit :</b> "Le <span style="color: #ff3a86; font-weight: bold;">chot</span> grimpe sur le sofa."</p>
            <p style="font-size: 1.1rem;"><b>🔹 Correction audio :</b> 🔊 <i>"Écoute bien la différence entre 'chat' et 'chot'."</i></p>
        </div>
        
        <div style="background-color: rgba(255, 58, 134, 0.05); padding: 15px; border-radius: 10px; margin: 15px 0;">
            <h4 style="color: #ff3a86;">Pourquoi c'est utile ?</h4>
            <ul>
                <li>Permet aux enfants d'apprendre à leur rythme</li>
                <li>Renforce le lien entre l'oral et l'écrit</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive demonstration
        st.markdown("### Essaie avec ton propre texte:", unsafe_allow_html=True)
        
        practice_text = st.text_input("Texte à lire:", value="Le chat saute sur le mur.")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
            <div style="background-color: rgba(255, 58, 134, 0.1); padding: 15px; border-radius: 10px; text-align: center;">
                <p style="font-size: 1.5rem;">{practice_text}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.button("🎤 Commencer l'enregistrement", key="start_recording_reading")
        
        st.info("Cette fonctionnalité nécessite un microphone. La reconnaissance vocale sera disponible prochainement!")
    
    # Tab 3: Générateur Automatique d'Exercices Adaptés
    with tabs[2]:
        if current_tab_index == 2:
            st.session_state['dyslexie_selected_tab'] = 2
            
        st.markdown("""
        <div style="background-color: #fffaf0; padding: 20px; border-radius: 10px; border-left: 5px solid #ffc300;">
            <h3 style="color: #ffc300;">📊 Générateur Automatique d'Exercices Adaptés</h3>
            <p style="font-size: 1.1rem;">
                L'IA crée des exercices personnalisés selon les difficultés de l'élève.
            </p>
            <h4>Fonctionnalités:</h4>
            <ul>
                <li>Génération d'exercices interactifs adaptés au niveau de l'enfant</li>
                <li>Adaptation en temps réel selon les progrès</li>
                <li>Suggestions d'exercices de lecture et d'écriture personnalisés</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Audio playback
        audio_file = "/home/ubuntu/side/SmartAid/assets/audio/solutions/dyslexie/ex3.mp3"
        display_audio_with_autoplay(audio_file, "exercises_generator", autoplay=(current_tab_index == 2))
        
        # Interactive example
        st.markdown("### Exemple d'exercice généré:", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background-color: rgba(255, 195, 0, 0.1); padding: 20px; border-radius: 10px; margin: 15px 0;">
            <h4 style="color: #ffc300;">Texte de lecture:</h4>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                Ce soir, maman raconte une histoire à Ahmad.<br>
                Il est fatigué mais il adore écouter les contes.<br>
                "Il était une fois un petit lapin courageux..." commence maman.<br>
                Ahmad ferme les yeux et imagine le lapin qui saute dans la forêt.<br>
                Peu à peu, il s'endort, heureux.
            </p>
            
            <h4 style="color: #ffc300; margin-top: 20px;">Questions de compréhension:</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive questions
        q1 = st.text_input("Qui raconte une histoire à Ahmad ?")
        q2 = st.text_input("Comment se sent Ahmad ?")
        q3 = st.text_input("Qu'aime-t-il écouter ?")
        
        if st.button("Vérifier mes réponses", key="check_answers"):
            score = 0
            feedback = []
            
            if "maman" in q1.lower():
                score += 1
                feedback.append("Question 1: ✅ Correct! C'est bien maman qui raconte l'histoire.")
            else:
                feedback.append("Question 1: ❌ La réponse correcte est 'maman'.")
                
            if "fatigué" in q2.lower():
                score += 1
                feedback.append("Question 2: ✅ Correct! Ahmad est fatigué.")
            else:
                feedback.append("Question 2: ❌ La réponse correcte est 'fatigué'.")
                
            if "contes" in q3.lower() or "histoires" in q3.lower():
                score += 1
                feedback.append("Question 3: ✅ Correct! Ahmad aime écouter les contes.")
            else:
                feedback.append("Question 3: ❌ La réponse correcte est 'les contes'.")
            
            # Display feedback
            st.markdown(f"""
            <div style="background-color: rgba(255, 195, 0, 0.1); padding: 15px; border-radius: 10px; margin: 15px 0;">
                <h4 style="color: #ffc300;">Résultats:</h4>
                <p>Score: {score}/3</p>
                <ul>
                    {"".join(f"<li>{fb}</li>" for fb in feedback)}
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # Adaptive exercise suggestion based on mistakes
            if score < 3:
                st.markdown("""
                <div style="background-color: rgba(255, 195, 0, 0.05); padding: 15px; border-radius: 10px; margin: 15px 0;">
                    <h4 style="color: #ffc300;">Suggestion d'exercice adapté:</h4>
                    <p>Basé sur tes réponses, voici un exercice qui pourrait t'aider à améliorer ta compréhension de lecture.</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Tab 4: Transformation Vocale
    with tabs[3]:
        if current_tab_index == 3:
            st.session_state['dyslexie_selected_tab'] = 3
            
        st.markdown("""
        <div style="background-color: #f0f9ff; padding: 20px; border-radius: 10px; border-left: 5px solid #2196F3;">
            <h3 style="color: #2196F3;">🎵 Transformation Vocale</h3>
            <p style="font-size: 1.1rem;">
                L'IA transforme une phrase écrite en un clip vocal interactif pour aider l'enfant à mieux comprendre et retenir les mots.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Example
        st.markdown("### Exemple d'utilisation:", unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background-color: rgba(33, 150, 243, 0.1); padding: 15px; border-radius: 10px; margin: 15px 0;">
            <p style="font-size: 1.1rem;"><b>👦 L'enfant écrit :</b> "J'aime jouer au ballon."</p>
            <p style="font-size: 1.1rem;"><b>🤖 L'IA génère une voix qui dit la phrase de différentes manières :</b></p>
            <ul>
                <li><b>Version lente:</b> "J'ai-me jouer au bal-lon."</li>
                <li><b>Version chantée:</b> "J'aaaime jouer au ballon !"</li>
                <li><b>Version robotique:</b> "J'AIME... JOUER... AU BALLON..."</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive transformation
        st.markdown("### Essaie avec ta propre phrase:", unsafe_allow_html=True)
        
        user_phrase = st.text_input("Entre une phrase simple:", value="J'aime jouer au ballon.")
        
        # Voice style selection
        voice_style = st.radio(
            "Choisis un style vocal:",
            ["Version lente", "Version chantée", "Version robotique"],
            horizontal=True
        )
        
        # Audio file mapping
        audio_files = {
            "Version lente": "/home/ubuntu/side/SmartAid/assets/audio/solutions/dyslexie/ex4lente.mp3",
            "Version chantée": "/home/ubuntu/side/SmartAid/assets/audio/solutions/dyslexie/ex4chante.mp3",
            "Version robotique": "/home/ubuntu/side/SmartAid/assets/audio/solutions/dyslexie/ex4robot.mp3"
        }
        
        # Display selected transformation
        if voice_style:
            audio_file = audio_files[voice_style]
            
            # Description of transformation
            descriptions = {
                "Version lente": "Les syllabes sont prononcées lentement pour mieux entendre chaque son",
                "Version chantée": "La phrase est chantée pour rendre l'apprentissage plus amusant",
                "Version robotique": "Les mots sont séparés distinctement comme par un robot"
            }
            
            st.markdown(f"""
            <div style="background-color: rgba(33, 150, 243, 0.1); padding: 15px; border-radius: 10px; margin: 15px 0;">
                <h4 style="color: #2196F3;">Ta phrase en {voice_style.lower()}:</h4>
                <p>{descriptions[voice_style]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display audio player
            display_audio_with_autoplay(audio_file, f"vocal_transform_{voice_style}", autoplay=False)
    
    # Add hidden tab change detection (same as before)
    for i, tab_name in enumerate(tab_names):
        if i != st.session_state['dyslexie_selected_tab']:
            if tabs[i]:
                st.markdown(f"""
                <script>
                    // Tab change detection for tab {i}
                    (function() {{
                        const tabHeaders = document.querySelectorAll('[data-baseweb="tab-list"] [role="tab"]');
                        if (tabHeaders && tabHeaders.length > {i}) {{
                            tabHeaders[{i}].addEventListener('click', function() {{
                                // Use a hidden button to trigger a Streamlit event
                                document.getElementById('tab_change_btn_{i}').click();
                            }});
                        }}
                    }})();
                </script>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <button id="tab_change_btn_{i}" style="display: none;"></button>
                """, unsafe_allow_html=True)
                
                if st.button(f"Change to tab {i}", key=f"change_tab_{i}", help="This button is controlled by JavaScript", 
                           on_click=lambda idx=i: set_active_tab(idx)):
                    pass

def set_active_tab(tab_index):
    """Set the active tab index in session state"""
    st.session_state['dyslexie_selected_tab'] = tab_index

def display_audio_with_autoplay(file_path, key_prefix, autoplay=False):
    """
    Display audio player with optional autoplay functionality and replay button.
    
    Args:
        file_path (str): Path to the audio file
        key_prefix (str): Prefix for the session state keys
        autoplay (bool): Whether to autoplay the audio
    """
    # Set up auto-play flag if not already in session state
    auto_play_key = f"{key_prefix}_auto_play"
    if auto_play_key not in st.session_state:
        st.session_state[auto_play_key] = autoplay
    
    # Try to read audio file
    try:
        # Check if file exists and handle either case
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                audio_bytes = f.read()
        else:
            # Create a placeholder for when the file doesn't exist yet
            st.warning(f"Le fichier audio '{file_path}' n'est pas disponible. Ajoutez-le pour entendre l'explication.")
            return
        
        # Get file type
        file_extension = file_path.split(".")[-1].lower()
        if file_extension == "mp3":
            mime_type = "audio/mp3"
        elif file_extension == "wav":
            mime_type = "audio/wav"
        else:
            mime_type = f"audio/{file_extension}"
        
        # Encode audio for embedding
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
        
        # Create audio player with autoplay if needed
        autoplay_attr = 'autoplay' if st.session_state[auto_play_key] else ''
        
        # Audio player HTML
        audio_html = f"""
        <div style="display: flex; align-items: center; margin: 15px 0;">
            <audio id="{key_prefix}_player" controls {autoplay_attr} style="width: 100%;">
                <source src="data:{mime_type};base64,{audio_base64}" type="{mime_type}">
                Votre navigateur ne supporte pas l'élément audio.
            </audio>
        </div>
        """
        
        st.markdown(audio_html, unsafe_allow_html=True)
        
        # Add replay button
        col1, col2 = st.columns([5, 1])
        with col2:
            if st.button("🔄 Replay", key=f"{key_prefix}_replay"):
                # We can't directly control the audio element from Python,
                # but we can reload the component which will trigger autoplay
                st.session_state[auto_play_key] = True
                st.rerun()
        
        # Reset autoplay for next time if it was triggered by replay
        if st.session_state[auto_play_key] and not autoplay:
            st.session_state[auto_play_key] = False
    
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier audio: {str(e)}")