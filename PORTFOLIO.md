# Portfólio técnico de QA

**Demétrios Alves da Silva · Python, testes e automação**

[Perfil](README.md) · [Experiência](docs/EXPERIENCIA.md) · [LinkedIn](https://www.linkedin.com/in/demetriosalvess)

Projetos pessoais de estudo e desenvolvimento. As experiências profissionais estão descritas separadamente; os casos abaixo não representam sistemas ou entregas de clientes.

## Roteiro de avaliação

| Interesse | Projeto | Acesso |
|---|---|---|
| Organização de uma automação web | [Selenium](https://github.com/Demetrios10/Automacao-Selenium-Python/blob/main/docs/PORTFOLIO.md) | Público |
| Fundamentos de programação e validação | [Python](https://github.com/Demetrios10/Fundamentos-Python/blob/main/docs/PORTFOLIO.md) | Público |
| Aplicação de monitoramento e testes com Playwright | [Resumo técnico](#api-monitor-e-playwright) | Resumo público; código privado |

## Automação web com Selenium

**Problema:** transformar a interação manual com um formulário em cenários legíveis e verificáveis.

**Solução:** separar os seletores e ações no Page Object, a criação do Chrome em um gerenciador de sessão e as asserções em testes. O fluxo usa dados fictícios e não envia cadastro ao servidor.

**Decisões técnicas:** esperas explícitas para sincronização; sessão própria por cenário; encerramento do navegador ao terminar; registros de erro e capturas quando o navegador permite.

**Evidência:** oito unitários aprovados no relatório de 07/11/2026. Onze cenários E2E definidos; a tentativa documentada falhou ao iniciar o Chrome. Esses cenários não são apresentados como aprovados.

[Estudo de caso e arquivos para revisão](https://github.com/Demetrios10/Automacao-Selenium-Python/blob/main/docs/PORTFOLIO.md)

## Fundamentos de Python

**Problema:** organizar exercícios de programação para permitir estudo, execução e revisão sem depender da ordem de importação.

**Solução:** 33 aulas em seis temas, com entrada pelo terminal e organização da execução em funções `main()`.

**Decisões técnicas:** preservar exemplos pequenos; validar entradas com maior risco de erro; evitar impressão e leitura ao importar os módulos; conferir resultados conhecidos e execução com entradas de exemplo.

**Evidência:** nove testes aprovados no relatório de 07/11/2026, incluindo verificações que percorrem as 33 aulas. Não representa cobertura de todas as entradas.

[Estudo de caso e trilha](https://github.com/Demetrios10/Fundamentos-Python/blob/main/docs/PORTFOLIO.md)

## API Monitor e Playwright

**Problema:** acompanhar o comportamento de APIs e verificar os fluxos críticos do painel sem alterar os dados da instalação de uso diário.

**Aplicação:** projeto pessoal com FastAPI, SQLite e interface responsiva. Reúne cadastro de monitores, verificações HTTP/JSON, histórico, incidentes, fila de alertas, importação/exportação, backups e gestão de acesso.

**Automação:** projeto Python separado, com pytest, Playwright e Page Objects. Cada teste inicia uma aplicação local e usa banco, chave e administrador descartáveis. As APIs monitoradas e os envios de e-mail/Telegram recebem respostas controladas.

**Resultado registrado:** 43 testes aprovados, sem falhas ou casos ignorados, no Chromium headless em Windows. A execução verificou autenticação, troca e recuperação de senha, monitores, incidentes, operações e telas de 320, 390, 768 e 1440 pixels.

**Limites:** esse resultado não comprova entrega real de mensagens, serviços externos, produção, carga, Firefox ou WebKit. O workflow manual de GitHub Actions foi preparado e ainda depende da configuração de acesso e da primeira execução na nuvem.

**Acesso:** o aplicativo e a suíte permanecem privados. O resumo acima apresenta o trabalho sem publicar código, banco, credenciais, capturas operacionais ou dados de usuários. Para conversar sobre o projeto, entre em contato pelo [LinkedIn](https://www.linkedin.com/in/demetriosalvess).

## Como interpretar os resultados

| Projeto | Registro disponível | Limite principal |
|---|---|---|
| Fundamentos de Python | 9 testes aprovados; verificações das 33 aulas | Entradas de exemplo, não todas as combinações |
| Selenium | 8 unitários aprovados; 11 E2E definidos | Navegador não iniciou na tentativa registrada |
| API Monitor + Playwright | 43 aprovados no Chromium isolado | Integrações externas controladas; CI não executada |

Os números correspondem a suítes e condições diferentes. Não são somados como uma taxa única de qualidade ou cobertura. A revisão deste portfólio foi documental; as execuções originais estão identificadas nas evidências dos projetos.

Revisão: 09/11/2026.
