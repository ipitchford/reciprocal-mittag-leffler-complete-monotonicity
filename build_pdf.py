"""Build manuscript.pdf from manuscript.md: pandoc -> LaTeX -> tectonic (XeTeX)."""
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parent; B=ROOT/'build'
text=(ROOT/'manuscript.md').read_text().split('\n',1)[1].lstrip()
title='Reciprocal Mittag--Leffler functions: complete monotonicity below the parameter band, and the exact boundary near order two'
(B/'m.md').write_text('---\ntitle: "'+title+'"\nauthor: "Anonymous"\ndate: "Version 0.1.0-candidate, 4 November 2026. Zenodo DOI [10.5281/zenodo.23934934](https://doi.org/10.5281/zenodo.23934934) (all versions: [10.5281/zenodo.23934933](https://doi.org/10.5281/zenodo.23934933))."\n---\n\n'+text)
cmd=['pandoc',str(B/'m.md'),'-f','markdown+tex_math_single_backslash+autolink_bare_uris','-s','--shift-heading-level-by=-1','-V','documentclass=article','-V','fontsize=11pt','-V','geometry:margin=25mm','-V','papersize=a4','-V','colorlinks=true','-V','urlcolor=teal','-V','linkcolor=black','--include-in-header='+str(B/'header.tex'),'-o',str(B/'manuscript.tex')]
r=subprocess.run(cmd,capture_output=True,text=True)
if r.returncode: raise SystemExit(r.stderr)
r=subprocess.run(['tectonic','--keep-logs','-o',str(B),str(B/'manuscript.tex')],capture_output=True,text=True)
if r.returncode: raise SystemExit(r.stdout[-3000:]+r.stderr[-3000:])
(ROOT/'manuscript.pdf').write_bytes((B/'manuscript.pdf').read_bytes()); print('ok')
