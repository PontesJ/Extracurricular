# CONCEITOS INICIAIS

## JSON - JAVASCRIPT OBJECT NOTATION

A sigla JSON significa **Notação de Objetos JavaScript** (JavaScript Object Notation). Ele define um padrão para estruturar a informação de forma que ela seja legível tanto para humanos quanto para computadores.

Apesar de ter JavaScript no nome, o JSON não é um formato exclusivo da linguagem, ele apenas se baseia na forma com que o JavaScript define seus objetos para estruturar a informação. Várias linguagens possuem ferramentas para interpretar e analisar informações no formato JSON.

Exemplos de JSON:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/55cd7de87d6b1273baba3c51b0254be3_html_aacba98f.jpg" widgth = 50>

### VALIDAÇÃO DO JSON

Para que uma aplicação seja capaz de entender uma informação no formato JSON é importante que esta esteja formatada corretamente e, a fim de garantir a formatação correta é necessário validar a informação.

Para que um JSON seja válido é necessário que ele cumpra algumas regras de validação. Todas as regras de validação podem ser vistas em <a href="http://www.json.org/json-pt.html">http://www.json.org/json-pt.html</a>, o site oficial do formato.

As regras que listaremos a seguir foram retiradas diretamente da documentação do site.

Vamos dar prosseguimento aos estudos passando por cada uma delas.

---

## JSON - OBJETOS E ARRAYS

Ele precisa estar organizado em uma **coleção de pares nome/valor** ou numa **lista ordenada de valores**. Isso implica que a raiz do seu arquivo JSON precisa ser um **objeto** ou um **array**.

Um **objeto** é um conjunto desordenado de pares nome/valor. Um objeto começa com **{** (chave) e termina com **}** (chave). Cada nome é seguido por : (dois pontos) e os pares nome/valor são seguidos por , (vírgula), exatamente como um objeto JavaScript, porém o nome sempre deve ser uma string.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/55cd7de87d6b1273baba3c51b0254be3_html_ffaecdd4.jpg" widgth = 50>

Um **array** é uma coleção de valores ordenados. O array começa com [ (colchete) e termina com ] (colchete). Os valores são separados por , (vírgula).

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/55cd7de87d6b1273baba3c51b0254be3_html_8b239c05.jpg" widgth = 50>

Os tipos de valores que o formato JSON suporta são string, número, objeto, array, true/false e null. Sendo que string e número possuem suas próprias regras de validação.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/55cd7de87d6b1273baba3c51b0254be3_html_24c11f75.jpg" widgth = 50>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/55cd7de87d6b1273baba3c51b0254be3_html_81b76c75.jpg" widgth = 50>

### STRINGS E NÚMEROS

Para o JSON uma string é uma coleção de nenhum ou mais caracteres Unicode, envolvido entre aspas duplas usando barras invertidas como caractere de escape.

Um caractere está representado como um simples caractere de string. Uma cadeia de caracteres é parecida com uma cadeia de caracteres em C ou Java.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/55cd7de87d6b1273baba3c51b0254be3_html_472d6020.jpg" widgth = 50>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/55cd7de87d6b1273baba3c51b0254be3_html_eb1816d7.jpg" widgth = 50>

Um valor numérico no JSON é similar a um valor numérico nas linguagens C ou Java, exceto quando não se usa os números octais ou hexadecimais.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/55cd7de87d6b1273baba3c51b0254be3_html_19e1e686.jpg" widgth = 50>

Para validar um arquivo JSON é necessário que todas essas regras sejam seguidas, sem exceções. Caso algum aspecto da informação não esteja de acordo, como um objeto faltando uma chave de fechamento, uma vírgula a mais ou a menos ou uma string sem aspas duplas, o JSON é considerado inválido e as aplicações são incapazes de interpretá-lo.

Para validar seu JSON, você pode utilizar um serviço online, como o <a href="https://jsonlint.com/">JSON Lint</a>, para validação apenas, ou o <a href="myjson.com">MyJSON</a>, para validação e hospedagem.

---

## LINKS DE REFERÊNCIA

A seguir indicamos alguns links que podem complementar e enriquecer seu autoestudo.

JSON Official Site: <a href="http://www.json.org/json-pt.html">http://www.json.org/json-pt.html</a>

JSON: <a href="https://www.w3schools.com/js/js_json_intro.asp">https://www.w3schools.com/js/js_json_intro.asp</a>

JSON: <a href="https://pt.wikipedia.org/wiki/JSON">https://pt.wikipedia.org/wiki/JSON</a>

SON Syntax: <a href="https://www.w3schools.com/js/js_json_syntax.asp">https://www.w3schools.com/js/js_json_syntax.asp</a>

Formatação de Data: <a href="https://www.w3.org/TR/NOTE-datetime">https://www.w3.org/TR/NOTE-datetime</a>

JSON Lint: <a href="https://jsonlint.com/">https://jsonlint.com/</a>

MyJSON: <a href="http://myjson.com/">http://myjson.com/</a>

---

# NODE.JS

## INTRODUÇÃO

O Node.js nos permite construir aplicações escaláveis usando o JavaScript no lado do servidor. Ele utiliza o motor de JavaScript presente no navegador Google Chrome, o **V8 JavaScript Runtime**.

Exemplos de aplicações que podemos construir utilizando o Node:

- Um servidor de chat;

- Uma aplicação de upload de arquivos;

- Um servidor de propagandas;

- Aplicações *real-time* que atualizam ao vivo as informações, como um *dashboard* de acompanhamento, por exemplo.

A ferramenta **Node** não é, como podemos pensar inicialmente, um *framework web*, ele apenas providencia um arcabouço para que possamos construir aplicações utilizando JavaScript, com funcionalidades em nível de rede.

Podemos utilizar a ferramenta **Node** para executar arquivos JavaScript, porém se executarmos a ferramenta sem nenhum arquivo de código, ela irá abrir um *prompt* onde podemos digitar o código JavaScript e ver o resultado imediatamente.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_b5b88dc7.png" widgth = 50>

---

## CALLBACK

As principais características do Node.js são ele ser assíncrono e não-blocante (*non-blocking*). Operações “blocantes” são operações em que o processo do Node.js deve aguardar a conclusão de alguma operação externa para dar continuidade à execução do código.

Para operações de escrita e leitura, a biblioteca básica do Node.js oferece métodos que são executados de forma paralela. Esses métodos aceitam uma função para ser executada ao fim da execução do método, a ela damos o nome de ***callback***.

Vamos ver um exemplo de um código sem ***callback*** e um código com ***callback***.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_6657dc88.png" widgth = 50>

Nesse primeiro exemplo as operações ocorrem na ordem em que aparecem no código:

1. A função **lerArquivo** é chamada;

2. A função **lerArquivo** retorna um valor e o associa à variável **texto**;

3. Imprime o valor associado à variável **texto** no terminal;

4. Imprime a *string* 'Fim' no terminal.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_192a11b7.png" widgth = 50>

Nesse segundo exemplo, a função **lerArquivo** possui como segundo parâmetro uma função. Essa função recebe como parâmetro o resultado da leitura do arquivo para que possamos usá-lo quando o arquivo tiver sido lido. Essa função é o nosso ***callback***.

A ordem das operações ficaria mais ou menos assim:

1. A função **lerArquivo** é chamada;

