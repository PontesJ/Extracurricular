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

---

# ENCAPSULAMENTO

Na programação orientação a objetos dizemos que um objeto possui uma interface, ou seja, o que ele conhece e o que sabe fazer. Por meio da interface é possível saber quais serviços podem ser executados e também as mensagens que o objeto recebe. Através do conceito de encapsulamento podemos definir e limitar o acesso por meio de diferentes níveis para as classes, atributos e métodos.

Utilizamos encapsulamento quando queremos definir como nossas classes, propriedades e métodos serão acessados por outras classes ou objetos dentro da aplicação. Este impõe diferentes restrições de acesso direto às informações trazendo mais segurança, integridade aos dados e controle durante o desenvolvimento, pois quando chamamos um método, não é necessário saber o que ele faz, mas sim como chamá-lo. A fim de nos beneficiarmos desse cenário com diferentes possibilidades, utilizamos algumas palavras reservadas para indicar e delimitar quem acessa o que, fazendo com que as classes, atributos e métodos, sejam visíveis somente onde é estritamente necessário.

Existem três níveis de encapsulamento no Swift:

- ***public*** – Permite acesso a qualquer outro elemento e por qualquer função.

- ***internal*** – Permite acesso apenas dentro da própria classe e nas classes herdeiras. Aprofundaremos sobre este conceito no próximo capítulo (4 – Herança).

- ***private*** – Permite acesso apenas pela própria classe.

Um exemplo de encapsulamento é a variável saldoBancario de um cliente de banco. Ela não pode ter um acesso público, senão qualquer parte do programa poderia mudar o seu valor. Neste caso, definimos a variável como privada para que seu valor seja alterado usando somente os mecanismos da classe que tem suas devidas travas e regras para cada operação (saque, transferência, extrato, etc.).

**Nota:** por padrão, o nível de encapsulamento é *internal.*

Vamos a um exemplo:

Criaremos uma classe Carro, com uma das propriedades como *private*, que pode ser acessada apenas pela própria classe, e tentaremos alterá-la com uma nova atribuição por meio de um objeto:

```
class Carro {
    var modelo: String = "Gool"
    
    //Criamos a propriedade privada
    private var qtdeCombustivel: Float = 25
    
    func quantidadeCombustivel()->Void{
        print(qtdeCombustivel)
    }
}

//Criamos o objeto da classe
var carro1 = Carro()

//Tenta fazer a alteração da qtdeCombustivel, atribuindo diretamente no atributo qtdeCombustivel       
carro1.qtdeCombustivel = 35
//Resultado: erro
```

Obtivemos um erro, pois nossa propriedade qtdeCombustivel é *private*, e não pode ser alterada por nada que não seja da própria classe.

Dissemos anteriormente que nossos conceitos de encapsulamento podem ser aplicados tanto a atributos como a métodos, então vamos nos aproveitar disso para conseguir fazer essa alteração de valor. Conseguem pensar em uma solução viável para modificar o valor da variável qtdeCombustivel?

```
class Carro {
    var modelo: String = "Gool"
    
    //Criamos a propriedade privada
    private var qtdeCombustivel: Float = 25
    
    //Criamos o método que abastece o carro
    func abastecer(qtdeLitros: Float)->Void{
        qtdeCombustivel += qtdeLitros
    }
    
    func quantidadeCombustivel()->Void{
        print(qtdeCombustivel)
    }
}

//Criamos o objeto da classe
var carro1 = Carro()
   
//Faz a alteração da qtdeCombustivel, usando o método da classe
carro1.abastecer(qtdeLitros: 35)
carro1.quantidadeCombustivel()
//Resultado: 35
```

**Saída**

```
60.0
```

Sim, com o uso de um método! Utilizando um método que é acessível externamente conseguimos modificar os valores atribuídos na classe.

Encapsular não é algo mandatório para o funcionamento do programa, mas é uma boa prática para que nossa estrutura seja sólida e nossos objetos sejam seguros do ponto de vista de escrita e leitura, pois ambas as operações só serão feitas de dentro da própria classe se forem declarados como privados.

