

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError as err:
        print("No encontré el archivo!", err)
    except IsADirectoryError:
        print("Encontre el archivo pero este es un directorio, no0 puedo leerlo")
    except PermissionError as err:
        print("no tengo permisos par leerlo", err)
    except OSError as err:
        if err.errno==2:
            print("No encontré el archivo")
        elif err.errno==13:
            print("encontré el archivo pero no pude leerlo")

def main():
    try:
        configuration = open('config.txt')
    except OSError as err:
        if err.errno==2:
            print("No encontré el archivo")
        elif err.errno==13:
            print("encontré el archivo pero no pude leerlo")


if __name__ == '__main__':
    main()