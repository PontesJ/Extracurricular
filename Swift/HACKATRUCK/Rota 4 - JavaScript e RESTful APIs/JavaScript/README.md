# CONCEITOS INICIAIS

## INTRODUÇÃO

### HISTÓRICO

O JavaScript começou a ser desenvolvido por Brendan Eich em 1995. O motivo foi a necessidade de se criar uma linguagem para o browser Netscape, empresa onde ele trabalhava. Inicialmente, a linguagem se chamava Mocha e posteriormente mudaram seu nome para LiveScript e então, após um acordo com a Sun Microsystems, para JavaScript.

Em setembro de 1995, o LiveScript foi lançado na versão beta do navegador Netscape 2.0 e teve seu nome alterado para JavaScript em dezembro do mesmo ano, na versão 2.0B3 do navegador.

Pelo nome, JavaScript, podemos pensar que a linguagem compartilha as características da linguagem Java, porém esse é um engano comum. A palavra 'java' foi introduzida no nome da linguagem, apenas como uma estratégia de marketing da Netscape para aproveitar da popularidade da linguagem Java quando o JavaScript foi lançado. As duas linguagens possuem sintaxe, semânticas e usos muito diferentes.

A aceitação do JavaScript como linguagem *client-side* das páginas web foi grande, que significa que a linguagem roda diretamente no navegador web do computador do usuário, e como consequência a Microsoft criou um dialeto compatível com o JavaScript chamado de JScript e o incluiu no Internet Explorer 3.0 em agosto de 1996. Apesar de terem nomes diferentes, JavaScript e JScript são muito similares.

Em 1996, a Netscape submeteu o JavaScript como candidato a padrão industrial para a *European Computer Manufacturers Association*, o que resultou na versão padronizada chamada ECMAScript. A ECMA é uma organização criada com o objetivo de ser responsável pela padronização de sistemas de informação.

Desde 2012, todos os navegadores modernos possuem suporte total ao ECMAScript 5.1. A sexta versão do ECMAScript foi publicada em 2017 e chamada de ECMAScript 2015. Ela também foi conhecida inicialmente como ECMAScript 6 ou ES6.

---

## ONDE ENCONTRAR E COMO USAR

O JavaScript foi por muito tempo conhecido apenas como linguagem *client-side*. Porém, ela foi se tornando cada vez mais popular ao longo dos anos também como uma linguagem *server-side*, ou seja, uma linguagem que também roda do lado do servidor.

Isso se deu por conta da criação e popularização de ferramentas como o Node.js, que providencia um ambiente no servidor capaz de interpretar JavaScript. Além disso, podemos encontrar e utilizar o JavaScript em diversas ferramentas, como por exemplo, na base de dados MongoDB, que aceita consultas escritas em JS/SQL - uma combinação de SQL com JavaScript, e no Unity, que tem suporte a uma versão modificada de JavaScript.

Quando falamos em desenvolvimento do lado do cliente, *client-side*, temos diversos *frameworks* desenvolvidos especificamente para facilitar a manipulação dos elementos da página web para que possamos criar experiências cada vez mais ricas para os usuários. Um *framework* é um conjunto de conceitos e funcionalidades comuns entre vários projetos condensados para auxiliar no desenvolvimento do seu software. Podemos citar três populares *Frameworks*, o AngularJS, o React e o JQuery.

Nosso foco será aprender o JavaScript para ser utilizado no lado do servidor, *server-side*, então não iremos falar sobre *frameworks client-side* nem sobre a manipulação de elementos da página web neste material. Neste caso, caso queira estudar um pouco sobre estes assuntos, recomendamos acessar, por exemplo, Front-end JavaScript frameworks e o blog Tableless.

---

## CARACTERÍSTICAS E CONCEITOS

Como toda linguagem de programação, o JavaScript tem diversas características e conceitos por trás de sua implementação e é importante que nós conheçamos essas características para que possamos entender o seu funcionamento.

### LINGUAGEM DE SCRIPT

O JavaScript é uma <a href="https://en.wikipedia.org/wiki/Scripting_language">linguagem de script</a>. Por definição scripts são programas escritos para automatizar a execução de tarefas que poderiam ser executadas uma a uma por uma pessoa.

Como é comum nas linguagens de script, o JavaScript é uma <a href="https://en.wikipedia.org/wiki/Interpreter_language">linguagem interpretada</a>, e não compilada. Ou seja, as instruções do script são executadas diretamente sem ter sido previamente traduzidas para a linguagem de máquina por um compilador. Outros exemplos de linguagens interpretadas são o Python e o Ruby.

### LINGUAGEM MULTIPARADIGMA

<a href="https://en.wikipedia.org/wiki/Programming_paradigm#Multi-paradigm">Linguagens multiparadigma</a> são linguagens de programação que tem suporte a mais de um paradigma de programação. Isso dá liberdade para o programador utilizar o paradigma de programação mais adequado para solucionar o problema que pretender resolver.

O JavaScript possui suporte aos paradigmas:

- Imperativo, como a <a href="https://en.wikipedia.org/wiki/C_(programming_language)">Linguagem C</a>.

- Funcional, como o <a href="https://www.haskell.org/">Haskell</a> e <a href="https://pt.wikipedia.org/wiki/Scheme">Scheme</a>.

- Orientado a objetos (paradigma este que foi abordado anteriormente em nosso curso).

O JavaScript possui elementos de sintaxe de linguagens imperativas como if, else, for entre outros. Então, é possível implementar os scripts de forma estruturada e procedural, caso necessário. Exemplo:

```
for(i=1; i<=10;i++){
    if(i%2 == 0){
        console.log(i + ' é par')
    }else{
        console.log(i + ' é impar')
    }
}
```

**Saída**

```
1 é impar
2 é par
3 é impar
4 é par
5 é impar
6 é par
7 é impar
8 é par
9 é impar
10 é par
```

O JavaScript também possui características que possibilitam que a linguagem possa ser utilizada como uma <a href="https://eloquentjavascript.net/1st_edition/chapter6.html">linguagem funcional</a>, ou seja, com o suporte a funções com parâmetros e com retorno de funções (<a href="https://en.wikipedia.org/wiki/Higher-order_function">*high-order functions*</a>) e <a href="https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Closures">*closures*</a>. Exemplo:


```
function dobrarNumero(numero){
    return numero * 2
}

function mostrarNumero(numero){
    console.log(numero)
    return numero
}

var arrayDeNumeros = [1,1,2,3,5,8,13,21]

arrayDeNumeros.map(dobrarNumero).map(mostrarNumero)
```

**Saída**

```
2
2
4
6
10
16
26
42
```

Outra forma de trabalhar com JavaScript é de forma orientada a objetos. Porém, a orientação a objetos do JavaScript é <a href="https://en.wikipedia.org/wiki/Prototype-based_programming">baseada em protótipos</a> ao invés de classes, que é o mais comum de se ver em outras linguagens. Isso faz com que a forma como tratamos a orientação a objetos aqui seja diferente do habitual. Iremos explorar esse conceito no tópico orientação a objetos deste módulo.

```
function Carro(numeroDeRodas, cor){
    this.numeroDeRodas = numeroDeRodas
    this.cor = cor  
    this.isLigado = false
    
    this.ligar = function(){
        if (this.isLigado == false) {
            console.log('o carro está ligado.')
            this.isLigado = true
        }else{
            console.log('o carro já estava ligado.')
        }
    }
}

var meuCarro = new Carro(4, 'azul')

meuCarro.ligar()
meuCarro.ligar()
```

**Saída**

