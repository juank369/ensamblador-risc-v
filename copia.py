from sly import Parser
from alex import Lexico
from counter import Counter

class Semantico(Parser):
    tokens = Lexico.tokens

    def __init__(self):
        self.result = []



    # tipos R  # instruccion rd, rs1, rs2
    @_('TIPOR REGISTER COMMA REGISTER COMMA REGISTER')
    def instruction(self, p):
        self.result.append(tipoR(p.TIPOR, p.REGISTER0, p.REGISTER1, p.REGISTER2))

 # tipos I   # instruccion rd, rs1, imm
    @_('TIPOI REGISTER COMMA REGISTER COMMA CONSTANTE')
    def instruction(self, p):
        self.result.append(tipoI(p.TIPOI, p.REGISTER0, p.REGISTER1, p.CONSTANTE))

 # tipo I de carga #instruccion rd, imm(rs1)

    @_('TIPOIC REGISTER COMMA CONSTANTE PA REGISTER PB')
    def instruction(self, p):
        self.result.append(tipoIC(p.TIPOIC, p.REGISTER0, p.CONSTANTE ,p.REGISTER1))

# tipo S  #instruccion rs2, imm(rs1)

    @_('TIPOS REGISTER COMMA CONSTANTE PA REGISTER PB')
    def instruction(self, p):
        self.result.append(tipoS(p.TIPOS, p.REGISTER0, p.CONSTANTE ,p.REGISTER1))

 # tipos B  # instruccion rs1, rs2, imm
    @_('TIPOB REGISTER COMMA REGISTER COMMA CONSTANTE')
    def instruction(self, p):
        self.result.append(tipoB(p.TIPOB, p.REGISTER0, p.REGISTER1, p.CONSTANTE))

     # tipos J  # instruccion rd, imm
    @_('TIPOJ REGISTER COMMA CONSTANTE')
    def instruction(self, p):
        self.result.append(tipoJ(p.TIPOJ, p.REGISTER, p.CONSTANTE))

    #tipo I raro# jalr rd, imm(rs1)

     # tipos U  # instruccion rd, imm
    @_('TIPOU REGISTER COMMA CONSTANTE')
    def instruction(self, p):
        self.result.append(tipoU(p.TIPOU, p.REGISTER, p.CONSTANTE))




def validar(v1,v2,v3=0):
    if(v3!=0):#tipoI
        if(v1!=v2!=v3):
            return False
    elif(v3==0):
        if(v1!=v2):
            return False
    return True
    
def noValidaR():
    print(f"¡¡¡--instruccion {Counter.cont} no valida expresion repetida--!!!")
    return "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def noValidaC():
    print(f"¡¡¡--instruccion {Counter.cont} no valida imm no valido--!!!")
    return "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


#---------------------------------------------------

def tipoR(i, d, o1, o2):    # instruccion rd, rs1, rs2  == i d o1 o2

    if(validar(d,o1,o2)):
        return noValidaR()
    codificada="0110011"#opcode para todos


    codificada=str( format(int(d[1:]),'05b'))+codificada#  rd

    if(i=="add" or i=="sub"):#funct 3 de add y sub
        codificada="000"+codificada
    elif(i=="xor"):  #funct3 de xor
        codificada=str( format(4,'03b'))+codificada
    elif(i=="or"):#func3 de or
        codificada=str( format(6,'03b'))+codificada
    elif(i=="and"):#func3 de and
        codificada=str( format(7,'03b'))+codificada
    elif(i=="sll"):#func3 de sll
        codificada=str( format(1,'03b'))+codificada
    elif(i=="srl" or i=="sra"):#func3 de srl y sra
        codificada=str( format(5,'03b'))+codificada
    elif(i=="slt"):#func3 de slt
        codificada=str( format(2,'03b'))+codificada
    elif(i=="sltu"):#func3 de sltu
        codificada=str( format(3,'03b'))+codificada



    codificada=str( format(int(o2[1:]),'05b'))+str( format(int(o1[1:]),'05b'))+codificada #agregamos rs1 y rs2

    
    
    if(i=="sub" or i=="sra"): 
        codificada="0100000"+codificada #agregamos funct7 de sub y de sra

    else:
        codificada="0000000"+codificada ##funcion 7 de la mayoria  

    return codificada
#--------------------------------------------------------I

def complemento(n, bits):
                   #1 x 2ala12 complemento a 2
    return format((1 << bits) + n if n < 0 else n, f'0{bits}b')


def tipoI(i, d, o1, imm):  # instruccion rd, rs1, imm  == i rd, rs1, imm

    if(validar(d,o1)):
        return noValidaR()

    if((i=="slli" or i=="srli" or i=="srai") and (int(imm)<0 or int(imm)>32) or (i=="sltiu" and int(imm)<0 )):
        return noValidaC()

    codificada="0010011"

    codificada=str( format(int(d[1:]),'05b'))+codificada#  rd

    if(i=="addi"): ##func3 ADDI
        codificada="000"+codificada
    elif(i=="xori"):  #funct3 de xor
        codificada=str( format(4,'03b'))+codificada
    elif(i=="ori"):#func3 de ORI
        codificada=str( format(6,'03b'))+codificada
    elif(i=="andi"):#func3 de ANDI
        codificada=str( format(7,'03b'))+codificada
    elif(i=="slli"):#func3 de SLLI
        codificada=str( format(1,'03b'))+codificada
    elif(i=="srli"):#func3 de SRLI
        codificada=str( format(5,'03b'))+codificada
    elif(i=="srai"):#func3 de SRAI
        codificada=str( format(5,'03b'))+codificada
    elif(i=="slti"):#func3 de SRAI
        codificada=str( format(2,'03b'))+codificada
    elif(i=="sltiu"):#func3 de SRAI
        codificada=str( format(3,'03b'))+codificada
    
    

    codificada=str( format(int(o1[1:]),'05b'))+codificada #agregamos rs1

    if(i=="slli" or i=="srli"):  #funcion 7
        codificada=str( format(int(imm),'05b'))+codificada
        codificada="0000000"+codificada
        return codificada
    
    if(i=="srai"):  #funcion 7
        codificada=str( format(int(imm),'05b'))+codificada
        codificada="0100000"+codificada
        return codificada
    
    


    if(int(imm)<0):#funcion 7
        codificada= complemento(int(imm),12)+codificada
    else:
        codificada=str( format(int(imm),'012b'))+codificada #agregamos imm

    return codificada
    
