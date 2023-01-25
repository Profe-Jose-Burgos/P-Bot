# IMPORTAR LIBRERÍAS
# by: yinela, ashley y victoria
# python version : 3.9.12


# keras                         2.10.0
# Keras-Preprocessing           1.1.2
# nltk                          3.7
# numpy                         1.21.5
# tensorflow                    2.10.1
# tensorflow-estimator          2.10.0
# tensorflow-io-gcs-filesystem  0.27.0
# selenium                      4.7.2

def start():
    import pip

    # py -m pip install tensorflow
    # py -m pip install keras
    # py -m pip install nltk

    # __________________________ de aqui para abajo en consola______________

    # pip.main(["list"])

    pip.main(["install", "numpy"])
    pip.main(["install", "nltk==3.7"])
    pip.main(["install", "tensorboard"])
    pip.main(["install", "tensorflow-estimator"])
    pip.main(["install", "keras==2.10.0"])
    pip.main(["install", "Keras-Preprocessing==1.1.2"])
    pip.main(["install", "tensorflow==2.5"])
    pip.main(["install", "selenium==4.7.2"])

    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('universal_tagset')
    nltk.download('spanish_grammars')
    nltk.download('tagsets')
    nltk.download('stopwords')
    nltk.download('omw-1.4')


# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':
    start()