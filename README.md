# python-linter-agents

Projeto para validar, corrigir e refatorar código Python usando CrewAI e modelos gratuitos via OpenRouter.

## Passos rápidos

1. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure o arquivo `.env` com sua chave do OpenRouter.
4. Rode o script principal:
   ```bash
   python main.py
   ```

## Dependências principais
- crewai
- openai
- crewai-tools
- black
- pylint
- bandit

## Exemplo de uso
O script `main.py` executa agentes que analisam, corrigem e explicam código Python automaticamente. 

OPENAI_API_KEY=REMOVIDO

## Como corrigir definitivamente:

### 1. **Remova o ambiente virtual antigo**
No terminal, dentro da pasta do projeto:
```bash
deactivate || true
rm -rf .venv
```

### 2. **Garanta que o pyenv está ativo**
Execute:
```bash
pyenv local 3.11.8
```

### 3. **Verifique o Python correto**
Execute:
```bash
which python3
python3 --version
```
O caminho deve ser algo como:
```
/Users/gcampion/.pyenv/versions/3.11.8/bin/python3
Python 3.11.8
```
Se não for, feche o terminal e abra um novo, ou rode:
```bash
exec "$SHELL"
```
E repita o passo acima.

### 4. **Crie o ambiente virtual com o Python 3.11.8**
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Depois de ativar, confira:
```bash
python --version
python3 --version
```
Ambos devem mostrar Python 3.11.8.

### 5. **Instale as dependências**
```bash
pip install --upgrade pip setuptools
pip install -r requirements.txt
```

### 6. **Execute o script**
```bash
python3 main.py
```

**Resumo:**  
O ambiente virtual precisa ser criado com o Python 3.11.8 do pyenv, não com o Python do sistema.  
Se seguir esses passos, vai funcionar!

Se ainda tiver dúvidas, envie a saída dos comandos:
```bash
which python3
python3 --version
ls -l .venv/bin/python*
```
Assim confirmo para você!