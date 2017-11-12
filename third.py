from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import numpy as np
import pickle
import generateSpace as gs

batch_size = 128
num_classes = 10
epochs = 2

# the data, shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)



def mlp(space):
    print(space)
    model = Sequential()
    model.add(Dense(512, activation=space['activation'], input_shape=(784,)))
    model.add(Dropout(space['dropout']))
    # model.add(Dense(512, activation='relu'))
    # model.add(Dropout(space['dropout']))
    model.add(Dense(num_classes, activation='softmax'))

    model.summary()
    model.compile(loss='categorical_crossentropy',
                  optimizer=RMSprop(),
                  metrics=['accuracy'])

    history = model.fit(x_train, y_train,
                        batch_size=batch_size,
                        epochs=epochs,
                        verbose=1,
                        validation_data=(x_test, y_test))
    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])
    return {'loss': score[0], 'status': STATUS_OK, 'model':model}
    #return score[0]

# Define an objective function to minimize
# The classifier will be created, trained, and scored within this function
#def objective(space):
    
    # Build a classifier based on the parameters chosen
    #model = mlp(activation=space['activation'])
    #print(model)
    #print(type(model))

    #print('Loss value : ', model.score)
    #model.summary()
    #return {'loss': model.score, 'status': STATUS_OK, 'model':'mlp'}

    #how to return model





# Define the parameter space to search over
# In this case the objective function is expecting a single dictionary argument, 
# so the space variable is set up to match that
# space = {
#          'activation': hp.choice('activation', ['tanh', 'relu']),
#          'dropout': hp.uniform('dropout', low=0.001, high=1)
#          #'learning_rate':hp.uniform('learning_rate', low=0.001, high=0.999),
#         }


space = {}

space = gs.genSpace()
print (' printing space from model: ', space)
#evaluations = gs.evaluations
# space['activation'] = hp.choice('activation', ['tanh', 'relu'])
# space['dropout'] = hp.uniform('dropout', low=0.001, high=1)





# Create a Trials object to store results of each evaluation
trials = Trials()

# Run the search for the specified number of evaluations
best = fmin(mlp,
            space=space,
            algo=tpe.suggest,
            trials=trials,
            max_evals=2)

# Get the trained model from the best trial
pickle.dump(trials, open("results.pkl", "wb"))
print (best)
# best_model = trials.best_trial['result']['model']

# # Compute the training and testing scores on this model
# print("Training Accuracy: %f" % best_model.score(X_train, y_train))
# print("Testing Accuracy: %f" % best_model.score(X_test, y_test))