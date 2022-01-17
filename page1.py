import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def carregar_dados():
	url='https://raw.githubusercontent.com/robertferro/previsao_plano_saude/main/dados_plano.csv'
	df = pd.read_csv(url)
	dic_sexo = {'male':0,
	       'female':1}
	dic_fumante = {'yes':1,
	              'no':0}
	dic_regiao = {'southwest':0, 'southeast':1, 'northwest':2, 'northeast':3}
	df['Sexo'] = df['Sexo'].map(dic_sexo)
	df['Fumante'] = df['Fumante'].map(dic_fumante)
	df['Regiao'] = df['Regiao'].map(dic_regiao)
	return df

df_page1 = carregar_dados()




def page1():
	st.markdown('# Visão Geral dos Dados')
	st.write()
	df_page1.hist(figsize=(12,12))
	st.pyplot(plt)

	st.markdown('''**75% dos registros tem custo inferior ou igual a 16639.912515**''')
	st.markdown('''**Os dados estão bem distribuídos, exceto com relação a variável alvo Fumante,
					 que apresenta mais pessoas que não são fumantes e a variável Filhos,
	 				onde as categorias 4 ou 5 filhos apresentam menor número de registros.**''')
	col1,col2 = st.columns(2)
	f1 = col1.checkbox('FUMANTE')
	f2 = col2.checkbox('NÃO FUMANTE')
	if f1:
		df_page1[df_page1['Fumante']==1].drop('Fumante',axis=1).hist(figsize=(12,8))
		st.pyplot(plt)
	else:
		pass

	if f2 :
		df_page1[df_page1['Fumante']==0].drop('Fumante',axis=1).hist(figsize=(12,8))
		st.pyplot(plt)
	else:
		pass
	pass