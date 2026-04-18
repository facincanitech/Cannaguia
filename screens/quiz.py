# screens/quiz.py — Quiz de direcionamento personalizado do CannaGuia

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.metrics import dp

from theme import (
    FUNDO_ESCURO, FUNDO_CARD, FUNDO_CARD2, VERDE_ESCURO, VERDE_PRIMARIO,
    VERDE_CLARO, VERDE_HOVER, TEXTO_BRANCO, TEXTO_CINZA,
    TRANSPARENTE, AVISO_LEGAL, EMOJI_FONT,
)


# ── Estrutura do quiz ─────────────────────────────────────────────────────────
PERGUNTAS = [
    {
        'id': 'finalidade',
        'pergunta': 'Qual é a sua principal finalidade?',
        'opcoes': [
            ('dor',        '🩹  Dor crônica / Dor neuropática'),
            ('ansiedade',  '🧠  Ansiedade, pânico ou TEPT'),
            ('epilepsia',  '⚡  Epilepsia ou convulsões'),
            ('sono',       '😴  Distúrbios do sono / Insônia'),
            ('recreativo', '😊  Uso recreativo / Bem-estar'),
            ('outro',      '❓  Outro / Não sei ainda'),
        ],
    },
    {
        'id': 'diagnostico',
        'pergunta': 'Você possui diagnóstico médico e acompanhamento profissional?',
        'opcoes': [
            ('sim', '✅  Sim — tenho médico acompanhando'),
            ('nao', '❌  Não — ainda não consultei um médico'),
        ],
    },
    {
        'id': 'gastrico',
        'pergunta': 'Você tem sensibilidade gástrica ou problemas intestinais?',
        'opcoes': [
            ('sim', '✅  Sim — tenho gastrite, SII ou sensibilidade'),
            ('nao', '❌  Não — sem problemas gastrointestinais'),
        ],
    },
    {
        'id': 'efeito',
        'pergunta': 'Qual tipo de início de efeito você prefere?',
        'opcoes': [
            ('imediato', '⚡  Imediato — efeito em minutos (vaporização)'),
            ('gradual',  '🌊  Gradual — efeito mais suave e duradouro (óleo/sublingual)'),
        ],
    },
    {
        'id': 'experiencia',
        'pergunta': 'Você tem experiência prévia com cannabis?',
        'opcoes': [
            ('sim', '✅  Sim — já usei cannabis antes'),
            ('nao', '🌱  Não — sou iniciante / nunca usei'),
        ],
    },
]


