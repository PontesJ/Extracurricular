.data
	pergunta: .asciiz "Digite um número: "
	numero: .asciiz "O número "
	menor: .asciiz " é menor que 0"
	maior: .asciiz " é maior que 0"
	igual: .asciiz " é igual a 0"
.text
	li $v0, 4
	la $a0, pergunta
	syscall
	
	li $v0, 5
	syscall
	
	move $t0, $v0
	
	blt $t0, $zero, menorQue # Se $t0 for menor que 0
	
	bgt $t0, $zero, maiorQue # Se $t0 for maior que 0
	
	beq $t0, $zero, igualA # Se $t0 for igual a 0
	
	menorQue:
		li $v0, 4
		la $a0, numero
		syscall
		
		li $v0, 1
		move $a0, $t0
		syscall
		
		li $v0, 4
		la $a0, menor
		syscall
		
		li $v0, 10
		syscall
		
	maiorQue:
		li $v0, 4
		la $a0, numero
		syscall
		
		li $v0, 1
		move $a0, $t0
		syscall
		
		li $v0, 4
		la $a0, maior
		syscall
		
		li $v0, 10
		syscall
		
	igualA:
		li $v0, 4
		la $a0, numero
		syscall
		
		li $v0, 1
		move $a0, $t0
		syscall
		
		li $v0, 4
		la $a0, igual
		syscall
		
		li $v0, 10
		syscall