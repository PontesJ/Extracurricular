using System;

namespace _08
{
    class Aluno
    {
        private double nota1, nota2;
        private double media()
        {
            return (nota1 + nota2) / 2;
        }
        public void mensagem()
        {
            Console.Write("Digite a primeira nota: ");
            nota1 = int.Parse(Console.ReadLine());
            Console.Write("Digite a segunda nota: ");
            nota2 = int.Parse(Console.ReadLine());
            Console.WriteLine("A média é {0:0.00}", media());
        }
    }
}
