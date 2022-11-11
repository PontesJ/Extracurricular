using System;

namespace _12
{
    class Pessoa
    {
        protected string nome;
        protected int idade;
        protected void mensagemPessoa()
        {
            Console.WriteLine("Nome: {0}\nIdade: {1}", nome, idade);
        }
    }
}
