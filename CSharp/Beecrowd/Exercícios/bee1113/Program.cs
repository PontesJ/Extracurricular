using System;

namespace bee1113
{
    class Program
    {
        static void Main(string[] args)
        {
            int X = 1, Y = 2;
            while (X != Y) {
                string[] linha = Console.ReadLine().Split(' '); 
                X = int.Parse(linha[0]);
                Y = int.Parse(linha[1]);
                if (X > Y) Console.WriteLine("Decrescente");
                if (Y > X) Console.WriteLine("Crescente");
            }
        }
    }
}
