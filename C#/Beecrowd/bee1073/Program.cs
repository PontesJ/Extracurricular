using System;

namespace bee1073
{
    class Program
    {
        static void Main(string[] args)
        {
            int N;
            double i, cont;
            N = int.Parse(Console.ReadLine());
            if (N > 5 && N < 2000) {
                for (i = 2; i <= N; i += 2) {
                    cont = Math.Pow(i, 2.0);
                    Console.WriteLine("{0}^2 = {1}", i, cont);
                }
            }
        }
    }
}
