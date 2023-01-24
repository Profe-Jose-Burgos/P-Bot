# creación del archivo json, con los patrones de respuestas para el chatbot
import json


def guardar_json(datos):
    archivo = open("intents.json", "w")
    json.dump(datos, archivo, indent=4)


# posibles inputs de los usuarios y las respuestas con las cuales el chatbot debe de responderle al usuario.
def start_intents():
    libreto = {"intents":
        [
            {"tag": "saludos",
             "patterns": ["hola", "buenos dias", "buenas tardes", "buenas noches", "hay alguien?", "hey", "saludos",
                          "buenas"],
             "responses": ["Hola!"]},
            {"tag": "despedidas",
             "patterns": ["chao", "adiós", "hasta luego", "hasta pronto", "eso es todo", "hasta la proxima"],
             "responses": ["Hasta luego", "Fue un placer asistirte."]},
            {"tag": "agradecimientos",
             "patterns": ["gracias", "muchas gracias", "mil gracias", "muy amable", "te lo agradezco", "muy agradecido",
                          "gracias por su tiempo", "thank you", "thanks", "ty"],
             "responses": ["Fue un placer ayudarle. \n"]},
            {"tag": "norespuesta",
             "patterns": [""],
             "responses": ["No se detectó una respuesta \n"]},
            {"tag": "ayuda",
             "patterns": ["ayudame", "ayúdame", "necesito", "favor", "quiero", "me gustaría", "me gustaria", "ayuda"],
             "responses": ["Estoy aquí para asistirte."]},
            {"tag": "menu_principal",
             "patterns": ["enseñame las opciones", "otra vez", "volver"],
             "responses": ["Si deseas regresar al menú principal, escribe '8'"]},

        ]
    }
    guardar_json(libreto)


# ejecución de los intents
if __name__ == '__main__':
    start_intents()