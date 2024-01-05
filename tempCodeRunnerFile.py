while True:
  try:
    valor = float(input())
    saldo_conta = 0
  
    if valor > 0:
      #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
      saldo_conta += valor
      print("Deposito realizado com sucesso!")
      print(f"Saldo atual: R$ {saldo_conta:.2f}")
      
    
    elif valor == 0:
      #TODO: Imprimir a mensagem de valor inválido.
      print("Encerrando o programa...")
      break
    
    else:
      #TODO: Imprimir a mensagem de encerrar o programa.
      print("Valor invalido! Digite um valor maior que zero.")
  except EOFError:
    break