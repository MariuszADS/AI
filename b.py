# Importowanie niezbędnych bibliotek
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from tensorflow.keras import optimizers

# Dane treningowe
x_train = np.array([1, 2, 3, 4, 5], dtype=float)
y_train = np.array([3, 5.2, 7.1, 8, 11], dtype=float)

# Tworzenie modelu
model = keras.Sequential([layers.Dense(units=1, input_shape=[1])])

# Kompilacja modelu
model.compile(optimizer=optimizers.SGD(learning_rate=0.01), loss='mean_squared_error')

# Trenowanie modelu
history = model.fit(x_train, y_train, epochs=500, verbose=0)

# Wyświetlenie parametrów modelu
weights, bias = model.layers[0].get_weights()
print("Wagi:", weights)
print("Obciążenie (bias):", bias)

# Testowanie modelu na nowych danych
x_test = np.array([1, 2, 3, 4, 5], dtype=float)
predictions = model.predict(x_test)
print("Przewidywane wartości dla x_test:", predictions.flatten())

# Wykres danych treningowych i dopasowanej liniowej regresji
plt.figure(num='Wykres danych treningowych i dopasowanej liniowej regresji', figsize=(8, 6))
plt.scatter(x_train, y_train, color='blue', label='Dane treningowe')
plt.plot(x_test, predictions, color='red', label='Dopasowana linia regresji')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Liniowa regresja z jednym neuronem')
plt.legend()
plt.grid(True)
plt.show()

# Wykres szybkości uczenia się w kolejnych epokach
plt.figure(num='Wykres szybkości uczenia się w kolejnych epokach')
plt.plot(history.history['loss'])
plt.title('Szybkość uczenia się')
plt.xlabel('Epoka')
plt.ylabel('Strata (Loss)')
plt.grid(True)
plt.show()