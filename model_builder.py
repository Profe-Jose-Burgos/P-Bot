# importe de librerías
import json
import pickle
import numpy as np

import nltk
from nltk.stem import SnowballStemmer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import SGD

# reducción a su raíz de las palabras en español que el usuario pueda introducir
stemmer = SnowballStemmer('spanish')

# caracteres que el chatbot debe ignorar en caso tal el usuario los introduzca.
palabras_a_ignorar = ["?", "¿", "!", "¡"]

# apertura del archivo json creado con anterioridad
pbot_data = open("intents.json").read()
intents = json.loads(pbot_data)


# desglosar el texto dado en la unidad más pequeña de una oración.
def tokenizador():
    palabras = []
    clases = []
    documentos = []

    for intent in intents["intents"]:  # acceder a la lista de diccionarios
        for pattern in intent["patterns"]:  # acceder a la lista de palabras
            # tokenizar cada palabra
            w = nltk.word_tokenize(pattern)
            palabras.extend(w)
            # se añaden clases a la lista de clases
            documentos.append((w, intent["tag"]))

            if intent["tag"] not in clases:
                clases.append(intent["tag"])

    return palabras, clases, documentos


# proceso de encontrar la forma de la palabra relacionada
def lematizador(palabras, clases, documentos):  # base de datos
    palabras = [stemmer.stem(w.lower()) for w in palabras if w not in palabras_a_ignorar]
    palabras2 = palabras

    pickle.dump(palabras, open("palabras.pkl", "wb"))
    pickle.dump(clases, open("clases.pkl", "wb"))
    return palabras2


# procesamiento (información de entrenamiento)
def entrenamiento(palabras, clases, documentos):
    entrenamiento = []
    output_empty = [0] * len(clases)

    # creación de una matriz con el mismo número de columnas como clases
    for doc in documentos:
        bag = []
        pattern_words = doc[0]  # lista de tokens
        # lematizacion del token
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words if word not in palabras_a_ignorar]

        for palabra in palabras:
            bag.append(1) if palabra in pattern_words else bag.append(0)

        output_row = list(output_empty)
        output_row[clases.index(doc[1])] = 1

        entrenamiento.append([bag, output_row])

    entrenamiento = np.array(entrenamiento)

    x_train = list(entrenamiento[:, 0])  # valores de x
    y_train = list(entrenamiento[:, 1])  # valores de y
    return x_train, y_train


# aprendizaje del chatbot, red neuronal
def creador_modelo(x_train, y_train):
    model = Sequential()
    model.add(Dense(128, input_shape=(len(x_train[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(y_train[0]), activation='softmax'))

    sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)

    model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])
    hist = model.fit(np.array(x_train), np.array(y_train), epochs=300, batch_size=5, verbose=1)
    model.save("modelo.h5", hist)


# ejecución de los modelos
def comenzar_modelo():
    palabras, clases, documentos = tokenizador()
    palabras2 = lematizador(palabras, clases, documentos)
    x_train, y_train = entrenamiento(palabras2, clases, documentos)
    creador_modelo(x_train, y_train)


from intent_reference import start_intents

# para la ejecución automática
if __name__ == '__main__':
    start_intents()
    comenzar_modelo()