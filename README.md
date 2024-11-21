# Webscraping Notas - Sige

Este projeto tem como objetivo ajudar coordenadores de escolas a coletar automaticamente informações sobre as notas dos alunos diretamente do sistema **Sige**. A aplicação realiza um **webscraping** para identificar a quantidade de alunos com notas **maiores ou iguais a 6** e **menores que 6**, organizando os dados em um arquivo CSV para facilitar a análise e o acompanhamento do desempenho acadêmico.

---

## 🚀 Funcionalidades

- Automatiza a navegação no sistema Sige para seleção de turmas, séries e outros parâmetros.
- Coleta a quantidade de alunos com notas:
  - **Maiores ou iguais a 6**
  - **Menores que 6**
- Gera um arquivo **CSV** contendo os seguintes dados:
  - **Matérias**
  - **Notas >= 6**
  - **Notas < 6**

---


## ⚙️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- **Python 3.8+**
- **Selenium** (para automação do navegador)
- **Google Chrome** e o [ChromeDriver](https://sites.google.com/chromium.org/driver/)

---

## 📥 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/auto_sige.git
   cd auto_sige
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o caminho do **ChromeDriver** no arquivo principal, caso necessário.

---

## 🖥️ Uso

1. Configure as informações no `main.py`:
   - Insira as turmas e parâmetros desejados.

2. Execute o script principal:
   ```bash
   python -m main.py
   ```

3. O script irá:
   - Navegar pelo sistema Sige.
   - Coletar as informações das turmas.
   - Salvar os dados no arquivo CSV.

4. O arquivo CSV será gerado no diretório atual.

---

## 📝 Exemplo de Saída (CSV)

| **Matéria**            | **Notas >= 6** | **Notas < 6** |
|-------------------------|----------------|----------------|
| LÍNGUA PORTUGUESA      | 15             | 5              |
| MATEMÁTICA             | 12             | 8              |
| GEOGRAFIA              | 14             | 6              |
| ...                    | ...            | ...            |

---

## 🚧 Limitações

- A estrutura do site **Sige** pode mudar, o que exigirá ajustes nos seletores utilizados no script.
- É necessário acesso ao sistema **Sige** com um usuário autorizado.
- O script funciona com o **Google Chrome**; para outros navegadores, ajustes no driver serão necessários.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se você encontrou algum problema ou tem sugestões de melhorias, sinta-se à vontade para abrir uma [issue](https://github.com/Turut4/auto_sige/issues) ou enviar um **pull request**.

---

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

**Autor:** [Lucas Turuta](https://github.com/Turut4)  
Sinta-se à vontade para entrar em contato ou contribuir! 😊