```
o carro está ligado.
o carro já estava ligado.
```

---

## TIPAGEM FRACA E DINÂMICA

O JavaScript é uma linguagem de programação de <a href="https://en.wikipedia.org/wiki/Strong_and_weak_typing">tipagem fraca</a>, ou seja, o tipo da informação está associado ao valor da variável e não à variável em si. Na prática, isso significa que não é necessário definir o tipo das suas variáveis, pois o tipo associado a elas irá depender do tipo do valor que ela armazena.

Após declarar uma variável é possível associar valores de tipos diferentes ao longo da execução do código. O JavaScript fará os ajustes necessários para que o novo valor seja associado à sua variável, o que a caracteriza como uma linguagem de <a href="https://en.wikipedia.org/wiki/Type_system#DYNAMIC">tipagem dinâmica</a>, pois os tipos são avaliados ao longo da execução do código.

Veremos mais detalhes sobre os tipos de dados e como eles são avaliados no JavaScript na próxima seção.

```
var variavel = 10 // Inicialmente o tipo é Number
variavel = "Monteiro" // Agora o tipo passa a ser String
variavel = false // e por fim passa a ser um Boolean
```

JavaScript também é uma linguagem que possui funções de primeira-classe (*first-class functions*). Isso significa que podemos tratar funções como se fossem um tipo, passando-as como argumento de funções, retornando-as como resultado, armazenando em variáveis e criando funções em tempo de execução. Exemplo:

```
function criarFuncaoDeMultiplicar(multiplicador) {
    return function(numero){
        return numero * multiplicador
    }
}

var dobrar = criarFuncaoDeMultiplicar(2) // falamos que nosso multiplicador é 2 para dobrar

console.log( dobrar(19) ) // chamamos dobrar passando o número a ser dobrado
console.log( dobrar(7) )
```

**Saída**

```
38
14
```

---

# SINTAXE BÁSICA

## INTRODUÇÃO

O conjunto de conhecimentos apresentados inicialmente neste módulo, corresponde às ferramentas básicas para que possamos criar nossos próprios algoritmos em JavaScript. Então, é importante que você absorva bem esses conceitos e essas instruções.

Sempre que for praticar, você pode escrever seus códigos usando seu browser, o Node.js instalado no seu computador (indicação mais abaixo) ou sites online que emulam o ambiente necessário para escrever e interpretar seu código JavaScript.

Como usar o console do seu navegador:

- Mozilla Firefox: <a href="https://developer.mozilla.org/en-US/docs/Tools/Web_Console/Opening_the_Web_Console">https://developer.mozilla.org/en-US/docs/Tools/Web_Console/Opening_the_Web_Console</a>

- Google Chrome: <a href="https://developers.google.com/web/tools/chrome-devtools/console/?hl=pt-br">https://developers.google.com/web/tools/chrome-devtools/console/?hl=pt-br</a>

- Apple Safari: <a href="https://developer.apple.com/library/content/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/GettingStarted/GettingStarted.html">https://developer.apple.com/library/content/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/GettingStarted/GettingStarted.html</a>

- Microsoft Edge:  <a href="https://docs.microsoft.com/en-us/microsoft-edge/f12-devtools-guide">https://docs.microsoft.com/en-us/microsoft-edge/f12-devtools-guide</a>

Aqui estão alguns exemplos de sites que emulam o ambiente necessário para testar códigos em JavaScript:

- <a href="https://jsbin.com/?js,console">https://jsbin.com/?js,console</a>

- <a href="https://repl.it/languages/javascript">https://repl.it/languages/javascript</a>

Como instalar e usar o Node.js:

- <a href="https://code.tutsplus.com/tutorials/nodejs-step-by-step-introduction--net-19448">https://code.tutsplus.com/tutorials/nodejs-step-by-step-introduction--net-19448</a>

---

## VARIÁVEIS E TIPOS DE DADOS

Quando você estiver escrevendo seu algoritmo para solucionar algum problema ou automatizar alguma tarefa, toda informação a ser manipulada será no formato de dados. Esses dados serão armazenados em variáveis para que você possa acessá-las e modificá-las na execução do seu algoritmo.

Para criarmos variáveis, utilizamos as palavras-chaves **var**, **const** e **let**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_dd5865d6.jpg" widgth = 50>

As variáveis são uma funcionalidade essencial de praticamente todas as linguagens de programação. JavaScript não é exceção. Abaixo as descrições das palavras-chaves utilizadas para declarações de variáveis.

**’var’** declara uma variável, opcionalmente é possível atribuir a ela um valor em sua inicialização.

A declaração **‘const’** cria uma variável cujo o valor é fixo, ou seja, uma constante somente para leitura. Isso não significa que o valor é imutável, apenas que a variável constante não pode ser alterada ou retribuída.

**’let’** permite que você declare variáveis limitando seu escopo no bloco, instrução, ou em uma expressão na qual ela é usada. Isso é inverso da keyword **var**, que define uma variável globalmente ou no escopo inteiro de uma função, independentemente do escopo de bloco.

Os tipos básicos do JavaScript são:

- *Number* : representa números, sejam inteiros ou fracionários.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_63b720cf.jpg" widgth = 50>

- *String* : representam textos.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_8d119c28.jpg" widgth = 50>

- *Boolean* : representa um valor lógico.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_77f53411.jpg" widgth = 50>

- *Undefined e Null* : representam a ausência de valor. Quando declaramos uma variável e não a inicializamos ela tem o valor undefined.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_e7bfa0a7.jpg" widgth = 50>

- *Object* : representa as estruturas de dados Array e Dicionário.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_3c05aae9.jpg" widgth = 50>

JavaScript é uma linguagem de **tipagem dinâmica**, isso significa que os tipos não são associados às variáveis e sim ao valor que elas estão armazenando. Por isso, uma mesma variável pode armazenar valores de tipos diferentes ao longo da execução do código.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_6885391c.jpg" widgth = 50>

Para saber o tipo de uma variável basta usar o operador **typeof**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_13a61d90.jpg" widgth = 50>

Para criar suas próprias variáveis basta:

1. Escrever a palavra-chave **var**.

2. Definir o nome da sua variável.

3. Associar um valor, caso necessário.

Mas vale lembrar que não podemos dar qualquer nome para nossas variáveis. As regras para definirmos os identificadores das nossas variáveis são:

- Podemos usar letras, números, underline (_) e cifrão ($);

- Devem sempre começar com uma letra;

- Podemos iniciar com cifrão ($) e underline (_), mas neste material vamos manter sempre começando com uma letra;

- São "case sensitive", ou seja, há diferenciação entre letras maiúsculas e minúsculas;

- Não podemos usar palavras reservadas da linguagem para nomear nossas variáveis, como **for, if, else, typeof**, etc.

Agora que sabemos criar variáveis e quais os tipos de dados que elas podem armazenar, vamos ver um pequeno exemplo.

Imagine que você tem um aplicativo onde o usuário vai criar uma lista de tarefas. Para criar uma tarefa o usuário precisa dizer até quando a tarefa deve ser realizada, definir a descrição da tarefa e precisa definir se a tarefa foi feita ou não. Quais variáveis nós precisamos criar para armazenar essas informações?

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_c710a981.jpg" widgth = 50>

Criamos uma variável para armazenar a descrição da tarefa, uma variável para armazenar a data final da tarefa e uma variável para determinar se a tarefa foi feita ou não. Com variáveis podemos armazenar informação e posteriormente utilizar a informação no nosso código.

Lembre-se de sempre nomear suas variáveis com nomes significativos para que elas representem adequadamente o valor que armazenam.

