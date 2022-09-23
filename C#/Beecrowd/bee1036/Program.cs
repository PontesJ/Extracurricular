using System;

namespace bee1036
{
    class Program
    {
        static void Main(string[] args)
        {
            double A, B, C, raiz, bhaskara1, bhaskara2;
            string[] linha = Console.ReadLine().Split(' '); 
            A = double.Parse(linha[0]);
            B = double.Parse(linha[1]);
            C = double.Parse(linha[2]);
            raiz = Math.Pow(B, 2) - 4 * A * C;
            if (raiz < 0 || A == 0) {
                Console.WriteLine("Impossivel calcular");
            } else {
                bhaskara1 = (-B + Math.Sqrt(raiz)) / (2 * A);
                bhaskara2 = (-B - Math.Sqrt(raiz)) / (2 * A);
                Console.WriteLine("R1 = {0:0.00000}", bhaskara1);
                Console.WriteLine("R2 = {0:0.00000}", bhaskara2);
            }
        }
    }
}
