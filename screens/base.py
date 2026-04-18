# screens/base.py — Tela base reutilizável para seções de conteúdo

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.metrics import dp

from theme import (
    FUNDO_ESCURO, FUNDO_CARD, VERDE_ESCURO,
    VERDE_CLARO, TEXTO_BRANCO, TEXTO_CINZA, AVISO_LEGAL,
    TRANSPARENTE, EMOJI_FONT,
)


def _bg(widget, cor):
    """Aplica cor de fundo retangular a um widget via canvas."""
    with widget.canvas.before:
        cor_inst = Color(*cor)
        rect = Rectangle(pos=widget.pos, size=widget.size)

    def atualizar(inst, _val):
        rect.pos = inst.pos
        rect.size = inst.size

    widget.bind(pos=atualizar, size=atualizar)
    return cor_inst, rect


def _bg_round(widget, cor, raio=12):
    """Aplica cor de fundo arredondado via canvas."""
    with widget.canvas.before:
        cor_inst = Color(*cor)
        rect = RoundedRectangle(pos=widget.pos, size=widget.size, radius=[raio])

    def atualizar(inst, _val):
        rect.pos = inst.pos
        rect.size = inst.size

    widget.bind(pos=atualizar, size=atualizar)
    return cor_inst, rect


class CartaoConteudo(BoxLayout):
    """Cartão visual para exibir um item de conteúdo (subtítulo + texto)."""

    def __init__(self, subtitulo, texto, **kwargs):
        super().__init__(orientation='vertical', padding=dp(14),
                         spacing=dp(8), size_hint_y=None, **kwargs)
        _bg_round(self, FUNDO_CARD, raio=10)
        self.bind(minimum_height=self.setter('height'))

        if subtitulo:
            lbl_sub = Label(
                text=f'[b]{subtitulo}[/b]',
                markup=True,
                font_name=EMOJI_FONT,
                color=VERDE_CLARO,
                font_size='15sp',
                size_hint_y=None,
                halign='left',
                valign='top',
            )
            lbl_sub.bind(width=lambda inst, w: setattr(inst, 'text_size', (w, None)))
            lbl_sub.bind(texture_size=lambda inst, sz: setattr(inst, 'height', sz[1]))
            self.add_widget(lbl_sub)

        lbl_txt = Label(
            text=texto,
            markup=True,
            font_name=EMOJI_FONT,
            color=TEXTO_BRANCO,
            font_size='14sp',
            size_hint_y=None,
            halign='left',
            valign='top',
        )
        lbl_txt.bind(width=lambda inst, w: setattr(inst, 'text_size', (w, None)))
        lbl_txt.bind(texture_size=lambda inst, sz: setattr(inst, 'height', sz[1]))
        self.add_widget(lbl_txt)


class SecaoTitulo(BoxLayout):
    """Linha de título de seção: ícone emoji + texto em verde."""

    def __init__(self, texto, **kwargs):
        super().__init__(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(40),
            spacing=dp(6),
            **kwargs,
        )
        # Separar emoji do resto do texto (ex: '🌰 Sementes vs Clones')
        partes = texto.split(' ', 1)
        emoji = partes[0] if len(partes) > 1 else ''
        resto = partes[1] if len(partes) > 1 else texto

        if emoji:
            lbl_em = Label(
                text=emoji,
                font_name=EMOJI_FONT,
                font_size='17sp',
                size_hint=(None, 1),
                width=dp(28),
                halign='center',
                valign='middle',
            )
            self.add_widget(lbl_em)

        lbl_txt = Label(
            text=f'[b]{resto}[/b]',
            markup=True,
            color=VERDE_CLARO,
            font_size='17sp',
            halign='left',
            valign='middle',
        )
        lbl_txt.bind(size=lambda inst, sz: setattr(inst, 'text_size', sz))
        self.add_widget(lbl_txt)


