# Galaxy Dynamics Correction (GDC) — Dynamical History Experiment

**Status:** exploratory numerical experiment (27 October 2026). Not peer-reviewed and not a fit to astronomical observations.

## Question
Can transient, rotating gravitational disturbances leave persistent changes in stellar orbital angular momentum, and affect simplified present-day velocity-based mass indicators?

## Experiment
- 24,000 *test-particle orbits* in total (5 random seeds × 4 histories × 1,200 test stars).
- 3 Gyr integration in the same axisymmetric logarithmic background potential.
- Four histories: unperturbed, short transient perturbation, longer transient perturbation, two transient perturbations.
- Stellar self-gravity, hydrodynamics and baryonic feedback are **not** included.

## Results
| History | Mean absolute guiding-radius shift | Fraction shifted > 0.5 kpc |
| --- | ---: | ---: |
| No disturbance | 0.000 kpc | 0.0% |
| Short episode | 0.366 kpc | 23.8% |
| Long episode | 0.359 kpc | 22.1% |
| Two episodes | 0.919 kpc | 61.6% |

A simplified squared-mean-tangential-velocity proxy differs by up to **+5.0 percentage points locally** at 13 kpc in these test configurations. This is **not** a measured dark-matter mass bias.

## Reproduce
Requires Python 3.10+ and NumPy.

```bash
python -m pip install -r requirements.txt
python tutkimus.py
```

Outputs: `migraatio.csv` and `radat.csv`; see `LOPPURAPORTTI.md` for assumptions, definitions, limitations and references.

## Limitations
- Prescribed background potential already supports approximately 200 km/s rotation; it is not computed self-consistently from baryons.
- Angular momentum exchange with a prescribed non-axisymmetric perturbation; no fully self-consistent mass or energy budget.
- No stellar self-gravity, gas, magnetic fields or stellar feedback.
- Different stars can occupy the same final radial bin across histories.
- No actual galaxy dataset was fitted; this study cannot establish whether dark matter is present or absent.

## Research context
Sellwood & Binney (2002), *Radial mixing in galactic discs*: https://doi.org/10.1046/j.1365-8711.2002.05806.x

Antoja et al. (2018), *A dynamically young and perturbed Milky Way disk*: https://doi.org/10.1038/s41586-018-0510-7

## Attribution
Research concept and numerical exploration: project author. Computational assistance: OpenAI ChatGPT. Independently check and validate code/results before scholarly citation.