2. Quando a função **lerArquivo** terminar de ler o arquivo ela irá chamar o ***callback*** passando o resultado como parâmetro;

3. Imprime a *string* 'Fim' no terminal.

É importante que você entenda bem o conceito de ***callback***, pois iremos utilizá-lo extensivamente no Node.js.

---

## MÓDULOS

Não precisamos criar do zero todo o código para construir nossas aplicações com Node.js. O próprio já possui uma série de funcionalidades implementadas para que possamos utilizar em nossas aplicações. Já temos implementados nativamente, por exemplo, funcionalidades para criar um servidor HTTP e para ler e escrever arquivos.

Essas funcionalidades ficam no que chamamos de módulos. Os módulos representam uma biblioteca de funcionalidades, já implementadas, que podemos importar para dentro do nosso código e utilizar. Isso faz com que não seja necessário reescrever estas funcionalidades todas as vezes que precisarmos delas.

Para importar um módulo para o seu código basta utilizar a função ***require***. Esta função não é nativa do JavaScript, porém o Node.js possui essa funcionalidade por padrão em seu ambiente. Portanto, podemos utilizá-la sem a necessidades de instalar o <a href="https://requirejs.org/">RequireJS</a>.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_4ccfe07b.png" widgth = 50>

Além de utilizar métodos de módulos já existentes, podemos criar nossos próprios módulos, além de baixar módulos da internet e utilizá-los em nossas aplicações.

Para criar nosso próprio módulo, basta implementar as funcionalidades em um arquivo de código e exportá-las ao fim do arquivo.

Veja o exemplo onde criamos o arquivo **greet.js**:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_6f0417fd.png" widgth = 50>

Agora se quisermos acessar essa função no nosso aplicativo, basta importar o arquivo usando a função ***require,*** armazenando o resultado da importação em uma variável.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_9965dc80.png" widgth = 50>

