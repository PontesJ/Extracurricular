using System;

namespace bee1038
{
    class Program
    {
        static void Main(string[] args)
        {
            int lanche, quantidade;
            double valor = 0; 
            string[] linha = Console.ReadLine().Split(' '); 
            lanche = int.Parse(linha[0]); 
            quantidade = int.Parse(linha[1]);
            if (lanche == 1) valor = 4 * quantidade;
            if (lanche == 2) valor = 4.5 * quantidade;
            if (lanche == 3) valor = 5 * quantidade;
            if (lanche == 4) valor = 2 * quantidade;
            if (lanche == 5) valor = 1.5 * quantidade;
            Console.WriteLine("Total: R$ {0:0.00}", valor);
        }
    }
}
