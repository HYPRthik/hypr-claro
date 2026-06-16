#!/usr/bin/env python3
"""
patch_dashboard.py — Applies all requested modifications to Dashboard_Claro_v3.html
"""

import json, sys

HTML_PATH = '/home/user/Geocoding-HYPR/Dashboard_Claro_v3.html'
GIF_JSON_PATH = '/root/.claude/projects/-home-user-Geocoding-HYPR/66817438-60c1-5f0a-a205-dfa463cfe6c5/tool-results/mcp-Google_Drive-download_file_content-1781607494005.txt'

print("Loading HTML...")
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

print("Loading GIF base64...")
with open(GIF_JSON_PATH, 'r', encoding='utf-8') as f:
    gif_data = json.load(f)
gif_b64 = gif_data['content']
print(f"GIF base64 length: {len(gif_b64)}")

def replace_once(src, old, new, label=""):
    if old not in src:
        print(f"  [WARN] NOT FOUND: {label or repr(old[:80])}")
        return src
    result = src.replace(old, new, 1)
    print(f"  [OK] {label or repr(old[:60])}")
    return result

# ── 1a. Montserrat font
html = replace_once(html,
    'family=Urbanist:wght@600;700;800;900&display=swap',
    'family=Urbanist:wght@600;700;800;900&family=Montserrat:wght@600;700&display=swap',
    '1a fonts link')

html = replace_once(html,
    ".hub-eyebrow{font-family:'Space Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:3px;\n  color:var(--ac-l);margin-bottom:18px;opacity:0;animation:rise .7s .1s forwards}",
    ".hub-eyebrow{font-family:'Montserrat',sans-serif;font-size:11px;text-transform:uppercase;letter-spacing:3px;\n  color:#fff;font-weight:600;margin-bottom:18px;opacity:0;animation:rise .7s .1s forwards}",
    '1a hub-eyebrow CSS')

# ── 1b. Remove × HYPR
html = replace_once(html,
    '\n        <span class="x">× HYPR</span>',
    '',
    '1b remove × HYPR')

# ── 1c. Logo height
html = replace_once(html,
    '.stage-logo img{height:50px;width:auto;',
    '.stage-logo img{height:88px;width:auto;',
    '1c logo height')

# ── 1d. GIF background
OLD_EYEBROW = '    <div class="hub-eyebrow">Claro × HYPR · 2025 – 2026</div>'
NEW_EYEBROW = f'''    <div class="hero-bg-gif" style="position:absolute;inset:0;z-index:0;overflow:hidden;pointer-events:none;">
      <img src="data:image/gif;base64,{gif_b64}" alt="" style="width:100%;height:100%;object-fit:cover;opacity:0.15;mix-blend-mode:screen;filter:saturate(1.2) hue-rotate(340deg);">
    </div>
    <div class="hub-eyebrow">Claro × HYPR · 2025 – 2026</div>'''
html = replace_once(html, OLD_EYEBROW, NEW_EYEBROW, '1d GIF background')

# ── 1e. Big numbers subtexts
html = replace_once(html,
    '<div class="bn-l">Campanhas ativadas</div>\n          <div class="bn-s">6 campanhas · 9 flights</div>',
    '<div class="bn-l">Campanhas ativadas</div>',
    '1e campanhas bn-s')

html = replace_once(html,
    '<div class="bn-l">Features ativadas</div>\n          <div class="bn-s">7 tipos · 11 ativações</div>',
    '<div class="bn-l">Features ativadas</div>',
    '1e features bn-s')

html = replace_once(html,
    '<div class="bn-l">Investido pelo cliente</div>\n          <div class="bn-s">Budget contratado</div>',
    '<div class="bn-l">Investido pelo cliente</div>',
    '1e investido bn-s')

html = replace_once(html,
    '<div class="bn-l">Cliques</div>\n          <div class="bn-s">873.183 display + 313 vídeo</div>',
    '<div class="bn-l">Cliques</div>',
    '1e cliques bn-s')

html = replace_once(html,
    '<div class="bn-l">Criativos veiculados</div>\n          <div class="bn-s">144 imagens · 4 vídeos · 1 interativo</div>',
    '<div class="bn-l">+149 criativos veiculados</div>',
    '1e criativos bn-s')

# ── 1f. bignums flex
html = replace_once(html,
    '.bignums{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;margin:14px auto 6px;max-width:var(--maxw)}',
    '.bignums{display:flex;flex-wrap:wrap;gap:12px;margin:14px auto 6px;max-width:var(--maxw);justify-content:center;}\n.bn{flex:0 0 calc(20% - 12px);min-width:160px;}',
    '1f bignums flex')

# ── 1g. Orbit animation
html = replace_once(html,
    '@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}',
    '@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}\n@keyframes orbit{\n  0%{transform:rotate(0deg) translateX(var(--r,160px)) rotate(0deg)}\n  100%{transform:rotate(360deg) translateX(var(--r,160px)) rotate(-360deg)}\n}',
    '1g orbit keyframes')

html = replace_once(html,
    'opacity:0; animation:floatIn .9s forwards, bob 7s ease-in-out infinite;',
    'opacity:0; animation:floatIn .9s forwards, orbit var(--dur,18s) linear infinite var(--delay,0s);',
    '1g float animation')

