# main.py — Ponto de entrada do CannaGuia
# Aplicativo informativo sobre cannabis medicinal no Brasil
# Desenvolvido com Python + Kivy | Compatível com Buildozer (Android)

import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import platform

# Ajustar tamanho da janela para simulação desktop (ignorado no Android)
if platform not in ('android', 'ios'):
    Window.size = (400, 720)

# Registrar fonte com suporte a emoji
# Windows: usa Segoe UI Emoji | Android/Linux: usa fonte do sistema
_fontes_emoji = [
    'C:/Windows/Fonts/seguiemj.ttf',   # Windows 10/11
    'C:/Windows/Fonts/seguisym.ttf',   # fallback Windows
]
for _f in _fontes_emoji:
    if os.path.exists(_f):
        LabelBase.register('Emoji', _f)
        break

# Importar conteúdo estático
from content import CULTIVO, LEI_CULTIVO, CANABINOIDES, CONSUMO, VAPORIZADORES, ASSOCIACOES, ONDE_COMPRAR

# Importar telas
from screens.home       import TelaHome
from screens.base       import TelaBase
from screens.quiz       import TelaQuiz


class CannaGuiaApp(App):
    """Aplicativo principal CannaGuia."""

    title = 'CannaGuia — Cannabis Medicinal'

    def build(self):
        # Configurar cor de fundo padrão da janela
        Window.clearcolor = (0.071, 0.071, 0.071, 1)

        # Botão físico de voltar no Android
        Window.bind(on_keyboard=self._on_keyboard)

        # Gerenciador de telas com transição deslizante
        sm = ScreenManager(transition=SlideTransition())

        # ── Adicionar todas as telas ──────────────────────────────────────────
        sm.add_widget(TelaHome(name='home'))

        sm.add_widget(TelaBase(
            dados=CULTIVO,
            nome_anterior='home',
            name='cultivo',
        ))
        sm.add_widget(TelaBase(
            dados=LEI_CULTIVO,
            nome_anterior='home',
            name='lei_cultivo',
        ))
        sm.add_widget(TelaBase(
            dados=CANABINOIDES,
            nome_anterior='home',
            name='canabinoides',
        ))
        sm.add_widget(TelaBase(
            dados=CONSUMO,
            nome_anterior='home',
            name='consumo',
        ))
        sm.add_widget(TelaBase(
            dados=VAPORIZADORES,
            nome_anterior='home',
            name='vaporizadores',
        ))
        sm.add_widget(TelaBase(
            dados=ASSOCIACOES,
            nome_anterior='home',
            name='associacoes',
        ))
        sm.add_widget(TelaBase(
            dados=ONDE_COMPRAR,
            nome_anterior='home',
            name='onde_comprar',
        ))
        sm.add_widget(TelaQuiz(name='quiz'))

        return sm

    def _on_keyboard(self, _window, key, *args):
        """Intercepta botão físico de voltar no Android (tecla ESC = keycode 27)."""
        VOLTAR = 27   # ESC / back button Android
        if key == VOLTAR:
            sm = self.root
            if sm.current != 'home':
                sm.transition.direction = 'right'
                sm.current = 'home'
                return True  # consumir evento (não sair do app)
        return False


if __name__ == '__main__':
    CannaGuiaApp().run()