---

## OPERADORES

Aprendemos que variáveis armazenam a informação, os dados da aplicação. Mas como fazemos para utilizar esses valores realizando operações com eles? Para modificar a informação e chegar aos resultados que esperamos no nosso código iremos utilizar os operadores.

Existem diversos tipos de operadores, mas vamos falar brevemente sobre os operadores aritméticos, de comparação e lógicos. Para uma lista completa dos operadores do JavaScript visite <a href="https://www.w3schools.com/js/js_operators.asp">W3schools JavaScript Operators</a> e <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators">MDN Expressions and Operators</a>.

### OPERADORES ARITMÉTICOS

Os **operadores aritméticos** são os operadores utilizados para realizar cálculos de aritmética matemática. Os operadores aritméticos básicos são:

- Soma ( + ): soma dois valores numéricos.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_d4c8cb04.jpg" widgth = 50>

- Subtração ( - ): subtrai dois valores numéricos.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_58a695fb.jpg" widgth = 50>

- Divisão ( / ): divide dois valores numéricos.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_f874e2ec.jpg" widgth = 50>

- Multiplicação ( * ): multiplica dois valores numéricos.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_2240c4cb.jpg" widgth = 50>

- Resto da divisão ( % ): retorna o resto da divisão inteira entre dois números.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_1def4893.jpg" widgth = 50>

- Incremento e decremento ( ++ e -- ): incrementa ou decrementa o valor de uma variável em uma unidade. Caso ele venha antes da variável, ele incrementa a variável e depois retorna seu valor incrementado. Caso venha depois da variável, ele retorna o valor da variável e depois incrementa seu valor.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_559d9a03.jpg" widgth = 50>

### OPERADORES DE COMPARAÇÃO

Os **operadores de comparação** servem exatamente para comparar dois valores. O resultado da expressão sempre será um booleano de valor **true** ou **false**.

Os operadores de comparação são:

- Igual a (== ou ===): testa se um valor é igual ao outro.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_fafd4b34.jpg" widgth = 50>

- Diferente de (!= ou !==): testa se os dois valores são diferentes.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_85ef64a2.jpg" widgth = 50>

- Maior que (>) e menor que (<): testa se o primeiro valor é maior que o segundo e se o primeiro valor é menor que o segundo, respectivamente.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_52b1de5c.jpg" widgth = 50>

Os operadores de comparação são muito úteis quando precisamos saber se alguma condição é satisfeita no nosso código para que possamos tomar uma decisão ou seguir com algum fluxo no nosso algoritmo. Vamos utilizá-los bastante quando estivermos falando sobre **condicionais** mais a frente neste módulo.

No JavaScript temos mais dois operadores para testar a igualdade e diferença entre valores. Isso porque a linguagem tem uma propriedade chamada **coerção de tipo**. Isso faz com que, caso dois valores de tipos diferentes estejam sendo utilizados em uma expressão, o interpretador vai converter um dos tipos automaticamente para que a expressão possa ser avaliada.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_d4b70d82.jpg" widgth = 50>

O mesmo acontece quando comparamos valores de tipos diferentes. O JavaScript realiza conversões para que as comparações aconteçam. Para que nós não tenhamos que nos preocupar com esses comportamentos não esperados, basta utilizar os operadores **===** e **!==** para realizar a **comparação do tipo** e do valor, ao invés de apenas comparar o valor.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_d750c17.jpg" widgth = 50>

### OPERADORES LÓGICOS

Utilizamos os operadores lógicos para realizar operações com valores booleanos. Os operadores lógicos suportados no JavaScript são os operadores **AND**, **OR** e **NOT**.

- **AND ( && )**: Só é verdadeiro quando as duas expressões são verdadeiras.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_c0b1095e.jpg" widgth = 50>

- **OR ( || )**: Só é falso quando as duas expressões são falsas.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_ff29429.jpg" widgth = 50>

- **NOT ( ! )**: Inverte verdadeiro para falso e falso para verdadeiro.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_972584c4.jpg" widgth = 50>

Podemos utilizar os operadores lógicos em conjunto com os operadores de comparação para definir composições de condições a serem alcançadas, para seguir com o fluxo do nosso algoritmo.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_dccb607e.jpg" widgth = 50>

---

## LAÇOS DE REPETIÇÃO

Com as estruturas condicionais somos capazes de definir quando um certo bloco de código será executado com base em uma condição, ou seja, uma expressão lógica que pode ser avaliada em verdadeiro ou falso.

Quando precisarmos repetir um bloco de código por uma certa quantidade de vezes até que uma condição seja satisfeita, nós utilizamos os **laços de repetição**. Todo laço de repetição possui uma condição de parada. A cada repetição ele irá avaliar a condição de parada para definir se continua ou não a execução do bloco de código.

Temos que ficar atentos ao definir nossa condição de parada para garantir que ela seja alcançável, pois se não for, iremos ter criado um **laço infinito** que irá travar nossa aplicação, pois nunca iremos chegar ao fim do nosso algoritmo.

Laços de repetição são muito úteis para simplificar e automatizar tarefas repetitivas, como contagens, por exemplo.

Podemos criar laços de repetições de três formas, utilizando as palavras chave:

- **while;**

- **do while;**

- **for.**

### WHILE

O laço **while** irá repetir um bloco de código enquanto sua condição seja verdadeira. Quando a condição relacionada ao laço for avaliada em falsa, a repetição se encerra.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_512e977c.jpg" widgth = 50>

Nesse exemplo, vamos listar os números de 1 até 30 utilizando o while:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_a256244a.jpg" widgth = 50>

Os passos para criar um laço de repetição **while** são:

1. Escrever a palavra-chave **while**.

2. Definir, entre parênteses, a condição de parada.

3. Criar um bloco de código abrindo e fechando as chaves.

4. Inserir dentro do bloco de código, as instruções a serem repetidas.

### DO WHILE

A diferença do **do while** para o **while** está na avaliação da condição de parada. Enquanto, no **while** a condição é testada antes do bloco de código ser executado, no **do while** a condição de parada é testada **após** o bloco de código ser executado.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_34020359.jpg" widgth = 50>

Vamos novamente listar os números de 1 até 30, porém agora usando o do while.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_48175ef0.jpg" widgth = 50>

Os passos para criar um laço de repetição **do while** são:

1. Escrever a palavra chave **do**.

2. Criar um bloco de código abrindo e fechando as chaves.

3. Inserir dentro do bloco de código, as instruções a serem repetidas.

4. Ao fim do bloco, escrever a palavra chave **while**.

5. Entre parênteses, definir a condição de parada do laço de repetição.

### FOR

O laço de repetição **for** é um pouco diferente dos demais. Na própria definição do laço, nós definimos três coisas:

1. Uma variável que será utilizada para acompanhar o progresso do nosso laço de repetição.

2. A condição de parada do laço de repetição.

3. A atualização da nossa variável para acompanhar o progresso.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_8f4cc6b2.jpg" widgth = 50>

Vamos listar os números de 1 até 30 utilizando o **for** agora.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_1558c359.jpg" widgth = 50>

A **declaração** e **inicialização da variável** que utilizamos no laço só acontece quando nosso laço de repetição é inicializado. Esta variável só pode ser utilizada dentro do bloco de código associado ao **for**.

A **condição de parada** é testada ao fim de cada execução das instruções contidas no bloco de código. Caso ela seja verdadeira é realizada uma nova repetição. Caso ela seja falsa, o laço se encerra.

A **atualização da variável** acontece ao fim de cada repetição, antes da condição de parada ser avaliada.

