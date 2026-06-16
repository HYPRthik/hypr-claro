# Dashboard Claro × HYPR — Contexto para Claude Code

## Visão geral do projeto

Dashboard HTML single-file para o cliente **Claro**, compilando resultados de campanhas rodadas pela HYPR entre 2025 e 2026. O arquivo é auto-contido (sem backend), com todos os dados embutidos em JavaScript e a maioria dos assets em base64 dentro do próprio HTML.

**Arquivo principal:** `Dashboard_Claro_v2.html` — esta é a única versão de referência. Ignorar qualquer v1.

**Assets externos referenciados (devem estar na mesma pasta do HTML):**
- `claro-map-bg.gif` — background do mapa interativo
- `hypr-brand--branco (1).png` — logo HYPR branca
- `Claro-logo.png` — logo Claro oficial
- `claro_asset_background.gif` — asset de vídeo/GIF de background do hero (ainda será enviado)

**Base de dados:** `FINAL_Base_Consolidada_Claro_v1.xlsx` — planilha com métricas reais; todos os números devem ser extraídos exclusivamente dela.

---

## Identidade visual

- Fundo: `#080810` / `#0c0c16` (dark navy quase preto)
- Cor principal: `#DA291C` (vermelho Claro)
- Fontes: DM Sans (corpo), Space Mono (labels/códigos), Urbanist (títulos/números grandes)
- Estilo: glassmorphism + dark mode; cards com `backdrop-filter: blur`
- Nunca usar amarelo/gold (`#E8B23A`) como destaque de métricas-chave — trocar por vermelho Claro

---

## Estrutura do arquivo HTML

O HTML é uma SPA (Single Page Application) sem framework. A navegação é controlada por `go(id)` que alterna a classe `.active` entre as `div.view`.

**Seções (views):**
1. `#hub` — Menu principal / hero
2. `#consolidado` — Consolidado Geral (renderizado por `buildConsolidado()`)
3. `#campanhas` — Campanhas Ativadas (renderizado por `buildCampanhasHub()` e `buildFlightDetail(code)`)
4. `#materiais` — Hub de Materiais (renderizado por `buildMateriais()`)
5. `#brandlift` — Brand-Lift / Surveys (renderizado por `buildBrandlift()` + `renderBLChart()`)
6. `#criativos` — Central de Criativos (renderizado por `buildCriativos()` + `renderCreativeGrid()`)

Todo o conteúdo das seções 2–6 é injetado via `innerHTML` no `DOMContentLoaded` equivalente no final do script.

---

## REGRAS CRÍTICAS

1. **Nunca usar dados fictícios.** Se um dado não estiver presente na base, pergunte antes de inventar.
2. **Nunca misturar dados de clientes diferentes.**
3. **Nenhum disclaimer, nota de inconsistência ou aviso deve aparecer no arquivo final** — tudo que questione a veracidade dos números deve ser removido. O cliente vê os dados como corretos e validados.
4. **Total investido obrigatório: R$ 820.191** — qualquer linha de total deve refletir esse valor.
5. **Nomenclaturas oficiais:** Tap-to-Go (nunca Tap-to-Map), Survey (nunca "onda"), Display (imagens estáticas), Vídeo (assets em vídeo).

---

## Lista completa de modificações

### 1. Menu Principal (`#hub`)

- [ ] Inserir logo HYPR (`hypr-brand--branco (1).png`) ao lado da logo Claro no topo — ambas na topbar
- [ ] Substituir a logo Claro no stage central pela imagem `Claro-logo.png` (em arquivo, não base64)
- [ ] Texto `"CLARO × HYPR · 2025 – 2026"` deve ficar em **branco**, fonte **Montserrat**
- [ ] As imagens flutuantes (`.float`) devem orbitar ao redor da logo central da Claro (animação de rotação orbital, não apenas bob)
- [ ] A logo central da Claro deve ser maior (aumentar `.stage-logo img` de `height:50px` para ~80-90px)
- [ ] Remover o texto `"× HYPR"` que aparece abaixo da logo central (`.stage-logo .x`)
- [ ] **Big numbers — ajustes nos boxes:**
  - Box "9 campanhas": remover o sub "6 campanhas · 9 flights" → deixar apenas o número e label limpo
  - Box "Features ativadas": remover "7 tipos" do subtexto
  - Box "R$ 820 mil": remover "Budget contratado" do subtexto
  - Box "Cliques": remover a referência a cliques de vídeo do subtexto → mostrar apenas cliques display
  - Box "Criativos veiculados": deixar apenas "+149 criativos veiculados" como label, sem subtexto adicional
