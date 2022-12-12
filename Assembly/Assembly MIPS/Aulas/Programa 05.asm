.text
	li $t0, 75 # $t0 = 75
	li $t1, 25 # $t1 = 25
	sub $t2 $t0, $t1 # $t2 = $t0 - $st1
	subi $t3, $t2, 40 # $t3 = $t2 - 40
	
	li $v0 , 10
	syscall