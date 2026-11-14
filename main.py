# main.py
import tkinter as tk
from tkinter import ttk
import threading
import time
import subprocess
import os
import wave
import math
import struct
import random
import tempfile
import unicodedata
from rhythms_db import RHYTHMS

try:
    from AppKit import NSSound
    HAS_NSSOUND = True
except ImportError:
    HAS_NSSOUND = False

HAND_CURSOR = "pointinghand"

UI_TEXTS = {
    "en": {
        "window_title": "Rhythm Master — Musical Practice",
        "app_header": "Rhythm Master",
        "app_subtitle": "Interactive Strumming & Percussion Trainer",
        "search_placeholder": "Search rhythms...",
        "sound_guitar": "Guitar",
        "sound_perc": "Percussion",
        "sound_metro": "Metronome",
        "cat_all": "All",
        "cat_brazil": "Brazil",
        "cat_general": "General",
        "cat_tech": "Technique",
        "origin_label": "Origin",
        "sig_label": "Time Signature",
        "legend_items": [
            ("#32D74B", "↓(B) Bass / Thumb"),
            ("#0A84FF", "↓(T) Treble / Fingers"),
            ("#FF9F0A", "↓(S) Slap / Mute"),
            ("#BF5AF2", "↑ Upstroke")
        ],
        "bpm_label": "TEMPO",
        "btn_play": "▶   Play Rhythm",
        "btn_stop": "⏹   Stop",
        "shortcut_hint": "Press Spacebar to Play / Stop"
    },
    "pt": {
        "window_title": "Mestre dos Ritmos — Prática Musical",
        "app_header": "Mestre dos Ritmos",
        "app_subtitle": "Treinador Interativo de Batidas e Percussão",
        "search_placeholder": "Buscar ritmos...",
        "sound_guitar": "Violão",
        "sound_perc": "Percussão",
        "sound_metro": "Metrônomo",
        "cat_all": "Todos",
        "cat_brazil": "Brasil",
        "cat_general": "Geral",
        "cat_tech": "Técnica",
        "origin_label": "Origem",
        "sig_label": "Compasso",
        "legend_items": [
            ("#32D74B", "↓(B) Grave / Polegar"),
            ("#0A84FF", "↓(T) Agudo / Mão"),
            ("#FF9F0A", "↓(S) Tapa / Abafado"),
            ("#BF5AF2", "↑ Puxada")
        ],
        "bpm_label": "ANDAMENTO",
        "btn_play": "▶   Tocar Ritmo",
        "btn_stop": "⏹   Parar",
        "shortcut_hint": "Pressione Espaço para Tocar / Parar"
    }
}

COLORS = {
    "bg_main": "#141416",
    "bg_sidebar": "#1C1C1F",
    "bg_card": "#232327",
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
}


def draw_rounded_rect(canvas, x1, y1, x2, y2, radius=14, **kwargs):
    """Draws a smooth rounded rectangle on a Tkinter Canvas."""
    radius = min(radius, (x2 - x1) / 2, (y2 - y1) / 2)
    points = [
        x1 + radius, y1,
        x1 + radius, y1,
        x2 - radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)


class RoundedButton(tk.Canvas):
    """Modern rounded button with native macOS pointing hand cursor and hover effect."""
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


class StepCard(tk.Canvas):
    """Responsive rounded visual card for each rhythmic subdivision."""
    def __init__(self, parent, count_text, arrow_text, sound_type, **kwargs):
        super().__init__(parent, width=10, height=130, bg=COLORS["bg_card"], highlightthickness=0, **kwargs)
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
            w / 2, 36,
            text=self.count_text,
            fill=count_fg,
            font=("Helvetica Neue", count_font_size, "bold")
        )

        display_arrow = self.arrow_text
        if w < 58 and " (" in display_arrow:
            display_arrow = display_arrow.replace(" (", "\n(")
        elif w < 54 and "(" in display_arrow and not display_arrow.startswith("("):
            display_arrow = display_arrow.replace("(", "\n(")

        self.create_text(
            w / 2, 82,
            text=display_arrow,
            fill=arrow_fg,
            justify="center",
            font=("Helvetica Neue", arrow_font_size, "bold")
        )


