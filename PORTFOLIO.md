# Portfólio técnico de QA

**Demétrios Alves da Silva · Python, testes e automação**

[Perfil](README.md) · [Experiência e formação](docs/EXPERIENCIA.md) · [LinkedIn](https://www.linkedin.com/in/demetriosalvess)

Projetos pessoais de estudo e desenvolvimento. Os casos abaixo não representam sistemas ou entregas dos clientes das empresas em que trabalhei.

## Resultados documentados

| Projeto | Último registro consultado | Resultado | Evidência |
| --- | --- | --- | --- |
| SauceDemo · Playwright | 14/11/2026 | 20 cenários E2E aprovados; 35 capturas | [Relatório público](https://github.com/Demetrios10/saucedemo-playwright-python/blob/main/evidencias/RELATORIO.md) |
| Cadastro · Selenium | 12/11/2026 | 12 testes sem navegador aprovados; 11 cenários externos ignorados | [Relatório público](https://github.com/Demetrios10/Automacao-Selenium-Python/blob/main/evidencias/REVISAO-2026-11-12.md) |
| Fundamentos de Python | 07/11/2026 | 9 testes aprovados, incluindo execução e importação das 33 aulas | [Relatório público](https://github.com/Demetrios10/Fundamentos-Python/blob/main/evidencias/RELATORIO.md) |
| API Monitor · backend | 12/11/2026 | 25 testes aprovados | Repositório privado |
| API Monitor · Playwright | 12/11/2026 | 43 cenários de interface aprovados; 43 capturas | Repositório privado |

São execuções locais sob condições diferentes, não indicadores contínuos de CI ou percentuais de cobertura. Cenários ignorados não são contados como aprovados.

## SauceDemo · Playwright

**Objetivo:** verificar o caminho de compra de um e-commerce demonstrativo, incluindo autenticação e comportamento do carrinho.

**Implementação:** Python, pytest e Playwright com páginas de login, catálogo, carrinho, informações de checkout, resumo e confirmação. Um componente de produto compartilha a leitura de nomes, quantidades e preços entre telas.

**Cobertura:** login por botão e Enter; credenciais inválidas e campos ausentes; usuário bloqueado; logout; compras finalizadas de 1, 2, 3, 4 e 5 produtos; campos obrigatórios; cancelamento do checkout; remoção de item e retorno ao catálogo.

**Decisões:** contexto independente por cenário, seletores data-test, comparação monetária com Decimal e capturas do carrinho, resumo e confirmação.

**Limites e observações:** ambiente externo de demonstração, sem cobrança ou entrega real. Uma imprecisão do subtotal exibido pelo site foi documentada; as verificações monetárias usam centavos. Isso não corrige a formatação da interface.

[Repositório](https://github.com/Demetrios10/saucedemo-playwright-python) · [Evidências por cenário](https://github.com/Demetrios10/saucedemo-playwright-python/tree/main/evidencias/revisao-2026-11-14) · [Anomalia documentada](https://github.com/Demetrios10/saucedemo-playwright-python/blob/main/docs/ANOMALIAS.md)

## Cadastro · Selenium

**Objetivo:** transformar interações com um formulário em cenários legíveis e verificáveis.

**Implementação:** Page Object para campos e ações, gerenciador da sessão Chrome e testes separados. O fluxo usa dados fictícios, sem enviar cadastro ao servidor.

**Decisões:** esperas explícitas, sessão própria por cenário, encerramento do navegador e evidências estruturadas para resultados, falhas e cenários ignorados.

**Limite:** a revisão mais recente executou os testes sem navegador e ignorou os cenários externos. Tentativas anteriores falharam ao iniciar o Chrome; não há comprovação de aprovação E2E desse formulário.

[Repositório](https://github.com/Demetrios10/Automacao-Selenium-Python) · [Evidências por cenário](https://github.com/Demetrios10/Automacao-Selenium-Python/tree/main/evidencias/revisao-2026-11-12)

## Fundamentos de Python

**Objetivo:** manter uma trilha de exercícios que permita execução, revisão e importação independente.

**Implementação:** aulas organizadas por assunto, funções main(), tratamento de entradas e verificações automatizadas.

**Decisões:** exemplos pequenos, importações sem impressão ou leitura de dados e comparação de resultados conhecidos.

**Limite:** as verificações usam entradas de exemplo e não cobrem todas as combinações possíveis.

[Repositório](https://github.com/Demetrios10/Fundamentos-Python) · [Índice das aulas](https://github.com/Demetrios10/Fundamentos-Python/blob/main/curso_python/README.md)

## API Monitor e Playwright

**Objetivo:** acompanhar APIs e verificar fluxos críticos do painel sem alterar os dados da instalação de uso diário.

**Aplicação:** projeto pessoal com FastAPI, SQLite, Jinja2 e interface responsiva. Inclui monitores HTTP/JSON, histórico, incidentes, alertas, importação/exportação, backups e gestão de acesso.

**Automação:** suíte separada com pytest, Playwright, páginas por responsabilidade e componente de linha de monitor. Cada cenário usa aplicação local, banco e credenciais descartáveis. Testes de API são mantidos no backend, sem impor POM a serviços.

**Cobertura de interface:** autenticação, troca e recuperação de senha, monitores, incidentes, operações e larguras de 320, 390, 768 e 1440 pixels.

**Limites:** APIs monitoradas e envios de e-mail/Telegram são controlados pelo ambiente de teste. Os resultados não comprovam entrega real de mensagens, funcionamento em produção, carga ou execução em Firefox/WebKit.

**Acesso:** código e evidências completos permanecem privados. Este resumo não disponibiliza bancos, credenciais, capturas operacionais ou dados de usuários.

Revisão documental: 14/11/2026, com base nos relatórios indicados. Não houve nova execução de testes apenas para atualizar esta página.
