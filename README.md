# python-agents-crewai

Este projeto demonstra o uso do CrewAI para orquestrar múltiplos agentes autônomos que colaboram para criar, revisar, testar e refatorar código Python.

## Agentes
- **Code Writer:** Gera código Python funcional a partir de uma descrição.
- **Code Reviewer:** Avalia o código gerado, sugere melhorias e explica as mudanças.
- **Bug Finder:** Analisa o código revisado e identifica possíveis bugs ou falhas.
- **Refactor Expert:** Refatora o código corrigido, tornando-o mais limpo, performático e seguro, e explica as melhorias.

## Como usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/gct00/python-agents-crewai.git
   cd python-agents-crewai
   ```
2. Crie e ative um ambiente virtual com Python 3.11:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` com sua chave do OpenRouter:
   ```env
   OPENAI_API_KEY=sua_api_key_do_openrouter
   OPENAI_API_BASE=https://openrouter.ai/api/v1
   OPENAI_MODEL_NAME=mistralai/mistral-7b-instruct
   ```
5. Execute o script principal:
   ```bash
   python3 main.py
   ```

## Observações
- O arquivo `.env` está no `.gitignore` e não deve ser versionado.
- O projeto foi testado com CrewAI 0.19.0 e Python 3.11.
- Não envie a pasta `.venv` para o repositório.

## Licença
MIT 