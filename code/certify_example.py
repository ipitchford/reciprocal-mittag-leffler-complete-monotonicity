#!/usr/bin/env python3
"""Exact rational enclosure of a Mittag-Leffler complex-modulus counterexample.

Python standard library only. All proof inequalities use integers/Fraction.
Decimal strings are outward rounded rational interval endpoints.

The identities used for the Gamma constants are:
  M = AGM(1, 1/sqrt(2)), Gamma(1/4)^2 = 2*pi^(3/2)/M,
  Gamma(7/4) = (3/4)*pi*sqrt(2)/Gamma(1/4).
See NIST DLMF 19.8.5, 22.20 Example 1, and 5.4.5.
Pi is enclosed by Machin's formula and alternating arctangent series.
Gamma-series terms are split into even and odd n, giving rational recurrences.
The unused tails have explicit decreasing-ratio geometric bounds.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt

def require(condition, message):
    if not condition:
        raise SystemExit('CHECK FAILED: ' + message)


Q = 10 ** 80


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    def __post_init__(self):
        require(self.lo <= self.hi, 'line 29: self.lo <= self.hi')

    @staticmethod
    def exact(x):
        x = F(x)
        return I(x, x)

    def __add__(self, other):
        if not isinstance(other, I):
            other = I.exact(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        if not isinstance(other, I):
            other = I.exact(other)
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, I):
            other = I.exact(other)
        xs = [x*y for x in (self.lo, self.hi)
              for y in (other.lo, other.hi)]
        return I(min(xs), max(xs))

    __rmul__ = __mul__

    def inv(self):
        require(self.lo > 0 or self.hi < 0, 'line 61: self.lo > 0 or self.hi < 0')
        return I(1/self.hi, 1/self.lo)

    def __truediv__(self, other):
        if not isinstance(other, I):
            other = I.exact(other)
        return self * other.inv()

    def rounded(self):
        low = self.lo.numerator * Q // self.lo.denominator
        high = -((-self.hi.numerator * Q) // self.hi.denominator)
        return I(F(low, Q), F(high, Q))

    def sqrt(self):
        require(self.lo >= 0, 'line 75: self.lo >= 0')
        low = isqrt(self.lo.numerator * Q * Q // self.lo.denominator)
        high = isqrt(self.hi.numerator * Q * Q // self.hi.denominator) + 1
        require(F(low*low, Q*Q) <= self.lo, 'line 78: F(low*low, Q*Q) <= self.lo')
        require(F(high*high, Q*Q) >= self.hi, 'line 79: F(high*high, Q*Q) >= self.hi')
        return I(F(low, Q), F(high, Q))

    def square(self):
        if self.lo >= 0:
            return I(self.lo*self.lo, self.hi*self.hi)
        if self.hi <= 0:
            return I(self.hi*self.hi, self.lo*self.lo)
        return I(F(0), max(self.lo*self.lo, self.hi*self.hi))


def atan_reciprocal(d, terms=120):
    """Alternating-series enclosure; d>=2, terms even."""
    require(terms % 2 == 0 and d >= 2, 'line 92: terms % 2 == 0 and d >= 2')
    s = sum((F((-1)**k, (2*k+1)*d**(2*k+1))
             for k in range(terms)), F(0))
    next_term = F(1, (2*terms+1)*d**(2*terms+1))
    return I(s, s+next_term)


def gamma_reciprocals():
    pi = (16*atan_reciprocal(5) - 4*atan_reciprocal(239)).rounded()
    sqrt2 = I.exact(2).sqrt()
    a, b = I.exact(1), sqrt2.inv().rounded()
    for _ in range(10):
        a, b = ((a+b)/2).rounded(), (a*b).sqrt()
    # Exact AGM lies between its geometric and arithmetic iterates.
    agm = I(b.lo, a.hi)
    g14 = (2*pi*pi.sqrt()/agm).sqrt()
    inv14 = g14.inv().rounded()
    inv74 = (4*g14/(3*pi*sqrt2)).rounded()
    return pi, g14, inv14, inv74


def cmul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def rational_split(z, parity, terms=100):
    """Return rational finite sum and absolute tail bound without Gamma factor."""
    z = F(z[0]), F(z[1])
    z2 = cmul(z, z)
    r2 = z[0]*z[0]+z[1]*z[1]
    # |z| <= |Re z|+|Im z|, exact rational bound.
    r = abs(z[0])+abs(z[1])
    v = F(1+6*parity, 4)
    term = z if parity else (F(1), F(0))
    summation = (F(0), F(0))
    denprod = F(1)
    for _ in range(terms):
        summation = summation[0]+term[0], summation[1]+term[1]
        den = v*(v+1)*(v+2)
        denprod *= den
        raw = cmul(term, z2)
        term = raw[0]/den, raw[1]/den
        v += 3
    ratio = r2/(v*(v+1)*(v+2))
    require(0 <= ratio < 1, 'line 136: 0 <= ratio < 1')
    tail = r2**terms*(r if parity else 1)/denprod/(1-ratio)
    return summation, tail


def mittag(z, inv14, inv74, terms=100):
    out = [I.exact(0), I.exact(0)]
    error = F(0)
    for parity, invgamma in [(0, inv14), (1, inv74)]:
        summation, tail = rational_split(z, parity, terms)
        for j in (0, 1):
            out[j] += summation[j]*invgamma
        error += tail*invgamma.hi
    for j in (0, 1):
        out[j] = (out[j] + I(-error, error)).rounded()
    return out, error


def decimal_bound(q, places, upwards):
    scale = 10**places
    n = (-((-q.numerator*scale)//q.denominator) if upwards
         else (q.numerator*scale//q.denominator))
    sign = '-' if n < 0 else ''
    n = abs(n)
    return f'{sign}{n//scale}.{n%scale:0{places}d}'


def show(label, x, places=24):
    print(f'{label}: [{decimal_bound(x.lo, places, False)}, '
          f'{decimal_bound(x.hi, places, True)}]')


def main():
    pi, g14, inv14, inv74 = gamma_reciprocals()
    real_value, real_tail = mittag((-60, 0), inv14, inv74)
    complex_value, complex_tail = mittag((-60, 1), inv14, inv74)
    difference = (real_value[0].square()
                  - complex_value[0].square()
                  - complex_value[1].square())
    require(real_value[0].lo > 0, 'line 175: real_value[0].lo > 0')
    require(difference.lo > F(3, 10**8), 'line 176: difference.lo > F(3, 10**8)')
    require(difference.hi < F(4, 10**8), 'line 177: difference.hi < F(4, 10**8)')
    require(real_tail < F(1, 10**240), 'line 178: real_tail < F(1, 10**240)')
    require(complex_tail < F(1, 10**240), 'line 179: complex_tail < F(1, 10**240)')
    show('pi', pi)
    show('Gamma(1/4)', g14)
    show('E_{3/2,1/4}(-60)', real_value[0])
    show('Re E_{3/2,1/4}(-60+i)', complex_value[0])
    show('Im E_{3/2,1/4}(-60+i)', complex_value[1])
    show('E(-60)^2 - |E(-60+i)|^2', difference)
    print('PASS: exact rational enclosures prove E(-60)>0 and squared gap >3e-8.')
    print('PASS: both analytic series tails are bounded by 10^-240.')
    print('This finite certificate does not prove the unrestricted complete-monotonicity theorem.')


if __name__ == '__main__':
    main()
