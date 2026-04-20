// app.js — CannaGuia webapp logic

// ── Service Worker ────────────────────────────────────────────────────────────
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js').catch(() => {});
  });
}

// ── State ─────────────────────────────────────────────────────────────────────
let currentScreen = 'home';
let quizRespostas = {};
let quizPasso = 0;

// ── Navigation ────────────────────────────────────────────────────────────────
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-' + id).classList.add('active');
  currentScreen = id;
  window.scrollTo(0, 0);
}

function goHome() {
  showScreen('home');
}

// ── BUILD SEARCH INDEX ────────────────────────────────────────────────────────
const SEARCH_INDEX = [];
TODAS_SECOES.forEach(secao => {
  secao.secoes.forEach(sec => {
    sec.itens.forEach(([subtit, texto]) => {
      SEARCH_INDEX.push({
        sectionId:    secao.id,
        sectionName:  secao.titulo,
        sectionIcon:  secao.icone,
        titulo:       subtit,
        texto:        texto.replace(/<[^>]+>/g, ' '),
      });
    });
  });
});

// ── SEARCH ────────────────────────────────────────────────────────────────────
let searchTimer = null;
function onSearch(val) {
  clearTimeout(searchTimer);
  searchTimer = setTimeout(() => renderSearch(val.trim()), 250);
}

function renderSearch(q) {
  const resultsEl = document.getElementById('search-results');
  const menuEl    = document.getElementById('menu-grid');

  if (!q) {
    resultsEl.innerHTML = '';
    resultsEl.classList.remove('visible');
    menuEl.style.display = '';
    return;
  }

  const ql = q.toLowerCase();
  const hits = SEARCH_INDEX.filter(item =>
    item.titulo.toLowerCase().includes(ql) ||
    item.texto.toLowerCase().includes(ql) ||
    item.sectionName.toLowerCase().includes(ql)
  ).slice(0, 15);

  menuEl.style.display = 'none';
  resultsEl.classList.add('visible');

  if (!hits.length) {
    resultsEl.innerHTML = '<p style="color:var(--cinza);text-align:center;padding:20px 0">Nenhum resultado encontrado.</p>';
    return;
  }

  resultsEl.innerHTML = hits.map(h => {
    const snippet = h.texto.substring(0, 100).replace(/\n/g, ' ') + '…';
    return `<div class="search-card" onclick="openSection('${h.sectionId}')">
      <div class="sc-section">${h.sectionIcon} ${h.sectionName}</div>
      <div class="sc-title">${h.titulo}</div>
      <div class="sc-snippet">${snippet}</div>
    </div>`;
  }).join('');
}

// ── BUILD HOME ────────────────────────────────────────────────────────────────
const MENU_ITENS = [
  { id: 'lei_cultivo',  icone: '⚖️',  label: 'Lei de Cultivo',         sub: 'Habeas corpus, direitos e advogados' },
  { id: 'cultivo',      icone: '🌱',  label: 'Guia de Cultivo',         sub: 'Sementes, fases, colheita e cura' },
  { id: 'canabinoides', icone: '🔬',  label: 'Canabinoides & Terpenos', sub: 'THC, CBD, CBG, terpenos' },
  { id: 'variedades',   icone: '🌿',  label: 'Variedades & Strains',    sub: 'Kush, Haze, Hemp, Manga Rosa e mais' },
  { id: 'consumo',      icone: '💨',  label: 'Métodos de Consumo',      sub: 'Vaporização, óleo, oral' },
  { id: 'vaporizadores',icone: '🌬️', label: 'Vaporizadores',           sub: 'Tipos, câmaras, escolha' },
  { id: 'associacoes',  icone: '🏛️', label: 'Associações',             sub: 'Como se associar, documentos' },
  { id: 'onde_comprar', icone: '🛒',  label: 'Onde Comprar',            sub: 'Farmácias, associações, lojas' },
  { id: 'quiz',         icone: '🎯',  label: 'Quiz de Direcionamento',  sub: 'Descubra o que é ideal para você' },
];

function buildHome() {
  const grid = document.getElementById('menu-grid');
  grid.innerHTML = MENU_ITENS.map(item => `
    <button class="menu-btn" onclick="openSection('${item.id}')">
      <span class="m-icon">${item.icone}</span>
      <span class="m-label">${item.label}</span>
      <span class="m-sub">${item.sub}</span>
    </button>
  `).join('');
}

