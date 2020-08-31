def  miles_to_miles ( quilômetros ):
     quilômetros de retorno / 1,6

def  userInput ():  
    def  verificationFloat ( quilômetros ):
        verificação  =  False
        tente :
            quilômetros  =  flutuação ( quilômetros )
            verificação  =  verdadeiro
        exceto :
            print ( "O valor não é um número" )
         verificação de retorno , quilômetros ;

    enquanto  verdadeiro :
        quilômetros  =  entrada ( "Qual a distância em kilometros?" ). substituir ( "," , "." )
        verificação , quilômetros  =  verificaçãoFloat ( quilômetros )
        if ( verificação  ==  True ):
            pausa
     quilômetros de retorno

quilômetros  =  userInput ()
milhas  =  quilômetros_ a_ milhas ( quilômetros )
print ( "A distância em milhas:" , milhas , "mi" )
