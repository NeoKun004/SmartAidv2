import streamlit as st

def apply_styles():
    """Apply custom CSS styles to the application"""
    st.markdown("""
    <style>
        /* Fond général avec image */
        .stApp {
            background-image: url("https://img.freepik.com/free-vector/hand-drawn-colorful-math-background_23-2148157266.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }
        
        /* Ajouter une superposition semi-transparente pour améliorer la lisibilité */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.7);
            z-index: -1;
        }
        
        /* Fond général et polices */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        
        /* Titres */
        h1 {
            color: #FF6B6B;
            text-align: center;
            font-size: 3rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
            background: rgba(255,255,255,0.7);
            padding: 15px;
            border-radius: 15px;
            border: 3px dashed #4ECDC4;
        }
        
        h2, h3 {
            color: #5D5FEF;
            margin-top: 1.5rem;
            background: rgba(255,255,255,0.5);
            padding: 10px;
            border-radius: 10px;
            border-left: 5px solid #5D5FEF;
        }
        
        /* Formulaires et entrées */
        .stTextInput, .stNumberInput, .stSelectbox {
            background-color: rgba(255,255,255,0.8);
            border-radius: 10px;
            padding: 5px;
            border: 2px solid #4ECDC4;
        }
        
        .stTextInput:focus, .stNumberInput:focus, .stSelectbox:focus {
            border: 2px solid #FF6B6B;
        }
        
        /* Boutons */
        .stButton>button {
            background-color: #4ECDC4;
            color: white;
            font-weight: bold;
            border-radius: 20px;
            padding: 10px 25px;
            font-size: 1.2rem;
            border: none;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: #FF6B6B;
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0,0,0,0.15);
        }
        
        /* Messages */
        .stSuccess {
            background-color: rgba(78, 205, 196, 0.2);
            border: 2px solid #4ECDC4;
            border-radius: 10px;
            padding: 10px;
            color: #2A9D8F;
        }
        
        .stWarning {
            background-color: rgba(255, 107, 107, 0.2);
            border: 2px solid #FF6B6B;
            border-radius: 10px;
            padding: 10px;
            color: #E76F51;
        }
        
        .stInfo {
            background-color: rgba(93, 95, 239, 0.2);
            border: 2px solid #5D5FEF;
            border-radius: 10px;
            padding: 10px;
            color: #3A0CA3;
        }
        
        /* Séparateurs */
        hr {
            border: none;
            height: 3px;
            background: linear-gradient(90deg, transparent, #FF6B6B, #4ECDC4, #5D5FEF, transparent);
            margin: 2rem 0;
        }
        
        /* Questions numérotées */
        label {
            font-size: 1.1rem;
            font-weight: bold;
            color: #2A9D8F;
            background: rgba(255,255,255,0.7);
            padding: 8px 15px;
            border-radius: 8px;
            display: inline-block;
            margin-bottom: 5px;
            border-left: 4px solid #FF6B6B;
        }
        
        /* Conteneurs de questions */
        .question-container {
            background-color: rgba(255,255,255,0.6);
            padding: 15px;
            border-radius: 15px;
            margin-bottom: 15px;
            border: 2px solid #4ECDC4;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        /* Animation pour les éléments interactifs */
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .interactive-element {
            animation: pulse 2s infinite;
        }
        
        /* Tableaux de résultats */
        .dataframe {
            border-collapse: separate;
            border-spacing: 0;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .dataframe th {
            background-color: #5D5FEF;
            color: white;
            padding: 12px;
            text-align: center;
        }
        
        .dataframe td {
            padding: 10px;
            background-color: rgba(255,255,255,0.8);
        }
        
        /* Jauge de score */
        .score-gauge {
            background-color: rgba(255,255,255,0.8);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border: 3px solid #4ECDC4;
        }
        
        /* Espacement modéré entre les éléments */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        
        /* Ajouter un peu d'espace entre les cartes sur la page d'accueil */
        div.css-1r6slb0 {
            margin-bottom: 0.8rem !important;
            margin-top: 0.8rem !important;
        }
        
        /* Ajouter un peu d'espace entre les sections */
        .question-container {
            margin-bottom: 12px !important;
            margin-top: 12px !important;
        }
        
        /* Ajouter un peu d'espace entre les questions */
        .stTextInput, .stNumberInput, .stSelectbox {
            margin-bottom: 8px !important;
        }
        
        /* Ajouter un peu d'espace autour des boutons */
        .stButton {
            margin-top: 10px !important;
            margin-bottom: 10px !important;
        }
        
        /* Ajouter un peu d'espace autour des titres */
        h1, h2, h3 {
            margin-top: 12px !important;
            margin-bottom: 8px !important;
        }
        
        /* Ajouter de l'espace autour des messages */
        .stSuccess, .stWarning, .stInfo, .stError {
            margin-top: 15px !important;
            margin-bottom: 15px !important;
        }
        
        /* Ajouter de l'espace entre les éléments de la barre latérale */
        .css-1544g2n {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        .css-1544g2n > div {
            margin-bottom: 20px !important;
        }
        
        /* Ajouter de l'espace entre les cartes sur la page d'accueil */
        .css-12w0qpk {
            margin: 1rem 0 !important;
            padding: 1.5rem !important;
            border-radius: 15px !important;
        }
        
        /* Personnalisation de la sidebar */
        [data-testid="stSidebar"] {
            background-color: #a6fed4 !important;
        }
    </style>
    """, unsafe_allow_html=True)