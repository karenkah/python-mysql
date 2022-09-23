# python-mysql
## Inserir e ler dados em banco mysql, em ambiente docker.

### Executar o container mysql
```
$ docker run --network tua-rede --name nomecontainer -e MYSQL_ROOT_PASSWORD=tua-senha -d mysql:tag
```
### Entrar no container mysql
```
$ docker exec -it nomecontainer /bin/sh
```
### Executar o comando para entrar no banco de dados
```
mysql -u root -p
senha
```
### Executar os comandos para criar database e criar tabela (arquivo createNoMysql)

### Sair do banco de dados e sair do container mysql.

### Criar a imagem de python à partir do dockerfile, onde abrange o script dadosmysql.py e garante a instalação do mysql-connector-python:
```
$docker build -t suaimagempython .
```
### Executar o container da imagempython
```
$docker run -it --network tua-rede --name meupython suaimagempython

### Executar o script dadosmysql.py no diretório onde está salvo
```
$ python ./dadosmysql.py
```


