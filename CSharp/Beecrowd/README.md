<img src="https://camo.githubusercontent.com/38d44389f0e6e510bcd916cffb484df9026d4d374160c290f94d1d3db4efb3ca/68747470733a2f2f7777772e62656563726f77642e636f6d2e62722f686f6d652f77702d636f6e74656e742f75706c6f6164732f323032312f30382f62656563726f77645f5f726f786f486f72436c65616e2d736d616c6c2d504e472d312e706e67" width="400">

# Iniciante

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1002">Beecrowd 1002 - Área do Círculo</a>

A fórmula para calcular a área de uma circunferência é: **area = π . raio²**. Considerando para este problema que **π** = 3.14159:

\- Efetue o cálculo da área, elevando o valor de **raio** ao quadrado e multiplicando por **π**.

**Entrada**

A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável **raio**.

**Saída**

Apresentar a mensagem "A=" seguido pelo valor da variável **area**, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 2.00 | A=12.5664 |
| 100.64 | A=31819.3103 |
| 150.00 | A=70685.7750 |

**<a href="./Exercícios/bee1002/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1005">Beecrowd 1005 - Média 1</a>

Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

**Entrada**

O arquivo de entrada contém 2 valores com uma casa decimal cada um.

**Saída**

Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 5.0<br>7.1 | MEDIA = 6.43182 |
| 0.0<br>7.1 | MEDIA = 4.84091 |
| 10.0<br>10.0 | MEDIA = 10.00000 |

**<a href="./Exercícios/bee1005/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1007">Beecrowd 1007 - Diferença</a>

Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

**Entrada**

O arquivo de entrada contém 4 valores inteiros.

**Saída**

Imprima a mensagem **DIFERENCA** com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 5<br>6<br>7<br>8 | DIFERENCA = -26 |
| 0<br>0<br>7<br>8 | DIFERENCA = -56 |
| 5<br>6<br>-7<br>8 | DIFERENCA = 86 |

**<a href="./Exercícios/bee1007/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1014">Beecrowd 1014 - Consumo</a>

Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

**Entrada**

O arquivo de entrada contém dois valores: um valor inteiro **X** representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

**Saída**

Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 500<br>35.0 | 14.286 km/l |
| 2254<br>124.4 | 18.119 km/l |
| 4554<br>464.6 | 9.802 km/l |

**<a href="./Exercícios/bee1014/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1016">Beecrowd 1016 - Distância</a>

Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.

Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, consegue se afastar um quilômetro a cada 2 minutos.

Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa distância do outro carro.

**Entrada**

O arquivo de entrada contém um número inteiro.

**Saída**

Imprima o tempo necessário seguido da mensagem "minutos".

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 30 | 60 minutos |
| 110 | 220 minutos |
| 7 | 14 minutos |

**<a href="./Exercícios/bee1016/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1036">Beecrowd 1036 - Fórmula de Bhaskara</a>

Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

**Entrada**

Leia três valores de ponto flutuante (double) A, B e C.

**Saída**

Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 10.0 20.1 5.1 | R1 = -0.29788<br>R2 = -1.71212 |
| 0.0 20.0 5.0 | Impossivel calcular |
| 10.3 203.0 5.0 | R1 = -0.02466<br>R2 = -19.68408 |
| 10.0 3.0 5.0 | Impossivel calcular |

**<a href="./Exercícios/bee1036/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1038">Beecrowd 1038 - Lanche</a>

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

<img src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1038_pt.png">

**Entrada**

O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

**Saída**

O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 3 2 | Total: R$ 10.00 |
| 4 3 | Total: R$ 6.00 |
| 2 3 | Total: R$ 13.50 |

**<a href="./Exercícios/bee1038/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1042">Beecrowd 1042 - Sort Simples</a>

Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

**Entrada**

A entrada contem três números inteiros.

**Saída**

Imprima a saída conforme foi especificado.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 7 21 -14 | -14<br>7<br>21<br><br>7<br>21<br>-14 |

**<a href="./Exercícios/bee1042/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1044">Beecrowd 1044 - Múltiplos</a>

Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem **"Sao Multiplos"** ou **"Nao sao Multiplos"**, indicando se os valores lidos são múltiplos entre si.

**Entrada**

A entrada contém valores inteiros.

**Saída**

A saída deve conter uma das mensagens conforme descrito acima.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 6 24 | Sao Multiplos |
| 6 25 | Nao sao Multiplos |

**<a href="./Exercícios/bee1044/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1048">Beecrowd 1048 - Aumento de Salário</a>

A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

| Salário | Percentual de Reajuste |
| ------------- | ------------- |
| 0 - 400.00 | 15% |
| 400.01 - 800.00 | 12% |
| 800.01 - 1200.00 | 10% |
| 1200.01 - 2000.00 | 7% |
| Acima de 2000.00 | 4% |

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

**Entrada**

A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

**Saída**

Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 400.00 | Novo salario: 460.00<br>Reajuste ganho: 60.00<br>Em percentual: 15 % |
| 800.01 | Novo salario: 880.01<br>Reajuste ganho: 80.00<br>Em percentual: 10 % |
| 2000.00 | Novo salario: 2140.00<br>Reajuste ganho: 140.00<br>Em percentual: 7 % |

