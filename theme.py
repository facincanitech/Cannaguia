# theme.py — Configurações de tema e estilo do CannaGuia

# ── Cores (formato RGBA 0.0–1.0) ──────────────────────────────────────────────
FUNDO_ESCURO   = (0.071, 0.071, 0.071, 1)   # #121212 — fundo principal
FUNDO_CARD     = (0.118, 0.118, 0.118, 1)   # #1E1E1E — cartão
FUNDO_CARD2    = (0.169, 0.169, 0.169, 1)   # #2B2B2B — cartão alternativo
VERDE_ESCURO   = (0.157, 0.392, 0.196, 1)   # #286432 — cabeçalhos
VERDE_PRIMARIO = (0.227, 0.490, 0.267, 1)   # #3A7D44 — botões principais
VERDE_CLARO    = (0.298, 0.686, 0.314, 1)   # #4CAF50 — destaques
VERDE_HOVER    = (0.176, 0.345, 0.204, 1)   # #2D5834 — botão pressionado
TEXTO_BRANCO   = (0.878, 0.878, 0.878, 1)   # #E0E0E0 — texto principal
TEXTO_CINZA    = (0.620, 0.620, 0.620, 1)   # #9E9E9E — texto secundário
TEXTO_MUDO     = (0.400, 0.400, 0.400, 1)   # #666666 — texto suave
AMARELO_AVISO  = (1.000, 0.596, 0.000, 1)   # #FF9800 — avisos
AZUL_INFO      = (0.259, 0.647, 0.961, 1)   # #42A5F5 — informações
BRANCO_PURO    = (1.0,   1.0,   1.0,   1)
TRANSPARENTE   = (0.0,   0.0,   0.0,   0)

# ── Tamanhos de fonte ─────────────────────────────────────────────────────────
FONTE_TITULO   = '22sp'
FONTE_SUBTIT   = '18sp'
FONTE_NORMAL   = '15sp'
FONTE_PEQUENA  = '13sp'
FONTE_MICRO    = '11sp'

# ── Espaçamento ───────────────────────────────────────────────────────────────
PAD            = '16dp'
PAD_P          = '8dp'
PAD_G          = '24dp'
ALTURA_CABEC   = '60dp'
ALTURA_RODAPE  = '50dp'
RAIO           = [12,]

# ── Fonte com suporte a emoji ─────────────────────────────────────────────────
# Registrada em main.py; no Android o sistema já tem emoji nativo
EMOJI_FONT = 'Emoji'

# Nome do arquivo da imagem de logo na raiz do projeto
LOGO_IMG = 'screens/logo.png'

# ── Texto do aviso legal (usado em rodapé de todas as telas) ──────────────────
AVISO_LEGAL = (
    "[color=#FF9800][b]⚠ AVISO LEGAL:[/b][/color] "
    "Conteúdo exclusivamente informativo. Não substitui orientação médica. "
    "O uso de cannabis medicinal no Brasil exige prescrição médica. "
    "Consulte sempre um profissional de saúde habilitado."
)