Os passos para criar um laço de repetição **for** são:

1. Escrever a palavra-chave **for**.

2. Entre parênteses e separados por ponto e vírgula ';':

    1. Declarar a variável que será utilizada para acompanhar o progresso e definir seu valor inicial.

    2. Definir a condição de parada do laço de repetição.

    3. Definir a atualização da variável utilizada para acompanhar o progresso do laço de repetição.

3. Criar um bloco de código abrindo e fechando as chaves.

4. Inserir dentro do bloco de código, as instruções a serem repetidas.

---

## TRATAMENTO DE ERROS

Eventualmente, podem ocorrer operações que não são esperadas no nosso código. Por exemplo, o usuário pode entrar com um texto onde era esperado um número, ou um cálculo aritmético não pode ser feito com os números que o usuário entrou.

Para isso, a linguagem tem mecanismos para evidenciar esses problemas e tratá-los caso ocorram. Essas são as **exceções** (*exceptions*).

Para lançar uma exceção, basta na sua função usar a palavra-chave **throw** e criar um novo erro com sua mensagem personalizada.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_38d19c75.jpg" widgth = 50>

Nesse exemplo, temos uma função que retorna o resultado da divisão entre dois números. Porém, caso você tente fazer uma divisão por zero, nós vamos lançar uma exceção dizendo que isso não é possível.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_fa034008.jpg" widgth = 50>

Agora que sabemos como lançar exceções é importante sabermos que devemos tratá-las quando elas são lançadas. Se não prepararmos nosso código para o caso dessas exceções serem lançadas, nosso código simplesmente não irá funcionar.

Para que nosso código esteja preparado para o caso de exceções serem disparadas durante a execução de uma função, esta deve estar envolta por um bloco de código **try catch**.

Dentro do bloco **try**, nós escrevemos as chamadas das funções normalmente.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_fd1e600a.jpg" widgth = 50>

Após o bloco **try** devemos implementar o bloco **catch**. Caso uma exceção seja lançada por alguma função dentro do bloco **try**, essa exceção será armazenada em uma variável no bloco **catch** e poderá ser utilizada para tratar o erro adequadamente.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_b0381a79.jpg" widgth = 50>

Por fim, caso tenha alguma operação que gostaríamos de realizar, não importando se nossas funções lançaram ou não exceções, temos o bloco **finally**. As instruções neste bloco são executadas sempre, não importando se o código lançou ou não uma exceção.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/3ef59d710e17391a0ef51448c4439170_html_6c217947.jpg" widgth = 50>

---

## LINKS DE REFERÊNCIA

A seguir indicamos alguns links que podem complementar e enriquecer seu autoestudo.

### VARIÁVEIS E TIPOS DE DADOS

<a href="http://eloquentjavascript.net/01_values.html">http://eloquentjavascript.net/01_values.html</a>

<a href="http://eloquentjavascript.net/02_program_structure.html">http://eloquentjavascript.net/02_program_structure.html</a>

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures</a>

<a href="https://www.w3schools.com/js/js_datatypes.asp">https://www.w3schools.com/js/js_datatypes.asp</a>

<a href="https://www.w3schools.com/js/js_variables.asp">https://www.w3schools.com/js/js_variables.asp</a>

### OPERADORES

<a href="https://www.w3schools.com/js/js_operators.asp">https://www.w3schools.com/js/js_operators.asp</a>

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators</a>

Automatic type conversion:  <a href="http://eloquentjavascript.net/01_values.html">http://eloquentjavascript.net/01_values.html</a>

Operadores de comparação e lógicos:  <a href="https://www.w3schools.com/js/js_comparisons.asp">https://www.w3schools.com/js/js_comparisons.asp</a>

### FUNÇÕES

<a href="http://eloquentjavascript.net/03_functions.html">http://eloquentjavascript.net/03_functions.html</a>

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions</a>

<a href="https://www.w3schools.com/js/js_functions.asp">https://www.w3schools.com/js/js_functions.asp</a>

### CONDICIONAIS

<a href="https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide/Declara%C3%A7%C3%B5es">https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide/Declara%C3%A7%C3%B5es</a>

<a href="http://eloquentjavascript.net/02_program_structure.html">http://eloquentjavascript.net/02_program_structure.html</a>

<a href="https://www.w3schools.com/js/js_if_else.asp">https://www.w3schools.com/js/js_if_else.asp</a>

### LAÇOS DE REPETIÇÃO

<a href="http://eloquentjavascript.net/02_program_structure.html">http://eloquentjavascript.net/02_program_structure.html</a>

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration</a>

<a href="https://www.w3schools.com/js/js_loop_for.asp">https://www.w3schools.com/js/js_loop_for.asp</a>

<a href="https://www.w3schools.com/js/js_loop_while.asp">https://www.w3schools.com/js/js_loop_while.asp</a>

<a href="https://www.w3schools.com/js/js_break.asp">https://www.w3schools.com/js/js_break.asp</a>

### TRATAMENTO DE ERROS

<a href="http://eloquentjavascript.net/08_error.html">http://eloquentjavascript.net/08_error.html</a>

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#Exception_handling_statements">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#Exception_handling_statements</a>

<a href="https://www.w3schools.com/js/js_errors.asp">https://www.w3schools.com/js/js_errors.asp</a>

---

# ESTRUTURA DE DADOS

## ARRAY - PARTE 1

### ESTRUTURA DE DADOS

Em toda linguagem de programação existem estruturas de dados básicas para que possamos organizar nossa informação para que fique mais simples trabalhar com ela. No JavaScript as estruturas de dados básicas são os **Arrays** e os **Dicionários**.

Ambos são do tipo *object*, ou seja, possuem propriedades e métodos associados a eles. <u>Propriedades</u> são variáveis associadas ao objeto que armazenam informações a respeito dele. <u>Métodos</u> são funções associadas ao objeto que podem ser invocadas a partir dele.

Neste módulo vamos passar pelos conceitos básicos de cada um e entender como utilizá-los nos nossos códigos.

### ARRAYS - COLEÇÕES INDEXADAS

**Arrays** são um conjunto ordenado de valores. Nos referimos a um **array** pelo seu nome, que é comumente chamado de seu identificador, e nos referimos às informações armazenadas no **array** pela sua posição na lista, ou seja, seu índice.

Considerando para fins didáticos que temos um **array** chamado ‘frutas’ com dois nomes de frutas, nos referimos à primeira fruta como o valor na primeira posição e à segunda fruta como o valor na segunda posição do **array** ‘frutas’.

### CRIANDO UM ARRAY

Podemos criar um **array** de duas formas, vazio ou já populado com alguns elementos iniciais.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_b668849d.png" widgth = 50>

A forma mais comum de inicializar **arrays** é com a sintaxe de colchetes [].

Para sabermos quantos elementos um **array** possui, podemos acessar sua propriedade **lenght**, que diz quantos elementos o **array** possui.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_a4897ee7.png" widgth = 50>

### ACESSANDO ELEMENTOS NO ARRAY

Para acessar um elemento do **array**, ou seja, acessar uma das informações armazenadas nele, basta referenciarmos a informação pela sua posição dentro do **array** utilizando os colchetes [].

Importante notar que a posição dos elementos dentro do **array** começa em 0 (zero) e não em 1 (um). Então, o primeiro elemento do **array** está na posição zero, o segundo elemento na posição um e assim por diante. Logo, se um **array** tem dez elementos, os elementos estão localizados nas posições de zero até nove.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_a81f457c.png" widgth = 50>

---

## ARRAY - PARTE 2

