.data
	msg: .asciiz "Forne�a um n�mero: "
	numero: .asciiz "O n�mero "
	par: .asciiz " � par"
	impar: .asciiz " � �mpar"
.text
	li $v0, 4 # Imprimi string
	la $a0, msg # $a0 = msg
	syscall # Imprimi
	
	li $v0, 5 # L� no console
	syscall # L�
	
	li $t0, 2 # $t0 = 2
	div $v0, $t0 # $v0 / $t0
	mfhi $t0 # $t0 = Resto da divis�o
	
	move $t1, $v0 # $t1 = $v0
	
	beq $t0, $zero, imprimiPar # Se $t0 for igual a $zero, v� para "imprimiPar"
	
	li $v0, 4 # Imprimi string
	la $a0, numero
	syscall
		
	li $v0, 1 # Imprimi inteiro
	move $a0, $t1 # $a0 = $t0
	syscall
		
	li $v0, 4 # Imprimi string
	la $a0, impar
	syscall
	
	li $v0, 10
	syscall
	
	imprimiPar:
		li $v0, 4 # Imprimi string
		la $a0, numero
		syscall
		
		li $v0, 1 # Imprimi inteiro
		move $a0, $t1 # $a0 = $t0
		syscall
		
		li $v0, 4 # Imprimi string
		la $a0, par
		syscall
		
		li $v0, 10
		syscall