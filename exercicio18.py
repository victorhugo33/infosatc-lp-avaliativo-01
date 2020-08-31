def  cubic_meters_to_liters ( cubic_meters ):
    return  cubic_meters * 1000

def  userInput ():  
    def  verificationFloat ( cubic_meters ):
        verificação  =  False
        tente :
            cubic_meters  =  float ( cubic_meters )
            verificação  =  verdadeiro
        exceto :
            print ( "O valor não é um número" )
         verificação de retorno , cubic_meters ;

    enquanto  verdadeiro :
        metros cúbicos  =  entrada ( "Qual o volume em metros cúbicos?" ). substituir ( "," , "." )
        verificação , cubic_meters  =  verificationFloat ( cubic_meters )
        if ( verificação  ==  True ):
            pausa
    return  cubic_meters

cubic_meters  =  userInput ()
litros  =  cubic_meters_to_liters ( cubic_meters )
print ( "O volume em litros:" , litros , "l" )
