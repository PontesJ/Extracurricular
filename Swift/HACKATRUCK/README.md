# CONCEITOS INICIAIS

## ALGORITMOS & LÓGICA DE PROGRAMAÇÃO

O termo algoritmo designa uma sequência de instruções bem definidas para chegarmos a um objetivo. Como “sequência bem definida de instruções”, devemos entender instruções claras que podem ser facilmente entendidas por quem vai executá-las e em uma ordem bem estabelecida. Apesar do termo algoritmo ser muito utilizado na matemática e computação, ele está presente em muitas atividades do nosso dia a dia. Toda vez que executamos algum processo que pode ser repetido através de um conjunto de instruções como trocar o pneu de um carro, dar o nó em uma gravata, cozinhar um prato utilizando uma receita, tocar uma música utilizando uma partitura ou cifras, estamos executando um algoritmo.

Computadores, apesar de sua grande capacidade em processar e calcular grandes volumes de informação de forma muito rápida, não são máquinas inteligentes. Para realizar qualquer tarefa, por mais simples que seja, é preciso que sejam atribuídos a eles um conjunto de operações que eles consigam compreender. Cabe, portanto, à capacidade de raciocínio humano indicar ao computador quais instruções devem ser efetuadas, e em qual ordem, para que ele processe as informações disponíveis de forma útil e adequada, ou seja, devemos informar qual algoritmo o computador deve executar para atingir o que desejamos. O que chamamos de programa é, portanto, um algoritmo escrito em uma linguagem que o computador consiga entender.

A palavra lógica se origina da palavra grega logos, que significa conhecimento, pensamento. Podemos traduzir lógica, dentro de nosso contexto, como a arte de pensar de forma correta e bem estruturada. Quando nos referimos à lógica de programação, estamos falando da estruturação de nossas ideias com o objetivo de resolver um problema utilizando o computador como ferramenta.

Quando pretendemos fazer isto, devemos entender o problema que queremos resolver, dividi-lo em problemas menores até chegarmos a problemas que sabemos resolver, ou melhor, em problemas que sabemos mostrar ao computador como ele deve resolver. Por fim, devemos unir as soluções destes pequenos problemas (sempre que possível utilizando o computador para isto) para finalmente chegarmos à solução do problema original.

Este curso se propõe a mostrar as operações básicas que um computador consegue executar, que são, portanto, os menores problemas que podem ser resolvidos por um computador. Através de exemplos e exercícios, mostraremos como podemos conectar estas operações de forma a resolvermos problemas mais complexos.

---

## PROGRAMA

Como vimos na introdução, um programa é um conjunto de instruções, também conhecido como algoritmo, que pode ser entendido e executado por um computador/dispositivo móvel. Para que isto ocorra, o algoritmo deve ser escrito no que chamamos de **linguagem de programação**.

Uma linguagem de programação é construída de forma que seja compreendida por seres humanos e também lida e executada por um computador.

Existem inúmeras linguagens de programação para os mais diversos fins (e gostos). Como exemplos, podemos citar: **Swift**, Java, C##, JavaScript, C, C++, Ruby, Pascal, Python, Visual Basic, COBOL, FORTRAN, LISP, PROLOG, entre uma infinidade de outras.

Como nosso curso é direcionado ao desenvolvimento de aplicativos para dispositivos móveis em iOS, utilizaremos nos módulos de Lógica de Programação e Orientação a Objetos, a linguagem **Swift**, assim, já nos familiarizaremos e aprenderemos a sintaxe da linguagem junto aos conceitos e operações básicas.

Programar é criar um conjunto de instruções para um dispositivo executar, sempre de forma objetiva e ordenada, com o intuito do programa ser compreendido e bem processado. Vamos a um exemplo:

Ao montar uma pizza temos a seguinte lista de ingredientes:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/1._Conceitos_Iniciais_-_01.png" width = 400>

Quais são as nossas opções de instruções?

Se sugerirmos:

1 – AdicionarQueijo ( )

Teremos um problema, pois colocaríamos o queijo onde? As instruções, que também são conhecidas como comandos, precisam ser objetivas, mas também necessitam estar ordenadas. Vamos iniciar novamente:

1 – PegarMassa( )

2 – AdicionarQueijo( )

3 – AdicionarCalabresa( )

4 – AdicionarTomate( )

5 – AdicionarCheiroVerde( )

6 – AdicionarCebola( )

7 – AdicionarAzeitonas( )

Será esse o nosso melhor conjunto de instruções? Vamos ver o resultado?

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/1._Conceitos_Iniciais_-_02.png" width = 400>

Esquecemos de alguma coisa? Precisamos fatiar os ingredientes! Nova receita:

1 – FatiarQueijo( )

2 – FatiarCalabresa( )

3 – FatiarTomate( )

4 – FatiarCebola( )

5 – PegarMassa( )

6 – AdicionarQueijo( )

7 – AdicionarCalabresa( )

8 – AdicionarTomate( )

9 – AdicionarCebola( )

10 – AdicionarCheiroVerde( )

11 – AdicionarAzeitonas( )

Será!?

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/1._Conceitos_Iniciais_-_03.png" width = 400>

Agora sim!  Montamos nossa pizza e conseguimos entender o quanto comandos imprecisos ou a falta deles podem nos levar a resultados inesperados!

**💡 Repararam que nossos comandos foram escritos com as palavras juntas e sempre terminando com parênteses ( )? Veremos o porquê mais adiante!**

---

## VARIÁVEIS E CONSTANTES

Todo programa necessita armazenar dados em algum momento, e em Swift temos duas formas de fazer isso: variáveis e constantes. Uma variável, como o nome sugere, é um armazenador que pode ser alterado, já a constante é sempre uma... constante! Jamais poderá ser alterada. Para criar nossos armazenamentos utilizamos os prefixos *var* para variáveis e *let* para constantes. Vamos exemplificar e aprender a declarar variáveis e constantes:

```
var saborPizza = "Calabresa" //Variável
var tamanhoEmCM = 48 //Variável Númerica

let nomePizzaria = "PizzaForDevs" // Constante
let precoUnico = 49.99 // Constante Númerica

print(saborPizza)
print(tamanhoEmCM)
print(nomePizzaria)
print(precoUnico)
```

**Saída**

```
Calabresa
48
PizzaForDevs
49.99
```

**💡Podemos utilizar o comando print( ) para imprimir um valor!**

A nossa sintaxe é simples: *var* nomeDaVariavel = valorMutavel *let*nomeDaConstante = valorImutavel

**💡Ainda nesse módulo aprenderemos a criar variáveis sem definir um valor inicial!**

O *var* é utilizado somente para criar nossa variável, para atualizar o valor NÃO precisamos dele:

```
var saborPizza = "Calabresa" //variavel inicializada com o sabor Calabresa

saborPizza = "Quatro Queijos" //Novo valor para a váriavel saborPizza

print (saborPizza)
```

**Saída**

```
Quatro Queijos
```

Vimos no exemplo acima que conseguimos atualizar o sabor da nossa pizza, mas e se tentássemos atualizar o nome do nosso restaurante que está em uma constante?

```
let nomePizzaria = "PizzaForDevs"

nomePizzaria = "Pizzaria dos Programadores"
```

**Saída**

```
main.swift:3:1: error: cannot assign to value: 'nomePizzaria' is a 'let' constant
nomePizzaria = "Pizzaria dos Programadores"
^~~~~~~~~~~~
main.swift:1:1: note: change 'let' to 'var' to make it mutable
let nomePizzaria = "PizzaForDevs"
```

ERRO! Sempre que tentarmos atualizar o valor de uma constante seremos avisados que não é possível. Isso prova que constantes são armazenamentos criados para nunca serem alterados.<br>
Vamos praticar?  Coloque somente seu primeiro nome na variável chamada *nomeCompleto* e na próxima linha atualize o valor dela colocando também o seu sobrenome.

```
var nomeCompleto = "primeiroNome"

print(nomeCompleto)
```

**<a href="./Códigos/main01.swift">Código</a>**

Fácil, concordam?

**💡 Repararam que as variáveis e constantes que recebem valores numéricos não utilizam ASPAS DUPLAS “ ” para atribuir os valores? Entenderemos o porquê agora.**

---

## PADRÕES DE ESCRITA E NOMENCLATURAS

#### NOMENCLATURAS DE VARIÁVEIS E CONSTANTES

Os nomes das constantes e variáveis ​​podem conter diversos caracteres, incluindo caracteres Unicode. Vejamos alguns exemplos:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/1._Conceitos_Iniciais_-_04.png" width = 400>

Todos os casos acima são aceitos e válidos. De regra, temos que os nomes não podem conter espaços em branco, símbolos matemáticos, setas ou ainda caracteres de desenho de linha. Nomes de variáveis e constantes também não podem começar com números, mas os mesmos, como no exemplo acima, podem estar contidos após o primeiro caractere.

#### CAMEL CASE

