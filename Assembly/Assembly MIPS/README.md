# <a href="https://youtube.com/playlist?list=PLHCyLhqWSaHBFGanvPRIIvta3eSna2G6Z">Assembly MIPS</a>

<img src= "https://i.imgur.com/MRXvBIg.png" width = 500>

Obs:
- Para caracteres ou cadeia de caracteres = la (load address).
- Para tipo .word = lw (load word).

## <a href="https://youtu.be/XtznbGfyd1o">Aula 1 - Instalação da IDE MARs e Programa Olá, mundo! (Hello World)</a>

**<a href="/Aulas/Programa 01.asm">Código:</a>**

```
.data # Área para dados na mémoria principal

	msg: .asciiz "Olá, Mundo!" # Mensagem a ser exibida para o usuário

.text # Área para instruções do programa

	li $v0, 4 # Instrução para impressão de String
	la $a0, msg # Indicar o endereço em que está a mensagem
	syscall # Faça! Imprima
	
	li $v0, 10 # Instrução para encerrar o programa
	syscall # Faça! Encerre
```

## <a href="https://youtu.be/sn6j-sRffsw">Aula 2 - Impressão de Char (Apenas um Caractere)</a>

**<a href="/Aulas/Programa 02.asm">Código:</a>**

```
.data
	caractere: .byte 'A' # Caractere a ser impresso

.text 
	li $v0, 4 # Imprimir char ou string
	la $a0 , caractere
	syscall
	
	li $v0 ,10 # Encerrar o programa
	syscall
```

## <a href="https://youtu.be/cfHK3xv4tYc">Aula 3 - Impressão de Inteiros (int)</a>

**<a href="/Aulas/Programa 03.asm">Código:</a>**

```
.data
	idade: .word 51 # Valor inteiro na memória RAM
	
.text
	li $v0, 1
	lw $a0, idade
	syscall
	
	li $v0, 10
	syscall
```

<!--

Template

## <a href="">Aula X - XXXXX</a>

**<a href="/Aulas/Programa XX.asm">Código:</a>**

```

```

-->