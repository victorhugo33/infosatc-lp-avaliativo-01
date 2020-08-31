def  square_meters_to_hectares ( hectares ):
    retorno  hectares * 10.000

def  userInput ():  
    def  verificationFloat ( hectares ):
        verificação  =  False
        tente :
            hectares  =  flutuar ( hectares )
            verificação  =  verdadeiro
        exceto :
            print ( "O valor não é um número" )
         verificação de retorno , hectares ;

    enquanto  verdadeiro :
        hectares  =  insumo ( "Qual a área em hectares?" ). substituir ( "," , "." )
        verificação , hectares  =  verificaçãoFloat ( hectares )
        if ( verificação  ==  True ):
            pausa
    retornar  hectares

hectares  =  userInput ()
metros_quadrados  =  metros_quadrados_para_hectares ( hectares )
imprimir ( "A área em metros quadrados:" , metros quadrados , "m²" )
