class FormaGeometrica {
    func descricao() {
        print("Decrição de uma forma geométrica")
    }
}

class Retangulo: FormaGeometrica
{
    private var largura:Int
    private var comprimento: Int
    
    init (largura: Int, comprimento: Int)
    {
        self.largura = largura
        self.comprimento = comprimento
    }
    
    public func setLargura(largura: Int)
    {
        self.largura = largura
    }
    
    public func getLargura() -> Int
    {
        return largura
    }
    
    public func setComprimento(comprimento: Int)
    {
        self.comprimento = comprimento
    }
    
    public func getComprimento() -> Int
    {
        return comprimento
    }
    
    public func area() -> Int
    {
        return (comprimento * largura)
    }
}

class Circulo: FormaGeometrica
{
    private var raio:Int
    
    init (raio: Int)
    {
        self.raio = raio
    }
    
    public func setRaio(raio: Int)
    {
        self.raio = raio
    }
    
    public func getRaio() -> Int
    {
        return raio
    }
    
    public func area() -> Double
    {
        return (3.14 * (Double(raio) * Double(raio)))
    }
}

var ret1 = Retangulo(largura: 15, comprimento: 5)
print(ret1.area())

var cir1 = Circulo(raio: 5)
print(cir1.area())