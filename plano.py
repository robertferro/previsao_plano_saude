import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from page1 import page1
from page2 import page2





# st.set_page_config(page_title = 'Previsão Plano de Saúde', 
# 				   # layout = 'wide', 
# 				   initial_sidebar_state = 'auto')

st.title('Previsão Plano de Saúde')


paginas=['HOME','EDA','SIMULAÇÃO']
pagina=st.sidebar.selectbox('Selecione a opção que deseja navegar',paginas)

# page1
if pagina=='HOME':

	st.markdown('# **Seja bem vindo** ao app')
	st.markdown('''Baseado em um dataset que trás registros de um plano de saúde, o objetvo desse webap é prever quando uma pessoa é fumante ou não.
		''')
	st.markdown('## **DISTRIBUIÇÃO DOS DADOS**')
	page1()

# page2
if pagina=='EDA':
	
	page2()

# page3	 
if pagina=='SIMULAÇÃO':
	
	st.markdown('## **Preencha os dados de acordo com os dados do cliente**')
	

	st.markdown('---')
	st.markdown(' ')
	

	# colunas 
	
	st.markdown('## Dados do cliente')
	x1 = st.number_input('Idade')
	x2 = st.selectbox('Sexo', ['Masculino','Feminino'])
	x3 = st.number_input('IMC')
	x4 = st.number_input('Filhos')
	x5 = st.radio('Regiao', ['southwest','southeast', 'northwest','northeast'])
	x6 = st.number_input('Custos')

	
	# Criando um dataframe para entrada do modelo 
	dicionario = {'Idade':[x1], 
				  'Sexo':[x2],
				  'IMC':[x3], 
				  'Filhos':[x4],
		       	  'Regiao':[x5], 
		       	  'Custos':[x6], 
		       	  }


	df = pd.DataFrame(dicionario) 

	#  encoding das variaveis categoricas do dataframe
	dic_sexo = {'male':0,
           'female':1}

	dic_regiao = {'southwest':0, 'southeast':1, 'northwest':2, 'northeast':3}

	dados = df.copy()

	dados['Sexo'] = dados['Sexo'].map(dic_sexo)

	dados['Regiao'] = dados['Regiao'].map(dic_regiao)


	st.write(df)

	st.markdown('---')

	st.markdown('# Simulação')


	modelo = open('best_model', 'rb')
	modelo = pickle.load(modelo)



	if st.button('Executar a Simulação'):
		pred = modelo.predict(dados)
		if pred==1:
			st.warning('''De acordo com os dados de entrada a previsão
							 foi que a pessoa em questão é ''')
			st.markdown('# **Fumante**')
			st.error('''O modelo utilizado acerta em 88% das
			 			   vezes quando prever como sendo fumante e
			 			   consegue capturar até 96% dos exemplos de fumantes''')
		else:
			st.success('''De acordo com os dados de entrada a previsão
							 foi que a pessoa em questão é ''')
			st.markdown('# **Não Fumante**')
			st.markdown('''O modelo utilizado acerta em 99% das
			 			   vezes quando prever como não fumante  e
			 			    consegue capturar até 96% dos exemplos de não fumantes''')
			st.balloons()
		
