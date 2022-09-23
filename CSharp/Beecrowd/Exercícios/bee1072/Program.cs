using System;

namespace bee1072
{
    class Program
    {
        static void Main(string[] args)
        {
            int N, X, dentro = 0, fora = 0;
            N = int.Parse(Console.ReadLine());
            if (N < 10000) {
                for (int i = 0 ; i < N; i++) {
                    X = int.Parse(Console.ReadLine());
                    if (X > Math.Pow(-10, 7) && X < Math.Pow(10, 7)) {
                        if (X >= 10 && X <= 20) {
                            dentro++;
                        } else {
                            fora++;
                        }
                    }
                }
            }
            Console.WriteLine("{0} in", dentro);
            Console.WriteLine("{0} out", fora);
        }
    }
}
