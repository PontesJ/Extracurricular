.data # �rea para dados na m�moria principal

	msg: .asciiz "Ol�, Mundo!" # Mensagem a ser exibida para o usu�rio

.text # �rea para instru��es do programa

	li $v0, 4 # Instru��o para impress�o de String
	la $a0, msg # Indicar o endere�o em que est� a mensagem
	syscall # Fa�a! Imprima
	
	li $v0, 10 # Instru��o para encerrar o programa
	syscall # Fa�a! Encerre