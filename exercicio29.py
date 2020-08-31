def  arithmetic_average ( notas ):
    retornar  soma ( notas ) / len ( notas )

def  userInput ():  
    def  verificationFloat ( nota ):
        verificação  =  False
        tente :
            nota  =  float ( nota )
            verificação  =  verdadeiro
        exceto :
            print ( "O valor não é um número" )
         verificação de retorno , nota ;

    enquanto  verdadeiro :
        nota  =  input ( "Digite uma nota?" ). substituir ( "," , "." )
        verificação , nota  =  verificaçãoFloat ( nota )
        if ( verificação  ==  True ):
            pausa
     nota de retorno

notas  = [ userInput (), userInput (), userInput (), userInput ()]
média  =  média_aritmética ( notas )
print ( "A média aritmética do valor:" , mean )
