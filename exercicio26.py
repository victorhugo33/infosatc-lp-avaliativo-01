def  square_meters_to_hectares ( square_meters ):
    retornar  metros_quadrados * 0,0001

def  userInput ():  
    def  verificationFloat ( square_meters ):
        verificação  =  False
        tente :
            metros quadrados  =  float ( metros quadrados )
            verificação  =  verdadeiro
        exceto :
            print ( "O valor não é um número" )
         verificação de retorno , metros quadrados ;

    enquanto  verdadeiro :
        metros quadrados  =  input ( "Qual a área em metros quadrados?" ). substituir ( "," , "." )
        verificação , metros quadrados  =  verificaçãoFloat ( metros quadrados )
        if ( verificação  ==  True ):
            pausa
    return  square_meters

metros quadrados  =  userInput ()
hectares  =  metros quadrados_para_hectares ( metros quadrados )
imprimir ( "A área em hectares:" , hectares , "ha" )
