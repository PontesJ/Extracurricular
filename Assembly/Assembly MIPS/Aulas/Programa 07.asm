.text
	li $t0, 32 # $t0 = 32
	li $t1, 5 # $t1 = 5
	
	srl $s2, $t0, 2 # $s2 = $t0 / 2^2 // Só pega a parte inteira
	
	div $t0, $t1 # $t0 / $t1 -> A parte inteira vai para "lo" e o resto vai para "hi"
	
	mflo $s0 # $s0 = Parte inteira da divisão
	mfhi $s1 # #s1 = Resto da divisão