print("")
print("Jarvis Teste 1")
print("")
print("Ola Senhor, em que posso ajudar?")
print("")

comando = input("")

if(comando == "add tarefa"):
  print("")
  tarefa_materia = input("Qual Materia? ")
  print("")
  tarefa_prazo = input("Qual a data de entrega? ")
  print("")
  tarefa_descricao = input("O que deve fazer? ")
  print("")
  
  ver = input("Tarefa adicionada, gostaria de ver? ")
  
  if(ver == "sim"):
    print("")
    print("Voce deve fazer a tarefa de ", tarefa_materia, "ate o dia ", tarefa_prazo, ".")
    print("Descricao: ",tarefa_descricao)
  else:
    print("")
    print("Ok")
    
    comando2 = input("Deseja adicionar outra tarefa?")
    
    if(comando2 == "sim"):
      print("")
      tarefa_materia = input("Qual Materia? ")
      print("")
      tarefa_prazo = input("Qual a data de entrega? ")
      print("")
      tarefa_descricao = input("O que deve fazer? ")
      print("")
  
      ver = input("Tarefa adicionada, gostaria de ver? ")
  
      if(ver == "sim"):
        print("Voce deve fazer a tarefa de ", tarefa_materia, "ate o dia ", tarefa_prazo, ".")
        print("Descricao: ",tarefa_descricao)
        print("")
        print("Programa Finalizado")
      else:
        print("Ok")
        print("Programa Finalizado")
  
    else:
        print("Ok")
        print("Programa Finalizado")    
else:
    print("comando não reconhecido")
    print("Programa Finalizado")
