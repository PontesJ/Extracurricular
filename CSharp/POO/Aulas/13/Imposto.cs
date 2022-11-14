using System;

namespace _13
{
    class Imposto
    {
        public virtual void valeAlimentacao(double salario)
        {
            Console.WriteLine("Desconto padrão do vale alimentação: R$ {0}", salario * 0.1);
        }
        public void valeTransporte(double salario)
        {
            Console.WriteLine("Desconto padrão do vale transporte: R$ {0}", salario * 0.06);
        }
    }
}
