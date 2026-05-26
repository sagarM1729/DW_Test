<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pharma Commercial DataLake Explorer</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>

:root {
  /* Light mode (default) */
  --bg: #F7FAFC;
  --surface: #FFFFFF;
  --surface-2: #F1F5F9;
  --surface-3: #E2E8F0;
  --border: #CBD5E1;
  --border-2: #94A3B8;
  --text: #1E293B;
  --text-muted: #64748B;
  --text-dim: #94A3B8;

  --dim: #2563EB;
  --dim-bg: rgba(37,99,235,0.08);
  --dim-border: rgba(37,99,235,0.18);

  --fact: #F59E42;
  --fact-bg: rgba(245,158,66,0.08);
  --fact-border: rgba(245,158,66,0.18);

  --mmonth: #14B8A6;
  --mmonth-bg: rgba(20,184,166,0.08);
  --mmonth-border: rgba(20,184,166,0.18);

  --mquart: #6366F1;
  --mquart-bg: rgba(99,102,241,0.08);
  --mquart-border: rgba(99,102,241,0.18);

  --map: #EC4899;
  --map-bg: rgba(236,72,153,0.08);
  --map-border: rgba(236,72,153,0.18);

  --pk: #F59E42;
  --fk: #14B8A6;
  --ak: #6366F1;
  --sys: #94A3B8;

  --font-body: 'Outfit', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

.dark-mode {
  --bg: #060A14;
  --surface: #0C1422;
  --surface-2: #101A2E;
  --surface-3: #152038;
  --border: #1A2B45;
  --border-2: #243B5C;
  --text: #C8D8EE;
  --text-muted: #5A7898;
  --text-dim: #3A5270;

  --dim: #4F8EF7;
  --dim-bg: rgba(79,142,247,0.1);
  --dim-border: rgba(79,142,247,0.25);

  --fact: #F5A623;
  --fact-bg: rgba(245,166,35,0.1);
  --fact-border: rgba(245,166,35,0.25);

  --mmonth: #2DD4BF;
  --mmonth-bg: rgba(45,212,191,0.1);
  --mmonth-border: rgba(45,212,191,0.25);

  --mquart: #818CF8;
  --mquart-bg: rgba(129,140,248,0.1);
  --mquart-border: rgba(129,140,248,0.25);

  --map: #F472B6;
  --map-bg: rgba(244,114,182,0.1);
  --map-border: rgba(244,114,182,0.25);

  --pk: #FFD166;
  --fk: #06D6A0;
  --ak: #A78BFA;
  --sys: #3A5270;
}

* { margin:0; padding:0; box-sizing:border-box; }

body {
  font-family: var(--font-body);
  background: var(--bg);
  color: var(--text);
  height: 100vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

/* HEADER */
header {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 24px;
  height: 58px;
  display: flex;
  align-items: center;
  gap: 20px;
  flex-shrink: 0;
  position: relative;
  z-index: 10;
}
.brand {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}
.brand-icon {
  width: 32px; height: 32px;
  background: linear-gradient(135deg, #4F8EF7, #2DD4BF);
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  font-size: 16px;
}
.brand-text { font-size: 14px; font-weight: 700; letter-spacing: 0.02em; color: var(--text); }
.brand-sub { font-size: 11px; color: var(--text-muted); font-weight: 400; letter-spacing: 0.05em; text-transform: uppercase; }

.search-wrap {
  flex: 1;
  max-width: 380px;
  position: relative;
}
.search-wrap input {
  width: 100%;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 8px 12px 8px 36px;
  font-family: var(--font-body);
  font-size: 13px;
  color: var(--text);
  outline: none;
  transition: border-color 0.2s;
}
.search-wrap input:focus { border-color: var(--dim); }
.search-wrap input::placeholder { color: var(--text-dim); }
.search-icon {
  position: absolute; left: 10px; top: 50%; transform: translateY(-50%);
  color: var(--text-dim); font-size: 14px; pointer-events: none;
}

.header-stats {
  margin-left: auto;
  display: flex; gap: 16px; align-items: center;
}
.stat-pill {
  font-size: 11px; font-weight: 500; letter-spacing: 0.04em;
  background: var(--surface-2); border: 1px solid var(--border);
  border-radius: 20px; padding: 4px 10px; color: var(--text-muted);
}
.stat-pill span { color: var(--text); }

.platform-badge {
  font-family: var(--font-mono); font-size: 10px; font-weight: 600;
  border-radius: 4px; padding: 3px 7px;
}
.db-badge { background: var(--fact-bg); color: var(--fact); border: 1px solid var(--fact-border); }
.sf-badge { background: var(--mmonth-bg); color: var(--mmonth); border: 1px solid var(--mmonth-border); }

/* LAYOUT */
.layout {
  display: flex;
  flex: 1;
  overflow: hidden;
}

/* SIDEBAR */
.sidebar {
  width: 264px;
  flex-shrink: 0;
  background: var(--surface);
  border-right: 1px solid var(--border);
  overflow-y: auto;
  padding: 12px 0;
}
.sidebar::-webkit-scrollbar { width: 4px; }
.sidebar::-webkit-scrollbar-track { background: transparent; }
.sidebar::-webkit-scrollbar-thumb { background: var(--border-2); border-radius: 4px; }

.cat-group { margin-bottom: 4px; }
.cat-header {
  display: flex; align-items: center; gap: 8px;
  padding: 7px 16px;
  cursor: pointer;
  user-select: none;
}
.cat-header:hover { background: var(--surface-2); }
.cat-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
.cat-label { font-size: 11px; font-weight: 600; letter-spacing: 0.07em; text-transform: uppercase; flex: 1; }
.cat-count {
  font-family: var(--font-mono); font-size: 10px; font-weight: 500;
  background: var(--surface-3); border-radius: 10px; padding: 2px 6px;
  color: var(--text-muted);
}
.cat-chevron { font-size: 10px; color: var(--text-dim); transition: transform 0.2s; }
.cat-group.collapsed .cat-chevron { transform: rotate(-90deg); }

.table-list { list-style: none; }
.cat-group.collapsed .table-list { display: none; }

.table-item {
  padding: 6px 16px 6px 32px;
  cursor: pointer;
  display: flex; align-items: center; gap: 8px;
  transition: background 0.15s;
}
.table-item:hover { background: var(--surface-2); }
.table-item.active { background: var(--surface-3) !important; }
.table-item-name {
  font-family: var(--font-mono); font-size: 11px; font-weight: 500;
  color: var(--text-muted); white-space: nowrap; overflow: hidden;
  text-overflow: ellipsis; flex: 1;
}
.table-item.active .table-item-name { color: var(--text); }
.table-item-dot { width: 5px; height: 5px; border-radius: 50%; flex-shrink: 0; opacity: 0.6; }
.table-item.active .table-item-dot { opacity: 1; }

/* MAIN CONTENT */
.main {
  flex: 1;
  overflow-y: auto;
  background: var(--bg);
}
.main::-webkit-scrollbar { width: 6px; }
.main::-webkit-scrollbar-track { background: transparent; }
.main::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

/* WELCOME */
#welcome {
  padding: 48px 40px;
  max-width: 1100px;
}
.welcome-hero { margin-bottom: 40px; }
.welcome-hero h1 {
  font-size: 32px; font-weight: 800; letter-spacing: -0.02em;
  background: linear-gradient(135deg, #4F8EF7 0%, #2DD4BF 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text; margin-bottom: 10px;
}
.welcome-hero p {
  font-size: 14px; color: var(--text-muted); line-height: 1.7; max-width: 680px;
}

.overview-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
  margin-bottom: 36px;
}
.overview-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 16px;
  cursor: pointer;
  transition: all 0.2s;
  position: relative;
  overflow: hidden;
}
.overview-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
}
.overview-card:hover { border-color: var(--border-2); transform: translateY(-1px); }
.ov-count { font-family: var(--font-mono); font-size: 28px; font-weight: 600; margin-bottom: 4px; }
.ov-label { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 6px; }
.ov-desc { font-size: 11px; color: var(--text-muted); line-height: 1.5; }

.domain-cards {
  display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px;
}
.domain-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 20px 24px;
}
.domain-card h3 {
  font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--text-muted); margin-bottom: 10px;
}
.domain-card p { font-size: 13px; color: var(--text-muted); line-height: 1.65; }

/* TABLE DETAIL */
#table-detail { padding: 32px 36px; display: none; }

.detail-header {
  margin-bottom: 28px;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--border);
}
.detail-header-top {
  display: flex; align-items: flex-start; gap: 14px; margin-bottom: 14px;
}
.detail-table-name {
  font-family: var(--font-mono); font-size: 22px; font-weight: 600;
  color: var(--text); letter-spacing: -0.01em; flex: 1;
}
.cat-badge {
  font-family: var(--font-mono); font-size: 11px; font-weight: 600;
  border-radius: 6px; padding: 5px 10px; flex-shrink: 0;
}
.detail-desc {
  font-size: 13.5px; color: var(--text-muted); line-height: 1.7;
  max-width: 860px; margin-bottom: 14px;
}
.detail-meta {
  display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
}
.meta-tag {
  font-size: 11px; color: var(--text-muted); background: var(--surface);
  border: 1px solid var(--border); border-radius: 4px; padding: 3px 8px;
  display: flex; align-items: center; gap: 5px;
}
.meta-tag .dot { width: 6px; height: 6px; border-radius: 50%; }

.detail-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 28px;
}

.panel {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
}
.panel-header {
  padding: 14px 18px;
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; gap: 8px;
}
.panel-header h3 {
  font-size: 12px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.07em; color: var(--text-muted);
}
.panel-count {
  font-family: var(--font-mono); font-size: 10px;
  background: var(--surface-3); border-radius: 8px; padding: 2px 6px; color: var(--text-muted);
}
.panel-body { padding: 4px 0; max-height: 380px; overflow-y: auto; }
.panel-body::-webkit-scrollbar { width: 3px; }
.panel-body::-webkit-scrollbar-thumb { background: var(--border-2); }

/* Columns */
.col-row {
  display: flex; align-items: center; gap: 10px;
  padding: 8px 18px;
  border-bottom: 1px solid rgba(26,43,69,0.5);
  transition: background 0.1s;
}
.col-row:last-child { border-bottom: none; }
.col-row:hover { background: var(--surface-2); }
.col-name { font-family: var(--font-mono); font-size: 11.5px; font-weight: 500; min-width: 160px; color: var(--text); }
.col-badges { display: flex; gap: 4px; flex-shrink: 0; }
.badge {
  font-family: var(--font-mono); font-size: 9px; font-weight: 700;
  border-radius: 3px; padding: 2px 5px; letter-spacing: 0.05em;
}
.badge-pk { background: rgba(255,209,102,0.15); color: var(--pk); border: 1px solid rgba(255,209,102,0.3); }
.badge-fk { background: rgba(6,214,160,0.12); color: var(--fk); border: 1px solid rgba(6,214,160,0.25); }
.badge-ak { background: rgba(167,139,250,0.12); color: var(--ak); border: 1px solid rgba(167,139,250,0.25); }
.badge-sys { background: rgba(58,82,112,0.3); color: var(--sys); border: 1px solid rgba(58,82,112,0.5); }
.col-desc { font-size: 11px; color: var(--text-muted); flex: 1; }

/* Relationships */
.rel-section { padding: 10px 0; }
.rel-section-title {
  font-size: 10px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--text-dim); padding: 4px 18px 8px;
}
.rel-row {
  display: flex; align-items: flex-start; gap: 10px;
  padding: 8px 18px;
  border-bottom: 1px solid rgba(26,43,69,0.5);
  transition: background 0.1s; cursor: pointer;
}
.rel-row:last-child { border-bottom: none; }
.rel-row:hover { background: var(--surface-2); }
.rel-arrow { font-size: 12px; flex-shrink: 0; margin-top: 2px; }
.rel-content { flex: 1; }
.rel-table { font-family: var(--font-mono); font-size: 11px; font-weight: 600; color: var(--text); margin-bottom: 2px; }
.rel-key { font-family: var(--font-mono); font-size: 10px; color: var(--text-dim); margin-bottom: 3px; }
.rel-desc { font-size: 11px; color: var(--text-muted); line-height: 1.4; }

.empty-state {
  padding: 24px 18px; text-align: center;
  font-size: 12px; color: var(--text-dim);
}

/* Visualization */
.viz-panel {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
}
.viz-header {
  padding: 14px 18px;
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; justify-content: space-between;
}
.viz-header h3 {
  font-size: 12px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.07em; color: var(--text-muted);
}
.viz-hint { font-size: 11px; color: var(--text-dim); }
#viz-svg-container {
  padding: 12px;
  background: var(--bg);
  display: flex; justify-content: center;
}

/* Search highlight */
.hl { background: rgba(79,142,247,0.3); border-radius: 2px; }

/* Scrollbar */
#table-detail::-webkit-scrollbar { width: 6px; }
#table-detail::-webkit-scrollbar-thumb { background: var(--border); }

/* No results */
.no-results {
  padding: 20px 16px;
  font-size: 12px; color: var(--text-dim);
  text-align: center;
}
</style>
</head>
<body>

<header>
  <div class="brand">
    <div class="brand-icon">⬡</div>
    <div>
      <div class="brand-text">DataLake Explorer</div>
      <div class="brand-sub">Pharma Commercial · Gold Layer</div>
    </div>
  </div>
  <div class="search-wrap">
    <span class="search-icon">⌕</span>
    <input type="text" id="search-input" placeholder="Search tables, columns, descriptions…">
  </div>
  <div class="header-stats">
    <div class="stat-pill"><span>50</span> tables</div>
    <div class="stat-pill"><span>5</span> categories</div>
    <span class="platform-badge db-badge">Databricks</span>
    <span class="platform-badge sf-badge">Snowflake</span>
    <button id="flow-nav-btn" style="margin-left:18px;padding:6px 14px;border-radius:6px;border:1px solid var(--border-2);background:var(--surface-2);color:var(--text);font-family:var(--font-mono);font-size:12px;cursor:pointer;">🔗 System Flow</button>
    <button id="mode-toggle" style="margin-left:8px;padding:6px 14px;border-radius:6px;border:1px solid var(--border-2);background:var(--surface-2);color:var(--text);font-family:var(--font-mono);font-size:12px;cursor:pointer;">🌞/🌙</button>
  </div>
