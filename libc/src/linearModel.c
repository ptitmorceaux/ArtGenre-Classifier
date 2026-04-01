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

unsigned char create_linear_model(uint32_t input_dim, LinearModel** res_model) {
    /*
    Crée un modèle linéaire avec des poids et un biais initialisés aléatoirement.
    */
    // Allouer de la mémoire pour les poids et le biais et ajouter 1 pour le biais
    if (!res_model) return ERR_INVALID_PTR;
    unsigned char status = RES_EXIT_SUCCESS;
    
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
    status = fill_randomly_float_array(-1.0f, 1.0f, &(model->weights), input_dim + 1);

    if (status != RES_EXIT_SUCCESS) {
        free_linear_model(&model);
        return status;
    }
    
    *res_model = model
        
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
// Fonction de prédiction pour la regréssion
unsigned char predict_regression(LinearModel* model, float* input, float* result) {
    /*
    Prédit la classe pour une entrée donnée en utilisant le modèle linéaire (renvoie un double).
    */
    if (!model || !(*model) return ERR_INVALID_PTR;
    // Commence avec le biais
    float sum = model[0];
    for (int i = 0; i < input_dim; i++) {
        sum += model[i + 1] * input[i];
    }

    *result = sum;
    return RES_EXIT_SUCCESS;
 }


// Fonction de prédiction pour la classification
 unsigned char predict_classification(LinearModel* model, float* input, float* result) {
    /*
    Prédit la classe pour une entrée donnée en utilisant le modèle linéaire (renvoie 0 ou 1).
    */
    if (!model || !(*model) return ERR_INVALID_PTR;

    float sum = 0.0f;
    unsigned char status = RES_EXIT_SUCCESS; 
    
    status = predict_regression(mode, input, &sum);
     
    *result = sum >= 0.0f ? 1 : 0.0f;
    return RES_EXIT_SUCCESS;
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
            - Mise à jour du biais  : b = b + (alpha * Erreur * 1 --> pour Milhane) (car le biais on le multiplie par 1) --> Toujours pour Milhane
*/
unsigned char train_classification(LinearModel* models, float* dataset_inputs,
        float* dataset_expected_outputs, uint32_t input_dim, uint32_t dataset_size, float alpha, uint32_t epochs) {   
    if (!model || !(*model) return ERR_INVALID_PTR;
    // On boucle sur le nombre d'époques
    for (uint32_t i = 0; i < epochs; i++) {
        // On boucle sur le nombre d'exemple dans le dataset
        for (uint32_t j = 0; j < dataset_size; j++) {
            /* 
                ========================================================================================================================================
                # TODO
                    // Recupere genre le resultats de la prédiction : g = predict_classification(model, x --> recupere dans le dataset inputs     --> OK
                    // input_dim)
                    // Cacluler l'erreur : float error = expect - predict                                                                         --> OK
                    // Mise à jour des poids seulement si error est différent de 0                                                                --> OK
                ========================================================================================================================================
            */
            // On va récupere l'adresse mémoire de chaque image (cela revient à chercher le premier pixel de notre image)
            float* image = &dataset_inputs[j * input_dim];

            // Recupere le résulat de la prédiction
            float g = 0.0f;
            unsigned char status = predict_classification(model, image, &g);
            if (status != RES_EXIT_SUCCESS) return status;

            // Calcul de l'erreur
            float Y_expected = dataset_expected_outputs[j];
            float error = Y_expected - g;
            
            if (error != 0.) {
                // Mise à jour du biais
                model[0] += alpha * error * 1.0f; // --> Pour Milhane 

                // Mise à jour des poids
                for (uint32_t k = 0; k < input_dim; k++) {
                    model[k + 1] += alpha * error * X[k];
                }
            }
        }
    }
    return RES_EXIT_SUCCESS;
}