def calcular_resultado(respostas: dict) -> dict:
    """
    Algoritmo de recomendação baseado nas respostas do quiz.
    Retorna dict com produto, método, caminho, vaporizador recomendado.
    """
    finalidade  = respostas.get('finalidade', 'outro')
    diagnostico = respostas.get('diagnostico', 'nao') == 'sim'
    gastrico    = respostas.get('gastrico', 'nao') == 'sim'
    efeito      = respostas.get('efeito', 'gradual')
    experiencia = respostas.get('experiencia', 'nao') == 'sim'

    # ── Recomendação de produto ───────────────────────────────────────────────
    if finalidade == 'epilepsia':
        produto = 'CBD Alto (10:1 ou maior) — full spectrum ou isolado'
        ratio   = 'CBD dominante (ex.: 20:1 CBD:THC)'
    elif finalidade == 'ansiedade':
        produto = 'CBD Alto (10:1 ou maior) — broad spectrum ou isolado'
        ratio   = 'CBD dominante — THC mínimo para evitar piora da ansiedade'
    elif finalidade == 'dor':
        if experiencia:
            produto = 'Balanceado (1:1 CBD:THC) ou CBD moderado (5:1)'
            ratio   = 'Full spectrum 1:1 — sinergia para dor crônica'
        else:
            produto = 'CBD moderado (5:1 ou 10:1) — iniciar com THC baixo'
            ratio   = 'Começar com CBD alto e ajustar gradualmente'
    elif finalidade == 'sono':
        if experiencia:
            produto = 'Indica-dominante com CBN e/ou CBD (2:1)'
            ratio   = 'THC moderado + CBN para sono profundo'
        else:
            produto = 'CBD alto com linalol (terpeno sedativo)'
            ratio   = 'CBD alto — colheita tardia (mais CBN)'
    elif finalidade == 'recreativo':
        if experiencia:
            produto = 'Conforme preferência — híbrida ou sativa para dia, indica para noite'
            ratio   = 'THC moderado a alto, conforme tolerância'
        else:
            produto = 'CBD moderado (5:1) para primeiras experiências'
            ratio   = 'Iniciar com CBD — adaptar ao efeito antes de THC'
    else:
        produto = 'CBD moderado (5:1) como ponto de partida'
        ratio   = 'Consultar médico para orientação personalizada'

    # ── Recomendação de método ────────────────────────────────────────────────
    if efeito == 'imediato':
        metodo = 'Vaporização de flor seca ou concentrado'
        detalhe_metodo = (
            'Vaporizador portátil ou desktop. Temperatura 170–185°C. '
            'Efeito em 5–15 minutos, duração 1–3 horas.'
        )
        vaporizador = True
    else:
        if gastrico:
            metodo = 'Óleo sublingual (sob a língua)'
            detalhe_metodo = (
                'Manter o óleo sob a língua por 60–90 segundos antes de engolir. '
                'Absorção pela mucosa evita o trato digestivo. '
                'Efeito em 15–45 min, duração 4–8 horas.'
            )
        else:
            metodo = 'Óleo sublingual ou cápsulas'
            detalhe_metodo = (
                'Sublingual: início em 15–45 min. '
                'Cápsulas: início em 30–90 min, efeito mais uniforme. '
                'Duração 4–8 horas. Ideal para uso contínuo.'
            )
        vaporizador = False

    # ── Recomendação de caminho de acesso ─────────────────────────────────────
    if not diagnostico:
        caminho = 'Primeiro passo: consultar médico'
        detalhe_caminho = (
            'Sem laudo médico não é possível acessar produtos via farmácia nem a maioria '
            'das associações. Plataformas como Dr. Cannabis conectam você a médicos '
            'especializados em cannabis medicinal para consulta online.'
        )
    elif finalidade == 'epilepsia':
        caminho = 'Farmácia (Anvisa) ou Associação'
        detalhe_caminho = (
            'Para epilepsia, há produtos aprovados pela Anvisa (Canabidiol Prati, Epidiolex). '
            'Associações oferecem maior variedade e custo-benefício. '
            'Seu médico neurologista pode te orientar sobre a melhor formulação.'
        )
    elif finalidade in ['dor', 'ansiedade', 'sono']:
        caminho = 'Associação de Cannabis (recomendado) ou Farmácia'
        detalhe_caminho = (
            'Associações oferecem maior variedade de produtos, full spectrum e '
            'custo 3–5x menor que farmácias. Veja a seção "Associações" para '
            'lista das principais e como se associar.'
        )
    else:
        caminho = 'Associação de Cannabis'
        detalhe_caminho = (
            'Para o seu perfil, uma associação de cannabis oferece a maior '
            'flexibilidade de produtos. Consulte a seção "Associações" no app.'
        )

    # ── Alerta especial para epilepsia ────────────────────────────────────────
    alerta = None
    if finalidade == 'epilepsia':
        alerta = (
            '⚠️  IMPORTANTE: Epilepsia requer acompanhamento médico rigoroso. '
            'Nunca suspenda medicamentos anticonvulsivantes sem orientação médica. '
            'A cannabis medicinal pode ser usada como terapia complementar.'
        )
    elif not diagnostico:
        alerta = (
            '⚠️  Sem diagnóstico médico, o uso de cannabis pode mascarar condições '
            'que precisam de tratamento específico. Busque orientação profissional antes.'
        )

    return {
        'produto':         produto,
        'ratio':           ratio,
        'metodo':          metodo,
        'detalhe_metodo':  detalhe_metodo,
        'caminho':         caminho,
        'detalhe_caminho': detalhe_caminho,
        'vaporizador':     vaporizador,
        'alerta':          alerta,
    }


# ── Widgets auxiliares ────────────────────────────────────────────────────────

def _bg_solid(widget, cor):
    with widget.canvas.before:
        cor_i = Color(*cor)
        rect  = Rectangle(pos=widget.pos, size=widget.size)
    widget.bind(pos=lambda i, v: setattr(rect, 'pos', v),
                size=lambda i, v: setattr(rect, 'size', v))


