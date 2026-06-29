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

// Structure pour un modèle linéaire
unsigned char create_linear_model(uint32_t input_dim, LinearModel** res_model) {
    if (!res_model || *res_model) return ERR_INVALID_PTR;
    
    LinearModel* model = (LinearModel*) malloc(sizeof(LinearModel));
    if (!model) return ERR_MEMORY_ALLOCATION;
    
    // Allouer de la mémoire pour les poids + le biais
    model->length = input_dim + 1; // + 1 pour le biais
    model->weights = (float*) malloc((model->length) * sizeof(float));
    if (!model->weights) {
        free_linear_model(res_model);
        return ERR_MEMORY_ALLOCATION;
    }
    
    *res_model = model;
    return RES_EXIT_SUCCESS;
}

// Initialise un modèle linéaire avec des poids et un biais initialisés aléatoirement.
unsigned char create_linear_model_randomly(uint32_t input_dim, LinearModel** res_model) {
    if (!res_model || *res_model) return ERR_INVALID_PTR;
    unsigned char status = RES_EXIT_SUCCESS;
    
    status = create_linear_model(input_dim, res_model);
    if (status != RES_EXIT_SUCCESS) return status;
    LinearModel* model = *res_model;

    // Initialisation pour les poids et le biais avec des valeurs aléatoires entre -1 et 1
    status = fill_randomly_float_array(-1.0f, 1.0f, &(model->weights), model->length);
    if (status != RES_EXIT_SUCCESS) {
        free_linear_model(res_model);
        return status;
    }
        
    return RES_EXIT_SUCCESS;
}

