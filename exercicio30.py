def  conversão ( valor_real , cotacao_dolar ):
    return  valor_real * cotacao_dolar

def  userInput ():  
    def  verificationFloat ( valor_real , cotacao_dolar ):
        verificação  =  False
        tente :
            valor_real  =  float ( valor_real )
            cotacao_dolar  =  float ( cotacao_dolar )
            verificação  =  verdadeiro
        exceto :
            print ( "O valor não é um número" )
         verificação de retorno , valor_real , cotacao_dolar ;

    enquanto  verdadeiro :
        valor_real  =  input ( "Digite um valor em reais?" ). substituir ( "," , "." )
        cotacao_dolar  =  input ( "Digite a cotação do dólar?" ). substituir ( "," , "." )
        verificação , valor_real , cotacao_dolar =  verificationFloat ( valor_real , cotacao_dolar )
        if ( verificação  ==  True ):
            pausa
    return  valor_real , cotacao_dolar ;

valor_real , cotacao_dolar  =  userInput ()
dolar  =  redondo ( conversão ( valor_real , cotacao_dolar ), 2 )
print ( "O valor em dólares: US $" , dolar 
