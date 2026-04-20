// content.js — Conteúdo estático do CannaGuia (convertido de content.py)

const CULTIVO = {
  titulo: 'Guia de Cultivo',
  icone: '🌱',
  id: 'cultivo',
  aviso_extra: '⚠️ ATENÇÃO: No Brasil, o cultivo de cannabis é proibido sem autorização expressa da Anvisa (Lei 11.343/2006). Este conteúdo é exclusivamente educacional.',
  secoes: [
    {
      titulo: '🌰 Sementes vs Clones',
      itens: [
        ['Sementes — Vantagens', 'Maior diversidade genética, sem risco de transmissão de pragas e doenças via material vegetativo, vigor híbrido em F1, facilidade de armazenamento e transporte.'],
        ['Tipos de Sementes', '<b>Regulares:</b> Produzem machos e fêmeas (50/50). Usadas para cruzamentos.<br><br><b>Feminizadas:</b> Geneticamente modificadas para produzir quase 100% fêmeas. Ideal para cultivo medicinal — apenas fêmeas produzem flores ricas em canabinoides.<br><br><b>Autoflorescentes:</b> Florescem por idade (geralmente 70–90 dias), independentemente do fotoperíodo. Ótimas para iniciantes.'],
        ['Clones — Vantagens', 'Cópia genética exata da planta-mãe, sexo garantido, uniformidade na produção, início mais rápido sem fase de germinação. Risco: podem transmitir pragas e doenças da planta-mãe.'],
      ]
    },
    {
      titulo: '🛒 Onde Conseguir Sementes',
      itens: [
        ['Status Legal no Brasil', 'A venda de sementes de cannabis é uma <b>zona cinza legal</b> no Brasil. Não há lei específica proibindo a comercialização de sementes como "souvenirs para coleção", mas o cultivo sem autorização da Anvisa é ilegal.<br><br>Diversas lojas operam sob essa premissa com disclaimer de "uso exclusivo para coleção". O comprador assume os riscos legais.<br><br><b>Importante:</b> Adquirir sementes sem o habeas corpus preventivo não oferece proteção jurídica. Consulte a seção <b>Lei de Cultivo</b> antes.'],
        ['Bancos de Sementes — Internacionais', '<b>Seedsman (UK)</b> — grande variedade, envio discreto, preços acessíveis<br><b>ILGM — I Love Growing Marijuana</b> — garantia de germinação, suporte<br><b>Barney\'s Farm (NL)</b> — genéticas premium, múltiplos Cannabis Cup<br><b>Royal Queen Seeds (ESP)</b> — muito popular, boa relação custo-benefício<br><b>Dinafem (ESP)</b> — especialista em feminizadas e medicinais CBD<br><br><i>Fique atento à alfândega: sementes podem ser retidas. Bancos confiáveis reenviam em caso de apreensão.</i>'],
        ['Bancos de Sementes — Nacionais', '<b>Brazilian Seed Bank</b> — genéticas nacionais e importadas<br><b>Grow Shop Brasil</b> — lojas em SP e online<br><b>Lojas em São Paulo</b> — concentração no centro e Vila Madalena<br><b>Rio de Janeiro</b> — Ipanema, Lapa e grow shops da região<br><br>Vantagens do nacional: sem risco alfandegário, pagamento em real, entrega mais rápida. Desvantagem: variedade menor.<br><br><i>Pesquise reviews em fóruns como Canna.com.br antes de comprar.</i>'],
        ['Como Escolher uma Boa Semente', '<b>Cor e firmeza:</b> Sementes maduras são marrons/cinza com listras tigradas, duras ao apertar. Sementes verdes ou muito claras são imaturas — baixa taxa de germinação.<br><br><b>COA / Ficha técnica:</b> Bancos sérios informam THC estimado, CBD, tempo de floração e tipo (regular/fem/auto).<br><br><b>Desconfie de:</b> Preços muito abaixo do mercado, sem ficha técnica, sem histórico do vendedor.<br><br><b>Armazenamento:</b> Local escuro, fresco e seco. Geladeira (4–8°C) com sílica gel preserva até 5+ anos.'],
      ]
    },
    {
      titulo: '🌿 Fases da Planta',
      itens: [
        ['Germinação (3–7 dias)', 'A semente absorve água e a radícula (raiz embrionária) rompe a casca. Temperatura ideal: 22–26°C. Umidade: 70–90%. Método mais simples: entre dois lenços úmidos, em local escuro e quente.'],
        ['Muda / Seedling (2–3 semanas)', 'Surgem os primeiros cotilédones e depois as folhas serrilhadas características. Luz: 18h/dia. Temperatura: 20–26°C. Umidade: 60–70%. Solo bem drenado, regas leves. Evitar sobrefertilização.'],
        ['Fase Vegetativa (4–8 semanas)', 'A planta cresce em altura e desenvolve estrutura. Fotoperíodo: 18h luz / 6h escuro. Nutrição: <b>Nitrogênio (N)</b> alto para crescimento foliar. Técnicas: LST (Low Stress Training), topping, SCROG para controle de altura e aumento de produção.'],
        ['Floração (8–12 semanas)', 'Induzida reduzindo luz para 12h/dia (exceto autoflorescentes). Surgem os cálices, pistilos e tricomas. Nutrição: reduzir N, aumentar <b>Fósforo (P)</b> e <b>Potássio (K)</b>. Semana 6–8: flush final com água pura para eliminar resíduos de nutrientes.'],
      ]
    },
    {
      titulo: '✂️ Colheita',
      itens: [
        ['Quando Colher — Tricomas', 'O método mais preciso usa lupa 60–100x ou microscópio para observar tricomas:<br><br><b>Transparentes/Cristalinos:</b> Muito cedo — THC ainda se formando.<br><b>Leitosos/Opacos:</b> THC máximo — efeito mais cerebral e energético.<br><b>Âmbar (20–30%):</b> THC convertendo em CBN — efeito mais sedativo e corporal.<br><br>Para uso medicinal: geralmente 70–80% leitosos + 10–20% âmbar.'],
        ['Quando Colher — Pistilos', 'Método visual sem equipamento:<br><b>50–70% escuros/curvados:</b> Colheita precoce.<br><b>70–90% escuros/curvados:</b> Maturação ideal.<br><b>90–100% escuros:</b> Colheita tardia (mais CBN, menos THC).'],
        ['Processo de Corte', 'Cortar ramos principais ou planta inteira. Remover folhas fan (grandes, sem tricomas). Pendurar de cabeça para baixo em local escuro, temperatura 18–22°C, umidade 50–55%, ventilação suave. Secagem: 7–14 dias até galhos quebrarem ao dobrar.'],
      ]
    },
    {
      titulo: '🫙 Cura',
      itens: [
        ['Por que Curar?', 'A cura decompõe clorofila (reduz sabor de grama), converte amidos em açúcares, melhora aroma e sabor, potencializa efeitos e prolonga a conservação do material. Flores curadas podem durar 1–2 anos sem perda significativa.'],
        ['Como Curar', '1. Colocar flores em potes de vidro herméticos (Mason jars) — 75% cheios para deixar ar circular.<br>2. Primeiros 7–14 dias: abrir os potes 1–2x/dia por 15–30 min (processo chamado "burping") para liberar gases.<br>3. Manter em local escuro, 18–22°C, umidade interna 60–65% (usar Boveda 62 para controle preciso).<br>4. Cura mínima: 2–3 semanas. Ideal: 4–8 semanas. Premium: 3–6 meses.'],
        ['Sinais de Problemas', '<b>Mofo (Botrytis):</b> Manchas cinza/brancas, odor de bafio — descartar material afetado imediatamente.<br><b>Muito seco:</b> Tricomas se quebram, fumaça áspera — adicionar casca de laranja por 1 hora.<br><b>Muito úmido:</b> Flores pegajosas em excesso — deixar tampa aberta por mais tempo.'],
      ]
    },
  ]
};

