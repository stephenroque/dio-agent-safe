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
* **`AI.md`**: Registro completo do log de interações, raciocínio e saídas geradas pelo **Antigravity CLI (`agy`)** durante os testes de AppSec e mentoria de infraestrutura.

### Alterados
* **`agent/persona.md`**: Inclusão do comportamento de mentor de cibersegurança defensiva, priorizando perguntas de contexto, ética em testes (apenas ambientes autorizados/laboratório) e explicação clara de riscos.
* **`AGENTS.md`**: Adição da skill `vulnerability-analysis` na tabela de roteamento do agente para acionamento automático em demandas de segurança.

---

## 🌳 Estrutura do Projeto

```text
.
├── AGENTS.md
├── AI.md
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

```

---

## 🚀 Como Rodar o Agente (Antigravity CLI)

> **⚠️ Importante:** Sempre execute o comando na pasta raiz do projeto (`dio-agent-safe`) para que o agente localize corretamente o `AGENTS.md`, a `persona.md` e a pasta `skills/`.

1. **Clone o repositório e acesse a pasta:**
```bash
git clone [https://github.com/SEU-USUARIO/dio-agent-safe.git](https://github.com/SEU-USUARIO/dio-agent-safe.git)
cd dio-agent-safe

```


2. **Inicie o Antigravity CLI no terminal:**
```bash
agy

```


3. **(Opcional) Selecione o modelo desejado dentro do CLI:**
```text
/model

```



---

## 🛠️ Melhorias Implementadas e Resultados Obtidos

Além de seguir o fluxo proposto no desafio, foram implementadas as seguintes melhorias práticas (cujos logs completos podem ser consultados no arquivo **[`AI.md`](https://www.google.com/search?q=./AI.md)**):

### 1. Auditoria de AppSec com Mapeamento MITRE ATT&CK, CWE e OWASP (`agent/app.py`)

* **Identificação:** O agente analisou o código vulnerável e detectou não apenas o **SQL Injection (CWE-89)** na interpolação com `f-string`, mas também uma vulnerabilidade secundária de **Senhas em Texto Claro (CWE-256 / CWE-312)**.
* **Mapeamento:** Associou a falha à tática de *Initial Access* via técnica **MITRE ATT&CK T1190 (Exploit Public-Facing Application)** e **CAPEC-66**.
* **Hardening Completo:** Em vez de apenas parametrizar a query com `?`, o agente reescreveu o `agent/app.py` aplicando gerenciamento de contexto (`with sqlite3.connect(...)`), derivação de chave criptográfica com **PBKDF2-HMAC-SHA256 (100.000 iterações + Salt)** e comparação em tempo constante (`hmac.compare_digest`) contra *Timing Attacks*.
* **Validação:** Em uma segunda varredura, confirmou a mitigação da falha em conformidade com o **OWASP Top 10 (A03:2021 – Injection)**.

### 2. Mentoria Guiada em Cenário de Infraestrutura (Servidor Ubuntu Exposto)

Ao receber o relato *"Tenho um servidor Ubuntu exposto na internet. Não sei por onde começar"*, o agente acionou a skill `vulnerability-analysis` e:

* **Não executou nem sugeriu comandos às cegas:** Perguntou primeiro se o ambiente era de laboratório ou produção e quais serviços estavam instalados.
* **Guiou o raciocínio defensivo:** Após receber o contexto, estruturou a resposta em:
1. *O que já sabemos* (finalidade, exposição, gestão via SSH e estado atual);
2. *O que ainda precisamos descobrir* (portas abertas, blindagem do SSH e atualizações);
3. *As 3 primeiras verificações defensivas* (mapeamento de portas na rede, revisão do `/etc/ssh/sshd_config` e checagem de pacotes pendentes no Ubuntu), explicando o motivo de cada uma em linguagem acessível.



---

## 📸 Evidências e Logs de Execução

* 📄 **Log completo do terminal:** Confira o arquivo **[`AI.txt`](https://www.google.com/search?q=./AI.txt)** na raiz deste repositório com toda a transcrição da sessão no Antigravity CLI (`agy`).
