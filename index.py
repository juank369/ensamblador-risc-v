from alex import Lexico
from asin import Semantico
from counter import Counter


# Leer el archivo y procesar las instrucciones
lexer = Lexico()
parser = Semantico()
etiquetas={}

with open("prog1.asm", "r", encoding="utf-8") as archivo, open("instrucciones.bin", "w", encoding="utf-8") as salida:

    for linea in archivo:
        parser.parse(lexer.tokenize(linea))
    for instruccion_binaria in parser.result:
        salida.write(instruccion_binaria + "\n")
        Counter.plus()
        

print("Traducción completada.")
