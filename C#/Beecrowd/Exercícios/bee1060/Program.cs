using System;

namespace bee1060
{
    class Program
    {
        static void Main(string[] args)
        {
            int i, pos = 0;
            double num;
            for (i = 1; i <= 6; i++) {
                num = double.Parse(Console.ReadLine());
                if (num > 0) {
                    pos++;
                }
            }
            Console.WriteLine("{0} valores positivos", pos);
        }
    }
}
