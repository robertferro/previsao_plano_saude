import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ANALISES COM UM BOTAO PARA QUE APAREÇAM CONFORMA SEJAM SELECIONADAS
def page2():

	# CARREGANDO OS DADOS PARA VISUALIZAÇÃO
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

	opcoes = ['Correlação','Gráficos de Dispersão']
	opcao = st.sidebar.selectbox('Selecione a opção que deseja visualizar',opcoes)

	if opcao == "Correlação":

		st.markdown('# Matriz de correlação')
		corr = df.corr()
		mask = np.triu(np.ones_like(corr, dtype=np.bool))

		ax = sns.heatmap(corr, mask=mask, annot=True, center=0, cmap="YlGnBu")
		st.pyplot(plt)
		st.write('**Idade e Custo tem uma correlação positiva de 0.3, o que indica que os custos tendem a aumentar de acordo com a idade.**')

		st.write('**Fumante e Custos tem correlação positiva de 0.79, forte, que indica a condição de ser fumante ou não implica diretamente nos custos.**')

		st.markdown('**O IMC também exerce influência no custo,\n'
					'já que esse é um índice que diz se a pessoa está ou não dentro do peso recomendado, o que pode implicar em seu estado de saúde e consequentemente nos custos.**')

	elif opcao == "Gráficos de Dispersão":
		st.write('Nesta seção pode ser vistos gráficos de dispersão entre as variáveis quetem maior correlação e pode-se observar como elas se comportam.')
		
		st.write()
		analises = ['CUSTOS X IDADE','CUSTOS X IMC']
		analise = st.sidebar.selectbox('Selecione a análise desejada',analises)
		if analise =='CUSTOS X IDADE':
			fig,ax = plt.subplots(1,2, figsize=(12,6))
			sns.scatterplot(y='Custos',x='Idade',data=df,hue='Fumante',ax=ax[0])
			ax[0].set_title('Idade X Custos X Fumante');

			sns.scatterplot(y='Custos',x='Idade',data=df[df['Custos']>12000],hue='Fumante',ax=ax[1]);
			ax[1].set_title('IIdade X Custos X Fumante');
			st.pyplot(plt)

			st.markdown('## **Análises**')

			st.markdown('**Quando o custo vai até 12 mil, a relação Idade X Custo fica mais evidente.\n'
						'As pessoas com custo abaixo disso geralmente não são fumantes e o custo aumenta\n'
						'de forma gradativa conforme a idade avança.**')
			st.markdown('**Pessoas não fumantes se concentram com custos abaixo de 12 mil.**')
			st.markdown('**O fato de ser Fumante ou não pode elevar até em 10X os custos.**')
			st.markdown('**Quando os custos são superiores a 12 mil, a maioria dos registros são de possoas fumantes.**')
			st.markdown('**A maioria dos registros de pessoas não fumantes que ultrapassam os custos de 12 mil, se concentram na faixa etária de 52 a 64 anos.**')
			st.markdown('''**Quando os custos ultrapassam os 12 mil, pode-se perceber que se formam 2 grupos, um com custo abaixo de 30 mil,
							onde existem pessoas fumantes e não fumantes de maneira mais equilibrada, e outro com custos acima de 30mil, com grande maioria sendo pessoas fumantes.**''')


		elif analise == 'CUSTOS X IMC':
			fig, ax = plt.subplots(1,2, figsize=(12,6))
			sns.scatterplot(y='Custos',x='IMC',data=df[df['Fumante']==0], ax=ax[0],color='g',alpha=0.7);
			ax[0].set_title('Não fumantes',fontsize=25)

			sns.scatterplot(y='Custos',x='IMC',data=df[df['Fumante']==1], ax=ax[1],color='r', alpha=0.7);
			ax[1].set_title('Fumantes',fontsize=25);
			st.pyplot(plt)

			st.markdown('## **Análises**')
			st.markdown('''**A relação entre Custos e IMC, é mais acentuada quando as 
							pessoas são fumantes, onde conforme o IMC aumenta, os custos também sobem de maneira mais acentuada.
**''')
			st.markdown('''**Quando se trata de pessoas não fumantes,o IMC não influencia tanto o custo, sendo que nem sempre que sobe 
							o IMC o custo também sobe, e o registros encontram-se concentrados com custo abaixo de 15mil.**''')
	pass