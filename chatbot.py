# importe de librerías
from numpy.lib.function_base import insert
import random
import pandas as pd

import nltk, json, pickle
import numpy as np
from nltk.stem import SnowballStemmer
from tensorflow.keras.models import load_model

stemmer = SnowballStemmer('spanish')

model = load_model("modelo.h5")
intents = json.loads(open("intents.json").read())
palabras = pickle.load(open("palabras.pkl", "rb"))
clases = pickle.load(open("clases.pkl", "rb"))


# __________FUNCIONES QUE EL CHATBOT LE PUEDE OFRECER A LOS CLIENTES QUE LO UTILICEN
def menu_principal():
    menu_principal = {
        '1': ('Opción: ¿Quiénes somos?', accion1),
        '2': ('Opción: Horario de atención de nuestras sucursales.', accion2),
        '3': ('Opción: Agendar una cita de asesoría.', accion3),
        '4': ('Opción: Métodos de pago.', accion4),
        '5': ('Opción: Cotización de envío de paquetes.', accion5),
        '6': ('Opción: Reclamos y devoluciones.', accion6),
        '7': ('Opción: Recibe tus paquetes en tiempo EXPRESS, consulta nuestras tarifas.', accion7),

    }
    generar_menu(menu_principal)


# presentación del chatbot
def mostrar_menu(menu_principal):
    print('Hola soy P-BOT, estoy aquí para asistirte. ¿Deseas ayuda con algunas de estas opciones?')
    for clave in sorted(menu_principal):
        print(f' {clave}) {menu_principal[clave][0]}')


def ejecutar_opcion(opcion, menu_principal):
    menu_principal[opcion][1]()


def generar_menu(menu_principal):
    opcion = None
    mostrar_menu(menu_principal)
    opcion = leer_opcion(menu_principal)
    ejecutar_opcion(opcion, menu_principal)
    print()


# opción 1, descripción de la compañía
def accion1():
    print('SIC-Panamá es una empresa panameña de envío de paquetes en América, \n'
          'te conectamos con más de 30 sucursales entre Panamá, México, Brazil, Estados Unidos,\n'
          'Colombia, Nicaragua y Costa Rica. Nuestra misión es ofrecer vuelos diarios \n'
          'con un servicio de logística innovador, amigable y transparente.')


# opción 2, horarios de atención
def accion2():
    print('Nuestro horario de atención al cliente en nuestras \n'
          'sucursales es de Lunes a Viernes de 9:00 am a 5:00 pm Sábados \n'
          'de 9:00 am a 1:00 pm. Todas las sucursales están cerradas los Domingos.')


# opción 3, agendado de cita
def accion3():
    class Persona(object):
        def __init__(self, nombre, apellido):
            self.nombre = nombre
            self.apellido = apellido
            self.nombre_completo = self.nombre + " " + self.apellido
            self.calendario = Calendario()

        def disponible(self, tiempo):
            return self.calendario.disponible(tiempo)

        def hacer_cita(self, tiempo, record):
            self.calendario.anadir(tiempo, record)

        def get_record(self):
            return {
                'name': self.nombre_completo,
                'booking_class': self.__class__.__name__
            }

    class Cliente(Persona):
        def __init__(self, nombre, apellido, cedula):
            super(Cliente, self).__init__(nombre, apellido)
            self.cedula = cedula
            self.cliente_id = self.nombre[:1] + self.apellido + cedula

    class Agente(Persona):
        def __init__(self, nombre, apellido):
            super(Agente, self).__init__(nombre, apellido)

        def get_record(self):
            record = super(Agente, self).get_record()
            return record

    class Calendario(object):
        def __init__(self):
            self.entries = {}

        def disponible(self, tiempo):
            return tiempo not in self.entries

        def anadir(self, tiempo, record):
            self.entries[tiempo] = record

        def __str__(self):
            return str(self.entries)

    def agendar(agente, cliente, tiempo):
        if not agente.disponible(tiempo):
            print('El agente no está disponible')
            return
        if not cliente.disponible(tiempo):
            print('El cliente no está disponible'), cliente
            return

        agente.hacer_cita(tiempo, agente.get_record())
        cliente.hacer_cita(tiempo, cliente.get_record())

    A1 = Agente("José", "Burgos")
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    cedula = input('Ingrese su cédula: ')
    C1 = Cliente(nombre, apellido, cedula)
    from datetime import date, datetime
    year = date.today().year
    mes = int(input('Indique el mes (en números): '))
    dia = int(input('Indique el dia (en números). Estamos disponibles de lunes a viernes: '))
    hora = int(input('Indique la hora (en números, sin dos puntos). Estamos disponibles desde las 1 pm hasta 5 pm: '))
    tiempo = datetime(year, mes, dia, hora)
    agendar(A1, C1, tiempo)
    print("Su cita ha sido agendada para el: ", tiempo)


