# código de geração do gráfico 
import pandas as pd
import seaborn as sns

dados = pd.read_csv('gasolina.csv')

with sns.axes_style('darkgrid'):
  grafico = sns.lineplot(
      data=dados, 
      x='dia', 
      y='venda'
    )
  
  grafico.set(
      title='Variação do preço da gasolina', 
      ylabel='Preço (R$)', 
      xlabel='Dia'
    )

  imagem = grafico.get_figure()    
  imagem.savefig('variacao_gasolina.png', dpi=500)