Temos dois pontos importantes na forma com que importamos nosso módulo. Não é necessário definir a extensão do arquivo, no caso **.js**, e quando colocamos **./** em frente ao nome do arquivo queremos dizer que o arquivo está localizado na mesma pasta que seu código.

Somos capazes de exportar mais de uma função do nosso módulo.

Vamos modificar nosso módulo **greet.js** e criar uma nova função que irá, além de cumprimentar a pessoa, dizer que horas são.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_9f60135d.png" widgth = 50>

Agora que temos duas funções diferentes sendo exportadas, ao invés de usar **module.exports** para deixá-las acessíveis por quem importa no nosso módulo, usaremos **exports**.nomeDaFuncao. Isso faz com que sejamos capazes de exportar cada uma individualmente. Quando importarmos este módulo no nosso aplicativo poderemos usar nossas funções dessa forma:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_d14293d5.png" widgth = 50>

Como a função ***require*** sabe onde buscar nosso módulo?

Quando chamamos a função ***require*** podemos definir o local do nosso módulo de diferentes maneiras. São elas:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_7a789b8b.png" widgth = 50>

- Com **./** nós indicamos que o módulo que estamos importando está na mesma pasta que seu código.

- Com **../** nós indicamos que o módulo está na pasta anterior à pasta onde está o seu código.

- Podemos definir o caminho absoluto da localização do nosso módulo.

- Quando apenas declaramos o nome do módulo, o ***require*** irá buscar por ele. Primeiramente, na pasta **node_modules** na mesma pasta que seu código.

Se o módulo não estiver presente na pasta **node_modules** da sua aplicação, então o ***require*** vai procurar por ele nas pastas:

1. *Home* do usuário: /Home/user/node_modules

2. *Home*: /Home/node_modules

3. *Root*: /node_modules

Quando o ***require*** procura pelo seu módulo na pasta **node_modules**, ele está procurando tanto por um arquivo de código JavaScript com o nome do seu módulo, quanto por uma pasta com o nome do seu módulo.

Nossos módulos podem ser mais complexos, importando outros módulos dentro dele, e por isso podemos agrupá-los em pastas. A estas pastas nós damos o nome de packages ou pacotes. Um pacote nada mais é do que um módulo que podemos importar na nossa aplicação. É uma boa prática que todo pacote tenha um arquivo chamado **package.json** onde ficam definidas várias características do pacote.

---

## MÓDULOS - NPM

Podemos instalar na nossa aplicação, pacotes desenvolvidos por terceiros e disponíveis online no repositório de pacotes do Node.js. Para isso, o Node.js possui uma ferramenta chamada **npm** (*Node Package Manager*). Com o **npm** nós somos capazes de instalar pacotes tanto na nossa aplicação quanto de maneira global.

Quando instalamos um pacote em nossa aplicação, é criada dentro da pasta da aplicação, uma pasta chamada **node_modules** onde ficam todos os pacotes instalados com o **npm**. Assim, podemos importar no nosso código, esse pacote em forma de um módulo.

Para instalar um pacote em nossa aplicação, basta abrir o terminal e entrar com o comando **npm install** nome_do_pacote **--save**, no diretório do seu projeto.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_890c4acc.png" widgth = 50>

Caso um pacote seja instalado de forma global, nós não somos capazes de importá-lo no nosso código. Ao invés de estar disponível como um módulo, o pacote é instalado como uma ferramenta de linha de comando e podemos utilizá-la apenas no terminal do computador.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_85a86a2e.png" widgth = 50>

É possível procurar por pacotes de três formas:

1. No repositório oficial de pacotes do Node.js no site <a href="https://www.npmjs.com/search">https://www.npmjs.com/search</a>.

2. No GitHub, site de repositórios de código online, pelo link <a href="https://github.com/search">https://github.com/search</a>.

3. Pela ferramenta **npm search** no terminal.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_3b4805b9.png" widgth = 50>

Sempre que você estiver escrevendo um código e pensar "Será que alguém já não escreveu um código para isso?", procure por um pacote de Node.js em uma dessas três fontes. A probabilidade é alta de que você encontre algo útil para seu projeto.

Como comentado um pouco acima, é uma boa prática que todo pacote tenha um arquivo chamado **package.json**. Também é importante que tenhamos um arquivo **package.json** em nosso projeto. Nesse arquivo ficam informações a respeito da aplicação e uma delas, são as **dependências do projeto**.

Para criarmos um esqueleto básico de **package.json** no nosso projeto podemos usar o comando **npm init**. Ele irá fazer uma série de perguntas, como o nome do projeto e a versão do projeto, sendo que ao final será criado na pasta do seu projeto um arquivo **package.json**, como o exemplo na imagem abaixo.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_6e425db0.png" widgth = 50>

**JSON** significa *JavaScript Object Notation*, ou seja, Notação de Objetos do JavaScript. Arquivos **JSON** são arquivos em que a informação dentro deles está escrita da mesma forma que se define um objeto na linguagem JavaScript.

Como podemos ver no exemplo acima, o arquivo **package.json** armazena as informações do seu aplicativo. Na propriedade **dependencies** estão listados todos os pacotes que você utiliza no seu projeto. Quando você instala um pacote utilizando **npm install** pacote **--save**, a flag **--save** está dizendo para o **npm** que ele, além de instalar o pacote, deve registrar o pacote na propriedade **dependencies** do arquivo **package.json**.

Assim não é necessário que você, quando armazenar seu projeto em um repositório, armazene os pacotes juntos. Quando você executar o comando **npm install**, o **npm** automaticamente irá buscar no arquivo **package.json** quais as dependências do projeto e irá instalar uma a uma nas versões corretas.

---

## EVENTOS - INTRODUÇÃO

O Node.js tem uma estrutura baseada em eventos. Ele possui objetos que são capazes de emitir sinais que disparam ações dentro do código. Chamamos esses sinais emitidos de **eventos** e a ação de emitir um sinal, chamamos de **disparar um evento**.

Os objetos capazes de disparar esses eventos herdam suas propriedades e métodos do construtor **EventEmitter**. Esses objetos também são capazes de "ouvir eventos", isso significa que eles vão ficar no plano de fundo aguardando um evento específico ser disparado. Apenas quando esse evento for disparado esses objetos irão executar alguma ação.

No exemplo a seguir, vamos criar um objeto capaz de emitir e ouvir eventos. O primeiro passo é importar o construtor **EventEmitter** do módulo **events** do Node.js, não sendo necessário instalar nenhum pacote adicional.

Após importar o construtor, vamos criar uma nova instância do **EventEmitter** e associá-la a uma variável.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_ea06db7a.png" widgth = 50>

A função **.on()** é responsável por registrar no objeto os eventos que ele irá ‘escutar’. Ela recebe dois parâmetros:

1. O nome do evento que ele irá esperar ser disparado;

2. Uma função que irá ser executada quando o evento for disparado.

Agora que sabemos registrar eventos no nosso objeto, vamos aprender a disparar esses eventos. A função responsável por disparar eventos é a função **.emit()**. Ela recebe pelo menos um parâmetro, o nome do evento a ser disparado, e após este parâmetro é possível passar todos os argumentos que serão passados para o objeto que está registrado naquele evento.

No exemplo abaixo, nosso objeto **logger** está disparando o evento **"error"** e enviando como parâmetro a string **"error message here"**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_1f93c86e.png" widgth = 50>

Isso faz com que a função associada com o evento **"error"** seja executada, recebendo como parâmetro a string **"error message here"**.

Muitos objetos nativos do Node.js são capazes de emitir e de ouvir eventos, como o objeto da classe **http.Server**.

Para criar um servidor HTTP precisamos importar o módulo **http** e utilizar a função **createServer()**. Esta função retorna uma instância da classe **http.Server**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_df86390f.png" widgth = 50>

De acordo com a <a href="https://nodejs.org/api/http.html#http_class_http_server">documentação oficial</a>, os objetos da classe **http.Server** emitem uma série de eventos. Entre eles, temos o evento ***request***. Ele é emitido todas as vezes que uma requisição HTTP é feita. Vamos registrar ao evento ***request*** uma função para tratar a requisição.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_5742044a.png" widgth = 50>

Por último, vamos associar nossa aplicação com a porta 8080, para que seja possível fazer requisições HTTP para ela. Vamos usar o método **.listen()**, que recebe como parâmetro a porta que queremos associar à nossa aplicação web.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_8a186c9c.png" widgth = 50>

Agora temos uma aplicação web que é capaz de receber requisições HTTP na porta 8080 e que, quando recebe uma requisição, escreve no console qual foi o método HTTP utilizado na requisição e qual foi a URL utilizada.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_dd53bd0d.png" widgth = 50>

---

## STREAMS

Quando estamos lidando com arquivos ou informações grandes sendo enviadas na rede, temos que ser capazes, para garantir eficiência, de enviá-las e acessá-las pedacinho por pedacinho, podendo ainda manipulá-las assim que elas chegam. Não é eficiente esperar que todo o arquivo seja transferido ou que toda a informação seja transferida para então começar a processá-los.

Para mitigar esses casos, o Node.js implementa **streams**. Estes nada mais são que canais por onde a informação pode fluir, não havendo a necessidade de armazenar em memória grande quantidade de informação a ser manipulada.

Existem vários tipos de **streams**, mas vamos adereçar dois tipos principais, as **readable streams** e as **writable streams**, que em outras palavras, são as *streams* de leitura e *streams* de escrita, respectivamente.

**Readable streams** são responsáveis por providenciar uma interface de leitura de dados de alguma fonte, como um arquivo ou a própria rede. O módulo **fs** e o objeto **request** das requisições HTTP são exemplos de objetos que implementam uma interface de **readable streams**.

**Writable streams** são objetos responsáveis por realizar operações de escrita. O módulo **fs** e o objeto **response** das requisições HTTP são exemplos de objetos que implementam uma interface de **writable streams**.

Quando nós recebemos uma requisição, o Node.js abre uma stream de leitura representada pelo objeto **request**, e uma stream de escrita representada pelo objeto **response**, ambos parâmetros da nossa função de callback. Por isso é possível escrever várias vezes no objeto **response**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_bdd8fb9d.png" widgth = 50>

Assim é possível ler os dados de uma requisição observando o evento **readable**. Uma *readable* stream dispara vários eventos <a href="https://nodejs.org/api/stream.html#stream_class_stream_readable">como os descritos na documentação</a>. Vamos nos atentar a dois deles no momento:

- **readable**: emitido quando as informações estão prontas para serem lidas.

- **end**: emitido quando não há mais informação para ser lida.

Podemos preparar nosso código para que, quando o evento **readable** for emitido realizemos a ação de leitura da informação e que quando o evento **end** for emitido, nós finalizemos a requisição.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_6b5930cf.png" widgth = 50>

Todo esse código que escrevemos para ouvir os eventos e ler a informação pedaço a pedaço, pode ser simplificado utilizando o método **.pipe()**. Ele se responsabiliza em lidar com essa parte de eventos, leitura e escrita quando queremos ler de uma **readable stream** e escrever em um **writable stream**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_b28c0028.png" widgth = 50>

Segue exemplo, para copiar o conteúdo de um arquivo para outro arquivo:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_5cde7019.png" widgth = 50>

1. Importe o módulo **fs** do Node.js que possui ferramentas para manipular arquivos.

2. Crie uma stream de leitura com o arquivo que vai ser copiado.

3. Crie uma stream de escrita com o arquivo que vai receber a informação a ser copiada.

4. Utilize o **.pipe()** para passar a informação da *stream* de leitura para a *stream* de escrita.

Podemos fazer o pipe de qualquer *stream* de leitura para uma *stream* de escrita.

No exemplo a seguir, vamos criar um serviço de upload de arquivo simples. Enviaremos o arquivo através de uma requisição HTTP e armazenaremos o arquivo enviado em disco. Para fazer a requisição podemos utilizar ferramentas como <a href="https://www.postman.com/">Postman</a> ou **curl** no terminal (ex: **curl --upload-file exemplo.txt http://localhost:8080**).

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/deb17ea884dde7e93a5dac6c8b110843_html_b28c0028.png" widgth = 50>

No código acima estamos:

1. Importando os módulos **http** e **fs** do Node.js.

2. Criando um servidor HTTP para lidar com as requisições.

3. Registrando uma função ao evento **request** no nosso servidor.

4. Criando uma *stream* de escrita com o nome do arquivo que será o destino das informações transmitidas pela rede.

5. Utilizando **.pipe()** para ler as informações da requisição e escrevê-las no arquivo de destino.

6. Ao fim da transmissão dos dados, finalizando a requisição.

Quando enviamos um arquivo para a nossa aplicação, o Node.js não pára tudo que está fazendo para poder recebê-lo. Por conta da forma como funciona, assincronamente em um modelo não-blocante, nosso servidor é capaz de receber a informação de pedaço em pedaço, sendo que ao mesmo tempo que recebe a informação, ele a escreve em disco, não necessitando carregar tudo em memória para então escrever em disco.

---

## LINKS DE REFERÊNCIA

A seguir indicamos alguns links que podem complementar e enriquecer seu autoestudo.

### MATERIAL OFICIAL SOBRE NODE.JS

<a href="https://nodejs.org/en/">https://nodejs.org/en/</a>

<a href="https://nodejs.org/api/synopsis.html">https://nodejs.org/api/synopsis.html</a>

Blocking and non-blocking: <a href="https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/">https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/</a>

Node.js API: <a href="https://nodejs.org/api/">https://nodejs.org/api/</a>

Modules: <a href="https://nodejs.org/api/modules.html">https://nodejs.org/api/modules.html</a>

HTTP Module: <a href="https://nodejs.org/api/http.html">https://nodejs.org/api/http.html</a>

File System Module: <a href="https://nodejs.org/api/fs.html">https://nodejs.org/api/fs.html</a>

Events: <a href="https://nodejs.org/api/events.html">https://nodejs.org/api/events.html</a>

Streams: <a href="https://nodejs.org/api/stream.html">https://nodejs.org/api/stream.html</a>

### OUTROS RECURSOS

<a href="https://www.w3schools.com/nodejs/">https://www.w3schools.com/nodejs/</a>

<a href="https://en.wikipedia.org/wiki/Node.js">https://en.wikipedia.org/wiki/Node.js</a>

<a href="https://pt.wikipedia.org/wiki/Node.js">https://pt.wikipedia.org/wiki/Node.js</a>

<a href="http://eloquentjavascript.net/20_node.html">http://eloquentjavascript.net/20_node.html</a>

---

# APLICAÇÕES DE RESTFUL

## CRIANDO UMA APLICAÇÃO SIMPLES

Agora que temos uma base sólida de JavaScript e Node.js vamos criar uma API RESTful para uma aplicação simples. O objetivo deste tópico é compreendermos como os conhecimentos adquiridos durantes os estudos podem ser utilizados no contexto de uma aplicação real.

### A APLICAÇÃO

Iremos criar uma aplicação de lista de tarefas e uma API RESTful para que as informações das listas possam ser lidas por outras aplicações, como por exemplo, um aplicativo de celular ou uma aplicação web.

Nossa aplicação vai consistir em **listas** e **tarefas**. Uma lista terá um identificador, um nome e um *array* de tarefas. Uma tarefa consiste em um identificador, uma descrição e um atributo dizendo se a tarefa está feita ou não.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_9c31b0fc.png" widgth = 50>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_b9d17297.png" widgth = 50>

As funcionalidades que iremos implementar em nossa aplicação serão:

- Criar nova lista.

- Renomear lista.

- Apagar lista.

- Listar todas as listas.

- Criar nova tarefa em uma lista.

- Alternar tarefa para completa ou não completa.

- Apagar tarefa em uma lista.

- Listar tarefas de uma lista.

Precisamos definir a forma com que essas funcionalidades serão acessadas em nossa API RESTful. Para isso, para cada uma dessas funcionalidades, vamos associar um método HTTP e uma rota.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_59e20e96.png" widgth = 50>

---

## FUNCIONALIDADE - MÓDULO LISTA

Antes de criarmos nossa API RESTful utilizando Node.js e Express vamos criar a base da nossa aplicação, e as funções, que serão responsáveis por acessar e modificar os dados armazenados. Essas funções vão ficar em um arquivo separado, um módulo, o qual iremos importar na nossa API.

No nosso módulo iremos criar uma classe chamada ListaDAO. DAO é uma sigla para *Data Access Object* (Objeto de Acesso aos Dados). Isso significa que essa classe é a classe responsável por acessar e modificar os dados, esteja onde eles estiverem. Criar uma classe DAO faz com que as responsabilidades fiquem distribuídas, aumentando e deixando o código mais fácil de entender e facilitando modificações e atualizações futuras.

Outra vantagem de se criar uma classe DAO é a possibilidade de realizar alterações na origem da informação sem impactar diretamente o local onde a informação é utilizada. Se você busca seus dados em um arquivo local e quer passar a utilizar um serviço na nuvem, basta alterar a implementação dos métodos na DAO, sem precisar alterar aonde eles são utilizados.

Então, vamos por a mão na massa!

1. Vamos criar uma função construtora chamada ListaDAO.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_c0436b0.png" widgth = 50>

2. Nosso construtor terá uma propriedade chamada **listas**, que possui como valor associado um objeto vazio, onde iremos armazenar todas as listas que forem criadas posteriormente.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_7b85b7cb.png" widgth = 50>

3. Ao fim, vamos exportar uma instância do nosso construtor, para que possamos importar suas funcionalidades em nossa aplicação posteriormente.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_af68a71c.png" widgth = 50>

Com isso a base do nosso módulo está construída. O próximo passo é criar as funcionalidades necessárias para termos uma aplicação de lista de tarefas funcionando. As funcionalidades foram descritas no tópico anterior, **A aplicação**. Primeiramente, vamos definir os métodos necessários e então, implementar cada um deles separadamente.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_375a7981.png" widgth = 50>

Vamos ver a implementação de cada um dos métodos.

As explicações irão estar limitadas aos trechos de código principais de cada método. Nos métodos em que a operação pode vir a falhar retornamos um objeto com duas propriedades, **success** e **message**, indicando se a operação foi concluída com sucesso e a mensagem relacionada ao sucesso da operação.

---

## FUNCIONALIDADES - CRIAR NOVA LISTA

Esse método recebe como parâmetro o **nome** da nova lista a ser criada.

1. Gere um identificador para a nova lista.

2. Crie um objeto **novaLista** com os atributos **id**, **nome** e **tarefas**. O atributo tarefas terá um array vazio associado a ele.

3. Adicione a nova lista na propriedade **listas** do construtor.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_58f39461.png" widgth = 50>

---

## FUNCIONALIDADES - RENOMEAR LISTA

Esse método recebe dois parâmetros: o identificador da lista que deseja renomear e o novo nome da lista.

1. Teste se a lista com o identificador existe entre as listas armazenadas.

2. Troque o valor da propriedade **nome** da lista pelo novo valor.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_8c610a01.png" widgth = 50>

---

## FUNCIONALIDADES - APAGAR LISTA

Esse método recebe como parâmetro o identificador da lista que deseja apagar.

1. Teste se a lista com o identificador existe entre as listas armazenadas.

2. Exclua a lista do nosso objeto listas usando o operador **delete**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_375999ce.png" widgth = 50>

---

## FUNCIONALIDADES - LISTAR TODAS AS LISTAS

Esse método retorna o objeto com as listas armazenadas.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_701efb40.png" widgth = 50>

---

## FUNCIONALIDADES - ADICIONAR NOVA TAREFA EM UMA LISTA

Esse método recebe como parâmetro, a descrição da nova tarefa a ser criada e o identificador da lista onde iremos criar a nova tarefa. O identificador da tarefa é criado com base no número total de tarefas já criadas naquela lista, garantindo que eles sejam sempre únicos no contexto da lista.

1. Crie o identificador da nova tarefa a ser criada com base na quantidade de tarefas que já foram criadas naquela lista.

2. Crie o objeto que irá representar uma tarefa em si.

3. Adicione a nova tarefa no array de tarefas da lista, atualizando o número de tarefas já criadas na lista, somando uma unidade.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_4f7a8fa1.png" widgth = 50>

---

## FUNCIONALIDADES - ATUALIZAR TAREFA EM UMA LISTA

### ALTERAR TAREFA PARA COMPLETA OU NÃO COMPLETA

Esse método recebe como parâmetro o identificador da lista e o identificador da tarefa que queremos alternar o estado. Se a propriedade **completa** da tarefa for **true**, será alterada para **false**, e vice-e-versa.

1. Percorra o *array* de tarefas no objeto lista correspondente ao identificador passado por parâmetro.

2. Quando encontrar uma tarefa com o mesmo identificador passado por parâmetro, o valor da propriedade **completa** da tarefa é alternado para **true** ou **false**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_cb36ffff.png" widgth = 50>

---

## FUNCIONALIDADES - APAGAR TAREFA EM UMA LISTA

Esse método recebe como parâmetro o identificador da lista onde queremos apagar a tarefa e o identificador da tarefa a ser apagada.

1. Percorra o *array* de tarefas no objeto lista correspondente ao identificador passado por parâmetro.

2. Quando encontrar a tarefa correspondente ao identificador passado por parâmetro, a tarefa é removida da lista de tarefas do objeto lista.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_150c9de0.png" widgth = 50>

---

## FUNCIONALIDADES - LISTAR TAREFAS DE UMA LISTA

Esse método retorna o *array* de tarefas da lista que possui o identificador passado por parâmetro.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_2a7cb308.png" widgth = 50>

Com isso, temos todos os métodos do nosso módulo implementados e prontos para serem utilizados

---

## ROTAS - A API RESTFUL

O próximo passo é criar a interface de comunicação com nossa aplicação, a nossa API. Iremos seguir os princípios REST, explorados previamente no material, portanto ela será uma API RESTful. Vamos criar nossa API utilizando Node.js e o módulo Express.

A interface de comunicação que iremos criar, dando acesso às funcionalidades da aplicação, já foram definidas previamente, mas para que não seja necessário voltar ao início deste material, iremos disponibilizar ela novamente.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_59e20e96.png" widgth = 50>

O primeiro passo é criar a estrutura inicial da nossa API web. Para isso vamos:

1. Instalar os módulos express e body-parser na nossa aplicação.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_1bf7262c.png" widgth = 50>

2. Importar os módulos necessários e criar a base da nossa API RESTful.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_4bd55622.png" widgth = 50>

Com a base criada só precisamos definir as rotas da nossa API.

Em cada uma das rotas vamos ter exemplos de requisições, divididos em três partes:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_bf174065.png" widgth = 50>

1. O método HTTP correspondente a requisição.

2. A URL local para realizar a requisição.

3. O corpo da requisição, se necessário.

---

## ROTAS POR FUNCIONALIDADES

### CRIAR NOVA LISTA

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_b1fd41e4.png" widgth = 50>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_98b0b7af.png" widgth = 50>

### RENOMEAR LISTA

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_84bd596f.png" widgth = 50>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_1fc41890.png" widgth = 50>

### APAGAR LISTA

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_b56af451.png" widgth = 50>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_8c0b16fb.png" widgth = 50>

### LISTAR TODAS AS LISTAS

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_3d9e17bd.png" widgth = 50>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_ffc48852.png" widgth = 50>

### CRIAR NOVA TAREFA EM UMA LISTA

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_c1413da5.png" widgth = 50>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_e78f8a70.png" widgth = 50>

### ALTERAR TAREFA PARA COMPLETA OU NÃO COMPLETA

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_2c21f3de.png" widgth = 50>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_982d58e.png" widgth = 50>

### APAGAR TAREFA EM UMA LISTA

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_efa0bf74.png" widgth = 50>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_d7d51e05.png" widgth = 50>

### LISTAR TAREFAS DE UMA LISTA

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_c4d7ed01.png" widgth = 50>

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/7eba6968a5607de693f8f6505dbafda2_html_73c1078e.png" widgth = 50>

---

# EXPRESS

## INSTALANDO O EXPRESS NA SUA APLICAÇÃO

A primeira coisa que precisamos fazer é instalar o **express** em nossa aplicação. Primeiramente, vamos baixar o pacote utilizando o comando **npm**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_5490dc81.png" widgth = 50>

Isso vai fazer com que o pacote **express** seja baixado na pasta **node_modules**, no mesmo diretório do seu aplicativo, e seja registrado como dependência do seu projeto no arquivo **package.json**.

O próximo passo é importar o módulo do *express* na nossa aplicação.

Vamos criar um arquivo chamado **app.js** e nele vamos escrever todo o código da nossa aplicação de exemplo.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_7d8ed1c4.png" widgth = 50>

Agora que temos o módulo disponível, precisamos inicializar nosso aplicativo. Para isso, basta criar uma nova instância do *express*:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_ab1e24a2.png" widgth = 50>

---

## ROTAS

Como nossa aplicação é um aplicativo web, iremos utilizar o protocolo HTTP (*Hypertext Transfer Protocol*) para utilizá-lo. O protocolo HTTP é um protocolo de comunicação que consiste na base para comunicação de dados na web.

Principal conceito do HTTP que iremos utilizar é quanto aos métodos que ele define, principalmente os descritos a seguir:

- GET – Apenas retorna informação, nada mais, nada menos.

- POST – Envia uma nova entidade para o servidor aceitar, como parte do recurso definido na rota.

- PUT – Solicita a criação de um novo recurso. Se ele já existir, apenas o atualiza, se não, o cria.

- DELETE – Solicita a remoção de um determinado recurso.

Como vimos previamente no tópico sobre REST, utilizamos o método HTTP como interface padrão das APIs RESTful. O *express* é ideal para desenvolvermos APIs deste tipo, pois ele já apresenta métodos correspondentes ao método HTTP.

O conceito de roteamento consiste em definirmos rotas na nossa aplicação que, quando acessadas, retornam o que é esperado pela solicitação. Cada rota é uma URI (*Uniform Resource Identifier*), uma *string* no formato **host/resource/etc**, utilizada para identificar um recurso na nossa aplicação.

Vamos criar uma rota que quando acessada, imprime no console um texto qualquer.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_4765495a.png" widgth = 50>

Para definirmos uma rota na nossa aplicação express, temos que definirmos três coisas:

1. *Method* : O método HTTP que irá acessar aquele recurso. No exemplo temos o **app.get.**

2. *Path* : A rota que identifica o recurso. No exemplo temos a rota **"/teste".**

3. *Handler* : A função que irá ser chamada quando aquela rota for acessada.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_5c0e11cc.png" widgth = 50>

A função que é chamada quando a rota for acessada com o método HTTP correspondente recebe dois parâmetros, o ***request*** e o ***response***, que são os mesmos objetos que o Node.js providencia quando fazemos requisições.

Por fim, definimos em que porta nossa aplicação irá ‘escutar’ para que possamos fazer nossas requisições utilizando o método **.listen()**. A porta padrão para requisições HTTP é a porta 8080.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_af6c4801.png" widgth = 50>

Com isso temos nossa aplicação express completa e funcionando! O código completo ficou assim:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_b1cc612d.png" widgth = 50>

Para executarmos nossa aplicação é só executar nosso arquivo de código com o Node.js no terminal.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_6ac94924.png" widgth = 50>

sso fará com que nossa aplicação esteja acessível pelo endereço **localhost:8080/teste** no navegador web de sua escolha.

Agora temos uma aplicação Node.js Express simples e funcionando.

Dando sequência, vamos entrar em detalhes de implementação para que possamos ser capazes de criar APIs RESTful completas.

---

## RESPONSE

O parâmetro ***response*** é um objeto que possui uma série de propriedades e métodos.

Os métodos mais comuns são:

- **.send()**: Envia uma resposta de vários tipos.

- **.sendFile()**: Envia um arquivo como resposta.

- **.json()**: Envia um resposta JSON.

- **.redirect()**: Redireciona uma solicitação.

- **.status()**: Define o status HTTP da resposta.

- **.end()**: Termina o processo de resposta.

Você pode encontrar detalhes sobre as propriedades e métodos do objeto *response* na <a href="http://expressjs.com/pt-br/4x/api.html#res">**documentação oficial**</a>.

Vamos analisar a seguir, alguns exemplos de respostas possíveis para requisições HTTP.

O método **.send()** é capaz de enviar como resposta para a requisição:

- Objetos.

- Strings.

- Arrays.

- Objetos do tipo Buffer.

A documentação do método pode ser acessada por <a href="http://expressjs.com/pt-br/4x/api.html#res.send">esse link</a>.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_cfb26eb7.png" widgth = 50>

Caso você queira retornar um arquivo como resposta da requisição, por exemplo, uma página web, basta utilizar o método **.sendFile()** passando como parâmetro o caminho do arquivo a ser enviado.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_716e72a4.png" widgth = 50>

O método em si recebe até três parâmetros, sendo eles:

- O nome do arquivo a ser enviado.

- Um objeto com propriedades a respeito do envio do arquivo. As propriedades utilizadas podem ser vistas na <a href="http://expressjs.com/pt-br/4x/api.html#res.sendFile">documentação do método</a>.

- *Callback* chamada ao fim do envio. Caso tenha algum erro no envio, ela recebe um parâmetro com a mensagem de erro, se der tudo certo o parâmetro é nulo.

Por último, temos um exemplo do método **.json()**. Ele recebe um valor e o envia como JSON válido. A documentação do método pode ser encontrada <a href="http://expressjs.com/pt-br/4x/api.html#res.json">aqui</a>.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_4b83f319.png" widgth = 50>

---

## REQUEST

O parâmetro ***request*** é um objeto que possui uma série de informações a respeito da requisição HTTP em si. Entre as várias propriedades da requisição, as que mais iremos utilizar são:

- **.body**: O corpo da requisição. Por exemplo, quando usamos POST.

- **.params**: Parâmetros da requisição no formato **/rota/:parametro**.

