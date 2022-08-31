import mysql.connector

con = mysql.connector.connect(
    host='<iphostmysql>',
    user='',
    password='',
    database='registro',
)

cursor = con.cursor()

musica = "Demons"
artista = "Imagine Dragons"
comando = f'INSERT INTO musicas (musica, artista) VALUES ("{musica}", "{artista}")'
cursor.execute(comando)

con.commit()


ler = f'SELECT musica FROM musicas WHERE idmusica = "1";'
cursor.execute(ler)
resultado = cursor.fetchall()

ler2 = f'SELECT artista FROM musicas WHERE idmusica = "1";'
cursor.execute(ler2)
resultado2 = cursor.fetchall()

print(f'{resultado} é uma musica do {resultado2}')


cursor.close()
con.close()