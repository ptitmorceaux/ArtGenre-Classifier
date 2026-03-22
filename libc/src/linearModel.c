#include "../include/linearModel.h"

/**  Structure for a linear model **/
/*
    # Mettre en place l'équation `y = W X + b` : 
        - W : poids du modèle
        - X : features d'entrée
        - b : biais du modèle

    # Implémenter dans un tableau les poids et les biais du modèle, 
        Ainsi que les features d'entrée ou la première case du tableau sera le biais
        -> (w(0) = b) et les cases suivantes seront les poids (w(i) = W(i-1)).
*/

EXPORT double* create_linear_model(int input_dim) {
    """
    Crée un modèle linéaire avec des poids et un biais initialisés aléatoirement.
    """
    // Allouer de la mémoire pour les poids et le biais et ajouter 1 pour le biais
    double *model = (double*)malloc((input_dim + 1) * sizeof(double));

    // Initialisation de l'aléatoire pour les poids et le biais
    srand(time(NULL));


    // INitialiser les poids et le biais avec des valeurs aléatoires entre -1 et 1
    for (int i = 0; i < input_dim + 1; i++) {
        model[i] = ((double)rand() / RAND_MAX) * 2 - 1;
    }

    return model;
}

EXPORT void free_linear_model(double* model) {
    """
    Libère la mémoire allouée pour le modèle linéaire.
    """
    free(model);
}

 /** Fonction de prédiction **/
 /*
    # Implémenter 2 fonction de prédiction :
        - `predict_classification` : pour les tâches de classification, qui retourne la classe prédite (0 ou 1)
        - `predict_regression` : pour les tâches de régression, qui retourne la valeur
 */

 EXPORT double predict_classification(double* model, double* input, int input_dim) {
    """
    Prédit la classe pour une entrée donnée en utilisant le modèle linéaire (renvoie 0 ou 1).
    """
    // Commence avec le biais
    double sum = model[0];
    for (int i = 0; i < input_dim; i++) {
        sum += model[i + 1] * input[i];
    }

    return sum >= 0 ? 1 : 0;
 }

 /** Fonction d'entraînement **/
 /*
    # Implémenter une fonction d'entraînement :
        - `train_linear_model` : pour entraîner le modèle sur un ensemble de données
            (Règle de Rosenblatt pour la classification ou descente de gradient pour la régression)
 */