// ── OPEN SECTION ──────────────────────────────────────────────────────────────
function openSection(id) {
  if (id === 'quiz') {
    startQuiz();
    return;
  }
  const data = TODAS_SECOES.find(s => s.id === id);
  if (!data) return;
  buildContentScreen(data);
  showScreen('content');
}

// ── BUILD CONTENT SCREEN ──────────────────────────────────────────────────────
function buildContentScreen(data) {
  document.getElementById('content-icon').textContent  = data.icone;
  document.getElementById('content-title').textContent = data.titulo;

  const area = document.getElementById('content-scroll');
  let html = '';

  if (data.aviso_extra) {
    html += `<div class="aviso-extra">${data.aviso_extra}</div>`;
  }

  data.secoes.forEach(sec => {
    const parts = sec.titulo.split(' ');
    const emoji = parts[0];
    const rest  = parts.slice(1).join(' ');
    html += `<div class="section-title">
      <span class="st-emoji">${emoji}</span>
      <span class="st-text">${rest}</span>
    </div>`;

    sec.itens.forEach(([sub, txt]) => {
      html += `<div class="card">
        ${sub ? `<div class="card-sub">${sub}</div>` : ''}
        <div class="card-body">${txt}</div>
      </div>`;
    });
  });

  area.innerHTML = html;
  area.scrollTop = 0;
}

// ── QUIZ ──────────────────────────────────────────────────────────────────────
function startQuiz() {
  quizRespostas = {};
  quizPasso = 0;
  showScreen('quiz');
  renderQuizStep(0);
}

function renderQuizStep(idx) {
  const area = document.getElementById('quiz-scroll');
  updateProgressBar(idx);

  if (idx >= PERGUNTAS.length) {
    renderQuizResult();
    return;
  }

  const p     = PERGUNTAS[idx];
  const total = PERGUNTAS.length;

  let html = `
    <div class="quiz-prog-label">Pergunta ${idx + 1} de ${total}</div>
    <div class="quiz-question">${p.pergunta}</div>
  `;

  p.opcoes.forEach(([val, txt]) => {
    html += `<button class="quiz-option" onclick="quizResponder(${idx}, '${val}')">${txt}</button>`;
  });

  if (idx > 0) {
    html += `<button class="quiz-btn-prev" onclick="renderQuizStep(${idx - 1})">← Pergunta anterior</button>`;
  }

  area.innerHTML = html;
  area.scrollTop = 0;
}

function quizResponder(idx, val) {
  quizRespostas[PERGUNTAS[idx].id] = val;
  quizPasso = idx + 1;
  renderQuizStep(quizPasso);
}

function renderQuizResult() {
  const area = document.getElementById('quiz-scroll');
  const res  = calcularResultado(quizRespostas);
  updateProgressBar(PERGUNTAS.length);

  let html = `<div class="result-title">✨ Seu Resultado Personalizado</div>`;

  if (res.alerta) {
    html += `<div class="alerta-card">${res.alerta}</div>`;
  }

  html += resultCard('💊', 'Produto Recomendado',
    `${res.produto}<br><br><span style="color:var(--cinza)">${res.ratio}</span>`);

  html += resultCard('🌬️', 'Método de Consumo',
    `<b>${res.metodo}</b><br><br>${res.detalheMetodo}`);

  html += resultCard('🏛️', 'Como Acessar',
    `<b>${res.caminho}</b><br><br>${res.detalheCaminho}`);

  if (res.vaporizador) {
    html += resultCard('🌬️', 'Vaporizador Indicado',
      'Baseado na sua preferência por efeito imediato, um vaporizador de flor seca é a escolha ideal.<br><br>Confira a seção <b>Vaporizadores</b> no menu para guia completo de modelos e preços.');
  }

  html += `<div class="disclaimer">Este resultado é uma orientação geral baseada no seu perfil. Para uso medicinal, siga sempre a prescrição do seu médico e ajuste dosagens com acompanhamento profissional.</div>`;

  html += `<button class="btn-refazer" onclick="startQuiz()">🔄  Refazer o Quiz</button>`;

  area.innerHTML = html;
  area.scrollTop = 0;
}

function resultCard(icon, title, body) {
  return `<div class="result-card">
    <div class="rc-head"><span>${icon}</span> ${title}</div>
    <div class="rc-body">${body}</div>
  </div>`;
}

function updateProgressBar(passo) {
  const total = PERGUNTAS.length;
  const pct   = Math.round((Math.min(passo, total) / total) * 100);
  document.getElementById('quiz-progress').style.width = pct + '%';
}

// ── INIT ──────────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  buildHome();
  showScreen('home');
});