### BUSCANDO UM ELEMENTO NO ARRAY

Para saber a posição de um elemento em um **array**, podemos utilizar um dos vários métodos que os **arrays** já tem ou percorrer o **array** procurando pelo índice do elemento que procuramos.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_53956b68.png" widgth = 50>

### INSERINDO NOVOS ELEMENTOS NO ARRAY

Temos duas formas de inserir elementos em um **array**.

1. Podemos delegar um valor diretamente para uma posição dentro do **array**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_d38d31fa.png" widgth = 50>

Dessa forma os elementos intermediários não definidos possuem o valor *undefined*.

2. Ou podemos utilizar o método **push** para inserir um elemento ao final do **array**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_32abdb89.png" widgth = 50>

### REMOVENDO ELEMENTOS DO ARRAY

Para remover um elemento de um **array**, precisamos saber em que posição o elemento está e utilizar o método **splice**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_b03b8961.png" widgth = 50>

---

## ARRAY - PARTE 3

O **Array** é uma das estruturas de objetos mais utilizadas no JavaScript, é um objeto global usado na construção de ‘**arrays**’: objetos de alto nível semelhantes a listas.

O JavaScript disponibiliza alguns métodos para manipulação de **arrays**. Abaixo alguns que você deve conhecer:

### POP()

O método **pop()** remove o último elemento de um **array** e retorna aquele elemento.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_11a330dd.png" widgth = 50>

### SHIFT()

O método **shift()** remove o primeiro elemento de um **array** e retorna esse elemento. <u>**Este método muda o tamanho do array**</u>.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_35b3634.png" widgth = 50>

### UNSHIFT()

O método **unshift()** adiciona um ou mais elementos no início de um **array** e retorna o número de elementos (propriedade **length**) atualizado.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_bddd932a.png" widgth = 50>

### FOREACH()

O método **forEach()** executa uma dada função em cada elemento de um **array**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_16f1fa92.png" widgth = 50>

### INCLUDES()

Determina se um **array** contém um determinado elemento, retornando true ou false apropriadamente.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_435a34ee.png" widgth = 50>

### FILTER()

O método **filter()** cria um novo **array** com todos os elementos que passaram no teste implementado pela função fornecida.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_3a0a3314.png" widgth = 50>

### MAP()

O método **map()** invoca a função **callback** passada por argumento para cada elemento do **Array** e devolve um novo **Array** como resultado.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_c6c18a68.png" widgth = 50>

### REDUCE()

O método **reduce()** executa uma função **reducer** (provida por você) para cada membro do **array**, resultando num único valor de retorno.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_292f2a29.png" widgth = 50>

### SOME()

Este método verifica se pelo menos um item do **array** passou pela condição. Se passado, o método retorna “true” senão “false”.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_6d86459e.png" widgth = 50>

### EVERY()

Este método verifica se todo o item do **array** passou pela condição. Se passado, retorna "true" senão "false".

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_532fddd.png" widgth = 50>

### SORT()

Este método é usado para organizar/ordenar os itens do **array** em ordem crescente ou decrescente.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_bdd49259.png" widgth = 50>

### ARRAY.FROM()

Isso altera todas as coisas que são semelhantes a **array** ou iteráveis em um **array** verdadeiro, especialmente quando se trabalha com **DOM**, para que você possa usar outros métodos do **Array** como **reduce**, **map**, **filter** e assim por diante.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_fa2e7aee.png" widgth = 50>

### TRABALHANDO COM DOM

**DOM - Modelo de Documento por Objetos** - é uma convenção multiplataforma e independente de linguagem para representação e interação com objetos em documentos HTML, XHTML e XML.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_c3eda038.png" widgth = 50>

Caso desejamos obter e percorrer todos os itens da lista, os elementos **\<li>** ou **LI’s**, é preciso convertê-lo para um **array** válido. O método **Array.from()** é para isto, servirá de conversor do resultado do seletor, via JavaScript, para que possamos utilizar todos os recursos do **Array** que o JavaScript fornece. Veja abaixo:

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_7bbfd543.png" widgth = 50>

### ARRAY.OF()

Este método cria um **array** de todos os argumentos passados para ela. Veja abaixo:

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_66d72a39.png" widgth = 50>

---

## DICIONÁRIOS

### CRIANDO UM DICIONÁRIO

Podemos criar um dicionário utilizando chaves **{}**.

Ele pode ser inicializado com informação ou vazio.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_9ac7eabc.jpg" widgth = 50>

### ACESSANDO ELEMENTOS DE UM DICIONÁRIO

Para acessar um elemento no dicionário, basta referenciá-lo a partir de sua chave.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_193fcccb.jpg" widgth = 50>

### INSERINDO UM ELEMENTO EM UM DICIONÁRIO

Para inserir um valor em um dicionário, basta você associar o valor a uma nova chave no dicionário. Se você associar o valor a uma chave já existente, ele vai substituir o valor antigo pelo novo valor.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_b903a406.jpg" widgth = 50>

### REMOVENDO UM ELEMENTO DE UM DICIONÁRIO

Para remover um valor do dicionário, basta utilizar o operador **delete**. Ele vai remover a chave e o valor associado a ela do seu objeto.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_8738333c.jpg" widgth = 50>

Para saber se um dicionário ou objeto possui uma propriedade podemos usar o operador **in**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_4b69f14a.jpg" widgth = 50>

### ITERANDO UM ELEMENTO DE UM DICIONÁRIO

Para iterar os elementos de um dicionário, basta utilizarmos um laço de repetição **for** em conjunto do operador **in**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/420b9616e7033d4f9eab23d30654770b_html_528175dc.jpg" widgth = 50>

Assim podemos listar as chaves de um dicionário e acessar todos os seus valores em um laço de repetição.

---

## LINKS DE REFERÊNCIA

A seguir indicamos alguns links que podem complementar e enriquecer seu autoestudo.

### GERAIS

<a href="http://eloquentjavascript.net/04_data.html">http://eloquentjavascript.net/04_data.html</a>

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects</a>

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures</a>

<a href="https://www.w3schools.com/js/js_objects.asp">https://www.w3schools.com/js/js_objects.asp</a>

### ARRAYS

<a href="https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array">https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array</a>

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections</a>

<a href="https://www.w3schools.com/js/js_arrays.asp">https://www.w3schools.com/js/js_arrays.asp</a>

<a href="https://www.w3schools.com/js/js_array_methods.asp">https://www.w3schools.com/js/js_array_methods.asp</a>

<a href="https://www.w3schools.com/js/js_array_sort.asp">https://www.w3schools.com/js/js_array_sort.asp</a>

### DICIONÁRIOS

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections</a>

---

# FUNÇÕES E ESCOPO

## INTRODUÇÃO

### FUNÇÕES

Uma função é um conjunto de expressões encapsuladas em um bloco de código. Para declarar uma função basta usar a palavra-chave **function**, definir um identificador para a função, abrir e fechar parênteses e abrir e fechar chaves.

O identificador da função segue as mesmas regras para nomear variáveis.

Para executar a função posteriormente, basta se referenciar a ela pelo seu identificador seguido de parênteses.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_206d9cb8.jpg" widgth = 50>

As funções podem receber parâmetros, ou seja, valores que serão utilizados na execução das operações da função. Os parâmetros que a função recebe são definidos entre os parênteses da declaração da função e separados por vírgula.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_206d9cb8.jpg" widgth = 50>

As funções podem produzir algum valor e devolver esse valor ao final de sua execução. Esse valor é o retorno da função. Nós definimos o retorno da função com a palavra-chave **return**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_bb6707e7.jpg" widgth = 50>

