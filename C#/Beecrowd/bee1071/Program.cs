using System;

namespace bee1071
{
    class Program
    {
        static void Main(string[] args)
        {
            int x, y, maior = 0, menor = 0, soma = 0;
            x = int.Parse(Console.ReadLine());
            y = int.Parse(Console.ReadLine());
            if (x > y) {
                maior = x;
                menor = y;
            } else if (y > x) {
                maior = y;
                menor = x;
            }
            if (x != y) {
                for (menor += 1 ; maior > menor; menor++) {
                    if (menor % 2 == 1 || menor % 2 == -1) {
                        soma += menor;
                    }
                }
                Console.WriteLine("{0}", soma);
            } else Console.WriteLine("0");
        }
    }
}
