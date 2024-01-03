'''
Este va a ser mi primer proyecto de control de versiones xd

'''

def palindromo(string): 
    start = 0
    end = -1
    control = len(string)// 2 +1
    val = True

    while control != 0 and string[start] == string[end]: 
        control -= 1
    
    if control != 0: val = False

    return val

##Funcion para hacer minusculas los textos 
def lowerCase(string): 
    string = string.lower() 
    return string

def removeSpaces(string):
    pass