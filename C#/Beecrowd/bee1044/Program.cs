using System;

namespace bee1044
{
    class Program
    {
        static void Main(string[] args)
        {
            int a, b; 
            string[] linha = Console.ReadLine().Split(' '); 
            a = int.Parse(linha[0]); 
            b = int.Parse(linha[1]);
            if (a % b == 0 || b % a == 0) Console.WriteLine("Sao Multiplos");
            else Console.WriteLine("Nao sao Multiplos");
        }
    }
}