# ── 2a. Consolidado subtitle
html = replace_once(html,
    'Todos os números do portfólio Claro × HYPR. Métricas de entrega, investimento e performance somadas das 6 campanhas / 9 flights. Vídeo entregue apenas na campanha iPhone 17.',
    'Principais métricas da entrega HYPR ao longo da nossa jornada.',
    '2a subtitle')

# ── 2b. Remove kc-badge + fix color
html = replace_once(html,
    "${k.imp?'<span class=\"kc-badge\">chave</span>':''}</div>",
    '</div>',
    '2b remove kc-badge')

html = replace_once(html,
    '.kcard.imp .kc-v{color:var(--ac2)}',
    '.kcard.imp .kc-v{color:var(--ac-l)}',
    '2b imp color')

# ── 2c. Rename metrics
html = replace_once(html,
    '{l:"Views completos de vídeo",v:fmtInt(t.v_views),s:"iPhone 17 (único com vídeo)"}',
    '{l:"Views 100% em vídeo",v:fmtInt(t.v_views),s:"iPhone 17 (único com vídeo)",video:true}',
    '2c views rename')

html = replace_once(html,
    '{l:"Cliques totais",v:fmtInt(t.clicks+t.v_clicks),s:fmtInt(t.clicks)+" display · "+t.v_clicks+" vídeo",imp:1}',
    '{l:"Cliques",v:fmtInt(t.clicks+t.v_clicks),s:"",imp:1,video:false}',
    '2c cliques rename')

html = replace_once(html,
    '{l:"CTR médio (display)",v:fmtPct(t.ctr),s:"ponderado pelo portfólio"}',
    '{l:"CTR",v:fmtPct(t.ctr),s:"",video:false}',
    '2c CTR rename')

html = replace_once(html,
    '{l:"Investido pelo cliente",v:fmtBRL0(t.investido_cliente),s:"Budget contratado total",imp:1}',
    '{l:"Total investido",v:fmtBRL0(t.investido_cliente),s:"",imp:1,video:false}',
    '2c investido rename')

html = replace_once(html,
    '{l:"CPC médio",v:fmtBRL(t.cpc),s:"custo por clique (display)"}',
    '{l:"CPC",v:fmtBRL(t.cpc),s:"",video:false}',
    '2c CPC rename')

html = replace_once(html,
    '{l:"VTR (vídeo)",v:fmtPct(t.v_vtr),s:"view-through rate · iPhone 17"}',
    '{l:"VTR",v:fmtPct(t.v_vtr),s:"view-through rate · iPhone 17",video:true}',
    '2c VTR rename')

html = replace_once(html,
    '{l:"Impressões visíveis entregues",v:fmtInt(t.impr),s:"Display · "+F.length+" flights",imp:1}',
    '{l:"Impressões visíveis entregues",v:fmtInt(t.impr),s:"Display · "+F.length+" flights",imp:1,video:false}',
    '2c impr mark display')

# ── 2d. Split kpis display/video - replace kg generation block
kg_search = '  let kg = kpis.map(k=>`<div class="kcard ${k.imp?\'imp\':\'\'}">\n    <div class="kc-l">${k.l} '
kg_end_str = '.join("");'
kg_idx = html.find(kg_search)
if kg_idx >= 0:
    kg_end_idx = html.find(kg_end_str, kg_idx)
    old_kg_full = html[kg_idx:kg_end_idx + len(kg_end_str)]
    NEW_KG = """  const kpisDisplay = kpis.filter(k => !k.video);
  const kpisVideo   = kpis.filter(k => k.video);
  const renderKpis = arr => arr.map(k=>`<div class="kcard ${k.imp?'imp':''}">
    <div class="kc-l">${k.l}</div>
    <div class="kc-v urb">${k.v}</div><div class="kc-s">${k.s||''}</div></div>`).join("");
  let kg = `<div class="panel-t" style="font-size:13px;margin:16px 0 8px;color:var(--tm)">Display</div>
  <div class="kgrid">${renderKpis(kpisDisplay)}</div>
  <div class="panel-t" style="font-size:13px;margin:16px 0 8px;color:var(--tm)">Vídeo</div>
  <div class="kgrid">${renderKpis(kpisVideo)}<div class="kcard"><div class="kc-l">Rentabilidade do CPCV</div><div class="kc-v urb">47%</div><div class="kc-s">CPCV efetivo R$ 0,19 vs. R$ 0,36 contratado</div></div></div>`;"""
    html = html[:kg_idx] + NEW_KG + html[kg_end_idx + len(kg_end_str):]
    print("  [OK] 2d+2e split display/video kpis")
else:
    print(f"  [WARN] 2d could not find kg block")

# Replace single kgrid usage with ${kg}
html = replace_once(html,
    '  <div class="kgrid">${kg}</div>\n\n  <div class="panel">',
    '  ${kg}\n\n  <div class="panel">',
    '2d replace kgrid wrapper')

