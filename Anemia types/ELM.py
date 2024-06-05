import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from matplotlib import pyplot as plt
import random
from sklearn.metrics import confusion_matrix
import seaborn as sns
from PIL import Image
np.random.seed(42)
def load_and_preprocess_image(file_path, target_size=(28, 28)):
    image_array = np.array(Image.open(file_path).convert('L').resize(target_size))
    return image_array

class ELM:
    def __init__(self,input_length,num_hidden_nodes,num_output_nodes):
        self.beta = np.zeros((num_hidden_nodes, num_output_nodes))
        # self.beta = np.random.uniform(-1, 1, size=(num_hidden_nodes, num_output_nodes))
        self.w = np.random.uniform(-1, 1, size=(input_length, num_hidden_nodes))
        self.bias = np.random.uniform(-1, 1, size=(num_hidden_nodes))
    
        # print('Bias shape:', self.bias.shape)
        # print('W shape:', self.w.shape)
        # print('Beta shape:', self.beta.shape)

    def activation_sigmoid(self,x):
        return 1. / (1. + np.exp(-x))
        # return np.maximum(0, x)


    def fit(self, X, Y):
        H = self.activation_sigmoid(X.dot(self.w) + self.bias)
        H_pinv = np.linalg.pinv(H)
        self.beta = H_pinv.dot(Y)
    
    def pred(self, X):
        predicts = self.activation_sigmoid(X.dot(self.w) + self.bias)
        return np.argmax(predicts.dot(self.beta),axis=-1)

    def acc(self, predictss, Y):
        acc = np.sum(predictss == Y) / len(Y)
        return acc
    
    def cm(self, predicts, Y):
        conf = confusion_matrix(Y, predicts)
        plt.figure(figsize=(8, 6))
        sns.heatmap(conf, annot=True, fmt='d',cbar=False, linewidths=0.5, linecolor='black')
        plt.xlabel('Predykcja')
        plt.ylabel('Rzeczywistość')
        plt.title('Macierz pomyłek')
        plt.show()

    def cm_mod(self, predicts, Y, lower, upper):
        conf = confusion_matrix(Y, predicts)
        mask = np.logical_or(conf < lower, conf > upper)
        plt.figure(figsize=(8, 6))
        sns.heatmap(conf, annot=True, fmt='d',cbar=False, mask=mask, cmap='coolwarm', linewidths=0.5, linecolor='black')
        plt.xlabel('Predykcja')
        plt.ylabel('Rzeczywistość')
        plt.title('Macierz pomyłek')
        plt.show()
    
     
