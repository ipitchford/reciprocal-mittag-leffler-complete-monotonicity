"""Independent finite checks for the Mittag--Leffler boundary manuscript.

Python standard library only. These exact algebra and high-precision numerical
checks are not a proof of the universal analytic theorem or a certified radius.
"""
from decimal import Decimal as D, getcontext
from fractions import Fraction as Q
from math import factorial
import platform
import time

def require(condition, message):
    if not condition:
        raise SystemExit('CHECK FAILED: ' + message)



def reciprocal_coefficients(a):
    b = [1 / a[0]]
    for n in range(1, len(a)):
        b.append(-sum(a[k] * b[n-k] for k in range(1, n+1)) / a[0])
    return b


def exact_checks():
    e22 = [Q(1, factorial(2*n+1)) for n in range(7)]
    e23 = [Q(2, factorial(2*n+2)) for n in range(7)]
    r22 = reciprocal_coefficients(e22)
    r23 = reciprocal_coefficients(e23)
    require(r22[:5] == [Q(1), -Q(1,6), Q(7,360), -Q(31,15120), Q(127,604800)], 'line 25: r22[:5] == [Q(1), -Q(1,6), Q(7,360), -Q(31,15120), Q(127,604800)]')
    require(r23[:4] == [Q(1), -Q(1,12), Q(1,240), -Q(1,6048)], 'line 26: r23[:4] == [Q(1), -Q(1,12), Q(1,240), -Q(1,6048)]')
    require(all((-1)**n * c > 0 for n,c in enumerate(r22)), 'line 27: all((-1)**n * c > 0 for n,c in enumerate(r22))')
    require(all((-1)**n * c > 0 for n,c in enumerate(r23)), 'line 28: all((-1)**n * c > 0 for n,c in enumerate(r23))')
    print('Exact reciprocal series at (2,2), degrees 0..6:', ', '.join(map(str,r22)))
    print('Exact reciprocal series at (2,3), degrees 0..6:', ', '.join(map(str,r23)))
    # R(2,beta)>=2 is equivalent to beta^2-3 beta-6<=0.
    for b in (Q(1,2),Q(1),Q(2),Q(3),Q(4),Q(9,2),Q(5)):
        ratio = (b+2)*(b+3)/(b*(b+1))
        require(ratio-2 == -(b*b-3*b-6)/(b*(b+1)), 'line 34: ratio-2 == -(b*b-3*b-6)/(b*(b+1))')
    print('Exact gamma-ratio polynomial identity: PASS (7 rational evaluations)')
    print('Anchor kernel integrals: (2,2) = 1/6; (2,3) = 1/12 (zeta(2) identity).')


def atan_inverse(n):
    x = D(1)/n
    term = x
    total = D(0)
    for k in range(2500):
        add = term / (2*k+1)
        total += add
        if abs(add) < D('1e-95'):
            return total
        term *= -x*x
    raise AssertionError('atan did not converge')


def high_precision_checks():
    getcontext().prec = 90
    pi = 16*atan_inverse(5)-4*atan_inverse(239)
    a = 2*pi
    z = -a*a
    integral_i = sum(((-1)**(k+1)*a**(2*k)/D((2*k)*factorial(2*k)) for k in range(1,151)), D(0))
    integral_si = sum(((-1)**k*a**(2*k+1)/D((2*k+1)*factorial(2*k+1)) for k in range(151)), D(0))
    # psi(2n+3)=H_(2n+2)-gamma; gamma terms cancel because E=E'=0
    # at the exact anchor. Direct finite series independently check that fact.
    harmonic = [D(0)]
    for k in range(1,303):
        harmonic.append(harmonic[-1]+D(1)/k)
    e = ep = epp = beta_derivative = alpha_derivative = D(0)
    for n in range(151):
        den = D(factorial(2*n+2))
        term = z**n/den
        e += term
        beta_derivative -= harmonic[2*n+2]*term
        alpha_derivative -= n*harmonic[2*n+2]*term
        if n:
            ep += n*z**(n-1)/den
        if n>=2:
            epp += n*(n-1)*z**(n-2)/den
    beta_formula = integral_i/(a*a)
    alpha_formula = -beta_formula-integral_si/(2*a)
    slope_integral = 1+a*integral_si/(2*integral_i)
    slope_series = -alpha_derivative/beta_derivative
    errors = {
        'anchor E':abs(e), 'anchor Eprime':abs(ep),
        'Esecond':abs(epp-1/(4*a**4)),
        'beta derivative':abs(beta_derivative-beta_formula),
        'alpha derivative':abs(alpha_derivative-alpha_formula),
        'slope formulas':abs(slope_integral-slope_series),
    }
    require(max(errors.values()) < D('1e-75'), "line 86: max(errors.values()) < D('1e-75')" + ' ' + str(errors))
    require(beta_derivative > 0 and alpha_derivative < 0, 'line 87: beta_derivative > 0 and alpha_derivative < 0')
    print('Decimal working precision: 90; Mittag--Leffler terms: 151; integral terms: 150/151.')
    for name,value in [('I(2pi)',integral_i),('Si(2pi)',integral_si),('partial_beta E',beta_derivative),('partial_alpha E',alpha_derivative),('bprime(2)',slope_integral)]:
        print(name+' = '+format(value,'.55f'))
    print('Maximum agreement error:',max(errors.values()))
    print('Parameter cap M =',format((3+D(33).sqrt())/2,'.25f'))
    print('High-precision slope and derivative consistency: PASS')
    print('LIMIT: no interval arithmetic, no certified parameter neighbourhood, no proof-assistant verification.')


if __name__ == '__main__':
    started = time.perf_counter()
    print('Python:',platform.python_version())
    exact_checks()
    high_precision_checks()
    print('Elapsed seconds:',round(time.perf_counter()-started,3))
