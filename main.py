from dotenv import load_dotenv
load_dotenv()
from crewai import Agent, Task, Crew

code_writer = Agent(
    role="Code Writer",
    goal="Gerar código Python funcional a partir de uma descrição",
    backstory="Você é um programador experiente, capaz de transformar requisitos em código Python limpo e eficiente.",
    verbose=True
)

code_reviewer = Agent(
    role="Code Reviewer",
    goal="Avaliar código Python e sugerir melhorias",
    backstory="Você é especialista em boas práticas de Python, PEP8 e qualidade de código.",
    verbose=True
)

bug_finder = Agent(
    role="Bug Finder",
    goal="Identificar falhas e bugs comuns em código Python",
    backstory="Você é um analista focado em identificar erros e pontos falhos no código Python.",
    verbose=True
)

refactor_agent = Agent(
    role="Refactor Expert",
    goal="Reescrever o código corrigido e limpo",
    backstory="Você é um engenheiro que reestrutura código para torná-lo mais limpo, performático e seguro.",
    verbose=True
)

# Tarefas em sequência: cada agente recebe o output do anterior

task_writer = Task(
    description="Crie uma função Python que some dois números e imprima o resultado.",
    expected_output="Código Python funcional gerado.",
    agent=code_writer
)

task_reviewer = Task(
    description="Revise o código gerado pelo Code Writer, sugira melhorias e explique as mudanças.",
    expected_output="Código revisado e sugestões de melhoria.",
    agent=code_reviewer
)

task_bug_finder = Task(
    description="Analise o código revisado e identifique possíveis bugs ou falhas.",
    expected_output="Relatório de bugs encontrados no código.",
    agent=bug_finder
)

task_refactor = Task(
    description="Refatore o código corrigido, tornando-o mais limpo, performático e seguro.",
    expected_output="Código final refatorado e explicação das melhorias.",
    agent=refactor_agent
)

crew = Crew(
    tasks=[task_writer, task_reviewer, task_bug_finder, task_refactor],
    agents=[code_writer, code_reviewer, bug_finder, refactor_agent]
)
crew.kickoff() 