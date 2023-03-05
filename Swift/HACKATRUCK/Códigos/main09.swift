var porcentagem : Int = 60

switch porcentagem
{
    case 0:
        print("Insatisfatório, não acertou nenhuma questão.")
    case 1...20:
        print("Insatisfatório, desempenho muito baixo.")
    case 21..<50:
        print("Insatisfatório, vamos estudar mais?")
    case 50..<70:
        print("Foi por pouco, vamos estudar mais!")
    case 70..<90:
        print("Satisfatório, você foi aprovado!")
    default:
        print("Excelente, desempenho memorável!")
}