#------------------------------------------IC

def tipoIC(i, d, imm, o1):

    if(validar(d,o1)):
        return noValidaR()
    
    if((i=="lbu" and int(imm)<0 ) or (i=="lhu" and int(imm)<0 )):
        return noValidaC()
    
    codificada="0000011" #opcode

    codificada=str( format(int(d[1:]),'05b'))+codificada#  rd

    if(i=="lb"): ##func3 lb
        codificada="000"+codificada
    elif(i=="lh"):#func3 de lh
        codificada=str( format(1,'03b'))+codificada
    elif(i=="lw"):#func3 de lh
        codificada=str( format(2,'03b'))+codificada
    elif(i=="lbu"):#func3 de lh
        codificada=str( format(4,'03b'))+codificada
    elif(i=="lhu"):#func3 de lh
        codificada=str( format(5,'03b'))+codificada


    codificada=str( format(int(o1[1:]),'05b'))+codificada #agregamos rs1

    if(int(imm)<0):#funcion 7
        codificada= complemento(int(imm),12)+codificada
    else:
        codificada=str( format(int(imm),'012b'))+codificada #agregamos imm

    return codificada


#----------------------------------------------S

def tipoS(i, o2, imm, o1):

    if(validar(o2,o1)):
        return noValidaR()
    
    codificada="0100011" #opcode

    c=""
    if(int(imm)<0):#primeros 5 del imm
        c= complemento(int(imm),12)
    else:
        c=str( format(int(imm),'012b')) #agregamos imm

    codificada=c[7:]+codificada

    if(i=="sb"): ##func3
        codificada="000"+codificada
    elif(i=="sh"):#func3
        codificada=str( format(1,'03b'))+codificada
    elif(i=="sw"):#func3
        codificada=str( format(2,'03b'))+codificada

    codificada=str( format(int(o1[1:]),'05b'))+codificada #agregamos rs1

    codificada=str( format(int(o2[1:]),'05b'))+codificada #agregamos rs1

    codificada =c[:7]+codificada

    return codificada


    

#------------------------------------------------------tipoB

def complemento2(n, bits):
    return format((1 << bits) + n if n < 0 else n, f'0{bits+1}b') 


def tipoB(i, o1, o2, imm):  # instruccion rd, rs1, imm  

    if((i=="bltu" and int(imm)<0) or (i=="bgeu" and int(imm)>4094)):
        return noValidaC()

    
    if((int(imm) < -4096) or (int(imm)>4094)):
        return noValidaC()
    
    codificada="1100011" #opcode

    c=""
    if(int(imm)<0):#primeros 5 del imm
        c= complemento(int(imm),13)
    else:
        c=str( format(int(imm),'013b')) #agregamos imm

    
    imm12 = c[0]   # Bit 12
    imm10_5 = c[2:8]  # Bits 10 a 5
    imm4_1 = c[8:12]  # Bits 4 a 1
    imm11 = c[1]  # Bit 11
    
    
    
    codificada=imm4_1+imm11+codificada
    

    if(i=="beq"):
        codificada="000"+codificada
    elif(i=="bne"):#func3
        codificada=str( format(1,'03b'))+codificada
    elif(i=="blt"):#func3
        codificada=str( format(4,'03b'))+codificada
    elif(i=="bge"):#func3
        codificada=str( format(5,'03b'))+codificada
    elif(i=="bltu"):#func3
        codificada=str( format(6,'03b'))+codificada
    elif(i=="bgeu"):#func3
        codificada=str( format(7,'03b'))+codificada

    codificada=str( format(int(o1[1:]),'05b'))+codificada #agregamos rs1
    codificada=str( format(int(o2[1:]),'05b'))+codificada #agregamos rs2
    
    codificada=imm12+imm10_5+ codificada

    
        
    return codificada


#-----------------------------J

def tipoJ(i, d, imm):

    codificada="1101111"

    codificada=str( format(int(d[1:]),'05b'))+codificada#  rd
    c=""
    if(int(imm)<0):#funcion 7
        c= complemento(int(imm),21)
    else:
        c=str( format(int(imm),'021b'))
    
    imm1_9=c[1:9]
    imm11=c[9]
    imm10_1=c[10:20]
    imm20=c[0]








#-----------------------------------------------------------------u

def tipoU(i,d,imm):

    if(int(imm)< -(2**31) or int(imm)> ((2**31) - 1)):
        return noValidaC

    codificada=""

    if(i=="lui"):
        codificada="0110111"
    elif(i=="auipc"):
        codificada="0010111"

    
    codificada=str( format(int(d[1:]),'05b'))+codificada#  rd

    if(int(imm)<0):#funcion 7
        codificada= complemento(int(imm),20)+codificada
    else:
        codificada=str( format(int(imm),'020b'))+codificada #agregamos imm

    return codificada

    


     

