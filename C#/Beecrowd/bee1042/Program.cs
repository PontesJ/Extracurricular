using System;

namespace bee1042
{
    class Program
    {
        static void Main(string[] args)
        {
            int n1, n2, n3; 
            string[] linha = Console.ReadLine().Split(' '); 
            n1 = int.Parse(linha[0]); 
            n2 = int.Parse(linha[1]);
            n3 = int.Parse(linha[2]);
            if (n1 > n2 && n1 > n3) {
                if (n2 > n3) Console.WriteLine("{0}\n{1}\n{2}\n\n{3}\n{4}\n{5}", n3, n2, n1, n1, n2, n3);
                else Console.WriteLine("{0}\n{1}\n{2}\n\n{3}\n{4}\n{5}", n2, n3, n1, n1, n2, n3);
            }
            if (n2 > n1 && n2 > n3) {
                if (n1 > n3) Console.WriteLine("{0}\n{1}\n{2}\n\n{3}\n{4}\n{5}", n3, n1, n2, n1, n2, n3);
                else Console.WriteLine("{0}\n{1}\n{2}\n\n{3}\n{4}\n{5}", n1, n3, n2, n1, n2, n3);
            }
            if (n3 > n1 && n3 > n2){
                if (n1 > n2) Console.WriteLine("{0}\n{1}\n{2}\n\n{3}\n{4}\n{5}", n2, n1, n3, n1, n2, n3);
                else Console.WriteLine("{0}\n{1}\n{2}\n\n{3}\n{4}\n{5}", n1, n2, n3, n1, n2, n3);
            }
        }
    }
}