# ── 2f. Timeline CSS
TIMELINE_CSS = """.timeline{position:relative;padding:40px 30px 20px;overflow-x:auto}
.tl-line{position:relative;height:4px;background:var(--bd2);border-radius:2px;margin:60px 20px 80px;min-width:600px}
.tl-line::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,var(--ac-d),var(--ac-l));border-radius:2px}
.tl-dot{position:absolute;top:50%;transform:translate(-50%,-50%);width:16px;height:16px;border-radius:50%;background:var(--ac);border:3px solid var(--bg);box-shadow:0 0 0 2px var(--ac),0 0 16px rgba(218,41,28,.5);cursor:pointer;transition:.2s;z-index:5}
.tl-dot:hover,.tl-dot.active{transform:translate(-50%,-50%) scale(1.4);box-shadow:0 0 0 3px var(--ac-l),0 0 24px rgba(218,41,28,.7)}
.tl-label{position:absolute;top:calc(100% + 12px);left:50%;transform:translateX(-50%);font-family:'Space Mono',monospace;font-size:9px;color:var(--tm);white-space:nowrap;text-align:center;line-height:1.4}
.tl-card{position:absolute;bottom:calc(100% + 16px);left:50%;transform:translateX(-50%);min-width:200px;background:var(--bg2);border:1px solid var(--ac-hover);border-radius:14px;padding:14px 16px;opacity:0;pointer-events:none;transition:.2s;z-index:20;box-shadow:0 16px 40px rgba(0,0,0,.6)}
.tl-dot:hover .tl-card,.tl-dot.active .tl-card{opacity:1;pointer-events:auto}
.tl-card-t{font-family:'Urbanist',sans-serif;font-weight:800;font-size:14px;margin-bottom:10px;color:var(--t)}
.tl-card-row{display:flex;justify-content:space-between;gap:16px;font-size:11px;padding:3px 0;border-bottom:1px solid var(--bd)}
.tl-card-row:last-of-type{border:none}
.tl-card-row .k{color:var(--tm)}.tl-card-row .v{font-weight:600}
.tl-det-btn{display:block;width:100%;margin-top:10px;padding:7px;text-align:center;background:var(--ac-soft2);border:1px solid var(--ac-hover);border-radius:8px;font-size:11px;color:var(--ac-l);font-weight:600;cursor:pointer;transition:.2s}
.tl-det-btn:hover{background:var(--grad-ac);color:#fff;border-color:transparent}
.tl-detail{display:none;margin-top:16px;padding:18px;background:var(--glass);border:1px solid var(--bd);border-radius:14px}
.tl-detail.open{display:block}
"""
html = replace_once(html,
    '@keyframes bob{',
    TIMELINE_CSS + '@keyframes bob{',
    '2f timeline CSS')

# ── 2f. Replace flight table with timeline HTML
OLD_TABLE_PANEL = """  <div class="panel">
    <div class="panel-h"><div><div class="panel-t">Desempenho por flight</div>
      <div class="panel-st">Display · valores reais da Base Consolidada · linha TOTAL reponderada por fórmula</div></div></div>
    <div class="tbl-wrap"><table class="dt"><thead><tr>
      <th class="l">Campanha</th><th>Código</th><th>Budget</th><th>Impr. visíveis</th><th>Cliques</th>
      <th>CTR</th><th>CPC</th><th>CPM efetivo</th><th>Rentab.</th></tr></thead>
      <tbody>${rows}${totRow}</tbody></table></div>
  </div>"""

NEW_TIMELINE_PANEL = """  <div class="panel">
    <div class="panel-h"><div><div class="panel-t">Desempenho por flight</div>
      <div class="panel-st">Linha do tempo da jornada HYPR × Claro</div></div></div>
    ${buildTimeline(F, t)}
  </div>"""

html = replace_once(html, OLD_TABLE_PANEL, NEW_TIMELINE_PANEL, '2f replace table with timeline')

