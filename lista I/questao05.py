preco = float(input("Digite o preço da mercadoria "))
p = int(input("Digite a porcentagem de desconto "))
desconto = preco * p / 100
print("O desconto é de R$ %.2f e o preço a pagar é R$ %.2f" %(desconto, preco - desconto))
                                                        
