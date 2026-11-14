# main.py
import tkinter as tk
from tkinter import ttk
import threading
import time
import subprocess
import os
import json
import wave
import math
import struct
import random
import tempfile
import unicodedata
from rhythms_db import RHYTHMS
from practice_data import (
    CHORD_VOICINGS,
    HARMONIC_FIELDS_MAJOR,
    HARMONIC_FIELDS_MINOR,
    PROGRESSION_TEMPLATES,
    GENRE_PROGRESSIONS,
    RHYTHM_COACHING,
    DEFAULT_COACHING,
)

try:
    from AppKit import NSSound
    HAS_NSSOUND = True
except ImportError:
    HAS_NSSOUND = False

HAND_CURSOR = "pointinghand"
PREFS_PATH = os.path.expanduser("~/.rhythm_master_prefs.json")

UI_TEXTS = {
    "en": {
        "window_title": "Rhythm Master — Interactive Music Coach",
        "app_header": "Rhythm Master",
        "app_subtitle": "Interactive Strumming, Rhythm & Ear Coach",
        "sound_guitar": "Guitar",
        "sound_perc": "Percussion",
        "sound_metro": "Metronome",
        "cat_fav": "★",
        "cat_all": "All",
        "cat_brazil": "Brazil",
        "cat_general": "General",
        "cat_tech": "Technique",
        "origin_label": "Origin",
        "sig_label": "Time",
        "prog_label": "HARMONY MODE",
        "type_fixed": "Fixed Chord",
        "type_prog_maj": "Major Progression",
        "type_prog_min": "Minor Progression",
        "type_genre": "Music Genre",
        "bars_per_chord_1": "1 bar / chord",
        "bars_per_chord_2": "2 bars / chord",
        "curr_chord": "NOW",
        "next_chord": "NEXT",
        "songs_prefix": "Songs:",
        "tip_prefix": "Coach Tip:",
        "count_in_banner": "GET READY — COUNT-IN",
        "gap_muted_banner": "INTERNAL CLOCK TEST — MUTED BAR",
        "bar_counter": "Bar",
        "coach_label": "PRACTICE TOOLS",
        "coach_countin": "⏱ Count-in",
        "coach_speed": "📈 Speed +5",
        "coach_gap": "🔇 Gap 2+1",
        "tap_btn": "👆 Tap",
        "legend_items": [
            ("#32D74B", "↓(B) Bass / Thumb"),
            ("#0A84FF", "↓(T) Treble / Fingers"),
            ("#FF9F0A", "↓(S) Slap / Mute"),
            ("#BF5AF2", "↑ Upstroke")
        ],
        "bpm_label": "TEMPO",
        "btn_play": "▶   Play Rhythm",
        "btn_stop": "⏹   Stop",
        "shortcut_hint": "Spacebar: Play/Stop  •  T: Tap Tempo",
        "tooltips": {
            "sound_guitar": "Synthesized acoustic guitar using Karplus-Strong string modeling.",
            "sound_perc": "Percussive bass, snare, and slap sounds for rhythmic clarity.",
            "sound_metro": "Pure click track marking the downbeat and main pulses.",
            "fav_star": "Save or remove this rhythm from your Favorites list.",
            "harmony_type": "Select harmony type: Fixed Chord, Major/Minor Progressions, or Genre.",
            "harmony_val1": "Select specific chord, tonic key, or music genre.",
            "harmony_val2": "Select structural progression format (e.g. I-V-vi-IV).",
            "bars_per_chord": "Switch between 1 bar per chord or 2 bars per chord.",
            "count_in": "Plays a 1-bar click count-in before starting so you can get ready.",
            "speed_trainer": "Automatically increases tempo by +5 BPM every 4 bars.",
            "gap_click": "Plays 2 bars with sound and mutes 1 bar to test your internal timing.",
            "tap_btn": "Click repeatedly (or press 'T') to detect the BPM of a song.",
            "play_btn": "Start or stop playback (Shortcut: Spacebar)."
        }
    },
    "pt": {
        "window_title": "Mestre dos Ritmos — Professor Interativo",
        "app_header": "Mestre dos Ritmos",
        "app_subtitle": "Professor Interativo de Batidas, Harmonia e Tempo",
        "sound_guitar": "Violão",
        "sound_perc": "Percussão",
        "sound_metro": "Metrônomo",
        "cat_fav": "★",
        "cat_all": "Todos",
        "cat_brazil": "Brasil",
        "cat_general": "Geral",
        "cat_tech": "Técnica",
        "origin_label": "Origem",
        "sig_label": "Compasso",
        "prog_label": "MODO DE HARMONIA",
        "type_fixed": "Acorde Fixo",
        "type_prog_maj": "Progressão Maior",
        "type_prog_min": "Progressão Menor",
        "type_genre": "Gênero Musical",
        "bars_per_chord_1": "1 comp. / acorde",
        "bars_per_chord_2": "2 comp. / acorde",
        "curr_chord": "AGORA",
        "next_chord": "PRÓXIMO",
        "songs_prefix": "Músicas:",
        "tip_prefix": "Dica do Professor:",
        "count_in_banner": "PREPARE-SE — CONTAGEM DE ENTRADA",
        "gap_muted_banner": "RELÓGIO INTERNO — COMPASSO MUDO",
        "bar_counter": "Compasso",
        "coach_label": "MODO DE ESTUDO",
        "coach_countin": "⏱ Count-in",
        "coach_speed": "📈 Acelerar +5",
        "coach_gap": "🔇 Mudo 2+1",
        "tap_btn": "👆 Tap",
        "legend_items": [
            ("#32D74B", "↓(B) Grave / Polegar"),
            ("#0A84FF", "↓(T) Agudo / Mão"),
            ("#FF9F0A", "↓(S) Tapa / Abafado"),
            ("#BF5AF2", "↑ Puxada")
        ],
        "bpm_label": "ANDAMENTO",
        "btn_play": "▶   Tocar Ritmo",
        "btn_stop": "⏹   Parar",
        "shortcut_hint": "Espaço: Tocar/Parar  •  T: Tap Tempo",
        "tooltips": {
            "sound_guitar": "Violão acústico sintetizado em tempo real (modelagem física de cordas).",
            "sound_perc": "Sons de bumbo, caixa e tapa para treinar a precisão rítmica.",
            "sound_metro": "Cliques puros de metrônomo marcando a cabeça do compasso e os tempos.",
            "fav_star": "Salva ou remove este ritmo da sua lista de Favoritos.",
            "harmony_type": "Selecione o tipo de harmonia: Acorde Fixo, Progressões ou Gênero.",
            "harmony_val1": "Selecione o acorde, a tônica do campo harmônico ou o gênero.",
            "harmony_val2": "Selecione o formato estrutural da progressão (ex: I-V-vi-IV).",
            "bars_per_chord": "Alterna entre 1 ou 2 compassos por acorde.",
            "count_in": "Toca 1 compasso de contagem preparatória antes de iniciar a batida.",
            "speed_trainer": "Aumenta o andamento automaticamente em +5 BPM a cada 4 compassos.",
            "gap_click": "Toca 2 compassos com áudio e silencia 1 compasso para testar seu relógio interno.",
            "tap_btn": "Clique no ritmo da música (ou aperte 'T') para descobrir o BPM automaticamente.",
            "play_btn": "Inicia ou para a execução (Atalho: Barra de Espaço)."
        }
    }
}

COLORS = {
    "bg_main": "#141416",
    "bg_sidebar": "#1C1C1F",
    "bg_card": "#232327",
    "bg_subpanel": "#1D1D21",
    "bg_step": "#2C2C32",
    "bg_step_active": "#0A84FF",
    "border_subtle": "#33333A",
    "text_primary": "#F5F5F7",
    "text_secondary": "#98989F",
    "accent_blue": "#0A84FF",
    "accent_green": "#30D158",
    "accent_red": "#FF453A",
    "accent_orange": "#FF9F0A",
    "accent_purple": "#BF5AF2",
    "accent_gold": "#FFD60A",
}


def draw_rounded_rect(canvas, x1, y1, x2, y2, radius=14, **kwargs):
    radius = min(radius, (x2 - x1) / 2, (y2 - y1) / 2)
    points = [
        x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1,
        x2, y1, x2, y1 + radius, x2, y1 + radius, x2, y2 - radius,
        x2, y2 - radius, x2, y2, x2 - radius, y2, x2 - radius, y2,
        x1 + radius, y2, x1 + radius, y2, x1, y2, x1, y2 - radius,
        x1, y2 - radius, x1, y1 + radius, x1, y1 + radius, x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)