class AvisoExtra(Label):
    """Label de aviso especial (ex.: aviso de legalidade no cultivo)."""

    def __init__(self, texto, **kwargs):
        super().__init__(
            text=texto,
            markup=True,
            color=TEXTO_BRANCO,
            font_size='13sp',
            size_hint_y=None,
            halign='left',
            valign='top',
            **kwargs,
        )
        _bg_round(self, (0.300, 0.180, 0.020, 1), raio=8)
        self.padding = (dp(12), dp(10))
        self.bind(width=lambda inst, w: setattr(inst, 'text_size', (w - dp(24), None)))
        self.bind(texture_size=lambda inst, sz: setattr(inst, 'height', sz[1] + dp(20)))


class TelaBase(Screen):
    """
    Tela base para todas as seções de conteúdo.
    Recebe um dict de conteúdo e renderiza automaticamente.
    """

    def __init__(self, dados, nome_anterior='home', **kwargs):
        super().__init__(**kwargs)
        self.dados = dados
        self.nome_anterior = nome_anterior
        self._construir_ui()

    def _construir_ui(self):
        raiz = BoxLayout(orientation='vertical')
        _bg(raiz, FUNDO_ESCURO)

        # ── Cabeçalho ────────────────────────────────────────────────────────
        cabec = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(58),
            padding=(dp(8), dp(4)),
            spacing=dp(8),
        )
        _bg(cabec, VERDE_ESCURO)

        btn_voltar = Button(
            text='← Voltar',
            font_name=EMOJI_FONT,
            size_hint=(None, 1),
            width=dp(90),
            font_size='14sp',
            color=TEXTO_BRANCO,
            background_color=TRANSPARENTE,
            background_normal='',
        )
        btn_voltar.bind(on_press=self._voltar)

        icone = self.dados.get('icone', '')
        titulo = self.dados.get('titulo', '')

        # Ícone emoji em fonte separada para renderizar corretamente no Windows
        lbl_icone = Label(
            text=icone,
            font_name=EMOJI_FONT,
            font_size='22sp',
            size_hint=(None, 1),
            width=dp(34),
            halign='center',
            valign='middle',
        )

        lbl_titulo = Label(
            text=f'[b]{titulo}[/b]',
            markup=True,
            color=TEXTO_BRANCO,
            font_size='17sp',
            halign='left',
            valign='middle',
        )
        lbl_titulo.bind(size=lambda inst, sz: setattr(inst, 'text_size', sz))

        cabec.add_widget(btn_voltar)
        cabec.add_widget(lbl_icone)
        cabec.add_widget(lbl_titulo)

        # ── Área de conteúdo rolável ──────────────────────────────────────────
        scroll = ScrollView(do_scroll_x=False)
        grade = GridLayout(
            cols=1,
            size_hint_y=None,
            padding=(dp(14), dp(12), dp(14), dp(16)),
            spacing=dp(10),
        )
        grade.bind(minimum_height=grade.setter('height'))

        # Aviso extra (cultivo, etc.)
        aviso_extra = self.dados.get('aviso_extra')
        if aviso_extra:
            grade.add_widget(AvisoExtra(aviso_extra))

        # Seções e itens
        for secao in self.dados.get('secoes', []):
            grade.add_widget(SecaoTitulo(secao['titulo']))
            for subtit, texto in secao.get('itens', []):
                grade.add_widget(CartaoConteudo(subtit, texto))

        scroll.add_widget(grade)

        # ── Rodapé com aviso legal ────────────────────────────────────────────
        rodape = Label(
            text=AVISO_LEGAL,
            markup=True,
            font_size='11sp',
            color=TEXTO_CINZA,
            size_hint_y=None,
            height=dp(50),
            halign='center',
            valign='middle',
        )
        rodape.bind(size=lambda inst, sz: setattr(inst, 'text_size', (sz[0] - dp(20), None)))
        _bg(rodape, (0.09, 0.09, 0.09, 1))

        raiz.add_widget(cabec)
        raiz.add_widget(scroll)
        raiz.add_widget(rodape)
        self.add_widget(raiz)

    def _voltar(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = self.nome_anterior
