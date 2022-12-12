# <a href="https://youtube.com/playlist?list=PLHCyLhqWSaHBFGanvPRIIvta3eSna2G6Z">Assembly MIPS</a>

<img src= "https://i.imgur.com/MRXvBIg.png" width = 500>

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

---

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

---

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

Obs:
- Para caracteres ou cadeia de caracteres = la (load address).
- Para tipo .word = lw (load word).

---

## <a href="https://youtu.be/h5tas4VkkDM">Aula 4 - Soma de Inteiros (add e addi)</a>

<img src="https://i.imgur.com/DYIJKiA.png" width = 500>

**<a href="/Aulas/Programa 04.asm">Código:</a>**

```
.text
	li $t0, 75 # $t0 = 75
	li $t1, 25 # $t1 = 25
	add $s0, $t0, $t1 # $s0 = $t0 + $t1
	addi $s1, $s0, 36 # $s1 = $s0 + 36
	
	li $v0 , 10
	syscall
```

---

## <a href="https://youtu.be/ybzPO7YQ4eE">Aula 5 - Subtração de Inteiros (sub e subi)</a>

<img src="https://i.imgur.com/j3VSiGX.png" width = 500>

**<a href="/Aulas/Programa 05.asm">Código:</a>**

```
.text
	li $t0, 75 # $t0 = 75
	li $t1, 25 # $t1 = 25
	sub $t2 $t0, $t1 # $t2 = $t0 - $st1
	subi $t3, $t2, 40 # $t3 = $t2 - 40
	
	li $v0 , 10
	syscall
```

---

## <a href="https://youtu.be/Lm6OMCIezoM">Aula 6 - Multiplicação de Inteiros (mul e sll) - SHIFT LEFT</a>

<img src="https://i.imgur.com/LVMY4JV.png" width = 500>
<img src="https://i.imgur.com/POX9zRL.png" width = 500>
<img src="https://i.imgur.com/a46Z6AR.png" width = 500>

**<a href="/Aulas/Programa 06.asm">Código:</a>**

```
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
```

---

## <a href="https://youtu.be/D8kDCU7qaWQ">Aula 7 - Divisão de Inteiros (div e srl) - SHIFT RIGHT</a>

<img src="https://i.imgur.com/gvnLOgm.png" width = 500>

**<a href="/Aulas/Programa 07.asm">Código:</a>**

```
.text
	li $t0, 32 # $t0 = 32
	li $t1, 5 # $t1 = 5
	
	srl $s2, $t0, 2 # $s2 = $t0 / 2^2 // Só pega a parte inteira
	
	div $t0, $t1 # $t0 / $t1 -> A parte inteira vai para "lo" e o resto vai para "hi"
	
	mflo $s0 # $s0 = Parte inteira da divisão
	mfhi $s1 # #s1 = Resto da divisão
```

---

## <a href="https://youtu.be/yMBKV05mndI">Aula 8 - Leitura de Inteiros</a>

<img src="https://i.imgur.com/dyW2Mto.png" width = 500>

**<a href="/Aulas/Programa 08.asm">Código:</a>**

```
.data
	saudacao: .asciiz "Olá. Por favor, forneça sua idade: "
	saida: .asciiz "Sua idade é: "
	anos: .asciiz " anos"
.text
	li $v0, 4 # Imprimi uma string
	la $a0, saudacao # $a0 = saudacao
	syscall # Imprimi 
	
	li $v0, 5 # Leitura de inteiro / Valor lido irá para $v0
	syscall
	
	move $t0, $v0 # $t0 = $v0
	
	li $v0, 4 # Imprimi uma string
	la $a0, saida # a0 = saida
	syscall # Imprimi
	
	li $v0, 1 # Imprimi um inteiro
	move $a0, $t0 # $a0 = $t0 
	syscall # Imprimi
	
	li $v0, 4
	la $a0, anos
	syscall # Imprimi
	
	li $v0 , 10
	syscall
```

---

## <a href="https://youtu.be/McVQ0d_25Hw">Aula 9 - Leitura de Strings (Caracteres)</a>

<img src="https://i.imgur.com/RZZLRDi.png" width = 500>

**<a href="/Aulas/Programa 09.asm">Código:</a>**

