using System;

namespace _03
{
    class Pessoa
    {
        public string nome;
        public int idade;
        public void mensagem()
        {
            Console.WriteLine("Olá {0}, você tem {1} anos", nome, idade);
        }
    }
}