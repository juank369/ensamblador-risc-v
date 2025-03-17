from sly import Parser
from alex import Lexico
from counter import Counter
from codificar import Codificar

class Semantico(Parser):
    tokens = Lexico.tokens

    def __init__(self):
        self.result = []


    
    # tipos R  # instruccion rd, rs1, rs2
    @_('TIPOR REGISTER COMMA REGISTER COMMA REGISTER')
    def instruction(self, p):
        self.result.append(Codificar.tipoR(p.TIPOR, p.REGISTER0, p.REGISTER1, p.REGISTER2))

    # tipos I   # instruccion rd, rs1, imm
    @_('TIPOI REGISTER COMMA REGISTER COMMA CONSTANTE')
    def instruction(self, p):
        self.result.append(Codificar.tipoI(p.TIPOI, p.REGISTER0, p.REGISTER1, p.CONSTANTE))

    # tipo I de carga #instruccion rd, imm(rs1)
    @_('TIPOIC REGISTER COMMA CONSTANTE PA REGISTER PB')
    def instruction(self, p):
        self.result.append(Codificar.tipoIC(p.TIPOIC, p.REGISTER0, p.CONSTANTE ,p.REGISTER1))

    # tipo S  #instruccion rs2, imm(rs1)
    @_('TIPOS REGISTER COMMA CONSTANTE PA REGISTER PB')
    def instruction(self, p):
        self.result.append(Codificar.tipoS(p.TIPOS, p.REGISTER0, p.CONSTANTE ,p.REGISTER1))

    
    