.data
	pergunta: .asciiz "Digite seu nome: "
	saudacao: .asciiz "Olá, "
	nome: .space 25
.text
	li $v0, 4 # Imprimi string
	la $a0, pergunta # $a0 = pergunta
	syscall # Imprimi
	
	li $v0, 8 # Lê no console
	la $a0, nome # $a0 = nome / nome = valor digitado pelo usuário
	la $a1, 25 #a1 = 25 / Tamanho máximo do valor
	syscall # Pede a leitura
	
	li $v0, 4 # Imprimi string
	la $a0, saudacao # $a0 = saudacao
	syscall # Imprimi
	
	li $v0 4 # Imprimi string
	la $a0, nome # $a0 = nome
	syscall # Imprimi
	
	li $v0, 10
	syscall