# ── 2f. Add timeline JS functions before buildConsolidado
TIMELINE_JS = r"""function buildTimeline(F, t){
  const total = F.length - 1;
  const dots = F.map((f, i) => {
    const pct = total > 0 ? (i/total)*100 : 50;
    const above = i % 2 === 0;
    return `<div class="tl-dot" style="left:${pct}%" data-tl="${f.code}">
      <div class="tl-card" style="${above?'bottom:calc(100% + 16px);top:auto':'top:calc(100% + 16px);bottom:auto'}">
        <div class="tl-card-t">${f.camp}</div>
        <div class="tl-card-row"><span class="k">Mês</span><span class="v">${f.mes}</span></div>
        <div class="tl-card-row"><span class="k">Budget</span><span class="v">${fmtBRL0(f.budget)}</span></div>
        <div class="tl-card-row"><span class="k">Impressões</span><span class="v">${fmtMi(f.impr)}</span></div>
        <div class="tl-card-row"><span class="k">Cliques</span><span class="v">${fmtInt(f.clicks)}</span></div>
        <div class="tl-card-row"><span class="k">CTR</span><span class="v">${fmtPct(f.ctr)}</span></div>
        <button class="tl-det-btn" onclick="toggleTlDetail('${f.code}')">Ver detalhes</button>
      </div>
      <span class="tl-label">${f.mes}<br>${f.code}</span>
    </div>`;
  }).join('');

  const details = F.map(f => {
    const feats = DATA.features.filter(ft=>ft.code.includes(f.code));
    const cre   = DATA.creatives.filter(c=>c.camp===f.creativeCamp).slice(0,4);
    let featHtml = feats.length ? feats.map(ft=>`<div style="font-size:11px;padding:6px 0;border-bottom:1px solid var(--bd)"><b style="color:var(--ac-l)">${ft.feat}</b>${ft.clicks!=null?' · '+fmtInt(ft.clicks)+' cliques':''}</div>`).join('') : '<span style="font-size:11px;color:var(--tm)">—</span>';
    let creHtml  = cre.length ? `<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(100px,1fr));gap:8px;margin-top:8px">${cre.map(c=>c.type==='image'?`<img src="${c.src}" style="width:100%;border-radius:6px;border:1px solid var(--bd)" alt="">`:``).join('')}</div>` : '';
    const hasVid = f.video;
    return `<div class="tl-detail" id="tld-${f.code}">
      <div class="panel-t" style="margin-bottom:12px">${f.camp} · ${f.mes}</div>
      <div class="kgrid" style="grid-template-columns:repeat(auto-fill,minmax(140px,1fr))">
        <div class="kcard"><div class="kc-l">Impressões</div><div class="kc-v urb" style="font-size:20px">${fmtMi(f.impr)}</div></div>
        <div class="kcard"><div class="kc-l">Cliques</div><div class="kc-v urb" style="font-size:20px">${fmtInt(f.clicks)}</div></div>
        <div class="kcard"><div class="kc-l">CTR</div><div class="kc-v urb" style="font-size:20px">${fmtPct(f.ctr)}</div></div>
        <div class="kcard"><div class="kc-l">CPC</div><div class="kc-v urb" style="font-size:20px">${fmtBRL(f.cpc)}</div></div>
        <div class="kcard"><div class="kc-l">CPM efetivo</div><div class="kc-v urb" style="font-size:20px">${fmtBRL(f.cpm_ef)}</div></div>
        <div class="kcard imp"><div class="kc-l">Budget</div><div class="kc-v urb" style="font-size:20px">${fmtBRL0(f.budget)}</div></div>
        ${hasVid?`<div class="kcard imp"><div class="kc-l">Views 100%</div><div class="kc-v urb" style="font-size:20px">${fmtInt(f.v_views)}</div></div><div class="kcard"><div class="kc-l">VTR</div><div class="kc-v urb" style="font-size:20px">${fmtPct(f.v_vtr)}</div></div>`:''}
      </div>
      ${feats.length?`<div style="margin-top:14px"><div style="font-family:'Space Mono',monospace;font-size:9.5px;color:var(--tm);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">Features ativadas</div>${featHtml}</div>`:''}
      ${cre.length?`<div style="margin-top:14px"><div style="font-family:'Space Mono',monospace;font-size:9.5px;color:var(--tm);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">Preview de criativos</div>${creHtml}</div>`:''}
    </div>`;
  }).join('');

  return `<div class="timeline">
    <div class="tl-line">${dots}</div>
  </div>
  ${details}`;
}

function toggleTlDetail(code){
  document.querySelectorAll('.tl-detail').forEach(el=>{
    if(el.id==='tld-'+code) el.classList.toggle('open');
    else el.classList.remove('open');
  });
}

"""
html = replace_once(html,
    'function buildConsolidado(){',
    TIMELINE_JS + 'function buildConsolidado(){',
    '2f add timeline JS functions')

# ── 2g. Feature cards function
BUILD_FEAT_CARDS_JS = r"""function buildFeatCards(){
  const map = {};
  DATA.features.forEach(f=>{
    if(!map[f.feat]) map[f.feat]={feat:f.feat, camps:[], vi:0, clicks:0, ctr_sum:0, ctr_n:0, plays:0};
    map[f.feat].camps.push(f.camp);
    if(f.vi) map[f.feat].vi += f.vi;
    if(f.clicks) map[f.feat].clicks += f.clicks;
    if(f.ctr){map[f.feat].ctr_sum += f.ctr; map[f.feat].ctr_n++;}
    if(f.plays) map[f.feat].plays += f.plays;
  });
  return Object.values(map).map(g=>{
    const featName = g.feat.replace('Tap-to-Map','Tap-to-Go');
    const camps = [...new Set(g.camps)].join(', ');
    return `<div class="featcard" style="padding:18px">
      <div class="featcard-n">${featName}</div>
      <div style="font-size:10.5px;color:var(--tm);margin-bottom:10px">${camps}</div>
      ${g.vi?`<div class="featcard-row"><span class="k">Impressões</span><span class="v">${fmtInt(g.vi)}</span></div>`:''}
      ${g.clicks?`<div class="featcard-row"><span class="k">Cliques</span><span class="v">${fmtInt(g.clicks)}</span></div>`:''}
      ${g.ctr_n?`<div class="featcard-row"><span class="k">CTR</span><span class="v">${fmtPct(g.ctr_sum/g.ctr_n)}</span></div>`:''}
      ${g.plays?`<div class="featcard-row"><span class="k">Plays PDOOH</span><span class="v">${fmtInt(g.plays)}</span></div>`:''}
    </div>`;
  }).join('');
}

"""
html = replace_once(html,
    'function buildConsolidado(){',
    BUILD_FEAT_CARDS_JS + 'function buildConsolidado(){',
    '2g add buildFeatCards')

# 2g. Replace features table panel with cards panel
# Find and replace the features panel in consolidado
feat_marker = 'panel-t">Features ativadas</div>\n      <div class="panel-st">Resultados por tipo de feature'
feat_idx = html.find(feat_marker)
if feat_idx >= 0:
    panel_start = html.rfind('<div class="panel">', 0, feat_idx)
    # find the </div> that closes this panel - it should end with </table></div></div>\n\n
    panel_end_search = '</table></div>\n  </div>'
    panel_end = html.find(panel_end_search, feat_idx)
    if panel_end >= 0:
        old_feat_panel = html[panel_start:panel_end + len(panel_end_search)]
        NEW_FEAT_PANEL = """  <div class="panel">
    <div class="panel-h"><div><div class="panel-t">Features ativadas — resultados consolidados</div></div></div>
    <div class="det-feat">${buildFeatCards()}</div>
  </div>"""
        html = html[:panel_start] + NEW_FEAT_PANEL + html[panel_end + len(panel_end_search):]
        print("  [OK] 2g replace features table with cards")
    else:
        print("  [WARN] 2g could not find panel end")
