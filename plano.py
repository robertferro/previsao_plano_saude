import streamlit as st
import pandas as pd
import pickle



st.set_page_config(page_title = 'Previsão Plano de Saúde', 
				   layout = 'wide', 
				   initial_sidebar_state = 'auto')

st.title('Previsão Plano de Saúde')


paginas=['Home','Objetivo','Simulação']
pagina=st.sidebar.selectbox('Selecione a opção que deseja navegar',paginas)

# page1
if pagina=='Home':
	# imagem = 'img3.jpg'
	st.markdown('# **Seja bem vindo** ao previsao plano saude app')
	# st.image(imagem,use_column_width='always')

# page2
if pagina=='RESUMO':
	# insight='insight.jpg'
	st.write(' Este web app foi desenvolvido baseado em um dataset do que traz operações bancárias com montante entre 4 mil e 35 mil Euros, e tem como objetivo reduzir o índice de inadimplência, que inicialmente era de 21% , chegando a ficar em torno de 6%, como pode ser observado no gráfico abaixo. ')
	# st.image(insight)

# page3	 
if pagina=='Simulação':
	
	st.markdown('## **Preencha os dados de acordo com os dados do cliente**')
	

	st.markdown('---')
	st.markdown(' ')

	# sidebar
	

	# colunas 
	col1, col2 = st.columns(2)
	col1.markdown('## Dados do cliente')
	x1 = col1.number_input('Idade')
	x2 = col1.selectbox('Sexo', ['Masculino','Feminino'])
	x3 = col1.number_input('IMC')
	x4 = col1.number_input('Filhos')
	x5 = col1.radio('Regiao', ['southwest','southeast', 'northwest','northeast'])
	x6 = col1.number_input('Custos')

	
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

	st.markdown('### Simulação')


	modelo = open('best_model', 'rb')
	modelo = pickle.load(modelo)



	if st.button('Executar a Simulação'):
		pred = modelo.predict(dados)
		if pred==1:
			st.markdown('# **Fumante**')
		else:
			st.markdown('# **Não Fumante**')
		