class RoundedButton(tk.Canvas):
    def __init__(self, parent, text="", command=None, bg_color="#0A84FF", hover_color="#409CFF",
                 fg_color="#FFFFFF", font=("Helvetica Neue", 13, "bold"), radius=12, height=44, **kwargs):
        super().__init__(parent, height=height, bg=parent["bg"], highlightthickness=0, cursor=HAND_CURSOR, **kwargs)
        self.command = command
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.fg_color = fg_color
        self.font = font
        self.radius = radius
        self.text_str = text
        self.current_bg = bg_color

        self.bind("<Configure>", self._redraw)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_click)

    def _redraw(self, event=None):
        self.delete("all")
        w = self.winfo_width()
        h = self.winfo_height()
        if w < 10 or h < 10:
            return
        draw_rounded_rect(self, 2, 2, w - 2, h - 2, radius=self.radius, fill=self.current_bg, outline="")
        self.create_text(w / 2, h / 2, text=self.text_str, fill=self.fg_color, font=self.font)

    def _on_enter(self, event):
        self.current_bg = self.hover_color
        self._redraw()

    def _on_leave(self, event):
        self.current_bg = self.bg_color
        self._redraw()

    def _on_click(self, event):
        if self.command:
            self.command()

    def configure_style(self, text=None, bg_color=None, hover_color=None, fg_color=None):
        if text is not None:
            self.text_str = text
        if bg_color is not None:
            self.bg_color = bg_color
            self.current_bg = bg_color
        if hover_color is not None:
            self.hover_color = hover_color
        if fg_color is not None:
            self.fg_color = fg_color
        self._redraw()


class ToolTip:
    def __init__(self, widget, text_func, delay=450):
        self.widget = widget
        self.text_func = text_func
        self.delay = delay
        self.tip_window = None
        self.after_id = None

        self.widget.bind("<Enter>", self._schedule, add="+")
        self.widget.bind("<Leave>", self._hide, add="+")
        self.widget.bind("<ButtonPress>", self._hide, add="+")

    def _schedule(self, event=None):
        self._cancel()
        self.after_id = self.widget.after(self.delay, self._show)

    def _cancel(self):
        if self.after_id:
            self.widget.after_cancel(self.after_id)
            self.after_id = None

    def _show(self):
        if self.tip_window:
            return
        text = self.text_func() if callable(self.text_func) else self.text_func
        if not text:
            return

        x = self.widget.winfo_rootx() + 10
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 6

        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        try:
            tw.tk.call("::tk::unsupported::MacWindowStyle", "style", tw._w, "help", "noActivates")
        except tk.TclError:
            pass
        tw.wm_geometry(f"+{x}+{y}")

        frame = tk.Frame(tw, bg="#2C2C34", bd=1, relief="solid", highlightbackground="#484852", highlightthickness=1)
        frame.pack()

        lbl = tk.Label(
            frame, text=text, justify="left", wraplength=260,
            bg="#2C2C34", fg="#F5F5F7", padx=10, pady=6,
            font=("Helvetica Neue", 11)
        )
        lbl.pack()

    def _hide(self, event=None):
        self._cancel()
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None


class StepCard(tk.Canvas):
    def __init__(self, parent, count_text, arrow_text, sound_type, **kwargs):
        super().__init__(parent, width=10, height=126, bg=COLORS["bg_card"], highlightthickness=0, **kwargs)
        self.count_text = count_text
        self.arrow_text = arrow_text
        self.sound_type = sound_type
        self.is_active = False

        type_colors = {
            "B": COLORS["accent_green"],
            "T": COLORS["accent_blue"],
            "S": COLORS["accent_orange"],
            "U": COLORS["accent_purple"],
            None: "#3A3A40"
        }
        self.indicator_color = type_colors.get(sound_type, "#3A3A40")
        self.bind("<Configure>", self._redraw)

    def set_active(self, active):
        if self.is_active != active:
            self.is_active = active
            self._redraw()

    def _redraw(self, event=None):
        self.delete("all")
        w = self.winfo_width()
        h = self.winfo_height()
        if w < 8 or h < 10:
            return

        bg = COLORS["bg_step_active"] if self.is_active else COLORS["bg_step"]
        outline = "#5AC8FA" if self.is_active else COLORS["border_subtle"]
        count_fg = "#FFFFFF" if self.is_active else COLORS["text_secondary"]
        arrow_fg = "#FFFFFF" if self.is_active else (COLORS["text_primary"] if self.arrow_text != "-" else "#55555E")

        text_len = len(self.arrow_text)
        if w < 48:
            arrow_font_size = 11 if text_len > 2 else 14
            count_font_size = 9
            radius = 8
        elif w < 68:
            arrow_font_size = 13 if text_len > 2 else 16
            count_font_size = 10
            radius = 11
        else:
            arrow_font_size = 16 if text_len > 2 else 19
            count_font_size = 11
            radius = 14

        draw_rounded_rect(self, 1, 2, w - 1, h - 2, radius=radius, fill=bg, outline=outline, width=1.5)

        pill_w = max(12, min(28, w * 0.48))
        pill_color = "#FFFFFF" if self.is_active else self.indicator_color
        draw_rounded_rect(self, (w - pill_w) / 2, 12, (w + pill_w) / 2, 17, radius=3, fill=pill_color, outline="")

        self.create_text(
            w / 2, 36, text=self.count_text, fill=count_fg,
            font=("Helvetica Neue", count_font_size, "bold")
        )

        display_arrow = self.arrow_text
        if w < 58 and " (" in display_arrow:
            display_arrow = display_arrow.replace(" (", "\n(")
        elif w < 54 and "(" in display_arrow and not display_arrow.startswith("("):
            display_arrow = display_arrow.replace("(", "\n(")

        self.create_text(
            w / 2, 80, text=display_arrow, fill=arrow_fg, justify="center",
            font=("Helvetica Neue", arrow_font_size, "bold")
        )


