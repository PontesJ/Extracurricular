.data # Área para dados na mémoria principal

	msg: .asciiz "Olá, Mundo!" # Mensagem a ser exibida para o usuário

.text # Área para instruções do programa

	li $v0, 4 # Instrução para impressão de String
	la $a0, msg # Indicar o endereço em que está a mensagem
	syscall # Faça! Imprima
	
	li $v0, 10 # Instrução para encerrar o programa
	syscall # Faça! Encerre