// Crée un modèle linéaire avec des poids et un biais initialisés à partir de données fournies.
unsigned char create_linear_model_from_init_weights(float* weights, uint32_t input_dim, float bias, LinearModel** res_model) {
    if (!res_model || *res_model) return ERR_INVALID_PTR;
    unsigned char status = RES_EXIT_SUCCESS;
    
    status = create_linear_model(input_dim, res_model);
    if (status != RES_EXIT_SUCCESS) return status;
    LinearModel* model = *res_model;

    // Initialisation pour les poids et le biais avec les valeurs fournies
    model->weights[0] = bias;
    for (uint32_t i = 0; i < input_dim; i++) {
        model->weights[i + 1] = weights[i];
    }
    
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
        - `predict_linear_classification` : pour les tâches de classification, qui retourne la classe prédite (-1 ou 1)
        - `predict_linear_regression` : pour les tâches de régression, qui retourne la valeur
 */
// Fonction de prédiction pour la regréssion
unsigned char predict_linear_regression(LinearModel* model, float* input, float* result) {
    /*
    Prédit la classe pour une entrée donnée en utilisant le modèle linéaire (renvoie un double).
    */
    if (!model || !model->weights) return ERR_INVALID_PTR;
    
    // Commence avec le biais
    float sum = model->weights[0];
    
    for (uint32_t i = 1; i < model->length; i++) {
        sum += model->weights[i] * input[i - 1];
    }

    *result = sum;
    return RES_EXIT_SUCCESS;
 }


// Fonction de prédiction pour la classification
unsigned char predict_linear_classification(LinearModel* model, float* input, int32_t* result) {
    /*
    Prédit la classe pour une entrée donnée en utilisant le modèle linéaire (renvoie -1 ou 1).
    */
    if (!model || !model->weights) return ERR_INVALID_PTR;

    float sum = 0.0f;
    unsigned char status = RES_EXIT_SUCCESS; 
    
    status = predict_linear_regression(model, input, &sum);
    if (status != RES_EXIT_SUCCESS) return status;
    
    *result = sum >= 0 ? 1 : -1;
    return RES_EXIT_SUCCESS;
 }


 /** Fonction d'entraînement **/
 /*
    # Implémenter deux fonctions d'entraînement :
        - `train_linear_classification_rossenblatt` : pour entraîner le modèle sur un ensemble de données
            (Règle de Rosenblatt pour la classification)
        - `train_linear_regressions_gradient_descent` : pour entraîner le modèle sur un ensemble de données
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
            - Mise à jour du biais  : b = b + (alpha * Erreur * 1) (car le biais on le multiplie par 1)
*/
unsigned char train_linear_classification(LinearModel* model, float* dataset_inputs,
        float* dataset_expected_outputs, uint32_t dataset_size, float alpha, uint32_t epochs) {   
    if (!model || !model->weights) return ERR_INVALID_PTR;
    /*
     * Début de l'entraînement par la règle de Rosenblatt.
     * L'algorithme va parcourir toutes les images du dataset plusieurs fois (epochs).
     * Pour chaque image, il effectue une prédiction. S'il se trompe (erreur != 0), 
     * il ajuste immédiatement son biais et ses poids en fonction du pas d'apprentissage (alpha)
     * pour s'améliorer lors du prochain passage.
    */

    uint32_t input_dim = model->length - 1;
    // On boucle sur le nombre d'époques
    for (uint32_t i = 0; i < epochs; i++) {
        // On boucle sur le nombre d'exemple dans le dataset
        for (uint32_t j = 0; j < dataset_size; j++) {
            /* 
                ========================================================================================================================================
                # TODO
                    // Recupere genre le resultats de la prédiction : g = predict_linear_classification(model, x --> recupere dans le dataset inputs     --> OK
                    // input_dim)
                    // Cacluler l'erreur : float error = expect - predict                                                                         --> OK
                    // Mise à jour des poids seulement si error est différent de 0                                                                --> OK
                ========================================================================================================================================
            */
            // On va récupere l'adresse mémoire de chaque image (cela revient à chercher le premier pixel de notre image)
            float* image = &(dataset_inputs[j * input_dim]);

            // Recupere le résulat de la prédiction
            int32_t g = 0;
            unsigned char status = predict_linear_classification(model, image, &g);
            if (status != RES_EXIT_SUCCESS) {
                free_linear_model(&model);
                return status;
            }

            // Calcul de l'erreur
            float Y_expected = dataset_expected_outputs[j];
            float error = Y_expected - g;
            
            if (error != 0) {
                // Mise à jour du biais
                model->weights[0] += alpha * error;

                // Mise à jour des poids
                for (uint32_t k = 0; k < input_dim; k++) {
                    model->weights[k + 1] += alpha * error * image[k];
                }
            }
        }
    }
    return RES_EXIT_SUCCESS;
}

// Descente de Gradient Stochastique (SGD) `https://fr.wikipedia.org/wiki/Algorithme_du_gradient_stochastique` & `https://www.ibm.com/fr-fr/think/topics/stochastic-gradient-descent`
/*
    Entraîner un modèle de régression (valeurs continues) via la descente de gradient stochastique.
    Note : L'initialisation des poids et du biais est déjà gérée par `create_linear_model`.

    Algorithme (à répéter pour chaque époque et chaque exemple du dataset) :
        - Prédire la sortie continue g(X) avec les poids et le biais actuels.
        - Calculer l'erreur : Erreur = Y_attendu - g(X).
        - Ajuster continuellement le modèle avec le pas d'apprentissage (alpha) pour réduire cette erreur :
            - Mise à jour des poids : W_i = W_i + (alpha * Erreur * X_i)
            - Mise à jour du biais  : b = b + (alpha * Erreur * 1) (car le biais on le multiplie par 1)
*/
unsigned char train_linear_regression(LinearModel* model, float* dataset_inputs,
        float* dataset_expected_outputs, uint32_t dataset_size, float alpha, uint32_t epochs) {
    if (!model || !model->weights) return ERR_INVALID_PTR;
    /*
     * Début de l'entraînement par descente de gradient stochastique.
    * Contrairement à la classification (-1 ou 1), ici on prédit une valeur continue (ex: 6.7).
     * L'algorithme calcule l'écart (la distance) entre la prédiction et la vraie valeur.
     * Il va ensuite utiliser cet écart pour ajuster proportionnellement le biais et les poids.
     * Plus l'erreur est grande, plus le pas de correction sera grand. Plus on se rapproche de la valeur, plus le pas de correction sera petit.
    */
    
    uint32_t input_dim = model->length - 1;
    // On boucle sur le nombre d'époques
    for (uint32_t i = 0; i < epochs; i++) {
        // On boucle sur le nombre d'exemple dans le dataset
        for (uint32_t j = 0; j < dataset_size; j++) {
            // On va récupere l'adresse mémoire de chaque image (cela revient à chercher le premier pixel de notre image)
            float* image = &dataset_inputs[j * input_dim];

            // Recupere le résulat de la prédiction
            float g = 0.0f;
            unsigned char status = predict_linear_regression(model, image, &g);
            if (status != RES_EXIT_SUCCESS) {
                free_linear_model(&model);
                return status;
            }

            // Calcul de l'erreur
            float Y_expected = dataset_expected_outputs[j];
            float error = Y_expected - g;
   
            // Mise à jour du biais
            model->weights[0] += alpha * error;

            // Mise à jour des poids
            for (uint32_t k = 0; k < input_dim; k++) {
                model->weights[k + 1] += alpha * error * image[k];
            }
        }
    }
    return RES_EXIT_SUCCESS;
}


////////////////////////////////////////////////////////////////////////////////////

/*
    Grace aux strides on ne charge en RAM qu'une seule fois le dataset, on ne fait pas de copie

    [X (m, n)]  -->  [X+ (n, m)]

    m=rows et n=columns
  
    Cas  ///  Pseudo-inverse :
    - m >= n  ///  X+ = (X^T * X)^-1 * X^T
    - m < n   ///  X+ = X^T * (X * X^T)^-1
*/
unsigned char pseudo_inverse_2d_matrix(Matrix* X, Matrix** res) {
    if (!X || !X->data || !res || *res != NULL) return ERR_INVALID_PTR;

    unsigned char status = RES_EXIT_SUCCESS;

    status = allocate_2d_matrix_float32(X->columns, X->rows, res);
    if (status != RES_EXIT_SUCCESS) return status;

    Matrix X_transpose = {
        .data = X->data,
        .rows = X->columns,
        .columns = X->rows,
        .row_stride = X->col_stride,
        .col_stride = X->row_stride
    };

    /////////////////////////////////////////

    Matrix* tmp = NULL;
    if (X->rows >= X->columns)
        // m >= n  ///  allouer pour X^T * X
        status = allocate_2d_matrix_float32(X->columns, X->columns, &tmp);
    else
        // m < n   ///  allouer pour X * X^T
        status = allocate_2d_matrix_float32(X->rows, X->rows, &tmp);
    
    if (status != RES_EXIT_SUCCESS) {
        free_matrix(res);
        return status;
    }

    /////////////////////////////////////////

    if (X->rows >= X->columns)
        // m >= n  ///  X^T * X
        status = multiply_2d_matrix(&X_transpose, X, &tmp);

    else
        // m < n   ///  X * X^T
        status = multiply_2d_matrix(X, &X_transpose, &tmp);
    
    if (status != RES_EXIT_SUCCESS) {
        free_matrix(&tmp);
        free_matrix(res);
        return status;
    }

    /////////////////////////////////////////

    // inverser la matrice tmp (X^T * X)^-1 ou (X * X^T)^-1
    status = inverse_2d_matrix(tmp);
    if (status != RES_EXIT_SUCCESS) {
        free_matrix(&tmp);
        free_matrix(res);
        return status;
    }

    /////////////////////////////////////////

    if (X->rows >= X->columns)
        // m >= n  ///  ((X^T * X)^-1) * (X^T)
        status = multiply_2d_matrix(tmp, &X_transpose, res);
    else
        // m < n   ///  (X^T) * ((X * X^T)^-1)
        status = multiply_2d_matrix(&X_transpose, tmp, res);

    if (status != RES_EXIT_SUCCESS) {
        free_matrix(&tmp);
        free_matrix(res);
        return status;
    }
    
    /////////////////////////////////////////

    free_matrix(&tmp);
    return status;
}


/*
    Utilisation de la pseudo inverse pour calculer W en un coup

    IMPORTANT :
    - Le dataset d'entrée doit déjà contenir la colonne du biais (1.0f) dans la première colonne -> input_with_bias (m, n)
    - La matrice expected_outputs doit être de dimension (m, 1)

    En sortie : W -> (n, 1)
    En sortie -> LinearModel* (il faut penser à free_linear_model() après utilisation)
*/
unsigned char get_linear_regression_weights(Matrix* dataset_inputs_with_bias, Matrix* dataset_expected_outputs, LinearModel** res_model) {
    
    if (!res_model || *res_model != NULL) return ERR_INVALID_PTR;

    if (!dataset_inputs_with_bias || !dataset_inputs_with_bias->data ||
        !dataset_expected_outputs || !dataset_expected_outputs->data
    ) return ERR_INVALID_PTR;
    
    if (dataset_inputs_with_bias->rows == 0 || dataset_inputs_with_bias->columns == 0 ||
        dataset_expected_outputs->rows == 0 || dataset_expected_outputs->columns == 0
    ) return ERR_INVALID_MATRIX_DIMENSIONS;

    unsigned char status = RES_EXIT_SUCCESS;

    Matrix* pseudo_inverse = NULL;
    status = pseudo_inverse_2d_matrix(dataset_inputs_with_bias, &pseudo_inverse);
    if (status != RES_EXIT_SUCCESS) return status;

    LinearModel* weights = NULL;
    status = create_linear_model(pseudo_inverse->rows - 1, &weights);
    if (status != RES_EXIT_SUCCESS) {
        free_matrix(&pseudo_inverse);
        return status;
    }

    Matrix W = {
        .data = weights->weights,
        .rows = weights->length,
        .columns = 1,
        .row_stride = 1,
        .col_stride = 1
    };

    // X+ * Y = W
    // (n, m) * (m, 1) = (n, 1)
    status = multiply_2d_matrix(pseudo_inverse, dataset_expected_outputs, &W);
    if (status != RES_EXIT_SUCCESS) {
        free_matrix(&pseudo_inverse);
        free_linear_model(&weights);
        return status;
    }

    free_matrix(&pseudo_inverse);
    *res_model = weights;
    return status;
}