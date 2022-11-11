using System;

namespace _06
{
    class Program
    {
        static void Main(string[] args)
        {
            Pessoa p1 = new Pessoa();
            p1.peso = 46.6;
            p1.altura = 1.77;
            Console.WriteLine("Seu IMC é de {0:0.00}", p1.imc());
            Console.WriteLine(p1.indice());
        }
    }
}
