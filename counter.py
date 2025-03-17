
class Counter:
    contLn=0   #contador de lineas

    interface=1 #como se muestran los datos

    bytes=0 #posicion por bytes

    @classmethod
    def plus(cls):
        cls.contLn+=1
        cls.bytes+=4



    