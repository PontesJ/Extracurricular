.text
	li $t0, 12 # $t0 = 12
	addi $t1, $zero, 10 # $t1 = 0 + 10
	
	sll $s1, $t1, 10 # $s1 = $t1 * 2^10
	
	mul $s0, $t0, $t1 # $s0 = $t0 * $t1
	
	li $v0, 1 # Imprime um inteiro
	move $a0, $s0 # $a0 = $s0
	syscall # Faça, Imprimi
	
	li $v0 , 10
	syscall