**💡 O encapsulamento do Swift funciona apenas se a classe e sua instância estiverem em arquivos separados. Apenas para efeito de ensino, mantivemos no mesmo simulador.**

---

# HERANÇA

Herança é um conceito muito importante em Orientação a Objetos (OO), pois permite uma melhor organização e reaproveitamento de código. Por meio desse conceito, as classes *filhas* compartilham os atributos e métodos da *classe mãe*.

Os apelidos “classe pai”, “classe mãe”, “supertipo”, “superclasse” e “classe base” são a mesma coisa, então não se assuste ao ver algum desses termos, pois todos se referem à classe original a ser herdada.

Já os termos “classe filha”, “subtipo”, “subclasse” e “classe derivada” também são sinônimos, e se referem às classes que herdam os atributos e métodos de uma superclasse.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/oo/4._Heranca_-_01.png" width = 400>

Para dizer que uma classe herda o comportamento de outra, usamos a palavra **“estende”**. No exemplo abaixo veremos “Carro estende Veiculo”, onde a classe Carro é a subclasse e a classe Veiculo é a superclasse. Desse modo, Carro terá todos os atributos públicos da classe Veiculo, e também poderá utilizar seus métodos públicos (ou até mesmo modificá-los, se necessário, conforme veremos no capítulo de Polimorfismo). É justamente por isso que dizemos que as classes filhas herdam o comportamento das classes mães, e também podem acrescentar outras características (atributos) ou novas funcionalidades (novos métodos). É importante notar que herança também segue os princípios de visibilidade e encapsulamento, portanto, o que é privado em uma classe não será observado nas suas subclasses.

O conceito de herança está claramente relacionado com o conceito de **“é um(a)”**. No nosso exemplo anterior, Carro é um Veículo. A herança também se relaciona com os conceitos:

**Generalização** - Quando partimos de uma classe e chegamos à sua superclasse. 

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/oo/4._Heranca_-_02.png" width = 400>

**Especialização** - Quando partimos de uma superclasse e chegamos na sua subclasse.

Assim, Carro é uma especialização de Veiculo e Veiculo é uma generalização de Carro. Do mesmo modo será com qualquer outro meio de transporte se definirmos que “MeioDeTransporte estende Veiculo”. Isso exemplifica outro ponto relevante: uma superclasse pode ser estendida por infinitos subtipos, no entanto, um subtipo ***NORMALMENTE*** herda as características de uma única superclasse por vez.

**💡 É possível herdar mais de uma superclasse com o uso de Protocolos, mas não se preocupem com isso neste momento, apenas saibam que é possível!**

Vejamos nosso exemplo acima em código:

```
class Veiculo{
    var pneus: String?
    var assentos: String?
    var motor: String?
    
    func desc() {
        print("Número de rodas \(self.pneus ?? " "), Número de Assentos \(self.assentos ?? " "), Potencia Motor \(self.motor ?? " ")") 
    }
}

class Carro: Veiculo {
    var tipo: String?
}

class Caminhao: Veiculo {
    var tipo: String?
    var eixos: Int?
}

class Motocicleta: Veiculo {
    var cilindradas: Int?
}

class Aviao: Veiculo {
    var numMotores: Int?
}

var c = Caminhao()
c.pneus = "TY607 295/80 R22,5"
c.assentos = "3 Lugares"
c.motor = "V8"
c.tipo = " Caçamba "
c.eixos = 5
c.desc()
```

**Saída**

```
Número de rodas TY607 295/80 R22,5, Número de Assentos 3 Lugares, Potencia Motor V8
```

**Vamos treinar?**

Corrija os erros, instancie um objeto e adicione valores para Motocicleta e Avião. Usem como exemplo o código disponibilizado no exemplo anterior:

```
class Veiculo{
    var pneus: String?
    var assentos: String?
    var motor: String?
    
    func desc() {
        print("Número de rodas \(self.pneus ?? " "), Número de Assentos \(self.assentos ?? " "), Potencia Motor \(self.motor ?? " ")") 
    }
}

class Motocicleta {
    var cilindradas: Int?
}

class Aviao, Veiculo {
    var numMotores: Int?
}
```

