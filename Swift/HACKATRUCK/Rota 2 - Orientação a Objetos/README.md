# CONCEITOS INICIAIS

## INTRODUÇÃO

Vamos adentrar mais um pouco no mundo da programação. Começaremos, nesse módulo a ver Orientação a Objetos, entendendo o que são esses objetos e como representá-los.

Orientação a Objetos (OO) é um paradigma utilizado para representar elementos do mundo real dentro das nossas aplicações; com ela é possível criar programas componentizados deixando partes com responsabilidades comuns agrupadas. Essas partes se comunicam por meio de mensagens e são chamadas de Objetos.

Conceitualmente, a Orientação a Objetos consiste na identificação dos objetos e de seus processamentos. O termo Objeto é utilizado para representar elementos do mundo real, onde tudo ao seu redor são exemplos de objetos: carro, mesa, janela, livro, pessoa, etc.

Veremos os conceitos de forma introdutória e depois aprofundaremos cada um deles. Dessa forma, vamos conhecer: Classes, Objetos, Propriedades, Métodos, Encapsulamento, Herança e Polimorfismo.

---

## CLASSES

As classes podem ser exemplificadas por meio de agrupamentos que fazemos por semelhanças. Por exemplo, pense em um carro como um grupo, onde cada carro, seja ele utilitário ou passeio (diferentes categorias de carro), possui propriedades e atributos comuns a ambos. Exemplo de classe:

```
class Carro {
    // Seus atributos e metodos podem ser definidos aqui. 
}
```

Dessa forma, declaramos uma classe chamada Carro.

---

## OBJETOS

Um objeto, de forma bem sucinta, pode ser definido como qualquer coisa que você vê e que "cabe" em uma classe específica. Exemplos: Gato, Cachorro, Baleia, Caneta, Lápis, Borracha, etc. A partir do nosso exemplo, a classe Carro, podemos exemplificar criando, saveiro e gol. Ambos serão objetos pertencentes à mesma classe, Carro. Código:

```
class Carro{
    // Seus atributos e metodos podem ser definidos aqui. 
}

let saveiro  = Carro () // criamos um objeto de Person
let gol  = Carro () // criamos um objeto de Person
```

Dessa forma, declaramos dois objetos instanciando a classe Carro.

---

## PROPRIEDADES

Vamos voltar ao nosso exemplo da classe Carro. Como dito anteriormente, cada carro possui alguns atributos, propriedades e métodos comuns, ou seja, independentemente de ter uma determinada categoria, marca e modelo, todos possuem ano, cor, etc. Todas as informações podem ser chamadas de propriedades da classe Carro. Então, chegamos ao seguinte cenário: as propriedades são os atributos comuns dessa classe que serão compartilhados para cada objeto criado a partir dela. Vamos ver isso na prática: 

```
class Carro {
    
// 1
    var ano: Int? // Estas são algumas das propriedades da classe Carro
    var marca: String?
    var modelo: String?
    var versao: String?
    var cor: String?
}
```

Nessa primeira etapa da nossa classe, criamos algumas propriedades de carro.

**💡 Repararam que utilizamos um “?” (sinal de interrogação) após o nome das variáveis? Veremos o porquê mais adiante, mas já adiantando, eles são chamados de “Opcionais”, ou seja, em algum momento estas variáveis podem não ter nenhum valor.**

---

## MÉTODOS

Métodos/funções são os comportamentos dos objetos de uma Classe. Digamos que todo carro pode:

- Andar

- Dar ré

- Buzinar

Essas e outras ações ocorrem independentemente de qual dos objetos estivermos falando (Saveiro, Gol, etc.). Essas ações podem vir a ser os métodos/funções da classe.

Vamos adicionar à nossa classe exemplo Carro, estes métodos?

```
class Carro {
    
// 1
    var ano: Int? // Estas são algumas das propriedades da classe Carro
    var marca: String?
    var modelo: String?
    var versao: String?
    var cor: String?
    
    func andar(){
        print("Andando para frente")
    }
    
    func darRe(){
        print("Andando para trás")
    }
    
    func buzinar(){
        print("BIIIIIIP BIIIIP BIIIP")
    }
}
```

---

## ENCAPSULAMENTO

Através do encapsulamento podemos definir diferentes níveis de acesso para as classes, propriedades e métodos. Utilizamos deste conceito quando queremos controlar como nossas classes, objetos e propriedades serão acessados por outras classes ou objetos dentro da aplicação. Por meio deste conceito, conseguimos ter mais segurança e controle. Existem alguns níveis que abordaremos mais à frente no capítulo específico. Um exemplo para facilitar o entendimento pode ser o saldo bancário de um cliente. Ele não pode ser de acesso público, pois isso definiria que qualquer outra parte do programa poderia alterar esse valor. Neste caso, definimos a variável como privada (palavra reservada ***private***), e assim ela será controlada apenas por métodos que irão conter mecanismos de segurança.

