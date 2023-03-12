class Veiculo{
    var pneus: String?
    var assentos: String?
    var motor: String?
    
    func desc() {
        print("Número de rodas \(self.pneus ?? " "), Número de Assentos \(self.assentos ?? " "), Potencia Motor \(self.motor ?? " ")") 
    }
}

class Motocicleta : Veiculo {
    var cilindradas: Int?
    func cilin()
    {
        print("Essa moto tem \(cilindradas!) cilindradas")
    }
}

class Aviao : Veiculo {
    var numMotores: Int?
}

var moto1 = Motocicleta()
moto1.cilindradas = 200
moto1.cilin()