def  kilograms_to_pounds ( kilograms ):
    retorno  quilogramas / 0,45

def  userInput ():  
    def  verificationFloat ( quilogramas ):
        verificação  =  False
        tente :
            quilogramas  =  flutuante ( quilogramas )
            verificação  =  verdadeiro
        exceto :
            print ( "O valor não é um número" )
         verificação de retorno , quilogramas ;

    enquanto  verdadeiro :
        quilogramas  =  input ( "Qual a massa em quilogramas?" ). substituir ( "," , "." )
        verificação , quilogramas  =  verificaçãoFloat ( quilogramas )
        if ( verificação  ==  True ):
            pausa
    retornar  quilogramas

quilogramas  =  userInput ()
libras  =  kilograms_to_pounds ( kilograms )
print ( "A massa em libras:" , libras , "lb" )
