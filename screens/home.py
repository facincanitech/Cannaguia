# screens/home.py — Tela inicial com menu principal e busca do CannaGuia

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.metrics import dp
from kivy.clock import Clock

from theme import (
    FUNDO_ESCURO, FUNDO_CARD, VERDE_ESCURO, VERDE_CLARO,
    VERDE_HOVER, TEXTO_BRANCO, TEXTO_CINZA, TEXTO_MUDO,
    TRANSPARENTE, EMOJI_FONT, LOGO_IMG,
)
from content import CULTIVO, CANABINOIDES, VARIEDADES, CONSUMO, VAPORIZADORES, ASSOCIACOES, ONDE_COMPRAR


# ── Menu principal ────────────────────────────────────────────────────────────
MENU_ITENS = [
    ('lei_cultivo',   '⚖️', 'Lei de Cultivo',          'Habeas corpus, direitos e advogados'),
    ('cultivo',       '🌱', 'Guia de Cultivo',          'Sementes, fases, colheita e cura'),
    ('canabinoides',  '🔬', 'Canabinoides',            'THC, CBD, terpenos e efeitos'),
    ('variedades',    '🌿', 'Variedades & Strains',    'Kush, Haze, Hemp, Manga Rosa e mais'),
    ('consumo',       '💨', 'Métodos de Consumo',      'Vaporização, sublingual, tópico'),
    ('vaporizadores', '🌬️', 'Vaporizadores',           'Tipos, câmaras e como escolher'),
    ('associacoes',   '🏛️', 'Associações',             'Como funciona no Brasil'),
    ('onde_comprar',  '🛒', 'Onde Comprar',            'Produtos, sementes e equipamentos'),
    ('quiz',          '🎯', 'Quiz de Direcionamento',  'Descubra o melhor caminho para você'),
]

# ── Índice de busca (construído uma vez ao importar) ──────────────────────────
_FONTES = [
    ('cultivo',       CULTIVO),
    ('canabinoides',  CANABINOIDES),
    ('variedades',    VARIEDADES),
    ('consumo',       CONSUMO),
    ('vaporizadores', VAPORIZADORES),
    ('associacoes',   ASSOCIACOES),
    ('onde_comprar',  ONDE_COMPRAR),
]

INDICE_BUSCA = []
for _tela, _dados in _FONTES:
    for _secao in _dados['secoes']:
        for _subtit, _texto in _secao['itens']:
            INDICE_BUSCA.append({
                'tela':   _tela,
                'icone':  _dados['icone'],
                'secao':  _dados['titulo'],
                'titulo': _subtit,
                'texto':  _texto,
                # campo pré-normalizado para busca rápida
                'indice': (_subtit + ' ' + _texto).lower(),
            })


def _buscar(query):
    """Retorna itens do índice que contenham todas as palavras da query."""
    palavras = query.lower().strip().split()
    if not palavras:
        return []
    return [
        item for item in INDICE_BUSCA
        if all(p in item['indice'] for p in palavras)
    ]


# ── Widgets ───────────────────────────────────────────────────────────────────

def _bg_solid(widget, cor):
    with widget.canvas.before:
        Color(*cor)
        r = Rectangle(pos=widget.pos, size=widget.size)
    widget.bind(pos=lambda i, v: setattr(r, 'pos', v),
                size=lambda i, v: setattr(r, 'size', v))


def _bg_round(widget, cor, raio=10):
    with widget.canvas.before:
        Color(*cor)
        r = RoundedRectangle(pos=widget.pos, size=widget.size, radius=[raio])
    widget.bind(pos=lambda i, v: setattr(r, 'pos', v),
                size=lambda i, v: setattr(r, 'size', v))


