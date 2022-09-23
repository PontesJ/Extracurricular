using System;

namespace bee1014
{
    class Program
    {
        static void Main(string[] args)
        {
            int distancia;
            double litros, consumo;
            distancia = int.Parse(Console.ReadLine());
            litros = double.Parse(Console.ReadLine());
            consumo = distancia/litros;
            Console.WriteLine("{0:0.000} km/l", consumo);
        }
    }
}