**<a href="./Códigos/main02.swift">Código</a>**

---

## HERANÇA - CONTINUAÇÃO

Como vimos nos exemplos anteriores, podemos também adicionar atributos na subclasse, e isso se estende também a adicionar novos métodos, a fazer overloading, e até mesmo reescrevê-los, overriding (detalharemos no próximo capitulo essa definição).

Vejamos os exemplos a seguir: 

```
class Veiculo{
    var pneus: String?
    var assentos: String?
    var motor: String?
    var cidadeDeRegistro: String?
    
    func desc() {
        print("Número de pneus \(self.pneus ?? " "), Número de Assentos \(self.assentos ?? " "), Potencia Motor \(self.motor ?? " ")") 
    }
    
    func registro() {
        print("Nossa cidade de registro é \(self.cidadeDeRegistro ?? " ")") 
    }
}

class Motocicleta: Veiculo {
    var cilindradas: Int?
    
    func descansar(){
         print("Farei paradas de 2h em 2h, o destino é Maresias.  \n") 
    }
}

class Aviao: Veiculo {
    var numMotores: Int?
    
    func voar () {
         print("Estamos a 1000 pés de altitude.") 
    }
}

var m = Motocicleta()
m.pneus = "2"
m.assentos = "2 Lugares"
m.motor = "2 cilindros"
m.cidadeDeRegistro = " Campinas "
m.cilindradas = 800
m.desc()
m.descansar()

var a = Aviao()
a.pneus = "4"
a.assentos = "12 Lugares"
a.motor = "Cirrus SR22 8000"
a.numMotores = 1
a.cidadeDeRegistro = " Campinas "
a.desc()
a.voar()
```

**Saída**

```
Número de pneus 2, Número de Assentos 2 Lugares, Potencia Motor 2 cilindros
Farei paradas de 2h em 2h, o destino é Maresias.  

Número de pneus 4, Número de Assentos 12 Lugares, Potencia Motor Cirrus SR22 8000
Estamos a 1000 pés de altitude.
```

Adicionamos novos atributos, cilindradas e numMotores respectivamente, e também novos métodos, descansar() para Motocicleta e voar() para Avião. Dessa forma, adicionamos comportamentos que são cabíveis somente para a realidade da própria classe.

Com o *overloading* (sobrecarga), conseguimos especificar mais o comportamento da classe por meio de novos métodos com o mesmo nome e ações distintas a serem executadas, e isso é fazer sobrecarga. Para que isso ocorra e se torne possível, existem as assinaturas dos métodos que consistem em validar a soma de **Nome do Método + (Tipo dos Parâmetros) + Tipo do Retorno**. Para que nosso conceito seja válido, essa soma não pode ser repetida, ou seja, precisamos de assinaturas únicas. Exemplos:

func calcula(a: Int, b: Int) -> retorno INT

func calcula(a: Double, b: Double) -> retorno DOUBLE

func calcula(a: String, b: String) -> retorno STRING

Então, podemos definir e criar um método mais genérico, e fazer nossas especificações somente por meio de diferentes assinaturas, ou seja, métodos com o mesmo nome, mas com diferenças nos parâmetros ou até mesmo no tipo de retorno. Estes seriam exemplos de diferentes assinaturas para o método calcula. Vamos olhar no código como eles se comportariam?

```
class Soma{
    func calcula( a : Int, b : Int) -> Int{
       return a+b;
    }
    
    func calcula(a : Double, b: Double) -> Double{
        return a+b;
    }
    
    func calcula(a: String, b: String) -> String{
        return a+b;
    }
}

var calc = Soma();

print( calc.calcula( a:1 , b:1 ));

print( calc.calcula( a:2.0 , b:2.1 ));

print( calc.calcula( a:"vi" , b:"ram?" ));
```

**Saída**

```
2
4.1
viram?
```