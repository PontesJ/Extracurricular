.data
	msg: .asciiz "Digite um número: "
	branco: .byte ' '
.text
	li $v0, 4
	la $a0, msg
	syscall
	
	li $v0, 5
	syscall
	
	move $t0, $zero
	move $t1, $v0
	
	while:
		bgt $t0, $t1, saida # Se $t0 for maior que $t1, vai para saida
		li $v0, 1
		move $a0, $t0
		syscall
		
		li $v0, 4
		la $a0, branco
		syscall
		
		addi $t0, $t0, 1
		j while # Vai para "while"
		
	saida:
		li $v0, 10
		syscall