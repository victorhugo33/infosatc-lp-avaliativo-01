  
def  fahrenheitToCelsius ( fahrenheitTemperature ):
    return  5 * ( fahrenheitTemperature - 32 ) / 9

def  userInput ():
    def  verificationFloat ( fahrenheitTemperature ):
        verificação  =  False
        tente :
            fahrenheitTemperature  =  float ( fahrenheitTemperature )
            verificação  =  verdadeiro
        exceto :
            print ( "O valor  não é um número" )
         verificação de retorno , fahrenheitTemperature ;

    enquanto  verdadeiro :
        fahrenheitTemperature  =  input ( "Qual a temperatura em graus fahrenheit?" ). substituir ( "," , "." )
        verificação , fahrenheitTemperature  =  verificationFloat ( fahrenheitTemperature )
        if ( verificação  ==  True ):
            pausa
    return  fahrenheitTemperature

fahrenheitTemperature  =  userInput ()
celsiusTemperature  =  fahrenheitToCelsius ( fahrenheitTemperature )
imprimir ( "A temperatura em celsius:" , celsiusTemperature , "ºC" )