Um segundo padrão, chamado Camel Case, afeta mais coisas além de variáveis e constantes. Segundo a convenção da documentação oficial do *Swift* nomes de tipos (classes) e protocolos são **UpperCamelCase**. Todo o restante é **lowerCamelCase**. Mas o que é Camel Case?<br>
O Camel Case é uma forma de agrupar e combinar palavras de forma legível e sem espaços para validar a nossa regra de nomenclatura. Vejamos alguns exemplos:

```
/*
    Nome Completo
    user login count
*/

var nomeCompleto = ""

var userLoginCount = ""
```

Devemos ainda ressaltar que siglas podem se manter 100% em maiúsculas. Por exemplo:

```
/*
    padrão ABNT
    código UTF8
*/

var padraoABNT = ""

var codigoUTF8 = ""
```

Dessa forma, utilizando **lowerCamelCase** e **UpperCamelCase** conseguimos manter nossas Strings válidas e legíveis.

---

## TIPOS DE DADOS

Tipo de dado nada mais é que o tipo da informação que queremos utilizar no nosso código, logo, ao criar nossas variáveis é **obrigatório** que seja informado um tipo. Seja ele de forma **explícita** ou **implícita**. A seguir, veremos ambas as formas após conhecermos os tipos.

Definições e exemplos:
 
**Int -** É utilizado para números inteiros.<br>
**Exemplos:** 2, 10, -5134, -7832

**Character -** É utilizado para um único caractere.<br>
**Exemplos:** “A”, “B”, “9”, “@”, “%”

**String -** É utilizado para dois ou mais caracteres, um GRUPO de caracteres.<br>
**Exemplos:** “Palavra”, “Tipo 2”, “Uma String é um grupo de caracteres.”
 
**Float -** É utilizado para números com decimais e tem capacidade para armazenar números de até 7 casas (contando a parte inteira); ao entrar uma oitava, ele fará o arredondamento pra cima caso a oitava posição seja maior que 5 ou apenas cortará se for menor 5.<br>
**Exemplos:** 2.99, 10.99, -5134.1323, -7832.31273<br>
Se tentarmos atribuir:<br>
10.499999 o **Swift** irá considerar 10.5<br>
2.9999999 o **Swift** irá considerar 3<br>
1.123456789 o **Swift** irá considerar 1.123457

**Double -** Também é utilizado para números com decimais e tem o dobro da capacidade do ***Float***, ficando assim com altíssima precisão.<br>
**Exemplos:** 2.99, 10.99, -7896,99, -6575787.768756987<br>
Se tentarmos atribuir: 123456789.12345678 o **Swift** irá considerar 123456789.1234568

**Bool -**  É um tipo binário (booleano), ou seja, ele armazena apenas se é verdadeiro ou falso.<br>
**Exemplos:** true ou false

**💡 Estes são apenas os tipos mais básicos de dados que temos no Swift!**

**Qual a diferença entre tipos explícitos e implícitos?**

Falamos que o tipo é obrigatório, certo? Mas, por que quando criamos nossas primeiras variáveis e constantes não os informamos?<br>
O **Swift** faz essa tipificação de forma automática quando criamos uma variável ou constante atribuindo um valor a ela, logo, nossos primeiros exemplos já tinham nossos tipos definidos de forma implícita.<br>
Sim! Se for um número inteiro ele automaticamente criará um ***Int***.

```
var num1 = 10 //Tipificação Implicita
var num2: Int = 10 //Tipificação Explicita

print (num1)
print(type(of: num1)) //Comando para verificar o tipo

print (num2)
print(type(of: num2))//Comando para verificar o tipo
```

**Saída**

```
10
Int
10
Int
```

Para criarmos uma ***String*** de forma implícita, basta que nosso valor esteja entre aspas duplas “ ”.

```
var nome = "Ayrton" //Tipificação Implicita
var sobrenome: String = "Senna" //Tipificação Explicita

print (nome)
print(type(of: nome)) //Comando para verificar o tipo

print (sobrenome)
print(type(of: sobrenome))//Comando para verificar o tipo
```

**Saída**

```
Ayrton
String
Senna
String
```

Já qualquer decimal criado de for implícita, será definido como ***Double***! Então, se quisermos trabalhar com nosso ***Float***, precisamos fazer de forma explícita.

```
var pi =  3.14 //Tipificação Implicita

var piDouble: Double = 3.14 //Tipificação Explicita

var piFloat: Float = 3.14//Tipificação Explicita

print (pi)
print(type(of: pi)) //Comando para verificar o tipo

print (piDouble)
print(type(of: piDouble))//Comando para verificar o tipo

print (piFloat)
print(type(of: piFloat))//Comando para verificar o tipo
```

**Saída**

```
3.14
Double
3.14
Double
3.14
Float
```

Nossos ***Booleanos (Bool)*** também podem ser criados de forma implícita e explícita. Vejamos:

```
var verdadeiro =  true //Tipificação Implicita

var falso: Bool = false //Tipificação Explicita

print (verdadeiro)
print(type(of: verdadeiro)) //Comando para verificar o tipo

print (falso)
print(type(of: falso))//Comando para verificar o tipo
```

**Saída**

```
true
Bool
false
Bool
```

Para criar ***Characteres (Character)*** sempre faremos de forma explícita (de forma implícita, mesmo com um único caractere, será criado uma ***String***):

```
var caractere: Character = "a" //Tipificação Explicita
var caractere2: Character = "@" //Tipificação Explicita
var caractere3: Character = "3" //Tipificação Explicita

print(caractere)
print(caractere2)
print(caractere3)
```

**Saída**

```
a
@
3
```

**Vamos retornar aos exemplos de criação de variáveis:**<br>
Uma vez demonstrados os tipos de dados e os dados armazenados, vamos dar continuidade e entender mais um pouco sobre criar variáveis.<br>
Podemos criar sem atribuir um valor inicial desde que, informemos o seu tipo (Declaração explícita) e façamos a atribuição quando necessário.

```
var char: Character 
var texto: String
var nummero: Int
var decimal: Double

char = "!" 
texto = "Palavras, Textos, Frases, Numéros, R$ 99.990, etc."
nummero = 99
decimal = 0.99

print (char)
print (texto)
print (nummero)
print (decimal)
```

**Saída**

```
!
Palavras, Textos, Frases, Numéros, R$ 99.990, etc.
99
0.99
```

Podemos também criar múltiplas variáveis do mesmo tipo em uma só linha:

```
var saborPizza, saborSuco: String
var querSuco: Bool
var precoPizza, precoSucoPequeno, precoSucoGrande: Double

saborPizza = "Pepperoni" 
saborSuco = "Laranja"

querSuco = true

precoPizza = 29.99
precoSucoPequeno = 5.99 
precoSucoGrande = 8.99

print (saborPizza)
print (saborSuco)
print (querSuco)
print (precoPizza)
print (precoSucoPequeno)
print (precoSucoGrande)
```

**Saída**

```
Pepperoni
Laranja
true
29.99
5.99
8.99
```

**Vamos treinar?**

```
/************************* 
*******Criar 3 váriaveis Int 
**************************/

print() //Imprimir os valores
print() //Imprimir os valores
print() //Imprimir os valores

/************************* 
*******Criar 3 váriaveis String 
**************************/

print() //Imprimir os valores
print() //Imprimir os valores
print() //Imprimir os valores

/************************* 
*******Criar 2 váriaveis Bool 
**************************/

print() //Imprimir os valores
print() //Imprimir os valores
```

**<a href="./Códigos/main02.swift">Código</a>**

**💡 Repararam nos comentários que estão dentro do simulador? Podemos comentar usando:**<br>
**// para linha única**<br>
**Ou**<br>
**/* Para**<br>
**Multilinhas */**

**Tudo que estiver após o // ou compreendido entre /*  */ serão apenas comentários que não influenciarão no nosso processamento!**

## COMANDOS DE ATRIBUIÇÃO

Começaremos aqui a ver as operações que podem ser realizadas dentro de um programa. Os primeiros comandos que estudaremos são os comandos de atribuição. <br>
Vimos nos tópicos anteriores o que são e para que servem as variáveis e os tipos de dados. Vimos também que devemos declarar estas variáveis antes de usá-las e como podemos fazer isto. Precisamos agora começar a utilizá-las.<br>
O primeiro comando que estudaremos é o comando de atribuição, assim chamado por atribuir (definir) um valor a uma variável.<br>
Para nossas **atribuições**, utilizamos sempre o =, independente se no momento de criação ou na atribuição posterior. O valor que vamos atribuir também pode estar em outras variáveis:

```
var nome: String = "João"

var sobrenome: String = "Almeida"

var nomeCompleto: String = nome + " " + sobrenome

print (nomeCompleto)
```

**Saída**

```
João Almeida
```

Isso faz com que o valor fique **gravado** na variável.

**💡 Utilizamos + para fazer a concatenação (junção) de Strings. Observe que colocamos  + “  ” +  para adicionar uma String com espaço entre as Strings nome e sobrenome.**

