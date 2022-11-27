#!/bin/usr/python3
""" ATUALIZAR-DATA-BASE: permite trocar uma senha na lista.
Principal Referência: https://docs.microsoft.com/pt-br/azure/mysql/connect-python
apt install python3 python3-pip
pip3 install flask mysql-connector-python"""

import os
from flask import Flask
from mysql.connector import errorcode
import mysql.connector

container_atualizar = os.getenv('CONTAINER_ATUALIZAR')
container_listar = os.getenv('CONTAINER_LISTAR')
gerador_pass_port = os.getenv('GERADOR_PASS_PORT')
atualizar_pass_port = os.getenv('ATUALIZAR_PASS_PORT')
listar_pass_port = os.getenv('LISTAR_PASS_PORT')
database_host = os.getenv('DATABASE_HOST')
mysql_user = os.getenv('MYSQL_USER')
mysql_password = os.getenv('MYSQL_PASSWORD')
mysql_database = os.getenv('MYSQL_DATABASE')
pontuacao = os.getenv('PONTUACAO') #'@#$%()[]<>'

app = Flask(__name__)

@app.route('/atualizar/<servico>/<user>/<password>')
def atualizar(servico='', user='', password=''):
    """ Server function atualizar """
    config = {
        'host':database_host,
        'user':mysql_user,
        'password':mysql_password,
        'database':mysql_database
    }
    result = [False, "ERRO", 500]
    try:
        conn = mysql.connector.connect(**config)
        print("Conexao bem sucedida")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ERRO: Nome ou senha do banco incorretas (permissao)")
            result = [False, "ERRO: Nome ou senha do banco incorretas (permissao)", 501]
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("ERRO: Banco não existe no servidor consultado")
            result = [False, "ERRO: Banco nao existe no servidor consultado", 502]
        else:
            print("ERRO: não identificado no codigo")
            print(err)
            result = [False, "ERRO: não identificado no codigo", 502]
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dados_logon WHERE user='"+user+"' AND servico='"+servico+"';")
        registers = cursor.fetchall()
        print("Resultado: ", cursor.rowcount, " registros.")
        if cursor.rowcount > 0:
            cursor.execute("UPDATE dados_logon SET password='" + password + \
                           "' WHERE user='" + user + "' AND servico='" + servico + "';")
            result = [True, 'Registro atualizado.', 200]
            print("Registro localizado")
        else:
            result = [False, "Nenhum registro encontrado.", 500]
            print("Registro não localizado")
        print("Executando o commit.")
        conn.commit()
        cursor.close()
        conn.close()
        print("Done.")
    return result

app.run(host='0.0.0.0', port=atualizar_pass_port, debug=False)
