[app]

# ── Informações do app ────────────────────────────────────────────────────────
title           = CannaGuia
package.name    = cannaguia
package.domain  = br.cannaguia
source.dir      = .
source.include_exts = py,png,jpg,kv,atlas,ttf
source.include_patterns = logo.png
version         = 1.0.0

# ── Dependências Python ───────────────────────────────────────────────────────
requirements    = python3,kivy

# ── Orientação e interface ────────────────────────────────────────────────────
orientation     = portrait
fullscreen      = 0

# ── Ícone e splash (adicionar arquivos na raiz do projeto) ────────────────────
icon.filename     = logo.png
presplash.filename = logo.png

# ── Android ───────────────────────────────────────────────────────────────────
android.permissions     = INTERNET
android.api             = 33
android.minapi          = 21
android.sdk             = 33
android.ndk             = 25b
android.ndk_api         = 21
android.accept_sdk_license = True
android.arch            = arm64-v8a

# ── iOS (não configurado) ────────────────────────────────────────────────────
# ios.kivy_ios_url    = https://github.com/kivy/kivy-ios
# ios.kivy_ios_branch = master

# ── Log e debug ───────────────────────────────────────────────────────────────
log_level       = 2
warn_on_root    = 1

[buildozer]
# Diretório de build (gerado automaticamente)
build_dir    = .buildozer
bin_dir      = ./bin

# Usar versão mais recente do buildozer e python-for-android
# Instalar com: pip install buildozer
# Build:        buildozer android debug
# Deploy:       buildozer android deploy run logcat
