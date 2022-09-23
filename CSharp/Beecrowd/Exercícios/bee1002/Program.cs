using System;

namespace bee1002
{
    class Program
    {
        static void Main(string[] args)
        {
            double raio, area;
            raio = double.Parse(Console.ReadLine());
            area = 3.14159 * (Math.Pow(raio, 2));
            Console.WriteLine("A={0:0.0000}", area);
        }
    }
}