```
class Correntista {
    
    var nome: String = "Leandro"
    
    //Criamos a propriedade privada
    private var saldo: Double = 1000

}

//Criamos o objeto da classe
var pessoa1 = Correntista()
       
pessoa1.saldo = 2.50
//Resultado: erro

```

**💡 É possível observar a mensagem de erro dizendo que não podemos alterar o valor da variável por ser inacessível e ser privada. Veremos no capítulo específico de “Encapsulamento” a forma correta de alterar, nesses casos. É válido lembrar que estamos trabalhando com um simulador. Encapsulamento, no Swift, funciona se e somente se estivermos trabalhando com a instância e a classe em arquivos separados!**

---

## HERANÇA

A herança é um poderoso procedimento onde se herda as propriedades em comum de uma classe pai, também conhecida como superclasse, para serem utilizadas em classes filho. Por exemplo, vamos imaginar que uma fábrica de automóveis resolve fabricar novos estilos de veículos, como motocicletas e ônibus, os mesmos possuem diferentes processos para produção, mas todos possuem, motor, número de assentos, número de rodas, certo? Esse compartilhamento de propriedades pode se dar por meio de herança, onde todas as classes têm características em comum e herdam de uma superclasse. Veremos exemplos ilustrados no capítulo específico para facilitar o entendimento.

---

## POLIMORFISMO

A ordem dos nossos insights sobre POO (Programação Orientada a Objetos) é incremental, então, conseguimos ir construindo o conhecimento pouco a pouco. Para falar sobre polimorfismo utilizaremos dos conceitos de herança. Nos baseando no exemplo de criarmos uma montadora, conseguimos pensar e afirmar, por exemplo, que todos os veículos buzinam, mas a buzina de um ônibus, de um carro e uma moto têm diferenças! Isso é polimorfismo, características em comum, mas com execuções diferentes. Aprofundaremos, no capítulo específico, com implementações e ilustrações.

---

# CLASSES

## INTRODUÇÃO

Classe é um termo utilizado em Orientação a Objetos (OO) para designar um grupo de elementos com determinadas características. Uma classe pode ser considerada como uma base sobre a qual serão criados os objetos, com atributos e métodos, ou seja, ela descreve as características e comportamentos. A composição de uma classe se dá por 3 postos-chaves, o **NOME** da classe, o conjunto de **ATRIBUTOS** da classe e por fim o conjunto de **MÉTODOS** da classe. Vamos ver alguns exemplos de classe:

```
class Person {
    var nome: String?
    var sobrenome: String?
     
    func nomeCompleto() {
        print(" \(self.nome ?? " ") \(self.sobrenome ?? " ")")
    }
}
```

```
class Carro {
    var ano: Int? // Estas são algumas das propriedades da classe Carro
    var marca: String?
    var modelo: String?
    var versao: String?
    var cor: String?
    
    func descricao(){
        print("O carro \(self.modelo!) da marca \(self.marca!), versao \(self.versao!) e ano \(self.ano!), é da cor \(self.cor!)")
    }
}
```

```
class Correntista {
    var nome: String?
    
    //Criamos a propriedade privada
    private var saldo: Double = 1000
    
    //Criamos o método que altera o Saldo
    func mudarSaldo(novoSaldo: Double){
        
        saldo = novoSaldo
    }
    
    func verSaldo(){
        print(saldo)
    }   
}
```

As classes, como podemos ver, são a implementação (descrição) do que virá a ser um objeto. Dessa forma, as classes possuem atributos e métodos. Deixaremos 2 descrições para irem se acostumando:

- **CLASSE**: é a descrição geral (implementação) de um objeto, com atributos e métodos;

- **OBJETO**: é uma instância de uma classe, com valores específicos para os atributos.

Não se preocupe se a definição de objeto não ficou clara ainda, debateremos mais à frente, ainda neste capítulo! Por ora, voltemos à definição de classe e suas observações.

Para definirmos uma classe necessitamos:

- O **nome** da classe;

- O nome e tipo das suas variáveis (**atributos**);

- O nome e especificação das suas funcionalidades (**métodos**).

Classe = Nome + Atributos + Métodos.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/oo/2._Classes_-_01.png" width = 400>