Sempre é necessário atentar-se ao tipo de dado a ser gravado, já que ele deve ter o mesmo tipo da nossa variável que foi criada. Feito isso, nossa variável passa a **conter** aquele valor **armazenado** até que um novo seja adicionado a ela (não existe limite de quantidade para o processo de atribuição). Vejamos mais alguns exemplos:

```
var char: Character = "$"
print(char)

var numero: Int
numero = 123
print(numero)

var primeiroNome: String = "João"
var segundoNome:String

segundoNome = primeiroNome

print(primeiroNome)
print(segundoNome)
```

**Saída**

```
$
123
João
João
```

Podemos também sobrescrever o valor de uma variável: 

```
var primeiroNome: String = "João"
var segundoNome: String = "Marcos"

segundoNome = primeiroNome //Nessa linha gravamos na variável segundoNome o valor da variável primeiroNome

print(primeiroNome)
print(segundoNome)
```

**Saída**

```
João
João
```

**💡 Cuidado: Uma vez atualizado não é possível recuperar o valor gravado anteriormente!**

**Vamos treinar?**<br>
Atribua novas informações para as variáveis:

```
var data: String = "01/01/2022"

var banco: String = "Foundations Bank"

var valorSaque: Double
valorSaque = 160.00

/******************* 
Altere os valores aqui 
********************/

data = 
banco = 
valorSaque =

/********************
Imprima os novos valores aqui 
********************/

print(data)
print(banco)
print(valorSaque)
```

**<a href="./Códigos/main03.swift">Código</a>**

Agora, atribua utilizando as informações contidas nas variáveis:

```
/******************* 
Valores à serem utilizados
********************/
var dataDoSaque: String  = "01/01/2021"
var nomeBanco: String = "Money Bank"
var valorParaSacar: Double = 700

/******************* 
Variáveis à serem atualizadas
********************/

var data: String = ""
var banco: String = ""
var valorSaque: Double = 0

/******************* 
Altere os valores aqui 
********************/

/********************
Imprima os novos valores aqui 
********************/

print(data)
print(banco)
print(valorSaque)
```

**<a href="./Códigos/main04.swift">Código</a>**

E confira os valores no painel de saída de dados.

## OPERAÇÕES ARITMÉTICAS

Operações aritméticas são operações numéricas (***Int, Float, Double***) e podem ser unidas para formar uma expressão matemática mais complexa.<br>
Os operadores que utilizaremos aqui são **+, -, *, /, %, pow( ), sqrt( )** que estão descritos abaixo:

| **Operador** | **Operação** |
| ------------- | ------------- |
| **Adição +** | É utilizado para somar |
| **Subtração -** | É utilizado para subtrair |
| **Multiplicação *** | É utilizado para multiplicar |
| **Divisão /** | É utilizado para dividir |
| **Resto %** | Retorna o ***resto*** da divisão entre dois números |

**Exemplos:**

```
var x: Int = 10
var y: Int = 2

var total: Int 
total = x + y
print("Resultado - Adição de " + String(x) + " + " + String(y) + " é " + String(total))

total = x - y
print("Resultado - Subtração de " + String(x) + " - " + String(y) + " é " + String(total))

total = x * y
print("Resultado - Multiplicação de " + String(x) + " * " + String(y) + " é " + String(total))

total = x / y
print("Resultado - Divisão de " + String(x) + " / " + String(y) + " é " + String(total))

total = x % y
print("Resultado - O resto da Divisão de " + String(x) + " % " + String(y) + " é " + String(total))

total = x % 3
print("Resultado - O resto da Divisão de " + String(x) + " % " + String(3) + " é " + String(total))
```

**Saída**

```
Resultado - Adição de 10 + 2 é 12
Resultado - Subtração de 10 - 2 é 8
Resultado - Multiplicação de 10 * 2 é 20
Resultado - Divisão de 10 / 2 é 5
Resultado - O resto da Divisão de 10 % 2 é 0
Resultado - O resto da Divisão de 10 % 3 é 1
```

**💡 Para utilizar no print( ) as variáveis em conjunto com os demais textos(Strings), precisamos converter eles para String. Por isso utilizamos String( ) para transformar os números em texto. Veremos uma forma mais prática de fazer essa junção mais abaixo: a interpolação de Strings!**

| **Operador** | **Operação** |
| ------------- | ------------- |
| **pow( )** | É utilizado para elevar à potência de um número |
| **sqrt( )** | É utilizado para calcular a raiz quadrada de um número |

**Exemplos:**

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/1._Conceitos_Iniciais_-_07.png" width = 400>

**💡 Para utilizar pow( )  e sqrt( ), potência e raiz quadrada, precisamos importar a classe UIKit.**<br>
**💡 Prestaram atenção na Interpolação de Strings em ação? Utilizando apenas um (variavel) conseguimos imprimir os valores das variáveis. Vamos ver mais um exemplo e exercitar?**<br>
**Exemplo:**

```
var nomeCurso: String = "Foundations"
var duracaoEmMeses: Int = 6
var duracaoEmAnos: Float = 0.5

var latitude: Double = -22.812449
var longitude: Double = -47.0636755

print("O Curso \(nomeCurso), tem duração aproximada de \(duracaoEmMeses) meses (\(duracaoEmAnos) ano), sua Localização em Lat, Log é \(latitude), \(longitude)")
```

**Saída**

```
O Curso Foundations, tem duração aproximada de 6 meses (0.5 ano), sua Localização em Lat, Log é -22.812449, -47.0636755
```

**Hora de treinar:**

```
var x: Int = 12
var y: Int = 3

var total: Int 
total = x + y
print("O resultado da Soma de \(x) + \(y) é \(total)")

total = x - y
print(" ")

total = x * y
print(" ")

total = x / y
print(" ")

total = x % y
print(" ")

total = x % 5
print(" ")
```

**<a href="./Códigos/main05.swift">Código</a>**

E aí? Tranquilo utilizar interpolação de ***Strings***? É bem mais fácil do que ter que converter e concatenar ***Strings,*** concordam?<br>
Outra coisa que precisamos aprender, é o que chamamos de precedência dos operadores, ou seja, a ordem em que as operações são executadas. Essa regra é similar à regra aplicada em uma expressão matemática.<br>
Imagine que tenhamos a expressão “4 + 5 * 3”. Esta expressão seria executada com a mesma precedência matemática; primeiro a multiplicação, depois a soma. Seria entendida pelo computador como “4 + 15”, o que resultaria no valor 19.<br>
Outra possibilidade seria escrever esta mesma expressão como “(4 + 5) * 3”, que daria o valor 27, proveniente de (9 * 3). Sendo assim, já percebemos que os parênteses têm prioridade na ordem de execução. Para este fim, é definida uma prioridade entre os operadores, na seguinte ordem:

| **Ordem** | **Operador** |
| ------------- | ------------- |
| **1** | Parênteses ( ) |
| **2** | Raiz sqrt( ) e Potência pow( ) |
| **3** | Multiplicação *, Divisão /  e Resto % |
| **4** | Adição +  e Subtração - |

No caso de operadores com a mesma ordem de precedência, o computador executa primeiro as operações mais à esquerda. Desta forma, teríamos os seguintes resultados para as expressões abaixo:

| **Expressão** | **Como é interpretado** | **Saída** |
| ------------- | ------------- | ------------- |
| **3 + 2 * 5** | 3 + (2 * 5) | 13 |
| **(3 + 2) * 5** | (3 + 2) * 5 | 25 |
| **3 + 2 - 1** | (3 + 2) - 1 | 4 |
| **2 – 3 * 4** | 2 – (3 * 4) | -10 |
| **3 + 2 * pow(3,2)** | 3 + (2 *(pow(3,2))) | 21 |

Veja que podemos utilizar parênteses, como na expressão “(3 + 2) * 5”, para alterar a ordem em que o computador executa as operações. Isso se dá pelo motivo de que os parênteses tem a maior precedência entre os operadores.

---

## OPERAÇÕES LÓGICAS

Operadores lógicos também chamados de booleanos (Bool), possuem dois valores possíveis, TRUE (verdadeiro) ou FALSE (falso), e ao serem combinados com operadores geram equações com saída deste mesmo tipo, verdadeiras e falsas. Os operadores que podemos usar são: ***NOT*** **( ! ),** ***AND*** **( && )** e ***OR*** **( || )**.

O operador **NOT ( ! )** inverte o valor à sua direita, ou seja, ele nega (inverte) o valor. Sendo assim, vemos abaixo as 2 possíveis operações:

| **Operação** | **Saída** |
| ------------- | ------------- |
| ***!true*** | Nosso resultado é ***false*** |
| ***!false*** | Nosso resultado é ***true*** |

**Exemplos:**

```
var resultado: Bool

resultado = !true

print("O resultado de !true é \(resultado)") 

resultado = !false

print("O resultado de !false é \(resultado)") 
```

**Saída**

```
O resultado de !true é false
O resultado de !false é true
```

Já o operador **AND** ( **&&** ) assume um valor verdadeiro (**true**) apenas se os seus dois operandos tiverem valores verdadeiros. Temos 4 possibilidades, como descreve a tabela abaixo:

| **Operação** | **Saída** |
| ------------- | ------------- |
| ***true*** && ***true*** | Nosso resultado é ***true*** |
| ***false*** && ***true*** | Nosso resultado é ***false*** |
| ***true*** && ***false*** | Nosso resultado é ***false*** |
| ***false*** && ***false*** | Nosso resultado é ***false*** |

**Exemplos:**

```
var resultado: Bool

resultado = true && true

print("O resultado de true && true é \(resultado)") 

resultado = true && false

print("O resultado de true && false é \(resultado)") 

resultado = false && true

print("O resultado de false && true é \(resultado)") 

resultado = false && false

print("O resultado de false && false é \(resultado)") 
```

**Saída**

```
O resultado de true && true é true
O resultado de true && false é false
O resultado de false && true é false
O resultado de false && false é false
```

O operador **OR** ( **||** ) assume um valor verdadeiro (**true**) se um de seus dois operandos tiver valor verdadeiro, como na tabela abaixo:

| **Operação** | **Saída** |
| ------------- | ------------- |
| ***true*** **\|\|** ***true*** | Nosso resultado é ***true*** |
| ***false*** **\|\|** ***true*** | Nosso resultado é ***true*** |
| ***true*** **\|\|** ***false*** | Nosso resultado é ***true*** |
| ***false*** **\|\|** ***false*** | Nosso resultado é ***false*** |

**Exemplos:**

```
var resultado: Bool

resultado = true || true

print("O resultado de true || true é \(resultado)") 

resultado = true || false

print("O resultado de true || false é \(resultado)") 

resultado = false || true

print("O resultado de false || true é \(resultado)") 

resultado = false || false

print("O resultado de false || false é \(resultado)") 
```

**Saída**

```
O resultado de true || true é true
O resultado de true || false é true
O resultado de false || true é true
O resultado de false || false é false
```

Assim como os operadores aritméticos, os operadores lógicos também seguem uma regra de precedência:

| **Ordem** | **Operador** |
| ------------- | ------------- |
| **1** | Parênteses **( )** |
| **2** | ***NOT*** ! |
| **3** | ***AND*** && |
| **4** | ***OR*** \|\| |

Com os operadores aritméticos, devemos primeiramente resolver as operações com o operador de maior precedência. Temos assim, os seguintes valores para as expressões abaixo:

| **Expressão** | **Como é interpretada** | **Saída** |
| ------------- | ------------- | ------------- |
| **true \|\| true && false** | true \|\| (true && false) | true |
| **true && (true \|\| false)** | true && (true \|\| false) | true |
| **true && (!true \|\| false)** | true && (!true \|\| false) | false |
| **false \|\| false \|\| true** | (false \|\| false) \|\| true | true |
| **true && false && true** | (true && false) && true | false |

Podemos também utilizar variáveis lógicas no lugar das expressões ***true*** ou ***false,*** como por exemplo, x e y. A seguir, mostramos alguns exemplos de uso de expressões lógicas no corpo de um programa (lembrando sempre que as variáveis devem ser declaradas, apropriadamente, como Bool).

**Exemplos:**

```
var x, y, resultado: Bool

x = true
y = false

resultado = x || y

print("O resultado de \(x) || \(y) é \(resultado)") 

resultado = !x

print("O resultado de !x é \(resultado)") 

resultado = !y && x

print("O resultado de !y && x é \(resultado)") 

resultado = false || false

print("O resultado de false && false é \(resultado)") 
```

**Saída**

```
O resultado de true || false é true
O resultado de !x é false
O resultado de !y && x é true
O resultado de false && false é false
```

---

## OPERADORES DE COMPARAÇÃO

Operações de comparação atuam sobre dois operandos de mesmo tipo e retornam um valor lógico. São usados quando precisamos determinar a relação entre os dois operandos. Os comandos de comparação que podemos utilizar são:

| **Operador** | **Como é interpretada** |
| ------------- | ------------- |
| **==** | É utilizado para verificar igualdade. |
| **!=** | É utilizado para verificar desigualdade (diferente). |
| **<** | É utilizado para verificar se um operando é menor que. |
| **>** | É utilizado para verificar se um operando é maior que. |
| **<=** | É utilizado para verificar se um operando é menor ou igual a. |
| **>=** | É utilizado para verificar se um operando é maior ou igual a. |

**Exemplos:**

```
var salarioJoao, salarioPedro, salarioMarcos: Double
var resultado: Bool

salarioJoao = 1300

salarioPedro = 1000

salarioMarcos = 1000

/**************       JOAO X PEDRO            ********************/
resultado = salarioJoao == salarioPedro
print ("o salario do João é igual o salário do Pedro? \(resultado)")

