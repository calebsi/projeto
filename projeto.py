def caixa_mercado():
  precos = {
    "maçã": 1.99,
    "banana": 2.99,
    "laranja": 3.99,
    "uva": 4.99,
    "pêra": 5.99,
  }
  total = 0
  while True:
    produto = input("Qual produto você deseja comprar? (Digite 'sair' para finalizar a compra): ")
    if produto == "sair":
      break
    elif produto in precos:
      quantidade = int(input("Quantos quilos de {} você deseja comprar? ".format(produto)))
      total += precos[produto] * quantidade
    else:
      print("Produto não encontrado.")
  print("Total a pagar: R${:.2f}".format(total))

caixa_mercado()