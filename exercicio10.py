def  kilometros_per_hour_to_meters_per_second ( kilometros_per_hour ):
    retornar  kilometros_per_hora / 3.6

def  userInput ():  
    def  verificationFloat ( miles_per_hour ):
        verificação  =  False
        tente :
            km_per_hour  =  float ( kilometros_per_hour )
            verificação  =  verdadeiro
        exceto :
            print ( "O valor não é um número" )
         verificação de retorno , quilômetros_por_ hora ;

    enquanto  verdadeiro :
        kilometros_per_hour  =  input ( "Qual a velocidade em kilometros por hora?" ). substituir ( "," , "." )
        verificação , quilômetros_per_hour  =  verificaçãoFloat ( quilômetros_per_hour )
        if ( verificação  ==  True ):
            pausa
    retornar  kilômetros_per_hour

kilometers_per_hour  =  userInput ()
metros_per_second  =  quilômetros_per_hour_to_meters_per_second ( quilômetros_per_hour )
imprimir ( "A velocidade em metros por segundo:" , metros_per_segundo , "m / s" )