const LEI_CULTIVO = {
  titulo: 'Lei de Cultivo',
  icone: '⚖️',
  id: 'lei_cultivo',
  aviso_extra: '⚠️ ATENÇÃO: Este conteúdo é informativo e não substitui orientação jurídica profissional. Consulte um advogado especializado antes de tomar qualquer decisão relacionada ao cultivo.',
  secoes: [
    {
      titulo: '📋 O Que Diz a Lei',
      itens: [
        ['Lei 11.343/2006 — Lei de Drogas', 'A Lei de Drogas proíbe o cultivo de cannabis sem autorização expressa da Anvisa. Não há distinção legal explícita entre cultivo para uso próprio e tráfico — a diferença fica a critério do juiz com base em quantidade, local e circunstâncias.<br><br>A Anvisa pode autorizar cultivo apenas para <b>pesquisa científica</b> ou <b>fabricação industrial</b> de produtos registrados — não para pacientes individuais.'],
        ['Decisões do STJ e STF', 'O <b>STJ e STF</b> têm concedido habeas corpus a pacientes que cultivam para uso medicinal próprio, com base em:<br><br>• Art. 196 CF — Direito à saúde<br>• Art. 1º CF — Dignidade da pessoa humana<br>• Princípio da proporcionalidade<br><br>Isso não legaliza o cultivo — oferece proteção judicial individual caso a caso. Cada processo é analisado separadamente.'],
      ]
    },
    {
      titulo: '🛡️ Habeas Corpus Preventivo',
      itens: [
        ['⚠️ Obrigatório Antes de Plantar', '<span style="color:#FF9800"><b>Não plante sem ter o habeas corpus em mãos.</b></span><br><br>O habeas corpus preventivo é o único instrumento que oferece proteção jurídica real contra prisão ou apreensão. Sem ele, mesmo com laudo médico, você pode ser autuado por tráfico ou cultivo ilegal.<br><br><b>Ordem obrigatória:</b><br>1. Obter laudo + receita médica<br>2. Contratar advogado especializado<br>3. Impetrar habeas corpus preventivo no TJ do seu estado<br>4. Aguardar concessão judicial<br>5. Somente então iniciar o cultivo'],
        ['O Que é e Como Funciona', 'Instrumento jurídico que protege o paciente <b>antes</b> de qualquer prisão ou apreensão. Funciona como uma ordem judicial que impede autoridades de prender ou processar o paciente pelo cultivo descrito na decisão.<br><br><b>Onde impetrar:</b> TJ (Tribunal de Justiça) do seu estado<br><b>Tempo médio:</b> Semanas a meses — varia por estado<br><b>Custo:</b> Honorários do advogado (Defensoria Pública é gratuita)'],
        ['Documentos Necessários', '• <b>Laudo médico</b> detalhado com diagnóstico e justificativa<br>• <b>Receita médica</b> indicando cannabis medicinal<br>• <b>RG e CPF</b><br>• <b>Comprovante de residência</b><br>• Histórico de tratamentos anteriores<br>• Declaração do médico sobre falha de outros tratamentos'],
      ]
    },
    {
      titulo: '👨‍⚖️ Apoio Jurídico',
      itens: [
        ['Onde Encontrar Advogados Especializados', '• <b>OAB Cannabis</b> — Comissão especial da OAB<br>• <b>ABRACANNABIS</b> — Lista de advogados parceiros por estado<br>• <b>APEPI / ABRACE / Flor da Vida</b> — Suporte jurídico a associados<br>• <b>Instituto Igarapé</b> — Advocacy em política de drogas<br>• Grupos de pacientes no Telegram/Facebook por estado<br><br><i>Verifique sempre a especialização em cannabis/saúde antes de contratar.</i>'],
        ['Defensoria Pública — Atendimento Gratuito', 'Pacientes de baixa renda têm direito a atendimento gratuito pela Defensoria Pública do estado.<br><br>• Presente em capitais e muitas cidades do interior<br>• Pode impetrar habeas corpus sem custo<br>• Buscar em defensoria.[seu-estado].def.br<br><br>Leve toda a documentação médica na primeira consulta.'],
      ]
    },
  ]
};

const CANABINOIDES = {
  titulo: 'Canabinoides & Terpenos',
  icone: '🔬',
  id: 'canabinoides',
  secoes: [
    {
      titulo: '⚗️ Canabinoides Principais',
      itens: [
        ['THC — Tetrahidrocanabinol', '<b>Ponto de vaporização:</b> 🌡️ 157°C<br><b>Psicoativo:</b> Sim<br><b>Efeitos:</b> Euforia, alteração sensorial, analgesia, estimulação de apetite, antinauseante, relaxamento muscular.<br><b>Aplicações médicas:</b> Dor crônica, náusea por quimioterapia, espasticidade, anorexia em HIV/AIDS.<br><b>Atenção:</b> Em doses altas ou em pessoas sensíveis pode causar ansiedade, paranoia e taquicardia. Contraindicado em menores e pessoas com predisposição a psicose.'],
        ['CBD — Canabidiol', '<b>Ponto de vaporização:</b> 🌡️ 160–180°C<br><b>Psicoativo:</b> Não<br><b>Efeitos:</b> Ansiolítico, anticonvulsivante, anti-inflamatório, neuroprotetor, antipsicótico leve.<br><b>Aplicações médicas:</b> Epilepsia (especialmente Dravet e Lennox-Gastaut), ansiedade, TEPT, inflamação crônica, dor neuropática.<br><b>No Brasil:</b> Regulamentado pela Anvisa. Produtos como Canabidiol Prati, Charlotte\'s Web e Epidiolex disponíveis com prescrição.'],
        ['CBG — Canabigerol', '<b>Ponto de vaporização:</b> 🌡️ 52°C (volátil a baixas temperaturas)<br><b>Psicoativo:</b> Não<br><b>Precursor:</b> Chamado de "mãe dos canabinoides" — THC e CBD são sintetizados a partir do CBG.<br><b>Efeitos:</b> Antibacteriano, neuroprotetor, anti-inflamatório intestinal, pode reduzir pressão intraocular (glaucoma).<br><b>Status:</b> Pesquisas em estágio inicial, disponível em algumas formulações especializadas.'],
        ['CBN — Canabidinol', '<b>Ponto de vaporização:</b> 🌡️ 185°C<br><b>Psicoativo:</b> Levemente (10–20% do THC)<br><b>Origem:</b> Produzido pela degradação oxidativa do THC (material envelhecido ou exposto ao calor/luz).<br><b>Efeitos:</b> Sedativo, analgésico, anti-inflamatório, potencial antibacteriano.<br><b>Uso:</b> Muito valorizado para distúrbios do sono. Encontrado em cultivares maduros com colheita tardia.'],
        ['CBC — Canabicrômeno', '<b>Ponto de vaporização:</b> 🌡️ 220°C<br><b>Psicoativo:</b> Não<br><b>Efeitos:</b> Anti-inflamatório, analgésico (potencializa THC e CBD), antidepressivo, pode estimular neuroplasticidade.<br><b>Pesquisa:</b> Promissor para dor, inflamação e saúde cerebral.'],
      ]
    },
    {
      titulo: '🌸 Terpenos Principais',
      itens: [
        ['Mirceno', '<b>Ponto de vaporização:</b> 🌡️ 168°C<br><b>Aroma:</b> Terra, almíscar, frutas tropicais<br><b>Efeitos:</b> Sedativo, relaxante muscular, analgésico. Facilita a passagem de canabinoides pela barreira hematoencefálica.<br><b>Encontrado em:</b> Manga, lúpulo, tomilho'],
        ['Limoneno', '<b>Ponto de vaporização:</b> 🌡️ 176°C<br><b>Aroma:</b> Cítrico, limão, laranja<br><b>Efeitos:</b> Ansiolítico, antidepressivo, antifúngico, potencializa absorção de outros terpenos.<br><b>Encontrado em:</b> Cascas cítricas, alecrim'],
        ['Pineno (α e β)', '<b>Ponto de vaporização:</b> 🌡️ α-Pineno 155°C | β-Pineno 166°C<br><b>Aroma:</b> Pinho, bosque<br><b>Efeitos:</b> Broncodilatador, anti-inflamatório, pode contrariar déficits de memória causados pelo THC, promove alerta e foco.<br><b>Encontrado em:</b> Pinheiro, sálvia, alecrim'],
        ['Linalol', '<b>Ponto de vaporização:</b> 🌡️ 198°C<br><b>Aroma:</b> Floral, lavanda<br><b>Efeitos:</b> Ansiolítico, sedativo, anestésico local, anticonvulsivante. Potencializa efeitos do CBD.<br><b>Encontrado em:</b> Lavanda, coentro, canela'],
        ['Cariofileno', '<b>Ponto de vaporização:</b> 🌡️ 119°C (ativo mesmo em baixas temperaturas)<br><b>Aroma:</b> Pimenta, especiarias, madeira<br><b>Efeitos:</b> Anti-inflamatório (age diretamente em receptores CB2), analgésico, gastroprotetor. Único terpeno que ativa o sistema endocanabinoide.<br><b>Encontrado em:</b> Pimenta preta, cravo, canela'],
        ['Terpinoleno', '<b>Ponto de vaporização:</b> 🌡️ 186°C<br><b>Aroma:</b> Floral, herbáceo, pinho<br><b>Efeitos:</b> Antioxidante, sedativo leve, antifúngico.<br><b>Encontrado em:</b> Maçã, lilás, pimentas'],
      ]
    },
    {
      titulo: '🧬 Efeito Entourage',
      itens: [
        ['O que é', 'O efeito entourage é a sinergia entre canabinoides, terpenos e flavonoides presentes na planta inteira. Quando combinados, esses compostos amplificam e modulam os efeitos uns dos outros de maneira mais eficaz do que qualquer composto isolado.<br><br>Exemplo: CBD isolado tem eficácia anticonvulsivante, mas o extrato de espectro completo (full spectrum) com THC, terpenos e outros canabinoides demonstra resultados superiores em estudos clínicos.'],
        ['Espectro Completo vs Isolado', '<b>Isolado (Isolate):</b> CBD puro 99%+. Sem THC. Previsível, sem risco de falso positivo em exame. Menos efeito entourage.<br><br><b>Broad Spectrum:</b> Múltiplos canabinoides + terpenos, THC removido (<0,3%). Efeito entourage parcial.<br><br><b>Full Spectrum:</b> Todos os compostos naturais incluindo THC (<0,3%). Maior efeito entourage. Pode causar falso positivo.'],
      ]
    },
    {
      titulo: '🌍 Indica vs Sativa vs Híbrida',
      itens: [
        ['Cannabis Indica', '<b>Origem:</b> Afeganistão, Paquistão, Índia<br><b>Aparência:</b> Plantas mais baixas, folhas largas e escuras<br><b>Perfil de efeitos (tradicional):</b> Relaxante, sedativo, corporal ("body high"), indicado para noite.<br><b>Terpenos comuns:</b> Mirceno, linalol, cariofileno<br><b>Uso médico:</b> Dor, insônia, espasmos musculares, estimulação de apetite<br><br><i>Nota: A distinção indica/sativa é simplificada. Na ciência moderna, o que determina o efeito é o perfil de canabinoides + terpenos, não a subespécie.</i>'],
        ['Cannabis Sativa', '<b>Origem:</b> Regiões equatoriais (América, África, Ásia)<br><b>Aparência:</b> Plantas altas, folhas finas e claras<br><b>Perfil de efeitos (tradicional):</b> Energizante, criativo, cerebral ("head high"), indicado para dia.<br><b>Terpenos comuns:</b> Limoneno, pineno, terpinoleno<br><b>Uso médico:</b> Depressão, fadiga, déficit de foco, náusea, dores de cabeça'],
        ['Cannabis Híbrida', 'A grande maioria das cultivares modernas são híbridas, cruzamentos entre indica e sativa. Podem ser:<br><br><b>Indica-dominante:</b> Mais relaxante<br><b>Sativa-dominante:</b> Mais energizante<br><b>Balanceada (50/50):</b> Efeitos equilibrados<br><br>Exemplos populares: Girl Scout Cookies, Blue Dream, OG Kush, White Widow, Gorilla Glue.'],
      ]
    },
  ]
};

