import pandas as pd 
import matplotlib.pyplot as plt

#faturamento, items mais vendidos, avaliacoes clientes, categorias mais vendidas e frete medio

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

#print(loja.head());

def faturamento(lojas):
    lojas;
    faturamento = (lojas["Preço"] + lojas["Frete"]).sum()
    return faturamento;

def qtd_produtos_categorias(lojas):
 lojas;
 resultado = lojas.groupby('Categoria do Produto')['Produto'].count().sort_values()
 return resultado 

print(qtd_produtos_categorias(loja))
#qtd categorias por produto = loja.groupby('Produto')['Categoria do Produto'].nunique().sort_values()

def avalia_cliente(lojas):  
    lojas;
    avaliacoes = round(lojas['Avaliação da compra'].mean(),2);
    return avaliacoes

def produtos_mais_e_menos_vendidos(lojas):
   lojas;
   produto =lojas['Produto'].value_counts()

   produto_menos = produto[produto == produto.min()];
   produto_mais = produto[produto == produto.max()];
   return produto_menos, produto_mais;
   
def media_frete(lojas):  
    lojas;
    media = round(lojas['Frete'].mean(),2);
    return media;

def separa_data(lojas):
   lojas["dia"] = lojas["Data da Compra"].str.split("/").str[0];
   lojas["mes"] = lojas["Data da Compra"].str.split("/").str[1];
   lojas["ano"] = lojas["Data da Compra"].str.split("/").str[2];

separa_data(loja);
separa_data(loja2);
separa_data(loja3);
separa_data(loja4);

#def grafico_faturamento_por_ano(lojas):
#    # calcula o faturamento por ano
#    faturamento_por_ano = (lojas["Preço"] + lojas["Frete"]).groupby(lojas["ano"]).sum()
#
#    # gera o gráfico
#    plt.bar(faturamento_por_ano.index, faturamento_por_ano.values)
#    plt.title("Total faturado por ano")
#    plt.xlabel("Ano")
#    plt.ylabel("Faturamento (R$)")
#    plt.xticks(rotation=0)
#    plt.show()
#
#def grafico_avaliacao_media_por_ano(lojas):
#    # calcula média da avaliação para cada ano
#    avaliacao_ano = lojas.groupby("ano")["Avaliação da compra"].mean()
#
#    plt.plot(avaliacao_ano.index, avaliacao_ano.values, marker="o")
#    plt.title("Avaliação Média por Ano")
#    plt.xlabel("Ano")
#    plt.ylabel("Avaliação Média")
#    plt.xticks(rotation=0)
#    plt.grid(True)
#    plt.show()
#
#def grafico_vendas_por_estado(lojas):
#    # conta quantas vendas ocorreram em cada estado
#    vendas_estado = lojas["Local da compra"].value_counts()
#
#    plt.bar(vendas_estado.index, vendas_estado.values)
#    plt.title("Quantidade de Vendas por Estado")
#    plt.xlabel("Estado")
#    plt.ylabel("Quantidade de Vendas")
#    plt.xticks(rotation=0)
#    plt.show()
#
#def grafico_faturamento_por_categoria(lojas):
#    # calcula o faturamento por categoria
#    faturamento_categoria = (lojas["Preço"] + lojas["Frete"]).groupby(lojas["Categoria do Produto"]).sum()
#
#    plt.bar(faturamento_categoria.index, faturamento_categoria.values)
#    plt.title("Faturamento por Categoria de Produto")
#    plt.xlabel("Categoria")
#    plt.ylabel("Faturamento (R$)")
#    plt.xticks(rotation=45)
#    plt.show()

def dashboard_loja(lojas):

    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    
    # ------- FATURAMENTO POR ANO -------
    faturamento_ano = (lojas["Preço"] + lojas["Frete"]).groupby(lojas["ano"]).sum()
    axs[0, 0].bar(faturamento_ano.index, faturamento_ano.values)
    axs[0, 0].set_title("Faturamento por Ano")
    axs[0, 0].set_xlabel("Ano")
    axs[0, 0].set_ylabel("R$")

    # ------- AVALIAÇÃO MÉDIA POR ANO -------
    avaliacao_ano = lojas.groupby("ano")["Avaliação da compra"].mean()
    axs[0, 1].plot(avaliacao_ano.index, avaliacao_ano.values, marker="o")
    axs[0, 1].set_title("Avaliação Média por Ano")
    axs[0, 1].set_xlabel("Ano")
    axs[0, 1].set_ylabel("Avaliação")
    axs[0, 1].grid(True)

    # ------- VENDAS POR ESTADO -------
    vendas_estado = lojas["Local da compra"].value_counts()
    axs[1, 0].bar(vendas_estado.index, vendas_estado.values)
    axs[1, 0].set_title("Vendas por Estado")
    axs[1, 0].set_xlabel("Estado")
    axs[1, 0].set_ylabel("Quantidade")

    # ------- FATURAMENTO POR CATEGORIA -------
    faturamento_categoria = (lojas["Preço"] + lojas["Frete"]).groupby(lojas["Categoria do Produto"]).sum()
    axs[1, 1].bar(faturamento_categoria.index, faturamento_categoria.values)
    axs[1, 1].set_title("Faturamento por Categoria")
    axs[1, 1].set_xlabel("Categoria")
    axs[1, 1].set_ylabel("R$")
    axs[1, 1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.show()


dashboard_loja(loja);
dashboard_loja(loja2);
dashboard_loja(loja3);
dashboard_loja(loja4);

