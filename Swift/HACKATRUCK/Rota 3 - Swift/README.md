# SINTAXE BÁSICA

## CONCEITOS INICIAIS

Você está iniciando o módulo sobre uma linguagem de programação consistente e intuitiva desenvolvida pela Apple: Swift!

Este módulo é importante para qualquer desenvolvedor que deseje trabalhar com os dispositivos da Apple, pois somente duas linguagens são oficialmente suportadas por ela: Objective-C e Swift. Ambas rodam sobre um conjunto de padrões e funcionalidades similares nos dispositivos com iOS, tvOS, watchOS ou MacOS. Swift é a mais nova dentre elas e está em evolução constante. Em seu lançamento foi definida como "Objective-C sem o C".

Este módulo será bastante prático! Sugerimos que caso você possua um MacBook, utilize o Xcode (IDE oficial da Apple) e o Swift 5 no Playground para rodar os exemplos e se exercitar como programador. Caso você não possua, não se preocupe! A maior parte dos exemplos funciona também em editores online de Swift. E neste módulo, assim como nos módulos de Lógica de Programação e Orientação a Objetos, utilizaremos o Paiza.io (https://paiza.io/en/projects/new?language=swift).

Você também pode procurar outras fontes de informação! Lembre-se que o bom profissional de computação deve saber pesquisar quando necessário! Use e abuse de buscas no Google, da documentação oficial da Apple e do Stackoverflow para se aprofundar na linguagem!

Nesse módulo vamos abordar alguns aspectos básicos da sintaxe do Swift. **Importante notar que neste curso utilizaremos sempre o *Swift* em sua versão 5**. Se quiser testar os exemplos de código por si só, recomendamos o uso dos editores online, onde existe uma infraestrutura similar ao Playground do Xcode do Mac, porém no seu navegador. Um Playground nada mais é do que um arquivo de código *Swift* onde cada linha é avaliada pelo compilador em tempo real e o resultado da computação de cada uma dessas linhas é mostrado ao programador após sua execução. Veremos alguns itens novos e revisaremos alguns outros pontos já abordados nos 2 primeiros módulos para que possamos avançar para os próximos capítulos.

---

## HELLO, WORLD!

Sempre que se fala de uma linguagem nova de programação é comum iniciar a explicação dando-se um exemplo de código de um programa que apenas imprime na tela a String *“Hello, World!”*. A sintaxe do Swift é tão enxuta e declarativa, que esse exemplo se reduz a:

```
print("Hello, World!")
```

**Saída**

```
Hello, World!
```

Repare que não é necessário importar nenhuma biblioteca para se ter acesso à função *print* que imprime um valor de uma *String* na tela. Além disso, note também que não é necessário utilizar um ponto e vírgula no final do comando. Imagine que o código *Swift* é executado de maneira global, ou seja, o código é chamado no momento que o fluxo de execução passar pelo comando.

Vamos treinar? Faça um print com seu nome!

**</a href="./Códigos/main01.swift">Código</a>**

---

## COMENTÁRIOS

Comentários são utilizados por programadores para facilitar o entendimento de seu código. As palavras contidas nos comentários são descartadas pelo compilador e servem somente para o desenvolvedor ou time de desenvolvedores produzirem um código que seja de mais fácil manutenção e legibilidade. Os comentários em *Swift* lembram os de C e Java. Existem em dois formatos principais: por linha ou em blocos. Vamos ver cada um deles.

Se desejamos comentar uma única linha, podemos utilizar o “//”, nesse caso o compilador desconsidera todo o trecho que vai do “//” até o final da linha, como no exemplo:

```
print("Hello, World!") // irá imprimir uma saudação
//print("Hello, World Comentado!")
```

**Saída**

```
Hello, World!
```

Existe também a possibilidade de um comentário em bloco que se inicia com a expressão “/*” e finaliza com a expressão “*/”, podendo até ser escrito por múltiplas linhas. Veja um exemplo:

```
print("Hello, World!") // irá imprimir uma saudação
/*print("Hello, World!") 

Multiplas linhas comentadas

print("Hello, World!") */
```

**Saída**

```
Hello, World!
```

---

## VARIÁVEIS E CONSTANTES

Duas palavras reservadas do *Swift* são essenciais quando queremos trabalhar com variáveis e constantes: ***var*** e ***let***. Ambas são utilizadas antes do nome da variável ou constante. A palavra reservada var define um valor que poderá mudar conforme o fluxo de execução avança, por sua vez, a palavra reservada let define um valor que não deverá mudar nunca com o fluxo de execução.

Na introdução do módulo foi dito que o Swift preza por ser uma linguagem segura, ou seja, na qual o compilador nos ajuda a evitar estados inconsistentes, além de otimizar o código compilado sempre que possível. Para se aproveitar desse recurso, sugerimos que, a não ser que estritamente necessário para sua lógica, você faça uso de constantes ao invés de variáveis sempre que possível, pois se o valor de uma variável nunca for ser alterado, ela deveria ser, por concepção, uma constante.

Exemplo de uso de var:

```
var quantidadeVariavel = 10 // esse valor é variável e pode ser modificado
quantidadeVariavel = 11 // aqui atualizamos o valor da variável
```

Exemplo com o uso de let:

```
let quantidadeConstante = 10
quantidadeConstante = 11 // ERRO de compilação!
```

O erro se dá porque não se pode modificar o valor de uma constante.

Outro fator interessante a se observar é que tanto variáveis como constantes, em *Swift*, são iniciadas com algum valor e que a tipagem, apesar de não explícita em muitos casos, existe. Não declaramos o tipo de nossas variáveis e nem o das constantes de maneira explícita, e mesmo assim não tivemos problemas de tipagem. Como é possível? Graças a um conceito que já vimos nos primeiros módulos e vamos rever a seguir, chamado de inferência de tipos.

---

# TIPAGEM

*Swift* tem as seguintes características no que diz respeito à tipagem: estática (com uso de inferência de tipos) e forte.

Por **tipagem estática**, entendemos que todas as variáveis e constantes devem ter seus tipos definidos antes de serem utilizadas, assim o compilador pode ajudar na checagem de erros ao compilar o programa. Além disso, não se pode mudar o tipo de uma variável em tempo de execução, como no erro a seguir:

```
/* dez é uma variável do tipo Int (graças à inferência) 
de tipos que veremos a seguir, portanto não pode receber
um valor do tipo String depois de declarada:*/
var dez = 10 
dez = "DEZ" // Erro!!
```

Por **inferência de tipo**, queremos dizer que o compilador de *Swift* faz o trabalho de declaração do tipo pelo programador (quando possível), com o objetivo de deixar o código mais legível e menos verboso. Por exemplo:

```
let umDouble = 2.0 // tipo inferido: Double
let umaString = "Uma String" // tipo inferido: String
let umInteiro =  1 // tipo inferido: Int
```

Apesar de não termos explicitamente escrito em nosso código que a primeira constante é do tipo *Double*, a segunda do tipo *String* e a terceira do tipo *Int*, o compilador fez esse trabalho por nós, garantindo a tipagem estática do *Swift*. Se por um acaso quiséssemos ser explícitos com relação ao tipo, ainda assim poderíamos fazê-lo:

```
let umDouble: Double = 2.0
let umaString: String = "Uma String"
let umInteiro: Int =  1
```

Neste último exemplo, fomos explícitos com relação ao tipo mesmo sem necessidade, porém imagine que queremos ter um *caractere* representado em uma constante, como no exemplo:

```
let letraA = "A" // ao invés de um Character, temos uma String aqui
```

Como o compilador vai utilizar a sua própria regra de inferência de tipos para deduzir o tipo da constante *letraA*, ele irá considerar o tipo *String* ao invés do tipo *Character* para essa constante. Se quisermos forçar o tipo nesse caso, devemos explicitá-lo em nosso código:

```
let letraA: Character = "A" // letraA é do tipo Character
```

Dessa forma, *letraA* é do tipo *Character* e é inicializado com o valor *“A”*. Outro caso comum de confusão com inferência de tipos é quando queremos trabalhar com *Float* ao invés de *Double*, como ilustra o exemplo:

```
// a inferência de tipos levará o compilador a considerar n 
// como uma constante Double
let n = 2.0 

// para forçar o compilador a entender o valor passado 
// na inicialização como Float, devemos explicitar o tipo
let m: Float = 2.0
```

Dizemos também que *Swift* tem **tipagem forte**, ou seja, sempre que se passa um valor ou variável como parâmetro de uma função, o compilador checará se os tipos esperados pela função serão satisfeitos.

```
func multiplicaInteiros(x: Int, y: Int) -> Int {
    return x * y
}

var resultadoUm  = multiplicaInteiros(x: 2, y: 3) // retorna 6

var resultadoDois  = multiplicaInteiros(x: 2, y: "3") // Erro!
```

No exemplo acima, utilizamos uma função para exemplificar a tipagem forte. Apenas entenda que declaramos a função *multiplicaInteiros( )* que recebe dois inteiros como parâmetro, os multiplica e retorna um outro inteiro que é o resultado desta multiplicação. Perceba também, que o compilador é capaz de aceitar que passemos os parâmetros *2* e *3* para essa função, mas não aceita os parâmetros *2* e *“3”*, já que aspas definem o valor como *String* e graças à tipagem forte, o compilador é capaz de checar que o tipo do parâmetro esperado pela função funcao(*Int*) é diferente do tipo da expressão *“3”* (*String*).

---

## OPCIONAIS

Perceba que até agora todas as nossas variáveis e constantes sempre tiveram um valor. Nunca trabalhamos com a ausência de valor, também conhecido como *nil* em *Swift* ou *null* em outras linguagens de programação. Como podemos trabalhar com esse tipo de dado em *Swift*? A resposta são os tipos opcionais.

Em *Swift* pode-se declarar uma variável com o uso de um sinal de interrogação (“?”) após o tipo para dizer ao compilador que ela irá aceitar o valor *nil* além de um valor do tipo especificado. Como no exemplo a seguir:

```
var inteiro:Int? = 1
inteiro = nil // podemos atribuir nil para a variável Int? (opcional inteira)
```

É interessante notar que se não forçamos o uso do tipo opcional, a variável nunca pode se tornar nula durante a execução, algo que será garantido em tempo de compilação:

```
var inteiro = 1
inteiro = nil // Erro! Variável não é opcional
```

Os opcionais são especialmente importantes para se lidar com retornos de funções, pois nem sempre é possível garantir que será passado um parâmetro que seja válido para a função conseguir retornar um valor também válido. Vejamos esse caso em um exemplo um pouco mais concreto:

```
// primeira forma de desempacotamento de opcionais:
let stringDeNumero1 = "1"
let numeroInteiro1 = Int(stringDeNumero1)
let somaDeInteiros = numeroInteiro1! + 1 
print(somaDeInteiros)
// será impresso o valor 2
```

**Saída**

```
2
```

Perceba, pelo exemplo anterior, o uso do construtor de *Int* que recebe uma *String* como parâmetro e tenta converter uma *String* em um *Int*. Nem sempre tal conversão é possível ou trivial para o construtor, e nos casos que não o é, ele retorna *nil*. Por esse motivo, o retorno desse construtor não pode ser um simples *Int*, tem de ser um *Int*? para assim retornar *nil* nos casos em que a conversão falhe.

Essa característica vem de encontro com as funcionalidades de segurança do *Swift*, pois evita que o programador cometa erros com valores nulos em pontos não esperados de seu código. Se ele declarou que a variável pode ser nula, ele deve se responsabilizar por somente utilizá-la na presença de um valor. Denominamos a operação de extração do valor de um opcional de desempacotamento (*unwrapping*, em inglês). Existem duas maneiras principais de se desempacotar um opcional à procura de seu valor:

```
// primeira forma de desempacotamento de opcionais:
let stringDeNumero1 = "1"
let numeroInteiro1 = Int(stringDeNumero1)
let somaDeInteiros = numeroInteiro1! + 1 
print(somaDeInteiros)
// será impresso o valor 2
```

**Saída**

```
2
```

Nesse caso, utilizamos o operador *“!”* para desempacotar o *Int* contido em *numeroInteiro1*. Quando fazemos a operação com *“!”* estamos pegando o tipo ***Int?*** e o convertendo em um ***Int***, ou seja, estamos convertendo um opcional em um não opcional. Porém, estamos fazendo isso de uma forma bastante direta e nos responsabilizando por qualquer valor inesperado que tais variáveis possam vir a conter, ou seja, o compilador não teria como nos salvar do seguinte erro em tempo de execução:

```
// primeira forma de desempacotamento de opcionais:
let stringDeNumero1 = "Um"
let numeroInteiro1 = Int(stringDeNumero1)
let somaDeInteiros = numeroInteiro1! + 1 
/* Um erro em tempo de execução ocorrerá porque estamos tentando desempacotar um valor nil */
```

Perceba que utilizamos o operador *“!”* na constante *numeroInteiro1* novamente, porém nesse caso, ela estaria valendo *nil*, pois a função *Int(“Um”)* retornaria *nil* já que não saberia converter a *String “Um”* em um inteiro válido. Sempre que nosso programa tentar executar uma *“nil!”* (desempacotamento de um *nil*), ele seria morto por chegar em um estado inconsistente!

```
// segunda forma de desempacotamento de opcionais:
let stringDeNumero2 = "Dois"
let numeroInteiro2 = Int(stringDeNumero2)

if let a = numeroInteiro2 {
    print(a * 2)
}
/* nada será impresso nesse caso, pois o fluxo de execução não passará por dentro do bloco do if */
```

Utilizamos nesse caso a expressão *“if let”* do *Swift*. Essa expressão serve para declararmos uma constante (que no nosso exemplo se chama a) que poderá ser utilizada somente dentro do *“if”*. Além disso, os comandos dentro das chaves do *if* só são executados quando o desempacotamento resulta em uma constante não *nil*. Dessa forma, o programa não falha, pois nunca tentamos multiplicar o valor da constante *a* (com o valor *nil*) por 2, já que o código dentro do *if* nunca chega a ser executado.

---

## OPERADORES

As principais operações em *Swift* podem ser divididas em: Atribuições, Aritméticas, Resto de divisão, Incremento/Decremento, Lógicas e Comparações.

Já vimos diversos tipos de atribuições em *Swift*, e elas são feitas com o uso do operador “*=*”. Vejamos mais um exemplo:

```
var valor: String? // variável opcional do tipo String?
valor = nil // podemos atribuir o valor nil à ela
valor = "Uma String Qualquer"
// depois podemos atribuir o valor de uma string à ela
```

As operações aritméticas e de resto de divisão, em *Swift*, se assemelham muito às outras linguagens que talvez você conheça. Veja exemplos:

```
let soma = 1 + 2 // a constante soma valerá 3
let mult = 1 * 2 // a constante mult valerá 2
let subt = 1 - 2 // a constante subt valerá -1
let div: Double = 1 / 2
// a constante div valerá 0.5, precisamos nesse caso 
// explicitar que a queremos como um Double, se não ela
// valeria 0, pois seria uma divisão inteira de 1 por 2
let resto = 1 % 2 
// a constante resto valerá 1, pois o resto da divisão inteira 
// de 1 por 2 é 1
```

Operações de incremento e decremento por 1, também são bastante comuns na linguagem e existem em dois formatos principais: com os operadores “+=” ou “-=” antes ou depois do nome da variável.

```
// Exemplos de incremento/decremento simples:
var i = 1
i += 1
// agora i vale 2
i -= 1
// agora i vale 1, novamente
```

E se desejarmos trabalhar com incrementos ou decrementos de 2, por exemplo, para somente passar por números pares? Faríamos assim:

```
var a = 0 

a += 2 // a vale 2
a += 2 // a vale 4
a -= 2 // a volta a valer 2
```

Os operadores de incremento “++” e decremento “--” existiram até a versão 2.2 do *Swift*, mas foram removidos na versão 3, assim como outras sintaxes que a linguagem adotava e que são inspiradas na linguagem C. O objetivo é tornar o *Swift* sempre mais moderno, e sua sintaxe simples e intuitiva.

Para realizar operações lógicas em *Swift* temos dois operadores principais: o *AND (&&) e o OR (||)*. Perceba que assim como em outras linguagens que você conhece, os operadores lógicos são mais comumente utilizados em controles condicionais *(ifs)*, como veremos na próxima seção.

```
// Exemplos de uso do AND 
let verdade1 = true && true
let mentira1 = false && true

// Exemplos de uso do OR
let verdade2 = true || false
let mentira2 = false || false
```

Por fim, para comparações utilizamos principalmente os operadores *<, >, ==, !=, >=, <=*

```
if 1 < 2 {
    print("1 é menor do que 2...")
    
    if 2 > 1 {
        print("...2 é maior do que 1...")
        
        if 1 == 1 && 2 == 2 {
            print("...1 é igual a 1 e 2 é igual a 2...")
            
            if 1 != 2 {
                print("...1 é diferente de 2...")
                
                if 1 >= 1 && 2 <= 2 {
                  print("...1 é maior ou igual a 1 e 2 é menor ou igual a 2...")
                }
            }
        }
    }
}
```

**Saída**

```
1 é menor do que 2...
...2 é maior do que 1...
...1 é igual a 1 e 2 é igual a 2...
...1 é diferente de 2...
...1 é maior ou igual a 1 e 2 é menor ou igual a 2...
```

Perceba que nesse caso, todos as impressões (*print*) serão realizadas, pois todas as condições colocadas nos *ifs* são verdadeiras.

---

## COMANDOS CONDICIONAIS

Existem três estruturas muito importantes no *Swift* quando falamos em comandos condicionais: operador ternário, *if-else e switch*.

Vejamos primeiramente como funciona o operador ternário. Trata-se de um operador que pode ser utilizado com fins de legibilidade para atribuir um valor dependendo de uma condição, a uma variável ou a uma constante. Temos nesse comando, um resultado atribuído no caso de a condição ser verdadeira e um outro resultado para o caso contrário.

```
let resultado = (1 > 2) ? "1 é maior que 2" : "1 não é maior que 2"
print(resultado) // será impresso "1 não é maior que 2"
```

**Saída**

```
1 não é maior que 2
```

O exemplo acima utiliza o operador ternário para gerar a constante *resultado*. Perceba que dois valores são possíveis para serem atribuídos à constante. São eles: *“1 é maior que 2” e “1 não é maior que 2”*. Essas *strings* são atribuídas à *resultado* mediante a checagem da condição *1 > 2*, e como essa expressão é *false* a segunda *String* é retornada e atribuída à *resultado*. Nos casos de uso do ternário, onde a condição checada seja verdadeira, o valor da primeira expressão após o *“?”* é que é retornado e atribuído à constante ou variável.

Esse tipo de estrutura, apesar de possível, não é sempre a melhor escolha para se tratar fluxos de execução condicionais em nossos programas. Comandos mais comuns a desenvolvedores de software são o *if* e o *else* para tratar condições.

```
let temperatura = 21

if temperatura > 30 {
    print("Está muito quente!")
} else if temperatura > 20 {
    print("Está confortável.")
} else {
    print("Está frio!")
}
```


**Saída**

```
Está confortável.
```

A estrutura básica do *if* e do *else* é como ilustra o exemplo acima. Perceba que os parênteses são opcionais para as condições em *Swift*, ou seja, não somos obrigados a escrever *if (temperatura > 30) {…*; podemos omitir os parênteses apesar de seu uso ser opcional e em alguns casos, denotar a ordem em que as operações condicionais devem ser checadas. No exemplo anterior, será impresso *“Está confortável”*. Esse resultado ocorre pois, a primeira condição (temperatura > 30) é testada e resulta em *false* (temperatura vale 21, no exemplo), logo o bloco do primeiro *if* não é executado. A segunda condição (temperatura > 20), por sua vez, resulta em *true*, afinal 21 é realmente maior que 20, por isso os comandos dentro das chaves dessa segunda condição são executados. Imagine que temperatura fosse 10, nesse caso todas as condições testadas resultariam em *false* e, portanto, seria executado o bloco do *else* da penúltima linha do exemplo.

Uma outra maneira de se trabalhar com condicionais, é o comando *switch*:

```
let temperatura = 21

switch temperatura {
case 30:
    print("Trinta graus.")
case 29:
    print("Vinte e nove graus.")
default:
    print("Outra temperatura.")
}
```

**Saída**

```
Outra temperatura.
```

Perceba que o *switch* em *Swift* não precisa de *break* ao fim de cada bloco de condição. Além disso, o caso *default* em *Swift* é obrigatório; se não for definido, gera um erro de compilação. Lembre-se, *Swift* é seguro e quer evitar ao máximo que o programador cometa erros. Os *switches* em *Swift* podem ser ainda mais elaborados. Veja, por exemplo, um caso onde utilizamos um intervalo (*range*) dentro das condições:

```
let temperatura = 29

switch temperatura {
case 30...50:
    // 30...50 define um intervalo (tipo Range) que vai de 30 até 50 (inclusive)
    print("Muito quente!")
case 29:
    // temperatura exatamente igual a 29 graus
    print("Vinte e nove graus.")
case 20..<29:
    // 20..<29 define um Range que vai de 20 até 28 (29 é excluído nesse caso)
    print("Temperatura confortável.")
default:
    print("Outra temperatura.")
}
```

**Saída**

```
Vinte e nove graus.
```

Não somente *ranges* podem ser utilizados, mas podemos checar valores de *Enums, Strings, Caracteres,* tornando os ***switches*** em *Swift* altamente poderosos!

**💡 Por Enum, apenas conceituem como um grupo de constantes. Veremos mais definições na sequência do módulo.**

---

## LAÇOS

Para iterações em *Swift*, vamos olhar os comandos *while, repeat-while* e *for*. Os dois primeiros são utilizados para se iterar até que uma condição seja satisfeita, enquanto o último é utilizado para se iterar por coleções de dados (*Arrays,* por exemplo) ou *ranges*.

```
// Exemplo de do-while: suponha que temos uma função funcQuePodeRetornarUmInt() que retorne 
// um Int?, ou seja, ela pode retornar um inteiro ou nil. Queremos iterar, chamando-a até que
// um inteiro seja de fato retornado

var intOpcional: Int? // inicialmente nil, pois não atribuímos nenhum valor

repeat {
    intOpcional = funcQuePodeRetornarUmInt()
} while intOpcional == nil
```

**💡 Por *Array* (matriz, vetor), apenas entendam como um grupo de elementos (valores). Veremos mais definições na sequência do módulo.**

O trecho de código acima irá exaustivamente chamar nossa função *funcQuePodeRetornarUmInt()* até que ela retorne um *Int* e não *nil* ! Esse comportamento é atingido com o uso do *repeat-while.*

Agora, suponha que queremos iterar por um *Array* de N elementos. Para isso podemos utilizar um *while* para nos auxiliar ou, como veremos mais à frente, um *for.*

```
// Exemplo de while: suponha que "vetor" seja uma coleção (array) de N elementos, vamos 
// imprimir todos os valores de "vetor"

var i = 0

while i < N {
    print("O elemento atual vale \(vetor[i])")
    i += 1
}
```

Não se preocupe com esse *print* diferente, onde adicionamos o valor de vetor na posição *i* com o uso de interpolação de *strings* (esse “(…)” no meio da *String* é um operador de interpolação). Apenas entenda que serão impressas N linhas e cada uma delas será iniciada pela *String “O elemento atual vale”* seguida do valor do elemento propriamente dito. Iremos ver mais a fundo interpolação de *strings e Arrays* no próximo capítulo. Perceba que no exemplo acima utilizamos a estrutura *while condição { comandos }* para nos auxiliar a percorrer todos os elementos do vetor.

Apesar de muito útil em outras situações, para o problema de se percorrer um vetor, essa não é a maneira mais elegante de fazer tal operação em *Swift*, pois temos um comando muito poderoso chamado *for* que nos auxiliará com isso:

```
// Exemplo de for: suponha que "vetor" seja uma coleção (array) de N elementos, vamos 
// imprimir todos os valores do "vetor"

for elem in vetor {
    print("O elemento atual vale \(elem)")
}
```

Perceba quão poderoso é esse comando nesse formato. Com ele não precisamos mais incrementar a variável de controle *i* nem a inicializar; não precisamos indexar o vetor com *i* a cada iteração, e melhor ainda, nem precisamos saber que o vetor tem N elementos! O *Swift* se encarrega desses detalhes chatos de implementação, que deixariam nosso código verboso, e se encarrega de percorrer o vetor para nós.

Vale a pena ressaltar que o *for* pode ser usado com *ranges* e *Strings*. Vejamos mais alguns exemplos:

```
// Exemplo de for com Ranges

for i in 0...2 {
    print("i=\(i)")
}

// serão impressas as linhas:
// i=0
// i=1
// i=2

for i in 0..<2 {
    print("i=\(i)")
}

// serão impressas as linhas:
// i=0
// i=1
```

**Saída**

```
i=0
i=1
i=2
i=0
i=1
```

Novamente estamos utilizando ranges com as expressões “…” e “..<”. A primeira inclui o elemento final do *range*, enquanto a segunda não.

Vamos treinar um pouco do que revisamos antes de iniciar o próximo capítulo:

Crie um algoritmo que complete a sequência 1, 3, 5, 7,     , até seu décimo elemento, declarando o fator de crescimento em uma constante e imprimindo o próximo sempre em uma variável chamada *auxiliar*.

**</a href="./Códigos/main02.swift">Código</a>**

```
/*Criei um algoritmo que complete a sequencia 1, 3, 5, 7, ___ , 
até seu décimo elemento, declarando o fator de crescimento em uma constante
e imprimindo o próximo sempre em uma variável chamada auxiliar.*/

let fator = 2
var auxiliar = 1

for i in 0..<10{
    print (auxiliar)
    auxiliar += fator
}
```

**Saída**

```
1
3
5
7
9
11
13
15
17
19
```

---

# ESTRUTURA DE DADOS

## INTRODUÇÃO

Linguagens de programação de mais alto nível, como Swift, tentam ao máximo facilitar a vida dos desenvolvedores por meio de abstrações de alto nível. Por exemplo, lembre-se da programação C e das dificuldades para se trabalhar com alocação de memória dinamicamente, vetores e strings. Grande parte do poder e da produtividade que o Swift entrega está no fato de possuir **Estruturas de Dados** e muito bem documentadas para permitir que o desenvolvedor seja produtivo e não precise ‘reinventar a roda’ em todos os programas que venha a implementar.

A Apple fornece a maior parte de suas estruturas de dados sobre a forma de bibliotecas, que chamamos de *frameworks*. O principal deles é o *Foundation*, que como o nome sugere, é a base para todos os outros. Esse é o *framework* onde importantes estruturas de dados do Swift estão definidas.

## STRING

É muito comum em nossos programas precisarmos trabalhar com textos. Para isso, no Swift temos a classe String que serve para abstrair as operações e os tipos de dados relacionados a essa coleção de caracteres Unicode. Ela define todas as strings em nossos programas.

Strings podem ser criadas de diversas maneiras em Swift. Apesar disso, algo que varia, é a mutabilidade. Strings constantes (declaradas com *let*) são por padrão imutáveis, ou seja, não podemos realizar operações nessas strings que as alterem (porém, perceba que podemos criar novas strings a partir delas, atribuindo seu valor). Strings declaradas com *var*, por sua vez, são mutáveis e podem ser alteradas em memória diretamente, sem a necessidade de declararmos uma nova String.

```
let stringImutável = "Uma string imutável" 
/* perceba que podemos acentuar nomes de varíaveis ou constantes em Swift! :)*/

// o símbolo + nesse caso será utilizado para concatenação de string 
// (explicaremos melhor no próximo parágrafo)

let novaString = stringImutável + ", ou seja, constante." 

// valor de novaString = "Uma string imutável, ou seja, constante."
// concatenação e atribuição válidas, mesmo a string inicial sendo constante.

// Observe esse outro exemplo
let outraStringImutavel = "Outra string imutável"
outraStringImutavel += " concatenada com outra string?!" // Erro!!!!

/* O erro ocorre porque não podemos alterar a string imutável propriamente 
dita,apenas poderíamos criar uma nova a partir dela.  Por fim, vamos fazer o 
mesmo com uma string mutável agora */

var stringMutavel = "Uma String mutável"
stringMutavel += " concatenada com outra string!!"

/* O valor de stringMutavel é "Uma string mutável concatenada com outra 
string!!". Pois, podemos concatenar uma nova string ao valor inicial dela, já 
que ela é mutável.*/
```

Perceba que caso você tenha uma String “Meu nome é:” que deva ser concatenada com o valor real do seu nome (vamos supor que seja “João da Silva”), resultando no valor final “Meu nome é: João da Silva”, em Swift, isso é tão simples como uma operação de soma de inteiros para o compilador do Swift. Assim, utilizamos o operador “+” não somente para números, mas também para Strings.

```
var entrada = "Meu nome é: " // string mutável
entrada += "João da Silva" // concatenação
entrada = entrada + "..." // comando similar ao anterior
// entrada se torna "Meu nome é: João da Silva..."
```

Uma outra forma de atingir nesse tipo de resultado é com o uso da interpolação. Essa é uma forma de trabalhar com strings auxiliada pela operação “\(String)” no meio de uma outra String. Esse comando é uma maneira legível de se pegar o valor que está entre os parênteses da operação “\(String)” sob a forma de String e concatená-lo a uma outra String. Por exemplo:

```
let entrada = "Meu nome é:"
let nome = "João da Silva"
let saida = "\(entrada) \(nome)!!! Olá!!!"
// saida se torna "Meu nome é: João da Silva!!! Olá!!!"
```

Da mesma forma que a operação + foi facilmente adaptada para ser utilizada com strings em Swift, podemos também utilizar os operadores de comparação. Veja alguns exemplos:

```
var cargo = "administrador"

if cargo == "administrador" {
    print("Acesso permitido!")
}

// Será impresso "Acesso permitido!"
// Perceba que utilizamos o operador == para comparar Strings nesse exemplo

var nome1 = "josé"
var nome2 = "maria"

if nome1 < nome2 {
    print("Ordenação dos nomes: \(nome1) -> \(nome2)")
}

// Será impresso "Ordenação dos nomes: josé -> maria"
// Perceba que utilizamos o operador < para descobrir se alfabeticamente
// nome1 vem antes de nome2.
```

**Saída**

```
Acesso permitido!
Ordenação dos nomes: josé -> maria
```

Por fim, podemos percorrer strings com um *for-in*. Nesse caso, iremos iterar sobre os caracteres dessa String. No Swift 5 toda String já é de forma nativa uma coleção (Array) de caracteres. Por exemplo, a String “Entrada” já é uma coleção de caracteres com 7 posições.

```
for c in "Entrada" {
    print(c)
}

// Será impresso:
// E
// n
// t
// r
// a
// d
// a
```

**Saída**

```
E
n
t
r
a
d
a
```

---

## ARRAY

Quando queremos trabalhar com vetores, que são coleções de dados indexadas por inteiros de 0 à N-1 (onde N é o tamanho da coleção), utilizamos os *Arrays*. Talvez, você já tenha trabalhado em alguma linguagem onde os *Arrays* podem conter qualquer tipo de elemento. Por exemplo, poderíamos misturar inteiros e strings em uma coleção (esse é o caso de Javascript ou Ruby). A linguagem Swift, como já comentamos, é muito segura! Dessa maneira, os *Arrays* precisam ser fortemente tipados, ou seja, buscamos ter elementos dos mesmos tipos em nossas coleções.

```
let pares: Array<Int> = [2, 4, 6, 8]
let impares = [1, 3, 5, 7] 
// Perceba que o compilador irá inferir o tipo Array<Int> na constante impares.
// Esse tipo também pode ser definido como Array[Int] (entre chaves e não somente entre <>) em Swift.
```

Assim como no caso das strings, *Arrays* declarados com *let* são imutáveis, enquanto *Arrays* declarados com *var* são mutáveis:

```
let paresImutavel = [2, 4, 6, 8]
paresImutavel.append(10) //Erro! Array imutável não pode receber novos elementos
var imparesMutaveis = [1, 3, 5, 7]
imparesMutaveis.append(9) // Agora, imparesMutaveis = [1, 3, 5, 7, 9]
```

Perceba a utilização do comando *“append”* chamado com o uso de um *“.”* após o nome de nosso *array*. Chamamos isso de envio da mensagem *“append”* (ou chamada do método *append*), responsável por adicionar ao final do *Array* (no caso, imparesMutaveis) o valor passado como parâmetro.

Veja um caso de erro onde tentamos adicionar uma String a um *Array* de *Int.*

```
var imparesMutaveis = [1, 3, 5, 7]
imparesMutaveis.append("nove") // Erro! O parametro "nove" é uma String e não um Int
```

Como *imparesMutaveis* é do tipo *Array<Int> (uma coleção de inteiros)* ele não pode receber uma String, por isso um erro no trecho de código anterior.

Veja a seguir que podemos utilizar o *for-in* ou um *for* tradicional, auxiliado pelo método *count* de um *Array* (que retorna à quantidade de elementos que ele possui) para percorrer os elementos de um *Array*:

```
var imparesMutaveis = [1, 3, 5, 7]
imparesMutaveis.append(9)

for impar in imparesMutaveis {
    print(impar)
}

// Será impresso:
// 1
// 3
// 5
// 7
// 9

// Caso prefira também pode-se utilizar um for com 
// a quantidade de elementos do Array, obtida com 
// o método count
for i in 0 ..< imparesMutaveis.count {
    print(imparesMutaveis[i])
}
```

**Saída**

```
1
3
5
7
9
1
3
5
7
9
```

Já sabemos como adicionar elementos a um *Array* e também como percorrê-los, porém, como podemos alterar uma posição que não seja a última ou trocar um elemento em um *Array*? Para isso, utilizamos o índice da seguinte forma *“array[índice]”* (chamada de indexação do *Array*) para nos auxiliar. *“array[índice]=”* pode ser utilizada para alterar um elemento na posição índice, enquanto *“array[índice]”* pode ser utilizada para buscar o elemento de *array* que esteja na posição índice. Veja alguns exemplos de utilização:

```
// Exemplo de indexação de Array
var imparesMutaveis = [1, 3, 5, 7]
let segundoImpar = imparesMutaveis[1] 
// Arrays vão de 0 até N-1 (onde N é o tamanho)
print("O segundo impar na coleção imparesMutaveis é \(segundoImpar)")

// Exemplo de alteração de elemento em determinado indice de um Array
imparesMutaveis[0] = 9
imparesMutaveis[1] = 11
imparesMutaveis[2] = 13
imparesMutaveis[3] = 15
// imparesMutaveis agora é [9, 11, 13, 15]
```

**Saída**

```
O segundo impar na coleção imparesMutaveis é 3
```

**💡 A quantidade de posições de um Array sempre é contabilizada a partir do 0 (zero). Dessa forma, um Array de 9 posições tem índices de 0 à 8.**

Em Swift, há outras formas muito comuns de se instanciar *Arrays* e concatenar elementos a eles. Veja essas formas alternativas no seguinte trecho de código:

```
// Esse é um jeito de se iniciar um array de inteiros vazio:
var pares = [Int]() 

// E esse é outro jeito de se concatenar elementos:
pares += [2, 4, 6, 8, 10]
pares += [12, 14, 16, 18, 20]
print(pares)
// Será impresso: "[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]"

// Esse é outro jeito de se iniciar um array de inteiros vazio:
var impares = Array<Int>()
impares += [1, 3, 5, 7]
print(impares)
// Será impresso: "[1, 3, 5, 7]"
```

**Saída**

```
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[1, 3, 5, 7]
```

Vamos treinar? Crie um Array com o nome de 3 pessoas e um segundo Array com as respectivas idades. Utilizando os laços de repetições já vistos, crie a seguinte estrutura de frase:

“A 1a pessoa tem o nome _____ e a idade      ”.

“A 2a pessoa tem o nome _____ e a idade      ”.

**</a href="./Códigos/main03.swift">Código</a>**

Resolução:

```
//Crie um Array com o nome de 3 pessoas e um segundo Array com as respectivas idades. 
//Utilizando os laços de repetições já vistos crie a seguinte estrutura de frase:
//“A 1a pessoa tem o nome _________ e a idade __________”.
//“A 2a pessoa tem o nome _________ e a idade __________”.

var nomes = [String]() 
var idades = [Int]()

nomes.append("João");
nomes.append("Pedro");
nomes.append("Fernando");
nomes.append("Alex");
nomes.append("Marcos");

idades.append(10);
idades.append(2);
idades.append(18);
idades.append(21);
idades.append(29);

for i in 0 ..< nomes.count{
    print("A \(i+1)a pessoa tem o nome \(nomes[i]) e a idade \(idades[i])")
}
```

**Saída**

```
A 1a pessoa tem o nome João e a idade 10
A 2a pessoa tem o nome Pedro e a idade 2
A 3a pessoa tem o nome Fernando e a idade 18
A 4a pessoa tem o nome Alex e a idade 21
A 5a pessoa tem o nome Marcos e a idade 29
```

---

## DICIONÁRIOS

Um outro tipo de dado muito comum quando queremos trabalhar com coleções, são os dicionários (conhecidos como vetores associativos, *hash maps* ou *hashes* em outras linguagens). A grande diferença entre um *array* e um dicionário é que enquanto indexamos *Arrays* com inteiros, dicionários são indexados com quaisquer objetos, por exemplo, Strings. Em um formato de chave e valor, tanto o tipo das chaves como o tipo dos valores devem ser pré-definidos, já que a tipagem é estática e forte. Vamos ver como fazer isso:

```
let precosDosProdutos = ["Livro": 20.0, "Lapiseira": 2.0, "Caneta": 4.0] 
// tipo inferido de precosDosProdutos: Dictionary<String, Double>
// chaves String e valores Double, também pode ser escrito como 
// [String: Double] em Swift
```

Nesse exemplo, criamos um dicionário onde as chaves são do tipo *String* e os preços são do tipo *Double* para guardar os preços de determinados produtos de uma determinada loja online.

Da mesma maneira que no caso dos *Arrays*, a mutabilidade dos Dicionários é definida com o uso na declaração da palavra-chave *let* ou *var*:

```
let precosDosProdutosImutavel = ["Livro": 20.0, "Lapiseira": 2.0, "Caneta": 4.0] 
precosDosProdutosImutavel["Borracha"] = 0.5 // Erro! Dicionário é imutável!

var precosDosProdutosMutavel = ["Livro": 20.0, "Lapiseira": 2.0, "Caneta": 4.0] 
precosDosProdutosMutavel["Borracha"] = 0.5 

/* precosDosProdutosMutavel agora vale: ["Livro": 20.0, "Lapiseira": 2.0, "Caneta": 4.0, "Borracha": 0.5] */
```

É interessante notar que Dicionários, no momento da sua indexação, retornam o tipo da chave, porém este retorno pode ser do tipo opcional (!). Sendo do tipo opcional (!) o compilador espera que a chave contenha um valor. Se esse valor não existir, o código irá quebrar e gerar um erro em tempo de execução. Por isso, antes de utilizarmos o valor de uma determinada chave de um dicionário, precisamos desempacotar essa entrada com *“if let”*, por exemplo, para evitar que o código quebre em tempo de execução.

```
var precosDosProdutosMutavel = ["Livro": 20.0, "Lapiseira": 2.0, "Caneta": 4.0] 
precosDosProdutosMutavel["Borracha"] = 0.5 
/* precosDosProdutosMutavel agora vale: ["Livro": 20.0, "Lapiseira": 2.0, "Caneta": 4.0, "Borracha": 0.5] */

if let preco = precosDosProdutosMutavel["Borracha"] {
    print("O preço da borracha é: \(preco)")
    // será impresso "O preço da borracha é: 0.5"
}
```

**Saída**

```
O preço da borracha é: 0.5
```

Para percorrer dicionários, utilizamos um outro tipo em Swift, chamado Tupla. Trata-se de uma maneira simples e rápida de associar um ou mais tipos em Swift. Vamos ver um exemplo de *for-in* em um dicionário que utiliza uma Tupla para passar por todas as chaves e valores:

```
var precosDosProdutosMutavel = ["Livro": 20.0, "Lapiseira": 2.0, "Caneta": 4.0] 
precosDosProdutosMutavel["Borracha"] = 0.5 
/* precosDosProdutosMutavel agora vale: ["Livro": 20.0, "Lapiseira": 2.0, "Caneta": 4.0, "Borracha": 0.5] */

for (chave, valor) in precosDosProdutosMutavel {
    print("O preço de \(chave) é: \(valor)")
}

// Será impresso:
// O preço de Lapiseira é: 2.0
// O preço de Borracha é: 0.5
// O preço de Livro é: 20.0
// O preço de Caneta é: 4.0
```

**Saída**

```
O preço de Caneta é: 4.0
O preço de Livro é: 20.0
O preço de Borracha é: 0.5
O preço de Lapiseira é: 2.0
```

Perceba que a Tupla (chave, valor) é associada a cada iteração a uma *String* e a um *Double* que estão contidos no dicionário.

Swift oferece outras formas muito comuns de se instanciar dicionários. Vejamos essas formas alternativas no seguinte trecho de código:

```
// Esse é um jeito de se iniciar um dicionário vazio: com chaves do
// tipo String e valores do tipo Double:
var precosDosProdutos = Dictionary<String, Double>()
precosDosProdutos["Borracha"] = 0.5
print(precosDosProdutos)
// Será impresso: "[Borracha: 0.5]"

// Esse é um outro jeito de se iniciar um dicionário em Swift:
var precoCombustivel = [String: Double]()
precoCombustivel["Gasolina"] = 3.555
print(precoCombustivel)
// Será impresso: "[Gasolina: 3.555]"
```

**Saída**

```
["Borracha": 0.5]
["Gasolina": 3.555]
```

**Vamos treinar?** Crie um dicionário com nome e valor de 5 carros e após percorra esse dicionário imprimindo a seguinte frase para cara item: “O carro ________ custa ________ reais”.

**</a href="./Códigos/main04.swift">Código</a>**

Solução:

```
//Vamos treinar? Crie um dicionário com nome e valor de 5 carros e após
//percorra esse dicionário imprimindo a seguinte frase para cara item: 
//“O carro __________ custa ________ reais”.

var carros = ["Fuxca": 25000, "Goool": 20000, "Onixx": 40000] 

for (chave, valor) in carros {
    print("O carro \(chave) custa \(valor) reais")
}
```

**Saída**

```
O carro Goool custa 20000 reais
O carro Fuxca custa 25000 reais
O carro Onixx custa 40000 reais
```

---

## ENUM

Talvez você já tenha utilizado *Enums* em outras linguagens, como C ou Java, porém os *Enums* em Swift são bem mais completos do que nessas linguagens. Podemos criar nossos próprios *Enums* e utilizar seus valores diretamente em *switches*. Os *Enums* nos ajudam a explicitar tipos importantes para o nosso programa, por exemplo: suponha que temos que tratar alguns caracteres especiais de maneira diferente em nosso código, ele pode ficar muito legível com um *Enum*. Vejamos:

```
// Exemplo de definição de um enum simples
// Perceba que Enums em Swift não são apenas constantes 
// inteiras como em outras linguagens

enum CaracterEspecial: Character {
    case Tab = "\t"
    case Linefeed = "\n"
    case CarriageReturn = "\r"
}
```

Agora, vejamos como utilizar os valores definidos em *Enums* em nossas variáveis:

```
enum Bussola {
    case Norte, Sul, Leste, Oeste
}

var direcao = Bussola.Norte // inferencia de tipo: Bussola
print(direcao)

direcao = .Leste // atribuindo novo valor
print(direcao)
```

**Saída**

```
Norte
Leste
```

*Enums* podem conter um pouquinho de lógica e podem definir valores associados. Suponha que queremos criar um tipo que nos ajude a trabalhar com horários de trens. Um trem pode estar “Dentro do Horário” ou “Atrasado por X minutos”. Podemos modelar isso dessa maneira em Swift:

```
enum HorarioTrem {
    case NoHorario
    case Atrasado(Int) // atrasado por alguns minutos
}

func descricao(status: HorarioTrem) {
    switch status {
    case .NoHorario:
        print("O trem está no horário")
    case .Atrasado(let min):
        print("O trem está atrasado por \(min) minutos")
    }
}

var status = HorarioTrem.NoHorario
descricao(status: status)
// Será impresso: "O trem está no horário"

status = .Atrasado(5)
descricao(status: status)
// Será impresso: "O trem está atrasado por 5 minutos"
```

**Saída**

```
O trem está no horário
O trem está atrasado por 5 minutos
```

Perceba que utilizamos um *switch* para “varrer” os valores possíveis para o *Enum* e extrair a quantidade de minutos que o trem está atrasado. Agora, imagine o poder que esse tipo de dado nos traz, além de uma série de possibilidades em um código muito mais legível e enxuto!

Para facilitar a fixação, **vamos treinar?** Crie um *Enum* para as estações do ano, e crie uma variável chamada atual e atribua um valor do *Enum* para ela:

**</a href="./Códigos/main05.swift">Código</a>**

Solução:

```
//crie um Enum para as estações do ano, e crie uma variavel 
//chamada atual e atribua um valor do Enum à ela

enum Estacao {
    case Outono
    case Inverno
    case Verão
    case Primavera
}

var atual = Estacao.Outono
print(atual)
```

**Saída**

```
Outono
```

---

## FUNÇÕES

No que diz respeito a retornos, as funções podem ser declaradas de duas maneiras distintas: a primeira quando ela tem algum tipo de retorno, e a segunda quando ela não deve retornar nada (*void* em outras linguagens). Além disso, as funções podem ou não conter parâmetros internos que serão levados em conta na sua execução. Veja exemplos:

```
func funcaoSemParamESemRetorno() {
    print("Nada será retornado")
}

func funcaoSemParamEComRetornoInt() -> Int {
    return 0
}

func funcaoComParamEComRetornoInt(param: Int) -> Int {
    return param + 1
}
```

Esses exemplos são bastante simples, porém dizemos que em Swift funções são “cidadãos de primeira classe”. O que queremos dizer com isso é basicamente que funções são tratadas como qualquer outro objeto do programa (um *Int* ou uma *String*, por exemplo), podendo serem atreladas a variáveis e serem passadas como parâmetro para outras funções. Pode-se ainda criar uma função como um retorno de uma outra função. O conceito parece confuso à primeira vista, mas não é, além disso, é altamente poderoso.

Veja esse exemplo de atribuição de funções a variáveis:

```
// Função que recebe uma String como parâmetro e
// imprime "String passada como parametro: " seguido
// de seu valor.
func imprima(str: String) {
    print("String passada como parametro: \(str)")
}

// Atribui-se a função anterior a uma constante 
let funcao = imprima

// Agora tanto funcao(str) como imprima(str) chamam
// os mesmos comandos, a mesma função!
funcao("Hello World!") // irá imprimir "String passada como parametro: Hello World!"
```

**Saída**

```
String passada como parametro: Hello World!
```

E agora, veja esse exemplo de atribuição de uma função que recebe uma outra função como parâmetro:

```
// Função que recebe uma String como parâmetro e
// imprime "String passada como parametro: " seguido
// de seu valor.
func imprima(str: String) {
    print("String passada como parametro: \(str)")
}

// Função que recebe uma outra função como parametro
func funcaoQueChamaFuncaoComHelloWorld(funcao: (String) -> ()) {
    // chamando a função
    funcao("Hello World!")
}

// Você pode chamar a função passando a outra função como parametro
funcaoQueChamaFuncaoComHelloWorld(funcao: imprima)
```

**Saída**

```
String passada como parametro: Hello World!
```

Isso abre uma série de possibilidades para a linguagem.

Vamos ver um exemplo com a classe *Array* que vimos anteriormente. *Arrays* em Swift possuem um método chamado *“map”* que recebe uma outra função como parâmetro. Essa função é chamada para cada elemento desse array e os resultados são colocados em um novo *array* (na mesma ordem). Veja um exemplo:

```
let vetor = [1, 2, 3, 4]

func duplicador(i: Int) -> Int {
    return i * 2
}

let vetorDuplicado = vetor.map(duplicador) 

print (vetorDuplicado)
```

**Saída**

```
[2, 4, 6, 8]
```

**Sugestão de estudo**: procure na documentação do *Array* de Swift pelos métodos *filter* e *sort*. Note como as funções e como os parâmetros são utilizados nesses casos.

Para finalizar essa nossa breve introdução às funções em Swift, vamos ver um exemplo de múltiplos retornos. Utilizamos as Tuplas (as que vimos na seção sobre Dicionários) para criar funções que possam retornar mais do que um valor (inclusive podendo ser de múltiplos tipos), e podemos gravar esses valores em múltiplas variáveis em apenas uma linha. Veja:

```
func buscarLatitudeLongitude() -> (String, Double, Double) {
    return ("Campinas", -22.002, -25.012)
}

let (cidade, lat, lng) = buscarLatitudeLongitude()
// Agora, temos: cidade = "Campinas, lat = -22.002 e lng = -25.012

print(cidade)
print(lat)
print(lng)
```

**Saída**

```
Campinas
-22.002
-25.012
```