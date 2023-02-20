from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

myData = loadtxt("Kuala_Lumpur_house_prices_clean.csv", delimiter=",", usecols=(1, 2, 3, 4, 5, 6))

x = myData[:, 0:6]
y = myData[:, 6]

# neural network using Sequential model
model = Sequential()

model.add(Dense(4, input_dim=6, activation="relu"))
model.add(Dense(2, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x, y, epochs=100, batch_size=myData.shape[0])

