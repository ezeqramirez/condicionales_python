# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if texto_1 > texto_2:
    print ('el mayor alfabeticamente es ', texto_1)
else:
    print ('el mayor alfabeticamente es ', texto_2)

texto_1_a = int(texto_1)
texto_2_a = int(texto_2)

if texto_1_a > texto_2_a:
    print ('la variable numerica mayor es ', texto_1_a)
else:
    print ('la variable numerica mayor es ', texto_2_a)

# sin buscar en google respondo, creo estar seguro que se depende al orden, como en el diccionario B es mayor que A
# porque se lee de izquierda a derecha, el 5 esta antes que el 7, entonces el 7 vale mas alfabeticamnte.
# y de manera numerica el 7 vale mas que el 5

#ezequiel ramirez