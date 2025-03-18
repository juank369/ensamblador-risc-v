    addi x1, x0, 10
    addi x2, x0, 20
    beq x1, x2, end  
    addi x3, x0, 30
    ori x5, x12, 40
    sh x5, 15(x11)
end:
    addi x4, x0, 40
    lui x2, 200