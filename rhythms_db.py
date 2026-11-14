# rhythms_db.py

RHYTHMS = {
    # ==================== GENERAL / INTERNATIONAL ====================
    "pop_rock_basic": {
        "pt": {
            "name": "Pop / Rock Básico",
            "category": "Geral",
            "description": "A batida mais versátil da música ocidental. Excelente para desenvolver coordenação."
        },
        "en": {
            "name": "Basic Pop / Rock",
            "category": "General",
            "description": "The most versatile strumming pattern in Western music. Great for building coordination."
        },
        "time_signature": "4/4",
        "default_bpm": 100,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "↑", "-", "↑", "↓ (T)", "↑"],
        "sounds": ["B", None, "T", "U", None, "U", "T", "U"]
    },
    "ballad_folk": {
        "pt": {
            "name": "Balada / Folk",
            "category": "Geral",
            "description": "Leve e fluida, ideal para músicas acústicas lentas e dedilhados rasqueados."
        },
        "en": {
            "name": "Ballad / Folk",
            "category": "General",
            "description": "Light and flowing pattern, ideal for slow acoustic songs and gentle strumming."
        },
        "time_signature": "4/4",
        "default_bpm": 80,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "-", "↓ (B)", "↑", "↓ (T)", "↑"],
        "sounds": ["B", None, "T", None, "B", "U", "T", "U"]
    },
    "waltz": {
        "pt": {
            "name": "Valsa",
            "category": "Geral",
            "description": "Compasso ternário clássico: um tempo forte seguido de dois tempos leves."
        },
        "en": {
            "name": "Waltz",
            "category": "General",
            "description": "Classic triple-meter feel: one strong downbeat followed by two light beats."
        },
        "time_signature": "3/4",
        "default_bpm": 110,
        "subdivision": 3,
        "count": ["1", "2", "3"],
        "arrows": ["↓ (B)", "↓ (T)", "↓ (T)"],
        "sounds": ["B", "T", "T"]
    },
    "guarania": {
        "pt": {
            "name": "Guarânia",
            "category": "Geral",
            "description": "Ritmo ternário tradicional sul-americano, muito presente na música sertaneja raiz."
        },
        "en": {
            "name": "Guarânia",
            "category": "General",
            "description": "Traditional South American triple-meter rhythm, common in classic country ballads."
        },
        "time_signature": "3/4",
        "default_bpm": 92,
        "subdivision": 6,
        "count": ["1", "e", "2", "e", "3", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "↑", "↓ (T)", "↑"],
        "sounds": ["B", None, "T", "U", "T", "U"]
    },
    "reggae_offbeat": {
        "pt": {
            "name": "Reggae",
            "category": "Geral",
            "description": "Ênfase total nos contratempos ('e') com abafamento seco após cada ataque."
        },
        "en": {
            "name": "Reggae",
            "category": "General",
            "description": "Strong emphasis on the offbeats ('and') with crisp muted stabs."
        },
        "time_signature": "4/4",
        "default_bpm": 85,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["-", "↓ (S)", "-", "↓ (S)", "-", "↓ (S)", "-", "↓ (S)"],
        "sounds": [None, "S", None, "S", None, "S", None, "S"]
    },
    "blues_shuffle": {
        "pt": {
            "name": "Blues Shuffle",
            "category": "Geral",
            "description": "Balanço ternário ('swing feel'), omitindo a nota do meio de cada tercina."
        },
        "en": {
            "name": "Blues Shuffle",
            "category": "General",
            "description": "Triplet swing feel, skipping the middle note of each triplet group."
        },
        "time_signature": "12/8",
        "default_bpm": 90,
        "subdivision": 6,
        "count": ["1", "trip", "let", "2", "trip", "let"],
        "arrows": ["↓ (B)", "-", "↑", "↓ (T)", "-", "↑"],
        "sounds": ["B", None, "U", "T", None, "U"]
    },
    "funk_groove": {
        "pt": {
            "name": "Funk / Groove",
            "category": "Geral",
            "description": "Subdivisão em semicolcheias (16 avos) com acentos sincopados e notas fantasmas."
        },
        "en": {
            "name": "Funk / Groove",
            "category": "General",
            "description": "16th-note subdivision with syncopated accents and muted percussive ghost strokes."
        },
        "time_signature": "4/4",
        "default_bpm": 98,
        "subdivision": 16,
        "count": ["1", "e", "n", "a", "2", "e", "n", "a", "3", "e", "n", "a", "4", "e", "n", "a"],
        "arrows": ["↓ (B)", "-", "↑", "-", "↓ (S)", "-", "↑", "↓ (T)", "-", "↑", "↓ (S)", "-", "↓ (T)", "↑", "-", "↑"],
        "sounds": ["B", None, "U", None, "S", None, "U", "T", None, "U", "S", None, "T", "U", None, "U"]
    },
    "bolero": {
        "pt": {
            "name": "Bolero",
            "category": "Geral",
            "description": "Clássico latino romântico com bordão marcante seguido de resposta suave."
        },
        "en": {
            "name": "Bolero",
            "category": "General",
            "description": "Romantic Latin classic featuring a prominent bass note followed by gentle chords."
        },
        "time_signature": "4/4",
        "default_bpm": 88,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "↑", "↓ (B)", "-", "↓ (T)", "-"],
        "sounds": ["B", None, "T", "U", "B", None, "T", None]
    },
    "country_boom_chick": {
        "pt": {
            "name": "Country / Folk Alternado",
            "category": "Geral",
            "description": "Estilo 'Boom-Chick': alterna bordões graves com batidas agudas cheias."
        },
        "en": {
            "name": "Country / Boom-Chick",
            "category": "General",
            "description": "Classic alternating bass notes followed by crisp full-chord strums."
        },
        "time_signature": "4/4",
        "default_bpm": 115,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "↑", "↓ (B)", "-", "↓ (T)", "↑"],
        "sounds": ["B", None, "T", "U", "B", None, "T", "U"]
    },
    "disco_pop": {
        "pt": {
            "name": "Disco / Pop Dance",
            "category": "Geral",
            "description": "Pulsação constante nos 4 tempos com puxadas abertas brilhantes no contratempo."
        },
        "en": {
            "name": "Disco / Pop Dance",
            "category": "General",
            "description": "Four-on-the-floor pulse with bright open upstrokes on every offbeat."
        },
        "time_signature": "4/4",
        "default_bpm": 118,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (S)", "↑", "↓ (B)", "↑", "↓ (S)", "↑"],
        "sounds": ["B", "U", "S", "U", "B", "U", "S", "U"]
    },
    "odd_meter_5_4": {
        "pt": {
            "name": "Compasso Ímpar / Take Five",
            "category": "Geral",
            "description": "Agrupamento assimétrico de 5 tempos (3 + 2), excelente para destravar a coordenação."
        },
        "en": {
            "name": "Odd Meter / Take Five",
            "category": "General",
            "description": "Asymmetric 5-beat grouping (3 + 2), ideal for developing rhythmic independence."
        },
        "time_signature": "5/4",
        "default_bpm": 128,
        "subdivision": 10,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e", "5", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "↑", "↓ (S)", "-", "↓ (B)", "-", "↓ (S)", "↑"],
        "sounds": ["B", None, "T", "U", "S", None, "B", None, "S", "U"]
    },

    # ==================== BRAZILIAN RHYTHMS ====================
    "traditional_samba": {
        "pt": {
            "name": "Samba Tradicional",
            "category": "Brasil",
            "description": "Marcação de surdo no grave (B) e síncope do tamborim nos agudos (T) e puxadas (↑)."
        },
        "en": {
            "name": "Traditional Samba",
            "category": "Brazil",
            "description": "Surdo bass pulse (B) paired with syncopated tamborim accents (T) and upstrokes (↑)."
        },
        "time_signature": "2/4",
        "default_bpm": 96,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (T)", "↑", "↓ (B)", "↑", "↓ (T)", "-"],
        "sounds": ["B", "U", "T", "U", "B", "U", "T", None]
    },
    "bossa_nova": {
        "pt": {
            "name": "Bossa Nova",
            "category": "Brasil",
            "description": "Polegar constante nos tempos 1 e 2, enquanto os dedos desenham a clave sincopada."
        },
        "en": {
            "name": "Bossa Nova",
            "category": "Brazil",
            "description": "Steady thumb on beats 1 and 2 while fingers pluck a syncopated clave pattern."
        },
        "time_signature": "2/4",
        "default_bpm": 115,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B+T)", "-", "↑ (T)", "↓ (B)", "-", "↑ (T)", "↓ (B)", "↑ (T)"],
        "sounds": ["B", None, "T", "B", None, "T", "B", "T"]
    },
    "partido_alto": {
        "pt": {
            "name": "Partido Alto",
            "category": "Brasil",
            "description": "Samba sincopado de roda com acento percussivo seco e resposta rápida."
        },
        "en": {
            "name": "Partido Alto",
            "category": "Brazil",
            "description": "Syncopated roda de samba groove with sharp percussive slaps and quick upstrokes."
        },
        "time_signature": "2/4",
        "default_bpm": 100,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (S)", "↑", "-", "↑", "↓ (B)", "↑"],
        "sounds": ["B", None, "S", "U", None, "U", "B", "U"]
    },
    "pagode": {
        "pt": {
            "name": "Pagode",
            "category": "Brasil",
            "description": "Levada swingada com abafamento característico do tantã e repique de mão."
        },
        "en": {
            "name": "Pagode",
            "category": "Brazil",
            "description": "Swung samba subgenre featuring distinctive muted slaps mimicking tantã and repique."
        },
        "time_signature": "2/4",
        "default_bpm": 104,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (S)", "↑", "↓ (B)", "↑", "↓ (S)", "↑"],
        "sounds": ["B", "U", "S", "U", "B", "U", "S", "U"]
    },
    "samba_cancao": {
        "pt": {
            "name": "Samba-Canção",
            "category": "Brasil",
            "description": "Samba lento e sentimental, com bordão expressivo e condução suave."
        },
        "en": {
            "name": "Samba-Canção",
            "category": "Brazil",
            "description": "Slow, romantic samba style with expressive bass notes and gentle strumming."
        },
        "time_signature": "2/4",
        "default_bpm": 76,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (T)", "↑", "↓ (B)", "-", "↓ (S)", "↑"],
        "sounds": ["B", "U", "T", "U", "B", None, "S", "U"]
    },
    "samba_enredo": {
        "pt": {
            "name": "Samba-Enredo",
            "category": "Brasil",
            "description": "Condução acelerada e contínua inspirada nas baterias das escolas de samba."
        },
        "en": {
            "name": "Samba-Enredo",
            "category": "Brazil",
            "description": "Fast, continuous Carnival parade samba groove driven by relentless percussion."
        },
        "time_signature": "2/4",
        "default_bpm": 134,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (T)", "↑", "↓ (B)", "↓ (T)", "↓ (S)", "↑"],
        "sounds": ["B", "U", "T", "U", "B", "T", "S", "U"]
    },
    "mpb_groove": {
        "pt": {
            "name": "MPB / Groove Pop Brasileiro",
            "category": "Brasil",
            "description": "Levada sincopada moderna típica de Djavan, Gilberto Gil e Seu Jorge."
        },
        "en": {
            "name": "MPB / Brazilian Pop Groove",
            "category": "Brazil",
            "description": "Modern syncopated acoustic groove inspired by Djavan, Gilberto Gil, and Seu Jorge."
        },
        "time_signature": "4/4",
        "default_bpm": 98,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (S)", "↑", "-", "↑", "↓ (S)", "↑"],
        "sounds": ["B", "U", "S", "U", None, "U", "S", "U"]
    },
    "baiao": {
        "pt": {
            "name": "Baião",
            "category": "Brasil",
            "description": "Célula rítmica da zabumba: grave forte na cabeça, contratempo agudo e grave antes do tempo 2."
        },
        "en": {
            "name": "Baião",
            "category": "Brazil",
            "description": "Zabumba drum pattern: strong bass downbeat, crisp upstroke, and anticipatory bass."
        },
        "time_signature": "2/4",
        "default_bpm": 108,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↑ (T)", "↓ (B)", "-", "↓ (T)", "↑", "-"],
        "sounds": ["B", None, "U", "B", None, "T", "U", None]
    },
    "xote": {
        "pt": {
            "name": "Xote",
            "category": "Brasil",
            "description": "Ritmo nordestino cadenciado e dançante, com dois graves marcados e resposta aguda."
        },
        "en": {
            "name": "Xote",
            "category": "Brazil",
            "description": "Steady, danceable Northeastern rhythm with two distinct bass pulses and bright response."
        },
        "time_signature": "4/4",
        "default_bpm": 95,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (B)", "-", "↓ (T)", "↑", "↓ (T)", "↑"],
        "sounds": ["B", None, "B", None, "T", "U", "T", "U"]
    },
    "forro_universitario": {
        "pt": {
            "name": "Forró Universitário / Pé-de-Serra",
            "category": "Brasil",
            "description": "Levada ágil entre o xote e o arrasta-pé, com alternância marcante de grave e abafado."
        },
        "en": {
            "name": "Forró Pé-de-Serra",
            "category": "Brazil",
            "description": "Lively forró groove sitting between xote and arrasta-pé with crisp muted accents."
        },
        "time_signature": "2/4",
        "default_bpm": 122,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (S)", "↑", "↓ (B)", "-", "↓ (T)", "↑"],
        "sounds": ["B", "U", "S", "U", "B", None, "T", "U"]
    },
    "arrasta_pe": {
        "pt": {
            "name": "Arrasta-pé",
            "category": "Brasil",
            "description": "Forró acelerado de festa junina, alternando graves rápidos e puxadas brilhantes."
        },
        "en": {
            "name": "Arrasta-pé",
            "category": "Brazil",
            "description": "Fast-paced June Festival forró alternating rapid bass notes and bright upstrokes."
        },
        "time_signature": "2/4",
        "default_bpm": 140,
        "subdivision": 4,
        "count": ["1", "e", "2", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (T)", "↑"],
        "sounds": ["B", "U", "T", "U"]
    },
    "maracatu": {
        "pt": {
            "name": "Maracatu",
            "category": "Brasil",
            "description": "Peso ancestral das alfaias pernambucanas com acentos graves sincopados."
        },
        "en": {
            "name": "Maracatu",
            "category": "Brazil",
            "description": "Heavy, ancestral Pernambuco alfaia drum feel with syncopated bass accents."
        },
        "time_signature": "4/4",
        "default_bpm": 92,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (B)", "↓ (T)", "-", "↓ (B)", "↓ (T)", "↑"],
        "sounds": ["B", None, "B", "T", None, "B", "T", "U"]
    },
    "frevo": {
        "pt": {
            "name": "Frevo",
            "category": "Brasil",
            "description": "Andamento vibrante e acelerado com ataques secos e sincopados no contratempo."
        },
        "en": {
            "name": "Frevo",
            "category": "Brazil",
            "description": "Vibrant, high-energy Carnival tempo with sharp syncopated offbeat stabs."
        },
        "time_signature": "2/4",
        "default_bpm": 145,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (S)", "↑", "↓ (B)", "↓ (T)", "↓ (S)", "↑"],
        "sounds": ["B", "U", "S", "U", "B", "T", "S", "U"]
    },
    "ijexa": {
        "pt": {
            "name": "Ijexá",
            "category": "Brasil",
            "description": "Toque suave e hipnótico dos afoxés da Bahia, cadenciado pelo agogô."
        },
        "en": {
            "name": "Ijexá",
            "category": "Brazil",
            "description": "Smooth, hypnotic Afro-Bahian afoxé groove guided by the agogô bell pattern."
        },
        "time_signature": "4/4",
        "default_bpm": 90,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↓ (T)", "↓ (B)", "-", "↓ (T)", "↓ (B)", "↓ (T)", "-"],
        "sounds": ["B", "T", "B", None, "T", "B", "T", None]
    },
    "axe_samba_reggae": {
        "pt": {
            "name": "Axé / Samba-Reggae",
            "category": "Brasil",
            "description": "Fusão baiana poderosa com graves marcados e repiques percussivos no meio do compasso."
        },
        "en": {
            "name": "Axé / Samba-Reggae",
            "category": "Brazil",
            "description": "Powerful Bahian fusion combining heavy bass pulses with percussive mid-bar slaps."
        },
        "time_signature": "4/4",
        "default_bpm": 112,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (S)", "↑", "↓ (B)", "↓ (B)", "↓ (S)", "↑"],
        "sounds": ["B", None, "S", "U", "B", "B", "S", "U"]
    },
    "choro": {
        "pt": {
            "name": "Choro",
            "category": "Brasil",
            "description": "Baixaria conduzindo a harmonia com resposta ágil de pandeiro e cavaquinho."
        },
        "en": {
            "name": "Choro",
            "category": "Brazil",
            "description": "Walking basslines driving the harmony with agile pandeiro and cavaquinho responses."
        },
        "time_signature": "2/4",
        "default_bpm": 102,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (T)", "↑", "↓ (B)", "↑", "↓ (T)", "↑"],
        "sounds": ["B", "U", "T", "U", "B", "U", "T", "U"]
    },
    "maxixe": {
        "pt": {
            "name": "Maxixe",
            "category": "Brasil",
            "description": "O 'tango brasileiro': síncope característica de colcheia-semicolcheia-colcheia."
        },
        "en": {
            "name": "Maxixe",
            "category": "Brazil",
            "description": "The 'Brazilian tango': signature syncopated feel with snappy offbeat accents."
        },
        "time_signature": "2/4",
        "default_bpm": 110,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "-", "↓ (T)", "↓ (B)", "↑", "↓ (T)", "-"],
        "sounds": ["B", "U", None, "T", "B", "U", "T", None]
    },
    "carimbo": {
        "pt": {
            "name": "Carimbó",
            "category": "Brasil",
            "description": "Ritmo amazônico contagiante com pulsação marcante de curimbó e maracas."
        },
        "en": {
            "name": "Carimbó",
            "category": "Brazil",
            "description": "Infectious Amazonian rhythm driven by curimbó drums and maracas."
        },
        "time_signature": "2/4",
        "default_bpm": 126,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "↑", "↓ (B)", "↓ (B)", "↓ (T)", "↑"],
        "sounds": ["B", None, "T", "U", "B", "B", "T", "U"]
    },
    "ciranda": {
        "pt": {
            "name": "Ciranda",
            "category": "Brasil",
            "description": "Ritmo tradicional do litoral nordestino, cadenciado como o balanço das ondas."
        },
        "en": {
            "name": "Ciranda",
            "category": "Brazil",
            "description": "Traditional Northeastern coastal rhythm with a hypnotic, wave-like sway."
        },
        "time_signature": "4/4",
        "default_bpm": 98,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "-", "↓ (B)", "↓ (B)", "↓ (T)", "-"],
        "sounds": ["B", None, "T", None, "B", "B", "T", None]
    },
    "marchinha": {
        "pt": {
            "name": "Marchinha de Carnaval",
            "category": "Brasil",
            "description": "Ritmo binário alegre e saltitante, tradicional dos carnavais antigos."
        },
        "en": {
            "name": "Carnival Marchinha",
            "category": "Brazil",
            "description": "Upbeat, bouncy duple-meter rhythm from classic Brazilian Carnival."
        },
        "time_signature": "2/4",
        "default_bpm": 124,
        "subdivision": 4,
        "count": ["1", "e", "2", "e"],
        "arrows": ["↓ (B)", "↓ (T)", "↓ (B)", "↓ (T)"],
        "sounds": ["B", "T", "B", "T"]
    },
    "vanerao": {
        "pt": {
            "name": "Vanerão",
            "category": "Brasil",
            "description": "Ritmo gaúcho enérgico e dançante, com forte marcação de baixo e batida cheia."
        },
        "en": {
            "name": "Vanerão",
            "category": "Brazil",
            "description": "Energetic Southern Brazilian dance rhythm with strong bass and full-chord strums."
        },
        "time_signature": "2/4",
        "default_bpm": 132,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "↑", "↓ (B)", "↓ (T)", "↓ (S)", "↑"],
        "sounds": ["B", None, "T", "U", "B", "T", "S", "U"]
    },
    "chamame": {
        "pt": {
            "name": "Chamamé",
            "category": "Brasil",
            "description": "Sobreposição rítmica entre 6/8 e 3/4 típica do sul do Brasil e litoral argentino."
        },
        "en": {
            "name": "Chamamé",
            "category": "Brazil",
            "description": "Polymetric 6/8 and 3/4 cross-rhythm native to Southern Brazil and Argentina."
        },
        "time_signature": "6/8",
        "default_bpm": 116,
        "subdivision": 6,
        "count": ["1", "2", "3", "4", "5", "6"],
        "arrows": ["↓ (B)", "↑", "↓ (T)", "↓ (B)", "↓ (T)", "↑"],
        "sounds": ["B", "U", "T", "B", "T", "U"]
    },
    "moda_de_viola": {
        "pt": {
            "name": "Moda de Viola",
            "category": "Brasil",
            "description": "Batida tradicional caipira, marcando com clareza os bordões e acordes abertos."
        },
        "en": {
            "name": "Moda de Viola",
            "category": "Brazil",
            "description": "Traditional Brazilian country strumming highlighting open bass strings and chords."
        },
        "time_signature": "4/4",
        "default_bpm": 105,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "↑", "↓ (B)", "↓ (T)", "↓ (T)", "↑"],
        "sounds": ["B", None, "T", "U", "B", "T", "T", "U"]
    },
    "sertanejo_universitario": {
        "pt": {
            "name": "Sertanejo Universitário / Arrocha",
            "category": "Brasil",
            "description": "Batida moderna com grave firme e abafamento percussivo nos tempos 2 e 4."
        },
        "en": {
            "name": "Modern Sertanejo / Arrocha",
            "category": "Brazil",
            "description": "Modern Brazilian country groove with solid bass and percussive slaps on beats 2 and 4."
        },
        "time_signature": "4/4",
        "default_bpm": 102,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (S)", "↑", "-", "↑", "↓ (S)", "↑"],
        "sounds": ["B", None, "S", "U", None, "U", "S", "U"]
    },
    "funk_carioca": {
        "pt": {
            "name": "Funk Carioca",
            "category": "Brasil",
            "description": "A célula sincopada clássica ('Tamborzão'): Tum-tá-tá-tum-tá."
        },
        "en": {
            "name": "Carioca Funk",
            "category": "Brazil",
            "description": "The iconic syncopated 'Tamborzão' cell: Boom-ch-ch-boom-ch."
        },
        "time_signature": "4/4",
        "default_bpm": 130,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "-", "↓ (S)", "-", "-", "↓ (B)", "↓ (S)"],
        "sounds": ["B", None, None, "S", None, None, "B", "S"]
    },
    "brega": {
        "pt": {
            "name": "Brega",
            "category": "Brasil",
            "description": "Pulsação romântica e popular com marcação constante de baixo e resposta aberta."
        },
        "en": {
            "name": "Brega",
            "category": "Brazil",
            "description": "Romantic, upbeat popular groove with steady bass pulses and open chord responses."
        },
        "time_signature": "4/4",
        "default_bpm": 118,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "-", "↓ (B)", "↑", "↓ (T)", "↑"],
        "sounds": ["B", None, "T", None, "B", "U", "T", "U"]
    },
    # ==================== NEW GENERAL / LATIN / INTERNATIONAL ====================
    "rumba_flamenca": {
        "pt": {
            "name": "Rumba Flamenca",
            "category": "Geral",
            "description": "Levada espanhola vibrante com tapa percussivo no tampo e rasqueados rápidos."
        },
        "en": {
            "name": "Rumba Flamenca",
            "category": "General",
            "description": "Vibrant Spanish groove combining percussive body slaps with rapid strums."
        },
        "time_signature": "4/4",
        "default_bpm": 112,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (S)", "↑", "-", "↑", "↓ (T)", "↑"],
        "sounds": ["B", "U", "S", "U", None, "U", "T", "U"]
    },
    "cumbia": {
        "pt": {
            "name": "Cumbia",
            "category": "Geral",
            "description": "Ritmo latino-americano contagiante com grave firme e contratempo abafado."
        },
        "en": {
            "name": "Cumbia",
            "category": "General",
            "description": "Infectious Latin American rhythm with a steady bass pulse and crisp offbeats."
        },
        "time_signature": "4/4",
        "default_bpm": 96,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (S)", "↑", "↓ (B)", "-", "↓ (S)", "↑"],
        "sounds": ["B", None, "S", "U", "B", None, "S", "U"]
    },
    "son_cubano": {
        "pt": {
            "name": "Son Cubano / Salsa",
            "category": "Geral",
            "description": "Baseado na clave afro-cubana, com forte antecipação harmônica antes da cabeça do compasso."
        },
        "en": {
            "name": "Son Cubano / Salsa",
            "category": "General",
            "description": "Built on the Afro-Cuban clave, featuring strong harmonic anticipation."
        },
        "time_signature": "4/4",
        "default_bpm": 106,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "↑", "-", "↑", "↓ (B)", "-"],
        "sounds": ["B", None, "T", "U", None, "U", "B", None]
    },
    "tango": {
        "pt": {
            "name": "Tango",
            "category": "Geral",
            "description": "Ataques secos e dramáticos (marcato) nos 4 tempos com fechamento percussivo."
        },
        "en": {
            "name": "Tango",
            "category": "General",
            "description": "Sharp, dramatic staccato marcato attacks across all four beats."
        },
        "time_signature": "4/4",
        "default_bpm": 116,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "-", "↓ (T)", "-", "↓ (S)", "↑"],
        "sounds": ["B", None, "T", None, "T", None, "S", "U"]
    },
    "rnb_neosoul": {
        "pt": {
            "name": "R&B / Neo-Soul",
            "category": "Geral",
            "description": "Levada relaxada com notas fantasmas abafadas e puxadas suaves nos contratempos."
        },
        "en": {
            "name": "R&B / Neo-Soul",
            "category": "General",
            "description": "Laid-back groove featuring muted ghost strokes and smooth offbeat upstrokes."
        },
        "time_signature": "4/4",
        "default_bpm": 82,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (S)", "↑", "-", "↓ (B)", "↓ (S)", "↑"],
        "sounds": ["B", None, "S", "U", None, "B", "S", "U"]
    },
    "rockabilly_train": {
        "pt": {
            "name": "Rockabilly / Train Beat",
            "category": "Geral",
            "description": "Batida rápida e contínua que imita o balanço de um trem nos trilhos."
        },
        "en": {
            "name": "Rockabilly / Train Beat",
            "category": "General",
            "description": "Fast, driving alternating pattern mimicking the chug of a train on the tracks."
        },
        "time_signature": "4/4",
        "default_bpm": 142,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (S)", "↑", "↓ (B)", "↑", "↓ (S)", "↑"],
        "sounds": ["B", "U", "S", "U", "B", "U", "S", "U"]
    },
    "reggaeton_dembow": {
        "pt": {
            "name": "Reggaeton / Dembow",
            "category": "Geral",
            "description": "Célula rítmica moderna adaptada para violão percussivo com acento sincopado."
        },
        "en": {
            "name": "Reggaeton / Dembow",
            "category": "General",
            "description": "Modern pop/urban rhythmic cell adapted for percussive acoustic guitar."
        },
        "time_signature": "4/4",
        "default_bpm": 95,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "-", "↓ (S)", "↓ (B)", "-", "↓ (S)", "-"],
        "sounds": ["B", None, None, "S", "B", None, "S", None]
    },
    "odd_meter_7_8": {
        "pt": {
            "name": "Compasso Ímpar 7/8",
            "category": "Geral",
            "description": "Agrupamento assimétrico (2 + 2 + 3), excelente desafio avançado de leitura rítmica."
        },
        "en": {
            "name": "Odd Meter 7/8",
            "category": "General",
            "description": "Asymmetric grouping (2 + 2 + 3), an advanced rhythmic independence exercise."
        },
        "time_signature": "7/8",
        "default_bpm": 124,
        "subdivision": 7,
        "count": ["1", "2", "3", "4", "5", "6", "7"],
        "arrows": ["↓ (B)", "↑", "↓ (S)", "↑", "↓ (B)", "↓ (T)", "↑"],
        "sounds": ["B", "U", "S", "U", "B", "T", "U"]
    },

    # ==================== NEW BRAZILIAN RHYTHMS ====================
    "coco": {
        "pt": {
            "name": "Coco",
            "category": "Brasil",
            "description": "Ritmo nordestino de pisada forte e síncope seca, imitando tamancos e ganzá."
        },
        "en": {
            "name": "Coco",
            "category": "Brazil",
            "description": "Northeastern Brazilian rhythm with heavy footsteps and sharp syncopated slaps."
        },
        "time_signature": "2/4",
        "default_bpm": 116,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (S)", "↑", "↓ (B)", "↓ (S)", "↓ (T)", "↑"],
        "sounds": ["B", "U", "S", "U", "B", "S", "T", "U"]
    },
    "milonga": {
        "pt": {
            "name": "Milonga",
            "category": "Brasil",
            "description": "Ritmo platino e gaúcho cadenciado, baseado na célula clássica da habanera."
        },
        "en": {
            "name": "Milonga",
            "category": "Brazil",
            "description": "Cadenced Southern Brazilian and Rioplatense rhythm built on the habanera cell."
        },
        "time_signature": "4/4",
        "default_bpm": 86,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "-", "↓ (T)", "↓ (B)", "-", "↓ (T)", "-"],
        "sounds": ["B", None, None, "T", "B", None, "T", None]
    },
    "cururu_caterete": {
        "pt": {
            "name": "Cururu / Cateretê",
            "category": "Brasil",
            "description": "Ritmo tradicional da viola caipira com alternância rápida de polegar e rasqueado."
        },
        "en": {
            "name": "Cururu / Cateretê",
            "category": "Brazil",
            "description": "Traditional Brazilian viola caipira rhythm with brisk thumb and strum alternation."
        },
        "time_signature": "2/4",
        "default_bpm": 118,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↓ (T)", "↑", "↓ (T)", "↓ (B)", "↓ (T)", "↑", "↓ (T)"],
        "sounds": ["B", "T", "U", "T", "B", "T", "U", "T"]
    },
    "lambada": {
        "pt": {
            "name": "Lambada / Guitarrada",
            "category": "Brasil",
            "description": "Ritmo paraense acelerado e dançante com forte acentuação nos contratempos."
        },
        "en": {
            "name": "Lambada / Guitarrada",
            "category": "Brazil",
            "description": "Fast, danceable rhythm from Pará featuring bright offbeat accents."
        },
        "time_signature": "4/4",
        "default_bpm": 124,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↓ (S)", "↑", "↓ (B)", "↑", "↓ (T)", "↑"],
        "sounds": ["B", "U", "S", "U", "B", "U", "T", "U"]
    },
    "samba_de_roda": {
        "pt": {
            "name": "Samba de Roda",
            "category": "Brasil",
            "description": "Samba tradicional do Recôncavo Baiano com acentuação aberta que lembra as palmas da roda."
        },
        "en": {
            "name": "Samba de Roda",
            "category": "Brazil",
            "description": "Traditional Bahian circle samba with open accents echoing handclaps."
        },
        "time_signature": "2/4",
        "default_bpm": 106,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (T)", "↓ (T)", "↓ (B)", "↑", "↓ (S)", "↑"],
        "sounds": ["B", None, "T", "T", "B", "U", "S", "U"]
    },

    # ==================== TECHNICAL INDEPENDENCE EXERCISES ====================
    "tech_thumb_independence": {
        "pt": {
            "name": "Exercício 1: Independência de Polegar",
            "category": "Técnica",
            "description": "Polegar constante nos 4 tempos (1, 2, 3, 4) enquanto as puxadas respondem nos contratempos."
        },
        "en": {
            "name": "Exercise 1: Thumb Independence",
            "category": "Technique",
            "description": "Steady thumb on all 4 beats while upstrokes answer on syncopated offbeats."
        },
        "time_signature": "4/4",
        "default_bpm": 84,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "-", "↓ (B)", "↑", "↓ (B)", "↑", "↓ (B)", "-"],
        "sounds": ["B", None, "B", "U", "B", "U", "B", None]
    },
    "tech_accent_shift_16th": {
        "pt": {
            "name": "Exercício 2: Deslocamento de Acento (16 avos)",
            "category": "Técnica",
            "description": "Pêndulo contínuo em semicolcheias deslocando o tapa percussivo para fora da cabeça do tempo."
        },
        "en": {
            "name": "Exercise 2: 16th-Note Accent Shift",
            "category": "Technique",
            "description": "Continuous 16th-note pendulum shifting percussive slaps off the main beats."
        },
        "time_signature": "4/4",
        "default_bpm": 78,
        "subdivision": 16,
        "count": ["1", "e", "n", "a", "2", "e", "n", "a", "3", "e", "n", "a", "4", "e", "n", "a"],
        "arrows": ["↓ (B)", "↑", "↓ (T)", "↑", "↓ (T)", "↑", "↓ (S)", "↑", "↓ (T)", "↑", "↓ (T)", "↑", "↓ (T)", "↑", "↓ (T)", "↑ (S)"],
        "sounds": ["B", "U", "T", "U", "T", "U", "S", "U", "T", "U", "T", "U", "T", "U", "T", "S"]
    },
    "tech_tresillo_3_3_2": {
        "pt": {
            "name": "Exercício 3: Polirritmia Cruzada (3 + 3 + 2)",
            "category": "Técnica",
            "description": "Agrupamento assimétrico dentro do 4/4 (clave tresillo), essencial para música brasileira e latina."
        },
        "en": {
            "name": "Exercise 3: Cross-Rhythm Grouping (3 + 3 + 2)",
            "category": "Technique",
            "description": "Asymmetric grouping inside 4/4 (tresillo clave), essential for Brazilian and Latin grooves."
        },
        "time_signature": "4/4",
        "default_bpm": 96,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "↑", "↓ (S)", "↑", "↑", "↓ (T)", "↑"],
        "sounds": ["B", "U", "U", "S", "U", "U", "T", "U"]
    },
    "tech_staccato_mute": {
        "pt": {
            "name": "Exercício 4: Controle de Abafamento Seco",
            "category": "Técnica",
            "description": "Alternância rápida entre acordes abertos e cortes secos para precisão entre as duas mãos."
        },
        "en": {
            "name": "Exercise 4: Crisp Mute & Staccato Control",
            "category": "Technique",
            "description": "Rapid alternation between open chords and dead-note slaps for two-hand synchronization."
        },
        "time_signature": "4/4",
        "default_bpm": 92,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↓ (S)", "↑", "↓ (S)", "↓ (T)", "↓ (S)", "↑", "↓ (S)"],
        "sounds": ["B", "S", "U", "S", "T", "S", "U", "S"]
    },
    "tech_upstroke_syncopation": {
        "pt": {
            "name": "Exercício 5: Puxadas Sincopadas (Contratempo)",
            "category": "Técnica",
            "description": "Treina a resistência e clareza das puxadas para cima (↑) sem apoiar nas descidas."
        },
        "en": {
            "name": "Exercise 5: Syncopated Upstroke Endurance",
            "category": "Technique",
            "description": "Builds upstroke clarity and endurance without relying on downbeat strums."
        },
        "time_signature": "4/4",
        "default_bpm": 88,
        "subdivision": 8,
        "count": ["1", "e", "2", "e", "3", "e", "4", "e"],
        "arrows": ["↓ (B)", "↑", "-", "↑", "-", "↑", "-", "↑"],
        "sounds": ["B", "U", None, "U", None, "U", None, "U"]
    },
}
