from sly import Parser
from alex import Lexico
from counter import Counter
from codificar import Codificar

class Semantico(Parser):
    tokens = Lexico.tokens

    def __init__(self):
        self.result = []


    
    
    # Tipos R: instrucción rd, rs1, rs2
    @_('TIPOR REGISTER COMMA REGISTER COMMA REGISTER')
    def instruction(self, p):
        self.result.append(Codificar.tipoR(p.TIPOR, p.REGISTER0, p.REGISTER1, p.REGISTER2))

    # Tipos I: instrucción rd, rs1, imm
    @_('TIPOI REGISTER COMMA REGISTER COMMA CONSTANTE')
    def instruction(self, p):
        self.result.append(Codificar.tipoI(p.TIPOI, p.REGISTER0, p.REGISTER1, p.CONSTANTE))

    # Tipo I de carga: instrucción rd, imm(rs1)
    @_('TIPOIC REGISTER COMMA CONSTANTE PA REGISTER PB')
    def instruction(self, p):
        self.result.append(Codificar.tipoIC(p.TIPOIC, p.REGISTER0, p.CONSTANTE, p.REGISTER1))

    # Tipo S: instrucción rs2, imm(rs1)
    @_('TIPOS REGISTER COMMA CONSTANTE PA REGISTER PB')
    def instruction(self, p):
        self.result.append(Codificar.tipoS(p.TIPOS, p.REGISTER0, p.CONSTANTE, p.REGISTER1))

    # Tipos B: instrucción rs1, rs2, etiqueta
    @_('TIPOB REGISTER COMMA REGISTER COMMA ETIQUETA')
    def instruction(self, p):
        self.result.append(Codificar.tipoB(p.TIPOB, p.REGISTER0, p.REGISTER1, p.ETIQUETA))

     # tipos U  # instruccion rd, imm
    @_('TIPOU REGISTER COMMA CONSTANTE')
    def instruction(self, p):
        self.result.append(Codificar.tipoU(p.TIPOU, p.REGISTER, p.CONSTANTE))