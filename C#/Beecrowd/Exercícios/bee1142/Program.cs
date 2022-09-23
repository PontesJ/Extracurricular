using System;

namespace bee1142
{
    class Program
    {
        static void Main(string[] args)
        {
            int N, i, n1 = 1, n2 = 2, n3 = 3;
            N = int.Parse(Console.ReadLine());
            for (i = 1; i <= N; i++) {
                Console.WriteLine("{0} {1} {2} PUM", n1, n2, n3);
                n1 += 4; n2 += 4; n3 += 4;
            }
        }
    }
}
