# Radiation Monitor Survey 2026

Compile `main.tex` from this directory:

```sh
latexmk -pdf main.tex
```

`Header.tex` contains the shared report style and detector-technology colour
definitions. Report content is organised under `chapters/`; conclusions,
appendices and references are separate inputs. The former monolithic filename is
retained as a compatibility entry point.

The detector colour convention is:

- blue: silicon telescope;
- orange: pixel detector;
- light green: scintillator;
- green: hybrid silicon--scintillator;
- purple: dosimetry/TEPC;
- yellow: neutral-particle converter;
- grey: magnetic, ToF or mixed/other technology.

Chronology is not encoded by cell colour. Post-2023 instrument names use a separate
bold purple text cue.
