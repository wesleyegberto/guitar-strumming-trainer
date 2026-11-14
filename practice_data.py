# practice_data.py

# Guitar string voicings: list of (freq_hz, delay_sec, gain)
# Bass (B) uses root + 5th; Treble (T) & Upstroke (U) use chord tones.
CHORD_VOICINGS = {
    "Em7": {
        "B": [(82.41, 0.000, 0.85), (123.47, 0.014, 0.45), (146.83, 0.026, 0.25)],
        "T": [(146.83, 0.000, 0.45), (196.00, 0.009, 0.65), (246.94, 0.018, 0.75), (329.63, 0.027, 0.80)],
        "U": [(329.63, 0.000, 0.70), (246.94, 0.008, 0.60), (196.00, 0.016, 0.45)],
    },
    "Am7": {
        "B": [(110.00, 0.000, 0.85), (164.81, 0.014, 0.45), (196.00, 0.026, 0.25)],
        "T": [(164.81, 0.000, 0.45), (196.00, 0.009, 0.65), (261.63, 0.018, 0.75), (329.63, 0.027, 0.80)],
        "U": [(329.63, 0.000, 0.70), (261.63, 0.008, 0.60), (196.00, 0.016, 0.45)],
    },
    "C7M": {
        "B": [(130.81, 0.000, 0.85), (164.81, 0.014, 0.45), (196.00, 0.026, 0.25)],
        "T": [(164.81, 0.000, 0.45), (196.00, 0.009, 0.65), (246.94, 0.018, 0.75), (329.63, 0.027, 0.80)],
        "U": [(329.63, 0.000, 0.70), (246.94, 0.008, 0.60), (196.00, 0.016, 0.45)],
    },
    "Dm7": {
        "B": [(146.83, 0.000, 0.85), (220.00, 0.014, 0.45), (261.63, 0.026, 0.25)],
        "T": [(146.83, 0.000, 0.45), (220.00, 0.009, 0.65), (261.63, 0.018, 0.75), (349.23, 0.027, 0.80)],
        "U": [(349.23, 0.000, 0.70), (261.63, 0.008, 0.60), (220.00, 0.016, 0.45)],
    },
    "G7": {
        "B": [(98.00, 0.000, 0.85), (146.83, 0.014, 0.45), (174.61, 0.026, 0.25)],
        "T": [(146.83, 0.000, 0.45), (196.00, 0.009, 0.65), (246.94, 0.018, 0.75), (349.23, 0.027, 0.80)],
        "U": [(349.23, 0.000, 0.70), (246.94, 0.008, 0.60), (196.00, 0.016, 0.45)],
    },
    "G": {
        "B": [(98.00, 0.000, 0.85), (123.47, 0.014, 0.45), (146.83, 0.026, 0.25)],
        "T": [(146.83, 0.000, 0.45), (196.00, 0.009, 0.65), (246.94, 0.018, 0.75), (392.00, 0.027, 0.80)],
        "U": [(392.00, 0.000, 0.70), (246.94, 0.008, 0.60), (196.00, 0.016, 0.45)],
    },
    "D": {
        "B": [(146.83, 0.000, 0.85), (220.00, 0.014, 0.45), (293.66, 0.026, 0.25)],
        "T": [(146.83, 0.000, 0.45), (220.00, 0.009, 0.65), (293.66, 0.018, 0.75), (369.99, 0.027, 0.80)],
        "U": [(369.99, 0.000, 0.70), (293.66, 0.008, 0.60), (220.00, 0.016, 0.45)],
    },
    "C": {
        "B": [(130.81, 0.000, 0.85), (164.81, 0.014, 0.45), (196.00, 0.026, 0.25)],
        "T": [(164.81, 0.000, 0.45), (196.00, 0.009, 0.65), (261.63, 0.018, 0.75), (329.63, 0.027, 0.80)],
        "U": [(329.63, 0.000, 0.70), (261.63, 0.008, 0.60), (196.00, 0.016, 0.45)],
    },
    "A": {
        "B": [(110.00, 0.000, 0.85), (164.81, 0.014, 0.45), (220.00, 0.026, 0.25)],
        "T": [(164.81, 0.000, 0.45), (220.00, 0.009, 0.65), (277.18, 0.018, 0.75), (329.63, 0.027, 0.80)],
        "U": [(329.63, 0.000, 0.70), (277.18, 0.008, 0.60), (220.00, 0.016, 0.45)],
    },
    "E": {
        "B": [(82.41, 0.000, 0.85), (123.47, 0.014, 0.45), (164.81, 0.026, 0.25)],
        "T": [(164.81, 0.000, 0.45), (207.65, 0.009, 0.65), (246.94, 0.018, 0.75), (329.63, 0.027, 0.80)],
        "U": [(329.63, 0.000, 0.70), (246.94, 0.008, 0.60), (207.65, 0.016, 0.45)],
    },
    "A7": {
        "B": [(110.00, 0.000, 0.85), (164.81, 0.014, 0.45), (196.00, 0.026, 0.25)],
        "T": [(164.81, 0.000, 0.45), (196.00, 0.009, 0.65), (277.18, 0.018, 0.75), (329.63, 0.027, 0.80)],
        "U": [(329.63, 0.000, 0.70), (277.18, 0.008, 0.60), (196.00, 0.016, 0.45)],
    },
}