resultado = salarioJoao != salarioPedro
print ("o salario do João é diferente do salário do Pedro? \(resultado)")

resultado = salarioJoao > salarioPedro
print ("o salario do João é maior que salário do Pedro? \(resultado)")

resultado = salarioJoao < salarioPedro
print ("o salario do João é menor que salário do Pedro? \(resultado)")

resultado = salarioJoao <= salarioPedro
print ("o salario do João é menor ou igual o salário do Pedro? \(resultado)")

resultado = salarioJoao >= salarioPedro
print ("o salario do João é maior ou igual o salário do Pedro? \(resultado)")

/**************        PEDRO x MARCOS           ********************/
resultado = salarioPedro <= salarioMarcos
print ("o salario do Pedro é menor ou igual o salário do Marcos? \(resultado)")

resultado = salarioPedro >= salarioMarcos
print ("o salario do Pedro é maior ou igual o salário do Marcos? \(resultado)")
```

**Saída**

```
o salario do João é igual o salário do Pedro? false
o salario do João é diferente do salário do Pedro? true
o salario do João é maior que salário do Pedro? true
o salario do João é menor que salário do Pedro? false
o salario do João é menor ou igual o salário do Pedro? false
o salario do João é maior ou igual o salário do Pedro? true
o salario do Pedro é menor ou igual o salário do Marcos? true
o salario do Pedro é maior ou igual o salário do Marcos? true
```

Não é necessário estabelecer uma ordem de precedência entre estes operadores, porque não conseguimos encadear mais de um operador de comparação por vez. Porém, como o resultado de uma operação de comparação é um valor lógico, podemos utilizá-lo no meio de uma expressão lógica. Neste caso, os operadores de comparação têm precedência sobre os operadores lógicos.<br>
Um exemplo disto é a expressão ***“5 < 2 && true”.*** Esta expressão é entendida pelo computador como ***“(5 < 2) && true”.*** Sabemos que 5 é maior que 2, então, a expressão ***“5 < 2”*** resulta em ***false***, logo, ***“false && true”*** resulta em ***false.***<br>
**Vejamos mais exemplos:**

```
print(1 > 2)

print(1 == 2)

print(1 != 2)

print(1 <= 2 && false) //true && false

print(1 < 2 && true) //true && true

print(2 < 2 || true) //false || true

print(2 <= 2 && true) //true && true
```

**Saída**

```
false
false
true
false
true
true
true
```

---

# COMANDOS DE DECISÃO

## COMANDO IF

Às vezes precisamos executar uma ação somente se uma condição for verdadeira, no ***Swift*** isso é representado pela instrução ***if.*** Você informa uma condição pro ***Swift*** verificar e um trecho de código a ser executado caso a condição seja válida.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/2._Comandos_de_Decisao_-_01.png" width = 400>

Vamos exemplificar e aprender a sintaxe do comando **if** :

Sintaxe:

```
if  condicao  {

    //Código a ser executado caso a condição seja verdadeira

}
```

```
var estaSol: Bool = true

if estaSol {
  print("O sol está visível")  
}
```

**Saída**

```
O sol está visível
```

No nosso exemplo nossa mensagem só é impressa porque **nossa condição é verdadeira**. No **if** podemos utilizar operadores lógicos e aritméticos. Para ambos a regra é a mesma, se a expressão for verdadeira, o trecho de código daquele **if** será executado. Vamos a mais alguns exemplos pra fixação da sintaxe:

```
var estaSol: Bool = true
var estaChovendo: Bool = true
var estaNublado: Bool = false
var descricaoTempo: String = "Ensolarado"

if estaSol {
  print("O sol está visível")  
}

//Operador AND
if  estaSol && estaChovendo {
  print("Chuva & Sol...")  
}

//Operador NOT
if !estaNublado {
  print("Opa, parece que está nublado sim! - Nesse caso o estaNublado (false), foi negado.")  
}

//Operador OR
if estaSol || estaChovendo {
  print("Opa, parece que está sol ou está chovendo")  
}

//Comparações
if 5 > 1 {
  print("Sim! Cinco é maior que um.")  
}

