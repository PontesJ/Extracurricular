using System;

namespace _09
{
    class Pessoa
    {
        public Pessoa()
        {
            Console.WriteLine("Construtor inicializado");
        }
        public Pessoa(string nome)
        {
            Console.WriteLine("Olá {0}", nome);
        }
    }
}