Os passos para declarar uma função são:

1. Escrever a palavra chave **function**.

2. Definir o identificador da função e o nome da função.

3. Entre parênteses, definir os parâmetros caso você precise de informações externas.

4. Abrir e fechar as chaves onde ficarão as instruções a serem executadas.

5. Escrever as instruções da função dentro das chaves.

6. Por fim, definir o retorno da função, caso a função retorne algum valor.

**💡 Dica: Para melhor visualização do código e mantê-lo “limpo”, é sugerido que utilize template string para concatenação e interpolação das Strings. Template literals são literais string que permitem expressões embutidas. Você pode usar string multilinhas e interpolação de string com elas. Elas eram chamadas "template strings" nas versões anteriores à especificação ES2015.**

Veja o exemplo utilizando o template literals:

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_af9fbd76.jpg" widgth = 50>

---

## FUNÇÕES ANÔNIMAS

Nos tópicos anteriores, aprendemos que para declarar uma função nós precisamos definir seu identificador (o nome da função), os parâmetros que a função vai receber (podemos declarar uma função sem parâmetros também) e definir o corpo da função (o bloco de instruções associadas àquela função) com seu retorno ao final.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_2d6fedb2.jpg" widgth = 50>

Essa é uma das formas de declarar uma função, na qual ela é identificada pelo seu identificador. Posteriormente, usamos o identificador da função para invocá-la. Isso faz com que as instruções no corpo da função sejam executadas.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_224c5e22.jpg" widgth = 50>

Porém, no JavaScript nós podemos criar funções sem a necessidade de identificá-las, como quando vamos utilizar a função em um contexto muito específico, ou apenas uma vez. Por exemplo, quando formos ordenar um array, podemos ordená-lo da forma padrão, crescente, ou podemos definir como queremos que a ordenação seja feita. Para isso definimos qual a função que será utilizada para realizar a comparação entre os elementos.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_ab2964e5.jpg" widgth = 50>

Quando uma função não possuir um identificador chamamos essa função de **função anônima.**

---

## QUANTIDADE DE PARÂMETROS VARIÁVEL

No JavaScript as funções que você declarar podem ter quantos parâmetros forem necessários ou nenhum parâmetro, como em praticamente todas as linguagens de programação. Um diferencial do JavaScript é que ao chamar uma função você pode passar mais ou menos parâmetros do que ela precisa.

Quando chamamos uma função passando para ela **mais** parâmetros do que ela precisa, ela simplesmente ignora os parâmetros a mais.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_300e7810.jpg" widgth = 50>

Quando chamamos uma função com **menos** parâmetros do que ela necessita, é associado aos parâmetros que faltam o valor **undefined.**

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_55609417.jpg" widgth = 50>

Podemos criar funções que se aproveitam dessa característica da linguagem, de poder receber quantos parâmetros forem necessários, e criar funções que aceitem uma quantidade de parâmetros variável.

Toda vez que uma função é chamada, é criada uma propriedade no corpo da função chamada **arguments**. Essa propriedade é um objeto que se comporta como um array; ela possui uma propriedade **length** que nos informa quantos argumentos foram passados para a função e podemos nos referenciar a cada um deles pela ordem em que foram inseridos na chamada da função (0, 1, 2, …).

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_eb1e26ae.jpg" widgth = 50>

No código acima, temos como exemplo uma função que diz quantos argumentos ela recebeu utilizando o objeto **arguments.**

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_1a92c130.jpg" widgth = 50>

No exemplo acima, temos um objeto chamado **lista** que possui duas propriedades, o nome da lista e um array que armazena as tarefas que estão na lista.

A função **adicionarTarefas()** recebe quantos argumentos forem necessários. Se o argumento for do tipo **string**, então, é criada uma nova tarefa com aquela descrição e a tarefa é adicionada no **array de tarefas** na nossa **lista.**

---

## FUNÇÕES COMO PARÂMETRO E RETORNO DE FUNÇÕES

Funções podem ser armazenadas em variáveis.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_8263edf9.jpg" widgth = 50>

Parâmetros de funções não passam de variáveis que estão presentes dentro do escopo da função. Diante desta característica, podemos passar funções como parâmetros de outras funções, ou seja, podemos utilizar esta função dentro do escopo da função que a recebeu.

No exemplo abaixo, vamos criar uma função que recebe como parâmetro um array e uma nova função. Então, vamos iterar por cada elemento deste array e aplicar a função que foi passada por parâmetro, criando assim um novo array com os resultados dessas modificações.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_f970ec71.jpg" widgth = 50>

Também podemos retornar funções como resultado de uma função.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_3391494a.jpg" widgth = 50>

Funções que operam com outras funções, seja recebendo-as como parâmetro ou as retornando, são chamadas de **funções de alta ordem** (high-order functions). Elas estão muito presentes no nosso dia-a-dia de programador, pois é um conceito presente em muitas linguagens modernas, como por exemplo, na linguagem Swift, na linguagem Python e em todas as linguagens de paradigma funcional (Haskell, Scala, Closure e Scheme).

Esse nível de abstração extra nos permite escrever nosso código voltado para a solução do problema em si, pois diminui a quantidade de linhas de código que precisamos escrever, diminuindo a incidência de possíveis bugs no código. Ela traz o código para mais perto da solução do problema, ao invés de focar nos conceitos da linguagem em si.

Abaixo estão alguns exemplos de funções de alta ordem que objetos do tipo array possuem e que podemos utilizar para simplificar nosso código, facilitando o seu entendimento.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_19fdedd7.jpg" widgth = 50>

---

## DEFINIÇÃO DE ESCOPO NO JAVASCRIPT

Escopo é o conjunto de variáveis, objetos e funções as quais você pode acessar em um determinado momento no seu código. Essa é uma característica importante da linguagem que garante que as funções no seu código só tenham acesso às informações necessárias para seu funcionamento.

No JavaScript temos dois tipos de escopo: o **escopo global** e o **escopo local.**

O **escopo global** são todas as variáveis, objetos e funções declaradas fora de uma função. Tudo declarado no escopo global pode ser acessado e modificado em qualquer ponto do código.

O **escopo local** abrange as variáveis, objetos e funções declaradas dentro de uma função. O JavaScript define novos escopos por função. Os parâmetros de uma função e tudo que for declarado dentro do corpo da função fazem parte do escopo local da função.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_39085022.jpg" widgth = 50>

Quando declaramos uma função dentro de outra função, quer dizer que criamos um novo escopo novamente. É possível aninhar escopos, ou seja, criar um novo escopo dentro de um escopo criado previamente.

É importante notar que os escopos de fora não tem acesso aos elementos dos escopos internos, mas os escopos internos têm acesso a todas as propriedades dos escopos externos a ela.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_c5fc1d5d.jpg" widgth = 50>

No JavaScript, blocos de código não criam novos escopos. Isso quer dizer que **condicionais** e **laços de repetição** não criam novos escopos. Se criarmos novas variáveis dentro de um bloco **if** ou de um laço **while**, essas variáveis serão criadas e estarão acessíveis no escopo em que o bloco está inserido.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_5897378e.jpg" widgth = 50>

No exemplo acima, mesmo a variável **mensagem** sendo criada dentro do bloco de código **if**, ela existe fora do contexto do bloco de código. Ela está presente no escopo global e pode ser utilizada fora dele. Caso o valor da variável **idade** fosse menor do que dezoito, a variável **mensagem** ainda poderia ser utilizada, com a diferença de que ela não teria valor associado. O valor associado à variável **mensagem** seria **undefined**.