else:
    print(f"  [WARN] 2g feature panel not found")

# ── 2h. Remove buildInconsistencias and foot
if '${buildInconsistencias()}' in html:
    html = replace_once(html,
        '\n  ${buildInconsistencias()}',
        '',
        '2h remove buildInconsistencias call')

foot_idx = html.find('<div class="foot">Fonte: FINAL_Base_Consolidada')
if foot_idx >= 0:
    foot_end = html.find('</div>', foot_idx) + 6
    html = html[:foot_idx] + html[foot_end:]
    print("  [OK] 2h remove foot from consolidado")
else:
    print("  [WARN] 2h foot not found")

# ── 3a. buildCampanhasHub with filters
OLD_CAMPBOX = """function buildCampanhasHub(){
  const F = DATA.flights;
  let boxes = F.map((f,i)=>{
    const cover = firstCreativeFor(f.creativeCamp);
    const nCre = DATA.creatives.filter(c=>c.camp===f.creativeCamp).length;
    const nFeat = DATA.features.filter(ft=>ft.code.includes(f.code)).length;
    const prelim = f.prelim ? '<span class="chip prelim" style="margin-left:6px">preliminar</span>' : '';
    return `<button class="campbox" data-flight="${f.code}">
      <div class="campbox-top">
        ${cover?`<img src="${cover}" alt="">`:''}\n        <span class="campbox-vert">${f.vert}</span>
        <span class="campbox-code">${f.code}</span>
      </div>
      <div class="campbox-body">
        <div class="campbox-name">${f.camp}${prelim}</div>
        <div class="campbox-per">${f.mes} · ${f.periodo}</div>
        <div class="campbox-mini">
          <div class="cm"><div class="cm-v urb">${fmtMi(f.impr)}</div><div class="cm-l">impressões</div></div>
          <div class="cm"><div class="cm-v urb">${fmtInt(f.clicks)}</div><div class="cm-l">cliques</div></div>
          <div class="cm"><div class="cm-v urb">${nCre}</div><div class="cm-l">criativos</div></div>
          <div class="cm"><div class="cm-v urb">${nFeat||'—'}</div><div class="cm-l">features</div></div>
        </div>
        <div class="campbox-go">Ver campanha <span>→</span></div>
      </div></button>`;
  }).join("");

  return `<div class="sec-head">
    <button class="sec-back" data-go="hub">← Voltar ao início</button>
    <h1 class="sec-title urb">Campanhas Ativadas</h1>
    <p class="sec-sub">Nove flights ao longo de seis campanhas. Clique em qualquer uma para ver os dados consolidados daquele flight, os criativos veiculados e os resultados das features ativadas.</p>
  </div>
  <div class="campgrid">${boxes}</div>
  <div class="foot">9 flights · 6 campanhas distintas · use o filtro da Central de Criativos para ver todas as peças</div>`;
}"""

NEW_CAMPBOX = r"""function buildCampBox(f, i){
  const cover = firstCreativeFor(f.creativeCamp);
  const nCre = DATA.creatives.filter(c=>c.camp===f.creativeCamp).length;
  const nFeat = DATA.features.filter(ft=>ft.code.includes(f.code)).length;
  const prelim = f.prelim ? '<span class="chip prelim" style="margin-left:6px">preliminar</span>' : '';
  return `<button class="campbox" data-flight="${f.code}">
    <div class="campbox-top">
      ${cover?`<img src="${cover}" alt="">`:''}
      <span class="campbox-vert">${f.vert}</span>
      <span class="campbox-code">${f.code}</span>
    </div>
    <div class="campbox-body">
      <div class="campbox-name">${f.camp}${prelim}</div>
      <div class="campbox-per">${f.mes} · ${f.periodo}</div>
      <div class="campbox-mini">
        <div class="cm"><div class="cm-v urb">${fmtMi(f.impr)}</div><div class="cm-l">impressões</div></div>
        <div class="cm"><div class="cm-v urb">${fmtInt(f.clicks)}</div><div class="cm-l">cliques</div></div>
        <div class="cm"><div class="cm-v urb">${nCre}</div><div class="cm-l">criativos</div></div>
        <div class="cm"><div class="cm-v urb">${nFeat||'—'}</div><div class="cm-l">features</div></div>
      </div>
      <div class="campbox-go">Ver campanha <span>→</span></div>
    </div></button>`;
}

let campFilter = {vert:'all', mes:'all'};

function buildCampanhasHub(){
  const F = DATA.flights;
  let boxes = F.map((f,i)=> buildCampBox(f,i)).join("");

  const verts = [...new Set(F.map(f=>f.vert))].sort();
  const meses = [...new Set(F.map(f=>f.mes))];
  const vertPills = `<button class="pill act" data-cf="vert" data-cv="all">Todas</button>` +
    verts.map(v=>`<button class="pill" data-cf="vert" data-cv="${v}">${v}</button>`).join("");
  const mesPills = `<button class="pill act" data-cf="mes" data-cv="all">Todos</button>` +
    meses.map(m=>`<button class="pill" data-cf="mes" data-cv="${m}">${m}</button>`).join("");

  return `<div class="sec-head">
    <button class="sec-back" data-go="hub">← Voltar ao início</button>
    <h1 class="sec-title urb">Campanhas Ativadas</h1>
    <p class="sec-sub">Nove flights ao longo de seis campanhas. Clique em qualquer uma para ver os dados consolidados daquele flight, os criativos veiculados e os resultados das features ativadas.</p>
  </div>
  <div class="filters" style="position:static;margin-bottom:20px">
    <div class="filter-row"><span class="filter-lbl">Vertical</span><div class="pills" id="vertPills">${vertPills}</div></div>
    <div class="filter-row"><span class="filter-lbl">Mês de início</span><div class="pills" id="mesPills">${mesPills}</div></div>
  </div>
  <div class="campgrid" id="campgrid">${boxes}</div>`;
}"""

