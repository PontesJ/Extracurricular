.data
	idade: .word 51 # Valor inteiro na mem�ria RAM
	
.text
	li $v0, 1
	lw $a0, idade
	syscall
	
	li $v0, 10
	syscall