- **.query**: Um objeto que contém uma propriedade para cada *query* na rota.

- **.method**: O método HTTP da requisição, como GET, POST, DELETE, etc.

Você pode encontrar detalhes sobre as propriedades e métodos do objeto *request* na <a href="http://expressjs.com/pt-br/4x/api.html#req">documentação oficial</a>.

Agora, vamos ver exemplos de como usar os atributos **.body**, **.params** e **.query**.

O atributo **.params** armazena as propriedades nomeadas na rota precedidas por **:** (dois pontos).

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_edc9e987.png" widgth = 50>

O atributo **.query** tem como propriedade todas as informações que vem após o caractere **?** na rota. Para saber as regras de formatação de uma query visite o <a href="https://en.wikipedia.org/wiki/Query_string">artigo da Wikipédia</a>, ele é bem atualizado e confiável. A função de uma query é definir parâmetros de busca.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_a4a69ab8.png" widgth = 50>

Por último temos a propriedade **.body**. Ela armazena a informação enviada no corpo da requisição. É muito utilizada para requisições HTTP com o método POST, pois envia as informações do novo objeto a ser criado na base de dados.

Porém, para que sua aplicação seja capaz de entender o conteúdo da propriedade **.body** da sua requisição é necessário providenciar uma ferramenta de parse do conteúdo. Ela será a responsável por interpretar a informação e disponibilizá-la no formato adequado. Se não providenciarmos uma ferramenta de parse, o valor associado a essa propriedade será sempre **undefined**.

