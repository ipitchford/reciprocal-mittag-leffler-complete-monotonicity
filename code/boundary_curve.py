"""Numerical boundary curve b(alpha): continuation of the double negative zero
E_{alpha,b}(x)=d/dx E_{alpha,b}(x)=0 from (alpha,b,x)=(2,3,-4 pi^2).
Exploratory high-precision numerics (mpmath); NOT a proof or certified radius.
Fails (nonzero exit) if any check fails; does not rely on assert."""
import sys, json
import mpmath as mp
mp.mp.dps = 40

def E(a, b, z, d=0):
    s = mp.mpf(0); k = d
    while True:
        c = mp.ff(k, d) * mp.power(z, k - d) * mp.rgamma(a*k + b)
        s += c
        if k > 60 and abs(c) < mp.mpf(10)**(-45) * (1 + abs(s)):
            return s
        k += 1

def solve(a, b0, x0):
    f = lambda b, x: [E(a, b, x), E(a, b, x, 1)]
    return mp.findroot(f, (b0, x0))

def main():
    fail = []
    a2 = 2*mp.pi
    I = mp.quad(lambda u: (1-mp.cos(u))/u, [0, a2]); Si = mp.si(a2)
    slope = 1 + a2*Si/(2*I)
    rows = []
    for direction in (+1, -1):
        b, x = mp.mpf(3), -a2**2
        prev = None
        for i in range(1, 51):
            a = 2 + direction*mp.mpf(i)/100
            if prev is not None:
                b, x = 2*b - prev[0], 2*x - prev[1]
            pb, px = b, x
            b, x = solve(a, b, x)
            prev = (pb, px) if prev is None else (rows[-1][1], rows[-1][2]) if rows else None
            prev = (b, x)
            rows.append((a, b, x))
    rows.sort()
    # tangent check by central difference
    r = {float(a): (b, x) for a, b, x in rows}
    fd = (r[2.01][0] - r[1.99][0]) / mp.mpf('0.02')
    print('closed-form b\'(2) =', mp.nstr(slope, 20))
    print('central difference =', mp.nstr(fd, 12))
    if abs(fd - slope) > 1e-3: fail.append('tangent mismatch')
    # beta=alpha band edge check: b(alpha) > alpha on the computed range below 2
    for a, b, x in rows:
        if a < 2 and not (b > a): fail.append('b<=alpha at %s' % a)
        if E(a, b, x, 2) <= 0: fail.append('not a minimum at %s' % a)
    out = [{'alpha': mp.nstr(a, 4), 'b': mp.nstr(b, 15), 'x': mp.nstr(x, 15)} for a, b, x in rows]
    json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else 'boundary_curve.json', 'w'), indent=1)
    for a, b, x in rows[::10] + [rows[-1]]:
        print(mp.nstr(a, 3), mp.nstr(b, 12), mp.nstr(x, 12))
    if fail:
        print('FAIL', fail); sys.exit(1)
    print('PASS: continuation consistent with exact tangent; b(alpha)>alpha on computed alpha<2.')

main()
