class Animal
{
    var nome: String?
    var raca: String?
    
    func emitirSom(){}
    func comer(comida: String){}
    func escalar(){}
    func babar(){}
}

class Cao : Animal
{
    override func emitirSom()
    {
        print("Au au")
    }
    override func comer(comida: String)
    {
        print("Comendo \(comida)")
    }
    override func babar()
    {
        print("Babando")
    }

    init(nome: String, raca: String)
    {
        super.init()
        self.nome = nome
        self.raca = raca
    }
}

class Gato : Animal
{
    override func emitirSom()
    {
        print("Miau")
    }
    override func comer(comida: String)
    {
        print("Comendo \(comida)")
    }
    override func escalar()
    {
        print("Escalando")
    }

    init(nome: String, raca: String)
    {
        super.init()
        self.nome = nome
        self.raca = raca
    }
}

var cao1 = Cao(nome: "Tob", raca: "Pastor")
var gato1 = Gato(nome: "Felix", raca: "Frajola")

cao1.emitirSom()
cao1.comer(comida: "carne")
cao1.babar()

gato1.emitirSom()
gato1.comer(comida: "peixe")
gato1.escalar()