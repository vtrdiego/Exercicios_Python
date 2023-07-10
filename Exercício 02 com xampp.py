import mysql.connector

conexao=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='lab07'
)

x=conexao.cursor()
print(conexao)

#x.execute('create database lab07')

'''x.execute('create table clientes(cod_cliente int(5) primary key auto_increment,\
nome_cliente varchar(50),sexo varchar(10),email varchar(50),telefone int(15))')'''

'''x.execute('create table endereco(cod_cliente int(5),logradouro varchar(50),cidade varchar(30),\
estado varchar(20),cep int(10),foreign key(cod_cliente)references clientes(cod_cliente))')'''

'''x.execute('create table bens(cod_cliente int(5),cod_bens int(5) primary key auto_increment,\
tipo varchar(40),valor varchar(10),foreign key(cod_cliente)references clientes(cod_cliente))')'''

'''cadastroClientes="insert into clientes(nome_cliente,sexo,email,telefone)values(%s,%s,%s,%s)"
clientes=[
    ('Carlos da Silva','M','carlos-silva@gmail.com',921854473),
    ('Angélica Almeida','F','angelicaAlmeida@gmail.com',985693326),
    ('Fabricio Alves','M','fabricioAlves@hotmail.com',974632584),
    ('Jorge Henrique','M','jorgeHQ@gmail.com',927415445),
    ('Renata Martins','F','renataMartins@hotmail.com',982635415),
    ]

x.executemany(cadastroClientes,clientes)
conexao.commit()
print(x.rowcount,"registros foram inseridos")'''


'''enderecoClientes="insert into endereco(cod_cliente,logradouro,cidade,estado,cep)values(%s,%s,%s,%s,%s)"
enderecos=[
    (1,'Rua Antônio de Paula nº85','São Paulo','SP',52637894),
    (2,'Rua Francisco de Souza nº541','São Paulo','SP',52441367),
    (3,'Rua Alberto Torres nº74','Rio de Janeiro','RJ',24635598),
    (4,'Avenida Roberto da Silva nº1425','Belo Horizonte','MG',96485563),
    (5,'Avenida Siqueira Campos nº855','Rio de Janeiro','RJ',27556895)
    ]

x.executemany(enderecoClientes,enderecos)
conexao.commit()
print(x.rowcount,"registros foram inseridos")'''


'''bensClientes="insert into bens(cod_cliente,tipo,valor)values(%s,%s,%s)"
bens=[
    (1,'Casa','200.000,00'),
    (2,'Carro','85.000,00'),
    (3,'Carro','78.000,00'),
    (4,'Casa','220.000,00'),
    (5,'Apartamento','150.000,00')
    ]

x.executemany(bensClientes,bens)
conexao.commit()
print(x.rowcount,"registros foram inseridos")'''


'''x.execute('select * from clientes order by nome_cliente')
tabela=x.fetchall()
for i in tabela:
    print(i)'''


'''x.execute('update clientes set nome_cliente="Bruno da Silva" where cod_cliente=1')
conexao.commit()
print(x.rowcount,"registro alterado")'''


'''x.execute('delete from endereco where cod_cliente=5')
conexao.commit()
print(x.rowcount,"registro deletado")'''








