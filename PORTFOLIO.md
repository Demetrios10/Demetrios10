# Portfólio técnico de QA

**Demétrios Alves da Silva · Python, testes e automação**

[Perfil](README.md) · [Experiência e formação](docs/EXPERIENCIA.md) · [LinkedIn](https://www.linkedin.com/in/demetriosalvess)

Projetos pessoais de estudo e desenvolvimento. Os casos abaixo não representam sistemas ou entregas dos clientes das empresas em que trabalhei.

## Resultados documentados

| Projeto | Último registro consultado | Resultado | Evidência |
| --- | --- | --- | --- |
| Cadastro completo · Playwright | 15/11/2026 | 22 cenários: 20 aprovados e duas falhas do site; 23 capturas | [Relatório público](https://github.com/Demetrios10/automation-demo-playwright-python/blob/main/docs/RESULTADOS.md) |
| SauceDemo · Playwright | 16/11/2026 | 20 cenários E2E aprovados | [Revisão pública](https://github.com/Demetrios10/saucedemo-playwright-python/blob/main/evidencias/REVISAO-2026-11-16.md) |
| Cadastro · Selenium | 16/11/2026 | 12 testes sem navegador aprovados; os 11 E2E tiveram erros ao iniciar o Chrome | [Revisão pública](https://github.com/Demetrios10/Automacao-Selenium-Python/blob/main/evidencias/REVISAO-2026-11-16.md) |
| Fundamentos de Python | 16/11/2026 | 9 testes aprovados, com execução e importação das 33 aulas | [Revisão pública](https://github.com/Demetrios10/Fundamentos-Python/blob/main/evidencias/REVISAO-2026-11-16.md) |
| API Monitor · backend | 16/11/2026 | 25 testes aprovados | Repositório privado |
| API Monitor · Playwright | 16/11/2026 | 43 cenários de interface e um teste do coletor aprovados | Repositório privado |

São execuções locais sob condições diferentes, não indicadores contínuos de CI ou percentuais de cobertura. Cenários ignorados não são contados como aprovados.

## Cadastro completo · Playwright

**Objetivo:** automatizar o formulário de cadastro com dados fictícios, Page Object Model e evidências por cenário.

**Implementação:** Python, pytest e Playwright; dados pessoais, gêneros, hobbies, idiomas, habilidade, país com busca, nascimento, senhas, foto e validações negativas. O fluxo de envio está implementado e aguarda navegação real; não há simulação de sucesso.

**Resultado e limites:** 20 dos 22 cenários passaram. O campo Country obrigatório não oferece opções e bloqueia o cadastro completo. A seleção do arquivo funciona, mas a prévia da foto não muda. As duas falhas e as capturas foram preservadas; não há comprovação de cadastro finalizado.

[Repositório](https://github.com/Demetrios10/automation-demo-playwright-python) · [Evidências](https://github.com/Demetrios10/automation-demo-playwright-python/tree/main/evidencias/validacao-inicial) · [Problemas encontrados](https://github.com/Demetrios10/automation-demo-playwright-python/blob/main/docs/DEFEITOS.md)

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

**Limite:** a revisão executou os testes sem navegador e tentou os 11 cenários externos. Todos os E2E apresentaram erro ao iniciar o Chrome; não há comprovação de aprovação E2E desse formulário.

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

Revisão: 16/11/2026. Os projetos indicados foram executados novamente, exceto o cadastro Playwright, cujo resultado de 15/11 foi preservado. Veja a [revisão geral do GitHub](docs/REVISAO-GITHUB.md).