</header>

<div class="layout">
  <aside class="sidebar" id="sidebar"></aside>
  <main class="main" id="main-content">
    <div id="welcome"></div>
    <div id="table-detail"></div>
    <div id="system-flow" style="display:none;padding:32px 0 0 0;width:100%;"></div>
  </main>
</div>

<script>
// --- System Flow Navigation ---
document.addEventListener('DOMContentLoaded', () => {
  const flowBtn = document.getElementById('flow-nav-btn');
  if (flowBtn) {
    flowBtn.onclick = () => {
      document.getElementById('main-content').scrollTop = 0;
      document.getElementById('system-flow').style.display = '';
      document.getElementById('welcome').style.display = 'none';
      document.getElementById('table-detail').style.display = 'none';
      buildSystemFlow();
    };
  }
});

function showExplorer() {
  document.getElementById('system-flow').style.display = 'none';
  document.getElementById('welcome').style.display = '';
  document.getElementById('table-detail').style.display = 'none';
}

// --- System Flow Diagram ---
function buildSystemFlow() {
  const flowDiv = document.getElementById('system-flow');
  const order = ['dimension','fact','mapping','metric_monthly','metric_quarterly'];
  const groups = {};
  order.forEach(c => { groups[c] = []; });
  Object.keys(TABLES).forEach(id => {
    const c = TABLES[id].category;
    if (groups[c]) groups[c].push(id);
  });

  // Layout constants
  const NODE_W = 180, NODE_H = 42, NODE_RX = 8;
  const COL_W = 220;
  const ROW_H = 58;
  const HEADER_H = 54;
  const PAD_TOP = 16, PAD_BOT = 24, PAD_SIDES = 20;

  const maxRows = Math.max(...order.map(cat => groups[cat].length));
  const W = order.length * COL_W + PAD_SIDES * 2;
  const H = maxRows * ROW_H + HEADER_H + PAD_TOP + PAD_BOT;

  // Node centre positions
  const nodePos = {};
  order.forEach((cat, ci) => {
    const laneX = PAD_SIDES + ci * COL_W + COL_W / 2;
    groups[cat].forEach((id, ri) => {
      nodePos[id] = { x: laneX, y: HEADER_H + PAD_TOP + ri * ROW_H + NODE_H / 2, cat };
    });
  });

  // Build full edge list: FK rels + derivedFrom (fact → metric)
  const edgeSet = {};
  RELS.forEach(r => {
    if (nodePos[r.f] && nodePos[r.t]) {
      const key = r.f + '|' + r.t;
      if (!edgeSet[key]) edgeSet[key] = { from: r.f, to: r.t, type: 'fk' };
    }
  });
  Object.keys(TABLES).forEach(id => {
    const derived = TABLES[id].derivedFrom || [];
    derived.forEach(src => {
      if (nodePos[src] && nodePos[id]) {
        const key = src + '|' + id;
        if (!edgeSet[key]) edgeSet[key] = { from: src, to: id, type: 'derived' };
      }
    });
  });
  const edges = Object.values(edgeSet);

  // Index edges by node for fast lookup
  const edgesFrom = {}, edgesTo = {};
  edges.forEach((e, i) => {
    (edgesFrom[e.from] = edgesFrom[e.from] || []).push(i);
    (edgesTo[e.to]   = edgesTo[e.to]   || []).push(i);
  });

  // Edge path helper
  function edgePath(e) {
    const a = nodePos[e.from], b = nodePos[e.to];
    const x1 = a.x, y1 = a.y, x2 = b.x, y2 = b.y;
    if (Math.abs(x1 - x2) < 4) {
      const mx = x1 + COL_W * 0.38;
      return 'M ' + x1 + ' ' + y1 + ' C ' + mx + ' ' + y1 + ', ' + mx + ' ' + y2 + ', ' + x2 + ' ' + y2;
    }
    const dx = x2 - x1;
    return 'M ' + x1 + ' ' + y1
      + ' C ' + (x1 + dx * 0.45) + ' ' + y1 + ', ' + (x2 - dx * 0.45) + ' ' + y2 + ', ' + x2 + ' ' + y2;
  }

  // ── Build SVG ──────────────────────────────────────────────────────────
  let svg = '<svg id="sf-svg" width="' + W + '" height="' + H + '" xmlns="http://www.w3.org/2000/svg"'
    + ' style="display:block;font-family:var(--font-mono);">';

  svg += '<defs>';
  // Arrowhead markers per category color + a grey default
  [...Object.values(CATS).map(c => c.color), '#94A3B8'].forEach((col, i) => {
    const mid = 'arr' + i;
    svg += '<marker id="' + mid + '" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">'
      + '<polygon points="0 0, 8 3, 0 6" fill="' + col + '"/>'
      + '</marker>';
  });
  svg += '<filter id="sf-shadow" x="-20%" y="-20%" width="140%" height="140%">'
    + '<feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.12"/>'
    + '</filter>';
  svg += '</defs>';

  // ── Lane backgrounds & headers ─────────────────────────────────────────
  order.forEach((cat, ci) => {
    const color = getCatColor(cat);
    const laneX = PAD_SIDES + ci * COL_W;
    svg += '<rect x="' + laneX + '" y="0" width="' + COL_W + '" height="' + H + '"'
      + ' fill="' + color + '" fill-opacity="' + (ci % 2 === 0 ? '0.03' : '0.015') + '"/>';
    if (ci > 0)
      svg += '<line x1="' + laneX + '" y1="0" x2="' + laneX + '" y2="' + H + '"'
        + ' stroke="' + color + '" stroke-opacity="0.12" stroke-width="1"/>';
    const hx = laneX + 10, hy = 8, hw = COL_W - 20, hh = HEADER_H - 16;
    svg += '<rect x="' + hx + '" y="' + hy + '" width="' + hw + '" height="' + hh + '"'
      + ' rx="10" fill="' + color + '" fill-opacity="0.12"'
      + ' stroke="' + color + '" stroke-width="1.5" stroke-opacity="0.35"/>';
    const lbl = getCatLabel(cat);
    svg += '<text x="' + (hx + hw / 2) + '" y="' + (hy + hh / 2 + 1) + '"'
      + ' text-anchor="middle" dominant-baseline="middle" font-size="11" font-weight="700"'
      + ' letter-spacing="0.06em" fill="' + color + '" opacity="0.9">'
      + (lbl.length > 16 ? lbl.slice(0,15)+'…' : lbl).toUpperCase() + '</text>';
    svg += '<text x="' + (hx + hw - 8) + '" y="' + (hy + 9) + '"'
      + ' text-anchor="end" font-size="9" font-weight="600" fill="' + color + '" opacity="0.65">'
      + groups[cat].length + '</text>';
  });

  // ── Edge layer (all hidden by default) ────────────────────────────────
  svg += '<g id="sf-edges">';
  edges.forEach((e, i) => {
    const fromColor = getCatColor(TABLES[e.from]?.category);
    const isDerived = e.type === 'derived';
    // Find marker index matching this color
    const catColors = Object.values(CATS).map(c => c.color);
    const mIdx = catColors.indexOf(fromColor);
    const markerId = mIdx >= 0 ? 'arr' + mIdx : 'arr' + catColors.length;
    svg += '<path id="sf-edge-' + i + '"'
      + ' d="' + edgePath(e) + '"'
      + ' fill="none"'
      + ' stroke="' + fromColor + '"'
      + ' stroke-width="' + (isDerived ? '1.5' : '1.5') + '"'
      + ' stroke-opacity="0"'
      + (isDerived ? ' stroke-dasharray="5,3"' : '')
      + ' marker-end="url(#' + markerId + ')"'
      + ' data-from="' + e.from + '" data-to="' + e.to + '"'
      + ' style="transition:stroke-opacity 0.2s,stroke-width 0.2s;pointer-events:none;"/>';
  });
  svg += '</g>';

  // ── Nodes ─────────────────────────────────────────────────────────────
  svg += '<g id="sf-nodes">';
  Object.keys(nodePos).forEach(id => {
    const n = nodePos[id];
    const color = getCatColor(n.cat);
    const rx = n.x - NODE_W / 2, ry = n.y - NODE_H / 2;
    const label = id.length > 20 ? id.slice(0, 19) + '…' : id;
    svg += '<g class="flow-node" id="sfn-' + id + '" data-id="' + id + '" style="cursor:pointer">';
    svg += '<rect class="sfn-shadow" x="' + rx + '" y="' + ry + '" width="' + NODE_W + '" height="' + NODE_H + '"'
      + ' rx="' + NODE_RX + '" fill="' + color + '" fill-opacity="0.06" stroke="none" filter="url(#sf-shadow)"/>';
    svg += '<rect class="sfn-bg" x="' + rx + '" y="' + ry + '" width="' + NODE_W + '" height="' + NODE_H + '"'
      + ' rx="' + NODE_RX + '" fill="' + color + '" fill-opacity="0.10"'
      + ' stroke="' + color + '" stroke-width="1.5" style="transition:fill-opacity 0.15s,stroke-width 0.15s;"/>';
    svg += '<rect x="' + rx + '" y="' + ry + '" width="4" height="' + NODE_H + '"'
      + ' rx="' + NODE_RX + '" fill="' + color + '" fill-opacity="0.6"/>';
    svg += '<rect x="' + rx + '" y="' + (ry + NODE_RX) + '" width="4" height="' + (NODE_H - NODE_RX) + '"'
      + ' fill="' + color + '" fill-opacity="0.6"/>';
    svg += '<text x="' + (rx + 14) + '" y="' + (n.y + 1) + '"'
      + ' dominant-baseline="middle" font-size="11.5" font-weight="600"'
      + ' fill="' + color + '" letter-spacing="-0.01em" style="pointer-events:none;">' + label + '</text>';
    svg += '</g>';
  });
  svg += '</g>';
  svg += '</svg>';

  // ── Wrapper ────────────────────────────────────────────────────────────
  flowDiv.innerHTML =
    '<div style="display:flex;align-items:center;gap:16px;padding:0 32px 20px;flex-wrap:wrap;">'
    + '<button onclick="showExplorer()" style="padding:7px 16px;border-radius:6px;border:1px solid var(--border-2);background:var(--surface-2);color:var(--text);font-family:var(--font-mono);font-size:12px;cursor:pointer;flex-shrink:0;">← Back</button>'
    + '<div style="font-family:var(--font-mono);font-size:13px;font-weight:600;color:var(--text);">System Flow</div>'
    + '<div style="font-size:12px;color:var(--text-muted);">Click a node to reveal its connections · Click again or click background to clear</div>'
    + '<div style="margin-left:auto;display:flex;gap:10px;align-items:center;flex-wrap:wrap;">'
    + '<span style="font-size:10px;color:var(--text-dim);font-family:var(--font-mono);">── FK &nbsp;&nbsp;╌╌ derived</span>'
    + Object.entries(CATS).map(([k,v]) =>
        '<span style="display:inline-flex;align-items:center;gap:5px;font-size:10px;font-family:var(--font-mono);color:' + v.color + ';">'
        + '<span style="width:8px;height:8px;border-radius:2px;background:' + v.color + ';display:inline-block;opacity:0.85;"></span>'
        + v.label.toUpperCase() + '</span>'
      ).join('')
    + '</div>'
    + '</div>'
    + '<div style="overflow-x:auto;padding:0 32px 32px;">' + svg + '</div>';

  // ── Interaction ────────────────────────────────────────────────────────
  setTimeout(() => {
    const svgEl = document.getElementById('sf-svg');
    let activeNode = null;

    function dimAll() {
      // Fade all nodes slightly
      document.querySelectorAll('.flow-node .sfn-bg').forEach(r => {
        r.style.fillOpacity = '0.04';
        r.style.strokeOpacity = '0.3';
      });
      // Hide all edges
      document.querySelectorAll('[id^="sf-edge-"]').forEach(p => {
        p.style.strokeOpacity = '0';
      });
    }

    function resetAll() {
      document.querySelectorAll('.flow-node .sfn-bg').forEach(r => {
        r.style.fillOpacity = '0.10';
        r.style.strokeOpacity = '1';
        r.style.strokeWidth = '1.5';
      });
      document.querySelectorAll('[id^="sf-edge-"]').forEach(p => {
        p.style.strokeOpacity = '0';
      });
      activeNode = null;
    }

    function activateNode(id) {
      activeNode = id;
      dimAll();

      // Collect connected indices
      const outIdx = edgesFrom[id] || [];
      const inIdx  = edgesTo[id]   || [];
      const allIdx = [...outIdx, ...inIdx];

      // Connected node ids
      const connectedIds = new Set([id]);
      allIdx.forEach(i => { connectedIds.add(edges[i].from); connectedIds.add(edges[i].to); });

      // Highlight connected nodes
      connectedIds.forEach(nid => {
        const bg = document.querySelector('#sfn-' + CSS.escape(nid) + ' .sfn-bg');
        if (bg) { bg.style.fillOpacity = '0.22'; bg.style.strokeOpacity = '1'; bg.style.strokeWidth = '2.5'; }
      });

      // Show edges
      allIdx.forEach(i => {
        const pathEl = document.getElementById('sf-edge-' + i);
        if (pathEl) pathEl.style.strokeOpacity = '0.75';
      });
    }

    // Node click
    document.querySelectorAll('.flow-node').forEach(g => {
      g.addEventListener('mouseenter', () => {
        if (activeNode) return;
        const bg = g.querySelector('.sfn-bg');
        if (bg) bg.style.fillOpacity = '0.20';
      });
      g.addEventListener('mouseleave', () => {
        if (activeNode) return;
        const bg = g.querySelector('.sfn-bg');
        if (bg) bg.style.fillOpacity = '0.10';
      });
      g.addEventListener('click', (ev) => {
        ev.stopPropagation();
        const id = g.getAttribute('data-id');
        if (activeNode === id) { resetAll(); return; }
        activateNode(id);
      });
    });

    // Click SVG background to clear
    svgEl.addEventListener('click', () => { resetAll(); });

  }, 0);
}
// --- Light/Dark Mode Toggle ---
const modeToggle = () => {
  document.body.classList.toggle('dark-mode');
  localStorage.setItem('explorer-mode', document.body.classList.contains('dark-mode') ? 'dark' : 'light');
  document.getElementById('mode-toggle').textContent = document.body.classList.contains('dark-mode') ? '🌙' : '🌞';
};
window.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('mode-toggle');
  if (btn) {
    btn.onclick = modeToggle;
    // Set initial mode from localStorage
    const saved = localStorage.getItem('explorer-mode');
    if (saved === 'dark') {
      document.body.classList.add('dark-mode');
      btn.textContent = '🌙';
    } else {
      document.body.classList.remove('dark-mode');
      btn.textContent = '🌞';
    }
  }
});
/* ─── DATA ──────────────────────────────────────────────────────────── */