Neste exemplo, vamos utilizar a biblioteca **body-parser**, que é a biblioteca utilizada como exemplo na <a href="http://expressjs.com/pt-br/4x/api.html#req.body">documentação do método</a>. Para instalar a biblioteca use **npm install --save body-parser**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/d642a9021e8122b048ae3876253ab888_html_2b62ad66.png" widgth = 50>

É possível fazer muito mais com o *express*. Ele é um framework poderoso que agrega várias funcionalidades essenciais para a criação de serviços e aplicações web. O conteúdo que vimos neste tópico aborda apenas o básico necessário para começar a se aventurar.

Para aprofundar o seu conhecimento você pode ler a documentação e os guias no site oficial, <a href="http://expressjs.com">**http://expressjs.com**</a>, além de consultar diversos tutoriais na internet, tanto em vídeo como em texto.

---

## LINKS DE REFERÊNCIA

A seguir indicamos alguns links que podem complementar e enriquecer seu autoestudo.

Roteamento: <a href="http://expressjs.com/pt-br/guide/routing.html">http://expressjs.com/pt-br/guide/routing.html</a>

Request: <a href="http://expressjs.com/pt-br/4x/api.html#req">http://expressjs.com/pt-br/4x/api.html#req</a>

Response: <a href="http://expressjs.com/pt-br/4x/api.html#res">http://expressjs.com/pt-br/4x/api.html#res</a>

