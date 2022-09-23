using System;

namespace bee1132
{
    class Program
    {
        static void Main(string[] args)
        {
            int n1, n2, maior = 0, menor = 0, soma = 0;
            n1 = int.Parse(Console.ReadLine());
            n2 = int.Parse(Console.ReadLine());
            if (n1 > n2) {
                maior = n1;
                menor = n2;
            } else if (n2 > n1) {
                maior = n2;
                menor = n1;
            }
            while (maior >= menor) {
                if (menor % 13 != 0) {
                    soma += menor;
                }
                menor ++;
            }
            Console.WriteLine("{0}", soma);
        }
    }
}
