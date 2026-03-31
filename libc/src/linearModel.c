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

unsigned char create_linear_model(uint32_t input_dim, Matrix** res_model) {
    /*
    Crée un modèle linéaire avec des poids et un biais initialisés aléatoirement.
    */
    // Allouer de la mémoire pour les poids et le biais et ajouter 1 pour le biais
    if (!res_model) return ERR_INVALID_PTR;
    
    LinearModel* model = (LinearModel*) malloc(sizeof(LinearModel));
    if (!model) return ERR_ALLOCATION_FAILED;
    model->weights = NULL;
    model->input_dim = input_dim;

    model->weights = (float*) malloc((input_dim + 1) * sizeof(float)); // +1 pour le biais
    if (!model->weights) {
        free_linear_model(&model);
        return ERR_ALLOCATION_FAILED;
    }

    // Initialisation pour les poids et le biais avec des valeurs aléatoires entre -1 et 1
    fill_randomly_float_array(-1.0f, 1.0f, model->weights, input_dim + 1);
    
    return RES_EXIT_SUCCESS;
}

unsigned char free_linear_model(LinearModel** model_ptr) {
    /*
    Libère la mémoire allouée pour le modèle linéaire.
    */
    if (!model_ptr || !(*model_ptr)) return ERR_INVALID_PTR;
    
    LinearModel* model = *model_ptr;
    if (model->weights) {
        free(model->weights);
    }

    free(model);

    *model_ptr = NULL;
    return RES_EXIT_SUCCESS;
}

 /** Fonction de prédiction **/
 /*
    # Implémenter 2 fonction de prédiction :
        - `predict_classification` : pour les tâches de classification, qui retourne la classe prédite (0 ou 1)
        - `predict_regression` : pour les tâches de régression, qui retourne la valeur
 */
 
// Fonction de prédiction pour la classification
 unsigned char predict_classification(double* model, double* input, int input_dim) {
    /*
    Prédit la classe pour une entrée donnée en utilisant le modèle linéaire (renvoie 0 ou 1).
    */
    // Commence avec le biais
    double sum = model[0];
    for (int i = 0; i < input_dim; i++) {
        sum += model[i + 1] * input[i];
    }

    return sum >= 0 ? 1 : 0;
 }

// Fonction de prédiction pour la regréssion
unsigned char predict_regression(double* model, double* input, int input_dim) {
    /*
    Prédit la classe pour une entrée donnée en utilisant le modèle linéaire (renvoie un double).
    */
    // Commence avec le biais
    double sum = model[0];
    for (int i = 0; i < input_dim; i++) {
        sum += model[i + 1] * input[i];
    }

    return sum;
 }

 /** Fonction d'entraînement **/
 /*
    # Implémenter deux fonctions d'entraînement :
        - `train_classification_rossenblatt` : pour entraîner le modèle sur un ensemble de données
            (Règle de Rosenblatt pour la classification)
        - `train_regressions_gradient_descent` : pour entraîner le modèle sur un ensemble de données
            (Descente de gradient pour la régression)
 */

// Règle de Rosenblatt (Perceptron Learning Algorithm) `https://fr.wikipedia.org/wiki/Perceptron` & `https://www.anyflo.com/bret/cours/rn/rn4.htm`
/*
    Entraîner un modèle de classification binaire supervisé.
    Note : L'initialisation des poids et du biais est déjà gérée par `create_linear_model`.

    Algorithme (à répéter pour chaque époque et chaque exemple du dataset) :
        - Prédire la sortie g(X) avec les poids et le biais actuels.
        - Calculer l'erreur : Erreur = Y_attendu - g(X).
        - Si l'erreur est différent de 0, on met à jour le modèle avec le pas d'apprentissage (alpha) en modifiant le biais ainsi que les poids :
            - Mise à jour des poids : W_i = W_i + (alpha * Erreur * X_i)
            - Mise à jour du biais  : b = b + (alpha * Erreur)
*/
unsigned char void train_classification(double* models, double* dataset_inputs, double* dataset_expected_outputs, int input_dim, int dataset_size, int alpha, int epochs) {
    // On boucle sur le nombre d'époques
    for (int i = 0; i < epochs; i++) {
        // On boucle sur le nombre d'exemple dans le dataset
        for (int j = 0; j < dataset_size; j++) {
            // FORCE
            // Recupere genre le resultats de la prédiction : g = predict_classification(model, x --> recupere dans le dataset inputs(avec le stride jsp CEST APPLATI MON CERVEAU), input_dim)
            // Cacluler l'erreur : double error = expect - predict
            // Mise à jour des poids seulement si error est différent de 0
            if (error != 0.) {
                // Mise à jour du biais
                model[0] += alpha * error;

                // Mise à jour des poids
                for (int k = 0; k < input_dim; k++) {
                    model[k + 1] += alpha * error * X[k]; // jsp
                }
            }
        }
    }
}