Wikipédia: <a href="https://en.wikipedia.org/wiki/Express.js">https://en.wikipedia.org/wiki/Express.js</a>

GitHub Repo: <a href="https://github.com/expressjs/express">https://github.com/expressjs/express</a>

Express - tutorial simples: <a href="http://nodebr.com/primeiros-passos-com-express-em-node-js/">http://nodebr.com/primeiros-passos-com-express-em-node-js/</a>

Query: <a href="https://en.wikipedia.org/wiki/Query_string">https://en.wikipedia.org/wiki/Query_string</a>

---

# CONSUMINDO APIS

## INTRODUÇÃO

### VAMOS APRENDER NESSE TÓPICO

Temos em mãos o conhecimento necessário para criar APIs RESTful utilizando Node.js e Express. Com isso somos capazes de criar aplicações móveis e aplicações web que consomem dessas APIs através de requisições HTTP.

Porém, as vezes é necessário que nossas APIs consumam de outras APIs. Para isso precisamos saber como realizar requisições HTTP utilizando Node.js.

Neste tópico, iremos aprender a consumir APIs RESTful utilizando Node.js e Express.

---

## REQUISIÇÕES HTTP COM NODE.JS

Para consumirmos APIs RESTful é necessário que sejamos capazes de realizar requisições HTTP utilizando os métodos definidos no protocolo HTTP. Existem diversas bibliotecas que implementam funcionalidades específicas para realizar requisições HTTP, como as bibliotecas **request** e **request-promise**.

Veremos aqui, como trabalhar com um módulo nativo do Node.js, o módulo **http**.

