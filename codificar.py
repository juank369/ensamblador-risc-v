from counter import Counter



def validar(v1,v2,v3=0):
    if(v3!=0):#tipoI
        if(v1!=v2!=v3):
            return False
    elif(v3==0):
        if(v1!=v2):
            return False
    return True
    
def noValidaR():
    print(f"¡¡¡--instruccion {Counter.contLn} no valida expresion repetida--!!!")
    return "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def noValidaC():
    print(f"¡¡¡--instruccion {Counter.contLn} no valida imm no valido--!!!")
    return "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def complemento(n, bits):
                   #1 x 2ala12 complemento a 2
    return format((1 << bits) + n if n < 0 else n, f'0{bits}b')



class Codificar:#......clase

    

    #---------------------------------------------------R
    @classmethod
    def tipoR(cls, i, d, o1, o2):    # instruccion rd, rs1, rs2  == i d o1 o2

        if(validar(d,o1,o2)):
            return noValidaR()
        opcode="0110011"#opcode para todos


        rd=str( format(int(d[1:]),'05b'))#  rd

        funct3=""
        if(i=="add" or i=="sub"):#funct 3 de add y sub
            funct3="000"
        elif(i=="xor"):  #funct3 de xor
            funct3=str( format(4,'03b'))
        elif(i=="or"):#func3 de or
            funct3=str( format(6,'03b'))
        elif(i=="and"):#func3 de and
            funct3=str( format(7,'03b'))
        elif(i=="sll"):#func3 de sll
            funct3=str( format(1,'03b'))
        elif(i=="srl" or i=="sra"):#func3 de srl y sra
            funct3=str( format(5,'03b'))
        elif(i=="slt"):#func3 de slt
            funct3=str( format(2,'03b'))
        elif(i=="sltu"):#func3 de sltu
            funct3=str( format(3,'03b'))



        rs1=str( format(int(o1[1:]),'05b'))

        rs2=str( format(int(o2[1:]),'05b'))

        
        funct7=""
        if(i=="sub" or i=="sra"): 
            funct7="0100000" #agregamos funct7 de sub y de sra

        else:
            funct7="0000000" ##funcion 7 de la mayoria  

        #segun su tipo lo guarda
        codificada=""
        if(Counter.interface==0):
            codificada = funct7+rs2+rs1+funct3+rd+opcode
        if(Counter.interface==1):
            codificada=f"{funct7}   {rs2}   {rs1}   {funct3}    {rd}    {opcode}"

        return codificada
    

    #-------------------------------------------------------------------I

    @classmethod
    def tipoI(cls, i, d, o1, imm):  # instruccion rd, rs1, imm  == i rd, rs1, imm

        if(validar(d,o1)):
            return noValidaR()
        
        if(int(imm)< -2048 or int(imm)>2047):
            return noValidaC
        

        if((i=="slli" or i=="srli" or i=="srai") and (int(imm)<0 or int(imm)>31) or (i=="sltiu" and (int(imm)<0 or int(imm>2047)) )):
            return noValidaC()

        opcode="0010011"

        rd=str( format(int(d[1:]),'05b'))#  rd

        funct3=""
        if(i=="addi"): ##func3 ADDI
            funct3="000"
        elif(i=="xori"):  #funct3 de xor
            funct3=str( format(4,'03b'))
        elif(i=="ori"):#func3 de ORI
            funct3=str( format(6,'03b'))
        elif(i=="andi"):#func3 de ANDI
            funct3=str( format(7,'03b'))
        elif(i=="slli"):#func3 de SLLI
            funct3=str( format(1,'03b'))
        elif(i=="srli"):#func3 de SRLI
            funct3=str( format(5,'03b'))
        elif(i=="srai"):#func3 de SRAI
            funct3=str( format(5,'03b'))
        elif(i=="slti"):#func3 de SRAI
            funct3=str( format(2,'03b'))
        elif(i=="sltiu"):#func3 de SRAI
            funct3=str( format(3,'03b'))
        
        

        rs1=str( format(int(o1[1:]),'05b')) #agregamos rs1

        imm11_0=""
        if(i=="slli" or i=="srli"):  #funcion imm  #solo trabaja con valores entre 0 y 31 y se completa con 00..
            imm11_0=str( format(int(imm),'05b'))
            imm11_0="0000000"+imm11_0
            
        
        if(i=="srai"):  #funcion imm #funcion 7  #solo trabaja con valores entre 0 y 31 y se completa con 0100....
            imm11_0=str( format(int(imm),'05b'))
            imm11_0="0100000"+imm11_0
        

        if(int(imm)<0):#funcion imm
            imm11_0= complemento(int(imm),12)
        else:
            imm11_0=str( format(int(imm),'012b')) #agregamos imm


        #segun su tipo lo guarda
        codificada=""
        if(Counter.interface==0):
            codificada = imm11_0+rs1+funct3+rd+opcode
        if(Counter.interface==1):
            codificada=f"{imm11_0}  {rs1}   {funct3}    {rd}    {opcode}"

        return codificada
    
    #------------------------------------------IC
    @classmethod
    def tipoIC(cls ,i, d, imm, o1):

        if(validar(d,o1)):
            return noValidaR()
        
        if(int(imm)< -2048 or int(imm)>2047):
            return noValidaC()
        
        
        if((i=="lbu" or i=="lhu" ) and (int(imm)<0 )):
            return noValidaC()
        
        opcode="0000011" #opcode

        rd=str( format(int(d[1:]),'05b'))#  rd

        funct3=""
        if(i=="lb"): ##func3 lb
            funct3="000"
        elif(i=="lh"):#func3 de lh
            funct3=str( format(1,'03b'))
        elif(i=="lw"):#func3 de lh
            funct3=str( format(2,'03b'))
        elif(i=="lbu"):#func3 de lh
            funct3=str( format(4,'03b'))
        elif(i=="lhu"):#func3 de lh
            funct3=str( format(5,'03b'))


        rs1=str( format(int(o1[1:]),'05b')) #agregamos rs1

        if(int(imm)<0):#funcion 7
            imm11_0= complemento(int(imm),12)
        else:
            imm11_0=str( format(int(imm),'012b')) #agregamos imm

                #segun su tipo lo guarda
        codificada=""
        if(Counter.interface==0):
            codificada = imm11_0+rs1+funct3+rd+opcode
        if(Counter.interface==1):
            codificada=f"{imm11_0}  {rs1}   {funct3}    {rd}    {opcode}"

        return codificada
    
    
    #----------------------------------------------S
    @classmethod
    def tipoS(cls,i, o2, imm, o1):

        if(validar(o2,o1)):
            return noValidaR()
        
        if(int(imm)< -2048 and int(imm)>2047):
            return noValidaC()
        
        opcode="0100011" #opcode

        c=""
        if(int(imm)<0):#primeros 5 del imm
            c= complemento(int(imm),12)
        else:
            c=str( format(int(imm),'012b')) #agregamos imm

        imm4_0=c[7:]

        if(i=="sb"): ##func3
            funct3="000"
        elif(i=="sh"):#func3
            funct3=str( format(1,'03b'))
        elif(i=="sw"):#func3
            funct3=str( format(2,'03b'))

        rs1=str( format(int(o1[1:]),'05b')) #agregamos rs1

        rs2=str( format(int(o2[1:]),'05b')) #agregamos rs2

        imm11_5 =c[:7]

                        #segun su tipo lo guarda
        codificada=""
        if(Counter.interface==0):
            codificada = imm11_5+rs2+rs1+funct3+imm4_0+opcode
        if(Counter.interface==1):
            codificada=f"{imm11_5}  {rs2}  {rs1}   {funct3}    {imm4_0}    {opcode}"

        return codificada
    

        
        