def _bg_round(widget, cor, raio=10):
    with widget.canvas.before:
        cor_i = Color(*cor)
        rect  = RoundedRectangle(pos=widget.pos, size=widget.size, radius=[raio])
    widget.bind(pos=lambda i, v: setattr(rect, 'pos', v),
                size=lambda i, v: setattr(rect, 'size', v))


class BotaoOpcao(Button):
    """Botão de opção do quiz com estilo de card."""

    def __init__(self, texto, **kwargs):
        super().__init__(
            text=texto,
            font_name=EMOJI_FONT,
            background_color=TRANSPARENTE,
            background_normal='',
            background_down='',
            color=TEXTO_BRANCO,
            font_size='14sp',
            size_hint_y=None,
            height=dp(54),
            halign='left',
            valign='middle',
            **kwargs,
        )
        self.text_size = (None, None)
        with self.canvas.before:
            self._cor = Color(*FUNDO_CARD)
            self._rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
        self.bind(pos=self._upd, size=self._upd)
        self.bind(state=self._on_state)
        # Ajustar text_size para não cortar texto longo
        self.bind(size=lambda i, s: setattr(i, 'text_size', (s[0] - dp(20), None)))
        self.bind(texture_size=lambda i, ts: setattr(i, 'height', max(dp(54), ts[1] + dp(20))))

    def _upd(self, *a):
        self._rect.pos  = self.pos
        self._rect.size = self.size

    def _on_state(self, inst, state):
        self._cor.rgba = VERDE_HOVER if state == 'down' else FUNDO_CARD


class CartaoResultado(BoxLayout):
    """Cartão de resultado com título colorido e texto explicativo."""

    def __init__(self, icone, titulo, texto, cor_titulo=None, **kwargs):
        super().__init__(
            orientation='vertical',
            padding=dp(14),
            spacing=dp(6),
            size_hint_y=None,
            **kwargs,
        )
        _bg_round(self, FUNDO_CARD2, raio=12)
        self.bind(minimum_height=self.setter('height'))

        cor = cor_titulo or VERDE_CLARO

        lbl_titulo = Label(
            text=f'[b]{icone}  {titulo}[/b]',
            markup=True,
            color=cor,
            font_size='15sp',
            size_hint_y=None,
            halign='left',
            valign='top',
        )
        lbl_titulo.bind(width=lambda i, w: setattr(i, 'text_size', (w, None)))
        lbl_titulo.bind(texture_size=lambda i, ts: setattr(i, 'height', ts[1] + dp(4)))

        lbl_texto = Label(
            text=texto,
            markup=True,
            color=TEXTO_BRANCO,
            font_size='13sp',
            size_hint_y=None,
            halign='left',
            valign='top',
        )
        lbl_texto.bind(width=lambda i, w: setattr(i, 'text_size', (w, None)))
        lbl_texto.bind(texture_size=lambda i, ts: setattr(i, 'height', ts[1] + dp(4)))

        self.add_widget(lbl_titulo)
        self.add_widget(lbl_texto)


# ── Tela principal do Quiz ────────────────────────────────────────────────────