- [ ] **Background animado no hero:** Entre o fim do cabeçalho (`.topbar`) e o início da seção "Explorar" (`.navsec`), adicionar o `claro_asset_background.gif` como background em loop. Configurar com:
  - `opacity` baixa (sugerido: 0.12–0.18) para não poluir
  - `mix-blend-mode: screen` ou similar para integrar ao tema escuro
  - `object-fit: cover`, posicionado absolutamente atrás do conteúdo
  - Não prejudicar legibilidade dos big numbers nem do stage
- [ ] **Alinhar os dois boxes da segunda fileira centralizados** em relação à primeira fileira de 3 (quando em grid de 5 boxes em 2 fileiras)

---

### 2. Consolidado Geral (`buildConsolidado()`)

- [ ] Alterar subtítulo da seção: trocar `"Todos os números do portfólio Claro × HYPR. Métricas de entrega, investimento e performance somadas das 6 campanhas / 9 flights. Vídeo entregue apenas na campanha iPhone 17."` por: **`"Principais métricas da entrega HYPR ao longo da nossa jornada."`**
- [ ] Remover os badges `<span class="kc-badge">chave</span>` de todas as métricas — o destaque por cor já é suficiente
- [ ] Mudar a cor de destaque das métricas `imp` de `var(--ac2)` (amarelo/gold) para `var(--ac-l)` (vermelho Claro `#FF4332`)
- [ ] Separar visualmente as métricas de **display** e **vídeo** — criar dois grupos distintos dentro do kgrid ou dois kgrids separados com títulos
- [ ] Renomear `"Views Completos de vídeo"` → **`"Views 100% em vídeo"`**
- [ ] Renomear `"Cliques Totais"` → **`"Cliques"`**
- [ ] Renomear `"CTR médio (display)"` e remover `"ponderado pelo portfólio"` do subtexto → apenas **`"CTR"`**
- [ ] Renomear `"Investido pelo cliente"` → **`"Total investido"`**; remover `"Budget contratado total"` do subtexto
- [ ] Renomear `"CPC médio"` → **`"CPC"`**
- [ ] Renomear `"VTR (vídeo)"` → **`"VTR"`**
- [ ] Adicionar métrica de **rentabilidade do CPCV** na seção de vídeo (além da rentabilidade CPM existente)
- [ ] **Desempenho por Flight — substituir tabela por linha do tempo interativa:**
  - Linha do tempo horizontal desde o início da parceria HYPR × Claro
  - Cada flight = uma bolinha na linha
  - Hover na bolinha: card flutuante com budget, impressões, cliques e CTR + botão "Ver detalhes"
  - "Ver detalhes": expande um painel inline (na mesma página) com todas as demais métricas, features ativadas e preview de criativos daquele flight
  - Para campanhas com brand-lift: adicionar botão que navega para a onda correspondente na seção Brand-Lift
  - Para iPhone 17: incluir informações de vídeo no card de detalhes
  - Usar o estilo visual dos campboxes da seção Campanhas Ativadas como inspiração
  - A tabela completa pode ser removida; se mantida, a linha TOTAL deve mostrar obrigatoriamente **R$ 820.191**
- [ ] **Features ativadas — substituir tabela por cards:**
  - Um card por feature (não por ativação), consolidando todas as campanhas em que foi usada
  - Cada card: ícone da feature (imagens oficiais serão fornecidas), campanhas em que foi ativada, métricas consolidadas
  - Para Tap-to-Go: incluir preview do criativo quando aplicável
  - Usar sempre a nomenclatura **Tap-to-Go** (nunca Tap-to-Map)
- [ ] Remover completamente a seção `buildInconsistencias()` e sua chamada
- [ ] Remover completamente o rodapé `"Fonte: FINAL_Base_Consolidada_Claro_v1.xlsx · abas..."`

---

### 3. Campanhas Ativadas (`buildCampanhasHub()` / `buildFlightDetail()`)