const CONSUMO = {
  titulo: 'Métodos de Consumo',
  icone: '💨',
  id: 'consumo',
  secoes: [
    {
      titulo: '♨️ Vaporização — O Método Recomendado',
      itens: [
        ['Como Funciona', 'O vaporizador aquece o material (flor seca ou extrato) a temperaturas entre <b>160°C e 220°C</b> — abaixo do ponto de combustão (230°C+). Isso volatiliza os canabinoides e terpenos sem queimar o material vegetal.'],
        ['Faixas de Temperatura', '<b>160–170°C:</b> Efeito mais suave e cerebral. Preserva terpenos voláteis. Ideal para início de sessão.<br><br><b>170–185°C:</b> Equilíbrio entre sabor e potência. Ativa THC e CBD eficientemente.<br><br><b>185–200°C:</b> Efeito mais intenso e corporal. Ativa canabinoides de ponto mais alto como CBN.<br><br><b>200–220°C:</b> Extração máxima. Vapor mais denso. Pode degradar alguns terpenos delicados.'],
        ['Vantagens vs Combustão', '✅ Sem benzeno, monóxido de carbono ou alcatrão<br>✅ Temperatura controlada preserva terpenos e canabinoides<br>✅ Sabor e aroma significativamente melhores<br>✅ Menos irritação respiratória<br>✅ Maior eficiência — extrai mais canabinoides da mesma quantidade<br>✅ AVB (Already Vaped Bud) ainda pode ser usado em infusões'],
      ]
    },
    {
      titulo: '🚫 Combustão — Por Que Evitar',
      itens: [
        ['Os Riscos da Fumaça', 'A combustão de qualquer material orgânico a >230°C gera mais de <b>100 compostos tóxicos</b>, incluindo:<br><br>• <b>Benzeno:</b> Carcinogênico, leucemia<br>• <b>Monóxido de carbono (CO):</b> Reduz oxigenação do sangue<br>• <b>Alcatrão:</b> Deposita-se nos pulmões, causa bronquite crônica<br>• <b>Hidrocarbonetos policíclicos:</b> Mutagênicos<br>• <b>Acroleína:</b> Irritante pulmonar severo'],
        ['O Problema do Papel e Tabaco', 'Cigarros de cannabis frequentemente usam tabaco (mistura), adicionando os riscos da nicotina e dependência. O papel de cigarro também libera compostos ao queimar.<br><br><b>Baseado/Blunt:</b> Combinação de todos esses riscos. O método mais prejudicial para a saúde.<br><br><i>Mesmo sem tabaco, a combustão da cannabis causa irritação das vias aéreas superiores e inferiores.</i>'],
        ['Alternativa Mais Segura ao Fumo', 'Se a vaporização não estiver disponível, o cachimbo d\'água (bong) com água fria filtra parte das partículas, mas <b>não elimina</b> os compostos tóxicos da combustão. Ainda assim, preferível ao baseado. A melhor alternativa sempre será o vaporizador.'],
      ]
    },
    {
      titulo: '🧱 Prensado — O Que é e Por Que Evitar',
      itens: [
        ['O Que é o Prensado', 'O "prensado" (também chamado de tijolo, haxixe prensado ou <i>brick weed</i>) é cannabis de baixa qualidade comprimida em blocos para facilitar transporte e armazenamento no tráfico ilegal.<br><br>Difere do haxixe artesanal de qualidade (charas, dry sift, rosin): enquanto o haxixe legítimo é resina concentrada de tricomas, o prensado é material vegetal misturado, comprimido com alta pressão e calor, destruindo grande parte dos terpenos e canabinoides.'],
        ['Por Que o Prensado é Perigoso', 'O principal risco não é a cannabis em si, mas o que é <b>misturado</b> no processo de prensagem para aumentar o peso e volume:<br><br><b>Adulterantes comuns identificados em análises:</b><br>• <span style="color:#FF5252">Henna</span> — corante marrom/negro, causa reação inflamatória pulmonar<br>• <span style="color:#FF5252">Cera de sapato / polish</span> — hidrocarbonetos tóxicos ao inalar<br>• <span style="color:#FF5252">Areia e terra compactada</span> — partículas inaláveis causam pneumonite<br>• <span style="color:#FF5252">Breu e resinas sintéticas</span> — compostos voláteis tóxicos na combustão<br>• <span style="color:#FF5252">Açúcar e amido</span> — fermentam e favorecem fungos; risco de aspergilose<br>• <span style="color:#FF5252">Compostos plásticos / PE</span> — liberam dioxinas ao queimar<br>• <span style="color:#FF5252">Chumbo e metais pesados</span> — detectados em amostras europeias para aumentar peso'],
        ['Efeitos à Saúde', '<b>Curto prazo:</b><br>• Tosse intensa, chiado, irritação das vias aéreas<br>• Dores de cabeça atípicas (especialmente após henna/resinas)<br>• Náusea e mal-estar além do esperado<br>• Reações alérgicas (henna — parafenilenodiamina / PPD)<br><br><b>Longo prazo (uso frequente):</b><br>• Bronquite crônica e dano ao epitélio respiratório<br>• Pneumonite por corpo estranho (areia/terra)<br>• Acúmulo de metais pesados (chumbo, cádmio)<br>• Aspergilose pulmonar (fungos em material úmido/mal-curado)<br><br><b>Nota:</b> Esses danos são <i>adicionais</i> aos já causados pela combustão em si — que já gera benzeno, alcatrão e CO.'],
        ['Como Identificar Adulteração', '<b>Teste do vidro (adulteração com areia/terra):</b><br>Esfregue um pouco em vidro limpo — resíduo granular indica adulteração com areia.<br><br><b>Teste da bolha (bubble hash test):</b><br>Coloque um fragmento em chama: haxixe puro de resina borbulha e queima de forma uniforme. Adulterado cheirará a plástico, escurecerá de forma irregular ou não borbulhará.<br><br><b>Teste do metal quente:</b><br>Aquece uma agulha e toca o material — resina pura amolece e libera aroma de cannabis. Adulterantes plásticos derretem diferente, com odor químico.<br><br><b>Cor e textura:</b> Prensado legítimo (seco) tem tom verde-amarronzado. Material muito escuro/preto ou com brilho excessivo levanta suspeita.'],
        ['Alternativas Mais Seguras', 'Se não houver acesso a flor curada de qualidade:<br><br>• <b>Óleos e cápsulas via associação/farmácia</b> — produto testado, sem adulteração<br>• <b>Haxixe artesanal (dry sift / kief)</b> — produzido de material conhecido, sem aditivos<br>• <b>Rosin prensado a frio</b> — extração por pressão e calor de flor de qualidade, sem solventes<br><br><b>Regra geral:</b> Conhecer a origem do material é a única forma de garantir que não há adulteração.'],
      ]
    },
    {
      titulo: '💧 Via Sublingual (Óleos)',
      itens: [
        ['Como Funciona', 'O óleo é aplicado <b>sob a língua</b> e absorvido diretamente pela mucosa oral para a corrente sanguínea, evitando o metabolismo de primeira passagem hepática.<br><br><b>Início dos efeitos:</b> 15–45 minutos<br><b>Pico:</b> 1–2 horas<br><b>Duração:</b> 4–8 horas'],
        ['Vantagens', '✅ Sem risco respiratório<br>✅ Efeito mais duradouro que a vaporização<br>✅ Dosagem precisa com conta-gotas graduado<br>✅ Discreto e portátil<br>✅ Ideal para pacientes que não podem inalar'],
        ['Como Usar Corretamente', '1. Aplicar o óleo sob a língua com o conta-gotas<br>2. Manter por <b>60–90 segundos</b> antes de engolir<br>3. Evitar comer ou beber por 10–15 min após<br>4. Começar com dose baixa (1–2 gotas) e aguardar 2h antes de redosar — efeito sublingual é mais lento que inalação'],
      ]
    },
    {
      titulo: '🍪 Via Oral (Comestíveis)',
      itens: [
        ['Como Funciona', 'Cannabis infundida em alimentos ou cápsulas é absorvida pelo trato digestivo. O THC é metabolizado no fígado em 11-hidroxi-THC, composto mais potente e de efeito mais prolongado.<br><br><b>Início:</b> 30–90 minutos (até 2h em jejum)<br><b>Pico:</b> 2–4 horas<br><b>Duração:</b> 6–12 horas'],
        ['⚠️ Atenção com Dosagem', 'A via oral é a que mais frequentemente causa "overdoses" não intencionais. Nunca redosar antes de 2 horas.<br><br><b>Regra de ouro:</b> "Comece baixo, vá devagar."<br><br>Para produtos de farmácia/associação: seguir dosagem prescrita. Para óleos orais: 5–10mg de THC é dose inicial para adultos sem tolerância.'],
      ]
    },
    {
      titulo: '🧴 Via Tópica',
      itens: [
        ['Como Funciona', 'Cremes, loções, bálsamos e adesivos transdérmicos com canabinoides aplicados diretamente na pele.<br><br><b>Tópicos regulares:</b> Agem localmente, não entram na corrente sanguínea — <b>sem efeito psicoativo</b>.<br><br><b>Transdérmicos (adesivos):</b> Atravessam a barreira da pele e atingem a corrente sanguínea — efeito sistêmico.'],
        ['Indicações', '• Dores musculares e articulares localizadas<br>• Artrite e inflamação local<br>• Neuropatia periférica<br>• Condições de pele (psoríase, eczema)<br>• Tensão muscular pós-exercício'],
      ]
    },
  ]
};