html = replace_once(html, OLD_CAMPBOX, NEW_CAMPBOX, '3a buildCampanhasHub with filters')

# 3a. Add camp filter event listener
CAMP_FILTER_EVENT = """// camp filter
document.addEventListener('click', e=>{
  const p = e.target.closest('.pill[data-cf]');
  if(!p) return;
  campFilter[p.dataset.cf] = p.dataset.cv;
  p.closest('.pills').querySelectorAll('.pill').forEach(x=>x.classList.remove('act'));
  p.classList.add('act');
  const F2 = DATA.flights.filter(f=>
    (campFilter.vert==='all'||f.vert===campFilter.vert) &&
    (campFilter.mes==='all'||f.mes===campFilter.mes));
  const cg = document.getElementById('campgrid');
  if(cg) cg.innerHTML = F2.map((f,i)=>buildCampBox(f,i)).join('');
});
"""
html = replace_once(html,
    '// flight detail click',
    CAMP_FILTER_EVENT + '// flight detail click',
    '3a camp filter event')

# ── 3b. Remove prelimNote and vidNote
html = replace_once(html,
    '  ${prelimNote}${vidNote}\n  <div class="kgrid">${kg}</div>',
    '  <div class="kgrid">${kg}</div>',
    '3b remove notes')

html = replace_once(html,
    '      <div class="panel-st">resultados reais desta campanha</div></div></div>',
    '      </div></div>',
    '3b remove "resultados reais"')

# ── 3c. Creative labels
html = replace_once(html,
    '<span class="ccard-type">IMG</span>',
    '<span class="ccard-type">Display</span>',
    '3c IMG→Display')

html = replace_once(html,
    '<span class="ccard-type vid">VÍDEO</span>',
    '<span class="ccard-type vid">Vídeo</span>',
    '3c VÍDEO→Vídeo')

html = replace_once(html,
    '<span class="ccard-type ifr">INTERATIVO</span>',
    '<span class="ccard-type">Display</span>',
    '3c INTERATIVO→Display')

# ── 4. Rewrite buildMateriais
OLD_MATERIAIS = """function buildMateriais(){
  const mats = [
    [\"📊\",\"Base Consolidada\",\"Planilha-mestra com todas as métricas por campanha e flight — display e vídeo, com dicionário de métricas.\",\"FINAL_Base_Consolidada_Claro_v1.xlsx\"],
    [\"🎯\",\"Resultados de Features\",\"Detalhamento por feature ativada: PDOOH, Topics, Segmentação iOS, Tap-to-Map, Downloaded Apps, Click-to-Calendar.\",\"aba · base consolidada\"],
    [\"📈\",\"Survey Brand-Lift\",\"Dados estruturados das 4 ondas de pesquisa de percepção (exposto vs. controle).\",\"aba · base consolidada\"],
    [\"🎨\",\"Pacote de Criativos\",\"Arquivo consolidado com todas as peças veiculadas, organizadas por campanha e tamanho.\",\"CRIATIVOS-CLARO-CONSOLIDADO\"],
    [\"📋\",\"Dicionário de Métricas\",\"Rastreabilidade de cada métrica apurada — origem e tratamento.\",\"aba · base consolidada\"],
    [\"⚠️\",\"Notas de Inconsistência\",\"Pontos de atenção e tratamentos aplicados para garantir a veracidade dos dados.\",\"aba · base consolidada\"],
  ];
  let cards = mats.map(m=>`<div class="matcard">
    <div class="matcard-ic">${m[0]}</div>
    <div class="matcard-t">${m[1]}</div>
    <div class="matcard-d">${m[2]}</div>
    <span class="matcard-tag">${m[3]}</span></div>`).join(\"\");
  return `<div class="sec-head">
    <button class="sec-back" data-go="hub">← Voltar ao início</button>
    <h1 class="sec-title urb">Hub de Materiais</h1>
    <p class="sec-sub">Os documentos e fontes de dados que sustentam este consolidado. Todos os números do dashboard são apurados a partir destes materiais.</p>
  </div>
  <div class="matgrid">${cards}</div>
  <div class="foot">Materiais Claro × HYPR · fontes de verdade do consolidado</div>`;
}"""