CHORD_PROGRESSIONS = {
    "fixed": {
        "pt": "Acorde Fixo (Am7)",
        "en": "Single Chord (Am7)",
        "chords": ["Am7"]
    },
    "pop_canon": {
        "pt": "Pop / Rock (G → D → Em7 → C)",
        "en": "Pop / Rock (G → D → Em7 → C)",
        "chords": ["G", "D", "Em7", "C"]
    },
    "bossa_251": {
        "pt": "Bossa / MPB (Dm7 → G7 → C7M → A7)",
        "en": "Bossa / MPB (Dm7 → G7 → C7M → A7)",
        "chords": ["Dm7", "G7", "C7M", "A7"]
    },
    "samba_cadence": {
        "pt": "Samba / Pagode (C7M → A7 → Dm7 → G7)",
        "en": "Samba / Pagode (C7M → A7 → Dm7 → G7)",
        "chords": ["C7M", "A7", "Dm7", "G7"]
    },
    "forro_baiao": {
        "pt": "Baião / Forró (A → E → D → E)",
        "en": "Baião / Forró (A → E → D → E)",
        "chords": ["A", "E", "D", "E"]
    },
}

RHYTHM_COACHING = {
    "traditional_samba": {
        "pt": ("Mas Que Nada, Trem das Onze", "Mantenha o pulso solto e acentue o 2º tempo como o surdo de marcação."),
        "en": ("Mas Que Nada, Trem das Onze", "Keep a loose wrist and lean into beat 2 like a surdo bass drum.")
    },
    "bossa_nova": {
        "pt": ("Garota de Ipanema, Chega de Saudade", "Puxe as cordas com os dedos juntos em bloco, sem rasguear com força."),
        "en": ("The Girl from Ipanema, Chega de Saudade", "Pluck the treble strings together cleanly rather than strumming hard.")
    },
    "partido_alto": {
        "pt": ("O Show Tem Que Continuar, Coisinha do Pai", "O tapa (S) deve soar seco: encoste a lateral da mão nas cordas logo após atacar."),
        "en": ("O Show Tem Que Continuar", "Keep the slap (S) crisp by resting the side of your palm on the strings.")
    },
    "pagode": {
        "pt": ("Deixa Acontecer, Telegrama", "Relaxe levemente os dedos da mão esquerda nos tempos abafados para dar swing."),
        "en": ("Deixa Acontecer, Telegrama", "Slightly release left-hand fret pressure on muted beats for authentic swing.")
    },
    "baiao": {
        "pt": ("Asa Branca, Xote das Meninas", "Acentue o grave antecipado antes do tempo 2 para criar o balanço da zabumba."),
        "en": ("Asa Branca, Xote das Meninas", "Accent the anticipated bass note right before beat 2 for the zabumba bounce.")
    },
    "xote": {
        "pt": ("Xote dos Milagres, Esperando na Janela", "Marque os dois graves iniciais com peso igual antes de abrir os agudos."),
        "en": ("Xote dos Milagres, Esperando na Janela", "Play the first two bass strokes with equal weight before opening the treble.")
    },
    "pop_rock_basic": {
        "pt": ("Wonderwall, Tempo Perdido", "Mantenha o antebraço balançando em colcheias constantes mesmo nas pausas ('-')."),
        "en": ("Wonderwall, Stand By Me", "Keep your forearm swinging in steady eighth notes even during rests ('-').")
    },
    "reggae_offbeat": {
        "pt": ("Three Little Birds, Vamos Fugir", "Corte o som imediatamente após cada ataque no contratempo ('e')."),
        "en": ("Three Little Birds, Is This Love", "Mute the strings immediately after each offbeat ('and') stab.")
    },
    "mpb_groove": {
        "pt": ("Flor de Lis, Burguesinha", "Use a ponta dos dedos para um estalo percussivo leve sem perder o groove."),
        "en": ("Flor de Lis, Burguesinha", "Use your fingertips for a light percussive snap while keeping the groove fluid.")
    },
    "rumba_flamenca": {
        "pt": ("Bamboleo, Entre Dos Aguas", "Gire o antebraço como se sacudisse água das mãos nos rasqueados rápidos."),
        "en": ("Bamboleo, Entre Dos Aguas", "Rotate your forearm smoothly on rapid strums and slap cleanly on beat 2.")
    },
}

DEFAULT_COACHING = {
    "pt": ("Repertório Livre / Improviso", "Mantenha o movimento pendular contínuo e relaxe os ombros durante a troca de acordes."),
    "en": ("Free Practice / Jam", "Keep a continuous pendulum motion and relax your shoulders during chord changes.")
}