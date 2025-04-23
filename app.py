# File path: app.py
import streamlit as st
from src.interface.styles import apply_styles
from src.interface.sidebar import show_sidebar
from src.interface.pages import home, questionnaire, test_selection, test_dyscalculie, test_tdah, results_dyscalculie, results_tdah
import src.interface.pages.test_dyslexie as test_dyslexie
import src.interface.pages.results_dyslexie as results_dyslexie
import src.interface.pages.test_dysgraphie as test_dysgraphie
import src.interface.pages.results_dysgraphie as results_dysgraphie

# Configure the page
st.set_page_config(
    page_title="Smart-Aid - Évaluation Éducative Interactive",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styles
apply_styles()

# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = 'accueil'
if 'all_responses' not in st.session_state:
    st.session_state['all_responses'] = []
if 'dyscalculie_responses' not in st.session_state:
    st.session_state['dyscalculie_responses'] = None
if 'tdah_responses' not in st.session_state:
    st.session_state['tdah_responses'] = None
if 'responses' not in st.session_state:
    st.session_state['responses'] = None
if 'dyscalculia_analysis' not in st.session_state:
    st.session_state['dyscalculia_analysis'] = None
if 'tdah_analysis' not in st.session_state:
    st.session_state['tdah_analysis'] = None
if 'dyscalculia_solution' not in st.session_state:
    st.session_state['dyscalculia_solution'] = None
if 'current_activity' not in st.session_state:
    st.session_state['current_activity'] = None
if 'recommended_activities' not in st.session_state:
    st.session_state['recommended_activities'] = None
if 'questionnaire_responses' not in st.session_state:
    st.session_state['questionnaire_responses'] = None
if 'suggested_test' not in st.session_state:
    st.session_state['suggested_test'] = None
if 'dysgraphie_responses' not in st.session_state:
    st.session_state['dysgraphie_responses'] = None
if 'dysgraphie_analysis' not in st.session_state:
    st.session_state['dysgraphie_analysis'] = None

# Show sidebar
show_sidebar()

# Route to the correct page based on state
if st.session_state['page'] == 'accueil':
    home.show_page()
elif st.session_state['page'] == 'questionnaire':
    questionnaire.show_page()
elif st.session_state['page'] == 'test_selection':
    test_selection.show_page()
elif st.session_state['page'] == 'test_dyscalculie':
    test_dyscalculie.show_page()
elif st.session_state['page'] == 'test_tdah':
    test_tdah.show_page()
elif st.session_state['page'] == 'test_dyslexie':
    test_dyslexie.show_page()
elif st.session_state['page'] == 'test_dysgraphie':
    test_dysgraphie.show_page()
elif st.session_state['page'] == 'resultats_dyscalculie':
    results_dyscalculie.show_page()
elif st.session_state['page'] == 'resultats_tdah':
    results_tdah.show_page()
elif st.session_state['page'] == 'resultats_dyslexie':
    results_dyslexie.show_page()
elif st.session_state['page'] == 'resultats_dysgraphie':
    results_dysgraphie.show_page()