**<a href="./Exercícios/bee1048/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1060">Beecrowd 1060 - Números Positivos</a>

Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

**Entrada**

Seis valores, negativos e/ou positivos.

**Saída**

Imprima uma mensagem dizendo quantos valores positivos foram lidos.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 7<br>-5<br>6<br>-3.4<br>4.6<br>12 | 4 valores positivos |

**<a href="./Exercícios/bee1060/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1064">Beecrowd 1064 - Positivos e Média</a>

Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

**Entrada**

A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

**Saída**

O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 7<br>-5<br>6<br>-3.4<br>4.6<br>12 | 4 valores positivos<br>7.4 |

**<a href="./Exercícios/bee1064/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1065">Beecrowd 1065 - Pares entre Cinco Números</a>

Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

**Entrada**

O arquivo de entrada contém 5 valores inteiros quaisquer.

**Saída**

Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 7<br>-5<br>6<br>-4<br>12 | 3 valores pares |

**<a href="./Exercícios/bee1065/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1071">Beecrowd 1071 - Soma de Impares Consecutivos I</a>

Leia 2 valores inteiros **X** e **Y**. A seguir, calcule e mostre a soma dos números impares entre eles.

**Entrada**

O arquivo de entrada contém dois valores inteiros.

**Saída**

O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 6<br>-5 | 5 |
| 15<br>12 | 13 |
| 12<br>12 | 0 |

**<a href="./Exercícios/bee1071/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1072">Beecrowd 1072 - Intervalo 2</a>

Leia um valor inteiro **N**. Este valor será a quantidade de valores inteiros **X** que serão lidos em seguida.
Mostre quantos destes valores **X** estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

**Entrada**

A primeira linha da entrada contém um valor inteiro **N** (**N** < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro **X** (-10<sup>7</sup> < **X** <10<sup>7</sup>).
 
**Saída**

Para cada caso, imprima quantos números estão dentro (**in**) e quantos valores estão fora (**out**) do intervalo.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 4<br>14<br>123<br>10<br>-25 | 2 in<br>2 out |

**<a href="./Exercícios/bee1072/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1073">Beecrowd 1073 - Quadrado de Pares</a>

Leia um valor inteiro **N**. Apresente o quadrado de cada um dos valores pares, de 1 até **N**, inclusive **N**, se for o caso.

**Entrada**

A entrada contém um valor inteiro **N** (5 < **N** < 2000).

**Saída**

Imprima o quadrado de cada um dos valores pares, de 1 até **N**, conforme o exemplo abaixo.

Tome cuidado! Algumas linguagens tem por padrão apresentarem como saída 1e+006 ao invés de 1000000 o que ocasionará resposta errada. Neste caso, configure a precisão adequadamente para que isso não ocorra.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 6 | 2^2 = 4<br>4^2 = 16<br>6^2 = 36 |

**<a href="./Exercícios/bee1073/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1078">Beecrowd 1078 - Tabuada</a>

Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
1 x N = N      2 x N = 2N        ...       10 x N = 10N

**Entrada**

A entrada contém um valor inteiro N (2 < N < 1000).

**Saída**

Imprima a tabuada de N, conforme o exemplo fornecido.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 140 | 1 x 140 = 140<br>2 x 140 = 280<br>3 x 140 = 420<br>4 x 140 = 560<br>5 x 140 = 700<br>6 x 140 = 840<br>7 x 140 = 980<br>8 x 140 = 1120<br>9 x 140 = 1260<br>10 x 140 = 1400 |

**<a href="./Exercícios/bee1078/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1113">Beecrowd 1113 - Crescente e Decrescente</a>

Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.

**Entrada**

A entrada contém vários casos de teste. Cada caso contém dois valores inteiros X e Y. A leitura deve ser encerrada ao ser fornecido valores iguais para X e Y.

**Saída**

Para cada caso de teste imprima “Crescente”, caso os valores tenham sido digitados na ordem crescente, caso contrário imprima a mensagem “Decrescente”.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 5 4<br>7 2<br>3 8<br>2 2 | Decrescente<br>Decrescente<br>Crescente<br> |

**<a href="./Exercícios/bee1113/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1132">Beecrowd 1132 - Múltiplos de 13</a>

Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

**Entrada**

O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

**Saída**

Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 100<br>200 | 13954 |

**<a href="./Exercícios/bee1132/Program.cs">Resolução</a>**

---

## <a href="https://www.beecrowd.com.br/judge/pt/problems/view/1142">Beecrowd 1142 - PUM</a>

Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

**Entrada**

O arquivo de entrada contém um número inteiro positivo N.

**Saída**

Imprima a saída conforme o exemplo fornecido.

| Exemplos de Entrada | Exemplos de Saída |
| ------------- | ------------- |
| 7 | 1 2 3 PUM<br>5 6 7 PUM<br>9 10 11 PUM<br>13 14 15 PUM<br>17 18 19 PUM<br>21 22 23 PUM<br>25 26 27 PUM |

**<a href="./Exercícios/bee1142/Program.cs">Resolução</a>**