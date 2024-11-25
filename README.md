# Análise de Desempenho Acadêmico

## Descrição do Projeto

Este projeto consiste em um programa que analisa e exibe informações sobre o desempenho acadêmico de alunos em uma turma. O sistema lê dados de notas (em um arquivo CSV ou inseridos manualmente) e fornece análises como média, mediana, variância, e histogramas de notas, usando bibliotecas como Pandas e Matplotlib.

## Funcionalidades

- **Leitura de Dados:** Carrega dados de um arquivo CSV com as notas dos alunos.
- **Análises Estatísticas:** Calcula média, mediana, variância e desvio padrão das notas.
- **Visualização:** Gera um histograma para mostrar a distribuição das notas.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação.
- **Pandas:** Biblioteca para manipulação e análise de dados.
- **NumPy:** Biblioteca para cálculos matemáticos e estatísticos.
- **Matplotlib:** Biblioteca para geração de gráficos.

## Estrutura do Projeto

```plaintext
projeto-analise-notas/
│
├── data/
│   └── notas.csv         # Arquivo CSV com as notas dos alunos
│
├── src/
│   ├── main.py           # Arquivo principal do programa
│   ├── analise.py        # Módulo para análises estatísticas
│   └── visualizacao.py    # Módulo para visualização de dados
│
├── venv_m3               #ambiente virtual
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto

```

# 📖 Como Rodar

## 🛠️ Com Ambiente Virtual

1. **Crie o ambiente virtual:**

   ```bash
   python3 -m venv venv_m3
   ```

2. **Ative o ambiente virtual:**

   - **Windows:**

     ```bash
     venv_m3\Scripts\activate
     ```

   - **macOS e Linux:**
     ```bash
     source venv_m3/bin/activate
     ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o programa:**
   Navegue até o diretório `src` e execute:

   ```bash
   python main.py
   ```

5. **(Opcional) Desative o ambiente virtual:**
   ```bash
   deactivate
   ```

### Rodando sem Ambiente Virtual

1. **Instale as dependências globalmente:**
   ```bash
    pip install -r requirements.txt
   ```
2. **Execute o programa:**

   Navegue até o diretório `src` e execute:

   ```bash
   python3 main.py
   ```

## Resultados Esperados

O programa exibirá as estatísticas calculadas no console e gerará um arquivo `distribuicao_notas`.