const CATS = {
  dimension: { label:'Dimensions', color:'#4F8EF7', desc:'Master & reference data — the "who, what, where" of the datalake.' },
  fact:      { label:'Facts',      color:'#F5A623', desc:'Transactional & event-level records from source systems (CRM, IQVIA, DDD).' },
  metric_monthly:   { label:'Monthly Metrics',   color:'#2DD4BF', desc:'KPIs aggregated at monthly grain for field force & commercial performance.' },
  metric_quarterly: { label:'Quarterly Metrics', color:'#818CF8', desc:'KPIs aggregated at quarterly grain — business review cadence.' },
  mapping:   { label:'Mapping / Bridge', color:'#F472B6', desc:'Lookup and bridge tables resolving many-to-many relationships.' },
};

// role: pk | fk | ak | measure | attribute | flag | temporal | system
const TABLES = {
  /* ── DIMENSIONS ───────────────────────────────────────────────────── */
  dim_rep_master: {
    category: 'dimension',
    description: 'Master registry of all field sales representatives. Captures identity, role hierarchy (Territory Manager, District Manager, etc.) and employment status. Central lookup for all rep-level CRM activity and performance attribution. Slowly-changing in nature — refreshed when reps join, leave, or change roles.',
    primaryKey: ['rep_id'],
    columns: [
      {n:'rep_id',          r:'pk',        d:'Unique internal rep identifier (surrogate key).'},
      {n:'rep_first_name',  r:'attribute', d:'Rep\'s first name.'},
      {n:'rep_last_name',   r:'attribute', d:'Rep\'s last name.'},
      {n:'rep_email_id',    r:'ak',        d:'Corporate email — alternate unique identifier.'},
      {n:'rep_role',        r:'attribute', d:'Salesforce role: e.g. Territory Manager, District Manager, Regional Business Director.'},
      {n:'status',          r:'attribute', d:'Employment status: Active / Inactive. Drives inclusion in reporting periods.'},
      {n:'sys_load_timestamp',r:'system',  d:'ETL load timestamp.'},
      {n:'source_file',     r:'system',    d:'Source file name that populated this record.'},
      {n:'data_date',       r:'system',    d:'Effective date of the record snapshot.'},
    ]
  },
  dim_prescriber: {
    category: 'dimension',
    description: 'Master registry of Healthcare Providers (HCPs) targeted by the sales force. Each prescriber carries a unique NPI (National Provider Identifier) used to cross-reference IQVIA Rx data. Tier classification drives call frequency targets and sampling strategy.',
    primaryKey: ['prescriber_id'],
    columns: [
      {n:'prescriber_id',     r:'pk',        d:'Internal HCP surrogate key.'},
      {n:'npi_id',            r:'ak',        d:'National Provider Identifier — universal HCP identifier for IQVIA data joins.'},
      {n:'prescriber_name',   r:'attribute', d:'Full name of the HCP.'},
      {n:'speciality',        r:'attribute', d:'Medical specialty (e.g. Cardiology, Internal Medicine). Used for specialty-level market share cuts.'},
      {n:'practice_type',     r:'attribute', d:'Practice setting: solo, group, hospital-affiliated, etc.'},
      {n:'prescriber_tier',   r:'attribute', d:'Commercial targeting tier (Tier 1/2/3) based on Rx volume and potential.'},
      {n:'prescriber_email',  r:'attribute', d:'HCP\'s email — used for digital/VAE engagement.'},
      {n:'prescriber_phone',  r:'attribute', d:'Practice contact number.'},
      {n:'practice_id',       r:'attribute', d:'Practice group identifier — links HCP to their affiliated practice.'},
      {n:'sys_load_timestamp',r:'system',    d:'ETL load timestamp.'},
      {n:'source_file',       r:'system',    d:'Source file name.'},
      {n:'data_date',         r:'system',    d:'Snapshot effective date.'},
    ]
  },
  dim_product: {
    category: 'dimension',
    description: 'Product catalog covering both company-promoted brands and competitor molecules tracked in the market. The company_flag column is critical — it distinguishes our products from market competitors. NDC-11 codes serve as universal cross-reference keys to IQVIA and DDD datasets.',
    primaryKey: ['product_id'],
    columns: [
      {n:'product_id',         r:'pk',        d:'Internal product surrogate key.'},
      {n:'ndc11',              r:'ak',        d:'National Drug Code (11-digit). Universal identifier for IQVIA and DDD joins.'},
      {n:'brand_name',         r:'attribute', d:'Branded product name (e.g. Lipitor).'},
      {n:'generic_name',       r:'attribute', d:'INN/generic molecule name (e.g. atorvastatin).'},
      {n:'manufacturer',       r:'attribute', d:'Pharmaceutical manufacturer name.'},
      {n:'atc_code',           r:'attribute', d:'WHO Anatomical Therapeutic Chemical code — enables therapeutic class grouping.'},
      {n:'company_flag',       r:'flag',      d:'"Y" = company product, "N" = competitor. Pivotal for market share numerator/denominator logic.'},
      {n:'price_per_unit_usd', r:'measure',   d:'List price per dispensing unit in USD.'},
      {n:'price_type',         r:'attribute', d:'Pricing basis: WAC, AWP, etc.'},
      {n:'sys_load_timestamp', r:'system',    d:'ETL load timestamp.'},
      {n:'source_file',        r:'system',    d:'Source file name.'},
      {n:'data_date',          r:'system',    d:'Snapshot effective date.'},
    ]
  },
  dim_geography: {
    category: 'dimension',
    description: 'Zip-code level geographic master with lat/lng coordinates for mapping. The geo_index and geos_in_zip fields handle multi-territory zip overlaps — critical for accurate spillover analysis. This table is the geographic foundation for all territory alignment and Rx attribution.',
    primaryKey: ['geo_id'],
    columns: [
      {n:'geo_id',        r:'pk',        d:'Internal geography surrogate key.'},
      {n:'zip_code',      r:'ak',        d:'5-digit US ZIP code — alternate key for IQVIA data joins.'},
      {n:'city',          r:'attribute', d:'City name.'},
      {n:'state',         r:'attribute', d:'State abbreviation (2-char).'},
      {n:'state_id',      r:'attribute', d:'State numeric FIPS code.'},
      {n:'region',        r:'attribute', d:'Sales region grouping (e.g. Northeast, Southeast).'},
      {n:'lat',           r:'measure',   d:'Latitude coordinate for mapping.'},
      {n:'lng',           r:'measure',   d:'Longitude coordinate for mapping.'},
      {n:'population',    r:'measure',   d:'ZIP population — used as sizing variable for territory potential models.'},
      {n:'geo_index',     r:'attribute', d:'Internal geographic index value.'},
      {n:'geos_in_zip',   r:'measure',   d:'Count of territory geos sharing this ZIP — indicates multi-territory overlap situations.'},
      {n:'sys_load_timestamp',r:'system',d:'ETL load timestamp.'},
      {n:'source_file',   r:'system',    d:'Source file name.'},
      {n:'data_date',     r:'system',    d:'Snapshot effective date.'},
    ]
  },
  dim_clm_content: {
    category: 'dimension',
    description: 'Library of all Closed Loop Marketing (CLM) digital sales aid files used by reps during HCP calls. Tracks versioning, language, channel, and approval status. Used to measure content performance (engagement duration, skip rate) and ensure reps are using the latest approved materials.',
    primaryKey: ['clm_file_id'],
    columns: [
      {n:'product_id',       r:'fk',       d:'FK → dim_product. CLM content is product-specific.'},
      {n:'clm_file_id',      r:'pk',       d:'Unique CLM content file identifier.'},
      {n:'clm_file_name',    r:'attribute',d:'Display name of the sales aid (e.g. "MOA Slide Deck v2").'},
      {n:'clm_file_type',    r:'attribute',d:'Content type: PDF, HTML, Video, Slide deck.'},
      {n:'clm_file_version', r:'attribute',d:'Version number — tracks content lifecycle and update cycles.'},
      {n:'clm_file_language',r:'attribute',d:'Language of the content (for multi-lingual deployments).'},
      {n:'clm_file_channel', r:'attribute',d:'Intended delivery channel: field, virtual, email.'},
      {n:'clm_file_status',  r:'attribute',d:'Approval status: Active / Retired / Under Review.'},
      {n:'sys_load_timestamp',r:'system',  d:'ETL load timestamp.'},
      {n:'source_file',      r:'system',   d:'Source file name.'},
      {n:'data_date',        r:'system',   d:'Snapshot effective date.'},
    ]
  },
  dim_territory_alignment: {
    category: 'dimension',
    description: 'Maps each sales rep to their assigned territories and geographies. This is a slowly-changing dimension — updated during annual (or mid-cycle) territory realignment exercises. Essential for correctly routing Rx data, call data, and sales revenue to the responsible rep and territory.',
    primaryKey: ['geo_id','territory_id','rep_id'],
    columns: [
      {n:'geo_id',         r:'fk',       d:'FK → dim_geography. The geography unit assigned to this rep/territory.'},
      {n:'territory_id',   r:'pk',       d:'Territory identifier (part of composite PK). Logical sales territory grouping.'},
      {n:'rep_id',         r:'fk',       d:'FK → dim_rep_master. The rep responsible for this territory geo.'},
      {n:'rep_role',       r:'attribute',d:'Rep role in this territory assignment (denormalized from dim_rep_master).'},
      {n:'sys_load_timestamp',r:'system',d:'ETL load timestamp.'},
      {n:'source_file',    r:'system',   d:'Source file name.'},
      {n:'data_date',      r:'system',   d:'Effective date — critical for point-in-time territory reporting.'},
    ]
  },
  dim_prescriber_geo_mapping: {
    category: 'dimension',
    description: 'Resolves the many-to-many relationship between prescribers (who may practice at multiple locations) and geographies. The primary_flag identifies the main practice, enabling accurate Rx attribution to a territory even when an HCP straddles multiple zip codes.',
    primaryKey: ['prescriber_id','geo_id'],
    columns: [
      {n:'prescriber_id',          r:'fk',       d:'FK → dim_prescriber. The HCP being mapped.'},
      {n:'geo_id',                 r:'fk',       d:'FK → dim_geography. The geography where this prescriber practices.'},
      {n:'primary_flag',           r:'flag',     d:'"Y" = primary practice location. Used to avoid double-counting Rx across territories.'},
      {n:'practice_name',          r:'attribute',d:'Name of the practice at this geographic location.'},
      {n:'practice_address_line_1',r:'attribute',d:'Street address of this practice location.'},
      {n:'sys_load_timestamp',     r:'system',   d:'ETL load timestamp.'},
      {n:'source_file',            r:'system',   d:'Source file name.'},
      {n:'data_date',              r:'system',   d:'Snapshot effective date.'},
    ]
  },

  /* ── FACTS ────────────────────────────────────────────────────────── */
  fact_call_activity: {
    category: 'fact',
    description: 'Core CRM fact table — every field call logged by a sales rep. Captures the complete call context: who visited whom, which product was detailed, samples dropped, call notes, outcome, and key messages. Source system is the CRM (typically Veeva CRM). This is the primary input for all rep activity and field force productivity metrics.',
    primaryKey: ['call_id'],
    columns: [
      {n:'monthly_call_plan_id', r:'fk',       d:'FK → fact_call_plan. Links execution (actual call) to plan (targeted call).'},
      {n:'call_id',              r:'pk',        d:'Unique call event identifier.'},
      {n:'rep_id',               r:'fk',        d:'FK → dim_rep_master. The rep who made the call.'},
      {n:'prescriber_id',        r:'fk',        d:'FK → dim_prescriber. The HCP visited.'},
      {n:'geo_id',               r:'fk',        d:'FK → dim_geography. Geography where the call occurred.'},
      {n:'prescriber_name',      r:'attribute', d:'Denormalized HCP name at time of call.'},
      {n:'prescriber_specialty', r:'attribute', d:'Denormalized HCP specialty at time of call.'},
      {n:'prescriber_grade',     r:'attribute', d:'Targeting grade/decile at time of call.'},
      {n:'prescriber_phone',     r:'attribute', d:'HCP phone number at time of call.'},
      {n:'prescriber_email',     r:'attribute', d:'HCP email at time of call.'},
      {n:'practice_id',          r:'attribute', d:'Practice identifier (denormalized).'},
      {n:'practice_name',        r:'attribute', d:'Practice name at time of call.'},
      {n:'practice_type',        r:'attribute', d:'Practice setting at time of call.'},
      {n:'practice_address_line1',r:'attribute',d:'Practice street address.'},
      {n:'practice_city',        r:'attribute', d:'Practice city.'},
      {n:'practice_state',       r:'attribute', d:'Practice state.'},
      {n:'practice_zip',         r:'attribute', d:'Practice ZIP code.'},
      {n:'call_date',            r:'temporal',  d:'Date of the call.'},
      {n:'call_start_timestamp', r:'temporal',  d:'Exact start time — used for call duration calculation.'},
      {n:'call_end_timestamp',   r:'temporal',  d:'Exact end time.'},
      {n:'call_duration_minutes',r:'measure',   d:'Total call duration in minutes. Input to avg_interaction_time metrics.'},
      {n:'call_submission_timestamp',r:'temporal',d:'When the call was submitted in CRM. Gap vs call_date flags backdating.'},
      {n:'product_id',           r:'fk',        d:'FK → dim_product. Primary product detailed in this call.'},
      {n:'ndc11',                r:'fk',        d:'FK → dim_product (via ndc11). NDC of the detailed product.'},
      {n:'brand_name',           r:'attribute', d:'Denormalized brand name.'},
      {n:'sample_dropped_flag',  r:'flag',      d:'"Y" if product samples were left with HCP. Input to sample_script_ratio.'},
      {n:'call_objective',       r:'attribute', d:'Pre-set call goal (e.g. efficacy discussion, patient case review).'},
      {n:'call_notes',           r:'attribute', d:'Free-text rep notes from the call.'},
      {n:'key_message_delivered',r:'attribute', d:'Which approved key message was delivered (e.g. safety, efficacy, dosing).'},
      {n:'call_outcome',         r:'attribute', d:'Result of the call: Successful, No Access, Left Samples Only, etc.'},
      {n:'next_action',          r:'attribute', d:'Planned follow-up action logged by the rep.'},
      {n:'sys_load_timestamp',   r:'system',    d:'ETL load timestamp.'},
      {n:'source_file',          r:'system',    d:'Source file name.'},
      {n:'data_date',            r:'system',    d:'Snapshot effective date.'},
    ]
  },
  fact_call_plan: {
    category: 'fact',
    description: 'Monthly call planning targets per rep-prescriber-product combination. Captures what calls each rep planned to make — the "plan" side of the plan vs. actual picture. The monthly_call_plan_id is the bridge key to fact_call_activity, enabling call plan attainment and frequency attainment metrics.',
    primaryKey: ['monthly_call_plan_id'],
    columns: [
      {n:'monthly_call_plan_id',      r:'pk',       d:'Unique plan record identifier — FK anchor for fact_call_activity.'},
      {n:'rep_id',                    r:'fk',       d:'FK → dim_rep_master. Rep this plan belongs to.'},
      {n:'prescriber_id',             r:'fk',       d:'FK → dim_prescriber. Targeted HCP for this plan.'},
      {n:'geo_id',                    r:'fk',       d:'FK → dim_geography. Geography of the planned call.'},
      {n:'product_id',                r:'fk',       d:'FK → dim_product. Product to be detailed.'},
      {n:'plan_year',                 r:'temporal', d:'Calendar year of the plan.'},
      {n:'plan_month',                r:'temporal', d:'Calendar month of the plan (1–12).'},
      {n:'plan_quarter',              r:'temporal', d:'Derived quarter (Q1–Q4).'},
      {n:'planned_calls_month',       r:'measure',  d:'Number of calls planned for this rep-HCP-product in the month.'},
      {n:'plan_created_date',         r:'temporal', d:'Date plan was finalized.'},
      {n:'plan_last_updated_date',    r:'temporal', d:'Last modification date — flags mid-cycle plan changes.'},
      {n:'target_call_duration_minutes',r:'measure',d:'Expected call duration target in minutes.'},
      {n:'sys_load_timestamp',        r:'system',   d:'ETL load timestamp.'},
      {n:'source_file',               r:'system',   d:'Source file name.'},
      {n:'data_date',                 r:'system',   d:'Snapshot effective date.'},
    ]
  },
  fact_clm_activity: {
    category: 'fact',
    description: 'Granular Closed Loop Marketing (CLM) engagement log — records how each piece of digital sales aid content was used within a call. Enriches fact_call_activity with content-level detail: how long each slide was shown, whether it was skipped, revisited, zoomed, or had video played. Source: Veeva CRM CLM module.',
    primaryKey: ['clm_activity_id'],
    columns: [
      {n:'clm_activity_id',             r:'pk',       d:'Unique CLM engagement event identifier.'},
      {n:'call_id',                     r:'fk',       d:'FK → fact_call_activity. The parent call this CLM event belongs to.'},
      {n:'rep_id',                      r:'fk',       d:'FK → dim_rep_master.'},
      {n:'prescriber_id',               r:'fk',       d:'FK → dim_prescriber.'},
      {n:'practice_id',                 r:'attribute',d:'Practice identifier (denormalized).'},
      {n:'geo_id',                      r:'fk',       d:'FK → dim_geography.'},
      {n:'product_id',                  r:'fk',       d:'FK → dim_product. Product the content relates to.'},
      {n:'brand_name',                  r:'attribute',d:'Denormalized brand name.'},
      {n:'clm_file_id',                 r:'fk',       d:'FK → dim_clm_content. The specific content file shown.'},
      {n:'clm_file_name',               r:'attribute',d:'Denormalized content file name.'},
      {n:'clm_display_start_timestamp', r:'temporal', d:'When this content item began displaying.'},
      {n:'clm_display_end_timestamp',   r:'temporal', d:'When this content item stopped displaying.'},
      {n:'clm_display_duration_seconds',r:'measure',  d:'Total seconds this content was on screen. Core CLM engagement measure.'},
      {n:'call_date',                   r:'temporal', d:'Date of the parent call.'},
      {n:'call_type',                   r:'attribute',d:'In-person vs. virtual.'},
      {n:'virtual_call_flag',           r:'flag',     d:'"Y" if conducted via phone/video.'},
      {n:'clm_skipped_flag',            r:'flag',     d:'"Y" if content was skipped without full display — signals low engagement.'},
      {n:'clm_revisited_flag',          r:'flag',     d:'"Y" if HCP asked rep to go back to this content.'},
      {n:'clm_zoom_used_flag',          r:'flag',     d:'"Y" if rep zoomed in on the content during display.'},
      {n:'clm_video_played_flag',       r:'flag',     d:'"Y" if embedded video was played.'},
      {n:'consent_captured_flag',       r:'flag',     d:'"Y" if HCP consent was digitally captured during this call.'},
      {n:'device_id',                   r:'attribute',d:'Rep\'s tablet/device ID used for the call.'},
      {n:'offline_flag',                r:'flag',     d:'"Y" if call was logged offline and synced later.'},
      {n:'clm_record_created_timestamp',r:'temporal', d:'When the CLM record was created in the source system.'},
      {n:'sys_load_timestamp',          r:'system',   d:'ETL load timestamp.'},
      {n:'source_file',                 r:'system',   d:'Source file name.'},
      {n:'data_date',                   r:'system',   d:'Snapshot effective date.'},
    ]
  },
  fact_digital_engagement: {
    category: 'fact',
    description: 'Virtual Account Engagement (VAE) / email tracking. Records every email sent by a rep to a prescriber and captures open events, click-throughs, timing, and engagement patterns. Complements field call activity with the digital channel, feeding into VAE open-rate metrics used in omnichannel performance measurement.',
    primaryKey: ['email_interaction_id'],
    columns: [
      {n:'email_interaction_id',r:'pk',       d:'Unique email interaction identifier.'},
      {n:'rep_id',              r:'fk',       d:'FK → dim_rep_master. Rep who sent the email.'},
      {n:'rep_email',           r:'attribute',d:'Sender email (denormalized for audit trail).'},
      {n:'prescriber_id',       r:'fk',       d:'FK → dim_prescriber. Recipient HCP.'},
      {n:'prescriber_tier',     r:'attribute',d:'HCP tier at time of send (denormalized).'},
      {n:'subject_topic',       r:'attribute',d:'Email topic / subject line category (approved messaging).'},
      {n:'sent_timestamp',      r:'temporal', d:'When the email was sent.'},
      {n:'is_opened',           r:'flag',     d:'"1" if the email was opened by the HCP.'},
      {n:'open_timestamp',      r:'temporal', d:'Timestamp of first open event.'},
      {n:'is_clicked',          r:'flag',     d:'"1" if a link was clicked within the email.'},
      {n:'click_timestamp',     r:'temporal', d:'Timestamp of first click event.'},
      {n:'engagement_day',      r:'temporal', d:'Day of week of open/click event — used for send-time optimization.'},
      {n:'engagement_hour',     r:'temporal', d:'Hour of day of engagement — used for send-time optimization.'},
      {n:'sys_load_timestamp',  r:'system',   d:'ETL load timestamp.'},
      {n:'source_file',         r:'system',   d:'Source file name.'},
      {n:'data_date',           r:'system',   d:'Snapshot effective date.'},
    ]
  },
  fact_xponents_rx: {
    category: 'fact',
    description: 'IQVIA Xponent® prescription data — the gold standard for measuring prescriber-level Rx behavior. Weekly TRx (Total Prescriptions) and NRx (New Prescriptions) by prescriber, product, and geography. This is the primary numerator for all market share, growth, and HCP-level Rx metrics. The our_product flag enables competitor Rx tracking in the same table.',
    primaryKey: ['week_end_date','prescriber_id','product_id','geo_id'],
    columns: [
      {n:'week_end_date',  r:'pk',      d:'Week ending date (Saturday). Part of composite PK.'},
      {n:'prescriber_id',  r:'fk',      d:'FK → dim_prescriber. Part of composite PK.'},
      {n:'product_id',     r:'fk',      d:'FK → dim_product. Part of composite PK.'},
      {n:'geo_id',         r:'fk',      d:'FK → dim_geography. Part of composite PK.'},
      {n:'trx_units',      r:'measure', d:'Total Rx units (new + refills) dispensed in this week.'},
      {n:'new_rx_units',   r:'measure', d:'New Rx units only (NRx) — excludes refills.'},
      {n:'our_product',    r:'flag',    d:'"Y" = company product. Allows competitor Rx to be stored in same table for market share calc.'},
      {n:'data_date',      r:'system',  d:'IQVIA data date (typically lags by ~2 weeks).'},
      {n:'source_file',    r:'system',  d:'Source file name.'},
      {n:'sys_load_timestamp',r:'system',d:'ETL load timestamp.'},
    ]
  },
  fact_iqvia_sales: {
    category: 'fact',
    description: 'IQVIA market-level sales data at geography and channel granularity. Provides the total market denominator for market share calculations. Also captures competitor product performance via the company_flag. Key distinction from Xponent: this is geography-level (not prescriber-level) and includes sales revenue alongside Rx volume.',
    primaryKey: ['week_end_date','ndc11','geo_id','channel_desc'],
    columns: [
      {n:'week_end_date',  r:'pk',      d:'Week ending date. Part of composite PK.'},
      {n:'year',           r:'temporal',d:'Calendar year (derived from week_end_date).'},
      {n:'ndc11',          r:'fk',      d:'FK → dim_product (via ndc11). Part of composite PK.'},
      {n:'product_id',     r:'fk',      d:'FK → dim_product. Surrogate key join.'},
      {n:'brand_name',     r:'attribute',d:'Denormalized brand name.'},
      {n:'generic_name',   r:'attribute',d:'Denormalized generic name.'},
      {n:'manufacturer',   r:'attribute',d:'Denormalized manufacturer.'},
      {n:'atc_code',       r:'attribute',d:'Denormalized ATC therapeutic code.'},
      {n:'geo_id',         r:'fk',      d:'FK → dim_geography. Part of composite PK.'},
      {n:'zip_id',         r:'attribute',d:'ZIP-level geography identifier.'},
      {n:'state',          r:'attribute',d:'State (denormalized).'},
      {n:'channel_desc',   r:'attribute',d:'Distribution channel: Retail, Mail Order, Specialty Pharmacy, Hospital. Part of composite PK.'},
      {n:'company_flag',   r:'flag',    d:'"Y" = company product. Enables competitor market tracking.'},
      {n:'trx_units',      r:'measure', d:'Total Rx units sold in this geo/channel/week.'},
      {n:'sales_revenue',  r:'measure', d:'Estimated net sales revenue in USD.'},
      {n:'data_date',      r:'system',  d:'IQVIA data date.'},
      {n:'source_file',    r:'system',  d:'Source file name.'},
      {n:'sys_load_timestamp',r:'system',d:'ETL load timestamp.'},
    ]
  },
  fact_npa_payer: {
    category: 'fact',
    description: 'IQVIA National Prescription Audit (NPA) data with payer type and channel breakdown. Enables payer mix analysis — what share of prescriptions are Commercial, Medicare Part D, Medicaid, or Cash. Also splits by channel (Retail, Mail Order, Specialty). Essential for managed care and market access performance measurement.',
    primaryKey: ['week_end_date','npi_id','ndc_code','payer_type','channel'],
    columns: [
      {n:'week_end_date',   r:'pk',      d:'Week ending date. Part of composite PK.'},
      {n:'npi_id',          r:'fk',      d:'FK → dim_prescriber (via npi_id). Part of composite PK.'},
      {n:'ims_id',          r:'ak',      d:'IQVIA internal IMS identifier for the prescriber.'},
      {n:'prescriber_id',   r:'fk',      d:'FK → dim_prescriber (surrogate). Enables internal join.'},
      {n:'ndc_code',        r:'fk',      d:'FK → dim_product (via ndc11). Part of composite PK.'},
      {n:'payer_type',      r:'attribute',d:'Payer segment: Commercial, Medicare, Medicaid, Cash. Part of composite PK.'},
      {n:'channel',         r:'attribute',d:'Distribution channel: Retail, Mail, Specialty. Part of composite PK.'},
      {n:'trx',             r:'measure', d:'Total Rx volume for this payer/channel segment.'},
      {n:'nrx',             r:'measure', d:'New Rx volume for this payer/channel segment.'},
      {n:'refills',         r:'measure', d:'Refill Rx volume — TRx minus NRx.'},
      {n:'projected_trx',   r:'measure', d:'IQVIA projection-adjusted TRx (accounts for data coverage gaps).'},
      {n:'projected_nrx',   r:'measure', d:'IQVIA projection-adjusted NRx.'},
      {n:'data_date',       r:'system',  d:'IQVIA data date.'},
      {n:'source_file',     r:'system',  d:'Source file name.'},
      {n:'sys_load_timestamp',r:'system',d:'ETL load timestamp.'},
    ]
  },
  fact_ddd_dispense: {
    category: 'fact',
    description: 'Drug Distribution Data (DDD) — patient-level dispense transactions. The most granular Rx dataset: individual dispense events with days supply, quantity, payer, and channel per patient. Used for patient adherence analysis, days-on-therapy calculation, and patient journey modeling. Contains anonymized patient_id.',
    primaryKey: ['transaction_date','prescriber_id','ndc11','patient_id'],
    columns: [
      {n:'transaction_date',r:'pk',       d:'Date of the dispense transaction. Part of composite PK.'},
      {n:'prescriber_id',   r:'fk',       d:'FK → dim_prescriber. Prescribing HCP. Part of composite PK.'},
      {n:'npi_id',          r:'fk',       d:'FK → dim_prescriber (via npi_id). External identifier.'},
      {n:'ims_id',          r:'ak',       d:'IQVIA IMS identifier for the prescriber.'},
      {n:'ndc11',           r:'fk',       d:'FK → dim_product (via ndc11). Dispensed product. Part of composite PK.'},
      {n:'payer_type',      r:'attribute',d:'Payer type at time of dispense.'},
      {n:'channel',         r:'attribute',d:'Dispensing channel: Retail, Specialty, Mail Order.'},
      {n:'nrx_flag',        r:'flag',     d:'"Y" if this is a new prescription (vs. refill).'},
      {n:'trx',             r:'measure',  d:'Prescription count (typically 1 per transaction).'},
      {n:'patient_id',      r:'attribute',d:'Anonymized patient identifier. Part of composite PK. Enables patient journey tracking.'},
      {n:'days_supply',     r:'measure',  d:'Days of medication supplied in this dispense. Key for adherence analysis.'},
      {n:'quantity',        r:'measure',  d:'Quantity of units dispensed.'},
      {n:'data_source',     r:'attribute',d:'Originating data vendor or source feed identifier.'},
      {n:'data_date',       r:'system',   d:'Data effective date.'},
      {n:'source_file',     r:'system',   d:'Source file name.'},
      {n:'sys_load_timestamp',r:'system', d:'ETL load timestamp.'},
    ]
  },

  /* ── MAPPING ──────────────────────────────────────────────────────── */
  zip_territory_mapping: {
    category: 'mapping',
    description: 'Lookup bridge resolving ZIP codes (via geo_id) to sales territory IDs. Used when territory_id is not directly available in source data — for example, enriching IQVIA geographic sales data with territory context before computing territory-level KPIs.',
    primaryKey: ['geo_id','territory_id'],
    columns: [
      {n:'geo_id',       r:'fk',       d:'FK → dim_geography. Part of composite PK.'},
      {n:'zip_code',     r:'attribute',d:'ZIP code (denormalized for convenience).'},
      {n:'territory_id', r:'attribute',d:'Sales territory identifier this ZIP belongs to.'},
    ]
  },

  /* ── MONTHLY METRICS ─────────────────────────────────────────────── */
  call_consistency_monthly: {
    category: 'metric_monthly',
    description: 'Measures how evenly call activity is distributed across a month per rep. A high ratio of calls made in the last 3 days of the month (end-loading) flags potential data integrity issues or rep behavior problems.',
    derivedFrom: ['fact_call_activity'],
    columns: [
      {n:'month',                    r:'temporal',d:'Reporting month (YYYY-MM).'},
      {n:'rep_id',                   r:'fk',      d:'FK → dim_rep_master. Grouping key.'},
      {n:'total_no_of_calls_made',   r:'measure', d:'Total calls in the month.'},
      {n:'no_of_calls_made_in_last_3_days',r:'measure',d:'Calls logged in the last 3 calendar days — end-loading signal.'},
      {n:'call_consistency',         r:'measure', d:'Derived ratio: last-3-day calls / total calls. Lower = more consistent distribution.'},
    ]
  },
  sales_per_call_monthly: {
    category: 'metric_monthly',
    description: 'Productivity KPI measuring TRx units generated per field call made, segmented by product and territory. Quantifies the ROI of sales activity and enables territory benchmarking.',
    derivedFrom: ['fact_xponents_rx','fact_call_activity'],
    columns: [
      {n:'product_id',   r:'fk',     d:'FK → dim_product. Grouping key.'},
      {n:'territory_id', r:'attribute',d:'Sales territory. Grouping key.'},
      {n:'month',        r:'temporal',d:'Reporting month.'},
      {n:'sales_made',   r:'measure', d:'TRx units attributed to this territory/product.'},
      {n:'calls_made',   r:'measure', d:'Total calls made in this territory/product.'},
      {n:'sales_per_call',r:'measure',d:'Derived: sales_made / calls_made.'},
    ]
  },
  prescriber_conversion_monthly: {
    category: 'metric_monthly',
    description: 'Tracks the rate at which newly targeted prescribers become active writers of the product. Key metric for measuring field force effectiveness at activating new HCPs.',
    derivedFrom: ['fact_xponents_rx'],
    columns: [
      {n:'product_id',             r:'fk',     d:'FK → dim_product.'},
      {n:'territory_id',           r:'attribute',d:'Sales territory.'},
      {n:'month',                  r:'temporal',d:'Reporting month.'},
      {n:'new_targeted_prescribers',r:'measure',d:'HCPs newly added to target list this month.'},
      {n:'new_writers_captured',   r:'measure', d:'Of those targeted, how many wrote at least one Rx.'},
      {n:'conversion_rate',        r:'measure', d:'new_writers_captured / new_targeted_prescribers × 100.'},
    ]
  },
  metric_monthly_marketshare_trx: {
    category: 'metric_monthly',
    description: 'Monthly TRx (Total Prescription) market share by product, territory, and specialty. Numerator from fact_xponents_rx (our product TRx); denominator from fact_iqvia_sales (total market TRx).',
    derivedFrom: ['fact_xponents_rx','fact_iqvia_sales'],
    columns: [
      {n:'product_id',           r:'fk',     d:'FK → dim_product.'},
      {n:'speciality',           r:'attribute',d:'HCP specialty grouping.'},
      {n:'our_product',          r:'flag',    d:'"Y" for company products only.'},
      {n:'territory_id',         r:'attribute',d:'Sales territory.'},
      {n:'sales_month',          r:'temporal',d:'Reporting month.'},
      {n:'our_product_trx_units',r:'measure', d:'Our product TRx — numerator.'},
      {n:'total_market_trx_units',r:'measure',d:'Total market TRx (all brands) — denominator.'},
      {n:'trx_market_share_pct', r:'measure', d:'Market share %: our_trx / total_trx × 100.'},
    ]
  },
  sample_script_ratio_monthly: {
    category: 'metric_monthly',
    description: 'Measures sampling efficiency — how many TRx units are generated per sample unit distributed. Used to evaluate sampling program ROI and identify over/under-sampling by territory.',
    derivedFrom: ['fact_call_activity','fact_xponents_rx'],
    columns: [
      {n:'month',             r:'temporal',d:'Reporting month.'},
      {n:'territory_id',      r:'attribute',d:'Sales territory.'},
      {n:'product_id',        r:'fk',     d:'FK → dim_product.'},
      {n:'sample_distributed',r:'measure', d:'Sample units dropped by reps in this territory/month.'},
      {n:'total_trx',         r:'measure', d:'TRx units generated.'},
      {n:'sample_script_ratio',r:'measure',d:'total_trx / sample_distributed. Higher = more efficient sampling.'},
    ]
  },
  target_reach: {
    category: 'metric_monthly',
    description: 'Measures what percentage of targeted HCPs were actually visited by each rep. Core field force reach KPI — ensures the salesforce is investing time with the right HCPs.',
    derivedFrom: ['fact_call_activity','fact_call_plan'],
    columns: [
      {n:'rep_id',                  r:'fk',     d:'FK → dim_rep_master.'},
      {n:'data_date',               r:'temporal',d:'Reporting date (point-in-time snapshot).'},
      {n:'total_unique_hcp_target', r:'measure', d:'Total unique HCPs on this rep\'s target list.'},
      {n:'total_unique_hcp_visited',r:'measure', d:'Unique targeted HCPs the rep actually visited.'},
      {n:'target_reach_pct',        r:'measure', d:'total_unique_hcp_visited / total_unique_hcp_target × 100.'},
    ]
  },
  metric_monthly_growth_nrx: {
    category: 'metric_monthly',
    description: 'Month-over-month NRx (New Prescription) growth rate by product, territory, and specialty. Lagged comparison: current period NRx vs. same-period prior month or prior year NRx.',
    derivedFrom: ['fact_xponents_rx'],
    columns: [
      {n:'product_id',         r:'fk',     d:'FK → dim_product.'},
      {n:'speciality',         r:'attribute',d:'HCP specialty.'},
      {n:'territory_id',       r:'attribute',d:'Sales territory.'},
      {n:'sales_month',        r:'temporal',d:'Reporting month.'},
      {n:'total_nrx_units',    r:'measure', d:'NRx units this period.'},
      {n:'total_nrx_units_prev',r:'measure',d:'NRx units prior period (lag).'},
      {n:'nrx_growth_pct',     r:'measure', d:'(current - prior) / prior × 100.'},
    ]
  },
  clm_utilization_monthly: {
    category: 'metric_monthly',
    description: 'Percentage of rep calls where CLM (Closed Loop Marketing) digital sales aids were actively used. Tracks digital channel adoption and compliance with promotional guidelines.',
    derivedFrom: ['fact_clm_activity'],
    columns: [
      {n:'month',             r:'temporal',d:'Reporting month.'},
      {n:'rep_id',            r:'fk',     d:'FK → dim_rep_master.'},
      {n:'total_calls_made',  r:'measure', d:'Total calls made by rep in month.'},
      {n:'calls_using_clm_media',r:'measure',d:'Calls where CLM content was shown.'},
      {n:'clm_utilization_pct',r:'measure',d:'calls_using_clm / total_calls × 100.'},
    ]
  },
  hcp_churn_monthly: {
    category: 'metric_monthly',
    description: 'Month-over-month HCP retention metric — tracks prescribers who stop writing the product. High churn signals potential access issues, competitive pressure, or gaps in rep engagement with the HCP base.',
    derivedFrom: ['fact_xponents_rx'],
    columns: [
      {n:'product_id',   r:'fk',      d:'FK → dim_product.'},
      {n:'territory_id', r:'attribute',d:'Sales territory.'},
      {n:'month',        r:'temporal', d:'Reporting month.'},
      {n:'current_hcps', r:'measure',  d:'HCPs who wrote the product this month.'},
      {n:'prev_hcps',    r:'measure',  d:'HCPs who wrote the product prior month.'},
      {n:'churned_hcps', r:'measure',  d:'HCPs present last month but absent this month.'},
      {n:'churn_rate',   r:'measure',  d:'churned_hcps / prev_hcps × 100.'},
    ]
  },
  metric_monthly_marketshare_nrx: {
    category: 'metric_monthly',
    description: 'Monthly NRx (New Prescription) market share — same structure as TRx market share but focused exclusively on new patients. NRx share is more sensitive to sales force effectiveness than TRx share.',
    derivedFrom: ['fact_xponents_rx','fact_iqvia_sales'],
    columns: [
      {n:'product_id',            r:'fk',     d:'FK → dim_product.'},
      {n:'speciality',            r:'attribute',d:'HCP specialty.'},
      {n:'our_product',           r:'flag',    d:'Company product flag.'},
      {n:'territory_id',          r:'attribute',d:'Sales territory.'},
      {n:'sales_month',           r:'temporal',d:'Reporting month.'},
      {n:'our_product_nrx_units', r:'measure', d:'Our product NRx — numerator.'},
      {n:'total_market_nrx_units',r:'measure', d:'Total market NRx — denominator.'},
      {n:'nrx_market_share_pct',  r:'measure', d:'NRx market share %.'},
    ]
  },
  freq_attainment_hcp: {
    category: 'metric_quarterly',
    description: 'Quarterly call frequency attainment at the HCP level — how many visits were planned vs. actually delivered per prescriber. Ensures high-value HCPs receive the target number of interactions per quarter.',
    derivedFrom: ['fact_call_activity','fact_call_plan'],
    columns: [
      {n:'quarter',          r:'temporal',d:'Reporting quarter (e.g. 2024-Q1).'},
      {n:'prescriber_id',    r:'fk',     d:'FK → dim_prescriber.'},
      {n:'planned_visits',   r:'measure', d:'Visits planned per call plan.'},
      {n:'actual_visits',    r:'measure', d:'Visits actually completed per call activity.'},
      {n:'freq_attainment_pct',r:'measure',d:'actual_visits / planned_visits × 100.'},
    ]
  },
  avg_interaction_time_monthly: {
    category: 'metric_monthly',
    description: 'Average call duration per rep per month. Longer, higher-quality interactions tend to correlate with better HCP engagement and key message recall. Benchmarks reps against each other and against plan targets.',
    derivedFrom: ['fact_call_activity'],
    columns: [
      {n:'month',             r:'temporal',d:'Reporting month.'},
      {n:'rep_id',            r:'fk',     d:'FK → dim_rep_master.'},
      {n:'total_no_of_calls', r:'measure', d:'Total calls in the month.'},
      {n:'total_time_spent',  r:'measure', d:'Total minutes across all calls.'},
      {n:'avg_interaction_time',r:'measure',d:'total_time_spent / total_no_of_calls.'},
    ]
  },
  prescription_velocity_monthly: {
    category: 'metric_monthly',
    description: 'Rate of change in TRx volume month-over-month per product and territory. A leading indicator of territory momentum — positive velocity signals growing prescriber adoption; negative signals potential issues needing intervention.',
    derivedFrom: ['fact_xponents_rx'],
    columns: [
      {n:'product_id',  r:'fk',     d:'FK → dim_product.'},
      {n:'territory_id',r:'attribute',d:'Sales territory.'},
      {n:'month',       r:'temporal',d:'Reporting month.'},
      {n:'trx_current', r:'measure', d:'TRx this month.'},
      {n:'trx_previous',r:'measure', d:'TRx prior month.'},
      {n:'velocity',    r:'measure', d:'(trx_current - trx_previous) / trx_previous. Month-over-month Rx velocity.'},
    ]
  },
  metric_monthly_growth_trx: {
    category: 'metric_monthly',
    description: 'Month-over-month TRx (Total Prescription) growth rate by product, territory, and specialty. Companion to NRx growth — TRx growth includes refill dynamics and thus reflects both new patient starts and adherence trends.',
    derivedFrom: ['fact_xponents_rx'],
    columns: [
      {n:'product_id',         r:'fk',      d:'FK → dim_product.'},
      {n:'speciality',         r:'attribute',d:'HCP specialty.'},
      {n:'territory_id',       r:'attribute',d:'Sales territory.'},
      {n:'sales_month',        r:'temporal', d:'Reporting month.'},
      {n:'total_trx_units',    r:'measure',  d:'TRx units this period.'},
      {n:'total_trx_units_prev',r:'measure', d:'TRx units prior period.'},
      {n:'trx_growth_pct',     r:'measure',  d:'(current - prior) / prior × 100.'},
    ]
  },
  calls_per_day_monthly: {
    category: 'metric_monthly',
    description: 'Average number of field calls a rep completes per working day in a month. Standard field force productivity benchmark used in quota-setting and performance management.',
    derivedFrom: ['fact_call_activity'],
    columns: [
      {n:'month',        r:'temporal',d:'Reporting month.'},
      {n:'rep_id',       r:'fk',     d:'FK → dim_rep_master.'},
      {n:'calls_made',   r:'measure', d:'Total calls made in month.'},
      {n:'calls_per_day',r:'measure', d:'calls_made / working days in month.'},
    ]
  },
  call_status_monthly: {
    category: 'metric_monthly',
    description: 'CRM submission compliance metric — compares calls logged vs. calls formally submitted/approved in the system. High gaps indicate data quality issues or delayed CRM entry by reps.',
    derivedFrom: ['fact_call_activity'],
    columns: [
      {n:'month',                 r:'temporal',d:'Reporting month.'},
      {n:'rep_id',                r:'fk',     d:'FK → dim_rep_master.'},
      {n:'total_calls_made',      r:'measure', d:'All call records in the system for this rep/month.'},
      {n:'total_calls_submitted', r:'measure', d:'Calls in "Submitted" status in CRM.'},
      {n:'call_status_sub',       r:'measure', d:'Submission rate: submitted / total × 100.'},
    ]
  },
  virtual_call_mix_monthly: {
    category: 'metric_monthly',
    description: 'Share of calls conducted virtually (phone/video) vs. in-person each month. Tracks omnichannel engagement strategy execution and digital adoption trends across the sales force.',
    derivedFrom: ['fact_call_activity'],
    columns: [
      {n:'month',          r:'temporal',d:'Reporting month.'},
      {n:'rep_id',         r:'fk',     d:'FK → dim_rep_master.'},
      {n:'total_calls',    r:'measure', d:'Total calls in month.'},
      {n:'virtual_calls',  r:'measure', d:'Calls with virtual_call_flag = Y.'},
      {n:'virtual_call_pct',r:'measure',d:'virtual_calls / total_calls × 100.'},
    ]
  },
  spillover_sales_monthly: {
    category: 'metric_monthly',
    description: 'TRx generated outside a rep\'s defined territory boundaries — "spillover." Quantifies how much Rx activity from an HCP flows into neighboring territories. Important for fair quota allocation and rep credit attribution.',
    derivedFrom: ['fact_xponents_rx','zip_territory_mapping'],
    columns: [
      {n:'product_id',   r:'fk',     d:'FK → dim_product.'},
      {n:'territory_id', r:'attribute',d:'Home territory.'},
      {n:'month',        r:'temporal',d:'Reporting month.'},
      {n:'total_trx',    r:'measure', d:'Total TRx attributed to HCPs in this territory.'},
      {n:'local_trx',    r:'measure', d:'TRx filled within the territory boundaries.'},
      {n:'spillover_trx',r:'measure', d:'TRx filled outside the territory — the spillover volume.'},
    ]
  },
  vae_open_rate_prescriber_monthly: {
    category: 'metric_monthly',
    description: 'Email open rate per prescriber per month. Part of the omnichannel engagement KPI suite — measures digital channel effectiveness alongside field call activity.',
    derivedFrom: ['fact_digital_engagement'],
    columns: [
      {n:'month',               r:'temporal',d:'Reporting month.'},
      {n:'prescriber_id',       r:'fk',     d:'FK → dim_prescriber.'},
      {n:'total_no_of_mails_sent',r:'measure',d:'Total emails sent to this HCP in the month.'},
      {n:'no_of_mails_opened',  r:'measure', d:'Emails opened by HCP.'},
      {n:'open_rate',           r:'measure', d:'no_of_mails_opened / total_no_of_mails_sent × 100.'},
    ]
  },

  /* ── QUARTERLY METRICS ───────────────────────────────────────────── */
  call_consistency_quarterly: {
    category: 'metric_quarterly',
    description: 'Quarterly aggregation of call distribution consistency per rep. Same logic as monthly version — measures end-loading patterns across the full quarter.',
    derivedFrom: ['fact_call_activity'],
    columns: [
      {n:'quarter',                      r:'temporal',d:'Reporting quarter.'},
      {n:'rep_id',                       r:'fk',      d:'FK → dim_rep_master.'},
      {n:'total_no_of_calls_made',       r:'measure', d:'Total calls in the quarter.'},
      {n:'no_of_calls_made_in_last_3_days',r:'measure',d:'End-loading signal calls.'},
      {n:'call_consistency',             r:'measure', d:'End-loading ratio for the quarter.'},
    ]
  },
  prescriber_conversion_quarterly: {
    category: 'metric_quarterly',
    description: 'Quarterly prescriber conversion — new targeted HCPs converted to writers in the quarter. Provides a more stable view than monthly given the longer window.',
    derivedFrom: ['fact_xponents_rx'],
    columns: [
      {n:'product_id',             r:'fk',      d:'FK → dim_product.'},
      {n:'territory_id',           r:'attribute',d:'Sales territory.'},
      {n:'quarter',                r:'temporal', d:'Reporting quarter.'},
      {n:'new_targeted_prescribers',r:'measure', d:'Newly targeted HCPs this quarter.'},
      {n:'new_writers_captured',   r:'measure',  d:'Of targeted, those who wrote Rx.'},
      {n:'conversion_rate',        r:'measure',  d:'Quarterly conversion %.'},
    ]
  },
  metric_quarterly_marketshare_trx: {
    category: 'metric_quarterly',
    description: 'Quarterly TRx market share — stable, smoothed view of market position used in Business Reviews and leadership reporting.',
    derivedFrom: ['fact_xponents_rx','fact_iqvia_sales'],
    columns: [
      {n:'product_id',           r:'fk',      d:'FK → dim_product.'},
      {n:'speciality',           r:'attribute',d:'HCP specialty.'},
      {n:'our_product',          r:'flag',     d:'Company product flag.'},
      {n:'territory_id',         r:'attribute',d:'Sales territory.'},
      {n:'sales_quarter',        r:'temporal', d:'Reporting quarter.'},
      {n:'our_product_trx_units',r:'measure',  d:'Our product quarterly TRx.'},
      {n:'total_market_trx_units',r:'measure', d:'Total market quarterly TRx.'},
      {n:'trx_market_share_pct', r:'measure',  d:'Quarterly TRx market share %.'},
    ]
  },
  avg_interaction_time_quarterly: {
    category: 'metric_quarterly',
    description: 'Quarterly average call duration per rep. Quarterly view smooths out monthly variance for performance reviews.',
    derivedFrom: ['fact_call_activity'],
    columns: [
      {n:'quarter',             r:'temporal',d:'Reporting quarter.'},
      {n:'rep_id',              r:'fk',     d:'FK → dim_rep_master.'},
      {n:'total_no_of_calls',   r:'measure', d:'Total calls in quarter.'},
      {n:'total_time_spent',    r:'measure', d:'Total minutes in quarter.'},
      {n:'avg_interaction_time',r:'measure', d:'Quarterly average call duration (minutes).'},
    ]
  },
  metric_quarterly_marketshare_nrx: {
    category: 'metric_quarterly',
    description: 'Quarterly NRx market share — quarterly view of new patient acquisition share of the market.',
    derivedFrom: ['fact_xponents_rx','fact_iqvia_sales'],
    columns: [
      {n:'product_id',            r:'fk',      d:'FK → dim_product.'},
      {n:'speciality',            r:'attribute',d:'HCP specialty.'},
      {n:'our_product',           r:'flag',     d:'Company product flag.'},
      {n:'territory_id',          r:'attribute',d:'Sales territory.'},
      {n:'sales_quarter',         r:'temporal', d:'Reporting quarter.'},
      {n:'our_product_nrx_units', r:'measure',  d:'Our product quarterly NRx.'},
      {n:'total_market_nrx_units',r:'measure',  d:'Total market quarterly NRx.'},
      {n:'nrx_market_share_pct',  r:'measure',  d:'Quarterly NRx market share %.'},
    ]
  },
  metric_quarterly_growth_nrx: {
    category: 'metric_quarterly',
    description: 'Quarter-over-quarter NRx growth rate. Used in Business Review decks and quarterly goal-setting cycles.',
    derivedFrom: ['fact_xponents_rx'],
    columns: [
      {n:'product_id',         r:'fk',      d:'FK → dim_product.'},
      {n:'speciality',         r:'attribute',d:'HCP specialty.'},
      {n:'territory_id',       r:'attribute',d:'Sales territory.'},
      {n:'sales_quarter',      r:'temporal', d:'Reporting quarter.'},
      {n:'total_nrx_units',    r:'measure',  d:'NRx this quarter.'},
      {n:'total_nrx_units_prev',r:'measure', d:'NRx prior quarter.'},
      {n:'nrx_growth_pct',     r:'measure',  d:'Quarter-over-quarter NRx growth %.'},
    ]
  },
  metric_quarterly_growth_trx: {
    category: 'metric_quarterly',
    description: 'Quarter-over-quarter TRx growth rate. Tracks overall prescription momentum including refill trends.',
    derivedFrom: ['fact_xponents_rx'],
    columns: [
      {n:'product_id',          r:'fk',      d:'FK → dim_product.'},
      {n:'speciality',          r:'attribute',d:'HCP specialty.'},
      {n:'territory_id',        r:'attribute',d:'Sales territory.'},
      {n:'sales_quarter',       r:'temporal', d:'Reporting quarter.'},
      {n:'total_trx_units',     r:'measure',  d:'TRx this quarter.'},
      {n:'total_trx_units_prev',r:'measure',  d:'TRx prior quarter.'},
      {n:'trx_growth_pct',      r:'measure',  d:'Quarter-over-quarter TRx growth %.'},
    ]
  },
  calls_per_day_quarterly: {
    category: 'metric_quarterly',
    description: 'Quarterly average daily call rate per rep. Used in quarterly performance reviews and rep ranking.',
    derivedFrom: ['fact_call_activity'],
    columns: [
      {n:'quarter',       r:'temporal',d:'Reporting quarter.'},
      {n:'rep_id',        r:'fk',     d:'FK → dim_rep_master.'},
      {n:'calls_made',    r:'measure', d:'Total calls in quarter.'},
      {n:'calls_per_day', r:'measure', d:'Average calls per working day.'},
    ]
  },
  call_status_quarterly: {
    category: 'metric_quarterly',
    description: 'Quarterly CRM submission compliance. Quarterly view provides better signal for rep compliance audits.',
    derivedFrom: ['fact_call_activity'],
    columns: [
      {n:'quarter',               r:'temporal',d:'Reporting quarter.'},
      {n:'rep_id',                r:'fk',     d:'FK → dim_rep_master.'},
      {n:'total_calls_made',      r:'measure', d:'All calls in quarter.'},
      {n:'total_calls_submitted', r:'measure', d:'Submitted calls in quarter.'},
      {n:'call_status_sub',       r:'measure', d:'Quarterly submission rate %.'},
    ]
  },
  virtual_call_mix_quarterly: {
    category: 'metric_quarterly',
    description: 'Quarterly virtual call adoption rate. Used to track omnichannel strategy compliance across the sales force on a quarterly cadence.',
    derivedFrom: ['fact_call_activity'],
    columns: [
      {n:'quarter',         r:'temporal',d:'Reporting quarter.'},
      {n:'rep_id',          r:'fk',     d:'FK → dim_rep_master.'},
      {n:'total_calls',     r:'measure', d:'Total calls in quarter.'},
      {n:'virtual_calls',   r:'measure', d:'Virtual calls in quarter.'},
      {n:'virtual_call_pct',r:'measure', d:'Quarterly virtual call mix %.'},
    ]
  },
  spillover_sales_quarterly: {
    category: 'metric_quarterly',
    description: 'Quarterly spillover Rx analysis — provides a more complete picture of territory boundary effects for quota and incentive compensation reviews.',
    derivedFrom: ['fact_xponents_rx','zip_territory_mapping'],
    columns: [
      {n:'product_id',   r:'fk',      d:'FK → dim_product.'},
      {n:'territory_id', r:'attribute',d:'Home territory.'},
      {n:'quarter',      r:'temporal', d:'Reporting quarter.'},
      {n:'total_trx',    r:'measure',  d:'Total quarterly TRx.'},
      {n:'local_trx',    r:'measure',  d:'In-territory TRx.'},
      {n:'spillover_trx',r:'measure',  d:'Out-of-territory TRx.'},
    ]
  },
  incr_sales_per_call_quarterly: {
    category: 'metric_quarterly',
    description: 'Incremental TRx generated per call vs. prior quarter baseline. Measures the true ROI of incremental sales force activity — how much additional Rx is driven by each additional call beyond the baseline.',
    derivedFrom: ['fact_xponents_rx','fact_call_activity'],
    columns: [
      {n:'product_id',       r:'fk',      d:'FK → dim_product.'},
      {n:'territory_id',     r:'attribute',d:'Sales territory.'},
      {n:'quarter',          r:'temporal', d:'Reporting quarter.'},
      {n:'sales_current',    r:'measure',  d:'TRx this quarter.'},
      {n:'sales_previous',   r:'measure',  d:'TRx prior quarter (baseline).'},
      {n:'incr_sales_per_call',r:'measure',d:'(sales_current - sales_previous) / calls_made. Incremental sales efficiency.'},
    ]
  },
  hcp_churn_quarterly: {
    category: 'metric_quarterly',
    description: 'Quarterly HCP churn analysis — prescriber retention view over the full quarter. Feeds into quarterly business reviews for market access and competitive landscape discussions.',
    derivedFrom: ['fact_xponents_rx'],
    columns: [
      {n:'product_id',   r:'fk',      d:'FK → dim_product.'},
      {n:'territory_id', r:'attribute',d:'Sales territory.'},
      {n:'quarter',      r:'temporal', d:'Reporting quarter.'},
      {n:'current_hcps', r:'measure',  d:'HCPs who wrote product this quarter.'},
      {n:'prev_hcps',    r:'measure',  d:'HCPs who wrote product prior quarter.'},
      {n:'churned_hcps', r:'measure',  d:'HCPs lost quarter-over-quarter.'},
      {n:'churn_rate',   r:'measure',  d:'Quarterly HCP churn %.'},
    ]
  },
  sales_per_call_quarterly: {
    category: 'metric_quarterly',
    description: 'Quarterly TRx per call productivity metric. Provides a stable, quarter-level view of field force Rx generation efficiency for QBR presentations.',
    derivedFrom: ['fact_xponents_rx','fact_call_activity'],
    columns: [
      {n:'product_id',   r:'fk',      d:'FK → dim_product.'},
      {n:'territory_id', r:'attribute',d:'Sales territory.'},
      {n:'quarter',      r:'temporal', d:'Reporting quarter.'},
      {n:'sales_made',   r:'measure',  d:'Quarterly TRx attributed to territory.'},
      {n:'calls_made',   r:'measure',  d:'Total calls in quarter.'},
      {n:'sales_per_call',r:'measure', d:'Quarterly TRx per call.'},
    ]
  },
  vae_open_rate_prescriber_quarterly: {
    category: 'metric_quarterly',
    description: 'Quarterly email open rate per prescriber. Quarterly view smooths campaign timing variance for strategic digital engagement analysis.',
    derivedFrom: ['fact_digital_engagement'],
    columns: [
      {n:'quarter',               r:'temporal',d:'Reporting quarter.'},
      {n:'prescriber_id',         r:'fk',     d:'FK → dim_prescriber.'},
      {n:'total_no_of_mails_sent',r:'measure', d:'Emails sent to HCP in quarter.'},
      {n:'no_of_mails_opened',    r:'measure', d:'Emails opened in quarter.'},
      {n:'open_rate',             r:'measure', d:'Quarterly email open rate %.'},
    ]
  },
};