const VAPORIZADORES = {
  titulo: 'Vaporizadores',
  icone: '🌬️',
  id: 'vaporizadores',
  secoes: [
    {
      titulo: '📱 Tipos de Vaporizadores',
      itens: [
        ['Caneta Vape (Vape Pen)', '<b>Para:</b> Concentrados (óleo, distillate, wax)<br><b>Preço:</b> R$ 80–300<br><b>Vantagens:</b> Extremamente portátil, discreto, fácil de usar<br><b>Desvantagens:</b> Não funciona com flor seca, cartuchos descartáveis geram resíduo, qualidade variável do extrato<br><b>Indicado para:</b> Iniciantes em vaporização, uso discreto'],
        ['Vaporizador Portátil de Flor Seca', '<b>Para:</b> Flor seca, haxixe (com tela)<br><b>Preço:</b> R$ 300–2.000+<br><b>Vantagens:</b> Portátil, bateria recarregável, controle de temperatura, uso com flor natural<br><b>Desvantagens:</b> Necessita limpeza regular, bateria limitada<br><b>Modelos populares:</b> DynaVap (R$400–700), Pax 3 (R$800+), Mighty/Crafty+ (R$1.500+), Arizer Air/Solo'],
        ['Vaporizador Desktop', '<b>Para:</b> Flor seca e concentrados<br><b>Preço:</b> R$ 1.500–5.000+<br><b>Vantagens:</b> Maior eficiência de extração, temperatura precisa, sem preocupação com bateria, vapor mais suave<br><b>Desvantagens:</b> Não portátil, maior investimento<br><b>Modelos referência:</b> Volcano Hybrid (Storz & Bickel, R$4.000+), Arizer Extreme Q (R$1.500), Plenty'],
      ]
    },
    {
      titulo: '🏺 Câmara de Aquecimento',
      itens: [
        ['Cerâmica', '<b>Características:</b> Aquecimento mais uniforme, inerte quimicamente, não altera sabor<br><b>Sabor:</b> Mais limpo e puro — ideal para apreciação de terpenos<br><b>Durabilidade:</b> Alta, mas frágil a impactos<br><b>Limpeza:</b> Fácil com álcool isopropílico<br><b>Indicada para:</b> Usuários que priorizam sabor e uso medicinal'],
        ['Metal (Aço Inox / Liga)', '<b>Características:</b> Mais resistente a impactos<br><b>Sabor:</b> Pode adicionar leve sabor metálico, especialmente em altas temperaturas<br><b>Durabilidade:</b> Muito alta<br><b>Atenção:</b> Evitar câmaras de alumínio — liberam partículas em altas temperaturas. Aço cirúrgico e titânio são seguros.'],
        ['Quartzo e Vidro', '<b>Características:</b> Encontrado em dab rigs e vaporizers de concentrado<br><b>Sabor:</b> Neutro, excelente para concentrados<br><b>Durabilidade:</b> Frágil, requer cuidado<br><b>Temperatura:</b> Precisa de aquecimento externo (tocha) em rigs tradicionais, ou elemento elétrico em e-nails'],
      ]
    },
    {
      titulo: '🎯 Como Escolher',
      itens: [
        ['Por Perfil de Uso', '<b>Iniciante / Custo-benefício:</b><br>DynaVap M (aquecido por maçarico) — R$400–500. Sem bateria, durabilidade extrema, aprendizado da técnica.<br><br><b>Uso diário portátil:</b><br>Mighty+ ou Crafty+ (Storz & Bickel) — R$1.500–2.000. Padrão-ouro em portáteis, convecção híbrida, vapor excelente.<br><br><b>Uso doméstico / médico:</b><br>Volcano Hybrid — R$4.000+. Referência global, uso em balão ou whip, vapor suave e eficiente.<br><br><b>Econômico portátil:</b><br>Arizer Solo 2 / Air 2 — R$600–900. Excelente custo-benefício, troca de bateria possível.'],
        ['Dicas de Compra', '• Comprar de revendedores autorizados para garantia<br>• Verificar tensão elétrica (110V/220V ou bivolt)<br>• Pesquisar no Reddit r/vaporents para reviews reais<br>• Desconfiar de modelos muito baratos sem procedência<br>• Manter nota fiscal para acionamento de garantia<br>• Kit básico: vaporizador + escova de limpeza + álcool isopropílico 99%'],
        ['Manutenção', '<b>Limpeza após cada uso:</b> Escovar câmara ainda morna<br><b>Limpeza semanal (uso diário):</b> Algodão embebido em álcool 99% na câmara e bocal<br><b>Tela (screen):</b> Substituir a cada 2–4 semanas<br><b>Caminho do vapor (vapor path):</b> Limpar com pipe cleaner e álcool mensalmente<br><b>Câmara de vidro:</b> Imergir em solução de álcool + sal grosso e agitar'],
      ]
    },
  ]
};

