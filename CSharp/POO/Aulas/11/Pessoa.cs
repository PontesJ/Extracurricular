using System;

namespace _11
{
    class Pessoa
    {
        private string nome = "Tatiana";
        public Pessoa(string nome)
        {
            Console.WriteLine(nome);
            Console.WriteLine(this.nome);
        }
    }
}