/* ─── RELATIONSHIPS ─────────────────────────────────────────────────── */
const RELS = [
  // Dims → Facts
  {f:'dim_rep_master',    fk:'rep_id',         t:'fact_call_activity',       tk:'rep_id',         d:'Identifies the rep who performed the call.'},
  {f:'dim_rep_master',    fk:'rep_id',         t:'fact_call_plan',           tk:'rep_id',         d:'Assigns planned call targets to a rep.'},
  {f:'dim_rep_master',    fk:'rep_id',         t:'fact_clm_activity',        tk:'rep_id',         d:'Identifies the rep who showed the CLM content.'},
  {f:'dim_rep_master',    fk:'rep_id',         t:'fact_digital_engagement',  tk:'rep_id',         d:'Identifies the rep who sent the email.'},
  {f:'dim_rep_master',    fk:'rep_id',         t:'dim_territory_alignment',  tk:'rep_id',         d:'Links rep to their territory assignments.'},
  {f:'dim_prescriber',    fk:'prescriber_id',  t:'fact_call_activity',       tk:'prescriber_id',  d:'Identifies the HCP who was visited.'},
  {f:'dim_prescriber',    fk:'prescriber_id',  t:'fact_call_plan',           tk:'prescriber_id',  d:'HCP targeted in the call plan.'},
  {f:'dim_prescriber',    fk:'prescriber_id',  t:'fact_clm_activity',        tk:'prescriber_id',  d:'HCP who received the CLM presentation.'},
  {f:'dim_prescriber',    fk:'prescriber_id',  t:'fact_digital_engagement',  tk:'prescriber_id',  d:'HCP who received the email.'},
  {f:'dim_prescriber',    fk:'prescriber_id',  t:'fact_xponents_rx',         tk:'prescriber_id',  d:'HCP whose Rx behavior is measured.'},
  {f:'dim_prescriber',    fk:'prescriber_id',  t:'fact_npa_payer',           tk:'prescriber_id',  d:'HCP whose payer-split Rx is tracked.'},
  {f:'dim_prescriber',    fk:'prescriber_id',  t:'fact_ddd_dispense',        tk:'prescriber_id',  d:'HCP who prescribed the dispensed drug.'},
  {f:'dim_prescriber',    fk:'prescriber_id',  t:'dim_prescriber_geo_mapping',tk:'prescriber_id', d:'Maps HCP to their practice geographies.'},
  {f:'dim_product',       fk:'product_id',     t:'fact_call_activity',       tk:'product_id',     d:'Product detailed during the call.'},
  {f:'dim_product',       fk:'product_id',     t:'fact_call_plan',           tk:'product_id',     d:'Product being promoted per the plan.'},
  {f:'dim_product',       fk:'product_id',     t:'fact_clm_activity',        tk:'product_id',     d:'Product the CLM content relates to.'},
  {f:'dim_product',       fk:'product_id',     t:'fact_xponents_rx',         tk:'product_id',     d:'Product whose prescriptions are tracked.'},
  {f:'dim_product',       fk:'product_id',     t:'fact_iqvia_sales',         tk:'product_id',     d:'Product in the IQVIA sales feed.'},
  {f:'dim_product',       fk:'ndc11',          t:'fact_ddd_dispense',        tk:'ndc11',          d:'Product dispensed (joined via NDC-11).'},
  {f:'dim_product',       fk:'product_id',     t:'dim_clm_content',          tk:'product_id',     d:'CLM content library is product-specific.'},
  {f:'dim_geography',     fk:'geo_id',         t:'fact_call_activity',       tk:'geo_id',         d:'Geography where the call took place.'},
  {f:'dim_geography',     fk:'geo_id',         t:'fact_call_plan',           tk:'geo_id',         d:'Geography of the planned call.'},
  {f:'dim_geography',     fk:'geo_id',         t:'fact_clm_activity',        tk:'geo_id',         d:'Geography of the CLM event.'},
  {f:'dim_geography',     fk:'geo_id',         t:'fact_xponents_rx',         tk:'geo_id',         d:'Geography where Rx was dispensed.'},
  {f:'dim_geography',     fk:'geo_id',         t:'fact_iqvia_sales',         tk:'geo_id',         d:'Geography of IQVIA sales data.'},
  {f:'dim_geography',     fk:'geo_id',         t:'dim_territory_alignment',  tk:'geo_id',         d:'Geography unit assigned to a territory.'},
  {f:'dim_geography',     fk:'geo_id',         t:'dim_prescriber_geo_mapping',tk:'geo_id',        d:'Prescriber practice location geography.'},
  {f:'dim_geography',     fk:'geo_id',         t:'zip_territory_mapping',    tk:'geo_id',         d:'ZIP-to-territory bridge.'},
  {f:'dim_clm_content',   fk:'clm_file_id',    t:'fact_clm_activity',        tk:'clm_file_id',    d:'The specific content file shown in the CLM event.'},
  // Fact → Fact
  {f:'fact_call_plan',    fk:'monthly_call_plan_id', t:'fact_call_activity', tk:'monthly_call_plan_id', d:'Links planned call to actual call — enables attainment measurement.'},
  {f:'fact_call_activity',fk:'call_id',         t:'fact_clm_activity',        tk:'call_id',        d:'CLM activity is a child event of a parent call.'},
  // Mapping
  {f:'zip_territory_mapping',fk:'geo_id',       t:'dim_geography',            tk:'geo_id',         d:'Resolves geo_id to territory for non-CRM data sources.'},
];