const ASSOCIACOES = {
  titulo: 'Associações de Cannabis',
  icone: '🏛️',
  id: 'associacoes',
  secoes: [
    {
      titulo: '⚖️ Marco Legal no Brasil',
      itens: [
        ['Regulamentação Anvisa', 'A <b>RDC 660/2022</b> (atualizada pela RDC 327/2019) da Anvisa regula o acesso à cannabis medicinal no Brasil por dois caminhos:<br><br><b>1. Produtos registrados/notificados:</b> Canabidiol Prati-Donaduzzi, Charlotte\'s Web, Epidiolex — disponíveis em farmácias com prescrição.<br><br><b>2. Importação por pessoa física:</b> Para produtos não disponíveis no Brasil, mediante autorização da Anvisa (formulário online), prescrição médica e laudo médico.'],
        ['Associações de Pacientes', 'As associações são entidades sem fins lucrativos que cultivam cannabis e fornecem produtos aos associados. Operam em uma <b>zona cinza jurídica</b> — não são formalmente legalizadas, mas decisões judiciais têm protegido suas atividades com base no direito à saúde e dignidade humana.<br><br>Vantagens sobre farmácia:<br>• Maior variedade de produtos (full spectrum, tinturas, cápsulas)<br>• Custo significativamente menor<br>• Acesso a cultivares com perfis específicos de canabinoides'],
      ]
    },
    {
      titulo: '📋 Como se Associar',
      itens: [
        ['Documentos Necessários', 'Os requisitos variam por associação, mas geralmente incluem:<br><br>• <b>RG e CPF</b> (ou CNH)<br>• <b>Comprovante de residência</b> recente<br>• <b>Laudo médico</b> descrevendo a condição de saúde<br>• <b>Prescrição médica</b> (receita) de profissional habilitado<br>• Em alguns casos: exames ou relatório do histórico de tratamentos<br><br><i>Dica: Médicos especializados em cannabis medicinal facilitam o processo. Plataformas como Dr. Cannabis conectam pacientes a prescritores.</i>'],
        ['Processo Passo a Passo', '1. Consultar médico e obter laudo + prescrição<br>2. Pesquisar associações atuantes na sua região ou que operem online<br>3. Entrar em contato com a associação via site ou redes sociais<br>4. Enviar documentação para análise<br>5. Pagar a taxa de associação (anual, geralmente R$50–200)<br>6. Aguardar aprovação e retirada/envio dos produtos<br><br><b>Tempo médio:</b> 1–4 semanas após aprovação dos documentos'],
        ['Custos Típicos', '<b>Taxa de associação:</b> R$50–200/ano<br><b>Óleo CBD 1.500mg (30ml):</b> R$150–350<br><b>Óleo Full Spectrum:</b> R$200–500<br><b>Cápsulas (60 un.):</b> R$180–400<br><br>Compare: produtos de farmácia similares custam 3–5x mais. Importação Anvisa tem custo adicional de logística internacional.'],
      ]
    },
    {
      titulo: '📄 Documentação por Canal de Acesso',
      itens: [
        ['⭐ Associações (ex: Flor da Vida)', 'O processo mais acessível para a maioria dos pacientes:<br><br>✅ <b>Receita médica</b> — prescrição de médico habilitado<br>✅ <b>Laudo médico</b> — documento descrevendo o diagnóstico<br>✅ RG/CPF e comprovante de residência<br><br><span style="color:#4CAF50">Não exige autorização da Anvisa.</span> Processo mais simples, produtos mais baratos e maior variedade.'],
        ['Farmácias (produtos registrados Anvisa)', 'Para produtos como Canabidiol Prati-Donaduzzi:<br><br>✅ <b>Receita médica</b> com retenção<br>✅ <b>Laudo médico</b><br><br>Disponível nas principais redes (Ultrafarma, Drogasil, Pague Menos). Sem autorização Anvisa pois o produto já é registrado no Brasil.'],
        ['Importação via Autorização Anvisa', 'Para produtos não registrados no Brasil (Charlotte\'s Web, Elixinol, etc.):<br><br>✅ <b>Receita médica</b><br>✅ <b>Laudo médico</b><br>✅ <b>Autorização Anvisa</b> — solicitada em anvisa.gov.br/cannabis<br><br>Processo mais burocrático. A autorização é pessoal e intransferível. Válida por 1 ano, renovável. Tempo médio de aprovação: 3–10 dias úteis.'],
        ['Como Obter a Autorização Anvisa', '1. Acesse <b>anvisa.gov.br/cannabis</b><br>2. Crie conta no portal Gov.br<br>3. Preencha o formulário de solicitação<br>4. Anexe: receita médica + laudo + RG<br>5. Aguarde análise (geralmente 3–10 dias úteis)<br>6. Receba autorização por e-mail<br>7. Use a autorização para importar ou comprar em plataformas autorizadas<br><br><i>Dica: A plataforma Dr. Cannabis e HempMeds Brasil auxiliam no processo.</i>'],
      ]
    },
    {
      titulo: '🏢 Principais Associações no Brasil',
      itens: [
        ['⭐ Flor da Vida — Associação de Pacientes', '<b>Site:</b> flordavida.ong.br/site/<br><b>Documentação exigida:</b><br>✅ Receita médica<br>✅ Laudo médico<br><span style="color:#4CAF50">Não exige autorização Anvisa.</span><br><br><b>Perfil:</b> ONG dedicada ao acesso à cannabis medicinal, atendimento humanizado, foco em pacientes que precisam de suporte.<br><b>Produtos:</b> Óleos, tinturas e outros — full spectrum e CBD isolado.'],
        ['ABRACE — Associação Brasileira de Pacientes de Cannabis', '<b>Estado:</b> Ceará (Fortaleza)<br><b>Fundação:</b> 2014 — pioneira no Brasil<br><b>Perfil:</b> Atende principalmente crianças com epilepsia refratária<br><b>Contato:</b> abraceceara.org.br'],
        ['APEPI — Ação pela Paz e pelo Instituto da Planta', '<b>Estado:</b> Rio de Janeiro<br><b>Perfil:</b> Foco em epilepsia pediátrica, ativismo e pesquisa<br><b>Destaque:</b> Uma das mais antigas e reconhecidas do RJ'],
        ['ACNPP — Associação Cannabis para Neuro e Psiquiatria de Porto Alegre', '<b>Estado:</b> Rio Grande do Sul<br><b>Perfil:</b> Foco em transtornos neurológicos e psiquiátricos'],
        ['ASPECAN — Associação de Pacientes e Familiares Usuários de Cannabis', '<b>Estado:</b> São Paulo<br><b>Perfil:</b> Grande base de associados, variedade de produtos'],
        ['Outras Associações por Estado', 'O número de associações no Brasil cresce anualmente. Para encontrar a mais próxima ou que melhor atenda seu caso:<br><br>• Consulte o site da <b>ABRACANNABIS</b> (Associação Brasileira de Cannabis)<br>• Grupos de Facebook/WhatsApp de pacientes por estado<br>• Plataforma Dr. Cannabis tem lista curada<br>• Associação Nacional de Farmacêuticos (CFF) para produtos farmacêuticos'],
      ]
    },
  ]
};

const ONDE_COMPRAR = {
  titulo: 'Onde Comprar',
  icone: '🛒',
  id: 'onde_comprar',
  secoes: [
    {
      titulo: '💊 Produtos Medicinais (Óleos, Cápsulas)',
      itens: [
        ['Farmácias com Produtos Anvisa', '<b>Canabidiol Prati-Donaduzzi:</b> Disponível em farmácias convencionais (Pague Menos, Drogasil, Ultrafarma). Necessita receita médica. Concentrações: 200mg, 600mg, 1200mg em 30ml.<br><br><b>Importação via Anvisa:</b> Para produtos internacionais (Charlotte\'s Web, Elixinol, etc.) — solicitar autorização em anvisa.gov.br/cannabis.<br><br><b>Farmácias de manipulação:</b> Algumas manipulam CBD em diferentes concentrações mediante laudo e receita.'],
        ['Associações de Pacientes', 'Veja seção "Associações" para lista completa e processo de associação.<br><br>Vantagens: menor custo, maior variedade, suporte de comunidade.<br>Requisito: laudo médico + documentação.'],
        ['Plataformas Online Especializadas', '<b>Dr. Cannabis:</b> Telemedicina + marketplace de produtos regulamentados<br><b>Cannect:</b> Plataforma de prescrição e acesso a produtos<br><b>HempMeds Brazil:</b> Importadora de produtos Charlotte\'s Web<br><br><i>Atenção: Desconfie de sites sem CNPJ claro, sem produtos com laudos de análise (COA) e que vendam THC livremente.</i>'],
      ]
    },
    {
      titulo: '💨 Vaporizadores',
      itens: [
        ['Lojas Físicas', 'Principais cidades têm head shops e grow shops que vendem vaporizadores:<br><br><b>São Paulo:</b> Concentração maior no centro e Vila Madalena<br><b>Rio de Janeiro:</b> Ipanema, Lapa<br><b>Outras cidades:</b> Buscar "grow shop [cidade]" no Google Maps'],
        ['⭐ Loja High420 — Vaporizadores de Ervas', '<b>Site:</b> lojahigh420.com/vaporizadores/vaporizador-de-ervas/<br><b>Especialidade:</b> Vaporizadores de ervas nacionais e importados, acessórios e peças de reposição.<br><b>Destaques:</b> Amplo catálogo de portáteis e desktops, atendimento especializado, envio para todo o Brasil.'],
        ['Outras Lojas Online Nacionais', '• Dankstop Brasil<br>• Vaporizer Shop Brasil<br>• Grow Indoor (equipamentos)<br>• Mercado Livre (revendedores verificados — atenção à procedência)<br><br><b>Dica:</b> Para garantia válida e produto original, prefira revendedores autorizados pelos fabricantes (Storz & Bickel tem revendedores oficiais no Brasil).'],
        ['Importação Direta', 'Vaporizadores podem ser importados sem restrição legal (são equipamentos de uso pessoal).<br><br><b>AliExpress:</b> Marcas asiáticas de entrada (cuidado com qualidade)<br><b>VaporizerWizard.com:</b> Reviews + links para revendedores<br><b>PuffItUp.com:</b> Especializado, envia internacionalmente<br><br><b>Imposto de importação:</b> Produtos acima de US$50 podem ser taxados (60% do valor + IOF). Frete + taxa pode elevar custo final significativamente.'],
      ]
    },
  ]
};

