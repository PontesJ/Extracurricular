using System;

namespace bee1005
{
    class Program
    {
        static void Main(string[] args)
        {
            double A, B, media;
            A = double.Parse(Console.ReadLine());
            B = double.Parse(Console.ReadLine());
            if (A >= 0 && B >= 0 && A <= 10 && B <= 10) {
                media = ((A * 3.5) + (B * 7.5)) / 11;
                Console.WriteLine("MEDIA = {0:0.00000}", media);
            }
        }
    }
}
