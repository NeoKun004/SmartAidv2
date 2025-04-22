import logging
from src.llm_connector import get_llm_connector

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_dyscalculie_recommendations(test_summary, total_score, max_score):
    """
    Generate personalized recommendations for dyscalculia based on test results.
    
    Args:
        test_summary (str): Summary of test results
        total_score (int): Total score obtained
        max_score (int): Maximum possible score
        
    Returns:
        str: Personalized recommendations
    """
    # Get the LLM connector
    llm_connector = get_llm_connector()
    
    try:
        prompt = f"""
        Tu es un expert en troubles d'apprentissage, spécialisé dans la dyscalculie. Un enfant vient de passer un test de dépistage de la dyscalculie avec les résultats suivants:
        
        {test_summary}
        
        Score total: {total_score}/{max_score}
        
        Génère des recommandations personnalisées pour aider cet enfant à améliorer ses compétences mathématiques. Inclus:
        1. Une évaluation du risque de dyscalculie (faible, modéré, élevé)
        2. Des activités spécifiques adaptées à ses difficultés
        3. Des conseils pour les parents et enseignants
        4. Des stratégies d'apprentissage adaptées
        
        Formaté en HTML simple avec des titres, paragraphes et listes.
        """
        
        # System prompt for the model
        system_prompt = "Tu es un pédagogue spécialisé dans l'évaluation des enfants ayant des troubles d'apprentissage. Tu donnes des analyses bienveillantes, positives et encourageantes."
        
        # Call the LLM model
        recommendations = llm_connector.generate_response(
            prompt=prompt,
            system_prompt=system_prompt,
            max_tokens=800,
            temperature=0.7
        )
        
        # Check that the response is not None or empty
        if recommendations is None or recommendations.strip() == "":
            logger.error("The LLM response is empty or None!")
            return "Je n'ai pas pu générer des recommandations. Veuillez réessayer plus tard."
        
        return recommendations
        
    except Exception as e:
        logger.error(f"Error generating dyscalculie recommendations: {str(e)}")
        
        # Fallback recommendations if LLM fails
        risk_level = "élevé" if total_score / max_score < 0.5 else "modéré" if total_score / max_score < 0.8 else "faible"
        
        fallback = f"""
        <h3>Évaluation du risque de dyscalculie: {risk_level}</h3>
        <p>Basé sur les résultats du test, voici quelques recommandations:</p>
        <ul>
            <li>Pratiquer régulièrement des activités avec les nombres</li>
            <li>Utiliser des supports visuels et manipulatifs</li>
            <li>Décomposer les problèmes mathématiques en étapes plus simples</li>
            <li>Renforcer les concepts de base avant de passer à des concepts plus avancés</li>
        </ul>
        <p>Si les difficultés persistent, une consultation avec un professionnel spécialisé est recommandée.</p>
        """
        
        return fallback

def generate_tdah_recommendations(test_summary, total_score, max_score):
    """
    Generate personalized recommendations for ADHD based on test results.
    
    Args:
        test_summary (str): Summary of test results
        total_score (int): Total score obtained
        max_score (int): Maximum possible score
        
    Returns:
        str: Personalized recommendations
    """
    # Get the LLM connector
    llm_connector = get_llm_connector()
    
    try:
        prompt = f"""
        Tu es un expert en troubles d'apprentissage, spécialisé dans le TDAH. Un enfant vient de passer un test de dépistage du TDAH avec les résultats suivants:
        
        {test_summary}
        
        Score total: {total_score}/{max_score}
        
        Génère des recommandations personnalisées pour aider cet enfant à améliorer son attention et sa concentration. Inclus:
        1. Une évaluation du risque de TDAH (faible, modéré, élevé)
        2. Des stratégies spécifiques adaptées à ses difficultés
        3. Des conseils pour les parents et enseignants
        4. Des techniques d'organisation et de gestion du temps
        
        Formaté en HTML simple avec des titres, paragraphes et listes.
        """
        
        # System prompt for the model
        system_prompt = "Tu es un pédagogue spécialisé dans l'évaluation des enfants ayant des troubles d'attention. Tu donnes des analyses bienveillantes, positives et encourageantes."
        
        # Call the LLM model
        recommendations = llm_connector.generate_response(
            prompt=prompt,
            system_prompt=system_prompt,
            max_tokens=800,
            temperature=0.7
        )
        
        # Check that the response is not None or empty
        if recommendations is None or recommendations.strip() == "":
            logger.error("The LLM response is empty or None!")
            return "Je n'ai pas pu générer des recommandations. Veuillez réessayer plus tard."
        
        return recommendations
        
    except Exception as e:
        logger.error(f"Error generating TDAH recommendations: {str(e)}")
        
        # Fallback recommendations if LLM fails
        risk_level = "élevé" if total_score / max_score > 0.7 else "modéré" if total_score / max_score > 0.4 else "faible"
        
        fallback = f"""
        <h3>Évaluation du risque de TDAH: {risk_level}</h3>
        <p>Basé sur les résultats du test, voici quelques recommandations:</p>
        <ul>
            <li>Créer un environnement de travail avec peu de distractions</li>
            <li>Établir des routines claires et prévisibles</li>
            <li>Diviser les tâches en étapes plus petites et gérable</li>
            <li>Utiliser des outils visuels comme des minuteurs et des listes</li>
        </ul>
        <p>Si les difficultés persistent, une consultation avec un professionnel spécialisé est recommandée.</p>
        """
        
        return fallback