const VARIEDADES = {
  titulo: 'Variedades & Strains',
  icone: '🌿',
  id: 'variedades',
  secoes: [
    {
      titulo: '🌿 Hemp — Cânhamo Industrial',
      itens: [
        ['O que é o Hemp', '<b>Espécie:</b> Cannabis sativa L. (baixo THC)<br><b>THC:</b> &lt;0,3% (legal internacionalmente)<br><b>CBD:</b> Alto — principal fonte comercial de CBD<br><br>O hemp é cultivado para fibra, óleo de semente, CBD e uso industrial. Não produz efeito psicoativo. É a base da maioria dos produtos CBD vendidos em farmácias e associações no Brasil.<br><br><b>Cultivares conhecidas:</b> Charlotte\'s Web, Elektra, Sour Space Candy, Special Sauce, Hawaiian Haze'],
        ['Diferença Hemp vs Cannabis "Comum"', '<b>Hemp:</b> Sativa, alta, fibra longa, THC &lt;0,3%, CBD alto<br><b>Cannabis medicinal/recreativa:</b> THC variável (5–30%+), selecionada para flores com tricomas<br><br>Geneticamente são a mesma espécie — a diferença está na seleção ao longo de gerações para perfis opostos de canabinoides.'],
      ]
    },
    {
      titulo: '🏔️ Família Kush',
      itens: [
        ['Hindu Kush', '<b>Origem:</b> Montanhas Hindu Kush (Afeganistão/Paquistão)<br><b>Tipo:</b> Indica pura<br><b>THC:</b> 15–20% | <b>CBD:</b> ~1%<br><b>Terpenos:</b> Mirceno, cariofileno, linalol<br><b>Aroma:</b> Terra, sândalo, pinho suave<br><b>Efeitos:</b> Relaxamento profundo, sedação, analgesia corporal<br><b>Uso médico:</b> Dor crônica, insônia, espasmos musculares<br><b>Perfil:</b> Landrace clássica — base genética de centenas de indica modernas'],
        ['OG Kush', '<b>Origem:</b> Florida/California, anos 90<br><b>Tipo:</b> Híbrida indica-dominante<br><b>THC:</b> 19–26% | <b>CBD:</b> &lt;1%<br><b>Terpenos:</b> Mirceno, limoneno, cariofileno<br><b>Aroma:</b> Limão, pinho, combustível/diesel<br><b>Efeitos:</b> Euforia inicial, relaxamento profundo, fome intensa<br><b>Uso médico:</b> Dor, estresse, depressão, insônia<br><b>Perfil:</b> Uma das mais influentes do mundo — gerou Bubba Kush, GSC, Gelato e dezenas de outras'],
        ['Bubba Kush', '<b>Origem:</b> California (OG Kush x landrace afgã)<br><b>Tipo:</b> Indica dominante<br><b>THC:</b> 17–22%<br><b>Terpenos:</b> Mirceno, cariofileno, linalol<br><b>Aroma:</b> Café, cacau, terra, hash<br><b>Efeitos:</b> "Body melt" intenso, sedação, euforia suave<br><b>Uso médico:</b> Insônia severa, dor crônica, TEPT'],
        ['Purple Kush', '<b>Tipo:</b> Indica pura (Hindu Kush x Purple Afghani)<br><b>THC:</b> 17–22%<br><b>Terpenos:</b> Mirceno, cariofileno, linalol<br><b>Aroma:</b> Uva, terra, doce<br><b>Cor:</b> Flores roxo-intensas por antocianinas (genética, não temperatura)<br><b>Efeitos:</b> Sedação total, relaxamento físico, felicidade<br><b>Uso médico:</b> Insônia, dor, ansiedade noturna'],
      ]
    },
    {
      titulo: '☀️ Família Haze',
      itens: [
        ['Haze Original', '<b>Origem:</b> Santa Cruz, California, anos 60–70<br><b>Tipo:</b> Sativa pura (landrace colombiana, mexicana, tailandesa e indiana)<br><b>THC:</b> 20–23% | <b>Floração:</b> 14–16 semanas<br><b>Terpenos:</b> Terpinoleno, ocimeno, mirceno<br><b>Aroma:</b> Cítrico, floral, terroso suave<br><b>Efeitos:</b> Energizante, criativo, cerebral intenso<br><b>Perfil:</b> Ancestral de quase todas as sativas modernas premium'],
        ['Amnesia Haze', '<b>Origem:</b> Amsterdam (Haze x afghã/tailandesa/hawaiiana)<br><b>Tipo:</b> Sativa dominante (70–80%)<br><b>THC:</b> 20–25%<br><b>Terpenos:</b> Terpinoleno, mirceno, ocimeno<br><b>Aroma:</b> Limão intenso, terra, especiarias<br><b>Efeitos:</b> Euforia cerebral, foco criativo, energia — pode causar desorientação em doses altas<br><b>Uso médico:</b> Depressão, fadiga, déficit de foco'],
        ['Super Silver Haze', '<b>Origem:</b> Shantibaba/Mr. Nice Seeds (Haze x Skunk x Northern Lights)<br><b>Tipo:</b> Sativa dominante<br><b>THC:</b> 18–23%<br><b>Terpenos:</b> Mirceno, terpinoleno, cariofileno<br><b>Aroma:</b> Cítrico, skunk, terroso<br><b>Efeitos:</b> Energizante, eufórico, duradouro<br><b>Prêmios:</b> High Times Cannabis Cup 3 anos consecutivos (1997–1999)'],
        ['Lemon Haze', '<b>Tipo:</b> Sativa dominante (Silver Haze x Lemon Skunk)<br><b>THC:</b> 17–22%<br><b>Terpenos:</b> Limoneno dominante, terpinoleno, cariofileno<br><b>Aroma:</b> Limão siciliano muito intenso, cítrico, doce<br><b>Efeitos:</b> Levantamento de humor, criatividade, alegria<br><b>Uso médico:</b> Depressão, ansiedade leve, fadiga'],
      ]
    },
    {
      titulo: '🦨 Família Skunk',
      itens: [
        ['Skunk #1', '<b>Origem:</b> Sacred Seeds, California, anos 70<br><b>Tipo:</b> Híbrida equilibrada (Afghani x Acapulco Gold x Colombian Gold)<br><b>THC:</b> 15–19%<br><b>Terpenos:</b> Mirceno, cariofileno, limoneno<br><b>Aroma:</b> Forte, penetrante, terra + cítrico — aroma "skunk" clássico<br><b>Efeitos:</b> Equilibrado corpo-mente, eufórico, relaxante<br><b>Legado:</b> Uma das cultivares mais influentes da história — base genética de centenas de híbridas europeias e americanas'],
        ['Super Skunk', '<b>Tipo:</b> Indica dominante (Skunk #1 x Afghani)<br><b>THC:</b> 18–22%<br><b>Terpenos:</b> Mirceno, cariofileno<br><b>Aroma:</b> Skunk amplificado, mais terroso e pesado<br><b>Efeitos:</b> Mais sedativo que Skunk #1, relaxamento corporal intenso<br><b>Uso médico:</b> Dor, insônia, inapetência'],
      ]
    },
    {
      titulo: '🌸 Híbridas Premium',
      itens: [
        ['Girl Scout Cookies (GSC)', '<b>Origem:</b> Bay Area, California (OG Kush x Durban Poison)<br><b>Tipo:</b> Híbrida indica-dominante<br><b>THC:</b> 19–28%<br><b>Terpenos:</b> Cariofileno, limoneno, linalol<br><b>Aroma:</b> Doce, terra, menta, notas de baunilha<br><b>Efeitos:</b> Euforia cerebral + relaxamento corporal equilibrado, fome intensa, bem-estar<br><b>Uso médico:</b> Dor, náusea, depressão, inapetência<br><b>Filhas famosas:</b> Gelato, Wedding Cake, Sherbet'],
        ['Gelato (Larry Bird)', '<b>Origem:</b> San Francisco (Sunset Sherbet x Thin Mint GSC)<br><b>Tipo:</b> Híbrida equilibrada a levemente indica<br><b>THC:</b> 20–25%<br><b>Terpenos:</b> Cariofileno, limoneno, mirceno<br><b>Aroma:</b> Doce cremoso, frutas, lavanda — como sorvete<br><b>Efeitos:</b> Euforia rápida e intensa, relaxamento sem sedação total<br><b>Uso médico:</b> Dor muscular, estresse, depressão'],
        ['Blue Dream', '<b>Origem:</b> California (Blueberry x Haze)<br><b>Tipo:</b> Sativa dominante<br><b>THC:</b> 17–24% | <b>CBD:</b> ~2%<br><b>Terpenos:</b> Mirceno, cariofileno, pineno<br><b>Aroma:</b> Mirtilo/blueberry, frutal, doce<br><b>Efeitos:</b> Euforia cerebral suave, motivação, relaxamento sem sedação<br><b>Uso médico:</b> Depressão, fadiga, dor leve — ótima para uso diurno'],
        ['White Widow', '<b>Origem:</b> Holanda, anos 90 (Brazilian Sativa x South Indian Indica)<br><b>Tipo:</b> Híbrida equilibrada<br><b>THC:</b> 18–25%<br><b>Terpenos:</b> Mirceno, cariofileno, pineno<br><b>Aroma:</b> Pinho, terra, amadeirado<br><b>Visual:</b> Flores cobertas de tricomas brancos — daí o nome<br><b>Efeitos:</b> Energizante, conversação, euforia cerebral + relaxamento leve<br><b>Uso médico:</b> Depressão, fadiga, dor leve, estresse'],
        ['Gorilla Glue #4 (GG4)', '<b>Origem:</b> GG Strains (Chem\'s Sister x Sour Dubb x Chocolate Diesel)<br><b>Tipo:</b> Híbrida indica-dominante<br><b>THC:</b> 25–30%+<br><b>Terpenos:</b> Cariofileno, mirceno, limoneno<br><b>Aroma:</b> Diesel, terra, café, pinho<br><b>Efeitos:</b> Sedação intensa, "colado no sofá", euforia inicial, analgesia potente<br><b>Uso médico:</b> Dor severa, insônia, TEPT — <b>não recomendada para iniciantes</b>'],
        ['Wedding Cake (Pink Cookies)', '<b>Tipo:</b> Indica dominante (Triangle Kush x Animal Mints)<br><b>THC:</b> 22–27%<br><b>Terpenos:</b> Cariofileno, limoneno, mirceno<br><b>Aroma:</b> Baunilha, doce, terra, pimenta<br><b>Efeitos:</b> Relaxamento profundo, euforia inicial, sedação gradual<br><b>Uso médico:</b> Dor crônica, ansiedade, insônia'],
      ]
    },
    {
      titulo: '🌴 Sativas Tropicais & Landrace',
      itens: [
        ['Durban Poison', '<b>Origem:</b> Durban, África do Sul — landrace pura<br><b>Tipo:</b> Sativa pura<br><b>THC:</b> 18–26%<br><b>Terpenos:</b> Terpinoleno, ocimeno, mirceno<br><b>Aroma:</b> Anis, alcaçuz, doce, terra<br><b>Efeitos:</b> Energizante extremo, foco intenso, produtividade — "o espresso da cannabis"<br><b>Uso médico:</b> Depressão, TDAH, fadiga, náusea<br><b>Perfil:</b> Genética base para GSC, Cookies e muitas híbridas modernas'],
        ['Jack Herer', '<b>Origem:</b> Holanda, anos 90 (Haze x Red Skunk x Northern Lights #5)<br><b>Tipo:</b> Sativa dominante<br><b>THC:</b> 18–24% | <b>CBD:</b> ~1%<br><b>Terpenos:</b> Terpinoleno, pineno, ocimeno<br><b>Aroma:</b> Pinho, especiarias, cítrico, floral<br><b>Efeitos:</b> Clareza mental, criatividade, foco, levantamento de humor<br><b>Uso médico:</b> Depressão, TDAH, fadiga, náusea matinal'],
        ['Manga Rosa (Brazilian)', '<b>Origem:</b> Brasil — cultivar nacional muito popular<br><b>Tipo:</b> Híbrida sativa-dominante<br><b>THC:</b> 16–22%<br><b>Terpenos:</b> Mirceno dominante, limoneno<br><b>Aroma:</b> Manga tropical intensa, doce, frutado — muito reconhecível e valorizado<br><b>Efeitos:</b> Euforia, alegria, relaxamento suave, sociável<br><b>Uso médico:</b> Depressão, estresse, inapetência<br><b>Perfil:</b> Uma das mais amadas no Brasil pela identidade tropical'],
        ['Pineapple Express', '<b>Tipo:</b> Híbrida sativa-dominante (Trainwreck x Hawaiian)<br><b>THC:</b> 19–25%<br><b>Terpenos:</b> Terpinoleno, ocimeno, cariofileno<br><b>Aroma:</b> Abacaxi tropical, cítrico, pinho<br><b>Efeitos:</b> Energizante, eufórico, criativo, levantamento de humor<br><b>Uso médico:</b> Depressão, fadiga, dor leve'],
        ['Hawaiian Haze', '<b>Tipo:</b> Sativa hemp/CBD ou sativa recreativa<br><b>THC:</b> &lt;0,3% (versão hemp) | variável em recreativa<br><b>CBD:</b> Alto na versão hemp<br><b>Terpenos:</b> Ocimeno, mirceno, terpinoleno<br><b>Aroma:</b> Tropical, floral, frutas exóticas<br><b>Efeitos:</b> Levantamento de humor, energia suave<br><b>Perfil:</b> Popular como hemp CBD de sabor agradável'],
      ]
    },
    {
      titulo: '❄️ Indica Clássicas',
      itens: [
        ['Northern Lights #5', '<b>Origem:</b> Seattle/Amsterdam (landrace afghã x thai)<br><b>Tipo:</b> Indica quase pura<br><b>THC:</b> 16–21%<br><b>Terpenos:</b> Mirceno, linalol, cariofileno<br><b>Aroma:</b> Pinho, terra, notas adocicadas<br><b>Efeitos:</b> Sedação física profunda, euforia suave, analgesia<br><b>Uso médico:</b> Insônia, dor crônica, espasmos, TEPT<br><b>Legado:</b> Múltiplos Cannabis Cup, base para Shiva Skunk, Cheese e muitas indica europeias'],
        ['Blueberry', '<b>Origem:</b> DJ Short, anos 70 (afghã x thai x mexicana)<br><b>Tipo:</b> Indica dominante<br><b>THC:</b> 17–20%<br><b>Terpenos:</b> Mirceno, linalol, cariofileno<br><b>Aroma:</b> Mirtilo fresco, doce, floral — muito característico<br><b>Cor:</b> Pode desenvolver tons azuis/roxos no frio<br><b>Efeitos:</b> Relaxante, felicidade, sedação gradual<br><b>Uso médico:</b> Insônia, dor, estresse<br><b>Legado:</b> Genitor do Blue Dream e muitas "Blue" strains'],
        ['Afghan Kush', '<b>Origem:</b> Afeganistão — landrace pura<br><b>Tipo:</b> Indica pura<br><b>THC:</b> 15–20% | <b>Resina:</b> Altíssima (base para haxixe)<br><b>Terpenos:</b> Mirceno, cariofileno, humuleno<br><b>Aroma:</b> Terra, hash, madeira, doce suave<br><b>Efeitos:</b> Sedação pesada, relaxamento total, sono<br><b>Uso médico:</b> Insônia severa, dor intensa, ansiedade grave'],
      ]
    },
    {
      titulo: '🍋 Strains CBD Alto (Medicinais)',
      itens: [
        ["Charlotte's Web", "<b>Origem:</b> Colorado (Stanley Brothers, 2011)<br><b>Tipo:</b> Hemp — sativa<br><b>CBD:</b> 13–20% | <b>THC:</b> &lt;0,3%<br><b>Terpenos:</b> Mirceno, cariofileno, terpinoleno<br><b>Aroma:</b> Floral, terra, pinho suave<br><b>Efeitos:</b> Sem psicoativo — anti-inflamatório, ansiolítico, anticonvulsivante<br><b>História:</b> Desenvolvida para Charlotte Figi, criança com síndrome de Dravet — reduziu convulsões de 300/sem para ~3/mês<br><b>No Brasil:</b> Disponível via importação Anvisa"],
        ['ACDC', '<b>Tipo:</b> Híbrida CBD (Cannatonic x Ruderalis)<br><b>CBD:</b> 14–20% | <b>THC:</b> &lt;1% | <b>Ratio:</b> ~20:1 CBD:THC<br><b>Terpenos:</b> Mirceno, cariofileno, pineno<br><b>Aroma:</b> Terra, pinho, frutal suave<br><b>Efeitos:</b> Sem psicoativo — analgesia, ansiolítico, anti-inflamatório<br><b>Uso médico:</b> Dor neuropática, esclerose múltipla, epilepsia, ansiedade'],
        ['Cannatonic', '<b>Tipo:</b> Híbrida equilibrada (MK Ultra x G13 Haze)<br><b>CBD:</b> 6–17% | <b>THC:</b> 6–17% | <b>Ratio:</b> 1:1 a 5:1 CBD:THC<br><b>Terpenos:</b> Mirceno, cariofileno, pineno<br><b>Aroma:</b> Cítrico, terra, pinho<br><b>Efeitos:</b> Relaxamento sem sedação, clareza mental, analgesia suave<br><b>Uso médico:</b> Dor, ansiedade, espasmos — versatilidade para uso diurno'],
        ['Harlequin', '<b>Tipo:</b> Sativa dominante CBD (Colombia x Nepal x Thailand x Switzerland)<br><b>CBD:</b> 8–16% | <b>THC:</b> 4–7% | <b>Ratio:</b> ~5:2 CBD:THC<br><b>Terpenos:</b> Mirceno, cariofileno, pineno<br><b>Aroma:</b> Manga, musk, terra<br><b>Efeitos:</b> Alerta, foco, analgesia sem intoxicação<br><b>Uso médico:</b> Dor, inflamação, ansiedade — ideal para uso diurno'],
      ]
    },
    {
      titulo: '🔮 Exóticas & Tendências',
      itens: [
        ['Runtz (White/Pink)', '<b>Origem:</b> California (Zkittlez x Gelato)<br><b>Tipo:</b> Híbrida equilibrada<br><b>THC:</b> 19–29%<br><b>Terpenos:</b> Cariofileno, limoneno, linalol<br><b>Aroma:</b> Balas de fruta, doce, cremoso — muito distinto<br><b>Efeitos:</b> Euforia intensa e duradoura, relaxamento corporal, fome<br><b>Visual:</b> Flores multicoloridas (verde, roxo, laranja)'],
        ['Zkittlez', '<b>Origem:</b> California (Grape Ape x Grapefruit)<br><b>Tipo:</b> Indica dominante<br><b>THC:</b> 15–23%<br><b>Terpenos:</b> Cariofileno, linalol, humuleno<br><b>Aroma:</b> Frutas tropicais, uva, balas — muito adocicado<br><b>Efeitos:</b> Relaxamento, felicidade, levantamento de humor, sedação suave<br><b>Prêmios:</b> Melhor indica no Emerald Cup 2016'],
        ['MAC (Miracle Alien Cookies)', '<b>Tipo:</b> Híbrida (Alien Cookies x Colombian x Starfighter)<br><b>THC:</b> 20–26%<br><b>Terpenos:</b> Cariofileno, limoneno, mirceno<br><b>Aroma:</b> Floral, cítrico, cremoso, diesel suave<br><b>Efeitos:</b> Euforia criativa equilibrada com relaxamento<br><b>Visual:</b> Tricomas excepcionalmente densos'],
        ['Mimosa', '<b>Tipo:</b> Sativa dominante (Clementine x Purple Punch)<br><b>THC:</b> 19–27%<br><b>Terpenos:</b> Limoneno, cariofileno, mirceno<br><b>Aroma:</b> Laranja fresca, cítrico, floral — como a bebida<br><b>Efeitos:</b> Levantamento de humor, energia, criatividade, sociável<br><b>Uso médico:</b> Depressão, fadiga, ansiedade social'],
        ['Gelato 41 / 45', '<b>Tipo:</b> Variações da família Gelato (Cookie Fam Genetics)<br><b>THC:</b> 20–26%<br><b>Diferenças:</b><br><b>#41 (Bacio Gelato):</b> Mais escura, floral, intensa — sedação<br><b>#45 (Sundae Driver cross):</b> Mais doce, frutada, equilibrada<br><b>Terpenos:</b> Cariofileno, mirceno, limoneno<br><b>Perfil:</b> Numeração indica fenotipo diferente da mesma cruz genética'],
      ]
    },
    {
      titulo: '📊 Como Comparar Strains',
      itens: [
        ['O Que Realmente Importa', 'O nome de uma strain é guia, não garantia. O efeito real depende de:<br><br>1. <b>Perfil de canabinoides:</b> THC%, CBD%, CBG%, CBN%<br>2. <b>Perfil de terpenos:</b> Mirceno, limoneno, cariofileno, etc.<br>3. <b>Fenotipo:</b> A mesma strain cultivada diferente pode variar muito<br>4. <b>Cura e armazenamento:</b> Afetam terpenos residuais<br>5. <b>Seu endocanabinoide individual:</b> Cada pessoa responde diferente<br><br><i>Strains com nomes iguais de produtores diferentes podem ter perfis completamente distintos.</i>'],
        ['Indica vs Sativa — A Verdade Científica', 'A distinção indica/sativa como preditor de efeito é <b>simplificada e frequentemente imprecisa</b>.<br><br>O que realmente define o efeito:<br>• <b>Relação THC:CBD</b> — quanto CBD há para modular o THC<br>• <b>Terpenos dominantes</b> — mirceno = sedativo, limoneno/terpinoleno = energizante<br>• <b>Sua tolerância e bioquímica</b><br><br>Conclusão: leia o COA (laudo de análise) e os terpenos, não apenas "indica ou sativa".'],
      ]
    },
  ]
};

