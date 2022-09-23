using System;

namespace bee1048
{
    class Program
    {
        static void Main(string[] args)
        {
            double salario, novosalario = 0, reajuste = 0;
            int porcentagem = 0;
            salario = double.Parse(Console.ReadLine());
            if (salario <= 400) {
                porcentagem = 15;
                reajuste = salario * 0.15;
                novosalario = salario + reajuste;
            }
            if (salario >= 400.01 && salario <= 800) {
                porcentagem = 12;
                reajuste = salario * 0.12;
                novosalario = salario + reajuste;
            }
            if (salario >= 800.01 && salario <= 1200) {
                porcentagem = 10;
                reajuste = salario * 0.1;
                novosalario = salario + reajuste;
            }
             if (salario >= 1200.01 && salario <= 2000) {
                porcentagem = 7;
                reajuste = salario * 0.07;
                novosalario = salario + reajuste;
            }
            if (salario > 2000) {
                porcentagem = 4;
                reajuste = salario * 0.04;
                novosalario = salario + reajuste;
            }
            Console.WriteLine("Novo salario: {0:0.00}", novosalario);
            Console.WriteLine("Reajuste ganho: {0:0.00}", reajuste);
            Console.WriteLine("Em percentual: {0} %", porcentagem);
        }
    }
}