- [ ] Adicionar filtro por **vertical** (ex: Telecom, B2B, etc.) na grade de campanhas
- [ ] Adicionar filtro por **mês de início da veiculação**
- [ ] **No detalhe de cada campanha (`buildFlightDetail`):**
  - Remover os avisos de vídeo sem entrega (ex: `"O formato vídeo foi ativado neste flight, mas não houve entrega"`) para as campanhas 6A0X7X, NW0LUN e 3GGX7R
  - Remover o disclaimer de dados preliminares da Web Summit (3GGX7R)
  - Na seção de features: usar ícones oficiais (serão fornecidos) e remover o texto `"resultados reais desta campanha"`
  - Na seção de criativos: usar apenas rótulo **`"Display"`** para imagens estáticas e **`"Vídeo"`** para vídeos (remover `"IMG"`, `"INTERATIVO"`, etc.)

---

### 4. Hub de Materiais (`buildMateriais()`)

- [ ] **Refazer completamente a seção.** O objetivo é um hub de acesso a materiais de Pós-vendas, Estudos e Audience Discovery — não um descritivo de bases de dados
- [ ] Os materiais estão organizados nesta pasta do Google Drive: `https://drive.google.com/drive/folders/1wg4SnRKzlq-ptXMqWX1MSq63gl55wrZo?usp=sharing`
- [ ] Criar cards por categoria: **Pós-vendas**, **Estudos**, **Audience Discovery** — cada card abrindo o link correspondente no Drive
- [ ] Remover o rodapé `"Materiais Claro × HYPR · fontes de verdade do consolidado"`
- [ ] **Perguntar ao usuário** a estrutura exata de pastas/arquivos dentro do Drive antes de implementar os cards, para garantir que os links sejam corretos

---

### 5. Brand-Lift (`buildBrandlift()`)

- [ ] Substituir o termo **"onda"** por **"Survey"** em toda a seção (labels de pills, títulos de cards, etc.)
- [ ] Adicionar filtro por **tipo de Survey**: "Awareness" e "Intenção" — a única survey de intenção é Atendimento Digital (Dez/25)
- [ ] Aumentar espaçamento entre a nota de metodologia e os cards acima (`.note` colada nos `.bl-cards`)
- [ ] Melhorar a exibição dos números de resposta (n exposto / controle) — atualmente em texto pequeno `.blc-n`; tornar mais legível e visualmente destacado

---

### 6. Central de Criativos (`buildCriativos()`)

- [ ] Adicionar disclaimer no topo da seção: `"Criativos enviados ao longo das campanhas podem não estar presentes na relação final."`
- [ ] Usar apenas rótulos **`"Display"`** para imagens estáticas e **`"Vídeo"`** para assets em vídeo (remover `"IMG"`, `"INTERATIVO"`, `"RICH MEDIA"`, etc.)
- [ ] Para campanhas com diferentes linhas criativas rotuladas (ex: Atendimento Digital): criar um label identificador por linha criativa (não precisa ser filtro, apenas rótulo visual no card)
- [ ] Adicionar filtro **"Apenas criativos de Features"** — para exibir somente criativos relacionados a features como Tap-to-Go

---

## Perguntas pendentes antes de implementar

1. **Hub de Materiais:** Quais são as pastas/subpastas e seus nomes exatos dentro do Google Drive linkado? Precisamos dos links diretos por categoria para criar os cards corretamente.
2. **Ícones de features:** As imagens oficiais de cada feature ainda serão enviadas — aguardar antes de implementar os cards de features no Consolidado e no detalhe de campanhas.
3. **claro_asset_background.gif:** Ainda será enviado — implementar o background do hero como placeholder (comentário no HTML) e finalizar quando o asset chegar.
4. **Logo Claro no stage:** Confirmar se a logo deve aparecer apenas como `<img src="Claro-logo.png">` (arquivo externo) ou deve ser re-embutida em base64 como as demais logos.
5. **Linha do tempo — datas exatas:** Confirmar as datas de início de cada flight para posicionar corretamente os pontos na linha do tempo. Estão na base xlsx?

---

## Observações técnicas

- O arquivo usa **Chart.js 4.4.1** via CDN para os gráficos de brand-lift
- Todas as imagens de criativos estão embutidas em base64 no objeto `DATA.creatives` — não há arquivos de imagem externos para os criativos
- O objeto `DATA` contém: `DATA.flights`, `DATA.totals`, `DATA.features`, `DATA.creatives`, `DATA.brandlift`
- A navegação entre seções usa `go(id)` — ao voltar para campanhas, `buildCampanhasHub()` é reconstruído
- Filtros de criativos usam estado global `cvFilter` — manter esse padrão para novos filtros
- Ao adicionar Montserrat no menu principal, incluir no `<link>` do Google Fonts
