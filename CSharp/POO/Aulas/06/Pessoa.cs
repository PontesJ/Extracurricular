using System;

namespace _06
{
    class Pessoa
    {
        public double peso, altura;
        public double imc()
        {
            return peso/(altura * altura);
        }
        public string indice()
        {
            double imc1 = imc();
            if (imc1 < 18.5) return "Abaixo do peso";
            else if (imc1 < 25) return "Peso normal";
            else if (imc1 < 30) return "Acima do peso";
            else if (imc1 < 35) return "Obesidade I";
            else if (imc1 < 40) return "Obesidade II";
            else return "Obesidade III";
        }
    }
}
