# content.py — Todo o conteúdo estático informativo do CannaGuia
# Estruturado como dicionários para facilitar renderização dinâmica

# ─────────────────────────────────────────────────────────────────────────────
# GUIA DE CULTIVO
# ─────────────────────────────────────────────────────────────────────────────
CULTIVO = {
    'titulo': 'Guia de Cultivo',
    'icone': '🌱',
    'aviso_extra': (
        "[color=#FF9800][b]⚠ ATENÇÃO:[/b][/color] No Brasil, o cultivo de cannabis "
        "é proibido sem autorização expressa da Anvisa (Lei 11.343/2006). "
        "Este conteúdo é exclusivamente educacional."
    ),
    'secoes': [
        {
            'titulo': '🌰 Sementes vs Clones',
            'itens': [
                ('Sementes — Vantagens',
                 'Maior diversidade genética, sem risco de transmissão de pragas e '
                 'doenças via material vegetativo, vigor híbrido em F1, facilidade de '
                 'armazenamento e transporte.'),
                ('Tipos de Sementes',
                 '[b]Regulares:[/b] Produzem machos e fêmeas (50/50). Usadas para cruzamentos.\n\n'
                 '[b]Feminizadas:[/b] Geneticamente modificadas para produzir quase 100% fêmeas. '
                 'Ideal para cultivo medicinal — apenas fêmeas produzem flores ricas em canabinoides.\n\n'
                 '[b]Autoflorescentes:[/b] Florescem por idade (geralmente 70–90 dias), '
                 'independentemente do fotoperíodo. Ótimas para iniciantes.'),
                ('Clones — Vantagens',
                 'Cópia genética exata da planta-mãe, sexo garantido, uniformidade '
                 'na produção, início mais rápido sem fase de germinação. '
                 'Risco: podem transmitir pragas e doenças da planta-mãe.'),
            ]
        },
        {
            'titulo': '🌿 Fases da Planta',
            'itens': [
                ('Germinação (3–7 dias)',
                 'A semente absorve água e a radícula (raiz embrionária) rompe a casca. '
                 'Temperatura ideal: 22–26°C. Umidade: 70–90%. '
                 'Método mais simples: entre dois lenços úmidos, em local escuro e quente.'),
                ('Muda / Seedling (2–3 semanas)',
                 'Surgem os primeiros cotilédones e depois as folhas serrilhadas características. '
                 'Luz: 18h/dia. Temperatura: 20–26°C. Umidade: 60–70%. '
                 'Solo bem drenado, regas leves. Evitar sobrefertilização.'),
                ('Fase Vegetativa (4–8 semanas)',
                 'A planta cresce em altura e desenvolve estrutura. '
                 'Fotoperíodo: 18h luz / 6h escuro. '
                 'Nutrição: [b]Nitrogênio (N)[/b] alto para crescimento foliar. '
                 'Técnicas: LST (Low Stress Training), topping, SCROG para controle de altura '
                 'e aumento de produção.'),
                ('Floração (8–12 semanas)',
                 'Induzida reduzindo luz para 12h/dia (exceto autoflorescentes). '
                 'Surgem os cálices, pistilos e tricomas. '
                 'Nutrição: reduzir N, aumentar [b]Fósforo (P)[/b] e [b]Potássio (K)[/b]. '
                 'Semana 6–8: flush final com água pura para eliminar resíduos de nutrientes.'),
            ]
        },
        {
            'titulo': '✂️ Colheita',
            'itens': [
                ('Quando Colher — Tricomas',
                 'O método mais preciso usa lupa 60–100x ou microscópio para observar tricomas:\n\n'
                 '[b]Transparentes/Cristalinos:[/b] Muito cedo — THC ainda se formando.\n'
                 '[b]Leitosos/Opacos:[/b] THC máximo — efeito mais cerebral e energético.\n'
                 '[b]Âmbar (20–30%):[/b] THC convertendo em CBN — efeito mais sedativo e corporal.\n\n'
                 'Para uso medicinal: geralmente 70–80% leitosos + 10–20% âmbar.'),
                ('Quando Colher — Pistilos',
                 'Método visual sem equipamento:\n'
                 '[b]50–70% escuros/curvados:[/b] Colheita precoce.\n'
                 '[b]70–90% escuros/curvados:[/b] Maturação ideal.\n'
                 '[b]90–100% escuros:[/b] Colheita tardia (mais CBN, menos THC).'),
                ('Processo de Corte',
                 'Cortar ramos principais ou planta inteira. '
                 'Remover folhas fan (grandes, sem tricomas). '
                 'Pendurar de cabeça para baixo em local escuro, '
                 'temperatura 18–22°C, umidade 50–55%, ventilação suave. '
                 'Secagem: 7–14 dias até galhos quebrarem ao dobrar.'),
            ]
        },
        {
            'titulo': '🫙 Cura',
            'itens': [
                ('Por que Curar?',
                 'A cura decompõe clorofila (reduz sabor de grama), '
                 'converte amidos em açúcares, melhora aroma e sabor, '
                 'potencializa efeitos e prolonga a conservação do material. '
                 'Flores curadas podem durar 1–2 anos sem perda significativa.'),
                ('Como Curar',
                 '1. Colocar flores em potes de vidro herméticos (Mason jars) — '
                 '75% cheios para deixar ar circular.\n'
                 '2. Primeiros 7–14 dias: abrir os potes 1–2x/dia por 15–30 min '
                 '(processo chamado "burping") para liberar gases.\n'
                 '3. Manter em local escuro, 18–22°C, umidade interna 60–65% '
                 '(usar Boveda 62 para controle preciso).\n'
                 '4. Cura mínima: 2–3 semanas. Ideal: 4–8 semanas. '
                 'Premium: 3–6 meses.'),
                ('Sinais de Problemas',
                 '[b]Mofo (Botrytis):[/b] Manchas cinza/brancas, odor de bafio — '
                 'descartar material afetado imediatamente.\n'
                 '[b]Muito seco:[/b] Tricomas se quebram, fumaça áspera — '
                 'adicionar casca de laranja por 1 hora.\n'
                 '[b]Muito úmido:[/b] Flores pegajosas em excesso — '
                 'deixar tampa aberta por mais tempo.'),
            ]
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# LEI DE CULTIVO (categoria separada)
# ─────────────────────────────────────────────────────────────────────────────
LEI_CULTIVO = {
    'titulo': 'Lei de Cultivo',
    'icone': '⚖️',
    'aviso_extra': (
        "[color=#FF9800][b]⚠ ATENÇÃO:[/b][/color] Este conteúdo é informativo e "
        "não substitui orientação jurídica profissional. Consulte um advogado "
        "especializado antes de tomar qualquer decisão relacionada ao cultivo."
    ),
    'secoes': [
        {
            'titulo': '📋 O Que Diz a Lei',
            'itens': [
                ('Lei 11.343/2006 — Lei de Drogas',
                 'A Lei de Drogas proíbe o cultivo de cannabis sem autorização '
                 'expressa da Anvisa. Não há distinção legal explícita entre '
                 'cultivo para uso próprio e tráfico — a diferença fica a critério '
                 'do juiz com base em quantidade, local e circunstâncias.\n\n'
                 'A Anvisa pode autorizar cultivo apenas para [b]pesquisa científica[/b] '
                 'ou [b]fabricação industrial[/b] de produtos registrados — '
                 'não para pacientes individuais.'),
                ('Decisões do STJ e STF',
                 'O [b]STJ e STF[/b] têm concedido habeas corpus a pacientes '
                 'que cultivam para uso medicinal próprio, com base em:\n\n'
                 '• Art. 196 CF — Direito à saúde\n'
                 '• Art. 1º CF — Dignidade da pessoa humana\n'
                 '• Princípio da proporcionalidade\n\n'
                 'Isso não legaliza o cultivo — oferece proteção judicial '
                 'individual caso a caso. Cada processo é analisado separadamente.'),
            ]
        },
        {
            'titulo': '🛡️ Habeas Corpus Preventivo',
            'itens': [
                ('⚠️ Obrigatório Antes de Plantar',
                 '[color=#FF9800][b]Não plante sem ter o habeas corpus em mãos.[/b][/color]\n\n'
                 'O habeas corpus preventivo é o único instrumento que oferece '
                 'proteção jurídica real contra prisão ou apreensão. '
                 'Sem ele, mesmo com laudo médico, você pode ser autuado '
                 'por tráfico ou cultivo ilegal.\n\n'
                 '[b]Ordem obrigatória:[/b]\n'
                 '1. Obter laudo + receita médica\n'
                 '2. Contratar advogado especializado\n'
                 '3. Impetrar habeas corpus preventivo no TJ do seu estado\n'
                 '4. Aguardar concessão judicial\n'
                 '5. Somente então iniciar o cultivo'),
                ('O Que é e Como Funciona',
                 'Instrumento jurídico que protege o paciente [b]antes[/b] '
                 'de qualquer prisão ou apreensão. Funciona como uma ordem judicial '
                 'que impede autoridades de prender ou processar o paciente '
                 'pelo cultivo descrito na decisão.\n\n'
                 '[b]Onde impetrar:[/b] TJ (Tribunal de Justiça) do seu estado\n'
                 '[b]Tempo médio:[/b] Semanas a meses — varia por estado\n'
                 '[b]Custo:[/b] Honorários do advogado (Defensoria Pública é gratuita)'),
                ('Documentos Necessários',
                 '• [b]Laudo médico[/b] detalhado com diagnóstico e justificativa\n'
                 '• [b]Receita médica[/b] indicando cannabis medicinal\n'
                 '• [b]RG e CPF[/b]\n'
                 '• [b]Comprovante de residência[/b]\n'
                 '• Histórico de tratamentos anteriores\n'
                 '• Declaração do médico sobre falha de outros tratamentos'),
            ]
        },
        {
            'titulo': '👨‍⚖️ Apoio Jurídico',
            'itens': [
                ('Onde Encontrar Advogados Especializados',
                 '• [b]OAB Cannabis[/b] — Comissão especial da OAB\n'
                 '• [b]ABRACANNABIS[/b] — Lista de advogados parceiros por estado\n'
                 '• [b]APEPI / ABRACE / Flor da Vida[/b] — Suporte jurídico a associados\n'
                 '• [b]Instituto Igarapé[/b] — Advocacy em política de drogas\n'
                 '• Grupos de pacientes no Telegram/Facebook por estado\n\n'
                 '[i]Verifique sempre a especialização em cannabis/saúde antes de contratar.[/i]'),
                ('Defensoria Pública — Atendimento Gratuito',
                 'Pacientes de baixa renda têm direito a atendimento gratuito '
                 'pela Defensoria Pública do estado.\n\n'
                 '• Presente em capitais e muitas cidades do interior\n'
                 '• Pode impetrar habeas corpus sem custo\n'
                 '• Buscar em defensoria.[seu-estado].def.br\n\n'
                 'Leve toda a documentação médica na primeira consulta.'),
            ]
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# CANABINOIDES E TERPENOS
# ─────────────────────────────────────────────────────────────────────────────
CANABINOIDES = {
    'titulo': 'Canabinoides & Terpenos',
    'icone': '🔬',
    'secoes': [
        {
            'titulo': '⚗️ Canabinoides Principais',
            'itens': [
                ('THC — Tetrahidrocanabinol',
                 '[b]Ponto de vaporização:[/b] 🌡️ 157°C\n'
                 '[b]Psicoativo:[/b] Sim\n'
                 '[b]Efeitos:[/b] Euforia, alteração sensorial, analgesia, '
                 'estimulação de apetite, antinauseante, relaxamento muscular.\n'
                 '[b]Aplicações médicas:[/b] Dor crônica, náusea por quimioterapia, '
                 'espasticidade, anorexia em HIV/AIDS.\n'
                 '[b]Atenção:[/b] Em doses altas ou em pessoas sensíveis pode causar '
                 'ansiedade, paranoia e taquicardia. Contraindicado em menores '
                 'e pessoas com predisposição a psicose.'),
                ('CBD — Canabidiol',
                 '[b]Ponto de vaporização:[/b] 🌡️ 160–180°C\n'
                 '[b]Psicoativo:[/b] Não\n'
                 '[b]Efeitos:[/b] Ansiolítico, anticonvulsivante, anti-inflamatório, '
                 'neuroprotetor, antipsicótico leve.\n'
                 '[b]Aplicações médicas:[/b] Epilepsia (especialmente Dravet e Lennox-Gastaut), '
                 'ansiedade, TEPT, inflamação crônica, dor neuropática.\n'
                 '[b]No Brasil:[/b] Regulamentado pela Anvisa. Produtos como Canabidiol Prati, '
                 'Charlotte\'s Web e Epidiolex disponíveis com prescrição.'),
                ('CBG — Canabigerol',
                 '[b]Ponto de vaporização:[/b] 🌡️ 52°C (volátil a baixas temperaturas)\n'
                 '[b]Psicoativo:[/b] Não\n'
                 '[b]Precursor:[/b] Chamado de "mãe dos canabinoides" — '
                 'THC e CBD são sintetizados a partir do CBG.\n'
                 '[b]Efeitos:[/b] Antibacteriano, neuroprotetor, anti-inflamatório '
                 'intestinal, pode reduzir pressão intraocular (glaucoma).\n'
                 '[b]Status:[/b] Pesquisas em estágio inicial, disponível em '
                 'algumas formulações especializadas.'),
                ('CBN — Canabidinol',
                 '[b]Ponto de vaporização:[/b] 🌡️ 185°C\n'
                 '[b]Psicoativo:[/b] Levemente (10–20% do THC)\n'
                 '[b]Origem:[/b] Produzido pela degradação oxidativa do THC '
                 '(material envelhecido ou exposto ao calor/luz).\n'
                 '[b]Efeitos:[/b] Sedativo, analgésico, anti-inflamatório, '
                 'potencial antibacteriano.\n'
                 '[b]Uso:[/b] Muito valorizado para distúrbios do sono. '
                 'Encontrado em cultivares maduros com colheita tardia.'),
                ('CBC — Canabicrômeno',
                 '[b]Ponto de vaporização:[/b] 🌡️ 220°C\n'
                 '[b]Psicoativo:[/b] Não\n'
                 '[b]Efeitos:[/b] Anti-inflamatório, analgésico (potencializa THC '
                 'e CBD), antidepressivo, pode estimular neuroplasticidade.\n'
                 '[b]Pesquisa:[/b] Promissor para dor, inflamação e saúde cerebral.'),
            ]
        },
        {
            'titulo': '🌸 Terpenos Principais',
            'itens': [
                ('Mirceno',
                 '[b]Ponto de vaporização:[/b] 🌡️ 168°C\n'
                 '[b]Aroma:[/b] Terra, almíscar, frutas tropicais\n'
                 '[b]Efeitos:[/b] Sedativo, relaxante muscular, analgésico. '
                 'Facilita a passagem de canabinoides pela barreira hematoencefálica.\n'
                 '[b]Encontrado em:[/b] Manga, lúpulo, tomilho'),
                ('Limoneno',
                 '[b]Ponto de vaporização:[/b] 🌡️ 176°C\n'
                 '[b]Aroma:[/b] Cítrico, limão, laranja\n'
                 '[b]Efeitos:[/b] Ansiolítico, antidepressivo, antifúngico, '
                 'potencializa absorção de outros terpenos.\n'
                 '[b]Encontrado em:[/b] Cascas cítricas, alecrim'),
                ('Pineno (α e β)',
                 '[b]Ponto de vaporização:[/b] 🌡️ α-Pineno 155°C | β-Pineno 166°C\n'
                 '[b]Aroma:[/b] Pinho, bosque\n'
                 '[b]Efeitos:[/b] Broncodilatador, anti-inflamatório, pode '
                 'contrariar déficits de memória causados pelo THC, '
                 'promove alerta e foco.\n'
                 '[b]Encontrado em:[/b] Pinheiro, sálvia, alecrim'),
                ('Linalol',
                 '[b]Ponto de vaporização:[/b] 🌡️ 198°C\n'
                 '[b]Aroma:[/b] Floral, lavanda\n'
                 '[b]Efeitos:[/b] Ansiolítico, sedativo, anestésico local, '
                 'anticonvulsivante. Potencializa efeitos do CBD.\n'
                 '[b]Encontrado em:[/b] Lavanda, coentro, canela'),
                ('Cariofileno',
                 '[b]Ponto de vaporização:[/b] 🌡️ 119°C (ativo mesmo em baixas temperaturas)\n'
                 '[b]Aroma:[/b] Pimenta, especiarias, madeira\n'
                 '[b]Efeitos:[/b] Anti-inflamatório (age diretamente em receptores CB2), '
                 'analgésico, gastroprotetor. Único terpeno que ativa o sistema endocanabinoide.\n'
                 '[b]Encontrado em:[/b] Pimenta preta, cravo, canela'),
                ('Terpinoleno',
                 '[b]Ponto de vaporização:[/b] 🌡️ 186°C\n'
                 '[b]Aroma:[/b] Floral, herbáceo, pinho\n'
                 '[b]Efeitos:[/b] Antioxidante, sedativo leve, antifúngico.\n'
                 '[b]Encontrado em:[/b] Maçã, lilás, pimentas'),
            ]
        },
        {
            'titulo': '🧬 Efeito Entourage',
            'itens': [
                ('O que é',
                 'O efeito entourage é a sinergia entre canabinoides, terpenos e '
                 'flavonoides presentes na planta inteira. Quando combinados, '
                 'esses compostos amplificam e modulam os efeitos uns dos outros '
                 'de maneira mais eficaz do que qualquer composto isolado.\n\n'
                 'Exemplo: CBD isolado tem eficácia anticonvulsivante, mas o extrato '
                 'de espectro completo (full spectrum) com THC, terpenos e outros '
                 'canabinoides demonstra resultados superiores em estudos clínicos.'),
                ('Espectro Completo vs Isolado',
                 '[b]Isolado (Isolate):[/b] CBD puro 99%+. Sem THC. '
                 'Previsível, sem risco de falso positivo em exame. Menos efeito entourage.\n\n'
                 '[b]Broad Spectrum:[/b] Múltiplos canabinoides + terpenos, '
                 'THC removido (<0,3%). Efeito entourage parcial.\n\n'
                 '[b]Full Spectrum:[/b] Todos os compostos naturais incluindo THC '
                 '(<0,3%). Maior efeito entourage. Pode causar falso positivo.'),
            ]
        },
        {
            'titulo': '🌍 Indica vs Sativa vs Híbrida',
            'itens': [
                ('Cannabis Indica',
                 '[b]Origem:[/b] Afeganistão, Paquistão, Índia\n'
                 '[b]Aparência:[/b] Plantas mais baixas, folhas largas e escuras\n'
                 '[b]Perfil de efeitos (tradicional):[/b] Relaxante, sedativo, '
                 'corporal ("body high"), indicado para noite.\n'
                 '[b]Terpenos comuns:[/b] Mirceno, linalol, cariofileno\n'
                 '[b]Uso médico:[/b] Dor, insônia, espasmos musculares, '
                 'estimulação de apetite\n\n'
                 '[i]Nota:[/i] A distinção indica/sativa é simplificada. '
                 'Na ciência moderna, o que determina o efeito é o perfil '
                 'de canabinoides + terpenos, não a subespécie.'),
                ('Cannabis Sativa',
                 '[b]Origem:[/b] Regiões equatoriais (América, África, Ásia)\n'
                 '[b]Aparência:[/b] Plantas altas, folhas finas e claras\n'
                 '[b]Perfil de efeitos (tradicional):[/b] Energizante, criativo, '
                 'cerebral ("head high"), indicado para dia.\n'
                 '[b]Terpenos comuns:[/b] Limoneno, pineno, terpinoleno\n'
                 '[b]Uso médico:[/b] Depressão, fadiga, déficit de foco, '
                 'náusea, dores de cabeça'),
                ('Cannabis Híbrida',
                 'A grande maioria das cultivares modernas são híbridas, '
                 'cruzamentos entre indica e sativa. Podem ser:\n\n'
                 '[b]Indica-dominante:[/b] Mais relaxante\n'
                 '[b]Sativa-dominante:[/b] Mais energizante\n'
                 '[b]Balanceada (50/50):[/b] Efeitos equilibrados\n\n'
                 'Exemplos populares: Girl Scout Cookies, Blue Dream, OG Kush, '
                 'White Widow, Gorilla Glue.'),
            ]
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# MÉTODOS DE CONSUMO
# ─────────────────────────────────────────────────────────────────────────────
CONSUMO = {
    'titulo': 'Métodos de Consumo',
    'icone': '💨',
    'secoes': [
        {
            'titulo': '♨️ Vaporização — O Método Recomendado',
            'itens': [
                ('Como Funciona',
                 'O vaporizador aquece o material (flor seca ou extrato) a '
                 'temperaturas entre [b]160°C e 220°C[/b] — abaixo do ponto de '
                 'combustão (230°C+). Isso volatiliza os canabinoides e terpenos '
                 'sem queimar o material vegetal.'),
                ('Faixas de Temperatura',
                 '[b]160–170°C:[/b] Efeito mais suave e cerebral. Preserva '
                 'terpenos voláteis. Ideal para início de sessão.\n\n'
                 '[b]170–185°C:[/b] Equilíbrio entre sabor e potência. '
                 'Ativa THC e CBD eficientemente.\n\n'
                 '[b]185–200°C:[/b] Efeito mais intenso e corporal. '
                 'Ativa canabinoides de ponto mais alto como CBN.\n\n'
                 '[b]200–220°C:[/b] Extração máxima. Vapor mais denso. '
                 'Pode degradar alguns terpenos delicados.'),
                ('Vantagens vs Combustão',
                 '✅ Sem benzeno, monóxido de carbono ou alcatrão\n'
                 '✅ Temperatura controlada preserva terpenos e canabinoides\n'
                 '✅ Sabor e aroma significativamente melhores\n'
                 '✅ Menos irritação respiratória\n'
                 '✅ Maior eficiência — extrai mais canabinoides da mesma quantidade\n'
                 '✅ AVB (Already Vaped Bud) ainda pode ser usado em infusões'),
            ]
        },
        {
            'titulo': '🚫 Combustão — Por Que Evitar',
            'itens': [
                ('Os Riscos da Fumaça',
                 'A combustão de qualquer material orgânico a >230°C gera mais de '
                 '[b]100 compostos tóxicos[/b], incluindo:\n\n'
                 '• [b]Benzeno:[/b] Carcinogênico, leucemia\n'
                 '• [b]Monóxido de carbono (CO):[/b] Reduz oxigenação do sangue\n'
                 '• [b]Alcatrão:[/b] Deposita-se nos pulmões, causa bronquite crônica\n'
                 '• [b]Hidrocarbonetos policíclicos:[/b] Mutagênicos\n'
                 '• [b]Acroleína:[/b] Irritante pulmonar severo'),
                ('O Problema do Papel e Tabaco',
                 'Cigarros de cannabis frequentemente usam tabaco (mistura), '
                 'adicionando os riscos da nicotina e dependência. '
                 'O papel de cigarro também libera compostos ao queimar.\n\n'
                 '[b]Baseado/Blunt:[/b] Combinação de todos esses riscos. '
                 'O método mais prejudicial para a saúde.\n\n'
                 '[i]Mesmo sem tabaco, a combustão da cannabis causa irritação '
                 'das vias aéreas superiores e inferiores.[/i]'),
                ('Alternativa Mais Segura ao Fumo',
                 'Se a vaporização não estiver disponível, o cachimbo d\'água '
                 '(bong) com água fria filtra parte das partículas, mas '
                 '[b]não elimina[/b] os compostos tóxicos da combustão. '
                 'Ainda assim, preferível ao baseado. '
                 'A melhor alternativa sempre será o vaporizador.'),
            ]
        },
        {
            'titulo': '💧 Via Sublingual (Óleos)',
            'itens': [
                ('Como Funciona',
                 'O óleo é aplicado [b]sob a língua[/b] e absorvido diretamente '
                 'pela mucosa oral para a corrente sanguínea, '
                 'evitando o metabolismo de primeira passagem hepática.\n\n'
                 '[b]Início dos efeitos:[/b] 15–45 minutos\n'
                 '[b]Pico:[/b] 1–2 horas\n'
                 '[b]Duração:[/b] 4–8 horas'),
                ('Vantagens',
                 '✅ Sem risco respiratório\n'
                 '✅ Efeito mais duradouro que a vaporização\n'
                 '✅ Dosagem precisa com conta-gotas graduado\n'
                 '✅ Discreto e portátil\n'
                 '✅ Ideal para pacientes que não podem inalar'),
                ('Como Usar Corretamente',
                 '1. Aplicar o óleo sob a língua com o conta-gotas\n'
                 '2. Manter por [b]60–90 segundos[/b] antes de engolir\n'
                 '3. Evitar comer ou beber por 10–15 min após\n'
                 '4. Começar com dose baixa (1–2 gotas) e aguardar 2h '
                 'antes de redosar — efeito sublingual é mais lento que inalação'),
            ]
        },
        {
            'titulo': '🍪 Via Oral (Comestíveis)',
            'itens': [
                ('Como Funciona',
                 'Cannabis infundida em alimentos ou cápsulas é absorvida '
                 'pelo trato digestivo. O THC é metabolizado no fígado em '
                 '11-hidroxi-THC, composto mais potente e de efeito mais prolongado.\n\n'
                 '[b]Início:[/b] 30–90 minutos (até 2h em jejum)\n'
                 '[b]Pico:[/b] 2–4 horas\n'
                 '[b]Duração:[/b] 6–12 horas'),
                ('⚠️ Atenção com Dosagem',
                 'A via oral é a que mais frequentemente causa '
                 '"overdoses" não intencionais. Nunca redosar antes de 2 horas.\n\n'
                 '[b]Regra de ouro:[/b] "Comece baixo, vá devagar."\n\n'
                 'Para produtos de farmácia/associação: seguir dosagem prescrita. '
                 'Para óleos orais: 5–10mg de THC é dose inicial para adultos sem tolerância.'),
            ]
        },
        {
            'titulo': '🧴 Via Tópica',
            'itens': [
                ('Como Funciona',
                 'Cremes, loções, bálsamos e adesivos transdérmicos com '
                 'canabinoides aplicados diretamente na pele.\n\n'
                 '[b]Tópicos regulares:[/b] Agem localmente, não entram na '
                 'corrente sanguínea — [b]sem efeito psicoativo[/b].\n\n'
                 '[b]Transdérmicos (adesivos):[/b] Atravessam a barreira da pele '
                 'e atingem a corrente sanguínea — efeito sistêmico.'),
                ('Indicações',
                 '• Dores musculares e articulares localizadas\n'
                 '• Artrite e inflamação local\n'
                 '• Neuropatia periférica\n'
                 '• Condições de pele (psoríase, eczema)\n'
                 '• Tensão muscular pós-exercício'),
            ]
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# VAPORIZADORES
# ─────────────────────────────────────────────────────────────────────────────
VAPORIZADORES = {
    'titulo': 'Vaporizadores',
    'icone': '🌬️',
    'secoes': [
        {
            'titulo': '📱 Tipos de Vaporizadores',
            'itens': [
                ('Caneta Vape (Vape Pen)',
                 '[b]Para:[/b] Concentrados (óleo, distillate, wax)\n'
                 '[b]Preço:[/b] R$ 80–300\n'
                 '[b]Vantagens:[/b] Extremamente portátil, discreto, fácil de usar\n'
                 '[b]Desvantagens:[/b] Não funciona com flor seca, cartuchos '
                 'descartáveis geram resíduo, qualidade variável do extrato\n'
                 '[b]Indicado para:[/b] Iniciantes em vaporização, uso discreto'),
                ('Vaporizador Portátil de Flor Seca',
                 '[b]Para:[/b] Flor seca, haxixe (com tela)\n'
                 '[b]Preço:[/b] R$ 300–2.000+\n'
                 '[b]Vantagens:[/b] Portátil, bateria recarregável, '
                 'controle de temperatura, uso com flor natural\n'
                 '[b]Desvantagens:[/b] Necessita limpeza regular, bateria limitada\n'
                 '[b]Modelos populares:[/b] DynaVap (R$400–700), Pax 3 (R$800+), '
                 'Mighty/Crafty+ (R$1.500+), Arizer Air/Solo'),
                ('Vaporizador Desktop',
                 '[b]Para:[/b] Flor seca e concentrados\n'
                 '[b]Preço:[/b] R$ 1.500–5.000+\n'
                 '[b]Vantagens:[/b] Maior eficiência de extração, temperatura precisa, '
                 'sem preocupação com bateria, vapor mais suave\n'
                 '[b]Desvantagens:[/b] Não portátil, maior investimento\n'
                 '[b]Modelos referência:[/b] Volcano Hybrid (Storz & Bickel, R$4.000+), '
                 'Arizer Extreme Q (R$1.500), Plenty'),
            ]
        },
        {
            'titulo': '🏺 Câmara de Aquecimento',
            'itens': [
                ('Cerâmica',
                 '[b]Características:[/b] Aquecimento mais uniforme, '
                 'inerte quimicamente, não altera sabor\n'
                 '[b]Sabor:[/b] Mais limpo e puro — ideal para apreciação de terpenos\n'
                 '[b]Durabilidade:[/b] Alta, mas frágil a impactos\n'
                 '[b]Limpeza:[/b] Fácil com álcool isopropílico\n'
                 '[b]Indicada para:[/b] Usuários que priorizam sabor e uso medicinal'),
                ('Metal (Aço Inox / Liga)',
                 '[b]Características:[/b] Mais resistente a impactos\n'
                 '[b]Sabor:[/b] Pode adicionar leve sabor metálico, '
                 'especialmente em altas temperaturas\n'
                 '[b]Durabilidade:[/b] Muito alta\n'
                 '[b]Atenção:[/b] Evitar câmaras de alumínio — '
                 'liberam partículas em altas temperaturas. '
                 'Aço cirúrgico e titânio são seguros.'),
                ('Quartzo e Vidro',
                 '[b]Características:[/b] Encontrado em dab rigs e vaporizers de concentrado\n'
                 '[b]Sabor:[/b] Neutro, excelente para concentrados\n'
                 '[b]Durabilidade:[/b] Frágil, requer cuidado\n'
                 '[b]Temperatura:[/b] Precisa de aquecimento externo (tocha) '
                 'em rigs tradicionais, ou elemento elétrico em e-nails'),
            ]
        },
        {
            'titulo': '🎯 Como Escolher',
            'itens': [
                ('Por Perfil de Uso',
                 '[b]Iniciante / Custo-benefício:[/b]\n'
                 'DynaVap M (aquecido por maçarico) — R$400–500. '
                 'Sem bateria, durabilidade extrema, aprendizado da técnica.\n\n'
                 '[b]Uso diário portátil:[/b]\n'
                 'Mighty+ ou Crafty+ (Storz & Bickel) — R$1.500–2.000. '
                 'Padrão-ouro em portáteis, convecção híbrida, vapor excelente.\n\n'
                 '[b]Uso doméstico / médico:[/b]\n'
                 'Volcano Hybrid — R$4.000+. '
                 'Referência global, uso em balão ou whip, vapor suave e eficiente.\n\n'
                 '[b]Econômico portátil:[/b]\n'
                 'Arizer Solo 2 / Air 2 — R$600–900. '
                 'Excelente custo-benefício, troca de bateria possível.'),
                ('Dicas de Compra',
                 '• Comprar de revendedores autorizados para garantia\n'
                 '• Verificar tensão elétrica (110V/220V ou bivolt)\n'
                 '• Pesquisar no Reddit r/vaporents para reviews reais\n'
                 '• Desconfiar de modelos muito baratos sem procedência\n'
                 '• Manter nota fiscal para acionamento de garantia\n'
                 '• Kit básico: vaporizador + escova de limpeza + álcool isopropílico 99%'),
                ('Manutenção',
                 '[b]Limpeza após cada uso:[/b] Escovar câmara ainda morna\n'
                 '[b]Limpeza semanal (uso diário):[/b] Algodão embebido em álcool 99% '
                 'na câmara e bocal\n'
                 '[b]Tela (screen):[/b] Substituir a cada 2–4 semanas\n'
                 '[b]Caminho do vapor (vapor path):[/b] Limpar com pipe cleaner '
                 'e álcool mensalmente\n'
                 '[b]Câmara de vidro:[/b] Imergir em solução de álcool + sal grosso '
                 'e agitar'),
            ]
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# ASSOCIAÇÕES
# ─────────────────────────────────────────────────────────────────────────────
ASSOCIACOES = {
    'titulo': 'Associações de Cannabis',
    'icone': '🏛️',
    'secoes': [
        {
            'titulo': '⚖️ Marco Legal no Brasil',
            'itens': [
                ('Regulamentação Anvisa',
                 'A [b]RDC 660/2022[/b] (atualizada pela RDC 327/2019) da Anvisa '
                 'regula o acesso à cannabis medicinal no Brasil por dois caminhos:\n\n'
                 '[b]1. Produtos registrados/notificados:[/b] Canabidiol Prati-Donaduzzi, '
                 'Charlotte\'s Web, Epidiolex — disponíveis em farmácias com prescrição.\n\n'
                 '[b]2. Importação por pessoa física:[/b] Para produtos não disponíveis '
                 'no Brasil, mediante autorização da Anvisa (formulário online), '
                 'prescrição médica e laudo médico.'),
                ('Associações de Pacientes',
                 'As associações são entidades sem fins lucrativos que cultivam '
                 'cannabis e fornecem produtos aos associados. Operam em uma '
                 '[b]zona cinza jurídica[/b] — não são formalmente legalizadas, '
                 'mas decisões judiciais têm protegido suas atividades com base '
                 'no direito à saúde e dignidade humana.\n\n'
                 'Vantagens sobre farmácia:\n'
                 '• Maior variedade de produtos (full spectrum, tinturas, cápsulas)\n'
                 '• Custo significativamente menor\n'
                 '• Acesso a cultivares com perfis específicos de canabinoides'),
            ]
        },
        {
            'titulo': '📋 Como se Associar',
            'itens': [
                ('Documentos Necessários',
                 'Os requisitos variam por associação, mas geralmente incluem:\n\n'
                 '• [b]RG e CPF[/b] (ou CNH)\n'
                 '• [b]Comprovante de residência[/b] recente\n'
                 '• [b]Laudo médico[/b] descrevendo a condição de saúde\n'
                 '• [b]Prescrição médica[/b] (receita) de profissional habilitado\n'
                 '• Em alguns casos: exames ou relatório do histórico de tratamentos\n\n'
                 '[i]Dica: Médicos especializados em cannabis medicinal facilitam '
                 'o processo. Plataformas como Dr. Cannabis conectam pacientes '
                 'a prescritores.[/i]'),
                ('Processo Passo a Passo',
                 '1. Consultar médico e obter laudo + prescrição\n'
                 '2. Pesquisar associações atuantes na sua região ou que operem online\n'
                 '3. Entrar em contato com a associação via site ou redes sociais\n'
                 '4. Enviar documentação para análise\n'
                 '5. Pagar a taxa de associação (anual, geralmente R$50–200)\n'
                 '6. Aguardar aprovação e retirada/envio dos produtos\n\n'
                 '[b]Tempo médio:[/b] 1–4 semanas após aprovação dos documentos'),
                ('Custos Típicos',
                 '[b]Taxa de associação:[/b] R$50–200/ano\n'
                 '[b]Óleo CBD 1.500mg (30ml):[/b] R$150–350\n'
                 '[b]Óleo Full Spectrum:[/b] R$200–500\n'
                 '[b]Cápsulas (60 un.):[/b] R$180–400\n\n'
                 'Compare: produtos de farmácia similares custam 3–5x mais.\n'
                 'Importação Anvisa tem custo adicional de logística internacional.'),
            ]
        },
        {
            'titulo': '📄 Documentação por Canal de Acesso',
            'itens': [
                ('⭐ Associações (ex: Flor da Vida)',
                 'O processo mais acessível para a maioria dos pacientes:\n\n'
                 '✅ [b]Receita médica[/b] — prescrição de médico habilitado\n'
                 '✅ [b]Laudo médico[/b] — documento descrevendo o diagnóstico\n'
                 '✅ RG/CPF e comprovante de residência\n\n'
                 '[color=#4CAF50]Não exige autorização da Anvisa.[/color] '
                 'Processo mais simples, produtos mais baratos e maior variedade.'),
                ('Farmácias (produtos registrados Anvisa)',
                 'Para produtos como Canabidiol Prati-Donaduzzi:\n\n'
                 '✅ [b]Receita médica[/b] com retenção\n'
                 '✅ [b]Laudo médico[/b]\n\n'
                 'Disponível nas principais redes (Ultrafarma, Drogasil, Pague Menos). '
                 'Sem autorização Anvisa pois o produto já é registrado no Brasil.'),
                ('Importação via Autorização Anvisa',
                 'Para produtos não registrados no Brasil (Charlotte\'s Web, Elixinol, etc.):\n\n'
                 '✅ [b]Receita médica[/b]\n'
                 '✅ [b]Laudo médico[/b]\n'
                 '✅ [b]Autorização Anvisa[/b] — solicitada em anvisa.gov.br/cannabis\n\n'
                 'Processo mais burocrático. A autorização é pessoal e intransferível. '
                 'Válida por 1 ano, renovável. Tempo médio de aprovação: 3–10 dias úteis.'),
                ('Como Obter a Autorização Anvisa',
                 '1. Acesse [b]anvisa.gov.br/cannabis[/b]\n'
                 '2. Crie conta no portal Gov.br\n'
                 '3. Preencha o formulário de solicitação\n'
                 '4. Anexe: receita médica + laudo + RG\n'
                 '5. Aguarde análise (geralmente 3–10 dias úteis)\n'
                 '6. Receba autorização por e-mail\n'
                 '7. Use a autorização para importar ou comprar em plataformas autorizadas\n\n'
                 '[i]Dica: A plataforma Dr. Cannabis e HempMeds Brasil auxiliam no processo.[/i]'),
            ]
        },
        {
            'titulo': '🏢 Principais Associações no Brasil',
            'itens': [
                ('⭐ Flor da Vida — Associação de Pacientes',
                 '[b]Site:[/b] flordavida.ong.br/site/\n'
                 '[b]Documentação exigida:[/b]\n'
                 '✅ Receita médica\n'
                 '✅ Laudo médico\n'
                 '[color=#4CAF50]Não exige autorização Anvisa.[/color]\n\n'
                 '[b]Perfil:[/b] ONG dedicada ao acesso à cannabis medicinal, '
                 'atendimento humanizado, foco em pacientes que precisam de suporte.\n'
                 '[b]Produtos:[/b] Óleos, tinturas e outros — full spectrum e CBD isolado.'),
                ('ABRACE — Associação Brasileira de Pacientes de Cannabis',
                 '[b]Estado:[/b] Ceará (Fortaleza)\n'
                 '[b]Fundação:[/b] 2014 — pioneira no Brasil\n'
                 '[b]Perfil:[/b] Atende principalmente crianças com epilepsia refratária\n'
                 '[b]Contato:[/b] abraceceara.org.br'),
                ('APEPI — Ação pela Paz e pelo Instituto da Planta',
                 '[b]Estado:[/b] Rio de Janeiro\n'
                 '[b]Perfil:[/b] Foco em epilepsia pediátrica, ativismo e pesquisa\n'
                 '[b]Destaque:[/b] Uma das mais antigas e reconhecidas do RJ'),
                ('ACNPP — Associação Cannabis para Neuro e Psiquiatria de Porto Alegre',
                 '[b]Estado:[/b] Rio Grande do Sul\n'
                 '[b]Perfil:[/b] Foco em transtornos neurológicos e psiquiátricos'),
                ('ASPECAN — Associação de Pacientes e Familiares Usuários de Cannabis',
                 '[b]Estado:[/b] São Paulo\n'
                 '[b]Perfil:[/b] Grande base de associados, variedade de produtos'),
                ('Outras Associações por Estado',
                 'O número de associações no Brasil cresce anualmente. '
                 'Para encontrar a mais próxima ou que melhor atenda seu caso:\n\n'
                 '• Consulte o site da [b]ABRACANNABIS[/b] (Associação Brasileira de Cannabis)\n'
                 '• Grupos de Facebook/WhatsApp de pacientes por estado\n'
                 '• Plataforma Dr. Cannabis tem lista curada\n'
                 '• Associação Nacional de Farmacêuticos (CFF) para produtos farmacêuticos'),
            ]
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# ONDE COMPRAR
# ─────────────────────────────────────────────────────────────────────────────
ONDE_COMPRAR = {
    'titulo': 'Onde Comprar',
    'icone': '🛒',
    'secoes': [
        {
            'titulo': '💊 Produtos Medicinais (Óleos, Cápsulas)',
            'itens': [
                ('Farmácias com Produtos Anvisa',
                 '[b]Canabidiol Prati-Donaduzzi:[/b] Disponível em farmácias '
                 'convencionais (Pague Menos, Drogasil, Ultrafarma). '
                 'Necessita receita médica. Concentrações: 200mg, 600mg, 1200mg em 30ml.\n\n'
                 '[b]Importação via Anvisa:[/b] Para produtos internacionais '
                 '(Charlotte\'s Web, Elixinol, etc.) — solicitar autorização em anvisa.gov.br/cannabis.\n\n'
                 '[b]Farmácias de manipulação:[/b] Algumas manipulam CBD em diferentes '
                 'concentrações mediante laudo e receita.'),
                ('Associações de Pacientes',
                 'Veja seção "Associações" para lista completa e processo de associação.\n\n'
                 'Vantagens: menor custo, maior variedade, suporte de comunidade.\n'
                 'Requisito: laudo médico + documentação.'),
                ('Plataformas Online Especializadas',
                 '[b]Dr. Cannabis:[/b] Telemedicina + marketplace de produtos regulamentados\n'
                 '[b]Cannect:[/b] Plataforma de prescrição e acesso a produtos\n'
                 '[b]HempMeds Brazil:[/b] Importadora de produtos Charlotte\'s Web\n\n'
                 '[i]Atenção: Desconfie de sites sem CNPJ claro, sem produtos '
                 'com laudos de análise (COA) e que vendam THC livremente.[/i]'),
            ]
        },
        {
            'titulo': '🌱 Sementes (Coleção)',
            'itens': [
                ('Status Legal no Brasil',
                 'A venda de sementes de cannabis é uma [b]zona cinza legal[/b] no Brasil. '
                 'Não há lei específica proibindo a venda de sementes como '
                 '"souvenirs para coleção", mas o cultivo é proibido sem autorização.\n\n'
                 'Diversas lojas operam no Brasil sob essa premissa, '
                 'geralmente com disclaimer de "uso exclusivo para coleção". '
                 'O comprador assume os riscos legais.'),
                ('Bancos de Sementes Confiáveis',
                 '[b]Internacionais com envio ao Brasil:[/b]\n'
                 '• Seedsman (UK) — grande variedade, envio discreto\n'
                 '• ILGM (I Love Growing Marijuana) — garantia de germinação\n'
                 '• Barney\'s Farm (NL) — genéticas premium\n\n'
                 '[b]Nacionais:[/b]\n'
                 '• Brazilian Seed Bank\n'
                 '• Grow Shop Brasil\n'
                 '• Diversas lojas em São Paulo e Rio de Janeiro\n\n'
                 '[i]Pesquise reviews em fóruns como Canna.com.br '
                 'antes de comprar.[/i]'),
            ]
        },
        {
            'titulo': '💨 Vaporizadores',
            'itens': [
                ('Lojas Físicas',
                 'Principais cidades têm head shops e grow shops que vendem vaporizadores:\n\n'
                 '[b]São Paulo:[/b] Concentração maior no centro e Vila Madalena\n'
                 '[b]Rio de Janeiro:[/b] Ipanema, Lapa\n'
                 '[b]Outras cidades:[/b] Buscar "grow shop [cidade]" no Google Maps'),
                ('⭐ Loja High420 — Vaporizadores de Ervas',
                 '[b]Site:[/b] lojahigh420.com/vaporizadores/vaporizador-de-ervas/\n'
                 '[b]Especialidade:[/b] Vaporizadores de ervas nacionais e importados, '
                 'acessórios e peças de reposição.\n'
                 '[b]Destaques:[/b] Amplo catálogo de portáteis e desktops, '
                 'atendimento especializado, envio para todo o Brasil.'),
                ('Outras Lojas Online Nacionais',
                 '• Dankstop Brasil\n'
                 '• Vaporizer Shop Brasil\n'
                 '• Grow Indoor (equipamentos)\n'
                 '• Mercado Livre (revendedores verificados — atenção à procedência)\n\n'
                 '[b]Dica:[/b] Para garantia válida e produto original, '
                 'prefira revendedores autorizados pelos fabricantes '
                 '(Storz & Bickel tem revendedores oficiais no Brasil).'),
                ('Importação Direta',
                 'Vaporizadores podem ser importados sem restrição legal '
                 '(são equipamentos de uso pessoal).\n\n'
                 '[b]AliExpress:[/b] Marcas asiáticas de entrada (cuidado com qualidade)\n'
                 '[b]VaporizerWizard.com:[/b] Reviews + links para revendedores\n'
                 '[b]PuffItUp.com:[/b] Especializado, envia internacionalmente\n\n'
                 '[b]Imposto de importação:[/b] Produtos acima de US$50 '
                 'podem ser taxados (60% do valor + IOF). '
                 'Frete + taxa pode elevar custo final significativamente.'),
            ]
        },
    ]
}
