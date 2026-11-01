# 🛡️ DIO Agent Safe — Especialização em Cibersegurança & AppSec

Evolução do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) transformando-o em um **Mentor de Cibersegurança Defensiva e Especialista em AppSec**. Sem realizar fine-tuning de modelos, o agente foi especializado exclusivamente por meio de Engenharia de Contexto (arquivos de conhecimento, *skills* estruturadas e ajustes de *persona*).

Neste projeto, em vez do *Hermes*, foi utilizado o **Antigravity CLI (`agy`)** com o modelo **Gemini 3.8 Flash** como *harness* de execução no terminal.

---

## 🎯 A Especialização e o Porquê

O objetivo desta evolução é fazer com que o agente deixe de dar respostas genéricas ou imediatistas e passe a agir como um profissional de segurança sênior e mentor:
1. **Abordagem Consultiva e Investigativa:** Antes de sugerir comandos ou alterações em cenários de infraestrutura, o agente levanta o contexto, mapeia a superfície de ataque (*attack surface*) e entende o ambiente (laboratório vs. produção).
2. **Análise Estruturada de Vulnerabilidades (AppSec):** Na revisão de código, o agente identifica falhas críticas, mapeia referências padrão de mercado (**CWE**, **MITRE ATT&CK**, **CAPEC** e **OWASP Top 10**), explica o mecanismo teórico de exploração e aplica **Defesa em Profundidade** na refatoração.
3. **Didática Defensiva:** Orienta iniciantes explicando o *porquê* de cada verificação antes de qualquer execução.

---

## 📂 Arquivos Criados e Alterados

Abaixo estão as adições e modificações realizadas em relação ao repositório base:

### Criados
* **`skills/vulnerability-analysis/SKILL.md`**: Roteiro estruturado com diretrizes defensivas para o agente conduzir análises de vulnerabilidade, coletar contexto antes de agir e avaliar impacto, probabilidade e severidade.
* **`skills/vulnerability-analysis/README.md`**: Documentação voltada para humanos explicando o funcionamento, gatilhos e objetivos da skill de análise de vulnerabilidades.
* **`agent/knowledge/security-basics.md`**: Base de conhecimento contendo conceitos fundamentais de segurança da informação (Vulnerabilidade, Ameaça, Risco, Tríade CIA — Confidencialidade, Integridade e Disponibilidade — e boas práticas de *hardening* e codificação segura).
* **`agent/app.py`**: Aplicação em Python/SQLite criada inicialmente com vulnerabilidade de *SQL Injection* (CWE-89) e senhas em texto claro (CWE-256) para teste, posteriormente refatorada pelo agente com *Prepared Statements* e *PBKDF2 + Salt*.
* **`AI.txt`**: Registro completo do log de interações, raciocínio e saídas geradas pelo **Antigravity CLI (`agy`)** durante os testes de AppSec e mentoria de infraestrutura.

### Alterados
* **`agent/persona.md`**: Inclusão do comportamento de mentor de cibersegurança defensiva, priorizando perguntas de contexto, ética em testes (apenas ambientes autorizados/laboratório) e explicação clara de riscos.
* **`AGENTS.md`**: Adição da skill `vulnerability-analysis` na tabela de roteamento do agente para acionamento automático em demandas de segurança.

---

## 🌳 Estrutura do Projeto

```text
.
├── AGENTS.md
├── AI.txt
├── CLAUDE.md
├── README.md
├── agent
│   ├── app.py
│   ├── knowledge
│   │   ├── dio-platform.md
│   │   ├── learning-experiences.md
│   │   └── security-basics.md
│   └── persona.md
├── docs
│   ├── glossary.md
│   └── youcom-mcp.md
└── skills
    ├── README.md
    ├── ai-builder-path/
    ├── explain-concept/
    ├── portfolio-review/
    ├── study-plan/
    ├── system/
    ├── unblock-challenge/
    ├── vulnerability-analysis
    │   ├── README.md
    │   └── SKILL.md
    └── web-search/