const TODAS_SECOES = [LEI_CULTIVO, CULTIVO, CANABINOIDES, VARIEDADES, CONSUMO, VAPORIZADORES, ASSOCIACOES, ONDE_COMPRAR];

// Quiz data
const PERGUNTAS = [
  {
    id: 'finalidade',
    pergunta: 'Qual é a sua principal finalidade?',
    opcoes: [
      ['dor',        '🩹  Dor crônica / Dor neuropática'],
      ['ansiedade',  '🧠  Ansiedade, pânico ou TEPT'],
      ['epilepsia',  '⚡  Epilepsia ou convulsões'],
      ['sono',       '😴  Distúrbios do sono / Insônia'],
      ['recreativo', '😊  Uso recreativo / Bem-estar'],
      ['outro',      '❓  Outro / Não sei ainda'],
    ],
  },
  {
    id: 'diagnostico',
    pergunta: 'Você possui diagnóstico médico e acompanhamento profissional?',
    opcoes: [
      ['sim', '✅  Sim — tenho médico acompanhando'],
      ['nao', '❌  Não — ainda não consultei um médico'],
    ],
  },
  {
    id: 'gastrico',
    pergunta: 'Você tem sensibilidade gástrica ou problemas intestinais?',
    opcoes: [
      ['sim', '✅  Sim — tenho gastrite, SII ou sensibilidade'],
      ['nao', '❌  Não — sem problemas gastrointestinais'],
    ],
  },
  {
    id: 'efeito',
    pergunta: 'Qual tipo de início de efeito você prefere?',
    opcoes: [
      ['imediato', '⚡  Imediato — efeito em minutos (vaporização)'],
      ['gradual',  '🌊  Gradual — efeito mais suave e duradouro (óleo/sublingual)'],
    ],
  },
  {
    id: 'experiencia',
    pergunta: 'Você tem experiência prévia com cannabis?',
    opcoes: [
      ['sim', '✅  Sim — já usei cannabis antes'],
      ['nao', '🌱  Não — sou iniciante / nunca usei'],
    ],
  },
];