class MacNativeAudioEngine:
    """
    Synthesizes acoustic guitar (Karplus-Strong), percussion, and metronome click samples,
    pre-loading them into RAM via macOS CoreAudio (NSSound) for zero-latency playback.
    """
    def __init__(self, pool_size=4):
        self.temp_dir = tempfile.gettempdir()
        self.mode = "guitar"  # "guitar", "percussion", or "metronome"
        self.files = {
            "guitar": {
                "B": os.path.join(self.temp_dir, "gtr_bass.wav"),
                "T": os.path.join(self.temp_dir, "gtr_treble.wav"),
                "U": os.path.join(self.temp_dir, "gtr_upstroke.wav"),
                "S": os.path.join(self.temp_dir, "gtr_slap.wav"),
            },
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

        self.pool_size = pool_size
        self.sound_pools = {"guitar": {}, "percussion": {}, "metronome": {}}
        self.pool_indices = {
            "guitar": {"B": 0, "T": 0, "U": 0, "S": 0},
            "percussion": {"B": 0, "T": 0, "U": 0, "S": 0},
            "metronome": {"M_ACCENT": 0, "M_BEAT": 0},
        }

        if HAS_NSSOUND:
            for mode_name, paths in self.files.items():
                for key, path in paths.items():
                    voices = []
                    for _ in range(pool_size):
                        snd = NSSound.alloc().initWithContentsOfFile_byReference_(path, False)
                        if snd:
                            voices.append(snd)
                    self.sound_pools[mode_name][key] = voices

    def _write_wav(self, path, samples, sample_rate=44100):
        with wave.open(path, "w") as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            data = b"".join(struct.pack("<h", max(-32767, min(32767, int(s * 32767)))) for s in samples)
            wav_file.writeframes(data)

    def _karplus_strong_string(self, freq, duration, sr=44100, decay=0.996, brightness=0.5, gain=1.0):
        """Physical modeling of a plucked/strummed acoustic guitar string without DC offset."""
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
        """Mixes multiple guitar strings with headroom and soft saturation protection."""
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
        bass_notes = [
            (110.00, 0.000, 0.85),
            (164.81, 0.014, 0.45),
            (196.00, 0.026, 0.25),
        ]
        samples_b = self._mix_strum(
            bass_notes, total_duration=0.44, sr=sr, decay=0.9965, brightness=0.25, target_peak=0.70
        )
        self._write_wav(self.files["guitar"]["B"], samples_b, sr)

        treble_notes = [
            (164.81, 0.000, 0.45),
            (196.00, 0.009, 0.65),
            (246.94, 0.018, 0.75),
            (329.63, 0.027, 0.80),
        ]
        samples_t = self._mix_strum(
            treble_notes, total_duration=0.36, sr=sr, decay=0.995, brightness=0.55, target_peak=0.72
        )
        self._write_wav(self.files["guitar"]["T"], samples_t, sr)

        up_notes = [
            (329.63, 0.000, 0.70),
            (246.94, 0.008, 0.60),
            (196.00, 0.016, 0.45),
        ]
        samples_u = self._mix_strum(
            up_notes, total_duration=0.26, sr=sr, decay=0.9935, brightness=0.50, target_peak=0.65
        )
        self._write_wav(self.files["guitar"]["U"], samples_u, sr)

        muted_notes = [
            (110.00, 0.000, 0.50),
            (196.00, 0.005, 0.65),
            (246.94, 0.010, 0.70),
            (329.63, 0.015, 0.65),
        ]
        samples_s = self._mix_strum(
            muted_notes, total_duration=0.11, sr=sr, decay=0.935, brightness=0.60, target_peak=0.60
        )
        for i in range(len(samples_s)):
            t = i / sr
            body_thump = 0.25 * math.exp(-t * 55) * math.sin(2 * math.pi * 120 * t)
            samples_s[i] = max(-0.85, min(0.85, samples_s[i] + body_thump))
        self._write_wav(self.files["guitar"]["S"], samples_s, sr)

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
        """Generates crisp woodblock-style metronome clicks (Accented Beat 1 vs. Regular Beat)."""
        sr = 44100
        dur = 0.055

        # Accented Beat 1: High woodblock pitch (1320 Hz + harmonic overtone)
        samples_acc = []
        for i in range(int(sr * dur)):
            t = i / sr
            env = math.exp(-t * 75)
            wave_val = 0.70 * math.sin(2 * math.pi * 1320 * t) + 0.30 * math.sin(2 * math.pi * 2640 * t)
            samples_acc.append(0.82 * env * wave_val)
        self._write_wav(self.files["metronome"]["M_ACCENT"], samples_acc, sr)

        # Regular Main Beat (2, 3, 4...): Warm woodblock pitch (880 Hz)
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

    def play(self, sound_type):
        mode = self.mode
        if sound_type not in self.files[mode]:
            return

        if HAS_NSSOUND and sound_type in self.sound_pools[mode] and self.sound_pools[mode][sound_type]:
            idx = self.pool_indices[mode][sound_type]
            snd = self.sound_pools[mode][sound_type][idx]
            self.pool_indices[mode][sound_type] = (idx + 1) % len(self.sound_pools[mode][sound_type])
            snd.stop()
            snd.setCurrentTime_(0.0)
            snd.play()
        else:
            subprocess.Popen(["afplay", self.files[mode][sound_type]], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


class RhythmMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1150x680")
        self.root.minsize(980, 620)
        self.root.configure(bg=COLORS["bg_main"])

        self.language = tk.StringVar(value="pt")
        self.sound_mode = tk.StringVar(value="guitar")
        self.category_filter = tk.StringVar(value="all")
        self.search_query = tk.StringVar(value="")
        self.current_rhythm_id = "traditional_samba"
        self.visible_keys = []

        self.audio = MacNativeAudioEngine()
        self.is_playing = False
        self.play_session_id = 0
        self.rhythm_thread = None
        self.bpm = tk.IntVar(value=96)
        self.step_cards = []
        self.cat_buttons = {}
        self.lang_buttons = {}
        self.sound_buttons = {}

        self._build_ui()
        self._apply_language()

        self.root.bind("<space>", self._on_spacebar)

    def _tr(self, key):
        return UI_TEXTS[self.language.get()][key]

    def _on_spacebar(self, event):
        if self.root.focus_get() != self.search_entry:
            self._toggle_playback()

    def _build_ui(self):
        header = tk.Frame(self.root, bg=COLORS["bg_main"], padx=28, pady=18)
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

        # Top-right segmented controls (Audio Mode + Language)
        right_controls = tk.Frame(header, bg=COLORS["bg_main"])
        right_controls.pack(side="right", anchor="center")

        # Audio mode switch (Guitar | Percussion | Metronome)
        sound_container = tk.Frame(right_controls, bg=COLORS["bg_sidebar"], padx=4, pady=4)
        sound_container.pack(side="left", padx=(0, 14))

        for mode_code in ["guitar", "percussion", "metronome"]:
            btn = tk.Label(
                sound_container, text="", padx=12, pady=6, cursor=HAND_CURSOR,
                font=("Helvetica Neue", 11, "bold")
            )
            btn.pack(side="left", padx=2)
            btn.bind("<Button-1>", lambda e, m=mode_code: self._set_sound_mode(m))
            self.sound_buttons[mode_code] = btn

        # Language switch (EN | PT)
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

        main_area = tk.Frame(self.root, bg=COLORS["bg_main"], padx=28, pady=6)
        main_area.pack(fill="both", expand=True)

        # Left Sidebar
        sidebar_canvas = tk.Canvas(main_area, width=300, bg=COLORS["bg_main"], highlightthickness=0)
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
        search_box.pack(fill="x", pady=(0, 12))

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
        cat_bar.pack(fill="x", pady=(0, 12))

        for cat_key in ["all", "brazil", "general", "tech"]:
            lbl = tk.Label(
                cat_bar, text="", pady=6, cursor=HAND_CURSOR,
                font=("Helvetica Neue", 11, "bold")
            )
            lbl.pack(side="left", expand=True, fill="x", padx=2)
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

        # Right Stage
        stage_canvas = tk.Canvas(main_area, width=10, bg=COLORS["bg_main"], highlightthickness=0)
        stage_canvas.pack(side="right", fill="both", expand=True, pady=(0, 22))

        stage_inner = tk.Frame(stage_canvas, bg=COLORS["bg_card"], padx=24, pady=22)
        stage_win = stage_canvas.create_window((0, 0), window=stage_inner, anchor="nw")
        stage_canvas.bind(
            "<Configure>",
            lambda e: (
                self._redraw_panel(stage_canvas, COLORS["bg_card"], COLORS["border_subtle"]),
                stage_canvas.itemconfigure(stage_win, width=e.width, height=e.height),
                self.lbl_description.config(wraplength=max(300, e.width - 56))
            )
        )

        top_info = tk.Frame(stage_inner, bg=COLORS["bg_card"])
        top_info.pack(fill="x")

        self.lbl_rhythm_title = tk.Label(
            top_info, text="", bg=COLORS["bg_card"], fg=COLORS["text_primary"],
            font=("Helvetica Neue", 20, "bold"), anchor="w"
        )
        self.lbl_rhythm_title.pack(side="left")

        badges_frame = tk.Frame(top_info, bg=COLORS["bg_card"])
        badges_frame.pack(side="right")

        self.badge_origin = tk.Label(
            badges_frame, text="", bg="#1D3557", fg="#64D2FF",
            font=("Helvetica Neue", 11, "bold"), padx=10, pady=5
        )
        self.badge_origin.pack(side="left", padx=(0, 8))

        self.badge_sig = tk.Label(
            badges_frame, text="", bg="#2C2C35", fg="#FFD60A",
            font=("Helvetica Neue", 11, "bold"), padx=10, pady=5
        )
        self.badge_sig.pack(side="left")

        self.lbl_description = tk.Label(
            stage_inner, text="", bg=COLORS["bg_card"], fg=COLORS["text_secondary"],
            font=("Helvetica Neue", 13), wraplength=600, justify="left", anchor="w"
        )
        self.lbl_description.pack(fill="x", pady=(10, 20))

        self.grid_frame = tk.Frame(stage_inner, bg=COLORS["bg_card"])
        self.grid_frame.pack(fill="x", pady=(6, 18))

        self.legend_frame = tk.Frame(stage_inner, bg=COLORS["bg_card"])
        self.legend_frame.pack(fill="x", pady=(0, 16))

        sep = tk.Frame(stage_inner, bg=COLORS["border_subtle"], height=1)
        sep.pack(fill="x", pady=(4, 16))

        bottom_controls = tk.Frame(stage_inner, bg=COLORS["bg_card"])
        bottom_controls.pack(fill="x", side="bottom")

        bpm_box = tk.Frame(bottom_controls, bg=COLORS["bg_card"])
        bpm_box.pack(side="left", fill="x", expand=True, padx=(0, 24))

        bpm_header = tk.Frame(bpm_box, bg=COLORS["bg_card"])
        bpm_header.pack(fill="x", pady=(0, 6))

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
            slider_row, text="−", width=36, height=34, radius=8,
            bg_color=COLORS["bg_step"], hover_color="#3A3A44",
            command=lambda: self._adjust_bpm(-5)
        )
        btn_minus.pack(side="left", padx=(0, 10))

        self.bpm_slider = tk.Scale(
            slider_row, from_=40, to=200, orient="horizontal",
            variable=self.bpm, command=self._update_bpm_label,
            bg=COLORS["bg_card"], fg="#FFFFFF", troughcolor=COLORS["bg_step"],
            activebackground=COLORS["accent_blue"], highlightthickness=0,
            bd=0, sliderrelief="flat", showvalue=False, cursor=HAND_CURSOR
        )
        self.bpm_slider.pack(side="left", fill="x", expand=True)

        btn_plus = RoundedButton(
            slider_row, text="+", width=36, height=34, radius=8,
            bg_color=COLORS["bg_step"], hover_color="#3A3A44",
            command=lambda: self._adjust_bpm(5)
        )
        btn_plus.pack(side="left", padx=(10, 0))

        play_box = tk.Frame(bottom_controls, bg=COLORS["bg_card"])
        play_box.pack(side="right")

        self.btn_play = RoundedButton(
            play_box, text="", width=200, height=50, radius=14,
            bg_color=COLORS["accent_green"], hover_color="#46E06D",
            fg_color="#000000", font=("Helvetica Neue", 15, "bold"),
            command=self._toggle_playback
        )
        self.btn_play.pack()

        self.lbl_shortcut = tk.Label(
            play_box, text="", bg=COLORS["bg_card"], fg=COLORS["text_secondary"],
            font=("Helvetica Neue", 10)
        )
        self.lbl_shortcut.pack(pady=(5, 0))

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
        self._apply_language()

    def _set_category(self, cat_key):
        self.category_filter.set(cat_key)
        self._refresh_category_tabs()
        self._update_rhythm_list()

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

    def _apply_language(self):
        self.root.title(self._tr("window_title"))
        self.lbl_header.config(text=self._tr("app_header"))
        self.lbl_subtitle.config(text=self._tr("app_subtitle"))
        self.lbl_bpm_title.config(text=self._tr("bpm_label"))
        self.lbl_shortcut.config(text=self._tr("shortcut_hint"))

        self.sound_buttons["guitar"].config(text=f"🎸  {self._tr('sound_guitar')}")
        self.sound_buttons["percussion"].config(text=f"🥁  {self._tr('sound_perc')}")
        self.sound_buttons["metronome"].config(text=f"⏱  {self._tr('sound_metro')}")

        self.cat_buttons["all"].config(text=self._tr("cat_all"))
        self.cat_buttons["brazil"].config(text=self._tr("cat_brazil"))
        self.cat_buttons["general"].config(text=self._tr("cat_general"))
        self.cat_buttons["tech"].config(text=self._tr("cat_tech"))

        self._refresh_sound_tabs()
        self._refresh_language_tabs()
        self._refresh_category_tabs()
        self._rebuild_legend()
        self._update_bpm_label(self.bpm.get())

        if self.is_playing:
            self.btn_play.configure_style(text=self._tr("btn_stop"), bg_color=COLORS["accent_red"], hover_color="#FF6961", fg_color="#FFFFFF")
        else:
            self.btn_play.configure_style(text=self._tr("btn_play"), bg_color=COLORS["accent_green"], hover_color="#46E06D", fg_color="#000000")

        self._update_rhythm_list()
        self._load_rhythm(self.current_rhythm_id, reset_bpm=False)

    def _rebuild_legend(self):
        for w in self.legend_frame.winfo_children():
            w.destroy()

        for color, label_text in self._tr("legend_items"):
            item = tk.Frame(self.legend_frame, bg=COLORS["bg_card"])
            item.pack(side="left", padx=(0, 14))

            dot = tk.Canvas(item, width=10, height=10, bg=COLORS["bg_card"], highlightthickness=0)
            dot.pack(side="left", padx=(0, 5))
            dot.create_oval(1, 1, 9, 9, fill=color, outline="")

            tk.Label(
                item, text=label_text, bg=COLORS["bg_card"], fg=COLORS["text_secondary"],
                font=("Helvetica Neue", 11)
            ).pack(side="left")

    @staticmethod
    def _normalize_sort_key(text):
        """Removes accents and lowercases text for proper alphabetical sorting in PT and EN."""
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
                (filter_val == "brazil" and cat_en == "Brazil") or
                (filter_val == "general" and cat_en == "General") or
                (filter_val == "tech" and cat_en == "Technique")
            )
            matches_search = (not query) or (query in name_local.lower())

            if matches_cat and matches_search:
                filtered_items.append((rhythm_id, name_local))

        # Sort alphabetically according to the active language's name
        filtered_items.sort(key=lambda item: self._normalize_sort_key(item[1]))

        for rhythm_id, name_local in filtered_items:
            self.visible_keys.append(rhythm_id)
            self.listbox.insert(tk.END, f"  {name_local}")

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

        self.lbl_rhythm_title.config(text=locale_info["name"])
        self.badge_origin.config(text=f"{self._tr('origin_label')}: {locale_info['category']}")
        self.badge_sig.config(text=f"{self._tr('sig_label')}: {data['time_signature']}")
        self.lbl_description.config(text=locale_info["description"])

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
        self._reset_cards()

    def _reset_cards(self):
        for card in self.step_cards:
            card.set_active(False)

    def _highlight_step(self, index, session_id):
        if not self.is_playing or session_id != self.play_session_id:
            return
        for i, card in enumerate(self.step_cards):
            card.set_active(i == index)

    def _get_step_interval(self, bpm_val, time_sig, total_steps):
        seconds_per_beat = 60.0 / bpm_val
        if time_sig in ["2/4", "4/4"]:
            factor = 0.25 if (time_sig == "2/4" and total_steps == 8) else 0.5
            return seconds_per_beat * factor
        elif time_sig in ["3/4", "6/8", "12/8"]:
            return seconds_per_beat / 3.0 if total_steps == 6 else seconds_per_beat
        return seconds_per_beat * 0.5

    def _metronome_loop(self, session_id):
        data = RHYTHMS[self.current_rhythm_id]
        sounds = data["sounds"]
        counts = data["count"]
        total_steps = len(sounds)
        time_sig = data["time_signature"]
        step = 0

        next_tick_time = time.perf_counter()

        while self.is_playing and session_id == self.play_session_id:
            if self.sound_mode.get() == "metronome":
                # Click only on main beat numbers ("1", "2", "3", "4", etc.)
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
            step = (step + 1) % total_steps

            now = time.perf_counter()
            remaining = next_tick_time - now

            if remaining < -0.1:
                next_tick_time = now
            elif remaining > 0.002:
                time.sleep(remaining - 0.0015)

            while self.is_playing and session_id == self.play_session_id and time.perf_counter() < next_tick_time:
                pass


if __name__ == "__main__":
    root = tk.Tk()
    app = RhythmMasterApp(root)
    root.mainloop()
