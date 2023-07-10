import mysql.connector

conexao=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='lab06'
)

x=conexao.cursor()
print(conexao)

#x.execute('create database lab06')

'''x.execute('create table computador(codigo_pc int(5) primary key auto_increment,marca_pc varchar(20),tipo_pc varchar(20),\
valor_pc varchar(10),qnt_pc int(5))')'''

'''y="insert into computador(marca_pc,tipo_pc,valor_pc,qnt_pc) values (%s,%s,%s,%s)"

tabela=[
    ('Positivo','Desktop','2.000',8),
    ('Dell','Desktop','3.500',5),
    ('Acer','All in One','2.600',3),
    ('Lenovo','Notebook','2.500',5),
    ('HP','Desktop','3.100',3),
    ]

x.executemany(y,tabela)
conexao.commit()
print(x.rowcount,'Registros foram inseridos!')'''

'''x.execute('select * from computador order by marca_pc')
info=x.fetchall()
for i in info:
    print(i)'''




    



