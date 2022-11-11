using System;

namespace _04
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Clear();
            Pessoa obj = new Pessoa();
            obj.apresentar();
            obj.apresentar("Ralf");
            obj.apresentar("Ralf", 30);
            Console.ReadLine();
        }
    }
}