//Comparações
if descricaoTempo == "Ensolarado" {
  print("Sim! O tempo está ensolarado.")  
}
```

**Saída**

```
O sol está visível
Chuva & Sol...
Opa, parece que está nublado sim! - Nesse caso o estaNublado (false), foi negado.
Opa, parece que está sol ou está chovendo
Sim! Cinco é maior que um.
Sim! O tempo está ensolarado.
```

Apenas como exemplo, vejamos algumas condições falsas:

```
var estaSol: Bool = false
var estaChovendo: Bool = false
var estaNublado: Bool = true
var descricaoTempo: String = "Chuvoso"

if estaSol {
  print("O sol está visível")  
}

//Operador AND
if estaSol && estaChovendo {
  print("Chuva & Sol...")  
}

//Operador OR
if estaSol || estaChovendo {
  print("Opa, parece que está sol ou está chovendo")  
}

//Comparações
if 5 > 10 {
  print("Sim! Cinco é maior que dez.")  
}

//Comparações
if descricaoTempo == "Ensolarado" {
  print("Sim! O tempo está ensolarado.")  
}
```

Nada foi impresso pois nossas condições não eram verdadeiras, mas isso também pode ser útil não pode? Vamos conhecer o comando que complementa o nosso **if**, o **else**.

---

## COMANDO IF-ELSE

Opcionalmente podemos adicionar um segundo bloco chamado de **else**, este será encarregado de nos prover um bloco que só será executado caso a **nossa condição não seja verdadeira**. No exemplo abaixo sairíamos pelo fluxo false na condicional.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/2._Comandos_de_Decisao_-_02.png" width = 400>

Sintaxe:

```
if condicao {

    //Código a ser executado caso a condição seja verdadeira

} else {

    //Código a ser executado caso a condição não seja verdadeira

}
```

```
var estaSol: Bool = false

if estaSol {
  print("O sol está visível")  
}else{
    print("O sol não está visível")  
}
```

**Saída**

```
O sol não está visível
```

Vamos ver mais exemplos com diferentes expressões condicionais:

```
var estaSol: Bool = false
var estaChovendo: Bool = false
var estaNublado: Bool = true
var descricaoTempo: String = "Chuvoso"

if estaSol {
    print("O sol está visível")  
}else{
    print("O sol não está visível")  
}

//Operador AND
if estaSol && estaChovendo {
    print("Chuva & Sol...")  
} else {
    print("Não temos Chuva & Sol hoje :(") 
}

//Operador OR
if estaSol || estaChovendo {
    print("Opa, parece que está sol ou está chovendo")  
} else {
    print("Opa, parece que não está sol ou não está chovendo")      
}

//Comparações
if 5 > 10 {
    print("Com essa condição nunca entraremos aqui não é mesmo? ")  
} else {
    print("Não! Cinco não é maior que dez.")  
}