A classe acima pode ser instanciada, por exemplo, nos seguintes objetos:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/oo/2._Classes_-_02.png" width = 400>

Em termos de implementação, a definição da classe e a instanciação dos objetos do exemplo acima, podem ser feitos da seguinte forma:

```
class Person { 

    var nome: String?
    var sobrenome: String?     
    
    func nomeCompleto() {
        print(" \(self.nome ?? " ") \(self.sobrenome ?? " ")")
    }
}

var p1 = Person()
var p2 = Person()
var pN = Person()
```

É como se criássemos realmente o esqueleto de algo, e quando os atributos receberem os valores, por meio do objeto, ganharão vida.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/oo/2._Classes_-_03.png" width = 400>

O modelo (classe) estabelece as características e o comportamento que o objeto deve ter de forma genérica, propiciando que cada objeto, com seus respetivos valores, tenha seus atributos próprios. Outra característica das classes é que elas são conceitos facilmente identificadas na especificação dos sistemas, geralmente, descritas como substantivos. Assim, a classe é um conceito estático que, uma vez definido, permanece como está. Para o desenvolvimento de software são definidas as classes a serem utilizadas e seus inter-relacionamentos. Isso é feito na etapa de projeto, quando o software está sendo desenhado/modelado.

Uma vez com as classes definidas, são iniciados os procedimentos de definição para atributos e métodos.

---

## ATRIBUTOS

Os atributos são as propriedades da classe e servem para descrever o esqueleto da classe e representá-la.  Se lembram das variáveis e tipos? São elas que serão utilizadas para definir nossos atributos. Vamos criar uma classe e treinar? Criem uma classe chamada Musica, e adicionem os atributos que vocês imaginam para música.

**<a href="./Códigos/main01.swift">Código</a>**

Possível implementação:

```
//Criem uma classe chamada Musica, e adicione os atributos que vocês imaginam pra música.

class Musica {
    var nome: String?
    var artista: String?
    var album: String?
    var anoLancamento: Int?
    var duracao: Double?
    var rating: Int? //Nota de 0-5 por exemplo
    var linkToPlay: String? 
}
```

**Tudo o que foi aprendido em “Variáveis e Constantes” pode e deve ser utilizado ao declarar atributos!**

---

## MÉTODOS

As ações que um objeto pode executar são chamadas de métodos. Elas definem o que será possível executar a partir dos objetos dessa classe. Um método em uma classe é apenas uma predefinição, pois a execução se dá por meio do objeto.

Uma classe, normalmente, tem diversos métodos, e cada um deles possui sua assinatura composta por um nome, o tipo de dado do retorno e sua lista de argumentos, sendo estes identificados por tipo e nome. Como vimos em “Funções”, os métodos são iniciados com a palavra reservada **func**, nome e os parâmetros, e logo após o tipo de retorno (tipo que será retornado após a execução). Vamos ver a sintaxe seguida de exemplos:

```
//Execução dará erro, exemplo teórico

func nomeDoMetodo() {
    //Corpo do método
}

func nomeDoMetodo() -> tipoDeDadoDoRetorno {
    //Corpo do método
}

func nomeDoMetodo (nomeDoParametro : tipoDoParametro) -> tipoDeDadoDoRetorno {
    //Corpo do método 
}

//Execução dará erro, exemplo teórico
```

```
//Criem uma classe chamada Musica, e adicione os atributos que vocês imaginam pra música.

class Musica {
    var nome: String?
    var artista: String?
    var album: String?
    var anoLancamento: Int?
    var duracao: Double?
    var rating: Int? //Nota de 0-5 por exemplo
    var linkToPlay: String? 

    func quemCanta(){
        print("O nome do artista é:" + artista!)
    }   
    
    func tocar()
    {
        print("Clique para ouvir:" + linkToPlay!)
    }
    
    func feat( participante : String ) -> String {
        return "o artista \(artista!) canta a música \(nome!)  com participação de \(participante)"    
    }
    
    func nota() -> Int{
        return rating!;
    }
}
```

Identificamos atributos e ações compartilhadas por qualquer item da categoria música. Embora cada item tenha seus valores, nossos métodos estão preparados para estas especificidades, ou seja, para cada música que chamarmos o método, ele fará o mesmo processamento, mas com valores distintos. Dessa forma, afetamos somente quem solicitou a ação. Veremos mais na sessão “Objetos”!

---

## OBJETOS

Um programa orientado a objetos é composto por um grupo de objetos que se comunicam através de mensagens. Um objeto é capaz de armazenar atributos e executar ações como resposta a mensagens recebidas, tal como, enviar mensagens a outros objetos. Essa troca de mensagens pode ser acionada nos objetos por meio dos métodos.

