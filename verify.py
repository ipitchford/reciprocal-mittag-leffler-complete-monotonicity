"""Run all finite checks for the reciprocal Mittag-Leffler release and write one JSON record.

Usage: python -I -B [-O] verify.py --output results.json
Runs code/verify_mittag_boundary.py (standard library), code/certify_example.py (exact rational
certificate, standard library) and code/boundary_curve.py (mpmath continuation of the double-zero
curve). Every check raises on failure (no assert), so python -O does not disable it. A negative control
corrupts one exact constant and requires the checker to fail. Finite checks only: the theorems rest on
the written proofs in manuscript.pdf.
"""
import json, subprocess, sys, tempfile, hashlib
from pathlib import Path
HERE = Path(__file__).resolve().parent
def fail(msg): raise SystemExit('VERIFY FAILED: ' + msg)
def run(script, *args, cwd=None):
    flags = ['-I', '-B'] + (['-O'] if sys.flags.optimize else [])
    r = subprocess.run([sys.executable] + flags + [str(script)] + list(args), capture_output=True, text=True, cwd=cwd)
    return r.returncode, r.stdout
def stable(text):
    return [l for l in text.splitlines() if not l.startswith(('Elapsed seconds', 'Python:'))]
out = None
if '--output' in sys.argv: out = Path(sys.argv[sys.argv.index('--output') + 1])
res = {'status': None, 'optimized_mode': bool(sys.flags.optimize), 'checks': {}}
code, txt = run(HERE / 'code' / 'verify_mittag_boundary.py')
if code != 0 or 'High-precision slope and derivative consistency: PASS' not in txt: fail('boundary tangent checks')
res['checks']['boundary_tangent'] = stable(txt)
code, txt = run(HERE / 'code' / 'certify_example.py')
if code != 0 or 'PASS: exact rational enclosures' not in txt: fail('modulus certificate')
res['checks']['modulus_certificate'] = stable(txt)
with tempfile.TemporaryDirectory() as td:
    jp = Path(td) / 'curve.json'
    code, txt = run(HERE / 'code' / 'boundary_curve.py', str(jp))
    if code != 0 or 'PASS: continuation' not in txt: fail('boundary curve')
    curve = json.loads(jp.read_text())
    shipped = json.loads((HERE / 'code' / 'boundary_curve.json').read_text())
    if curve != shipped: fail('boundary curve differs from shipped code/boundary_curve.json')
    res['checks']['boundary_curve'] = stable(txt) + ['curve sha256 ' + hashlib.sha256(jp.read_bytes()).hexdigest()]
    # negative control: a corrupted exact constant must be rejected
    bad = Path(td) / 'neg.py'
    bad.write_text((HERE / 'code' / 'verify_mittag_boundary.py').read_text().replace('Q(7,360)', 'Q(7,361)', 1))
    code, _ = run(bad)
    if code == 0: fail('negative control was not rejected')
    res['checks']['negative_control'] = ['corrupted coefficient 7/360 -> 7/361 rejected (nonzero exit)']
res['status'] = 'all checks passed'
res.pop('optimized_mode')
text = json.dumps(res, indent=1) + '\n'
if out: out.write_text(text)
print(res['status'])
