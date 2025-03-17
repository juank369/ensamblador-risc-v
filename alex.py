from sly import Lexer
from counter import Counter

x = 0


class Lexico(Lexer):
    tokens = {TIPOIC,TIPOI,TIPOR,TIPOS,TIPOB,TIPOJ,TIPOU, REGISTER,CONSTANTE, COMMA, PA, PB }
    ignore = ' \t\n'

    #tipo I de carga
    TIPOIC=r'lbu|lb|lhu|lh|lw'
    #tipo I
    TIPOI =r'addi|xori|ori|andi|slli|srli|srai|sltiu|slti'
    #tipo R
    TIPOR =r'add|sub|xor|or|and|sll|srl|sra|sltu|slt'

    #tipo S
    TIPOS=r'sb|sh|sw'

    #tipo B
    TIPOB=r'bltu|bgeu|beq|bne|blt|bge'
    
    #tipo J
    TIPOJ= r"jal"

    #tipo U
    TIPOU= r'lui|auipc'


    COMMA = r','
    REGISTER = r'\b(x(?:[0-9]|[1-2][0-9]|3[0-1])|zero|ra|sp|gp|tp|t0|t1|t2|s0|fp|s1|a0|a1|a2|a3|a4|a5|a6|a7|s2|s3|s4|s5|s6|s7|s8|s9|s10|s11|t3|t4|t5|t6)\b'#X(?:[0-9]|[1-2][0-9]|3[0-1])
    CONSTANTE = r'-?(409[0-4]|40[0-8]\d|[1-3]\d{3}|\d{1,3})'

    PA=r'\('
    PB=r'\)'
    
    

    def REGISTER(self, t):
        alias_a_numero = {
            "zero": "x0", "ra": "x1", "sp": "x2", "gp": "x3", "tp": "x4",
            "t0": "x5", "t1": "x6", "t2": "x7", "s0": "x8", "fp": "x8", "s1": "x9",
            "a0": "x10", "a1": "x11", "a2": "x12", "a3": "x13", "a4": "x14",
            "a5": "x15", "a6": "x16", "a7": "x17", "s2": "x18", "s3": "x19",
            "s4": "x20", "s5": "x21", "s6": "x22", "s7": "x23", "s8": "x24",
            "s9": "x25", "s10": "x26", "s11": "x27", "t3": "x28", "t4": "x29",
            "t5": "x30", "t6": "x31"
        }

        if t.value in alias_a_numero:
            t.value = alias_a_numero[t.value] 

        return t

    def error(self, t):
        print(f"-----\nCarácter no válido: {t.value[0]} en expresión #{Counter.contLn} índice: {self.index}. Corrija y reintente.")
        self.index += 1