def generate_dyslexie_recommendations(test_summary, total_score, max_score):
    """
    Generate personalized recommendations for dyslexia based on test results.
    
    Args:
        test_summary (str): Summary of test results
        total_score (int): Total score obtained
        max_score (int): Maximum possible score
        
    Returns:
        str: Personalized recommendations
    """
    # Get the LLM connector
    llm_connector = get_llm_connector()
    
    try:
        prompt = f"""
        Tu es un expert en troubles d'apprentissage, spécialisé dans la dyslexie. Un enfant vient de passer un test de dépistage de la dyslexie avec les résultats suivants:
        
        {test_summary}
        
        Score total: {total_score}/{max_score}
        
        Génère des recommandations personnalisées pour aider cet enfant à améliorer ses compétences en lecture. Inclus:
        1. Une évaluation du risque de dyslexie (faible, modéré, élevé)
        2. Des activités spécifiques pour renforcer la conscience phonologique
        3. Des conseils pour les parents et enseignants
        4. Des stratégies de lecture et d'apprentissage adaptées
        
        Formaté en HTML simple avec des titres, paragraphes et listes.
        """
        
        # System prompt for the model
        system_prompt = "Tu es un pédagogue spécialisé dans l'évaluation des enfants ayant des troubles de lecture. Tu donnes des analyses bienveillantes, positives et encourageantes."
        
        # Call the LLM model
        recommendations = llm_connector.generate_response(
            prompt=prompt,
            system_prompt=system_prompt,
            max_tokens=800,
            temperature=0.7
        )
        
        # Check that the response is not None or empty
        if recommendations is None or recommendations.strip() == "":
            logger.error("The LLM response is empty or None!")
            return "Je n'ai pas pu générer des recommandations. Veuillez réessayer plus tard."
        
        return recommendations
        
    except Exception as e:
        logger.error(f"Error generating dyslexie recommendations: {str(e)}")
        
        # Fallback recommendations if LLM fails
        risk_level = "élevé" if total_score / max_score < 0.3 else "modéré" if total_score / max_score < 0.7 else "faible"
        
        fallback = f"""
        <h3>Évaluation du risque de dyslexie: {risk_level}</h3>
        <p>Basé sur les résultats du test, voici quelques recommandations:</p>
        <ul>
            <li>Pratiquer régulièrement des exercices de conscience phonologique</li>
            <li>Utiliser des approches multisensorielles pour l'apprentissage de la lecture</li>
            <li>Lire à haute voix avec un adulte 10-15 minutes par jour</li>
            <li>Utiliser des outils visuels et des supports adaptés</li>
        </ul>
        <p>Si les difficultés persistent, une consultation avec un orthophoniste est recommandée.</p>
        """
        
        return fallback

def analyze_results_with_ai(test_type, responses):
    """
    Interface function to analyze test results with AI
    Used to handle various test types
    
    Args:
        test_type (str): Type of test (dyscalculie, tdah, dyslexie)
        responses (dict): Test responses
        
    Returns:
        str: Analysis and recommendations
    """
    if test_type == "dyslexie":
        # Extract detailed results for dyslexia
        detailed_results = responses.get('dyslexie_detailed_results', {})
        
        # Create a summary of test results
        test_summary = ""
        for test_key, test_data in detailed_results.items():
            test_name = {
                "denomination_rapide": "Dénomination Rapide",
                "pseudo_mots": "Décodage Pseudo-Mots",
                "suppression_phonemique": "Suppression Phonémique",
                "fluidite_lecture": "Fluidité de Lecture",
                "memoire_sons": "Mémoire des Sons",
                "confusion_lettres": "Confusion de Lettres"
            }.get(test_key, test_key)
            
            test_summary += f"{test_name}: {test_data.get('score', 0)}/{test_data.get('max', 0)}\n"
            if test_data.get('notes'):
                test_summary += f"  Notes: {test_data.get('notes')}\n"
        
        # Calculate total score
        total_score = sum(test_data.get("score", 0) for test_data in detailed_results.values())
        max_score = sum(test_data.get("max", 0) for test_data in detailed_results.values())
        
        # Generate recommendations
        return generate_dyslexie_recommendations(test_summary, total_score, max_score)
    
    # Add other test types (already implemented elsewhere)
    return None