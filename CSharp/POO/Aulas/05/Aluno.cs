using System;

namespace _05
{
    class Aluno
    {
        public string nome;
        public float nota1, nota2;
        public double media()
        {
            return (nota1 + nota2) / 2;
        }
        public string situacao(double media)
        {
            return media >= 7 ? "Aprovado" : "Reprovado";
        }
        public void mensagem()
        {
            double obterMedia = media();
            string obterSituacao = situacao(obterMedia);
            Console.WriteLine("O aluno {0} está {1}, com média de {2}", nome, obterSituacao, obterMedia);
        }
    }
}