/* ─── HELPERS ───────────────────────────────────────────────────────── */
function getCatColor(cat) { return CATS[cat]?.color || '#888'; }
function getCatLabel(cat) { return CATS[cat]?.label || cat; }

function getOutgoing(id) { return RELS.filter(r => r.f === id); }
function getIncoming(id) { return RELS.filter(r => r.t === id); }
function getDerivedFrom(id) { return TABLES[id]?.derivedFrom || []; }

function roleBadge(r) {
  if (r === 'pk') return '<span class="badge badge-pk">PK</span>';
  if (r === 'ak') return '<span class="badge badge-ak">AK</span>';
  if (r && r.startsWith('fk')) return '<span class="badge badge-fk">FK</span>';
  if (r === 'system') return '<span class="badge badge-sys">SYS</span>';
  return '';
}

/* ─── SIDEBAR ───────────────────────────────────────────────────────── */
function buildSidebar(filter = '') {
  const sb = document.getElementById('sidebar');
  const order = ['dimension','fact','mapping','metric_monthly','metric_quarterly'];
  const groups = {};
  order.forEach(c => { groups[c] = []; });
  Object.keys(TABLES).forEach(id => {
    const c = TABLES[id].category;
    if (groups[c]) groups[c].push(id);
  });

  sb.innerHTML = order.map(cat => {
    const tables = groups[cat].filter(id =>
      !filter || id.toLowerCase().includes(filter.toLowerCase()) ||
      (TABLES[id].description||'').toLowerCase().includes(filter.toLowerCase()) ||
      (TABLES[id].columns||[]).some(c => c.n.toLowerCase().includes(filter.toLowerCase()))
    );
    if (!tables.length && filter) return '';
    const color = getCatColor(cat);
    let html = '<div class="cat-group" id="cg-' + cat + '">';
    html += '<div class="cat-header" onclick="toggleCat(\'' + cat + '\')">';
    html += '<span class="cat-dot" style="background:' + color + '"></span>';
    html += '<span class="cat-label" style="color:' + color + '">' + getCatLabel(cat) + '</span>';
    html += '<span class="cat-count">' + tables.length + '</span>';
    html += '<span class="cat-chevron">▾</span>';
    html += '</div>';
    html += '<ul class="table-list">';
    html += tables.map(id =>
      '<li class="table-item" id="ti-' + id + '" onclick="selectTable(\'' + id + '\')">' +
        '<span class="table-item-dot" style="background:' + color + '"></span>' +
        '<span class="table-item-name">' + id + '</span>' +
      '</li>'
    ).join('');
    if (!tables.length) html += '<li class="no-results">No match</li>';
    html += '</ul></div>';
    return html;
  }).join('');
}

