using System;

namespace _13
{
    class Atendente : Imposto
    {
        public override void valeAlimentacao(double salario)
        {
            Console.WriteLine("Desconto do atendente no vale alimentação: R$ {0}", salario * 0.12);
        }
    }
}