function calcularResultado(respostas) {
  const finalidade  = respostas.finalidade  || 'outro';
  const diagnostico = respostas.diagnostico === 'sim';
  const gastrico    = respostas.gastrico    === 'sim';
  const efeito      = respostas.efeito      || 'gradual';
  const experiencia = respostas.experiencia === 'sim';

  let produto, ratio;
  if (finalidade === 'epilepsia') {
    produto = 'CBD Alto (10:1 ou maior) — full spectrum ou isolado';
    ratio   = 'CBD dominante (ex.: 20:1 CBD:THC)';
  } else if (finalidade === 'ansiedade') {
    produto = 'CBD Alto (10:1 ou maior) — broad spectrum ou isolado';
    ratio   = 'CBD dominante — THC mínimo para evitar piora da ansiedade';
  } else if (finalidade === 'dor') {
    if (experiencia) {
      produto = 'Balanceado (1:1 CBD:THC) ou CBD moderado (5:1)';
      ratio   = 'Full spectrum 1:1 — sinergia para dor crônica';
    } else {
      produto = 'CBD moderado (5:1 ou 10:1) — iniciar com THC baixo';
      ratio   = 'Começar com CBD alto e ajustar gradualmente';
    }
  } else if (finalidade === 'sono') {
    if (experiencia) {
      produto = 'Indica-dominante com CBN e/ou CBD (2:1)';
      ratio   = 'THC moderado + CBN para sono profundo';
    } else {
      produto = 'CBD alto com linalol (terpeno sedativo)';
      ratio   = 'CBD alto — colheita tardia (mais CBN)';
    }
  } else if (finalidade === 'recreativo') {
    if (experiencia) {
      produto = 'Conforme preferência — híbrida ou sativa para dia, indica para noite';
      ratio   = 'THC moderado a alto, conforme tolerância';
    } else {
      produto = 'CBD moderado (5:1) para primeiras experiências';
      ratio   = 'Iniciar com CBD — adaptar ao efeito antes de THC';
    }
  } else {
    produto = 'CBD moderado (5:1) como ponto de partida';
    ratio   = 'Consultar médico para orientação personalizada';
  }

  let metodo, detalheMetodo, vaporizador;
  if (efeito === 'imediato') {
    metodo = 'Vaporização de flor seca ou concentrado';
    detalheMetodo = 'Vaporizador portátil ou desktop. Temperatura 170–185°C. Efeito em 5–15 minutos, duração 1–3 horas.';
    vaporizador = true;
  } else {
    if (gastrico) {
      metodo = 'Óleo sublingual (sob a língua)';
      detalheMetodo = 'Manter o óleo sob a língua por 60–90 segundos antes de engolir. Absorção pela mucosa evita o trato digestivo. Efeito em 15–45 min, duração 4–8 horas.';
    } else {
      metodo = 'Óleo sublingual ou cápsulas';
      detalheMetodo = 'Sublingual: início em 15–45 min. Cápsulas: início em 30–90 min, efeito mais uniforme. Duração 4–8 horas. Ideal para uso contínuo.';
    }
    vaporizador = false;
  }

  let caminho, detalheCaminho;
  if (!diagnostico) {
    caminho = 'Primeiro passo: consultar médico';
    detalheCaminho = 'Sem laudo médico não é possível acessar produtos via farmácia nem a maioria das associações. Plataformas como Dr. Cannabis conectam você a médicos especializados em cannabis medicinal para consulta online.';
  } else if (finalidade === 'epilepsia') {
    caminho = 'Farmácia (Anvisa) ou Associação';
    detalheCaminho = 'Para epilepsia, há produtos aprovados pela Anvisa (Canabidiol Prati, Epidiolex). Associações oferecem maior variedade e custo-benefício. Seu médico neurologista pode te orientar sobre a melhor formulação.';
  } else if (['dor', 'ansiedade', 'sono'].includes(finalidade)) {
    caminho = 'Associação de Cannabis (recomendado) ou Farmácia';
    detalheCaminho = 'Associações oferecem maior variedade de produtos, full spectrum e custo 3–5x menor que farmácias. Veja a seção "Associações" para lista das principais e como se associar.';
  } else {
    caminho = 'Associação de Cannabis';
    detalheCaminho = 'Para o seu perfil, uma associação de cannabis oferece a maior flexibilidade de produtos. Consulte a seção "Associações" no app.';
  }

  let alerta = null;
  if (finalidade === 'epilepsia') {
    alerta = '⚠️ IMPORTANTE: Epilepsia requer acompanhamento médico rigoroso. Nunca suspenda medicamentos anticonvulsivantes sem orientação médica. A cannabis medicinal pode ser usada como terapia complementar.';
  } else if (!diagnostico) {
    alerta = '⚠️ Sem diagnóstico médico, o uso de cannabis pode mascarar condições que precisam de tratamento específico. Busque orientação profissional antes.';
  }

  return { produto, ratio, metodo, detalheMetodo, caminho, detalheCaminho, vaporizador, alerta };
}