function toggleCat(cat) {
  document.getElementById('cg-' + cat)?.classList.toggle('collapsed');
}

/* ─── WELCOME ───────────────────────────────────────────────────────── */
function buildWelcome() {
  const counts = {};
  Object.values(TABLES).forEach(t => { counts[t.category] = (counts[t.category]||0)+1; });
  const order = ['dimension','fact','mapping','metric_monthly','metric_quarterly'];
  const cards = order.map(cat => {
    const c = CATS[cat]; const n = counts[cat]||0;
    return '<div class="overview-card" onclick="filterToCategory(\'' + cat + '\')" style="border-color:' + c.color + '22">' +
      '<div class="ov-count" style="color:' + c.color + '">' + n + '</div>' +
      '<div class="ov-label" style="color:' + c.color + '">' + c.label + '</div>' +
      '<div class="ov-desc">' + c.desc + '</div>' +
      '<div style="position:absolute;top:0;left:0;right:0;height:2px;background:' + c.color + ';opacity:0.6"></div>' +
    '</div>';
  }).join('');

  let html = '';
  html += '<div class="welcome-hero">';
  html += '<h1>Pharma Commercial DataLake</h1>';
  html += '<p>A synthetic enterprise datalake covering the full pharma commercial domain — from CRM call activity and IQVIA market data through to territory-level KPIs and HCP engagement metrics. All 50 tables shown here are <strong>Gold Layer</strong>, served on both <strong>Databricks</strong> (compute) and <strong>Snowflake</strong> (BI/analytics serving).</p>';
  html += '</div>';
  html += '<div class="overview-grid">' + cards + '</div>';
  html += '<div class="domain-cards">';
  html += '<div class="domain-card">';
  html += '<h3>🔑 Key Join Paths</h3>';
  html += '<p><strong>rep_id</strong> — links dim_rep_master to all CRM facts and rep-level metrics.<br>';
  html += '<strong>prescriber_id / npi_id</strong> — bridges CRM data to IQVIA Xponent Rx.<br>';
  html += '<strong>product_id / ndc11</strong> — connects dim_product to all Rx, sales, and CLM data.<br>';
  html += '<strong>geo_id</strong> — links dim_geography to calls, Rx, sales, and territory alignment.</p>';
  html += '</div>';
  html += '<div class="domain-card">';
  html += '<h3>📦 Data Sources</h3>';
  html += '<p><strong>CRM (Veeva)</strong> → fact_call_activity, fact_call_plan, fact_clm_activity, fact_digital_engagement.<br>';
  html += '<strong>IQVIA Xponent</strong> → fact_xponents_rx (prescriber Rx).<br>';
  html += '<strong>IQVIA Market</strong> → fact_iqvia_sales (territory/channel sales).<br>';
  html += '<strong>IQVIA NPA</strong> → fact_npa_payer (payer mix).<br>';
  html += '<strong>DDD</strong> → fact_ddd_dispense (patient-level dispense).</p>';
  html += '</div>';
  html += '<div class="domain-card">';
  html += '<h3>⚠️ Important Design Notes</h3>';
  html += '<p><strong>company_flag</strong> in dim_product and fact tables distinguishes own brands from competitors — critical for market share logic. <strong>npi_id</strong> is the universal HCP key across CRM and IQVIA. <strong>ndc11</strong> is the universal product key for IQVIA/DDD joins. All metrics tables are aggregated; no PK constraints — grain is defined by the grouping key columns.</p>';
  html += '</div>';
  html += '<div class="domain-card">';
  html += '<h3>🏗 Platform Architecture</h3>';
  html += '<p><strong>Databricks</strong>: ETL processing of all bronze → silver → gold transformations. PySpark/SQL scripts ingest source files and build fact/dim tables.<br>';
  html += '<strong>Snowflake</strong>: Gold layer serving for BI tools (Tableau, Power BI). SQL-based metric computation jobs run on Snowflake. Metrics tables are primarily consumed here.</p>';
  html += '</div>';
  html += '</div>';
  document.getElementById('welcome').innerHTML = html;
}