Quando criamos um objeto, o mesmo requer um espaço em memória, para assim conseguir armazenar seus atributos e seus métodos (conjuntos de ações que são definidas para o objeto).

Exemplos de objetos do tipo Humano: José, Maria, Joaquim, etc.

**💡 Repararam que Humano foi escrito com letra maiúscula? Humano? Referencia a classe e o tipo, então, uma outra possibilidade seria dizer objetos da classe Humano.**

No mundo real observamos duas características marcantes: **ESTADO** e **COMPORTAMENTO.**

O estado de um objeto nos diz sobre as propriedades dele.

Por exemplo:

- Uma pessoa tem: idade, peso, altura, cor de cabelo, cor de pele.

- Um carro tem: rodas, cor, quantidade de lugares, ano de fabricação.

Em Orientação a Objetos chamamos essas propriedades de **Atributo**.

Já o comportamento nos diz sobre as ações que ele pode exercer/executar.

Por exemplo:

- Uma pessoa pode: andar( ), falar( ), ouvir( ), pular( ).

- Um carro pode: acelerar( ), frear( ), buzinar( ).

Em Orientação a Objetos chamamos esses comportamentos de **Métodos**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/oo/2._Classes_-_04.png" width = 400>

Os objetos podem representar conceitos reais (pessoa, animal, carro, pizza, etc.) ou abstratos (conta poupança, funcionário, pessoa física, etc.).

Cada objeto tem suas próprias “cópias” do que foi definido na classe, ou seja, cada um deles tem seus próprios atributos e métodos. Cada cópia representa uma instância daquela classe. Por exemplo: o carro 1, o carro 2 e o carro 3 são instâncias de Carro.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/oo/2._Classes_-_05.png" width = 400>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/oo/2._Classes_-_06.png" width = 400>

Vamos exemplificar e ver as definições do exemplo acima em código:

```
class Carro {
    var ano: Int? // Estas são algumas das propriedades da classe Carro
    var marca: String?
    var modelo: String?
    var versao: String?
    var cor: String?
    
    func descricao(){
        print("O carro \(self.modelo!) da marca \(self.marca!), versao \(self.versao!) e ano \(self.ano!), é da cor \(self.cor!)")
    }
}

var carro1 = Carro()
var carro2 = Carro()
var carro3 = Carro()

carro1.cor = "Laranja"
carro1.ano = 1980
carro1.modelo = "Fuxca"
carro1.versao = "Turbo Shift Auto"
carro1.marca = "WW"

carro2.cor = "Azul"
carro2.ano = 1980
carro2.modelo = "Fuxca"
carro2.versao = "Turbo Shift Auto"
carro2.marca = "WW"

carro3.cor = "Verde"
carro3.ano = 1980
carro3.modelo = "Fuxca"
carro3.versao = "Turbo Shift Auto"
carro3.marca = "WW"

print(carro1.descricao())
print(carro2.descricao())
print(carro3.descricao())
```

**Saída**

```
O carro Fuxca da marca WW, versao Turbo Shift Auto e ano 1980, é da cor Laranja
()
O carro Fuxca da marca WW, versao Turbo Shift Auto e ano 1980, é da cor Azul
()
O carro Fuxca da marca WW, versao Turbo Shift Auto e ano 1980, é da cor Verde
()
```

No exemplo, conseguimos ver que é possível criar N (diversos) objetos a partir de um só modelo (classe), cada qual com seus atributos e valores. Quando executamos a função descricao( ), ela traz o estado atual com os valores atuais pertinentes ao objeto relativo à chamada, então, concluímos que cada objeto é capaz de executar suas próprias operações.

---

## MENSAGENS

Um objeto isolado em um sistema não tem significado. Para que o mesmo seja útil, ele deve se relacionar com outros objetos e partes do sistema, viabilizando a troca de informações e o processamento dos dados. Essa comunicação se dá por meio de mensagens que trafegam a partir dos métodos. Veja as definições sobre mensagens:

- **Mensagens enviadas para as variáveis:** são as mensagens que resgatam ou alteram os valores de variáveis.

- **Mensagens enviadas para os métodos:** são mensagens que desencadeiam a realização dos métodos de cada objeto (chamadas dos métodos).

Uma mensagem enviada para um método deve ser composta por três partes:

- Um destino - objeto que receberá a mensagem;

- Nome do método a ser invocado pela mensagem;

- Parâmetros necessários para o método invocado.

Note que além desses três aspectos, a mensagem também pode receber uma resposta no formato do retorno do método invocado.