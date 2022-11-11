using System;

namespace _04
{
    class Pessoa
    {
        public void apresentar()
        {
            Console.WriteLine("Olá!");
        }
        public void apresentar(string nome)
        {
            Console.WriteLine("Olá {0}", nome);
        }
        public void apresentar(string nome, int idade)
        {
            Console.WriteLine("Olá {0}, sua idade é {1}", nome, idade);
        }
    }
}
