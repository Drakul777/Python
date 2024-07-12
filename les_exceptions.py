import json

class FileNotJsonFormatError(Exception)
    def __init__(self):
        self.message = "Vous ne pouvezmettre que des fichiers en .json"


def read_json_file(file_name):
    try:
        if not file_name.endswith('.json'):
            raise FileNotJsonFormatError
        fichier = open(file_name)
        print(json.load(fichier))
        fichier.close()
    except FileNotFoundError:
        print("Le fichier n'existe pas")

#excpt exception as e:
    #print(e)
#pour que le premier message uniquement apparaisse
    except Exception as e:
        print(e.message)


read_json_file('bonjour.txt')