O módulo **http** do Node.js possui uma série de métodos e construtores. Entre eles estão métodos que podemos utilizar para realizar requisições HTTP. O método que vamos aprender a utilizar se chama **http.request(options, callback)**.

---

## HTTP.REQUEST

O método **http.request** retorna um objeto **http.ClientRequest**. Esse objeto é uma <a href="https://nodejs.org/api/stream.html#stream_writable_streams">Writable Stream</a>, portanto podemos escrever informação no objeto utilizando o método **write**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/24a7b22dab654957d170dd3f9e3deabe_html_bc91ed63.png" widgth = 50>

Lembrando que temos sempre que chamar o método **end** para simbolizar o fim de uma requisição.

O método **http.request** recebe dois parâmetros.

O primeiro parâmetro que precisamos passar para o método é um objeto com as configurações relativas a requisição que queremos realizar, como a url da requisição e o método HTTP que queremos utilizar. A seguir, temos um exemplo de objeto com as opções esperadas pelo método. Para mais informações a respeito das opções esperadas no objeto consulte a <a href="https://nodejs.org/api/http.html#http_http_get_options_callback">documentação do método</a>.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/24a7b22dab654957d170dd3f9e3deabe_html_c4dd95cd.png" widgth = 50>

O segundo parâmetro é a função de *callback* que será chamada ao fim da requisição.

Está função irá receber um parâmetro, o objeto de resposta da requisição, para que você possa receber o resultado da requisição realizada. Por padrão, ele ‘ouve’ o evento **response**, emitido quando a requisição HTTP recebe sua resposta.

Podemos utilizar este objeto para ‘ouvir’ os eventos emitidos pela requisição, pois a resposta da requisição implementa a interface <a href="https://nodejs.org/api/stream.html#stream_class_stream_readable">Readable Stream</a>. A partir destes eventos, somos capazes de determinar quando a requisição nos traz a informação que precisamos (evento **data**) e quando a requisição termina (evento **end**).

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/24a7b22dab654957d170dd3f9e3deabe_html_8e933f39.png" widgth = 50>

---

## FAZENDO UMA REQUISIÇÃO EM UMA APLICAÇÃO NODE.JS + EXPRESS

Agora que já sabemos como o método **http.request** funciona, vamos ver um exemplo de utilização em uma aplicação Node.js utilizando Express.

O primeiro passo é construirmos a base da nossa aplicação web.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/24a7b22dab654957d170dd3f9e3deabe_html_6bb12853.png" widgth = 50>

Vamos adicionar uma interface para buscar os usuários cadastrados.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/24a7b22dab654957d170dd3f9e3deabe_html_1cd4d76f.png" widgth = 50>

Porém, as informações dos usuários não estão armazenadas localmente. Hospedamos o JSON com as informações do usuário no site <a href="myjson.com">My JSON</a> para simular nosso banco de dados. Ele provê para nós uma API de acesso as informações armazenadas. Os dados que iremos buscar neste exemplo estão disponíveis em <a href="myjson.com/1ez5xx">myjson.com/1ez5xx</a>.

O próximo passo é criar a requisição para o endereço **api.myjson.com/bins/1ez5xx**. Nas nossas opções, vamos definir as propriedades **method**, **hostname** e **path**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/24a7b22dab654957d170dd3f9e3deabe_html_31def0a.png" widgth = 50>

Agora vamos criar nossa requisição **getUser**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/24a7b22dab654957d170dd3f9e3deabe_html_dd28ec9a.png" widgth = 50>

Como temos a requisição pronta, temos que tratar a resposta, armazenar ou repassar os dados resultantes. Primeiramente, vamos pegar os dados da resposta ouvindo o evento **data**.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/24a7b22dab654957d170dd3f9e3deabe_html_65294f38.png" widgth = 50>

Precisamos ouvir o evento **end**, para podermos saber quando a informação terminou de ser transferida. Assim, podemos pegar a informação e enviar como resposta a requisição original feita na nossa aplicação Express.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/24a7b22dab654957d170dd3f9e3deabe_html_61c88b3.png" widgth = 50>

Por fim, devemos estar atentos aos erros que podem acontecer. Em uma requisição HTTP existem diversos tipos de problemas que podem ocorrer, como o endereço ao qual você está tentando acessar não existir mais ou você não ter acesso a ele. Quando algum erro acontece, o evento **error** e emitido pela requisição.

Antes de finalizar a requisição, vamos ouvir o evento **error** em nossa requisição, para podermos tratar o erro caso ele venha a ocorrer.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/24a7b22dab654957d170dd3f9e3deabe_html_d1c8a152.png" widgth = 50>

Com isso temos tudo que precisamos para fazer uma requisição utilizando Node.js.

---

## LINKS DE REFERÊNCIA

A seguir indicamos alguns links que podem complementar e enriquecer seu autoestudo.

Módulo **http**: <a href="https://nodejs.org/api/http.html">https://nodejs.org/api/http.html</a>

Método **http.request**: <a href="https://nodejs.org/api/http.html#http_http_get_options_callback">https://nodejs.org/api/http.html#http_http_get_options_callback</a>

Método **setEnconding**: <a href="https://nodejs.org/api/stream.html#stream_readable_setencoding_encoding">https://nodejs.org/api/stream.html#stream_readable_setencoding_encoding</a>

Outra forma de fazer requisições com Node.js: <a href="https://davidwalsh.name/nodejs-http-request">https://davidwalsh.name/nodejs-http-request</a>

HTTP Status Code Definitions: <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html">https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html</a>

---

# NODE-RED - EXTRA

## INTRODUÇÃO

Node-RED é uma ferramenta de programação para conectar dispositivos de hardware, APIs e serviços online de maneiras novas e interessantes.Ele fornece um editor baseado em navegador que torna mais fácil conectar fluxos usando a ampla gama de nós na paleta que podem ser implementados em seu tempo de execução com um único clique.

O Node-RED fornece um editor de fluxo baseado em navegador que facilita a conexão de fluxos usando a ampla gama de nós na paleta. Os fluxos podem ser implantados no tempo de execução com um único clique. As funções JavaScript podem ser criadas dentro do editor usando um editor de rich text. Uma biblioteca integrada permite que você salve funções úteis, modelos ou fluxos para reutilização.

Leve, ​​construído em Node.js e orientado por eventos. Isso o torna ideal para ser executado na extremidade da rede em hardware de baixo custo, como o Raspberry Pi, bem como na nuvem. Com mais de 225.000 módulos no repositório de pacotes do Node, é fácil estender a gama de nós da paleta para adicionar novos recursos.

Retirado e traduzido de: <a href="https://nodered.org/">Node-RED</a>.

---

## INSTALANDO E UTILIZANDO O NODE-RED

Não vamos entrar em detalhes sobre o processo de instalação do Node-RED. O passo a passo está detalhado no <a href="https://nodered.org/docs/getting-started/local">site oficial</a>. O comando para instalar a aplicação é:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_cc1ca1eb.png" widgth = 50>

Para executar o Node-RED abra um terminal e digite o comando:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_138343e3.png" widgth = 50>

Isso irá executar a ferramenta, que poderá ser acessada diretamente pelo seu navegador web no endereço:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_b57825f0.png" widgth = 50>

Ao acessarmos a ferramenta iremos ter acesso a interface principal do Node-RED:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_1c5bf7eb.png" widgth = 50>