/* ─── TABLE DETAIL ──────────────────────────────────────────────────── */
let currentTable = null;

function selectTable(id) {
  currentTable = id;
  const t = TABLES[id]; if (!t) return;
  document.querySelectorAll('.table-item').forEach(el => el.classList.remove('active'));
  document.getElementById('ti-' + id)?.classList.add('active');
  document.getElementById('welcome').style.display = 'none';
  const detail = document.getElementById('table-detail');
  detail.style.display = 'block';

  const color = getCatColor(t.category);
  const out = getOutgoing(id);
  const inc = getIncoming(id);
  const derived = getDerivedFrom(id);
  const pks = t.primaryKey || [];

  var colsHtml = '';
  (t.columns||[]).forEach(function(c) {
    var isPk = pks.indexOf(c.n) !== -1;
    var role = isPk ? 'pk' : c.r;
    colsHtml += '<div class="col-row">'
      + '<span class="col-name">' + c.n + '</span>'
      + '<span class="col-badges">' + roleBadge(role) + '</span>'
      + '<span class="col-desc">' + c.d + '</span>'
      + '</div>';
  });

  var outHtml = '';
  if (out.length) {
    out.forEach(function(r) {
      outHtml += '<div class="rel-row" onclick="selectTable(\'' + r.t + '\')">'
        + '<span class="rel-arrow" style="color:' + getCatColor(TABLES[r.t]?.category) + '">→</span>'
        + '<div class="rel-content">'
        + '<div class="rel-table">' + r.t + '</div>'
        + '<div class="rel-key">' + r.fk + ' → ' + r.tk + '</div>'
        + '<div class="rel-desc">' + r.d + '</div>'
        + '</div>'
        + '</div>';
    });
  } else {
    outHtml = '<div class="empty-state">No outgoing foreign keys</div>';
  }

  var incHtml = '';
  if (inc.length) {
    inc.forEach(function(r) {
      incHtml += '<div class="rel-row" onclick="selectTable(\'' + r.f + '\')">'
        + '<span class="rel-arrow" style="color:' + getCatColor(TABLES[r.f]?.category) + '">←</span>'
        + '<div class="rel-content">'
        + '<div class="rel-table">' + r.f + '</div>'
        + '<div class="rel-key">' + r.fk + ' → ' + r.tk + '</div>'
        + '<div class="rel-desc">' + r.d + '</div>'
        + '</div>'
        + '</div>';
    });
  } else {
    incHtml = '<div class="empty-state">Not referenced by other tables</div>';
  }

  var derivedHtml = '';
  if (derived.length) {
    derivedHtml = '<div class="rel-section">'
      + '<div class="rel-section-title">Derived from</div>';
    derived.forEach(function(ft) {
      derivedHtml += '<div class="rel-row" onclick="selectTable(\'' + ft + '\')">'
        + '<span class="rel-arrow" style="color:' + getCatColor(TABLES[ft]?.category) + '">↑</span>'
        + '<div class="rel-content">'
        + '<div class="rel-table">' + ft + '</div>'
        + '<div class="rel-desc">' + (TABLES[ft]?.description ? TABLES[ft].description.slice(0,80) + '…' : '') + '</div>'
        + '</div>'
        + '</div>';
    });
    derivedHtml += '</div>';
  }

  var pkDisplay = '';
  if (pks.length > 1) pkDisplay = 'Composite PK (' + pks.join(' + ') + ')';
  else if (pks.length === 1) pkDisplay = 'PK: ' + pks[0];
  else pkDisplay = 'No single PK (aggregated grain)';

  var relSections = '';
  if (out.length || inc.length) {
    relSections += '<div class="rel-section">'
      + '<div class="rel-section-title">References →</div>' + outHtml
      + '</div>';
    relSections += '<div class="rel-section">'
      + '<div class="rel-section-title">Referenced by ←</div>' + incHtml
      + '</div>';
  }
  var relEmpty = (!out.length && !inc.length && !derived.length) ? '<div class="empty-state">No defined relationships</div>' : '';
  detail.innerHTML = ''
    + '<div class="detail-header">'
    +   '<div class="detail-header-top">'
    +     '<div class="detail-table-name">' + id + '</div>'
    +     '<span class="cat-badge" style="background:' + color + '20;color:' + color + ';border:1px solid ' + color + '40">' + getCatLabel(t.category) + '</span>'
    +   '</div>'
    +   '<p class="detail-desc">' + t.description + '</p>'
    +   '<div class="detail-meta">'
    +     '<div class="meta-tag"><span class="dot" style="background:var(--pk)"></span>' + pkDisplay + '</div>'
    +     '<div class="meta-tag">' + ((t.columns||[]).length) + ' columns</div>'
    +     '<div class="meta-tag">' + out.length + ' FK refs out · ' + inc.length + ' FK refs in</div>'
    +     '<span class="platform-badge db-badge">Databricks</span>'
    +     '<span class="platform-badge sf-badge">Snowflake</span>'
    +   '</div>'
    + '</div>'
    + '<div class="detail-grid">'
    +   '<div class="panel">'
    +     '<div class="panel-header">'
    +       '<h3>Schema</h3>'
    +       '<span class="panel-count">' + ((t.columns||[]).length) + '</span>'
    +       '<span style="margin-left:auto;font-size:10px;color:var(--text-dim)">' 
    +         + '<span style="color:var(--pk)">■</span> PK &nbsp;'
    +         + '<span style="color:var(--fk)">■</span> FK &nbsp;'
    +         + '<span style="color:var(--ak)">■</span> AK &nbsp;'
    +         + '<span style="color:var(--sys)">■</span> SYS'
    +       '</span>'
    +     '</div>'
    +     '<div class="panel-body">' + colsHtml + '</div>'
    +   '</div>'
    +   '<div class="panel">'
    +     '<div class="panel-header">'
    +       '<h3>Relationships</h3>'
    +       '<span class="panel-count">' + (out.length + inc.length + derived.length) + '</span>'
    +     '</div>'
    +     '<div class="panel-body">'
    +       derivedHtml + relSections + relEmpty
    +     '</div>'
    +   '</div>'
    + '</div>'
    + '<div class="viz-panel">'
    +   '<div class="viz-header">'
    +     '<h3>Relationship Web</h3>'
    +     '<span class="viz-hint">Click any node to navigate · Hover for details</span>'
    +   '</div>'
    +   '<div id="viz-svg-container">' + buildViz(id) + '</div>'
    + '</div>';
}

