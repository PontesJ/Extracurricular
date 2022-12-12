.data
	msg: .asciiz "Digite um número: "
	par: .asciiz "Par"
	impar: .asciiz "Ímpar"
.text
	.main: # Programa Principal
		la $a0, msg # $a0 = msg
		jal imprimiString # Chama a função "imprimiString"
		
		jal lerInteiro # Chama a função "lerInteiro"
		
		move $a0, $v0 # $a0 = $v0
		
		jal parImpar # Chama a função "parImpar"
		
		beq $v0, $zero, ImprimiPar # if ($v0 == 0) Chama a função "ImprimiPar"
		la $a0, impar # $a0 = impar
		jal imprimiString # Chama a função "imprimiString"
		jal fim # Chama a função "fim"
		
	ImprimiPar: # Função "ImprimiPar
		la $a0, par # $a0 = par
		jal imprimiString # Chama a função "imprimiString"
		jal fim # Chama a função "fim"
	
	parImpar: # Função "parImpar"
		li $t1, 2 # $t1 = 2
		div $a0, $t1 # $a0 / $t1
		mfhi $v0 # $v0 = Resto da divisão
		jr $ra # Retorna para onde foi chamada
	
	imprimiString: # Função "imprimiString"
		li $v0, 4 # Imprimi String
		syscall # Imprimi
		jr $ra # Retorna para onde foi chamada
		
	lerInteiro: # Função "lerInteiro"
		li $v0, 5 # Le um inteiro
		syscall # Le
		jr $ra # Retorna para onde foi chamada
		
	fim: # Função "fim"
		li $v0, 10 # Encerra o programa
		syscall # Encerra