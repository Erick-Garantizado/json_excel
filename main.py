# Importando bibliotecas
import json
import pandas as pd

# Carregando arquivo json
with open("dados.json", encoding="utf-8") as arq:
    dados = json.load(arq)

# Criando data frame
excel = pd.DataFrame()

# Listas dos dados
nome = []
idade = []
cpf = []
rg = []
data_nasc = []
sexo = []
signo = []
mae = []
pai = []
email = []
senha = []
cep = []
endereco = []
numero = []
bairro = []
cidade = []
estado = []
telefone_fixo = []
celular = []
altura = []
peso = []
tipo_sanguineo = []
cor = []

# Inserindo dados nas listas
for chave, valor in enumerate(dados):
    nome.append(valor['nome'])
    idade.append(valor['idade'])
    cpf.append(valor['cpf'])
    rg.append(valor['rg'])
    data_nasc.append(valor['data_nasc'])
    sexo.append(valor['sexo'])
    signo.append(valor['signo'])
    mae.append(valor['mae'])
    pai.append(valor['pai'])
    email.append(valor['email'])
    senha.append(valor['senha'])
    cep.append(valor['cep'])
    endereco.append(valor['endereco'])
    numero.append(valor['numero'])
    bairro.append(valor['bairro'])
    cidade.append(valor['cidade'])
    estado.append(valor['estado'])
    telefone_fixo.append(valor['telefone_fixo'])
    celular.append(valor['celular'])
    altura.append(valor['altura'])
    peso.append(valor['peso'])
    tipo_sanguineo.append(valor['tipo_sanguineo'])
    cor.append(valor['cor'])

# Inserindos os dados no dataframe
excel['nome'] = nome
excel['idade'] = idade
excel['cpf'] = cpf
excel['rg'] = rg
excel['data_nasc'] = data_nasc
excel['sexo'] = sexo
excel['signo'] = signo
excel['mae'] = mae
excel['pai'] = pai
excel['email'] = email
excel['senha'] = senha
excel['cep'] = cep
excel['endereco'] = endereco
excel['numero'] = numero
excel['bairro'] = bairro
excel['cidade'] = cidade
excel['estado'] = estado
excel['telefone_fixo'] = telefone_fixo
excel['celular'] = celular
excel['altura'] = altura
excel['peso'] = peso
excel['tipo_sanguineo'] = tipo_sanguineo
excel['cor'] = cor

# Criando o arquivo em excel
excel.to_excel('dados.xlsx')