/* ─── VISUALIZATION (hub & spoke) ───────────────────────────────────── */
function buildViz(id) {
  var t = TABLES[id]; if (!t) return '';
  var out = getOutgoing(id);
  var inc = getIncoming(id);
  var derived = getDerivedFrom(id);

  var neighbors = [];
  var seen = {};
  for (var i = 0; i < out.length; ++i) {
    var r = out[i];
    if (!seen[r.t]) { seen[r.t] = true; neighbors.push({id:r.t, dir:'out', key:r.fk + '→' + r.tk}); }
  }
  for (var i = 0; i < inc.length; ++i) {
    var r = inc[i];
    if (!seen[r.f]) { seen[r.f] = true; neighbors.push({id:r.f, dir:'in', key:r.fk + '→' + r.tk}); }
  }
  for (var i = 0; i < derived.length; ++i) {
    var f = derived[i];
    if (!seen[f]) { seen[f] = true; neighbors.push({id:f, dir:'derived', key:'derived from'}); }
  }

  var W = 780, H = Math.max(320, 120 + neighbors.length * 28);
  var cx = W/2, cy = H/2;
  var R = Math.min(cy - 70, 170);
  var n = neighbors.length;
  var centerColor = getCatColor(t.category);

  // Draw lines with arrowheads
  var lines = '';
  for (var i = 0; i < neighbors.length; ++i) {
    var nb = neighbors[i];
    var angle = (2*Math.PI*i/n) - Math.PI/2;
    var nx = cx + R*Math.cos(angle);
    var ny = cy + R*Math.sin(angle);
    var nc = getCatColor(TABLES[nb.id]?.category);
    var dash = nb.dir === 'derived' ? '4,3' : '';
    // Arrowhead
    var arrowSize = 8;
    var dx = nx - cx, dy = ny - cy;
    var len = Math.sqrt(dx*dx + dy*dy);
    var ax = nx - (dx/len)*arrowSize;
    var ay = ny - (dy/len)*arrowSize;
    lines += '<line x1="' + cx + '" y1="' + cy + '" x2="' + ax + '" y2="' + ay + '"'
      + ' stroke="' + nc + '" stroke-width="2" stroke-opacity="0.5"'
      + ' stroke-dasharray="' + dash + '" marker-end="url(#arrowhead' + i + ')"/>'
      + '<marker id="arrowhead' + i + '" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto" markerUnits="strokeWidth">'
      + '<polygon points="0 0, 10 3.5, 0 7" fill="' + nc + '" opacity="0.7"/>'
      + '</marker>';
  }

  // Draw nodes
  var nodes = '';
  for (var i = 0; i < neighbors.length; ++i) {
    var nb = neighbors[i];
    var angle = (2*Math.PI*i/n) - Math.PI/2;
    var nx = cx + R*Math.cos(angle);
    var ny = cy + R*Math.sin(angle);
    var nc = getCatColor(TABLES[nb.id]?.category);
    var short = nb.id.length > 18 ? nb.id.slice(0,16)+'…' : nb.id;
    nodes += '<g class="viz-node" onclick="selectTable(\'' + nb.id + '\')" style="cursor:pointer">'
      + '<circle cx="' + nx + '" cy="' + ny + '" r="28" fill="' + nc + '22" stroke="' + nc + '" stroke-width="2"/>'
      + '<text x="' + nx + '" y="' + (ny+5) + '" text-anchor="middle" font-size="13" font-family="var(--font-mono)" fill="' + nc + '" font-weight="bold">' + short + '</text>'
      + '</g>';
  }

  // Center node
  var centerNode = '';
  centerNode += '<g>'
    + '<circle cx="' + cx + '" cy="' + cy + '" r="38" fill="' + centerColor + '33" stroke="' + centerColor + '" stroke-width="4" filter="url(#glow)"/>'
    + '<text x="' + cx + '" y="' + (cy+7) + '" text-anchor="middle" font-size="18" font-family="var(--font-mono)" fill="' + centerColor + '" font-weight="bold">' + id + '</text>'
    + '</g>';

  // SVG filter for glow
  var filter = '';
  filter += '<filter id="glow" x="-50%" y="-50%" width="200%" height="200%">'
    + '<feGaussianBlur stdDeviation="6" result="coloredBlur"/>'
    + '<feMerge>'
    + '<feMergeNode in="coloredBlur"/>'
    + '<feMergeNode in="SourceGraphic"/>'
    + '</feMerge>'
    + '</filter>';

  return '<svg width="' + W + '" height="' + H + '">' 
    + '<defs>' + filter + '</defs>'
    + lines
    + centerNode
    + nodes
    + '</svg>';
}

/* ─── SEARCH ────────────────────────────────────────────────────────── */
function filterToCategory(cat) {
  document.getElementById('search-input').value = '';
  buildSidebar();
  Object.keys(CATS).forEach(c => {
    const el = document.getElementById('cg-' + c);
    if (el) { if (c !== cat) el.classList.add('collapsed'); else el.classList.remove('collapsed'); }
  });
}

document.getElementById('search-input').addEventListener('input', function() {
  buildSidebar(this.value.trim());
});

/* ─── INIT ──────────────────────────────────────────────────────────── */
buildSidebar();
buildWelcome();
</script>
</body>
</html>
