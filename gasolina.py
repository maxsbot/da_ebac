# código de geração do gráfico
import pandas as pd
import seaborn as sns

dados_gasolina = pd.read_csv("gasolina.csv")

with sns.axes_style("darkgrid"):
    grafico = sns.lineplot(data=dados_gasolina, x="dia", y="venda")
    grafico.set(
        title="Valor medio diário da gasolina", xlabel="Dia", ylabel="Valor (R$)"
    )

    imagem = grafico.get_figure()
    imagem.savefig("variacao_gasolina.png", dpi=500)
