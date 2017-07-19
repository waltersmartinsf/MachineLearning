'''
This is an example to how to work with Keras package. 
You can find more in https://keras.io/#you-have-just-found-keras
'''

from keras.models import Sequential #a linear stack of layers
from keras.layers import Dense, Activation #Stacking layer

model = Sequential()

model.add(Dense(units=64, input_dim=100))
model.add(Activation('relu'))
model.add(Dense(units=10))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])