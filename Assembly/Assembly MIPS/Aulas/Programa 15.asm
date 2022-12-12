.data
	msg: .asciiz "Digite um n�mero: "
	par: .asciiz "Par"
	impar: .asciiz "�mpar"
.text
	.main: # Programa Principal
		la $a0, msg # $a0 = msg
		jal imprimiString # Chama a fun��o "imprimiString"
		
		jal lerInteiro # Chama a fun��o "lerInteiro"
		
		move $a0, $v0 # $a0 = $v0
		
		jal parImpar # Chama a fun��o "parImpar"
		
		beq $v0, $zero, ImprimiPar # if ($v0 == 0) Chama a fun��o "ImprimiPar"
		la $a0, impar # $a0 = impar
		jal imprimiString # Chama a fun��o "imprimiString"
		jal fim # Chama a fun��o "fim"
		
	ImprimiPar: # Fun��o "ImprimiPar
		la $a0, par # $a0 = par
		jal imprimiString # Chama a fun��o "imprimiString"
		jal fim # Chama a fun��o "fim"
	
	parImpar: # Fun��o "parImpar"
		li $t1, 2 # $t1 = 2
		div $a0, $t1 # $a0 / $t1
		mfhi $v0 # $v0 = Resto da divis�o
		jr $ra # Retorna para onde foi chamada
	
	imprimiString: # Fun��o "imprimiString"
		li $v0, 4 # Imprimi String
		syscall # Imprimi
		jr $ra # Retorna para onde foi chamada
		
	lerInteiro: # Fun��o "lerInteiro"
		li $v0, 5 # Le um inteiro
		syscall # Le
		jr $ra # Retorna para onde foi chamada
		
	fim: # Fun��o "fim"
		li $v0, 10 # Encerra o programa
		syscall # Encerra