```
.data
	pergunta: .asciiz "Digite seu nome: "
	saudacao: .asciiz "Olá, "
	nome: .space 25
.text
	li $v0, 4 # Imprimi string
	la $a0, pergunta # $a0 = pergunta
	syscall # Imprimi
	
	li $v0, 8 # Lê no console
	la $a0, nome # $a0 = nome / nome = valor digitado pelo usuário
	la $a1, 25 #a1 = 25 / Tamanho máximo do valor
	syscall # Pede a leitura
	
	li $v0, 4 # Imprimi string
	la $a0, saudacao # $a0 = saudacao
	syscall # Imprimi
	
	li $v0 4 # Imprimi string
	la $a0, nome # $a0 = nome
	syscall # Imprimi
	
	li $v0, 10
	syscall
```

---

## <a href="https://youtu.be/R2Lbr93GedU">Aula 12 - Comandos Condicionais Se (BEQ BNE BLT BGT BLE BGE)</a>

<img src="https://i.imgur.com/EUcSAwe.png" width = 500>

**<a href="/Aulas/Programa 12.asm">Código:</a>**

```
.data
	msg: .asciiz "Forneça um número: "
	numero: .asciiz "O número "
	par: .asciiz " é par"
	impar: .asciiz " é ímpar"
.text
	li $v0, 4 # Imprimi string
	la $a0, msg # $a0 = msg
	syscall # Imprimi
	
	li $v0, 5 # Lê no console
	syscall # Lê
	
	li $t0, 2 # $t0 = 2
	div $v0, $t0 # $v0 / $t0
	mfhi $t0 # $t0 = Resto da divisão
	
	move $t1, $v0 # $t1 = $v0
	
	beq $t0, $zero, imprimiPar # Se $t0 for igual a $zero, vá para "imprimiPar"
	
	li $v0, 4 # Imprimi string
	la $a0, numero
	syscall
		
	li $v0, 1 # Imprimi inteiro
	move $a0, $t1 # $a0 = $t0
	syscall
		
	li $v0, 4 # Imprimi string
	la $a0, impar
	syscall
	
	li $v0, 10
	syscall
	
	imprimiPar:
		li $v0, 4 # Imprimi string
		la $a0, numero
		syscall
		
		li $v0, 1 # Imprimi inteiro
		move $a0, $t1 # $a0 = $t0
		syscall
		
		li $v0, 4 # Imprimi string
		la $a0, par
		syscall
		
		li $v0, 10
		syscall
```

---

## <a href="https://youtu.be/Fk_G0gXlUfw">Aula 13 - Comandos Condicionais Se (Exercício Complementar)</a>

**<a href="/Aulas/Programa 13.asm">Código:</a>**

```
.data
	pergunta: .asciiz "Digite um número: "
	numero: .asciiz "O número "
	menor: .asciiz " é menor que 0"
	maior: .asciiz " é maior que 0"
	igual: .asciiz " é igual a 0"
.text
	li $v0, 4
	la $a0, pergunta
	syscall
	
	li $v0, 5
	syscall
	
	move $t0, $v0
	
	blt $t0, $zero, menorQue # Se $t0 for menor que 0
	
	bgt $t0, $zero, maiorQue # Se $t0 for maior que 0
	
	beq $t0, $zero, igualA # Se $t0 for igual a 0
	
	menorQue:
		li $v0, 4
		la $a0, numero
		syscall
		
		li $v0, 1
		move $a0, $t0
		syscall
		
		li $v0, 4
		la $a0, menor
		syscall
		
		li $v0, 10
		syscall
		
	maiorQue:
		li $v0, 4
		la $a0, numero
		syscall
		
		li $v0, 1
		move $a0, $t0
		syscall
		
		li $v0, 4
		la $a0, maior
		syscall
		
		li $v0, 10
		syscall
		
	igualA:
		li $v0, 4
		la $a0, numero
		syscall
		
		li $v0, 1
		move $a0, $t0
		syscall
		
		li $v0, 4
		la $a0, igual
		syscall
		
		li $v0, 10
		syscall
```

---

## <a href="https://youtu.be/FHo1s_Q33L8">Aula 14 - Laços de Repetição While (Enquanto)</a>

<img src="https://i.imgur.com/tOyLJyq.png" width = 500>

**<a href="/Aulas/Programa 14.asm">Código:</a>**

```
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
```

---

## <a href="https://youtu.be/tibWGO35FS0">Aula 15 - Subrotinas (Funções e Procedimentos)</a>

<img src="https://i.imgur.com/SQxuHtY.png" width = 500>

**<a href="/Aulas/Programa 15.asm">Código:</a>**

```
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
```

---

<!--

Template

## <a href="">Aula X - XXXXX</a>

**<a href="/Aulas/Programa XX.asm">Código:</a>**

```

```

---


<img src="" width = 500>

-->