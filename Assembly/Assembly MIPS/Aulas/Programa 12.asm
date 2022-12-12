.data
	msg: .asciiz "Forneça um número: "
	numero: .asciiz "O número "
	par: .asciiz " é par"
	impar: .asciiz " é ímpar"
.text
	li $v0, 4 # Imprimi string
	la $a0, msg # $a0 = msg
	syscall # Imprimi
	
	li $v0, 5 # Lê no console
	syscall # Lê
	
	li $t0, 2 # $t0 = 2
	div $v0, $t0 # $v0 / $t0
	mfhi $t0 # $t0 = Resto da divisão
	
	move $t1, $v0 # $t1 = $v0
	
	beq $t0, $zero, imprimiPar # Se $t0 for igual a $zero, vá para "imprimiPar"
	
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