class BotaoMenu(Button):
    """Card de navegação do menu principal."""

    def __init__(self, icone, titulo, subtitulo, **kwargs):
        super().__init__(
            background_color=TRANSPARENTE,
            background_normal='',
            background_down='',
            size_hint_y=None,
            height=dp(88),
            **kwargs,
        )
        with self.canvas.before:
            self._cor_fundo = Color(*FUNDO_CARD)
            self._rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[12])
        self.bind(pos=self._upd, size=self._upd, state=self._on_state)

        layout = BoxLayout(orientation='horizontal', spacing=dp(12),
                           padding=(dp(14), dp(10)))
        layout.pos  = self.pos
        layout.size = self.size
        self.bind(pos=lambda i, v: setattr(layout, 'pos', v),
                  size=lambda i, v: setattr(layout, 'size', v))

        lbl_icone = Label(
            text=icone,
            font_name=EMOJI_FONT,
            font_size='30sp',
            size_hint=(None, 1),
            width=dp(48),
            halign='center',
            valign='middle',
        )

        col = BoxLayout(orientation='vertical', spacing=dp(2))
        lbl_titulo = Label(
            text=f'[b]{titulo}[/b]',
            markup=True,
            color=TEXTO_BRANCO,
            font_size='15sp',
            halign='left',
            valign='bottom',
        )
        lbl_titulo.bind(size=lambda i, s: setattr(i, 'text_size', s))

        lbl_sub = Label(
            text=subtitulo,
            color=TEXTO_CINZA,
            font_size='12sp',
            halign='left',
            valign='top',
        )
        lbl_sub.bind(size=lambda i, s: setattr(i, 'text_size', s))

        col.add_widget(lbl_titulo)
        col.add_widget(lbl_sub)

        seta = Label(
            text='›',
            color=VERDE_CLARO,
            font_size='24sp',
            size_hint=(None, 1),
            width=dp(24),
            halign='center',
            valign='middle',
        )

        layout.add_widget(lbl_icone)
        layout.add_widget(col)
        layout.add_widget(seta)
        self.add_widget(layout)

    def _upd(self, *_):
        self._rect.pos  = self.pos
        self._rect.size = self.size

    def _on_state(self, _inst, state):
        self._cor_fundo.rgba = VERDE_HOVER if state == 'down' else FUNDO_CARD


class CartaoBusca(Button):
    """Card de resultado de busca."""

    def __init__(self, icone, secao, titulo, snippet, **kwargs):
        super().__init__(
            background_color=TRANSPARENTE,
            background_normal='',
            background_down='',
            size_hint_y=None,
            **kwargs,
        )
        with self.canvas.before:
            self._cor = Color(*FUNDO_CARD)
            self._rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
        self.bind(pos=self._upd, size=self._upd, state=self._on_state)

        layout = BoxLayout(
            orientation='vertical',
            padding=(dp(12), dp(8)),
            spacing=dp(4),
        )
        layout.pos  = self.pos
        layout.size = self.size
        self.bind(pos=lambda i, v: setattr(layout, 'pos', v),
                  size=lambda i, v: setattr(layout, 'size', v))

        # Linha superior: ícone da seção + nome da seção
        lbl_secao = Label(
            text=f'{icone}  {secao}',
            font_name=EMOJI_FONT,
            color=VERDE_CLARO,
            font_size='11sp',
            size_hint_y=None,
            height=dp(18),
            halign='left',
            valign='middle',
        )
        lbl_secao.bind(size=lambda i, s: setattr(i, 'text_size', s))

        # Título do item
        lbl_titulo = Label(
            text=f'[b]{titulo}[/b]',
            markup=True,
            color=TEXTO_BRANCO,
            font_size='14sp',
            size_hint_y=None,
            halign='left',
            valign='top',
        )
        lbl_titulo.bind(width=lambda i, w: setattr(i, 'text_size', (w, None)))
        lbl_titulo.bind(texture_size=lambda i, ts: setattr(i, 'height', ts[1]))

        # Trecho do texto (máx 120 chars)
        trecho = snippet.replace('\n', ' ')[:120] + ('…' if len(snippet) > 120 else '')
        lbl_snip = Label(
            text=trecho,
            color=TEXTO_CINZA,
            font_size='12sp',
            size_hint_y=None,
            halign='left',
            valign='top',
        )
        lbl_snip.bind(width=lambda i, w: setattr(i, 'text_size', (w, None)))
        lbl_snip.bind(texture_size=lambda i, ts: setattr(i, 'height', ts[1]))

        layout.add_widget(lbl_secao)
        layout.add_widget(lbl_titulo)
        layout.add_widget(lbl_snip)
        self.add_widget(layout)

        # Ajustar altura do card ao conteúdo do layout interno
        layout.bind(minimum_height=lambda i, h: setattr(self, 'height', h + dp(16)))

    def _upd(self, *_):
        self._rect.pos  = self.pos
        self._rect.size = self.size

    def _on_state(self, _inst, state):
        self._cor.rgba = VERDE_HOVER if state == 'down' else FUNDO_CARD