NEW_MATERIAIS = r"""function buildMateriais(){
  const cats = [
    {
      ic:'📋', label:'Pós-Vendas',
      desc:'Relatórios de campanha e análises de resultados de mídia.',
      items:[
        {title:'Atendimento Digital — Dez/25 (Completo)', url:'https://docs.google.com/presentation/d/1xkzeTe479Zoo1eLnVG0dZGkYSBXiEIjNTtrm2o9fYv0/edit'},
        {title:'Atendimento Digital — Jan/26 (One Page)', url:'https://docs.google.com/presentation/d/1Cz89-0G8pwxr_EtwQN7nAMMppE4KCl_IZTLRYZrDHVY/edit'},
        {title:'Atendimento Digital — Dez/25 (One Page)', url:'https://docs.google.com/presentation/d/1_4e9qe0fC8wano8Vq2Imi-7TJ4YdJ9DXzAFz4OFibbE/edit'},
        {title:'iPhone 17 — Mai/26', url:'https://docs.google.com/presentation/d/1vo-C2aObSeuf2p6TdV1p8w26ddJ7gp4kg_xVazpY0BA/edit'},
        {title:'PME — Mar/26', url:'https://docs.google.com/presentation/d/1ybfLGEdvdmfFIIlp-0QBzL6h1VBpRidciHP-YZ_z7N4/edit'},
        {title:'PME — Abr/26', url:'https://docs.google.com/presentation/d/1mlhjsbEeOqahfHMT7seaZPWw4KQtuDVKpiiZgVOmBds/edit'},
      ]
    },
    {
      ic:'🔬', label:'Estudos',
      desc:'Surveys, brand-lift e estudos de audiência conduzidos ao longo das campanhas.',
      items:[
        {title:'Survey F1 — Awareness', url:'https://docs.google.com/presentation/d/1zIOzKg5Sz2mHhRxGO64uNr3iI_wMwzEVe_vkk1XqimA/edit'},
        {title:'Audience Discovery — Claro Pós 2026', url:'https://docs.google.com/presentation/d/1s3sTbKBqm-p-MXJemdtvVIYTRQFuxA-0Ck2MhF73000/edit'},
        {title:'PME Eletromidia — Estudo', url:'https://docs.google.com/presentation/d/1nouRm-1pMi4S8q3JyAIXKzSF9MxYruluwtxDIvDBgwc/edit'},
      ]
    },
    {
      ic:'🎯', label:'Audience Discovery',
      desc:'Propostas e estudos de audiência personalizados para cada vertical.',
      items:[
        {title:'Samsung Família A', url:'https://docs.google.com/presentation/d/1tYiQpKJpvacBegyUpje6lHGI8WANCyaKEIl6asU2FVA/edit'},
        {title:'iPhone 17', url:'https://docs.google.com/presentation/d/1yk5IzEIk6U8HVfajxE-aGUOE0unKQFHgHvU3sX-NtWg/edit'},
        {title:'Jovi V70', url:'https://docs.google.com/presentation/d/14NPElhHhUfyAxvSGIzX2TCIxe9br7uFxRl_hj3hLR8U/edit'},
        {title:'PME | Copa do Mundo 2026', url:'https://docs.google.com/presentation/d/17b-hVdvvz-u7eZ6gIwvggdRqESKsY3MAJ7D-IuWRRZY/edit'},
        {title:'PME | Copa do Mundo (variante)', url:'https://docs.google.com/presentation/d/1Q-mQ-vVkE9IDIPmXxt_BSVbiRim0HV0Qan7K06fkDmY/edit'},
        {title:'Claro Flex | Copa do Mundo', url:'https://docs.google.com/presentation/d/1t4_G5owwRRqjnhC16vNVPrBgNTwEiG6CSRxkmI23JgQ/edit'},
        {title:'Claro Fibra | Pré-Copa do Mundo', url:'https://docs.google.com/presentation/d/151d17E-st4r_Ow7DHIQrcPMcAAO9cICh1G-26loHBn0/edit'},
        {title:'PME | Web Summit Rio', url:'https://docs.google.com/presentation/d/1Axf_jBsIisq09BZ1ijCkqvtiad-vpQeNiRKMCm_nAK8/edit'},
      ]
    }
  ];

  const cards = cats.map(cat=>`
    <div class="matcard" style="display:flex;flex-direction:column">
      <div class="matcard-ic">${cat.ic}</div>
      <div class="matcard-t">${cat.label}</div>
      <div class="matcard-d" style="margin-bottom:14px">${cat.desc}</div>
      <div style="display:flex;flex-direction:column;gap:6px;margin-top:auto">
        ${cat.items.map(it=>`<a href="${it.url}" target="_blank" rel="noopener"
          style="display:flex;align-items:center;gap:8px;font-size:11.5px;color:var(--tm);text-decoration:none;padding:7px 10px;border:1px solid var(--bd);border-radius:8px;transition:.18s;background:var(--glass)"
          onmouseover="this.style.borderColor='var(--ac-hover)';this.style.color='var(--t)'"
          onmouseout="this.style.borderColor='var(--bd)';this.style.color='var(--tm)'">
          <span style="color:var(--ac-l)">↗</span> ${it.title}
        </a>`).join('')}
      </div>
    </div>`).join('');

  return `<div class="sec-head">
    <button class="sec-back" data-go="hub">← Voltar ao início</button>
    <h1 class="sec-title urb">Hub de Materiais</h1>
    <p class="sec-sub">Acesse os materiais de Pós-Vendas, Estudos e Audience Discovery produzidos pela HYPR ao longo da parceria com a Claro.</p>
  </div>
  <div class="matgrid">${cards}</div>`;
}"""

html = replace_once(html, OLD_MATERIAIS, NEW_MATERIAIS, '4 rewrite buildMateriais')

