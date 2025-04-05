# Análise de Sentimentos Offline com Modelo GRU (Olist Reviews)

Este projeto executa uma análise de sentimentos **offline** em avaliações da base da Olist utilizando um modelo GRU treinado previamente em TensorFlow/Keras. Ele está empacotado e pronto para rodar via Docker, tornando a execução simples e portátil, sem necessidade de reconfigurar ambientes locais.

## 📁 Estrutura do Projeto

```
offline_sentiment_project/
├── app.py                        # Script principal de inferência
├── modelo_sentimento.h5         # Modelo GRU treinado
├── tokenizer.pkl                # Tokenizer treinado
├── olist_order_reviews_dataset.csv # Base de dados de entrada
├── requirements.txt             # Dependências do Python
├── Dockerfile                   # Imagem Docker para o app
└── README.md                    # Este arquivo
```

---

## ✅ O que o projeto faz

O script `app.py` carrega:

1. O modelo treinado (`modelo_sentimento.h5`);
2. O tokenizer (`tokenizer.pkl`);
3. A base de dados de avaliações (`olist_order_reviews_dataset.csv`).

Ele aplica pré-processamento textual e realiza a inferência de sentimento (positivo ou negativo) em cada review do dataset. Os resultados são salvos em um novo CSV com a coluna `sentimento`.

---

## 🚀 Como configurar e executar

### 1. Clone ou extraia o projeto

Caso tenha o `.zip`, extraia:

```bash
unzip offline_sentiment_project.zip
cd offline_sentiment_project
```

### 2. Construa a imagem Docker

Certifique-se de estar na raiz do projeto e que o Docker está instalado no seu sistema:

```bash
docker build -t sentimento-offline .
```

### 3. Execute o contêiner

O volume `-v $(pwd):/app` garante que os arquivos de entrada e saída fiquem sincronizados com seu diretório local.

```bash
docker run -v $(pwd):/app sentimento-offline
```

---

## 📤 O que acontece durante a execução

- O `app.py` é executado automaticamente dentro do contêiner;
- Ele carrega o modelo e o tokenizer salvos;
- Lê o arquivo `olist_order_reviews_dataset.csv`;
- Aplica a função `prever_sentimento` nas reviews disponíveis;
- Cria um novo arquivo com o resultado: `saida_sentimentos.csv`.

---

## 📄 Saída esperada

Um novo arquivo chamado `saida_sentimentos.csv` será gerado com a seguinte estrutura:

```
review_comment_message                 sentimento
Gostei muito do produto!              positivo
Não funcionou como esperado           negativo
Atendimento ruim, entrega atrasada   negativo
Produto excelente, recomendo!        positivo
```

---

## 🛠️ Problemas comuns

- `EOFError: Ran out of input`: significa que o `tokenizer.pkl` estava vazio — verifique se ele foi salvo corretamente durante o treinamento.
- `ValueError: ambiguous truth value`: ocorre ao tentar comparar diretamente arrays do NumPy — use `.item()` ou `float(p)` para acessar o valor escalar da predição.
- `KeyError: 'review'`: certifique-se de que a coluna usada no `app.py` para as avaliações (`review`) corresponda ao nome da coluna real no CSV.

---

## 📚 Requisitos

O ambiente é criado dentro do Docker, mas caso queira rodar localmente, instale:

```bash
pip install -r requirements.txt
```

---

## 🧠 Modelo Utilizado

- **Arquitetura**: GRU  
- **Framework**: TensorFlow/Keras  
- **Tokenizer**: Keras Tokenizer  
- **Treinamento**: feito com reviews da Olist (`review_comment_message`)
