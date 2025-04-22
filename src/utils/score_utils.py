def check_answers_and_provide_solutions(test_type, responses):
    """
    Check answers and provide solutions if needed
    Returns (correct_answers, total_questions, solutions)
    """
    correct_answers = 0
    total_questions = 0
    solutions = ""
    
    if test_type == "dyscalculie":
        # Définir les réponses correctes
        correct_values = {
            "q1": 8,
            "q2": 6,
            "q3": "10",
            "q4": "Une voiture"
        }
        
        # Vérifier chaque réponse
        for q, correct_val in correct_values.items():
            if q in responses:
                total_questions += 1
                if str(responses[q]) == str(correct_val):
                    correct_answers += 1
        
        # Si plus de 50% des réponses sont incorrectes, proposer des solutions
        if correct_answers < total_questions / 2:
            solutions = """
            ## Solutions et explications:
            
            1. **5 + 3 = 8** : Pour additionner, on compte tous les objets ensemble. 5 objets + 3 objets = 8 objets au total.
            
            2. **10 - 4 = 6** : Pour soustraire, on retire des objets du total. Si on a 10 objets et qu'on en retire 4, il reste 6 objets.
            
            3. **Suite logique 2, 4, 6, 8, ... = 10** : Dans cette suite, chaque nombre augmente de 2. Donc après 8, on ajoute 2 pour obtenir 10.
            
            4. **L'objet le plus lourd est "Une voiture"** : Parmi les options, la voiture est beaucoup plus lourde qu'une plume, une pomme ou un livre.
            
            ### Conseils pour s'améliorer:
            - Pratique les additions et soustractions avec des objets réels (comme des jouets ou des fruits)
            - Cherche des motifs dans les nombres autour de toi (comme les numéros de maisons)
            - Compare le poids des objets dans ta maison pour comprendre les différences
            """
    
    elif test_type == "tdah":
        # Si les résultats détaillés sont disponibles
        if 'detailed_results' in responses:
            detailed_results = responses['detailed_results']
            
            # Calculer le score total
            total_score = sum([detailed_results[key]["score"] for key in detailed_results])
            max_score = sum([detailed_results[key]["max"] for key in detailed_results])
            
            correct_answers = total_score
            total_questions = max_score
            
            # Si l'élève a un score faible, proposer des solutions
            if total_score < max_score / 2:
                solutions = """
                ## Conseils pour améliorer l'attention et la concentration:
                
                ### 1. Pour la mémorisation:
                - Créer des images mentales pour mieux retenir l'information
                - Répéter l'information à voix haute ou la reformuler dans tes propres mots
                - Utiliser des moyens mnémotechniques (comme des rimes ou des associations)
                
                ### 2. Pour l'attention soutenue:
                - Travailler dans un environnement calme avec peu de distractions
                - Diviser les grandes tâches en petites étapes de 10-15 minutes
                - Prendre des pauses courtes mais régulières (2-3 minutes toutes les 20 minutes)
                
                ### 3. Pour l'organisation:
                - Utiliser des listes de tâches ou des plannings visuels colorés
                - Préparer tout le matériel nécessaire avant de commencer une activité
                - Ranger son espace de travail pour éviter les distractions
                
                ### 4. Pour la flexibilité cognitive:
                - S'entraîner à changer de règles dans les jeux (comme "Jacques a dit")
                - Essayer de résoudre des problèmes de différentes façons
                - Pratiquer la technique du "Et si..." (imaginer d'autres possibilités)
                """
        else:
            # Définir les réponses correctes pour le test simple
            correct_values = {
                "q1": "bleu",
                "q2": "30 minutes",
                "q3": "chocolat"
            }
            
            # Vérifier chaque réponse
            for q, correct_val in correct_values.items():
                if q in responses:
                    total_questions += 1
                    if responses[q].lower() == correct_val.lower():
                        correct_answers += 1
            
            # Si plus de 50% des réponses sont incorrectes, proposer des solutions
            if correct_answers < total_questions / 2:
                solutions = """
                ## Solutions et explications:
                
                1. **La couleur du t-shirt de Pierre était bleue** : Dans l'histoire, il est mentionné que "Pierre portait un t-shirt bleu".
                
                2. **Ils ont joué au ballon pendant 30 minutes** : L'histoire précise qu'ils "ont joué au ballon pendant 30 minutes".
                
                3. **Marie a choisi une glace au chocolat** : À la fin de l'histoire, il est dit que "Marie une glace au chocolat".
                
                ### Conseils pour améliorer l'attention:
                - Lis l'histoire à voix haute pour mieux la comprendre
                - Essaie de visualiser l'histoire comme un film dans ta tête
                - Prends des notes ou dessine les éléments importants pendant ta lecture
                - Relis l'histoire une deuxième fois en te concentrant sur les détails
                """
    
    return correct_answers, total_questions, solutions