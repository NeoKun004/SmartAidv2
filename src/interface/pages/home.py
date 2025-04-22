import streamlit as st
from src.utils.image_utils import dyscalc_b64, dtha_b64
import os

def show_page():
    """Display the enhanced home page with animated title and local video"""

    # CSS pour les animations et l'esthétique améliorée
    st.markdown("""
    <style>
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }

        @keyframes colorChange {
            0% { color: #FF6B6B; }
            25% { color: #4ECDC4; }
            50% { color: #5D5FEF; }
            75% { color: #FFD166; }
            100% { color: #FF6B6B; }
        }

        .main-title {
            font-size: 4rem;
            font-weight: bold;
            text-align: center;
            animation: colorChange 8s infinite;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.2);
            margin-bottom: 0.5rem;
        }

        .subtitle {
            font-size: 1.5rem;
            text-align: center;
            margin-bottom: 2rem;
            line-height: 1.5;
            color: #333;
        }

        .emoji-float {
            font-size: 3rem;
            display: inline-block;
            animation: float 3s infinite ease-in-out;
            margin: 0 10px;
        }

        .emoji-1 { animation-delay: 0s; }
        .emoji-2 { animation-delay: 0.5s; }
        .emoji-3 { animation-delay: 1s; }
        .emoji-4 { animation-delay: 1.5s; }
        .emoji-5 { animation-delay: 2s; }

        .card-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin: 2rem 0;
        }

        .card {
            background-color: rgba(255,255,255,0.9);
            border-radius: 15px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            flex: 1;
            min-width: 300px;
        }

        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 12px 20px rgba(0,0,0,0.15);
        }

        .stButton>button {
            background: linear-gradient(45deg, #FF6B6B, #5D5FEF);
            color: white;
            border: none;
            border-radius: 30px;
            padding: 12px 30px;
            font-size: 1.2rem;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            text-align: center;
            display: block;
            width: 100%;
        }

        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 15px rgba(0,0,0,0.25);
        }

        .stButton:nth-of-type(1)>button {
            background: linear-gradient(45deg, #5D5FEF, #4ECDC4);
        }

        .stButton:nth-of-type(2)>button {
            background: linear-gradient(45deg, #FF6B6B, #FFD166);
        }
    </style>
    """, unsafe_allow_html=True)

    # Titre animé avec emojis flottants
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 30px; border-radius: 20px; margin-bottom: 20px; box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
        <div class="main-title">✨ SmartAid ✨</div>
        <div style="text-align: center; margin-bottom: 20px;">
            <span class="emoji-float emoji-1">🧠</span>
            <span class="emoji-float emoji-2">🚀</span>
            <span class="emoji-float emoji-3">🔮</span>
            <span class="emoji-float emoji-4">🎮</span>
            <span class="emoji-float emoji-5">🎨</span>
        </div>
        <div class="subtitle">
            Bienvenue dans ton espace magique d'apprentissage avec l'IA !<br>
            Prêt pour une aventure pleine de découvertes et de fun ?
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section vidéo locale
    video_path = "/home/ubuntu/side/SmartAid/data/intro.mp4"
    if os.path.exists(video_path):
        with open(video_path, "rb") as video_file:
            video_bytes = video_file.read()

        st.markdown("""
        <div style="background-color: rgba(255,255,255,0.8); padding: 30px; border-radius: 20px; margin-bottom: 20px; box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
            <h2 style="text-align: center; color: #5D5FEF; margin-bottom: 20px;">🎬 Découvre SmartAid en vidéo !</h2>
        </div>
        """, unsafe_allow_html=True)

        st.video(video_bytes)

        st.markdown("""
        <p style="text-align: center; margin-top: 15px; font-style: italic; color: #666;">
            Regarde cette vidéo pour en savoir plus sur notre aventure magique d'apprentissage !
        </p>
        """, unsafe_allow_html=True)
    else:
        st.warning("La vidéo d'introduction n'a pas été trouvée.")

    # Cartes interactives
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 30px; border-radius: 20px; margin-bottom: 20px; box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
        <h2 style="text-align: center; color: #FF6B6B; margin-bottom: 20px;">🧙‍♂️ Choisis ton chemin magique !</h2>
        <div class="card-container">
            <div class="card" style="border-top: 5px solid #5D5FEF;">
                <h3 style="color: #5D5FEF; text-align: center;">👨‍👩‍👧‍👦 Pour les Adultes</h3>
                <p style="text-align: center;">Parents et enseignants, complétez notre questionnaire pour nous aider à mieux comprendre les besoins de l'enfant.</p>
                <div style="text-align: center; margin: 15px 0;">
                    <img src="data:image/png;base64,""" + dtha_b64 + """" style="max-width: 80%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
                </div>
            </div>
            <div class="card" style="border-top: 5px solid #4ECDC4;">
                <h3 style="color: #4ECDC4; text-align: center;">👧‍👦 Pour les Enfants</h3>
                <p style="text-align: center;">Pars à l'aventure et découvre des jeux et des activités magiques adaptés juste pour toi !</p>
                <div style="text-align: center; margin: 15px 0;">
                    <img src="data:image/png;base64,""" + dyscalc_b64 + """" style="max-width: 80%; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Boutons d'action
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧩 Commencer le questionnaire", key="btn_questionnaire"):
            st.session_state['page'] = 'questionnaire'
            st.rerun()

    with col2:
        if st.button("🎮 Aller aux activités magiques", key="btn_direct_tests"):
            st.session_state['page'] = 'test_selection'
            st.rerun()

    # Section "À propos"
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.8); padding: 20px; border-radius: 20px; margin-top: 30px; box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
        <h2 style="color: #5D5FEF; text-align: center;">✨ La magie de SmartAid ✨</h2>
        <p style="font-size: 1.1rem; text-align: center;">
            SmartAid utilise l'intelligence artificielle pour créer une expérience d'apprentissage personnalisée 
            et adaptée aux besoins de chaque enfant. Nos activités sont conçues pour être amusantes 
            tout en développant des compétences essentielles.
        </p>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin-top: 20px;">
            <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin: 10px; width: 200px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <h3 style="color: #FF6B6B;">🔍 Détection</h3>
                <p>Identifie les forces et les points à améliorer</p>
            </div>
            <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin: 10px; width: 200px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <h3 style="color: #4ECDC4;">🧠 Adaptation</h3>
                <p>Activités personnalisées selon les besoins</p>
            </div>
            <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin: 10px; width: 200px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <h3 style="color: #5D5FEF;">🚀 Progression</h3>
                <p>Suivi des améliorations et nouveaux défis</p>
            </div>
            <div style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 15px; margin: 10px; width: 200px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <h3 style="color: #FFD166;">🎮 Amusement</h3>
                <p>Apprentissage ludique et motivant</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
