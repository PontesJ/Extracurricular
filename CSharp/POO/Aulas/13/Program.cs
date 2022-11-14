using System;

namespace _13
{
    class Program
    {
        static void Main(string[] args)
        {
            Imposto objE = new Estagiario();
            objE.valeAlimentacao(1000);
            objE.valeTransporte(1000);
            Console.WriteLine("==================");
            Imposto objA = new Atendente();
            objA.valeAlimentacao(2000);
            objA.valeTransporte(2000);
            Console.WriteLine("==================");
            Imposto objG = new Gerente();
            objG.valeAlimentacao(5000);
            objG.valeTransporte(5000);
        }
    }
}
