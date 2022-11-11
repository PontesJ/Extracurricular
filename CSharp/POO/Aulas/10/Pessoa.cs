using System;

namespace _10
{
    class Pessoa
    {
        private string nome;
        public string Nome
        {
            get{return nome;}  // Receber
            set{nome = value;} // Enviar
        }
    }
}