É possível declarar um variável localmente em um bloco de código na versão mais atual do JavaScript, o ECMAScript 2015, também conhecido como ES6. Para isso, ao invés de usar **var** para declarar suas variáveis, utilizamos a palavra-chave **let** ou **const.**

As palavras-chave **let** e **const** não definem suas variáveis como constantes. Elas apenas declaram a variável localmente em um bloco de código. É uma boa prática usarmos **let**, ao invés de **var**, sempre que possível, pois isso garante que as variáveis criadas não escapem para o escopo global. Isso diminui a incidência de bugs e evita comportamento imprevisto no seu código.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_6f50b924.jpg" widgth = 50>

---

## CONDICIONAIS

Como vimos anteriormente, em funções é possível definir um conjunto de instruções a serem executadas dentro de um par de chaves. Nós podemos chamar esse conjunto de um bloco de código.

No JavaScript podemos definir quando um bloco de código será executado ou não, utilizando estruturas de controle do fluxo do nosso algoritmo. Essas estruturas podem ser **estruturas condicionais** ou **laços de repetição.**

As estruturas condicionais definem, com base em uma expressão lógica, se um bloco de código vai ser executado ou não. Para isso usamos a palavra-chave **if.**

O **if** vem acompanhado de uma expressão lógica entre parênteses e um bloco de código. Caso a expressão lógica resulte em **true** (verdadeiro) o bloco de código associado é executado.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_5c5643e0.jpg" widgth = 50>

Caso você tenha um outro conjunto de instruções que serão executados, caso a condição não seja atendida, você pode usar a palavra-chave **else** e associar um novo bloco de código para ser executado.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_88030b6b.jpg" widgth = 50>

E você também pode associar uma condição no bloco **else**. A diferença de fazer uso de vários **if**'s, um após o outro, é que essas condições só serão avaliadas, caso a condição anterior seja falsa. Se a condição **if** ou **else if** anterior for verdadeira, então as condições **else if** posteriores não serão avaliadas.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_6a5c64a5.jpg" widgth = 50>

Vamos ver um exemplo: imagine que na sua aplicação você precisa saber qual, entre dois números, é o maior.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_e3019404.jpg" widgth = 50>

No exemplo acima, com a nossa condição **num1 > num2** fomos capazes de comparar a variável **num1** com a variável **num2** e saber qual das duas possui um valor associado maior que o outro.

Quando temos uma estrutura de seleção simples, apenas com um **if** e um **else**, podemos utilizar um operador especial chamado de **operador ternário**. Nele, nós definimos uma condição, e caso ela seja verdadeira, a primeira parte da expressão é retornada. Caso a condição seja falsa, a segunda condição é retornada.

O **operador ternário** é o sinal de interrogação **'?'** e os retornos são separados pelo sinal de dois pontos **':'**.

(condição) **?** (retorno verdadeiro) **:** (retorno falso)

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_7f0ebc1e.jpg" widgth = 50>

---

## HOISTING

Esse é um conceito presente na linguagem que causa um pouco de confusão quando estamos começando. O termo **hoisting** significa, em poucas palavras, "levar ao topo". No JavaScript todas as declarações de variáveis e funções que ocorrem ao longo do código são movidas para o topo do escopo em que estão inseridas.

Isso significa que você pode usar variáveis antes de declará-las, pois quando o script for interpretado, todas as declarações serão movidas para o topo, garantindo sua existência antes de ser utilizada.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_f6d0e7d1.jpg" widgth = 50>

Contudo temos que levar em consideração a diferença entre **declaração** e **inicialização**. Declarar uma variável não significa que ela tem um valor associado a ela. Quando uma variável não foi declarada e você a utiliza, você recebe um erro. Quando uma variável foi declarada, porém não foi inicializada, ela apenas está com o valor **undefined** associado a ela, não gerando erros. Então, sempre utilize suas variáveis após ter definido seu valor inicial.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/48d33088fe884ea5271304603670c64f_html_4c57aa25.jpg" widgth = 50>

É uma boa prática, para evitar bugs e comportamentos inesperados, que a declaração de todas as variáveis seja feita no início de cada escopo onde elas são utilizadas, seja ele o escopo global ou um escopo local.

---

## LINKS DE REFERÊNCIA

A seguir indicamos alguns links que podem complementar e enriquecer seu autoestudo.

### FUNÇÕES ANÔNIMAS

Funções: <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions</a>

Funções: <a href="http://eloquentJavaScript.net/03_functions.html">http://eloquentJavaScript.net/03_functions.html</a>

### QUANTIDADE DE PARÂMETROS VARIÁVEL

Arguments object: <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#Using_the_arguments_object">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#Using_the_arguments_object</a>

Arguments object: <a href="http://eloquentJavaScript.net/04_data.html#arguments_object">http://eloquentJavaScript.net/04_data.html#arguments_object</a>

### DEFINIÇÃO DE ESCOPO NO JAVASCRIPT

High-order Functions: <a href="http://eloquentJavaScript.net/05_higher_order.html">http://eloquentJavaScript.net/05_higher_order.html</a>

### FUNÇÕES COMO PARÂMETRO E RETORNO DE FUNÇÕES

JavaScript Scope: <a href="https://www.w3schools.com/js/js_scope.asp">https://www.w3schools.com/js/js_scope.asp</a>

Understanding scope in JavaScript: <a href="https://scotch.io/tutorials/understanding-scope-in-JavaScript">https://scotch.io/tutorials/understanding-scope-in-JavaScript</a>

Function Scope: <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#Function_scopel">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#Function_scopel</a>

Parameters and Scopes: <a href="http://eloquentJavaScript.net/03_functions.html#h_u4j2OhpYkg">http://eloquentJavaScript.net/03_functions.html#h_u4j2OhpYkg</a>

Nested Scope: <a href="http://eloquentJavaScript.net/03_functions.html#h_c/Ms2Ed/N0">http://eloquentJavaScript.net/03_functions.html#h_c/Ms2Ed/N0</a>

### HOISTING

Hoisting: <a href="https://www.w3schools.com/js/js_hoisting.asp">https://www.w3schools.com/js/js_hoisting.asp</a>

Hoisting: <a href="https://developer.mozilla.org/pt-BR/docs/Glossario/Hoisting">https://developer.mozilla.org/pt-BR/docs/Glossario/Hoisting</a>

JavaScript Hoisting: <a href="https://tableless.com.br/elevacao-ou-JavaScript-hoisting/">https://tableless.com.br/elevacao-ou-JavaScript-hoisting/</a>

Hoisting: <a href="https://scotch.io/tutorials/understanding-hoisting-in-JavaScript">https://scotch.io/tutorials/understanding-hoisting-in-JavaScript</a>

---

# ORIENTAÇÃO A OBJETOS

## PROPRIEDADES E MÉTODOS

Um objeto possui propriedades e métodos. Para criar um novo objeto basta associar o valor **{}** a uma variável.

As **propriedades** de um objeto são variáveis. Nelas podemos associar valores e acessá-los posteriormente.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_d8f26a6e.png" widgth = 50>

No exemplo acima, **descricao** e **estaFeita** são propriedades do objeto **tarefa**.

Métodos são propriedades que possuem como valor associado uma função.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_605db339.png" widgth = 50>

No exemplo acima, o objeto **tarefa** possui um método chamado **marcar()**. Dentro de um método o objeto que chamou a função é representado pela palavra-chave **this**. Então se quisermos nos referenciar a alguma propriedade do próprio objeto, seja para usá-la ou para alterar seu valor, basta escrever **this.nomeDaPropriedade**.

