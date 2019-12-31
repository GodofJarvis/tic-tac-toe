'''
Empty - 0.5
X - 1
O - 0

Matrix: x_value

1 2 3
- - -
4 5 6
- - -
7 8 9
- - -

Matrix: y_value will start with 0 instead of 1 and end with 8
'''

import numpy as np

def get_reshaped_data(values):
    # Reshape to a 2D array
    a = np.array(values)
    cols = 3
    b = np.reshape(a, (-1, cols))
    return b

def get_training_data():
#    train_values_x = []
#    train_values_y = []
    train_values_x = [
        [0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5],
        [1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1],
        [0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5],
        [1, 0.5, 0.5, 0.5, 0, 0.5, 1, 0.5, 0.5],
        [1, 0.5, 1, 0.5, 0, 0.5, 0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5, 0.5, 0, 1, 0.5, 0.5, 1],
        [0.5, 0.5, 0.5, 1, 0, 0.5, 1, 0.5, 0.5] ]
    train_values_y = [0, 8, 4, 4, 4, 4, 3, 1, 2, 0]
    #train_values_y = [1, 9, 5, 5, 5, 5, 4, 2, 3, 1]
    return train_values_x, train_values_y

'''    values_y = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
'''

#    for x in values_x:
#        train_values_x.append(x)
#    for y in values_y:
#        train_values_y.append(y)
