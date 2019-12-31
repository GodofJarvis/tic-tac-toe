import xo_game_data as xo_data
import pandas as pd
import numpy as np
import tensorflow.keras.utils as k_utils
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

class XO_Game():
    def __init__(self):
        values, labels = xo_data.get_training_data()
        self.x_train = np.asarray(values, dtype='float32')
        self.y_train = k_utils.to_categorical(np.asarray(labels, dtype='float32'))
        print (self.x_train.shape)
        print (self.y_train.shape)
        self.model = Sequential()

    def design_model(self):
        num_box = 9
        self.model.add(Dense(32, input_dim=num_box, kernel_initializer='normal', activation='relu'))
        self.model.add(Dense(num_box, kernel_initializer='normal', activation='softmax'))

        self.model.compile(
            loss = 'categorical_crossentropy',
            optimizer = 'adam',
            metrics = ['accuracy']
        )

    def train(self):
        self.model.fit(
            self.x_train,
            self.y_train,
            epochs = 100,
        )

    def predict(self):
        res = self.model.predict(self.x_train)
        print(res)

def main():
    xo_game = XO_Game()
    xo_game.design_model()
    xo_game.train()
    xo_game.predict()

if __name__ == '__main__':
    main()
