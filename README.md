# Rhythm Master — Interactive Strumming & Rhythm Trainer for macOS

**Rhythm Master** is a native macOS desktop application built with Python and Tkinter to help guitarists and musicians practice strumming patterns, subdivisions, and rhythmic grooves—featuring a comprehensive library of **Brazilian rhythms** alongside essential international styles.

![](screenshot-1.png)

---

## Features

- **3 Switchable Audio Engines:**
  - **Acoustic Guitar (Karplus-Strong Physical Modeling):** Synthesizes realistic plucked/strummed acoustic guitar strings in pure Python (Bass/Thumb, Treble/Fingers, Upstroke, and Palm Mute/Slap) with zero external audio files.
  - **Percussion:** Synthesized kick, snare, hi-hat, and rim/slap grooves.
  - **Metronome:** Crisp woodblock-style clicks marking main beats with an accented Beat 1.
- **Zero-Latency Native macOS Audio:** Pre-loads synthesized WAV buffers into RAM via `AppKit.NSSound` (CoreAudio) with a round-robin voice pool and a drift-free monotonic clock (`time.perf_counter()`).
- **Rich Rhythm Library (27+ Patterns):**
  - **Brazilian Rhythms:** Traditional Samba, Bossa Nova, Partido Alto, Pagode, Baião, Xote, Arrasta-pé, Maracatu, Frevo, Ijexá, Axé / Samba-Reggae, Choro, Maxixe, Carimbó, Vanerão, Chamamé, Moda de Viola, Carioca Funk (Tamborzão), and Brega.
  - **General / International:** Pop/Rock, Ballad/Folk, Waltz (3/4), Guarânia, Reggae (Offbeat), Blues Shuffle (12/8), Funk/Groove (16th-note syncopation), and Bolero.
- **Bilingual UI (PT / EN):** Instant live switching between Portuguese and English, including locale-aware alphabetical sorting and real-time search.
- **Responsive Visual Beat Grid:** Color-coded subdivision cards that scale dynamically and highlight in sync with the audio engine.
- **Native `.app` Bundling:** Includes `py2app` configuration and a `Makefile` to build and install a standalone macOS `.app` bundle.

---

## Project Structure

    ├── main.py            # Main GUI, audio synthesizer engine, and precision metronome loop
    ├── rhythms_db.py      # Bilingual database of general and Brazilian rhythmic patterns
    ├── setup.py           # py2app configuration for macOS .app bundling
    ├── requirements.txt   # Packaging and macOS Cocoa framework dependencies
    ├── Makefile           # Automation for setup, running, building, and installing
    └── README.md

---

## Requirements

- **macOS** (Apple Silicon or Intel)
- **Python 3.10+** (with Tcl/Tk support; via Homebrew: `brew install python-tk@3.14`)

---

## Quick Start

Using the included `Makefile`:

1. **Set up the virtual environment and install dependencies:**

       make setup

2. **Run the application in development mode:**

       make run

3. **Build the standalone macOS `.app` bundle:**

       make build

   The compiled app will be generated at `dist/Rhythm Master.app`.

4. **Install directly into `/Applications`:**

       make install

5. **Clean build artifacts or virtual environment:**

       make clean-build   # Removes build/ and dist/
       make clean         # Removes build/, dist/, venv/, and __pycache__/

---

## Keyboard Shortcuts & Controls

- **`Spacebar`:** Start / Stop playback.
- **`−` / `+` or Slider:** Adjust tempo between `40` and `200 BPM` in real time.
- **Top Bar Switches:** Toggle seamlessly between **Guitar / Percussion / Metronome** and **EN / PT** without interrupting playback.

---

## How the Guitar Synthesis Works

Instead of bundling static `.wav` or `.mp3` assets, `MacNativeAudioEngine` generates all acoustic guitar strokes on startup using the **Karplus-Strong string synthesis algorithm**:

- Each string is initialized with a zero-mean filtered noise burst and passed through a low-pass delay-line feedback loop.
- Downstrokes (`↓(B)`, `↓(T)`) and upstrokes (`↑`) mix multiple chord frequencies with realistic millisecond strum offsets.
- Percussive slaps (`↓(S)`) combine rapidly damped strings with a low-frequency wooden body resonance.

---

## License

MIT License — feel free to use, modify, and share.