# opción 4, métodos de pago
def accion4():
    print('Aceptamos tarjeta clave, tarjeta de crédito, débito internacional, Paypal o Yappy.')


# opción 5, cotizaciones
def accion5():
    print('Contamos con envío de paquetes dependiendo del peso y dimensiones. \n'
          'Paquete XS: 1 kg o menos, hasta 35 cm de longuitud sumando el lado más largo y el más corto. Con una tarifa base de 3 dólares estadounidenses.\n'
          'Paquete S: 30 kg o menos, entre 36 y 50 cm de longuitud sumando el lado más largo y el más corto. Con una tarifa base de 3.50 dólares estadounidenses. \n'
          'Paquete M: 30 kg o menos, entre 51 y 80 cm de longuitud sumando el lado más largo y el más corto. Con una tarifa base de 4 dólares estadounidenses. \n'
          'Paquete L: 30 kg o menos, entre 81 y 120 cm de longuitud sumando el lado más largo y el más corto. Con una tarifa base de 5 dólares estadounidenses.\n'
          'Además de la tarifa base, se agrega 1.50 dólares estadounidenses por kilogramo.')


# opción 7, promociones
def accion7():
    print('¡CÓRTALO A LA MITAD! , con nuestro servicio de envío EXPRESS \n'
          'recibe tu paquete en la mitad del tiempo por un costo de 5 dólares \n'
          'estadounidenses adicionales al costo del envío de tu paquete.')


# data frame para el sistema de reclamos y devoluciones
def reclamos_df(x, randomnumber):
    df = pd.DataFrame()
    df.insert(0, 'Reclamo', x)
    df.insert(1, 'Número', randomnumber)
    df.to_excel("reclamo.xlsx")


# opción 6, reclamos y devoluciones
def accion6():
    print('Lamentamos que tu experiencia no haya sido la mejor. Qué salió mal? \n'
          'a. Producto dañado/roto/defectuoso \n'
          'b. Lo que recibí no fue lo que compré \n'
          'c. No me gustó el producto \n'
          'd. Orden incompleta ')
    x = input()
    randomnumber = random.randint(0, 10000000000)
    print('Nuestros colaboradores te estarán contactando sobre tu caso, tu número de reclamo es', randomnumber)
    reclamos_df(x, randomnumber)


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)

    bag = [0] * len(words)

    for i in sentence_words:
        for j, w in enumerate(words):
            if w == i:
                bag[j] = 1
    return (np.array(bag))


def predict_class(sentence, model):
    p = bow(sentence, palabras, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25

    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": clases[r[0]], "probability": str(r[1])})
    return return_list


import random


def get_response(ints, intents_json):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]

    for i in list_of_intents:
        if (i["tag"] == tag):
            result = random.choice(i["responses"])
            break
    return result


def chatbot_response(text):
    ints = predict_class(text, model)
    respuesta = get_response(ints, intents)
    return respuesta


# en esta funcion se
def leer_opcion(menu_principal):
    while (entrada_usuario := input('Opción:')) not in menu_principal:
        return_list = predict_class(entrada_usuario, model)
        if (entrada_usuario == '8'):
            generar_menu(menu_principal)
        elif len(return_list) > 0:
            res = chatbot_response(entrada_usuario)
            print(res)
        else:
            print('Opción incorrecta, vuelva a intentarlo.')
    return entrada_usuario


def start_chatbot():
    start_intents()
    comenzar_modelo()


# _________________________________MAIN________________________
from intent_reference import start_intents
from model_builder import comenzar_modelo

