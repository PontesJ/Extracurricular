.data
	saudacao: .asciiz "Ol�. Por favor, forne�a sua idade: "
	saida: .asciiz "Sua idade �: "
	anos: .asciiz " anos"
.text
	li $v0, 4 # Imprimi uma string
	la $a0, saudacao # $a0 = saudacao
	syscall # Imprimi 
	
	li $v0, 5 # Leitura de inteiro / Valor lido ir� para $v0
	syscall
	
	move $t0, $v0 # $t0 = $v0
	
	li $v0, 4 # Imprimi uma string
	la $a0, saida # a0 = saida
	syscall # Imprimi
	
	li $v0, 1 # Imprimi um inteiro
	move $a0, $t0 # $a0 = $t0 
	syscall # Imprimi
	
	li $v0, 4
	la $a0, anos
	syscall # Imprimi
	
	li $v0 , 10
	syscall