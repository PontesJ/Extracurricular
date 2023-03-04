# ALGORITMOS & LÓGICA DE PROGRAMAÇÃO

O termo algoritmo designa uma sequência de instruções bem definidas para chegarmos a um objetivo. Como “sequência bem definida de instruções”, devemos entender instruções claras que podem ser facilmente entendidas por quem vai executá-las e em uma ordem bem estabelecida. Apesar do termo algoritmo ser muito utilizado na matemática e computação, ele está presente em muitas atividades do nosso dia a dia. Toda vez que executamos algum processo que pode ser repetido através de um conjunto de instruções como trocar o pneu de um carro, dar o nó em uma gravata, cozinhar um prato utilizando uma receita, tocar uma música utilizando uma partitura ou cifras, estamos executando um algoritmo.

Computadores, apesar de sua grande capacidade em processar e calcular grandes volumes de informação de forma muito rápida, não são máquinas inteligentes. Para realizar qualquer tarefa, por mais simples que seja, é preciso que sejam atribuídos a eles um conjunto de operações que eles consigam compreender. Cabe, portanto, à capacidade de raciocínio humano indicar ao computador quais instruções devem ser efetuadas, e em qual ordem, para que ele processe as informações disponíveis de forma útil e adequada, ou seja, devemos informar qual algoritmo o computador deve executar para atingir o que desejamos. O que chamamos de programa é, portanto, um algoritmo escrito em uma linguagem que o computador consiga entender.

A palavra lógica se origina da palavra grega logos, que significa conhecimento, pensamento. Podemos traduzir lógica, dentro de nosso contexto, como a arte de pensar de forma correta e bem estruturada. Quando nos referimos à lógica de programação, estamos falando da estruturação de nossas ideias com o objetivo de resolver um problema utilizando o computador como ferramenta.

Quando pretendemos fazer isto, devemos entender o problema que queremos resolver, dividi-lo em problemas menores até chegarmos a problemas que sabemos resolver, ou melhor, em problemas que sabemos mostrar ao computador como ele deve resolver. Por fim, devemos unir as soluções destes pequenos problemas (sempre que possível utilizando o computador para isto) para finalmente chegarmos à solução do problema original.

Este curso se propõe a mostrar as operações básicas que um computador consegue executar, que são, portanto, os menores problemas que podem ser resolvidos por um computador. Através de exemplos e exercícios, mostraremos como podemos conectar estas operações de forma a resolvermos problemas mais complexos.

---

# PROGRAMA

Como vimos na introdução, um programa é um conjunto de instruções, também conhecido como algoritmo, que pode ser entendido e executado por um computador/dispositivo móvel. Para que isto ocorra, o algoritmo deve ser escrito no que chamamos de **linguagem de programação**.

Uma linguagem de programação é construída de forma que seja compreendida por seres humanos e também lida e executada por um computador.

Existem inúmeras linguagens de programação para os mais diversos fins (e gostos). Como exemplos, podemos citar: **Swift**, Java, C#, JavaScript, C, C++, Ruby, Pascal, Python, Visual Basic, COBOL, FORTRAN, LISP, PROLOG, entre uma infinidade de outras.

Como nosso curso é direcionado ao desenvolvimento de aplicativos para dispositivos móveis em iOS, utilizaremos nos módulos de Lógica de Programação e Orientação a Objetos, a linguagem **Swift**, assim, já nos familiarizaremos e aprenderemos a sintaxe da linguagem junto aos conceitos e operações básicas.

Programar é criar um conjunto de instruções para um dispositivo executar, sempre de forma objetiva e ordenada, com o intuito do programa ser compreendido e bem processado. Vamos a um exemplo:

Ao montar uma pizza temos a seguinte lista de ingredientes:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/1._Conceitos_Iniciais_-_01.png">

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

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/1._Conceitos_Iniciais_-_02.png">

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

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/logica/1._Conceitos_Iniciais_-_03.png">

Agora sim!  Montamos nossa pizza e conseguimos entender o quanto comandos imprecisos ou a falta deles podem nos levar a resultados inesperados!

**💡 Repararam que nossos comandos foram escritos com as palavras juntas e sempre terminando com parênteses ( )? Veremos o porquê mais adiante!**