using System;

namespace _03
{
    class Program
    {
        static void Main(string[] args)
        {
            Pessoa obj = new Pessoa();
            obj.nome = "Ralf";
            obj.idade = 30;
            obj.mensagem();
        }
    }
}
