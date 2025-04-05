import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle

# Carrega o tokenizer salvo
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Carrega o modelo treinado
model = load_model("modelo_sentimento.h5")

# Função para prever o sentimento
def prever_sentimento(textos):
    sequencias = tokenizer.texts_to_sequences(textos)
    sequencias = tf.keras.preprocessing.sequence.pad_sequences(sequencias, maxlen=100)
    previsoes = model.predict(sequencias)
    return ["positivo" if p[0] > 0.5 else "negativo" for p in previsoes]

# Lê o arquivo de entrada
df = pd.read_csv("avaliacoes.csv")

# Aplica a função de predição
df["sentimento"] = prever_sentimento(df["review"].astype(str))

# Salva os resultados
df.to_csv("output.csv", index=False)

print("Análise concluída. Resultados salvos em output.csv.")