//Comparações
if descricaoTempo == "Ensolarado" {
    print("Sim! O tempo está ensolarado.")  
} else {
    print("Não o tempo não está Ensolarado hoje! O tempo está \(descricaoTempo).")  
}
```

**Saída**

```
O sol não está visível
Não temos Chuva & Sol hoje :(
Opa, parece que não está sol ou não está chovendo
Não! Cinco não é maior que dez.
Não o tempo não está Ensolarado hoje! O tempo está Chuvoso.
```

**Vamos treinar?**

Crie uma constante com o valor de *pi*π (3,14), e uma variável com um valor a ser definido por você, e compare-as utilizando ***IF-ELSE***, as mensagens de saída deverão conter as seguintes mensagens respectivamente: “Este número é menor que *pi*” ou “Este número é maior ou igual a *pi*”.

**<a href="./Códigos/main06.swift">Código</a>**

Resolução:

```
/*Crie uma constante com o valor de pi π (3,14), e uma variável com um valor 
a ser definido por você, e compare-as utilizando IF-ELSE, 
as mensagens de saída deverão conter as seguintes mensagens respectivamente: 
“Este número é menor que pi” ou “Este número é maior ou igual a pi”.*/

let pi: Double = 3.14

var numero: Double = 3

if numero < pi {
    print("Este número é menor que pi"  )    
} else {
    print("Este número é maior ou igual a pi")    
}
```

**Saída**

```
Este número é menor que pi
```

**💡Poderíamos utilizar inferência de tipo ( ***let pi = 3.14*** ) ao invés de informar o tipo para ambas as variáveis! Mas e aí, lembraram de utilizar ponto e não virgula na hora de informar os decimais?!**

---

## COMANDO IF - ELSE IF - ELSE

Isso ainda pode ficar mais interessante! E se quisermos testar mais de uma condição? No nosso cenário anterior sempre será executado um dos dois trechos, mas poderíamos testar mais uma condição dentro de um bloco true, ou de um bloco false (sim, é permitido encadear ***if***). Vamos ver como ficaria?

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/2._Comandos_de_Decisao_-_03.png" width = 400>

No exemplo acima temos um controle de idade, a partir de 18 podem entrar, a partir de 16 entram acompanhados de um responsável, e abaixo disso o acesso é negado, vamos ver no Swift?

```
var idade: Int = 16

if idade >= 16 {
    if idade > 18 {
        print ("Acesso permitido")
    }else{
        print ("Acesso permitido com responsável")
    }
} else{
    print ("Acesso negado")
}
```

**Saída**

```
Acesso permitido com responsável
```

Tudo tranquilo né? Vamos trabalhar com temperaturas e aprender mais uma possibilidade, para agregar ainda mais nossos conhecimentos sobre **condicionais**? Olhem o exemplo abaixo:

```
var temp = 13

if temp <= 12 {
    print("Está muito frio")
} else {
    print("Oba deu praia!")
}
```

**Saída**

```
Oba deu praia!
```

Como nosso código só verifica uma condição, da forma que foi estruturado ele nos diz que deu praia, com 13 graus? Meio frio né? E se pudéssemos tratar diferentes faixas de temperatura? Vamos conhecer o ***else if***, ele funciona também dentro da estrutura padrão do ***if***, vejamos:

Sintaxe:

```
if condicao {

    //Código a ser executado caso a primeira condição seja verdadeira

} else if condicao {

    //Código a ser executado caso a segunda condição seja verdadeira

} else {

    //Código a ser executado caso nenhuma condição não seja verdadeira
}
```

```
var temp = 13

if temp <= 12 {
    print("Está muito frio")
} else if temp <= 20 {
    print("Acho que podemos pegar o casaco!")
} else {
    print("Oba deu praia!")
}
```

**Saída**

```
Acho que podemos pegar o casaco!
```

Agora sabemos como adicionar mais condicionais no nosso **if**!

Vamos exercitar:

Crie uma condicional que trate o seguinte cenário:

Idade menor que 3 a saída deve ser “Um bebê”

Idade de 3 a 10 a saída deve ser “Uma criança”

Idade de 11 a 17 saída deve ser “Um adolescente”

Qualquer outra idade deve ser “Um adulto”

Bom treino!

**<a href="./Códigos/main07.swift">Código</a>**

Resolução:

```

/*
Idade menor que 3 a saída deve ser “Um bebê”
Idade de 3 a 12 a saída deve ser “Uma criança”
Idade de 13 a 17 saída deve ser “Um adolescente”
Qualquer outra idade deve ser “Um adulto”
*/
var idade:Int = 14

if idade < 3 {
    print ("Um bebê")
} else if idade >= 3 && idade <= 12 {
    print ("Uma criança")
} else if idade >= 13 && idade <= 17 {
    print ("Um adolescente")
} else {
    print ("Um adulto")
}
```

**Saída**

```
Um adolescente
```

---

## COMANDO SWITCH

O ***switch*** é uma forma de não entrarmos em grandes estruturas de ***if*** encadeadas e complexas. Ou seja, a lógica é a mesma do ***if***, diante de uma condição faça algo, mas o que o diferencia e possibilita que seja menos complexo? Vamos a sintaxe e alguns exemplos:

```
switch variavel/constante {

    case condicao1 :

        //Código a ser executado caso condicao1 seja verdadeira (No caso a condição padrão é ==, ou seja, ele irá comparar os dois valores)

    case condicao2 :

        //Código a ser executado caso condicao2 seja verdadeira (No caso a condição padrão é ==, ou seja, ele irá comparar os dois valores)

    default :

        //Código a ser executado caso nenhuma condicao1 seja verdadeira
}
```

**💡 Podemos adicionar quantos cases forem necessários!**

Vejam os 2 exemplos a seguir:

```
let num = 8
 
switch num {
case 0:
    print("Num tem o valor 0")
case 1:
    print("Num tem o valor 1")
default:
    print("Num tem outro valor diferente de 0 e 1")
}
```

**Saída**

```
Num tem outro valor diferente de 0 e 1
```

```
let favoriteColor = "black"
 
switch favoriteColor {
case "blue":
    print("minha cor predileta é Azul")
case "black":
    print("minha cor predileta é Preto")
case "red":
    print("minha cor predileta é Vermelho")
default:
    print("Não temos registro pra cor informada.")
}
```

**Saída**

```
minha cor predileta é Preto
```

Então com um apenas um ***switch*** podemos verificar quantas condições quisermos para um valor informado no início dele. 

**💡 Uma vez encontrado um valor correspondente ele saí da estrutura e não faz mais nenhuma verificação.**

Vamos treinar? Faça um caixa eletrônico!  Vamos fazer um depósito, crie um ***switch*** que imprima qual nota foi inserida, sua variável pode ser uma ***String*** ou um ***Int***.

**<a href="./Códigos/main08.swift">Código</a>**

Resolução:

```
var nota = 3

switch nota {
case 1:
    print("Nota de 1 real")
case 2:
    print("Nota de 2 reais")
case 5:
    print("Nota de 5 reais")
case 10:
    print("Nota de 10 reais")
case 20:
    print("Nota de 20 reais")
case 50:
    print("Nota de 50 reais")
case 100:
    print("Nota de 100 reais")
default:
    print("Nota inválida")
}
```

**Saída**

```
Nota inválida
```

Vamos aprender novos operadores? Vamos ver no próximo exemplo operadores de intervalo!

```
let reais = 10
 
switch reais {
case 0..<5:
    print("O preço está entre 0 e 4 reais.")
case 5...10:
    print("O preço está entre 5 reais e 10 reais.")
default:
    print("O preço é maior que 10 reais.")
}
```

**Saída**

```
O preço está entre 5 reais e 10 reais.
```

Agora que já virão aplicado vamos às definições:

| **Operador** | **Operação** |
| ------------- | ------------- |
| **A..<B** | É utilizado para definir um intervalo entre um numero A e B excluindo B. |
| **A...B** | É utilizado para definir um intervalo entre um numero A e B incluindo B. |

**Exemplos:**

2 ..< 8 - Está entre 2 e 7

0 ... 100 - Está entre 0 e 100

**💡 Iremos utilizar esses operadores nos próximos módulos!**

**Vamos treinar:**

Crie um switch que trate os seguintes casos e imprima a mensagem correspondente:

**Porcentagem seja 0** - “Insatisfatório, não acertou nenhuma questão.”

**Porcentagem esteja entre 1 e 20 (Incluindo 20)** - “Insatisfatório, desempenho muito baixo.”

**Porcentagem esteja entre 21 e 50 (excluindo 50)** - “Insatisfatório, vamos estudar mais?”

**Porcentagem esteja entre 50 e 70 (excluindo 70)** - “Foi por pouco, vamos estudar mais!”

**Porcentagem esteja entre 70 e 90 (excluindo 90)** - “Satisfatório, você foi aprovado!”

**Outros casos** - “Excelente, desempenho memorável!”

**<a href="./Códigos/main09.swift">Código</a>**

Bom treino!

Resolução:

```
/*
Crie um switch que trate os seguintes casos e imprima a mensagem correspondente:
Porcentagem seja 0 - “Insatisfatório, não acertou nenhuma questão.”
Porcentagem esteja entre 1 e 20 (Incluindo 20) - “Insatisfatório, desempenho muito baixo.”
Porcentagem esteja entre 21 e 50 (excluindo 50) - “Insatisfatório, vamos estudar mais?”
Porcentagem esteja entre 50 e 70 (excluindo 70) - “Foi por pouco, vamos estudar mais!”
Porcentagem esteja entre 70 e 90 (excluindo 90) - “Satisfatório, você foi aprovado!”
Outros casos - “Excelente, desempenho memorável!”
*/

var porcentagem: Double = 70
 
switch porcentagem {
case 0:
    print("O preço está entre 0 e 4 reais.")
case 1...20:
    print("Insatisfatório, desempenho muito baixo.")
case 21..<50:
    print("Insatisfatório, vamos estudar mais?")
case 50..<70:
    print("Foi por pouco, vamos estudar mais!")
case 70..<90:
    print("Satisfatório, você foi aprovado!")
default:
    print("Excelente, desempenho memorável!")
}
```

**Saída**

```
Satisfatório, você foi aprovado!
```

---

# COMANDOS DE REPETIÇÃO

## INTRODUÇÃO

Comandos de repetição são úteis quando desejamos fazer operações repetitivas, sem escrever diversas vezes o mesmo código. Isto se torna ainda mais importante quando não sabemos, na hora em que estamos desenvolvendo, quantas vezes este comando precisará ser repetido. Para solucionar esses empecilhos e aumentar a qualidade do código, vamos entender os comandos ***WHILE, REPEAT-WHILE*** e ***FOR***.

---

## COMANDO WHILE

O comando ***while*** repete um conjunto de operações enquanto uma condição for verdadeira. Sua sintaxe é a seguinte:

```
while condicao {
    //Comandos a serem executados em todas repetições enquanto a condição for verdadeira
}
```

Exemplos:

```
var numero = 1
var menorQueCinco = true
 
while menorQueCinco {
    if numero < 5{
        print("o número \(numero) é menor que 5")
    }else{
        menorQueCinco = false
    }
    numero += 1 //Essa linha é igual a escrever numero = numero + 1
}
```

**Saída**

```
o número 1 é menor que 5
o número 2 é menor que 5
o número 3 é menor que 5
o número 4 é menor que 5
```

Ou seja, executamos 4 vezes o comando ***print()***, mesmo ele sendo escrito uma única vez, e colocamos nossa condição como false utilizando o ***else***, fazendo com que nosso laço pare de ser executado assim que a condição passa a ser falsa.

**💡 Também podemos utilizar a palavra reservada break para parar a execução de um laço.**

Vejamos o uso do break a partir do mesmo exemplo:

```
var numero = 1
var menorQueCinco = true
 
while menorQueCinco {
    if numero < 5{
        print("o número \(numero) é menor que 5")
    }else{
       break
    }
    numero += 1 //Essa linha é igual a escrever numero = numero + 1
}
```

**Saída**

```
o número 1 é menor que 5
o número 2 é menor que 5
o número 3 é menor que 5
o número 4 é menor que 5
```

Ou seja, assim que a condição do if passa a ser falsa, o comando break é executado no else, e faz nosso laço parar.

É importante lembrar que, caso nossa condição do while seja falsa já no início, **nada será executado**. Por exemplo:

```
var x = 5
var y = 5
 
while x < y {
    print("x é menor que y")
}
```

**Vamos treinar?**

Construa um contador que imprima os números até 512.

**<a href="./Códigos/main10.swift">Código</a>**

Resolução:

```
//Construa um contador que imprima os números até 512.

var contador = 0

while contador <= 512 {
    print(contador)
    contador += 1 // o mesmo que escrever contador = contador + 1
}
```

**Saída**

```
0
1
2
...
512
```

---

## COMANDO REPEAT-WHILE

O comando ***repeat-while*** é uma variação do **while** cuja a condição só é verificada após a primeira execução dos comandos nele contidos. Vamos à sintaxe e em seguida, a uma comparação com o **while**:

```
repeat {
    //Comandos a serem executados pelo menos uma vez e posteriormente em todas repetições em que a condição for verdadeira
} while condicao
```

Comparação:

```
var x = 5
var y = 5
 
while x != y {
    print("x é diferente de y")
}
 
repeat {
    print("Mesmo sem validar a condição será executado ao menos uma vez")
} while x != y
```

**Saída**

```
Mesmo sem validar a condição será executado ao menos uma vez
```

Com a mesma condição, o nosso ***repeat-while*** imprimiu sua mensagem enquanto o ***while*** não.

Vamos ver mais um exemplo de uso:

```
var numero = 0

repeat {
   print("O número atual é \(numero)")
   numero += 1
} while (numero < 5);


/********** Condição falsa *********/ 
print("Condição falsa")

var numero2 = 120

repeat {
   print("O número atual é \(numero2)")
   numero2 += 1
} while (numero2 < 0);
```

**Saída**

```
O número atual é 0
O número atual é 1
O número atual é 2
O número atual é 3
O número atual é 4
Condição falsa
O número atual é 120
```

Vimos que no primeiro exemplo tivemos 5 mensagens impressas no primeiro bloco, com uma condição válida. Já o segundo exemplo está com uma condição falsa, mas ainda assim, imprime a sua primeira mensagem. Essa estrutura pode vir a ser útil dependendo do que estiver fazendo e do cenário que se está trabalhando.

---

## COMANDO FOR

Como vimos anteriormente, esse capítulo nos ensina a não repetirmos muitas vezes a mesma ação de forma manual, correto? Podemos, então, criar laços de repetição (*loops*) que irão trabalhar por nós (maravilhoso, não?), vamos conhecer agora o comando *for*. Vejamos a sintaxe:

```
For variavel in contador {
    //Comando a ser executado em todas repetições até que acabe o contador definido
}
```

E agora um exemplo básico para começarmos a nos familiarizar com o ***for***.

```
//Bom dia 5x

for i in 1...5 {
    print("Bom dia")
}
```

**Saída**

```
Bom dia
Bom dia
Bom dia
Bom dia
Bom dia
```

O “Bom dia” foi impresso 5 vezes porque nosso contador é um intervalo de 1 até 5.

**💡 Aprendemos sobre os operadores de limite no capítulo de Controle de Fluxo e os mesmos serão utilizados aqui. Recapitulando:**

| **Operador** | **Operação** |
| ------------- | ------------- |
| **A..<B** | É utilizado para definir um intervalo entre um numero A e B excluindo B. |
| **A...B** | É utilizado para definir um intervalo entre um numero A e B incluindo B. |

Vamos avançar mais um pouco e imaginar que precisamos imprimir tabuadas. Uma das possibilidades seria gerar 10 ***prints()***, correto?

```
// Tabuada do 6

print("6 x 1 = \(6 * 1)")
print("6 x 2 = \(6 * 2)")
print("6 x 3 = \(6 * 3)")
print("6 x 4 = \(6 * 4)")
print("6 x 5 = \(6 * 5)")
print("6 x 6 = \(6 * 6)")
print("6 x 7 = \(6 * 7)")
print("6 x 8 = \(6 * 8)")
print("6 x 9 = \(6 * 9)")
print("6 x 10 = \(6 * 10)")
```

**Saída**

```
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
```

E de fato funcionaria, mas vamos aprender uma nova forma de fazer isso? Para que seja mais eficiente e processado pela máquina solucionando as linhas repetitivas que foram criadas de forma manual, utilizaremos o ***for***.

```
//Tabuada do 6

for i in 1...10 {
    print(" 6 x \(i) = \(6 * i)")
}
```

**Saída**

```
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
```

Explicando, ***i*** é criada em tempo de execução, ou seja, não precisamos declará-la manualmente e ela recebe um valor a cada vez que passamos por essa linha, ou seja:

- Da primeira vez ela tem o valor 1, pois nosso limite é de 1...10

- Da segunda vez ela tem o valor 2, pois já executou os comandos para o valor 1 e assumiu o próximo valor do limite, e assim sucessivamente até que...

- Na última vez ela assume o valor 10, executa todos os comandos e sai desse laço de repetição.

Vamos agora entender isso da ótica dos nossos comandos:

A cada vez que entramos na fase de executar os comandos, a nossa constante ***i*** está com um novo valor, correto? Então é só combinar esse valor com o que queremos fazer e conseguimos partir de um cenário de 10 linhas de ***print()*** pra um novo, com apenas 3 linhas!

Vamos olhar de novo e escrever mais algumas tabuadas:

Escrevam a tabuada do 1 ao 10, abaixo dessa:

**<a href="./Códigos/main11.swift">Código</a>**

Já pensou na possibilidade de não fazer o trabalho de forma manual? 

```
//Tabuada do 6

for i in 1...10 {
    for j in 1...10 {
        print(" \(i) x \(j)  = \(j * i)")
    }
    print("_________________________")
}
```

**Saída**

```
1 x 1  = 1
1 x 2  = 2
1 x 3  = 3
1 x 4  = 4
1 x 5  = 5
1 x 6  = 6
1 x 7  = 7
1 x 8  = 8
1 x 9  = 9
1 x 10  = 10
_________________________
2 x 1  = 2
2 x 2  = 4
...
10 x 10  = 100
_________________________
```

Podemos criar um ***for*** dentro de outro ***for*** e diminuir ainda mais a escrita de código, só com a ressalva de que precisamos trocar o nome do nosso iterador, normalmente utilizamos ***i, j, k*** para referenciar nossos iteradores nos laços, mas nada impede que você atribua algum outro nome.

---

# FUNÇÕES

### INTRODUÇÃO

A função nos permite agrupar comandos (instruções) e tem por objetivo resolver um problema ou realizar uma ação. Podemos executá-la quantas vezes for necessário.

**Exemplo:**

```
func primeiraFuncao() {
    print("Essa é minha primeira função")
}
```

Para executar uma tarefa cotidiana, como chupar uma bala, repetimos uma determinada sequência de passos. Uma vez aprendida, essa sequência é executada de forma tão automática que nem reparamos. Podemos representar isso com um conjunto de instruções:

1- pegarBala( )

2- abrirBala( )

3- levarABoca( )

Em nosso exemplo iremos criar a função ***chuparBala( )*** que agrupa todos esses comandos:

```
func chuparBala() {
    pegarBala()
    abrirBala()
    porNaBoca()
}
```

Nela agrupamos todos os nossos comandos em uma função e ela será executada somente quando chamarmos a função ***chuparBala( )***.

**Note que não conseguiremos executar o código acima em nosso simulador, pois nossos 3 comandos não foram definidos.**

Para definir uma função utilizaremos o prefixo **func**, após ele, um nome seguido de ( ) e por fim { } que engloba todo o código contido na função. Veja o exemplo de uma função básica em Swift:

```
func corPredileta() {
    print("Minha cor predileta é laranja")
}
```

No nosso simulador vemos que nada foi impresso, e isso está correto! O motivo é simples, apenas criamos a função ***corPredileta( )*** com o comando print( ) mas não a executamos, isso só ocorrerá quando digitarmos ***corPredileta( )***, e isso denomina-se **chamar a função** e assim os comandos dentro dela serão executados.

```
func corPredileta() {
    print("Minha cor predileta é laranja")
}

corPredileta()
```

**Saída**

```
Minha cor predileta é laranja
```

**Vamos praticar?**

Crie uma função que se chame ***nomeCompleto*** e imprima a frase “Meu nome completo é Monteiro de Sousa”. Em seguida chame sua função e confira a saída.

**💡 Para chamar uma função basta colocar seu nome seguido de parênteses. No exercício será: nomeCompleto()!**

**<a href="./Códigos/main12.swift">Código</a>**

Vamos conferir?

```
/* Crie uma função que se chame nomeCompleto 
e imprima a frase “Meu nome completo é Monteiro de Sousa”. 
Em seguida chame sua função e confira a saída.*/


func nomeCompleto(){
    print("Meu nome completo é Monteiro de Sousa")
}

nomeCompleto()
```

**Saída**

```
Meu nome completo é Monteiro de Sousa
```

Você ainda pode estar se perguntando se realmente compensa escrever funções com apenas uma linha de código, como as acima. Vejamos: imagine um cenário onde utilizemos essa linha em 5 diferentes pontos e se precisássemos alterar uma informação seria em... 5 locais! Se centralizamos e alteramos somente em nossa função, todos os locais que ela for utilizada serão atualizados.

Agora vamos continuar apreendo sobre funções, mais especificamente sobre **parametrização**.

---

## PARÂMETROS

Vamos tornar o nosso exemplo das cores mais completo? Para isso, temos um recurso chamado parâmetro, ele nos permite fornecer um valor de entrada que poderá ser utilizado no corpo da nossa função.

**Exemplo:**

```
func corPredileta(cor: String) {
    print("Minha cor predileta é \(cor)")
}

corPredileta(cor: "Azul")
```

**Saída**

```
Minha cor predileta é Azul
```

Interessante, não? Acabamos de dizer para o ***Swift*** que nossa função aceita valores externos e que, nesse caso, o parâmetro deve se chamar ***cor*** e ser do tipo **String**. Ele ficará responsável por transportar os nossos dados externos para o corpo da nossa função. É importante mencionar que uma função aceita múltiplos parâmetros, sempre seguindo o padrão “nome e tipo”, como vimos no exemplo acima, tornando nossa função mais **útil**. Com essa alteração, ou seja, com o uso de múltiplos parâmetros, podemos, por exemplo, chamar nossa função 3 vezes passando 3 valores diferentes para o nosso parâmetro. Vejamos:

```
func corPredileta(cor: String) {
    print("Minha cor predileta é \(cor)")
}

corPredileta(cor: "Azul")

corPredileta(cor: "Preto")

corPredileta(cor: "Rosa")
```

**Saída**

```
Minha cor predileta é Azul
Minha cor predileta é Preto
Minha cor predileta é Rosa
```

Com uma única função tivemos 3 saídas diferentes, uma para cada chamada.

**Vamos exercitar?**

Complete o código abaixo com uma função chamada ***imprimeNome*** que receba uma **String** nome e imprima “Meu nome é:” + o nome passado por parâmetro.

**<a href="./Códigos/main13.swift">Código</a>**

Conseguiu? Vamos à solução:

```
/* Crie uma função chamada imprimeNome 
que receba uma String nome, 
e imprima seu nome quando chamada. */
func imprimeNome(nome: String){
    print ("Meu nome é \(nome)")
    
}

imprimeNome(nome: "Paulo")
```

**Saída**

```
Meu nome é Paulo
```

Dissemos que poderíamos ter mais de um parâmetro, certo? Vamos criar novamente a nossa função ***nomeCompleto***, recebendo, via parâmetro, o **nome** e o **sobrenome**? Vejamos:

```
/* Crie uma função que se chame nomeCompleto 
e imprima a frase “Meu nome completo é" 
+ os valores recebidos por parâmetro.
Em seguida chame sua função e confira a saída.*/


func nomeCompleto(pNome: String, pSobrenome: String){
    print("Meu nome completo é \(pNome) \(pSobrenome)")
}

var nome: String = "Monteiro"
var sobrenome: String = "de Souza"

nomeCompleto(pNome: nome, pSobrenome: sobrenome)
```

**Saída**

```
Meu nome completo é Monteiro de Souza
```

Podemos utilizar valores que estavam em variáveis para atribuir valor aos nossos parâmetros! Até agora vimos parâmetros do tipo **String**. E se quisermos trabalhar com números?

```
func somaValores(valorA: Int, valorB: Int){
    var total: Int
    total = valorA + valorB
    
    print ("O total da soma de \(valorA) + \(valorB) é de \(total)")    
}

somaValores(valorA: 12, valorB: 3)
```

**Saída**

```
O total da soma de 12 + 3 é de 15
```

Viu que interessante? Nossa função soma qualquer valor inteiro.

Para exercitar, vamos criar uma função que receba 2 valores e imprima o resultado das 4 operações básicas?

```
func operacoesBasicas(valorA: Double, valorB: Double){
    var total: Double
    total = valorA + valorB
    
    print ("O total da soma de \(valorA) + \(valorB) é de \(total)")
    
    total = valorA - valorB
    print ("O total da subtração de \(valorA) - \(valorB) é de \(total)")
    
}
operacoesBasicas(valorA: 12, valorB: 3)
```

**Saída**

```
O total da soma de 12.0 + 3.0 é de 15.0
O total da subtração de 12.0 - 3.0 é de 9.0
```

Complete o exemplo acima com multiplicação e divisão.

**<a href="./Códigos/main14.swift">Código</a>**

---

## TIPO DE RETORNO

Até agora nossas funções não nos retornavam nada, apenas imprimiam um valor no nosso console. Vamos aprender a devolver dados tipados?

```
/* Crie uma função chamada imprimeNome 
que receba uma String nome, 
e imprima seu nome quando chamada. */
func imprimeNome(nome: String) -> String{
    return "Meu nome é \(nome)"
}

print(imprimeNome(nome: "Paulo"))
```

**Saída**

```
Meu nome é Paulo
```

Viram as diferenças? Adicionamos que o tipo do nosso retorno vai ser uma ***String***, e no corpo da função adicionamos apenas um ***return***. Ou seja, agora a nossa função passa a não imprimir mais um valor, mas sim ***retornar*** um valor após seu processamento.

**Vamos treinar um pouco?** Duas tarefas:

1) Uma soma entre 2 inteiros só pode resultar num inteiro, certo? Vamos escrever uma função que some dois valores e retorne um INT?

2) Uma função que receba 2 números e retorne o valor da divisão! (Se atente ao tipo de retorno que vai escolher).

**<a href="./Códigos/main15.swift">Código</a>**

Sem dar aquela espiadinha aqui hein?! Vamos às resoluções:

```
/********************* HORA DE PRATICAR *****************************/

/********************* Exercício 1 *****************************/
//1) Uma soma entre 2 inteiros só pode resultar num inteiro, certo? Vamos escrever uma função que some dois valores e retorne um INT:

func somar(a: Int, b: Int) -> Int {
    return a + b
}

print(somar(a: 4,  b: 3))

/********************* Exercício 2 *****************************/
//2) Uma função que receba 2 números e retorne o resultado da divisão! (Se atente ao tipo de retorno que vai escolher).
func dividir(a: Double, b: Double) -> Double {
    return a / b
}

print(dividir(a: 4,  b: 3))
```

**Saída**

```
7
1.3333333333333333
```

---

## RECURSÃO

Uma função que chama a si mesma é conhecida como função recursiva. Essa técnica é chamada de recursão. Ao criar uma função desse tipo, temos que criar uma condição de parada para que a função não vire um *loop* infinito. Como citado, essa maneira de escrever funções é uma possível alternativa aos tradicionais *loops*.

```
func recurse () { 
    // corpo da função
    recurse () 
} 
recurse ()
```

**💡 Se estiver usando um compilador externo podemos ter um warning avisando sobre o loop infinito para o exemplo acima, pois não implementamos a condição de parada!**

Vamos ver alguns exemplos de recursão e entender como funciona na prática:

```
func contagemRegressiva(numero: Int) {
    
    print(numero)

    if numero > 0 {
        contagemRegressiva(numero: numero - 1)
    }
}

print("Contagem Regressiva:")
contagemRegressiva(numero:3)
```

**Saída**

```
Contagem Regressiva:
3
2
1
0
```

No exemplo acima, conseguimos ver alguns pontos importantes: a chamada da própria função dentro dela (o que configura a recursão), e a condição de parada (numero > 0) para que não tenhamos um loop infinito. Para que seja executada, temos uma chamada simples passando apenas o nosso parâmetro, como já fizemos anteriormente. Mas vamos tentar ir mais a fundo nesse exemplo e ver como ele faz para concluir essa tarefa.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/4._Funcoes_-_01.png" width = 400>

Da forma que nosso código está escrito ele faz a impressão do valor atual, e se o valor atual for maior que zero, ele chama novamente a nossa função (dentro dela mesma), passando o valor atual menos 1, ou seja, isso será repetido até nossa condição de parada não validar mais o valor, e aí o ciclo se encerra. Como podemos ver na imagem acima, o código nos exemplifica a ordem, imprime o valor atual (3), subtrai 1 e chama novamente a função passando 2 como parâmetro e assim sucessivamente.

Esse é um exemplo bem básico e simples para que possamos entender de fato o mecanismo de recursão. Vamos agora fazer uma simples alteração no nosso código, movendo uma linha apenas para outro local e ver o comportamento do código. Foi alterado propositalmente o nome da função, pois a mesma terá um comportamento totalmente diferente. Se atente no corpo da função que alteraremos apenas a linha que imprime o nosso valor:

```
func contador(numero: Int) {
    
    if numero > 0 {
        contador(numero: numero - 1)
    }
    
    print(numero)
}

print("Contador:")
contador(numero:3)
```

**Saída**

```
Contador:
0
1
2
3
```

Por que isso ocorre? Olhando apenas para o código é possível interpretar e entender? É SIMPLES!

Quando chamamos a função de forma recursiva, qualquer linha posterior a chamada só será executada após o término da execução da função atual, e assim sucessivamente, ou seja, chegaremos na condição de parada e voltaremos executando o restante das linhas de todas funções. Assim, podemos dizer que a função é sequencialmente executada, de acordo com a ordem em que foi solicitada. Vamos observar a diferença:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/4._Funcoes_-_02.png" width = 400>

Dessa forma, conseguimos observar que a execução é feita da esquerda para a direita (seguindo a ordem na qual foram executadas as chamadas da função, sempre subtraindo um da variável número (seta vermelha), mas as impressões (e os retornos, como veremos a seguir), “são executados” da direita para a esquerda (em verde), dessa forma a chamada mais “interna” é a que nos permite continuar a executar o código de quem a chamou, e dessa forma, ele volta executando o restante das funções (setas verdes).

Vamos ver um exemplo de uma aplicação de recursão para resolução de um problema:

*“***Fatorial***  é um número natural inteiro positivo, o qual é representado por n! O ***fatorial***  de um número é calculado pela multiplicação desse número por todos os seus antecessores até chegar ao número 1.”*

```
func fatorial(num: Int) -> Int{

    if (num == 0 || num == 1){
        return 1
    }
    
    return (num * fatorial(num: num - 1))
}

print(fatorial(num: 4))
```

**Saída**

```
24
```

Veja que nossa função resolveu isso com apenas 4 linhas de corpo!!! Incrível, não? Vamos às explicações:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/4._Funcoes_-_03.png" width = 400>

riamos a função fatorial(*N*) onde *N* é um inteiro, a primeira verificação a ser feita é se o valor é 0 ou 1 para construir a nossa condição de parada, dessa forma evitando o *loop*, e garantindo a premissa do fatorial, já que foi afirmado na definição que *“***Fatorial*** é um número natural inteiro positivo”*. 0! e 1! tem como resultado 1. Feita a nossa condição de parada, vamos à parte mais interessante, onde, se o número não for nem 0 nem 1, chamaremos novamente a função fatorial(*N-1*) com *N-1*, e por *N-1* se entende que é o fatorial número atual decrementado de 1, e assim sucessivamente até chegarmos no 1, onde sabemos que o resultado é 1. Dessa forma, começamos novamente nossa leitura da direita para a esquerda, pois já temos os dois valores para concluir a multiplicação (o número que entrou via parâmetro na função + o retorno da que foi chamada subsequentemente). Novamente, voltamos executando todas as multiplicações até chegar no resultado do nosso fatorial de *N*. No exemplo acima tivemos:

fatorial(num: 1) retornou 1

fatorial(num: 2) retornou 2x1 = 2

fatorial(num: 3) retornou  3x2 = 6

fatorial(num: 4) retornou  4x6 = 24

Então concluímos que 4! É 24.

---