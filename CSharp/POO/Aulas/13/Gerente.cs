using System;

namespace _13
{
    class Gerente : Imposto
    {
        public override void valeAlimentacao(double salario)
        {
            Console.WriteLine("Desconto do gerente no vale alimentação: R$ {0}", salario * 0.15);
        }
    }
}
