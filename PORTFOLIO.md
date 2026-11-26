# Portfólio técnico de QA

**Demétrios Alves da Silva** · [Perfil](README.md) · [Experiência](docs/EXPERIENCIA.md) · [LinkedIn](https://www.linkedin.com/in/demetriosalvess)

Projetos pessoais de estudo e desenvolvimento, sem relação com sistemas ou entregas de clientes das empresas em que trabalhei. Todos usam dados fictícios. Cada repositório traz instruções de execução, evidências por cenário e um estudo de caso detalhado.

## Resultados documentados

| Projeto | Resultado registrado | Data |
| --- | --- | --- |
| [SauceDemo E2E](#saucedemo-e2e) | 20 cenários E2E aprovados | 16/11/2026 |
| [Cadastro Web](#cadastro-web) | 20 de 22 cenários aprovados; 2 defeitos do site documentados | 15/11/2026 |
| [Cadastro com Selenium](#cadastro-com-selenium) | Testes unitários aprovados no CI; E2E executado sob demanda | 16/11/2026 |
| [Fundamentos de Python](#fundamentos-de-python) | Execução e importação das 33 aulas verificadas | 16/11/2026 |
| [API Monitor](#api-monitor-privado) | 25 testes de backend e 43 cenários de interface aprovados | 16/11/2026 |

São execuções pontuais em ambientes diferentes, e não métricas contínuas de cobertura. Cenários ignorados não entram como aprovados.

## Automação de API

Testes REST contra a JSONPlaceholder: contrato JSON, CRUD simulado, filtros e cenários negativos, com cliente HTTP isolado, fixtures, parametrização e testes unitários do roteamento. Roda no GitHub Actions a cada push.

[Repositório](https://github.com/Demetrios10/Automa-o-API)

## SauceDemo E2E

Jornada de compra completa: login por botão e Enter, credenciais inválidas, usuário bloqueado, logout, compras de 1 a 5 produtos, campos obrigatórios, cancelamento do checkout e remoção de itens.

- **Decisões:** contexto isolado por cenário, seletores `data-test` e comparação de valores com `Decimal`, em centavos
- **Achado:** imprecisão de ponto flutuante no subtotal exibido pelo site, [documentada](https://github.com/Demetrios10/saucedemo-playwright-python/blob/main/docs/ANOMALIAS.md)

[Repositório](https://github.com/Demetrios10/saucedemo-playwright-python) · [Evidências](https://github.com/Demetrios10/saucedemo-playwright-python/tree/main/evidencias/revisao-2026-11-14)

## Cadastro Web

Formulário completo com Page Object Model: dados pessoais, gênero, hobbies, idiomas, país com busca, data de nascimento, senhas, upload de foto e validações negativas. O envio só conta como sucesso se a navegação real acontecer; nenhum resultado é simulado.

- **Achados:** o campo obrigatório *Country* não oferece opções, o que bloqueia o cadastro, e a prévia da foto não é atualizada. Os dois [defeitos](https://github.com/Demetrios10/automation-demo-playwright-python/blob/main/docs/DEFEITOS.md) foram registrados com evidências.

[Repositório](https://github.com/Demetrios10/automation-demo-playwright-python) · [Evidências](https://github.com/Demetrios10/automation-demo-playwright-python/tree/main/evidencias/validacao-inicial)

## Cadastro com Selenium

Page Object com esperas explícitas, sessão de Chrome própria por cenário e evidências estruturadas de resultados, falhas e cenários ignorados. Os testes unitários do Page Object rodam no CI; os 11 cenários E2E rodam sob demanda, porque dependem do Chrome e de um site externo.

[Repositório](https://github.com/Demetrios10/Automacao-Selenium-Python) · [Evidências](https://github.com/Demetrios10/Automacao-Selenium-Python/tree/main/evidencias/revisao-2026-11-12)

## Fundamentos de Python

Trilha de 33 aulas em seis temas, com funções `main()`, tratamento de entradas e testes que verificam a execução e a importação de cada aula, testados em Python 3.12 e 3.14.

[Repositório](https://github.com/Demetrios10/Fundamentos-Python) · [Índice das aulas](https://github.com/Demetrios10/Fundamentos-Python/blob/main/curso_python/README.md)

## API Monitor (privado)

Aplicação para monitorar APIs, feita com FastAPI, SQLite e Jinja2: monitores HTTP/JSON, histórico, incidentes, alertas por e-mail e Telegram, importação e exportação, backups e gestão de acesso. Uma suíte separada em Playwright cobre autenticação, recuperação de senha, monitores, operações e layout responsivo de 320 a 1440 px. Cada cenário usa uma instância descartável da aplicação.

- **Limites:** as APIs monitoradas e os envios de mensagens são simulados no ambiente de teste; não há validação de produção, carga ou Firefox/WebKit.
- **Acesso:** código e evidências são privados; este resumo não expõe dados, credenciais ou capturas operacionais.
