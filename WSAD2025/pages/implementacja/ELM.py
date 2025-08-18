from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import tensorflow as tf
import os
import random
import numpy as np

class ELM:
    #################################################################################
    # inicjacja modelu, podajemy ilosc atrybutow wejsciowych, ilosc neuronow w warstwie ukrytej, liczbe neuronow wyjsciowych, lambda (wspolczynnik
    # regularyzacji przy obliczaniu pinva (mam wrazenie ze srednio dziala ale idk)), na koniec funkcje aktaywacji, domyslnie leaky_relu
    #################################################################################
    def __init__(self, input_length, num_hidden_nodes, num_output_nodes, lambda_ = 1e-2, activation='leaky_relu'):
        self.lambda_ = lambda_
        self.num_hidden_nodes = num_hidden_nodes
        self.beta = np.zeros((num_hidden_nodes, num_output_nodes))
        self.w = np.random.randn(input_length, num_hidden_nodes)
        self.bias = np.random.randn(num_hidden_nodes)
        self.activation_name = activation
    #################################################################################
    # funkcje aktywacji, mozna pokusic sie o troche inne zaprogramowanie tego, ale 
    # na ten moment zostaje tak jak jest
    #################################################################################
    def activation(self, x):
        if self.activation_name == 'relu':
            return np.maximum(0, x)
        elif self.activation_name == 'leaky_relu':
            return np.where(x > 0, x, 0.05 * x)
        elif self.activation_name == 'tanh':
            return np.tanh(x)
        elif self.activation_name == 'sigmoid':
            return 1.0 / (1.0 + np.exp(-x))
        elif self.activation_name == 'elu':
            return np.where(x > 0, x, np.exp(x) - 1)
        else:
            raise ValueError(f"Unsupported activation function: {self.activation_name}")

    #################################################################################
    # dopasowanie modelu do danych, czyli stworzenie macierzy H neuronow ukrytych,
    # a nastepnie obliczneie macierzy pseudoodwrotnej i wyliczeine wag beta
    #################################################################################
    def fit(self, X, Y):
        # lambda_ = 1e-1  # mały współczynnik regularyzacji
        H = self.activation(X.dot(self.w) + self.bias)
        H_pinv = np.linalg.pinv(H.T.dot(H) + self.lambda_ * np.eye(H.shape[1])).dot(H.T)
        self.beta = np.dot(H_pinv, Y)

    #################################################################################
    # obliczanie predykcji, w wersji ciaglej, trzeba o tym pamietac przy klasyfikacji
    #################################################################################

    
    def pred(self, X):
        H = self.activation(X.dot(self.w) + self.bias)
        predicts = H.dot(self.beta)
        return predicts
    
    #################################################################################
    # metryki modelu, aktualnie tylko dla klasyfikacji binarnej
    #################################################################################
    
    def evaluate(self, predictions, Y):
        predictions_binary = (predictions > 0.5).astype(int)
        accuracy = accuracy_score(Y, predictions_binary)
        f1 = f1_score(Y, predictions_binary)
        precision = precision_score(Y, predictions_binary)
        recall = recall_score(Y, predictions_binary)
        return accuracy, f1, precision, recall

    #################################################################################
    # najzwyklejsze w swiecie MSE
    #################################################################################

    def mse(self, predictions, Y):
        mse_value = mean_squared_error(Y, predictions)
        return mse_value