class TelaQuiz(Screen):
    """
    Tela de quiz com fluxo passo a passo.
    Coleta 5 respostas e exibe resultado personalizado.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.respostas   = {}
        self.passo_atual = 0
        self._construir_frame()
        self._mostrar_passo(0)

    # ── Estrutura da tela ─────────────────────────────────────────────────────

    def _construir_frame(self):
        self.raiz = BoxLayout(orientation='vertical')
        _bg_solid(self.raiz, FUNDO_ESCURO)

        # Cabeçalho
        cabec = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(58),
            padding=(dp(8), dp(4)),
            spacing=dp(8),
        )
        _bg_solid(cabec, VERDE_ESCURO)

        self.btn_voltar = Button(
            text='← Voltar',
            font_name=EMOJI_FONT,
            size_hint=(None, 1),
            width=dp(90),
            font_size='14sp',
            color=TEXTO_BRANCO,
            background_color=TRANSPARENTE,
            background_normal='',
        )
        self.btn_voltar.bind(on_press=self._voltar_home)

        self.lbl_titulo_cab = Label(
            text='[b]🎯  Quiz de Direcionamento[/b]',
            font_name=EMOJI_FONT,
            markup=True,
            color=TEXTO_BRANCO,
            font_size='16sp',
            halign='left',
            valign='middle',
        )
        self.lbl_titulo_cab.bind(
            size=lambda i, s: setattr(i, 'text_size', s))

        cabec.add_widget(self.btn_voltar)
        cabec.add_widget(self.lbl_titulo_cab)

        # Barra de progresso
        self.barra_prog = BoxLayout(
            size_hint_y=None,
            height=dp(6),
        )
        _bg_solid(self.barra_prog, (0.15, 0.15, 0.15, 1))
        with self.barra_prog.canvas.after:
            Color(*VERDE_CLARO)
            self._prog_rect = Rectangle(pos=self.barra_prog.pos, size=(0, dp(6)))
        self.barra_prog.bind(pos=self._atualizar_barra,
                             size=self._atualizar_barra)

        # Área de conteúdo central (será substituída a cada passo)
        self.scroll = ScrollView(do_scroll_x=False)
        self.grade  = GridLayout(
            cols=1,
            size_hint_y=None,
            padding=(dp(16), dp(16), dp(16), dp(20)),
            spacing=dp(10),
        )
        self.grade.bind(minimum_height=self.grade.setter('height'))
        self.scroll.add_widget(self.grade)

        # Rodapé
        rodape = Label(
            text=AVISO_LEGAL,
            markup=True,
            font_size='11sp',
            color=TEXTO_CINZA,
            size_hint_y=None,
            height=dp(48),
            halign='center',
            valign='middle',
        )
        rodape.bind(
            size=lambda i, s: setattr(i, 'text_size', (s[0] - dp(20), None)))
        _bg_solid(rodape, (0.09, 0.09, 0.09, 1))

        self.raiz.add_widget(cabec)
        self.raiz.add_widget(self.barra_prog)
        self.raiz.add_widget(self.scroll)
        self.raiz.add_widget(rodape)
        self.add_widget(self.raiz)

    # ── Renderização de passos ────────────────────────────────────────────────

    def _mostrar_passo(self, idx):
        """Renderiza a pergunta do passo idx na grade de conteúdo."""
        self.grade.clear_widgets()
        self._atualizar_barra()

        if idx >= len(PERGUNTAS):
            self._mostrar_resultado()
            return

        pergunta = PERGUNTAS[idx]
        total    = len(PERGUNTAS)

        # Indicador de progresso textual
        lbl_prog = Label(
            text=f'[color=#4CAF50]Pergunta {idx + 1} de {total}[/color]',
            markup=True,
            color=TEXTO_CINZA,
            font_size='13sp',
            size_hint_y=None,
            height=dp(28),
            halign='right',
            valign='middle',
        )
        lbl_prog.bind(size=lambda i, s: setattr(i, 'text_size', s))

        # Texto da pergunta
        lbl_q = Label(
            text=f'[b]{pergunta["pergunta"]}[/b]',
            markup=True,
            color=TEXTO_BRANCO,
            font_size='17sp',
            size_hint_y=None,
            halign='left',
            valign='top',
        )
        lbl_q.bind(width=lambda i, w: setattr(i, 'text_size', (w, None)))
        lbl_q.bind(texture_size=lambda i, ts: setattr(i, 'height', ts[1] + dp(10)))

        self.grade.add_widget(lbl_prog)
        self.grade.add_widget(lbl_q)

        # Botões de opção
        for valor, texto in pergunta['opcoes']:
            btn = BotaoOpcao(texto)
            btn.bind(on_press=lambda inst, v=valor, i=idx: self._responder(i, v))
            self.grade.add_widget(btn)

        # Botão voltar passo (se não for o primeiro)
        if idx > 0:
            btn_ant = Button(
                text='← Pergunta anterior',
                size_hint_y=None,
                height=dp(40),
                font_size='13sp',
                color=TEXTO_CINZA,
                background_color=TRANSPARENTE,
                background_normal='',
            )
            btn_ant.bind(on_press=lambda inst: self._mostrar_passo(idx - 1))
            self.grade.add_widget(btn_ant)

    def _responder(self, idx_passo, valor):
        """Registra resposta e avança para o próximo passo."""
        pergunta_id              = PERGUNTAS[idx_passo]['id']
        self.respostas[pergunta_id] = valor
        self.passo_atual         = idx_passo + 1
        self._mostrar_passo(self.passo_atual)
        self.scroll.scroll_y = 1  # voltar ao topo

    def _mostrar_resultado(self):
        """Calcula e exibe os cartões de resultado personalizado."""
        self.grade.clear_widgets()
        res = calcular_resultado(self.respostas)

        # Título
        lbl_t = Label(
            text='[b]✨  Seu Resultado Personalizado[/b]',
            markup=True,
            color=VERDE_CLARO,
            font_size='19sp',
            size_hint_y=None,
            halign='left',
            valign='top',
        )
        lbl_t.bind(width=lambda i, w: setattr(i, 'text_size', (w, None)))
        lbl_t.bind(texture_size=lambda i, ts: setattr(i, 'height', ts[1] + dp(8)))
        self.grade.add_widget(lbl_t)

        # Alerta especial (se houver)
        if res['alerta']:
            lbl_al = Label(
                text=f'[color=#FF9800]{res["alerta"]}[/color]',
                markup=True,
                color=TEXTO_BRANCO,
                font_size='13sp',
                size_hint_y=None,
                halign='left',
                valign='top',
            )
            _bg_round(lbl_al, (0.30, 0.18, 0.02, 1), raio=8)
            lbl_al.padding = (dp(12), dp(10))
            lbl_al.bind(width=lambda i, w: setattr(i, 'text_size', (w - dp(24), None)))
            lbl_al.bind(texture_size=lambda i, ts: setattr(i, 'height', ts[1] + dp(20)))
            self.grade.add_widget(lbl_al)

        # Cartões de resultado
        self.grade.add_widget(CartaoResultado(
            '💊', 'Produto Recomendado',
            f'{res["produto"]}\n\n[color=#9E9E9E]{res["ratio"]}[/color]',
        ))
        self.grade.add_widget(CartaoResultado(
            '🌬️', 'Método de Consumo',
            f'[b]{res["metodo"]}[/b]\n\n{res["detalhe_metodo"]}',
        ))
        self.grade.add_widget(CartaoResultado(
            '🏛️', 'Como Acessar',
            f'[b]{res["caminho"]}[/b]\n\n{res["detalhe_caminho"]}',
        ))

        if res['vaporizador']:
            self.grade.add_widget(CartaoResultado(
                '🌬️', 'Vaporizador Indicado',
                'Baseado na sua preferência por efeito imediato, '
                'um vaporizador de flor seca é a escolha ideal.\n\n'
                'Confira a seção [b]Vaporizadores[/b] no menu para '
                'guia completo de modelos e preços.',
                cor_titulo=AZUL_INFO if False else VERDE_CLARO,
            ))

        # Disclaimer final
        disc = Label(
            text=(
                '[color=#666666]Este resultado é uma orientação geral baseada no '
                'seu perfil. Para uso medicinal, siga sempre a prescrição do seu '
                'médico e ajuste dosagens com acompanhamento profissional.[/color]'
            ),
            markup=True,
            font_size='12sp',
            size_hint_y=None,
            halign='left',
            valign='top',
        )
        disc.bind(width=lambda i, w: setattr(i, 'text_size', (w, None)))
        disc.bind(texture_size=lambda i, ts: setattr(i, 'height', ts[1] + dp(8)))
        self.grade.add_widget(disc)

        # Botão refazer quiz
        btn_refazer = Button(
            text='🔄  Refazer o Quiz',
            size_hint_y=None,
            height=dp(50),
            font_size='15sp',
            color=TEXTO_BRANCO,
            background_color=TRANSPARENTE,
            background_normal='',
        )
        _bg_round(btn_refazer, VERDE_PRIMARIO, raio=10)
        btn_refazer.bind(on_press=lambda inst: self._reiniciar())
        self.grade.add_widget(btn_refazer)

        self.scroll.scroll_y = 1

    # ── Utilitários ───────────────────────────────────────────────────────────

    def _atualizar_barra(self, *args):
        total   = len(PERGUNTAS)
        passo   = min(self.passo_atual, total)
        largura = self.barra_prog.width * (passo / total)
        self._prog_rect.pos  = self.barra_prog.pos
        self._prog_rect.size = (largura, dp(6))

    def _reiniciar(self):
        self.respostas   = {}
        self.passo_atual = 0
        self._mostrar_passo(0)
        self._atualizar_barra()

    def _voltar_home(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