---

## PROTOTYPES

Além das propriedades e métodos que definimos, os objetos do JavaScript possuem alguns métodos por padrão. Por exemplo, o método **toString()** está presente em todos os objetos.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_a14c7409.png" widgth = 50>

Esses métodos e propriedades estão definidos no **prototype** do objeto. O **prototype** de um objeto é um outro objeto interno que possui métodos e propriedades definidas. Podemos ter acesso a ele utilizando o método **Object.getPrototypeOf()**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_f38b9ae4.png" widgth = 50>

O tipo padrão de **prototype** de um objeto é o **Object.prototype**, de um array é o Array.prototype e de uma função é o **Function.prototype**.

Quando nós chamamos um método ou uma propriedade de um objeto e esse método ou propriedade não está declarada nele, o JavaScript procura por esse método ou propriedade no **prototype** do objeto.

Caso queira criar um objeto com um **prototype** específico utilize a função **Object.create()**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_9b943797.png" widgth = 50>

Assim, um novo objeto é criado e o **prototype** do objeto será o objeto que você passar como parâmetro para a função. Caso você queira criar um objeto que não possui um **prototype**, passe **null** como parâmetro.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_81df4a5.png" widgth = 50>

---

## CONSTRUCTORS

Para criar objetos que compartilham o mesmo **prototype**, a maneira mais simples é utilizar um constructor. Se você chamar uma função com a palavra-chave **new** em frente a ela, o JavaScript irá tratar aquela função com um constructor. Um objeto criado a partir de um constructor com a palavra-chave **new** é chamada de uma **instância** daquele constructor.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_25c62f84.png" widgth = 50>

Por convenção, funções que definem constructors começam com letra maiúscula. Isso facilita diferenciar uma função normal de um constructor.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_eacd5417.png" widgth = 50>

Criar um objeto a partir de um constructor possui uma diferença que é a de apenas criar um objeto; o **prototype** do objeto deixa de ser o padrão **Object.prototype** e passa a ser o **prototype** da função que gerou aquela instância.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_c6eb69af.png" widgth = 50>

Todos os constructors possuem uma propriedade chamada **prototype** que é um objeto vazio derivado de **Object.prototype**. Podemos adicionar métodos a um constructor adicionando função à sua propriedade **prototype**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_e7cb6b0f.png" widgth = 50>

Alterando a propriedade **prototype** de um constructor, você automaticamente altera o **prototype** de todas as instâncias daquele constructor.

Preste muita atenção na diferença entre a propriedade **prototype** de um constructor e o **prototype** da função construtora. O **prototype** da função construtora é **Function.prototype**. A propriedade **prototype** da função construtora é o protótipo das instâncias que serão criadas a partir daquele constructor.

---

## GETTER E SETTER

Podemos definir dois métodos associados a uma propriedade de um objeto, o método **get** e o método **set**.

- **get**: chamado sempre que tentamos ler o valor de uma propriedade.

- **set**: chamado quando associamos um valor a uma propriedade.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_241cc594.png" widgth = 50>

Para definir uma propriedade em uma função construtora, podemos utilizar a função **Object.defineProperty()** passando como parâmetros o **prototype** no qual queremos adicionar uma propriedade, o nome da nova propriedade e as configurações dessa propriedade.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_6fda82fd.png" widgth = 50>

---

## HERANÇA

Quando falamos de orientação a objetos pensamos em três conceitos principais: encapsulamento, polimorfismo e herança.

Herança é a capacidade de uma classe herdar os atributos e métodos de uma outra classe. Chamamos a classe de quem estamos herdando de **classe-pai** e a classe que herdará os atributos e métodos de **classe-filha**.

No JavaScript a herança se dá pelo compartilhamento de protótipos. Vamos, por exemplo, criar um *constructor* de objetos que representarão alimentos. Ele terá um atributo **sabor** que irá armazenar a descrição daquele alimento e um método **souGostoso()** que irá dizer se o alimento é gostoso ou não.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_cbf1fd2c.png" widgth = 50>

Lembremos que criamos o método na propriedade **prototype** do nosso *constructor* pois essa propriedade é que irá constituir o protótipo das instâncias criadas a partir dele.

Agora vamos criar um *constructor* de objetos que representarão frutas. Nós queremos que nossas frutas possuam os mesmos atributos de um objeto **Alimento**, então nosso objetivo é herdar as propriedades e métodos do *constructor* **Alimento**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_fd55cf50.png" widgth = 50>

O que fizemos foi definir o constructor **Fruta** e dentro chamamos o *constructor* **Alimento**. A diferença é que usamos um método chamado **call()**. Esse método recebe como parâmetro o contexto que chamou aquela função e depois disso todos os parâmetros necessários para a chamada daquela função.

Então, o que efetivamente aconteceu quando criamos uma instância de **Fruta** foi:

- O *constructor* Fruta executou o *constructor* Alimento.

- Uma referência do objeto fruta, **this**, foi passada para o método **call()**, então todas as propriedades referentes ao objeto instanciado pelo *constructor* **Alimento** foram atribuídas para o objeto **Fruta** sendo instanciado.

- O parâmetro **sabor** foi passado para o construtor **Alimento**, que o utilizou para instanciar o novo objeto.

- Uma instância do objeto **Fruta** foi criada com todas as propriedades definidas no *constructor* **Alimento**.

Assim, nós conseguimos herdar as propriedades definidas no *constructor* **Alimento**. Porém, nós ainda não temos acesso aos métodos definidos na classe-pai.

Para ter acesso aos métodos temos que igualar a propriedade **prototype** do *constructor* **Fruta** com a propriedade **prototype** da classe-pai, **Alimento**.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_32dc044b.png" widgth = 50>

Para sobrescrever um método da classe-pai basta redefini-lo na propriedade **prototype** da classe-filha.

<src img="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/18c096107ae3bd615325a78c56832df6_html_e780ce56.png" widgth = 50>

Temos que dar essa volta toda para utilizarmos o conceito de herança, pois o JavaScript não possui o conceito de classes, onde são definidos todas as propriedades e métodos que os objetos instanciados a partir dela irão possuir. No JavaScript temos apenas objetos. Os protótipos são os templates em que os objetos estão baseados. É nele que as propriedades iniciais dos objetos instanciados a partir de um *constructor* são definidas.

Como cada **prototype** de um objeto também é um objeto, o **prototype** de um objeto também possui uma propriedade **prototype** e a propriedade **prototype** deste objeto também possui uma propriedade **prototype** e assim por diante, até chegarmos ao último objeto **prototype** nessa cadeia, o qual a sua propriedade **prototype** possui o valor associado null. A isso damos o nome de *prototype chain*, ou **cadeia de protótipos**.

---

## LINKS DE REFERÊNCIA

Objetos:<br>
<a href="http://eloquentjavascript.net/06_object.html">http://eloquentjavascript.net/06_object.html</a>

Object-oriented Programming:<br>
<a href="http://eloquentjavascript.net/1st_edition/chapter8.html">http://eloquentjavascript.net/1st_edition/chapter8.html</a>

Objetos:<br>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects</a>

Class vs Prototype:<br>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Details_of_the_Object_Model#Class-based_vs._prototype-based_languages">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Details_of_the_Object_Model#Class-based_vs._prototype-based_languages</a>

Herança no JavaScript:<br>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Details_of_the_Object_Model#Property_inheritance_revisited">https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Details_of_the_Object_Model#Property_inheritance_revisited</a>

Cadeia de protótipos:<br>
<a href="https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain">https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain</a>