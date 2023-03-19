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