# ── 5a. Onda → Survey
html = replace_once(html, '"Todas as ondas"', '"Todas as Surveys"', '5a todas ondas')
html = replace_once(html,
    '<span class="filter-lbl">Onda de pesquisa</span>',
    '<span class="filter-lbl">Survey</span>',
    '5a onda label')
html = replace_once(html,
    '"Lift por resposta — todas as ondas"',
    '"Lift por resposta — todas as Surveys"',
    '5a blTitle')

# ── 5b. Type filter pills
html = replace_once(html,
    '  const wavePills = `<button class="pill act" data-bl="all">Todas as Surveys</button>`',
    """  const typePills = `<button class="pill act" data-blt="all">Todas</button>
  <button class="pill" data-blt="Awareness">Awareness</button>
  <button class="pill" data-blt="Intenção">Intenção</button>`;
  const wavePills = `<button class="pill act" data-bl="all">Todas as Surveys</button>`""",
    '5b type pills')

html = replace_once(html,
    '      <div class="bl-cg"><span class="filter-lbl">Survey</span><div class="pills" id="blPills">${wavePills}</div></div>',
    '      <div class="bl-cg"><span class="filter-lbl">Tipo</span><div class="pills" id="blTypePills">${typePills}</div></div>\n      <div class="bl-cg"><span class="filter-lbl">Survey</span><div class="pills" id="blPills">${wavePills}</div></div>',
    '5b add type filter row')

# ── 5c. Note margin
html = replace_once(html,
    '  <div class="note"><strong>Metodologia:</strong>',
    '  <div class="note" style="margin-top:24px"><strong>Metodologia:</strong>',
    '5c note margin')

# ── 5d. Improve n display
html = replace_once(html,
    "      <div class=\"blc-n\">n exposto ${w.nExp} · controle ${w.nCtrl}</div></div>`;",
    """      <div style="display:flex;gap:10px;margin-top:8px">
        <div style="flex:1;background:var(--glass2);border-radius:8px;padding:7px 10px;text-align:center">
          <div style="font-family:'Urbanist',sans-serif;font-weight:800;font-size:16px;color:var(--ac-l)">${w.nExp}</div>
          <div style="font-size:9.5px;color:var(--tm);font-family:'Space Mono',monospace;text-transform:uppercase;letter-spacing:.5px">Exposto</div>
        </div>
        <div style="flex:1;background:var(--glass2);border-radius:8px;padding:7px 10px;text-align:center">
          <div style="font-family:'Urbanist',sans-serif;font-weight:800;font-size:16px;color:var(--tm)">${w.nCtrl}</div>
          <div style="font-size:9.5px;color:var(--tdim);font-family:'Space Mono',monospace;text-transform:uppercase;letter-spacing:.5px">Controle</div>
        </div>
      </div></div>`;""",
    '5d improve n display')

# ── 6a. Criativos disclaimer
html = replace_once(html,
    'Filtre por tamanho ou por campanha.</p>\n  </div>',
    'Filtre por tamanho ou por campanha.</p>\n  <div class="note" style="margin-top:14px"><strong>Atenção:</strong> Criativos enviados ao longo das campanhas podem não estar presentes na relação final.</div>\n  </div>',
    '6a disclaimer')

# ── 6d. Features filter
html = replace_once(html,
    "let cvFilter = {size:\"all\", camp:\"all\"};",
    "let cvFilter = {size:\"all\", camp:\"all\", feat:\"all\"};",
    '6d cvFilter feat')

html = replace_once(html,
    "  const campPills = `<button class=\"pill act\" data-f=\"camp\" data-v=\"all\">Todas<span class=\"ct\">${C.length}</span></button>` +\n    camps.map(s=>`<button class=\"pill\" data-f=\"camp\" data-v=\"${s}\">${s}<span class=\"ct\">${campCounts[s]}</span></button>`).join(\"\");",
    "  const campPills = `<button class=\"pill act\" data-f=\"camp\" data-v=\"all\">Todas<span class=\"ct\">${C.length}</span></button>` +\n    camps.map(s=>`<button class=\"pill\" data-f=\"camp\" data-v=\"${s}\">${s}<span class=\"ct\">${campCounts[s]}</span></button>`).join(\"\");\n  const featPill = `<button class=\"pill\" data-f=\"feat\" data-v=\"feat\">Apenas Features</button>`;",
    '6d featPill var')

html = replace_once(html,
    '    <div class="filter-row"><span class="filter-lbl">Campanha</span><div class="pills" id="campPills">${campPills}</div></div>',
    '    <div class="filter-row"><span class="filter-lbl">Campanha</span><div class="pills" id="campPills">${campPills}</div></div>\n    <div class="filter-row"><span class="filter-lbl">Tipo</span><div class="pills" id="featPills">${featPill}</div></div>',
    '6d feat filter row')

html = replace_once(html,
    '  const C = DATA.creatives.filter(c=>\n    (cvFilter.size==="all"||c.size===cvFilter.size) &&\n    (cvFilter.camp==="all"||c.camp===cvFilter.camp));',
    '  const C = DATA.creatives.filter(c=>\n    (cvFilter.size==="all"||c.size===cvFilter.size) &&\n    (cvFilter.camp==="all"||c.camp===cvFilter.camp) &&\n    (cvFilter.feat!=="feat"||c.feature===true));',
    '6d feat filter condition')

# ── Save
print(f"\nSaving ({len(html)} chars, {html.count(chr(10))} lines)...")
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
print("Done!")