# ── Tela Home ─────────────────────────────────────────────────────────────────

class TelaHome(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._debounce = None
        self._construir_ui()

    def _construir_ui(self):
        raiz = BoxLayout(orientation='vertical')
        _bg_solid(raiz, FUNDO_ESCURO)

        # ── Cabeçalho ─────────────────────────────────────────────────────────
        cabec = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(100),
            padding=(dp(12), dp(10)),
            spacing=dp(10),
        )
        _bg_solid(cabec, VERDE_ESCURO)

        img_logo = Image(
            source=LOGO_IMG,
            size_hint=(None, 1),
            width=dp(80),
            fit_mode='contain',
        )

        col_txt = BoxLayout(orientation='vertical', spacing=dp(2))
        lbl_nome = Label(
            text='[b]CannaGuia[/b]',
            markup=True,
            color=TEXTO_BRANCO,
            font_size='26sp',
            halign='left',
            valign='bottom',
        )
        lbl_nome.bind(size=lambda i, s: setattr(i, 'text_size', s))

        lbl_sub = Label(
            text='Cannabis Medicinal no Brasil',
            color=(0.8, 0.95, 0.8, 1),
            font_size='13sp',
            halign='left',
            valign='top',
        )
        lbl_sub.bind(size=lambda i, s: setattr(i, 'text_size', s))

        col_txt.add_widget(lbl_nome)
        col_txt.add_widget(lbl_sub)
        cabec.add_widget(img_logo)
        cabec.add_widget(col_txt)

        # ── Barra de busca ────────────────────────────────────────────────────
        barra = BoxLayout(
            size_hint_y=None,
            height=dp(48),
            padding=(dp(12), dp(6)),
        )
        _bg_solid(barra, (0.10, 0.10, 0.10, 1))

        self.campo_busca = TextInput(
            hint_text='🔍  Buscar no conteúdo...',
            font_name=EMOJI_FONT,
            font_size='14sp',
            foreground_color=TEXTO_BRANCO,
            hint_text_color=(*TEXTO_CINZA[:3], 0.6),
            background_color=(0.16, 0.16, 0.16, 1),
            cursor_color=VERDE_CLARO,
            multiline=False,
            padding=(dp(12), dp(8)),
        )
        # Borda verde ao focar
        self.campo_busca.bind(
            text=self._on_busca,
            focus=self._on_foco,
        )
        barra.add_widget(self.campo_busca)

        # ── Área de conteúdo (menu OU resultados) ─────────────────────────────
        self.scroll = ScrollView(do_scroll_x=False)
        self.grade  = GridLayout(
            cols=1,
            size_hint_y=None,
            padding=(dp(14), dp(10), dp(14), dp(20)),
            spacing=dp(10),
        )
        self.grade.bind(minimum_height=self.grade.setter('height'))
        self.scroll.add_widget(self.grade)
        self._montar_menu()

        # ── Rodapé ────────────────────────────────────────────────────────────
        rodape = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=dp(48),
            padding=(dp(8), dp(4)),
        )
        _bg_solid(rodape, (0.09, 0.09, 0.09, 1))

        lbl_av = Label(
            text='[color=#FF9800]⚠[/color]  Conteúdo informativo. Não substitui orientação médica.',
            markup=True,
            font_size='11sp',
            color=TEXTO_CINZA,
            halign='center',
            valign='middle',
        )
        lbl_av.bind(size=lambda i, s: setattr(i, 'text_size', (s[0] - dp(16), None)))

        lbl_cred = Label(
            text='[color=#3A7D44]Criado por FacincaniTech[/color]  [color=#666666]facincanitech@gmail.com[/color]',
            markup=True,
            font_size='10sp',
            color=TEXTO_MUDO,
            halign='center',
            valign='middle',
        )
        lbl_cred.bind(size=lambda i, s: setattr(i, 'text_size', s))

        rodape.add_widget(lbl_av)
        rodape.add_widget(lbl_cred)

        raiz.add_widget(cabec)
        raiz.add_widget(barra)
        raiz.add_widget(self.scroll)
        raiz.add_widget(rodape)
        self.add_widget(raiz)

    # ── Menu padrão ───────────────────────────────────────────────────────────

    def _montar_menu(self):
        self.grade.clear_widgets()

        lbl_escolha = Label(
            text='Escolha uma seção:',
            color=TEXTO_CINZA,
            font_size='13sp',
            size_hint_y=None,
            height=dp(28),
            halign='left',
            valign='middle',
        )
        lbl_escolha.bind(size=lambda i, s: setattr(i, 'text_size', s))
        self.grade.add_widget(lbl_escolha)

        for nome_tela, icone, titulo, subtitulo in MENU_ITENS:
            btn = BotaoMenu(icone, titulo, subtitulo)
            btn.bind(on_press=lambda inst, nt=nome_tela: self._navegar(nt))
            self.grade.add_widget(btn)

    # ── Busca ─────────────────────────────────────────────────────────────────

    def _on_foco(self, inst, focused):
        """Borda verde quando o campo está em foco."""
        inst.background_color = (0.18, 0.18, 0.18, 1) if focused else (0.16, 0.16, 0.16, 1)

    def _on_busca(self, _inst, texto):
        """Debounce de 300ms para não buscar a cada tecla."""
        if self._debounce:
            self._debounce.cancel()
        self._debounce = Clock.schedule_once(
            lambda dt: self._executar_busca(texto), 0.3
        )

    def _executar_busca(self, texto):
        self.grade.clear_widgets()
        texto = texto.strip()

        if not texto:
            self._montar_menu()
            return

        resultados = _buscar(texto)

        if not resultados:
            lbl = Label(
                text=f'Nenhum resultado para "[b]{texto}[/b]"',
                markup=True,
                color=TEXTO_CINZA,
                font_size='14sp',
                size_hint_y=None,
                height=dp(60),
                halign='center',
                valign='middle',
            )
            lbl.bind(size=lambda i, s: setattr(i, 'text_size', s))
            self.grade.add_widget(lbl)
            return

        lbl_qtd = Label(
            text=f'[color=#4CAF50]{len(resultados)}[/color] resultado(s) para "[b]{texto}[/b]"',
            markup=True,
            color=TEXTO_CINZA,
            font_size='13sp',
            size_hint_y=None,
            height=dp(30),
            halign='left',
            valign='middle',
        )
        lbl_qtd.bind(size=lambda i, s: setattr(i, 'text_size', s))
        self.grade.add_widget(lbl_qtd)

        for item in resultados[:30]:  # máx 30 resultados
            card = CartaoBusca(
                icone=item['icone'],
                secao=item['secao'],
                titulo=item['titulo'],
                snippet=item['texto'],
            )
            card.bind(on_press=lambda inst, nt=item['tela']: self._navegar(nt))
            self.grade.add_widget(card)

        self.scroll.scroll_y = 1

    # ── Navegação ─────────────────────────────────────────────────────────────

    def _navegar(self, nome_tela):
        self.manager.transition.direction = 'left'
        self.manager.current = nome_tela
