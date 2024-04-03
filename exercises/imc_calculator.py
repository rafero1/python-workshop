"""
Receba o peso e a altura de uma pessoa.

Calcule o IMC (Índice de Massa Corporal) de uma pessoa e retorne se
ela está com peso normal, abaixo do peso, ou acima do peso.

O IMC é calculado pela fórmula: peso / (altura ** 2)

Considere que:
IMC < 18.5 é abaixo do peso,
IMC >= 18.5 e IMC <= 24.9 é peso normal,
IMC > 24.9 e IMC <= 29.9 é acima do peso,
IMC > 29.9 é obesisdade.

retorne "Abaixo do peso", "Peso normal", "Acima do peso" ou "Obesidade" conforme o caso.

Dicas:
- use input() para receber os valores do usuário do peso e altura, e float() para converter para float

Execute o programa rodando o seguinte comando no terminal dentro da pasta raiz do projeto:
python exercises/imc_calculator.py
"""


def imc_calculator():
  raise NotImplementedError


# a condição __name__ == "__main__" verifica se o arquivo está sendo executado diretamente
# ele serve para garantir que o bloco dentro do if só seja executado se o arquivo for executado diretamente
# é uma forma de prevenir que um código indevido seja executado quando o arquivo é importado como módulo
if __name__ == "__main__":
  imc_calculator()