class MacNativeAudioEngine:
    def __init__(self, pool_size=4):
        self.temp_dir = tempfile.gettempdir()
        self.mode = "guitar"
        self.current_chord = "Am7"
        self.pool_size = pool_size

        self.files = {
            "guitar": {},
            "percussion": {
                "B": os.path.join(self.temp_dir, "perc_bass.wav"),
                "T": os.path.join(self.temp_dir, "perc_treble.wav"),
                "U": os.path.join(self.temp_dir, "perc_upstroke.wav"),
                "S": os.path.join(self.temp_dir, "perc_slap.wav"),
            },
            "metronome": {
                "M_ACCENT": os.path.join(self.temp_dir, "metro_accent.wav"),
                "M_BEAT": os.path.join(self.temp_dir, "metro_beat.wav"),
            }
        }
        self._generate_guitar_samples()
        self._generate_percussion_samples()
        self._generate_metronome_samples()

        self.sound_pools = {"guitar": {}, "percussion": {}, "metronome": {}}
        self.pool_indices = {"guitar": {}, "percussion": {}, "metronome": {}}

        if HAS_NSSOUND:
            for mode_name, paths in self.files.items():
                for key, path in paths.items():
                    voices = []
                    for _ in range(pool_size):
                        snd = NSSound.alloc().initWithContentsOfFile_byReference_(path, False)
                        if snd:
                            voices.append(snd)
                    self.sound_pools[mode_name][key] = voices
                    self.pool_indices[mode_name][key] = 0

    def _write_wav(self, path, samples, sample_rate=44100):
        with wave.open(path, "w") as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            data = b"".join(struct.pack("<h", max(-32767, min(32767, int(s * 32767)))) for s in samples)
            wav_file.writeframes(data)

    def _karplus_strong_string(self, freq, duration, sr=44100, decay=0.996, brightness=0.5, gain=1.0):
        period = max(2, int(round(sr / freq)))
        num_samples = int(sr * duration)

        raw = [random.uniform(-1.0, 1.0) for _ in range(period)]
        mean_val = sum(raw) / period
        ring = [x - mean_val for x in raw]

        passes = 1 if brightness >= 0.5 else (3 if brightness >= 0.35 else 6)
        for _ in range(passes):
            smoothed = [0.0] * period
            for i in range(period):
                prev_s = ring[(i - 1) % period]
                curr_s = ring[i]
                next_s = ring[(i + 1) % period]
                smoothed[i] = 0.25 * prev_s + 0.50 * curr_s + 0.25 * next_s
            ring = smoothed

        max_init = max((abs(x) for x in ring), default=1.0)
        if max_init > 0:
            ring = [x / max_init for x in ring]

        out = [0.0] * num_samples
        idx = 0
        attack_samples = int(sr * 0.004)

        for i in range(num_samples):
            curr = ring[idx]
            nxt = ring[(idx + 1) % period]
            ring[idx] = decay * 0.5 * (curr + nxt)

            if i < attack_samples:
                env = i / attack_samples
            elif i > num_samples - 600:
                env = (num_samples - i) / 600.0
            else:
                env = 1.0

            out[i] = curr * gain * env
            idx = (idx + 1) % period

        return out

    def _mix_strum(self, notes_with_delays, total_duration, sr=44100, decay=0.9955, brightness=0.45, target_peak=0.72):
        total_len = int(sr * total_duration)
        mix = [0.0] * total_len
        for freq, delay_sec, gain in notes_with_delays:
            start_idx = int(delay_sec * sr)
            note_dur = max(0.05, total_duration - delay_sec)
            string_samples = self._karplus_strong_string(
                freq, note_dur, sr, decay=decay, brightness=brightness, gain=gain
            )
            for j, val in enumerate(string_samples):
                if start_idx + j < total_len:
                    mix[start_idx + j] += val

        peak = max((abs(x) for x in mix), default=1.0)
        if peak > 0:
            scale = target_peak / peak
            mix = [math.tanh(x * scale * 1.15) * target_peak for x in mix]
        return mix

    def _generate_guitar_samples(self):
        sr = 44100
        slap_path = os.path.join(self.temp_dir, "gtr_slap_shared.wav")
        muted_notes = [
            (110.00, 0.000, 0.50), (196.00, 0.005, 0.65),
            (246.94, 0.010, 0.70), (329.63, 0.015, 0.65),
        ]
        samples_s = self._mix_strum(muted_notes, total_duration=0.11, sr=sr, decay=0.935, brightness=0.60, target_peak=0.60)
        for i in range(len(samples_s)):
            t = i / sr
            body_thump = 0.25 * math.exp(-t * 55) * math.sin(2 * math.pi * 120 * t)
            samples_s[i] = max(-0.85, min(0.85, samples_s[i] + body_thump))
        self._write_wav(slap_path, samples_s, sr)

        for chord_name, voicing in CHORD_VOICINGS.items():
            path_b = os.path.join(self.temp_dir, f"gtr_{chord_name}_B.wav")
            samples_b = self._mix_strum(voicing["B"], total_duration=0.44, sr=sr, decay=0.9965, brightness=0.25, target_peak=0.70)
            self._write_wav(path_b, samples_b, sr)

            path_t = os.path.join(self.temp_dir, f"gtr_{chord_name}_T.wav")
            samples_t = self._mix_strum(voicing["T"], total_duration=0.36, sr=sr, decay=0.995, brightness=0.55, target_peak=0.72)
            self._write_wav(path_t, samples_t, sr)

            path_u = os.path.join(self.temp_dir, f"gtr_{chord_name}_U.wav")
            samples_u = self._mix_strum(voicing["U"], total_duration=0.26, sr=sr, decay=0.9935, brightness=0.50, target_peak=0.65)
            self._write_wav(path_u, samples_u, sr)

            self.files["guitar"][(chord_name, "B")] = path_b
            self.files["guitar"][(chord_name, "T")] = path_t
            self.files["guitar"][(chord_name, "U")] = path_u
            self.files["guitar"][(chord_name, "S")] = slap_path

    def _generate_percussion_samples(self):
        sr = 44100
        dur_b = 0.14
        samples_b = [
            0.85 * math.exp(-(i / sr) * 22) * math.sin(2 * math.pi * (140 * math.exp(-(i / sr) * 18) + 45) * (i / sr))
            for i in range(int(sr * dur_b))
        ]
        self._write_wav(self.files["percussion"]["B"], samples_b, sr)

        dur_t = 0.11
        samples_t = [
            math.exp(-(i / sr) * 32) * (0.4 * math.sin(2 * math.pi * 240 * (i / sr)) + 0.5 * random.uniform(-1, 1))
            for i in range(int(sr * dur_t))
        ]
        self._write_wav(self.files["percussion"]["T"], samples_t, sr)

        dur_u = 0.05
        samples_u = [0.45 * math.exp(-(i / sr) * 75) * random.uniform(-1, 1) for i in range(int(sr * dur_u))]
        self._write_wav(self.files["percussion"]["U"], samples_u, sr)

        dur_s = 0.08
        samples_s = [
            0.75 * math.exp(-(i / sr) * 50) * (0.6 * math.sin(2 * math.pi * 520 * (i / sr)) + 0.4 * random.uniform(-1, 1))
            for i in range(int(sr * dur_s))
        ]
        self._write_wav(self.files["percussion"]["S"], samples_s, sr)

    def _generate_metronome_samples(self):
        sr = 44100
        dur = 0.055

        samples_acc = []
        for i in range(int(sr * dur)):
            t = i / sr
            env = math.exp(-t * 75)
            wave_val = 0.70 * math.sin(2 * math.pi * 1320 * t) + 0.30 * math.sin(2 * math.pi * 2640 * t)
            samples_acc.append(0.82 * env * wave_val)
        self._write_wav(self.files["metronome"]["M_ACCENT"], samples_acc, sr)

        samples_beat = []
        for i in range(int(sr * dur)):
            t = i / sr
            env = math.exp(-t * 80)
            wave_val = 0.75 * math.sin(2 * math.pi * 880 * t) + 0.25 * math.sin(2 * math.pi * 1760 * t)
            samples_beat.append(0.68 * env * wave_val)
        self._write_wav(self.files["metronome"]["M_BEAT"], samples_beat, sr)

    def set_mode(self, mode):
        if mode in self.files:
            self.mode = mode

    def set_chord(self, chord_name):
        if chord_name in CHORD_VOICINGS:
            self.current_chord = chord_name

    def play_metronome_click(self, accent=False):
        key = "M_ACCENT" if accent else "M_BEAT"
        self._play_key("metronome", key)

    def play(self, sound_type):
        mode = self.mode
        key = (self.current_chord, sound_type) if mode == "guitar" else sound_type
        self._play_key(mode, key)

    def _play_key(self, mode, key):
        if key not in self.files[mode]:
            return
        if HAS_NSSOUND and key in self.sound_pools[mode] and self.sound_pools[mode][key]:
            idx = self.pool_indices[mode][key]
            snd = self.sound_pools[mode][key][idx]
            self.pool_indices[mode][key] = (idx + 1) % len(self.sound_pools[mode][key])
            snd.stop()
            snd.setCurrentTime_(0.0)
            snd.play()
        else:
            subprocess.Popen(["afplay", self.files[mode][key]], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


class RhythmMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1240x780")
        self.root.minsize(1060, 700)
        self.root.configure(bg=COLORS["bg_main"])

        self.prefs = self._load_prefs()
        self.favorites = set(self.prefs.get("favorites", []))

        self.language = tk.StringVar(value=self.prefs.get("language", "pt"))
        self.sound_mode = tk.StringVar(value="guitar")
        self.category_filter = tk.StringVar(value="all")
        self.search_query = tk.StringVar(value="")
        self.current_rhythm_id = "traditional_samba"
        self.visible_keys = []

        # Harmony States
        self.count_in_enabled = tk.BooleanVar(value=True)
        self.speed_trainer_enabled = tk.BooleanVar(value=False)
        self.gap_click_enabled = tk.BooleanVar(value=False)
        self.bars_per_chord = tk.IntVar(value=1)

        self.harmony_type = tk.StringVar(value="fixed")  # "fixed", "prog_maj", "prog_min", "genre"
        self.harmony_val1 = tk.StringVar(value="Am7")   # Acorde fixo, Tônica Maior/Menor ou Gênero
        self.harmony_val2 = tk.StringVar(value="major_axis") # Formato da progressão

        self.tap_timestamps = []

        self.audio = MacNativeAudioEngine()
        self.is_playing = False
        self.play_session_id = 0
        self.rhythm_thread = None
        self.bpm = tk.IntVar(value=96)
        self.step_cards = []
        self.cat_buttons = {}
        self.lang_buttons = {}
        self.sound_buttons = {}
        self.coach_buttons = {}

        self._build_ui()
        self._apply_language()

        self.root.bind("<space>", self._on_spacebar)
        self.root.bind("<KeyPress-t>", self._on_tap_key)
        self.root.bind("<KeyPress-T>", self._on_tap_key)

    def _load_prefs(self):
        if os.path.exists(PREFS_PATH):
            try:
                with open(PREFS_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def _save_prefs(self):
        try:
            with open(PREFS_PATH, "w", encoding="utf-8") as f:
                json.dump({
                    "favorites": sorted(self.favorites),
                    "language": self.language.get()
                }, f, indent=2)
        except Exception:
            pass

    def _tr(self, key):
        return UI_TEXTS[self.language.get()][key]

    def _on_spacebar(self, event):
        if self.root.focus_get() != self.search_entry:
            self._toggle_playback()

    def _on_tap_key(self, event):
        if self.root.focus_get() != self.search_entry:
            self._handle_tap_tempo()

    def _get_active_chord_list(self):
        htype = self.harmony_type.get()
        v1 = self.harmony_val1.get()
        v2 = self.harmony_val2.get()

        if htype == "fixed":
            return [v1 if v1 in CHORD_VOICINGS else "Am7"]
        elif htype == "prog_maj":
            field = HARMONIC_FIELDS_MAJOR.get(v1, HARMONIC_FIELDS_MAJOR["C"])
            template = PROGRESSION_TEMPLATES.get(v2, PROGRESSION_TEMPLATES["major_axis"])
            return [field[d] for d in template["degrees"]]
        elif htype == "prog_min":
            field = HARMONIC_FIELDS_MINOR.get(v1, HARMONIC_FIELDS_MINOR["Am"])
            template = PROGRESSION_TEMPLATES.get(v2, PROGRESSION_TEMPLATES["minor_standard"])
            return [field[d] for d in template["degrees"]]
        elif htype == "genre":
            genre_data = GENRE_PROGRESSIONS.get(v1, GENRE_PROGRESSIONS["pop"])
            return genre_data["chords"]
        return ["Am7"]

    def _build_ui(self):
        # ==================== HEADER ====================
        header = tk.Frame(self.root, bg=COLORS["bg_main"], padx=28, pady=16)
        header.pack(fill="x")

        title_box = tk.Frame(header, bg=COLORS["bg_main"])
        title_box.pack(side="left")

        self.lbl_header = tk.Label(
            title_box, text="", bg=COLORS["bg_main"], fg=COLORS["text_primary"],
            font=("Helvetica Neue", 24, "bold")
        )
        self.lbl_header.pack(anchor="w")

        self.lbl_subtitle = tk.Label(
            title_box, text="", bg=COLORS["bg_main"], fg=COLORS["text_secondary"],
            font=("Helvetica Neue", 12)
        )
        self.lbl_subtitle.pack(anchor="w", pady=(2, 0))

        right_controls = tk.Frame(header, bg=COLORS["bg_main"])
        right_controls.pack(side="right", anchor="center")

        sound_container = tk.Frame(right_controls, bg=COLORS["bg_sidebar"], padx=4, pady=4)
        sound_container.pack(side="left", padx=(0, 14))

        for mode_code in ["guitar", "percussion", "metronome"]:
            btn = tk.Label(
                sound_container, text="", padx=13, pady=6, cursor=HAND_CURSOR,
                font=("Helvetica Neue", 11, "bold")
            )
            btn.pack(side="left", padx=2)
            btn.bind("<Button-1>", lambda e, m=mode_code: self._set_sound_mode(m))
            self.sound_buttons[mode_code] = btn

        lang_container = tk.Frame(right_controls, bg=COLORS["bg_sidebar"], padx=4, pady=4)
        lang_container.pack(side="left")

        for code, label in [("en", "EN"), ("pt", "PT")]:
            btn = tk.Label(
                lang_container, text=label, padx=14, pady=6, cursor=HAND_CURSOR,
                font=("Helvetica Neue", 11, "bold")
            )
            btn.pack(side="left", padx=2)
            btn.bind("<Button-1>", lambda e, c=code: self._set_language(c))
            self.lang_buttons[code] = btn

        # ==================== MAIN BODY ====================
        main_area = tk.Frame(self.root, bg=COLORS["bg_main"], padx=28, pady=4)
        main_area.pack(fill="both", expand=True)

        # Left Sidebar
        sidebar_canvas = tk.Canvas(main_area, width=310, bg=COLORS["bg_main"], highlightthickness=0)
        sidebar_canvas.pack(side="left", fill="y", padx=(0, 22), pady=(0, 22))
        sidebar_canvas.pack_propagate(False)

        sidebar_inner = tk.Frame(sidebar_canvas, bg=COLORS["bg_sidebar"], padx=14, pady=14)
        sidebar_win = sidebar_canvas.create_window((0, 0), window=sidebar_inner, anchor="nw")
        sidebar_canvas.bind(
            "<Configure>",
            lambda e: (
                self._redraw_panel(sidebar_canvas, COLORS["bg_sidebar"], COLORS["border_subtle"]),
                sidebar_canvas.itemconfigure(sidebar_win, width=e.width, height=e.height)
            )
        )

        search_box = tk.Canvas(sidebar_inner, height=38, bg=COLORS["bg_sidebar"], highlightthickness=0)
        search_box.pack(fill="x", pady=(0, 10))

        self.search_entry = tk.Entry(
            search_box, textvariable=self.search_query, bg=COLORS["bg_step"],
            fg=COLORS["text_primary"], insertbackground="#FFFFFF",
            font=("Helvetica Neue", 12), relief="flat", highlightthickness=0
        )
        search_win = search_box.create_window((12, 19), window=self.search_entry, anchor="w")
        search_box.bind(
            "<Configure>",
            lambda e: (
                self._redraw_panel(search_box, COLORS["bg_step"], COLORS["border_subtle"], radius=10),
                search_box.itemconfigure(search_win, width=max(50, e.width - 24))
            )
        )
        self.search_query.trace_add("write", lambda *args: self._update_rhythm_list())

        cat_bar = tk.Frame(sidebar_inner, bg=COLORS["bg_step"], padx=3, pady=3)
        cat_bar.pack(fill="x", pady=(0, 10))

        for cat_key in ["fav", "all", "brazil", "general", "tech"]:
            lbl = tk.Label(
                cat_bar, text="", pady=6, cursor=HAND_CURSOR,
                font=("Helvetica Neue", 10, "bold")
            )
            lbl.pack(side="left", expand=True, fill="x", padx=1)
            lbl.bind("<Button-1>", lambda e, ck=cat_key: self._set_category(ck))
            self.cat_buttons[cat_key] = lbl

        list_frame = tk.Frame(sidebar_inner, bg=COLORS["bg_sidebar"])
        list_frame.pack(fill="both", expand=True)

        self.listbox = tk.Listbox(
            list_frame, bg=COLORS["bg_sidebar"], fg=COLORS["text_primary"],
            selectbackground=COLORS["accent_blue"], selectforeground="#FFFFFF",
            activestyle="none", font=("Helvetica Neue", 13), cursor=HAND_CURSOR,
            borderwidth=0, highlightthickness=0, selectmode="single"
        )
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<<ListboxSelect>>", self._on_rhythm_select)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # ==================== RIGHT STAGE ====================
        stage_canvas = tk.Canvas(main_area, width=10, bg=COLORS["bg_main"], highlightthickness=0)
        stage_canvas.pack(side="right", fill="both", expand=True, pady=(0, 22))

        stage_inner = tk.Frame(stage_canvas, bg=COLORS["bg_card"], padx=26, pady=20)
        stage_win = stage_canvas.create_window((0, 0), window=stage_inner, anchor="nw")
        stage_canvas.bind(
            "<Configure>",
            lambda e: (
                self._redraw_panel(stage_canvas, COLORS["bg_card"], COLORS["border_subtle"]),
                stage_canvas.itemconfigure(stage_win, width=e.width, height=e.height),
                self.lbl_description.config(wraplength=max(320, e.width - 60)),
                self.lbl_songs_line.config(wraplength=max(320, e.width - 80)),
                self.lbl_tip_line.config(wraplength=max(320, e.width - 80))
            )
        )

        # 1. Rhythm Header: Star + Title + Status Badges
        top_info = tk.Frame(stage_inner, bg=COLORS["bg_card"])
        top_info.pack(fill="x")

        self.btn_fav = tk.Label(
            top_info, text="☆", bg=COLORS["bg_card"], fg=COLORS["accent_gold"],
            font=("Helvetica Neue", 23), cursor=HAND_CURSOR
        )
        self.btn_fav.pack(side="left", padx=(0, 8))
        self.btn_fav.bind("<Button-1>", lambda e: self._toggle_favorite())

        self.lbl_rhythm_title = tk.Label(
            top_info, text="", bg=COLORS["bg_card"], fg=COLORS["text_primary"],
            font=("Helvetica Neue", 20, "bold"), anchor="w"
        )
        self.lbl_rhythm_title.pack(side="left")

        badges_frame = tk.Frame(top_info, bg=COLORS["bg_card"])
        badges_frame.pack(side="right")

        self.lbl_bar_counter = tk.Label(
            badges_frame, text="", bg="#2C2C35", fg=COLORS["accent_green"],
            font=("Helvetica Neue", 11, "bold"), padx=10, pady=5
        )
        self.lbl_bar_counter.pack(side="left", padx=(0, 8))

        self.badge_origin = tk.Label(
            badges_frame, text="", bg="#1D3557", fg="#64D2FF",
            font=("Helvetica Neue", 11, "bold"), padx=10, pady=5
        )
        self.badge_origin.pack(side="left", padx=(0, 8))

        self.badge_sig = tk.Label(
            badges_frame, text="", bg="#2C2C35", fg=COLORS["accent_gold"],
            font=("Helvetica Neue", 11, "bold"), padx=10, pady=5
        )
        self.badge_sig.pack(side="left")

        # 2. Description & Dedicated Coaching Box
        self.lbl_description = tk.Label(
            stage_inner, text="", bg=COLORS["bg_card"], fg=COLORS["text_secondary"],
            font=("Helvetica Neue", 12), wraplength=680, justify="left", anchor="w"
        )
        self.lbl_description.pack(fill="x", pady=(6, 8))

        coaching_card = tk.Frame(stage_inner, bg=COLORS["bg_subpanel"], padx=14, pady=8)
        coaching_card.pack(fill="x", pady=(0, 12))

        self.lbl_songs_line = tk.Label(
            coaching_card, text="", bg=COLORS["bg_subpanel"], fg="#D1D1D6",
            font=("Helvetica Neue", 11, "bold"), wraplength=660, justify="left", anchor="w"
        )
        self.lbl_songs_line.pack(fill="x", pady=(0, 3))

        self.lbl_tip_line = tk.Label(
            coaching_card, text="", bg=COLORS["bg_subpanel"], fg="#98989F",
            font=("Helvetica Neue", 11, "italic"), wraplength=660, justify="left", anchor="w"
        )
        self.lbl_tip_line.pack(fill="x")

        # 3. Harmony Selector Bar (Type + Sub-selectors + High-contrast Text)
        harmony_bar = tk.Frame(stage_inner, bg=COLORS["bg_subpanel"], padx=14, pady=10)
        harmony_bar.pack(fill="x", pady=(0, 10))

        left_prog = tk.Frame(harmony_bar, bg=COLORS["bg_subpanel"])
        left_prog.pack(side="left", fill="y")

        self.lbl_prog_title = tk.Label(
            left_prog, text="", bg=COLORS["bg_subpanel"], fg=COLORS["text_secondary"],
            font=("Helvetica Neue", 9, "bold"), anchor="w"
        )
        self.lbl_prog_title.pack(anchor="w", pady=(0, 5))

        prog_controls_row = tk.Frame(left_prog, bg=COLORS["bg_subpanel"])
        prog_controls_row.pack(anchor="w")

        # Estilo visual de OptionMenu com texto PRETO e fundo claro para legibilidade total
        menu_config = {
            "bg": "#E4E4E6", "fg": "#000000",
            "activebackground": COLORS["accent_blue"], "activeforeground": "#FFFFFF",
            "font": ("Helvetica Neue", 10, "bold"), "highlightthickness": 0, "bd": 0,
            "padx": 8, "pady": 4, "cursor": HAND_CURSOR
        }
        menu_dropdown_config = {
            "bg": "#FFFFFF", "fg": "#000000",
            "activebackground": COLORS["accent_blue"], "activeforeground": "#FFFFFF",
            "font": ("Helvetica Neue", 11)
        }

        # Menu 1: Tipo de Harmonia (Fixo, Prog Maior, Prog Menor, Gênero)
        self.harmony_type_display = tk.StringVar(value="")
        self.menu_harmony_type = tk.OptionMenu(prog_controls_row, self.harmony_type_display, "", command=self._on_harmony_type_change)
        self.menu_harmony_type.config(**menu_config)
        self.menu_harmony_type["menu"].config(**menu_dropdown_config)
        self.menu_harmony_type.pack(side="left", padx=(0, 6))

        # Menu 2: Valor 1 (Acorde, Tônica ou Gênero)
        self.harmony_val1_display = tk.StringVar(value="")
        self.menu_harmony_val1 = tk.OptionMenu(prog_controls_row, self.harmony_val1_display, "", command=self._on_harmony_val1_change)
        self.menu_harmony_val1.config(**menu_config)
        self.menu_harmony_val1["menu"].config(**menu_dropdown_config)
        self.menu_harmony_val1.pack(side="left", padx=(0, 6))

        # Menu 3: Valor 2 (Formato da Progressão ex: I-V-vi-IV) - Visível apenas para Progressões
        self.harmony_val2_display = tk.StringVar(value="")
        self.menu_harmony_val2 = tk.OptionMenu(prog_controls_row, self.harmony_val2_display, "", command=self._on_harmony_val2_change)
        self.menu_harmony_val2.config(**menu_config)
        self.menu_harmony_val2["menu"].config(**menu_dropdown_config)
        self.menu_harmony_val2.pack(side="left", padx=(0, 6))

        # Botão Compassos por Acorde (1x / 2x)
        self.btn_bars_per_chord = tk.Label(
            prog_controls_row, text="", bg=COLORS["bg_step"], fg="#64D2FF",
            font=("Helvetica Neue", 10, "bold"), padx=10, pady=5, cursor=HAND_CURSOR
        )
        self.btn_bars_per_chord.pack(side="left")
        self.btn_bars_per_chord.bind("<Button-1>", lambda e: self._toggle_bars_per_chord())

        # High-contrast Current & Next Chord Cards on the right
        chord_teleprompter = tk.Frame(harmony_bar, bg=COLORS["bg_subpanel"])
        chord_teleprompter.pack(side="right")

        curr_box = tk.Frame(chord_teleprompter, bg="#16324F", padx=14, pady=4)
        curr_box.pack(side="left", padx=(0, 10))

        self.lbl_curr_chord_tag = tk.Label(
            curr_box, text="AGORA", bg="#16324F", fg="#64D2FF",
            font=("Helvetica Neue", 8, "bold")
        )
        self.lbl_curr_chord_tag.pack()

        self.lbl_curr_chord_val = tk.Label(
            curr_box, text="Am7", bg="#16324F", fg="#FFFFFF",
            font=("Helvetica Neue", 16, "bold"), width=6
        )
        self.lbl_curr_chord_val.pack()

        next_box = tk.Frame(chord_teleprompter, bg=COLORS["bg_step"], padx=12, pady=4)
        next_box.pack(side="left")

        self.lbl_next_chord_tag = tk.Label(
            next_box, text="PRÓXIMO", bg=COLORS["bg_step"], fg=COLORS["text_secondary"],
            font=("Helvetica Neue", 8, "bold")
        )
        self.lbl_next_chord_tag.pack()

        self.lbl_next_chord_val = tk.Label(
            next_box, text="Am7", bg=COLORS["bg_step"], fg="#D1D1D6",
            font=("Helvetica Neue", 14, "bold"), width=6
        )
        self.lbl_next_chord_val.pack()

        # 4. Status Banner
        self.lbl_status_banner = tk.Label(
            stage_inner, text="", bg=COLORS["bg_card"], fg=COLORS["accent_orange"],
            font=("Helvetica Neue", 11, "bold"), height=1
        )
        self.lbl_status_banner.pack(fill="x", pady=(0, 4))

        # 5. Beat Subdivision Grid
        self.grid_frame = tk.Frame(stage_inner, bg=COLORS["bg_card"])
        self.grid_frame.pack(fill="x", pady=(2, 10))

        # 6. Dedicated Legend Row
        self.legend_frame = tk.Frame(stage_inner, bg=COLORS["bg_card"])
        self.legend_frame.pack(fill="x", pady=(0, 8))

        sep = tk.Frame(stage_inner, bg=COLORS["border_subtle"], height=1)
        sep.pack(fill="x", pady=(2, 10))

        # 7. Grouped Bottom Controls
        bottom_controls = tk.Frame(stage_inner, bg=COLORS["bg_card"])
        bottom_controls.pack(fill="x", side="bottom")

        bpm_box = tk.Frame(bottom_controls, bg=COLORS["bg_card"])
        bpm_box.pack(side="left", fill="x", expand=True, padx=(0, 16))

        bpm_header = tk.Frame(bpm_box, bg=COLORS["bg_card"])
        bpm_header.pack(fill="x", pady=(0, 5))

        self.lbl_bpm_title = tk.Label(
            bpm_header, text="", bg=COLORS["bg_card"], fg=COLORS["text_secondary"],
            font=("Helvetica Neue", 10, "bold")
        )
        self.lbl_bpm_title.pack(side="left")

        self.lbl_bpm_val = tk.Label(
            bpm_header, text="96 BPM", bg=COLORS["bg_card"], fg=COLORS["text_primary"],
            font=("Helvetica Neue", 15, "bold")
        )
        self.lbl_bpm_val.pack(side="right")

        slider_row = tk.Frame(bpm_box, bg=COLORS["bg_card"])
        slider_row.pack(fill="x")

        btn_minus = RoundedButton(
            slider_row, text="−", width=34, height=34, radius=8,
            bg_color=COLORS["bg_step"], hover_color="#3A3A44",
            command=lambda: self._adjust_bpm(-5)
        )
        btn_minus.pack(side="left", padx=(0, 6))

        self.bpm_slider = tk.Scale(
            slider_row, from_=40, to=200, orient="horizontal",
            variable=self.bpm, command=self._update_bpm_label,
            bg=COLORS["bg_card"], fg="#FFFFFF", troughcolor=COLORS["bg_step"],
            activebackground=COLORS["accent_blue"], highlightthickness=0,
            bd=0, sliderrelief="flat", showvalue=False, cursor=HAND_CURSOR
        )
        self.bpm_slider.pack(side="left", fill="x", expand=True)

        btn_plus = RoundedButton(
            slider_row, text="+", width=34, height=34, radius=8,
            bg_color=COLORS["bg_step"], hover_color="#3A3A44",
            command=lambda: self._adjust_bpm(5)
        )
        btn_plus.pack(side="left", padx=(6, 8))

        self.btn_tap = RoundedButton(
            slider_row, text="👆 Tap", width=74, height=34, radius=8,
            bg_color="#2C2C35", hover_color="#3D3D4A",
            fg_color="#64D2FF", font=("Helvetica Neue", 11, "bold"),
            command=self._handle_tap_tempo
        )
        self.btn_tap.pack(side="left")

        coach_group = tk.Frame(bottom_controls, bg=COLORS["bg_subpanel"], padx=10, pady=6)
        coach_group.pack(side="left", padx=(0, 16))

        self.lbl_coach_group_title = tk.Label(
            coach_group, text="", bg=COLORS["bg_subpanel"], fg=COLORS["text_secondary"],
            font=("Helvetica Neue", 9, "bold"), anchor="w"
        )
        self.lbl_coach_group_title.pack(anchor="w", pady=(0, 4))

        coach_pills_row = tk.Frame(coach_group, bg=COLORS["bg_subpanel"])
        coach_pills_row.pack()

        for key_name, var_ref in [
            ("count_in", self.count_in_enabled),
            ("speed_trainer", self.speed_trainer_enabled),
            ("gap_click", self.gap_click_enabled),
        ]:
            btn = tk.Label(
                coach_pills_row, text="", padx=9, pady=5, cursor=HAND_CURSOR,
                font=("Helvetica Neue", 10, "bold")
            )
            btn.pack(side="left", padx=2)
            btn.bind("<Button-1>", lambda e, k=key_name, v=var_ref: self._toggle_coach_option(k, v))
            self.coach_buttons[key_name] = btn

        play_box = tk.Frame(bottom_controls, bg=COLORS["bg_card"])
        play_box.pack(side="right")

        self.btn_play = RoundedButton(
            play_box, text="", width=196, height=48, radius=14,
            bg_color=COLORS["accent_green"], hover_color="#46E06D",
            fg_color="#000000", font=("Helvetica Neue", 15, "bold"),
            command=self._toggle_playback
        )
        self.btn_play.pack()

        self.lbl_shortcut = tk.Label(
            play_box, text="", bg=COLORS["bg_card"], fg=COLORS["text_secondary"],
            font=("Helvetica Neue", 10)
        )
        self.lbl_shortcut.pack(pady=(4, 0))

        # Tooltips
        ToolTip(self.sound_buttons["guitar"], lambda: self._tr("tooltips")["sound_guitar"])
        ToolTip(self.sound_buttons["percussion"], lambda: self._tr("tooltips")["sound_perc"])
        ToolTip(self.sound_buttons["metronome"], lambda: self._tr("tooltips")["sound_metro"])
        ToolTip(self.btn_fav, lambda: self._tr("tooltips")["fav_star"])
        ToolTip(self.menu_harmony_type, lambda: self._tr("tooltips")["harmony_type"])
        ToolTip(self.menu_harmony_val1, lambda: self._tr("tooltips")["harmony_val1"])
        ToolTip(self.menu_harmony_val2, lambda: self._tr("tooltips")["harmony_val2"])
        ToolTip(self.btn_bars_per_chord, lambda: self._tr("tooltips")["bars_per_chord"])
        ToolTip(self.coach_buttons["count_in"], lambda: self._tr("tooltips")["count_in"])
        ToolTip(self.coach_buttons["speed_trainer"], lambda: self._tr("tooltips")["speed_trainer"])
        ToolTip(self.coach_buttons["gap_click"], lambda: self._tr("tooltips")["gap_click"])
        ToolTip(self.btn_tap, lambda: self._tr("tooltips")["tap_btn"])
        ToolTip(self.btn_play, lambda: self._tr("tooltips")["play_btn"])

    def _redraw_panel(self, canvas, fill_color, border_color, radius=18):
        canvas.delete("panel_bg")
        w = canvas.winfo_width()
        h = canvas.winfo_height()
        if w > 10 and h > 10:
            draw_rounded_rect(
                canvas, 1, 1, w - 1, h - 1, radius=radius,
                fill=fill_color, outline=border_color, width=1, tags="panel_bg"
            )
            canvas.tag_lower("panel_bg")

    def _set_sound_mode(self, mode):
        self.sound_mode.set(mode)
        self.audio.set_mode(mode)
        self._refresh_sound_tabs()

    def _set_language(self, lang_code):
        self.language.set(lang_code)
        self._save_prefs()
        self._apply_language()

    def _set_category(self, cat_key):
        self.category_filter.set(cat_key)
        self._refresh_category_tabs()
        self._update_rhythm_list()

    def _rebuild_harmony_menus(self):
        # 1. Menu Tipo de Harmonia
        type_menu = self.menu_harmony_type["menu"]
        type_menu.delete(0, "end")
        type_map = {
            "fixed": self._tr("type_fixed"),
            "prog_maj": self._tr("type_prog_maj"),
            "prog_min": self._tr("type_prog_min"),
            "genre": self._tr("type_genre")
        }
        for k, label in type_map.items():
            type_menu.add_command(label=label, command=lambda key=k: self._on_harmony_type_select(key))

        curr_type = self.harmony_type.get()
        self.harmony_type_display.set(type_map.get(curr_type, type_map["fixed"]))

        # 2. Menu Val1 (Acordes, Tônicas ou Gêneros)
        val1_menu = self.menu_harmony_val1["menu"]
        val1_menu.delete(0, "end")

        if curr_type == "fixed":
            self.menu_harmony_val2.pack_forget()
            choices = list(CHORD_VOICINGS.keys())
            for c in choices:
                val1_menu.add_command(label=c, command=lambda val=c: self._on_harmony_val1_select(val))
            if self.harmony_val1.get() not in choices:
                self.harmony_val1.set(choices[0])
            self.harmony_val1_display.set(self.harmony_val1.get())

        elif curr_type in ["prog_maj", "prog_min"]:
            self.menu_harmony_val2.pack(side="left", padx=(0, 6))
            choices = list(HARMONIC_FIELDS_MAJOR.keys()) if curr_type == "prog_maj" else list(HARMONIC_FIELDS_MINOR.keys())
            for c in choices:
                val1_menu.add_command(label=c, command=lambda val=c: self._on_harmony_val1_select(val))
            if self.harmony_val1.get() not in choices:
                self.harmony_val1.set(choices[0])
            self.harmony_val1_display.set(self.harmony_val1.get())

            # Reconstroi Menu Val2 (Templates de Progressão)
            val2_menu = self.menu_harmony_val2["menu"]
            val2_menu.delete(0, "end")
            for t_key, t_data in PROGRESSION_TEMPLATES.items():
                if (curr_type == "prog_maj" and "major" in t_key) or (curr_type == "prog_min" and "minor" in t_key):
                    val2_menu.add_command(label=t_data["label_pt"], command=lambda key=t_key: self._on_harmony_val2_select(key))
            if self.harmony_val2.get() not in PROGRESSION_TEMPLATES:
                self.harmony_val2.set("major_axis" if curr_type == "prog_maj" else "minor_standard")
            self.harmony_val2_display.set(PROGRESSION_TEMPLATES[self.harmony_val2.get()]["label_pt"])

        elif curr_type == "genre":
            self.menu_harmony_val2.pack_forget()
            choices = list(GENRE_PROGRESSIONS.keys())
            for g in choices:
                val1_menu.add_command(label=GENRE_PROGRESSIONS[g]["label_pt"], command=lambda val=g: self._on_harmony_val1_select(val))
            if self.harmony_val1.get() not in choices:
                self.harmony_val1.set(choices[0])
            self.harmony_val1_display.set(GENRE_PROGRESSIONS[self.harmony_val1.get()]["label_pt"])

        chords = self._get_active_chord_list()
        self.audio.set_chord(chords[0])
        self._update_chord_display(chords[0], chords[1 % len(chords)])

    def _on_harmony_type_select(self, key):
        self.harmony_type.set(key)
        if key == "fixed":
            self.harmony_val1.set("Am7")
        elif key == "prog_maj":
            self.harmony_val1.set("C")
            self.harmony_val2.set("major_axis")
        elif key == "prog_min":
            self.harmony_val1.set("Am")
            self.harmony_val2.set("minor_standard")
        elif key == "genre":
            self.harmony_val1.set("pop")
        self._rebuild_harmony_menus()

    def _on_harmony_val1_select(self, val):
        self.harmony_val1.set(val)
        if self.harmony_type.get() == "genre":
            self.harmony_val1_display.set(GENRE_PROGRESSIONS[val]["label_pt"])
        else:
            self.harmony_val1_display.set(val)
        chords = self._get_active_chord_list()
        self.audio.set_chord(chords[0])
        self._update_chord_display(chords[0], chords[1 % len(chords)])

    def _on_harmony_val2_select(self, key):
        self.harmony_val2.set(key)
        self.harmony_val2_display.set(PROGRESSION_TEMPLATES[key]["label_pt"])
        chords = self._get_active_chord_list()
        self.audio.set_chord(chords[0])
        self._update_chord_display(chords[0], chords[1 % len(chords)])

    def _on_harmony_type_change(self, val): pass
    def _on_harmony_val1_change(self, val): pass
    def _on_harmony_val2_change(self, val): pass

    def _toggle_bars_per_chord(self):
        new_val = 2 if self.bars_per_chord.get() == 1 else 1
        self.bars_per_chord.set(new_val)
        self._refresh_bars_per_chord_label()

    def _refresh_bars_per_chord_label(self):
        txt = self._tr("bars_per_chord_2") if self.bars_per_chord.get() == 2 else self._tr("bars_per_chord_1")
        self.btn_bars_per_chord.config(text=txt)

    def _toggle_coach_option(self, key_name, var_ref):
        var_ref.set(not var_ref.get())
        self._refresh_coach_buttons()

    def _toggle_favorite(self):
        rid = self.current_rhythm_id
        if rid in self.favorites:
            self.favorites.remove(rid)
        else:
            self.favorites.add(rid)
        self._save_prefs()
        self._refresh_fav_star()
        self._update_rhythm_list()

    def _refresh_fav_star(self):
        if self.current_rhythm_id in self.favorites:
            self.btn_fav.config(text="★", fg=COLORS["accent_gold"])
        else:
            self.btn_fav.config(text="☆", fg=COLORS["text_secondary"])

    def _handle_tap_tempo(self):
        now = time.perf_counter()
        if self.tap_timestamps and (now - self.tap_timestamps[-1]) > 2.2:
            self.tap_timestamps.clear()
        self.tap_timestamps.append(now)
        if len(self.tap_timestamps) > 5:
            self.tap_timestamps.pop(0)
        if len(self.tap_timestamps) >= 2:
            intervals = [
                self.tap_timestamps[i] - self.tap_timestamps[i - 1]
                for i in range(1, len(self.tap_timestamps))
            ]
            avg_interval = sum(intervals) / len(intervals)
            if avg_interval > 0:
                detected_bpm = max(40, min(200, int(round(60.0 / avg_interval))))
                self.bpm.set(detected_bpm)
                self._update_bpm_label(detected_bpm)

    def _refresh_sound_tabs(self):
        active = self.sound_mode.get()
        for mode_code, lbl in self.sound_buttons.items():
            if mode_code == active:
                lbl.config(bg=COLORS["accent_orange"], fg="#000000")
            else:
                lbl.config(bg=COLORS["bg_sidebar"], fg=COLORS["text_secondary"])

    def _refresh_language_tabs(self):
        active = self.language.get()
        for code, lbl in self.lang_buttons.items():
            if code == active:
                lbl.config(bg=COLORS["accent_blue"], fg="#FFFFFF")
            else:
                lbl.config(bg=COLORS["bg_sidebar"], fg=COLORS["text_secondary"])

    def _refresh_category_tabs(self):
        active = self.category_filter.get()
        for key, lbl in self.cat_buttons.items():
            if key == active:
                lbl.config(bg=COLORS["accent_blue"], fg="#FFFFFF")
            else:
                lbl.config(bg=COLORS["bg_step"], fg=COLORS["text_secondary"])

    def _refresh_coach_buttons(self):
        states = {
            "count_in": (self.count_in_enabled.get(), self._tr("coach_countin")),
            "speed_trainer": (self.speed_trainer_enabled.get(), self._tr("coach_speed")),
            "gap_click": (self.gap_click_enabled.get(), self._tr("coach_gap")),
        }
        for k, (enabled, label_txt) in states.items():
            lbl = self.coach_buttons[k]
            lbl.config(
                text=label_txt,
                bg=COLORS["accent_purple"] if enabled else COLORS["bg_step"],
                fg="#FFFFFF" if enabled else COLORS["text_secondary"]
            )

    def _update_chord_display(self, curr_chord, next_chord):
        self.lbl_curr_chord_val.config(text=curr_chord)
        self.lbl_next_chord_val.config(text=next_chord)

    def _apply_language(self):
        self.root.title(self._tr("window_title"))
        self.lbl_header.config(text=self._tr("app_header"))
        self.lbl_subtitle.config(text=self._tr("app_subtitle"))
        self.lbl_bpm_title.config(text=self._tr("bpm_label"))
        self.lbl_shortcut.config(text=self._tr("shortcut_hint"))
        self.lbl_prog_title.config(text=self._tr("prog_label"))
        self.lbl_coach_group_title.config(text=self._tr("coach_label"))
        self.lbl_curr_chord_tag.config(text=self._tr("curr_chord"))
        self.lbl_next_chord_tag.config(text=self._tr("next_chord"))
        self.btn_tap.configure_style(text=self._tr("tap_btn"))

        self.sound_buttons["guitar"].config(text=f"🎸  {self._tr('sound_guitar')}")
        self.sound_buttons["percussion"].config(text=f"🥁  {self._tr('sound_perc')}")
        self.sound_buttons["metronome"].config(text=f"⏱  {self._tr('sound_metro')}")

        self.cat_buttons["fav"].config(text=self._tr("cat_fav"))
        self.cat_buttons["all"].config(text=self._tr("cat_all"))
        self.cat_buttons["brazil"].config(text=self._tr("cat_brazil"))
        self.cat_buttons["general"].config(text=self._tr("cat_general"))
        self.cat_buttons["tech"].config(text=self._tr("cat_tech"))

        self._rebuild_harmony_menus()
        self._refresh_bars_per_chord_label()
        self._refresh_sound_tabs()
        self._refresh_language_tabs()
        self._refresh_category_tabs()
        self._refresh_coach_buttons()
        self._rebuild_legend()
        self._update_bpm_label(self.bpm.get())

        if self.is_playing:
            self.btn_play.configure_style(
                text=self._tr("btn_stop"), bg_color=COLORS["accent_red"], hover_color="#FF6961", fg_color="#FFFFFF"
            )
        else:
            self.btn_play.configure_style(
                text=self._tr("btn_play"), bg_color=COLORS["accent_green"], hover_color="#46E06D", fg_color="#000000"
            )

        self._update_rhythm_list()
        self._load_rhythm(self.current_rhythm_id, reset_bpm=False)

    def _rebuild_legend(self):
        for w in self.legend_frame.winfo_children():
            w.destroy()

        for color, label_text in self._tr("legend_items"):
            item = tk.Frame(self.legend_frame, bg=COLORS["bg_card"])
            item.pack(side="left", padx=(0, 18))

            dot = tk.Canvas(item, width=10, height=10, bg=COLORS["bg_card"], highlightthickness=0)
            dot.pack(side="left", padx=(0, 6))
            dot.create_oval(1, 1, 9, 9, fill=color, outline="")

            tk.Label(
                item, text=label_text, bg=COLORS["bg_card"], fg=COLORS["text_secondary"],
                font=("Helvetica Neue", 11)
            ).pack(side="left")

    @staticmethod
    def _normalize_sort_key(text):
        normalized = unicodedata.normalize("NFD", text)
        without_accents = "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")
        return without_accents.lower()

    def _update_rhythm_list(self):
        filter_val = self.category_filter.get()
        query = self.search_query.get().strip().lower()
        lang = self.language.get()

        self.listbox.delete(0, tk.END)
        self.visible_keys.clear()

        filtered_items = []
        for rhythm_id, data in RHYTHMS.items():
            cat_en = data["en"]["category"]
            name_local = data[lang]["name"]

            matches_cat = (
                filter_val == "all" or
                (filter_val == "fav" and rhythm_id in self.favorites) or
                (filter_val == "brazil" and cat_en == "Brazil") or
                (filter_val == "general" and cat_en == "General") or
                (filter_val == "tech" and cat_en == "Technique")
            )
            matches_search = (not query) or (query in name_local.lower())

            if matches_cat and matches_search:
                filtered_items.append((rhythm_id, name_local))

        filtered_items.sort(key=lambda item: self._normalize_sort_key(item[1]))

        for rhythm_id, name_local in filtered_items:
            self.visible_keys.append(rhythm_id)
            prefix = "★ " if rhythm_id in self.favorites else "   "
            self.listbox.insert(tk.END, f"{prefix}{name_local}")

        if self.current_rhythm_id in self.visible_keys:
            idx = self.visible_keys.index(self.current_rhythm_id)
            self.listbox.selection_set(idx)
            self.listbox.see(idx)

    def _on_rhythm_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            rhythm_id = self.visible_keys[selection[0]]
            self._load_rhythm(rhythm_id, reset_bpm=True)

    def _load_rhythm(self, rhythm_id, reset_bpm=True):
        was_playing = self.is_playing
        if was_playing and reset_bpm:
            self._stop()

        self.current_rhythm_id = rhythm_id
        lang = self.language.get()
        data = RHYTHMS[rhythm_id]
        locale_info = data[lang]

        self._refresh_fav_star()
        self.lbl_rhythm_title.config(text=locale_info["name"])
        self.lbl_bar_counter.config(text=f"{self._tr('bar_counter')} 1")
        self.badge_origin.config(text=f"{self._tr('origin_label')}: {locale_info['category']}")
        self.badge_sig.config(text=f"{self._tr('sig_label')}: {data['time_signature']}")
        self.lbl_description.config(text=locale_info["description"])

        songs_str, tip_str = RHYTHM_COACHING.get(rhythm_id, DEFAULT_COACHING)[lang]
        self.lbl_songs_line.config(text=f"🎵  {self._tr('songs_prefix')} {songs_str}")
        self.lbl_tip_line.config(text=f"💡  {self._tr('tip_prefix')} {tip_str}")

        if reset_bpm:
            self.bpm.set(data["default_bpm"])
            self._update_bpm_label(data["default_bpm"])

        if reset_bpm or not self.step_cards:
            old_cols = self.grid_frame.grid_size()[0]
            for c in range(old_cols):
                self.grid_frame.columnconfigure(c, weight=0, uniform="")

            for widget in self.grid_frame.winfo_children():
                widget.destroy()
            self.step_cards.clear()

            num_steps = len(data["arrows"])
            pad_x = 2 if num_steps > 8 else 4

            for i in range(num_steps):
                self.grid_frame.columnconfigure(i, weight=1, uniform="step")
                card = StepCard(
                    self.grid_frame,
                    count_text=data["count"][i],
                    arrow_text=data["arrows"][i],
                    sound_type=data["sounds"][i]
                )
                card.grid(row=0, column=i, sticky="nsew", padx=pad_x)
                self.step_cards.append(card)

        if was_playing and reset_bpm:
            self._start()

    def _adjust_bpm(self, delta):
        new_val = max(40, min(200, self.bpm.get() + delta))
        self.bpm.set(new_val)
        self._update_bpm_label(new_val)

    def _update_bpm_label(self, value):
        self.lbl_bpm_val.config(text=f"{int(float(value))} BPM")

    def _toggle_playback(self):
        if self.is_playing:
            self._stop()
        else:
            self._start()

    def _start(self):
        self.is_playing = True
        self.play_session_id += 1
        session_id = self.play_session_id

        self.btn_play.configure_style(
            text=self._tr("btn_stop"),
            bg_color=COLORS["accent_red"],
            hover_color="#FF6961",
            fg_color="#FFFFFF"
        )
        self.rhythm_thread = threading.Thread(
            target=self._metronome_loop,
            args=(session_id,),
            daemon=True
        )
        self.rhythm_thread.start()

    def _stop(self):
        self.is_playing = False
        self.play_session_id += 1
        self.btn_play.configure_style(
            text=self._tr("btn_play"),
            bg_color=COLORS["accent_green"],
            hover_color="#46E06D",
            fg_color="#000000"
        )
        self.lbl_status_banner.config(text="")
        self._reset_cards()

    def _reset_cards(self):
        for card in self.step_cards:
            card.set_active(False)

    def _highlight_step(self, index, session_id):
        if not self.is_playing or session_id != self.play_session_id:
            return
        for i, card in enumerate(self.step_cards):
            card.set_active(i == index)

    def _update_bar_ui(self, bar_num, curr_chord, next_chord, banner_text, banner_color, session_id):
        if not self.is_playing or session_id != self.play_session_id:
            return
        self.lbl_bar_counter.config(text=f"{self._tr('bar_counter')} {bar_num}")
        self._update_chord_display(curr_chord, next_chord)
        self.lbl_status_banner.config(text=banner_text, fg=banner_color)

    def _get_step_interval(self, bpm_val, time_sig, total_steps):
        seconds_per_beat = 60.0 / bpm_val
        if time_sig in ["2/4", "4/4"]:
            factor = 0.25 if (time_sig == "2/4" and total_steps == 8) else 0.5
            return seconds_per_beat * factor
        elif time_sig in ["3/4", "6/8", "12/8"]:
            return seconds_per_beat / 3.0 if total_steps == 6 else seconds_per_beat
        return seconds_per_beat * 0.5

    def _get_beats_per_bar(self, time_sig):
        try:
            return int(time_sig.split("/")[0])
        except Exception:
            return 4

    def _sleep_until(self, target_time, session_id):
        now = time.perf_counter()
        remaining = target_time - now
        if remaining > 0.002:
            time.sleep(remaining - 0.0015)
        while self.is_playing and session_id == self.play_session_id and time.perf_counter() < target_time:
            pass

    def _metronome_loop(self, session_id):
        data = RHYTHMS[self.current_rhythm_id]
        sounds = data["sounds"]
        counts = data["count"]
        total_steps = len(sounds)
        time_sig = data["time_signature"]

        if self.count_in_enabled.get():
            beats_count_in = self._get_beats_per_bar(time_sig)
            next_tick = time.perf_counter()
            for b in range(beats_count_in):
                if not self.is_playing or session_id != self.play_session_id:
                    return
                self.audio.play_metronome_click(accent=(b == 0))
                banner = f"{self._tr('count_in_banner')}:   {b + 1} / {beats_count_in}"
                self.root.after(0, lambda txt=banner: self.lbl_status_banner.config(text=txt, fg=COLORS["accent_orange"]))
                next_tick += 60.0 / self.bpm.get()
                self._sleep_until(next_tick, session_id)

        step = 0
        bar_index = 0
        next_tick_time = time.perf_counter()

        while self.is_playing and session_id == self.play_session_id:
            if step == 0:
                if bar_index > 0 and self.speed_trainer_enabled.get() and (bar_index % 4 == 0):
                    new_bpm = min(200, self.bpm.get() + 5)
                    self.root.after(0, lambda v=new_bpm: (self.bpm.set(v), self._update_bpm_label(v)))

                chords = self._get_active_chord_list()
                bpc = self.bars_per_chord.get()
                chord_step_idx = (bar_index // bpc) % len(chords)
                next_chord_idx = ((bar_index + bpc) // bpc) % len(chords)
                curr_chord = chords[chord_step_idx]
                next_chord = chords[next_chord_idx]
                self.audio.set_chord(curr_chord)

                is_gap_muted = self.gap_click_enabled.get() and (bar_index % 3 == 2)
                banner_txt = self._tr("gap_muted_banner") if is_gap_muted else ""
                banner_col = COLORS["accent_red"] if is_gap_muted else COLORS["accent_orange"]

                self.root.after(
                    0, self._update_bar_ui, bar_index + 1, curr_chord, next_chord, banner_txt, banner_col, session_id
                )

            is_gap_muted = self.gap_click_enabled.get() and (bar_index % 3 == 2)

            if not is_gap_muted:
                if self.sound_mode.get() == "metronome":
                    if step == 0:
                        self.audio.play("M_ACCENT")
                    elif counts[step].isdigit():
                        self.audio.play("M_BEAT")
                else:
                    sound = sounds[step]
                    if sound:
                        self.audio.play(sound)

            self.root.after(0, self._highlight_step, step, session_id)

            interval = self._get_step_interval(self.bpm.get(), time_sig, total_steps)
            next_tick_time += interval
            step += 1
            if step >= total_steps:
                step = 0
                bar_index += 1

            now = time.perf_counter()
            if next_tick_time - now < -0.1:
                next_tick_time = now
            else:
                self._sleep_until(next_tick_time, session_id)


if __name__ == "__main__":
    root = tk.Tk()
    app = RhythmMasterApp(root)
    root.mainloop()