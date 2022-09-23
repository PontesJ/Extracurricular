using System;

namespace bee1065
{
    class Program
    {
        static void Main(string[] args)
        {
            int i, par = 0;
            double num;
            for (i = 1; i <= 5; i++) {
                num = double.Parse(Console.ReadLine());
                if (num % 2 == 0) {
                    par++;
                }
            }
            Console.WriteLine("{0} valores pares", par);
        }
    }
}
