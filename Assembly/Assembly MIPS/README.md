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

<!--

Template

## <a href="">Aula X - XXXXX</a>

**<a href="/Aulas/Programa XX.asm">Código:</a>**

```

```

---


-->