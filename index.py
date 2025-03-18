from alex import Lexico
from asin import Semantico
from counter import Counter


# Leer el archivo y procesar las instrucciones
lexer = Lexico()
parser = Semantico()



with open("prog1.asm", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        if linea.strip().endswith(":"):  
            etiqueta = linea.strip()[:-1] 
            Counter.etiquetas[etiqueta] = Counter.bytes
            continue
        else:
            Counter.bytes += 4  


Counter.bytes=0
with open("prog1.asm", "r", encoding="utf-8") as archivo, open("instrucciones.bin", "w", encoding="utf-8") as salida:

    for linea in archivo:
        linea = linea.strip()  
        if linea.endswith(":"): 
            continue
        parser.parse(lexer.tokenize(linea))
        Counter.contLn +=1
        Counter.bytes+=4
    for instruccion_binaria in parser.result:
        salida.write(instruccion_binaria + "\n")
        
        
        
print("Traducción completada.")
