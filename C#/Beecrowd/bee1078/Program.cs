using System;

namespace Tabuada
{
    class Program
    {
        static void Main(string[] args)
        {
            int N, i, cont;
            N = int.Parse(Console.ReadLine());
            if (N > 2 && N < 1000) {
                for (i = 1; i <= 10; i++){
                    cont = N * i;
                    Console.WriteLine("{0} x {1} = {2}", i, N, cont);
                }
            }
        }
    }
}