Nela nós seremos capazes de criar fluxos utilizando e configurando ‘nós’. Mas antes de iniciarmos a criação destes fluxos, vamos entender os conceitos básicos por trás do Node-RED.

---

## NÓS E FLUXOS

O primeiro conceito que precisamos conhecer é o conceito de nós. Um nó é uma unidade básica de funcionalidade. Eles podem ser de vários tipos diferentes e cada um tem uma funcionalidade e um conjunto de configurações específicas.

Os tipos básicos de nós são:

- Nós de entrada (input);

- Nós de saída (output);

- Nós de função (function).

Eles ficam localizados na barra na lateral esquerda da interface e para adicioná-los no seu fluxo, basta clicar em um nó e arrastá-lo para tela principal.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_b1476676.png" widgth = 50>

É possível criar conexões entre nós e são essas conexões que dão funcionalidade ao nosso fluxo. Um fluxo é um conjunto de nós conectados, com início (input) e fim (output). Cada nó possui saídas e/ou entradas, as quais são utilizadas para conectá-los. Uma conexão entre nós faz com que as informações processadas no primeiro nó sejam passadas para o nó seguinte, de forma a utilizar para executar suas próprias funcionalidades.

Os nós de entrada (input) representam formas de iniciar um fluxo com algum tipo de informação. Podemos configurar um botão para iniciarmos manualmente, definir em uma requisição HTTP como ponto de entrada e até um timer, para que o fluxo seja iniciado em um intervalo de tempo predeterminado. Estes nós apresentam apenas saídas de informação, pois estarão sempre posicionados no início do fluxo.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_a9663ef4.png" widgth = 50>

Os nós de saída (output) definem o fim de um fluxo. Podemos definir o fim do fluxo de diversas formas, com uma mensagem no console, um envio de um e-mail, com uma resposta HTTP ou armazenando a informação em um banco de dados ou arquivo. Estes nós apresentam apenas entradas de informação, pois estarão sempre posicionados ao fim de um fluxo.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_cd96b9ec.png" widgth = 50>

Os nós de função (function) são nós intermediários. Eles não ficam nem no início nem no fim de um fluxo. Eles possuem entradas e saídas, pois esses nós são responsáveis por receber informação, processá-la de alguma forma e passar o resultado desse processamento para o próximo nó. Com nós de função podemos escrever código JavaScript, podemos definir tempos de espera, criar requisições HTTP intermediárias, converter formatos de informação, entre outras opções.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_46723f60.png" widgth = 50>

Com esses três tipos básicos de nós somo capazes de criar nossos próprios fluxos. Um fluxo é um conjunto de nós conectados com início e fim. No Node-RED podemos ter vários fluxos diferentes. Clicando no botão com o símbolo +, no canto superior direito do editor, criamos um novo fluxo.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_2cb1fdd6.png" widgth = 50>

Podemos ver quais os fluxos foram criados nas abas posicionadas na parte superior do editor.

Porém, quando criamos um novo fluxo ou editamos um fluxo existente essas novas modificações não serão acessíveis imediatamente. Para que as modificações sejam aplicadas ao funcionamento do fluxo é necessário fazer o deploy dessas modificações clicando no botão deploy.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_ee3c2bae.png" widgth = 50>

Dessa forma, as modificações que você tiver implementado nos fluxos já existentes e os novos fluxos que você tiver criado irão estar online.

---

## COMO ACESSAR SUA API CRIADA NO NODE-RED

Considere que criamos a seguinte API RESTful utilizando o Node-RED:

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_149e0100.png" widgth = 50>

Como fazemos para acessar as rotas definidas no nosso fluxo?

Cada rota definida nos nós de HTTP Request do nosso fluxo é acessível utilizando o endereço onde o Node-RED está hospedado. Para simplificar, vamos utilizar o endereço local, http://localhost:1880/. Podemos acessar suas rotas fazendo as requisições diretamente no endereço da ferramenta, somada a rota que desejamos acessar.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_dfb8ddeb.png" widgth = 50>

### INSTALANDO NOVOS NÓS

O poder do Node-RED consiste no que os nós que temos disponíveis podem oferecer em termos de funcionalidade. Podemos estender as funcionalidades do Node-RED instalando novos nós na ferramenta.

Existe uma grande gama de nós disponíveis na <a href="https://nodered.org/">Node-RED Library</a>, em pacotes de nós criados e disponibilizados pela comunidade. A forma mais simples de adicionar novos nós na sua biblioteca de nós do Node-RED é utilizando a funcionalidade Manage palette. Clique no botão de menu no canto superior esquerdo da ferramenta. Entre as opções, clique em Manage palette.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_db25e3d9.png" widgth = 50>

Com isso uma nova janela irá aparecer em frente ao seu editor de fluxos. Essa nova janela possui duas abas, Nodes e Install.

Na primeira aba, Nodes, estão listado todos os pacotes de nós já instalados no seu Node-RED. Ele já possui alguns pacotes instalados por padrão como o pacote Node-RED. Aqui você pode desabilitar e habilitar esses pacotes já instalados.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_229eed01.png" widgth = 50>

Na segunda aba, Install, estão listados os pacotes disponíveis para serem instalados. Como são muitos, inicialmente a lista está vazia e irá ser carregada assim que você entrar com algum termo de busca na barra de busca.

Após realizar uma busca, basta encontrar o pacote que gostaria de instalar e clicar em Install, do lado direito do nome do pacote.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_d3ac3f9b.png" widgth = 50>

Assim que a instalação for concluída os nós do pacote instalado estarão presentes entre as opções de nós, na barra da lateral esquerda do editor.

<img src="https://lms.hackatruck.com.br/courses/EADALGOOSWJS/document/imagens/js/2ee868dd8aa8260f8525eb7c70942528_html_9b6364c2.png" widgth = 50>

Para mais informações sobre importação e instalação de nós no Node-RED podem ser encontradas no <a href="https://nodered.org/docs/user-guide/runtime/adding-nodes">site oficial</a>. E para um resumo geral sobre a utilização da ferramenta, temos um excelente vídeo no YouTube chamado <a href="https://www.youtube.com/watch?v=f5o4tIz2Zzc">Node Red em 5 minutos</a> (em inglês), onde somos apresentados rapidamente a utilização básica do Node-RED.

---

## LINKS DE REFERÊNCIA

A seguir indicamos alguns links que podem complementar e enriquecer seu autoestudo.

Site oficial: <a href="nodered.org">nodered.org</a>

Instalação: <a href="https://nodered.org/docs/getting-started/installation">https://nodered.org/docs/getting-started/installation</a>

Node-RED Library: <a href="https://flows.nodered.org/">https://flows.nodered.org/</a>

Adicionando novos nós: <a href="https://nodered.org/docs/getting-started/adding-nodes">https://nodered.org/docs/getting-started/adding-nodes</a>

Criando um flow: <a href="https://nodered.org/docs/getting-started/first-flow">https://nodered.org/docs/getting-started/first-flow</a>

Sobre o Node-RED <a href="https://developer.ibm.com/code/open/node-red/">https://developer.ibm.com/code/open/node-red/</a>

Node-RED em 5 minutos: <a href="https://www.youtube.com/watch?v=f5o4tIz2Zzc">https://www.youtube.com/watch?v=f5o4tIz2Zzc</a>