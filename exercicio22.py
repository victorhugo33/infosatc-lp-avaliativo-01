def  yard_to_meters ( yard ):
     jardas de retorno * 0,91

def  userInput ():  
    def  verificationFloat ( jardas ):
        verificação  =  False
        tente :
            jardas  =  flutuação ( jardas )
            verificação  =  verdadeiro
        exceto :
            print ( "O valor não é um número" )
         verificação de retorno , jardas ;

    enquanto  verdadeiro :
        jardas  =  input ( "Qual o comprimento em jardas?" ). substituir ( "," , "." )
        verificação , jardas  =  verificação Flutuação ( jardas )
        if ( verificação  ==  True ):
            pausa
     jardas de retorno

jardas  =  userInput ()
metros  =  jardas_ a_metros ( jardas )
imprimir ( "O comprimento em metros:" , metros , "m" )
