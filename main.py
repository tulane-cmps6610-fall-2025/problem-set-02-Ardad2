"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time


# For printing the results.
try:
    import tabulate
except Exception:
    tabulate = None


class BinaryNumber:

    #store the decimal value as well as the bit vector.
    
    def __init__(self, n):
        self.decimal_val = int(n)
        self.binary_vec = list('{0:b}'.format(self.decinal_val)) if False else list('{0:b}'.format(self.decimal_val))

    def __repr__(self):
        return ('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec):
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)

def pad(x, y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y) - len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x) - len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x, y


# Grade-school (quadratic work) multiplication. Split/shift/add; returns a bit-vector.
def quadratic_multiply(x, y):

    #4 recursive products + linear time to combine. 

    # 

    # Product of 0 will always be 0.
    if x.decimal_val == 0 or y.decimal_val == 0:
        return ['0']

    #  Before padding, make sure to avoid inflating 1-bit x 1-bit to 2 bits and cause endless reucrsion.
    if len(x.binary_vec) == 1 and len(y.binary_vec) == 1:
        return ['1'] if (x.binary_vec[0] == '1' and y.binary_vec[0] == '1') else ['0']

    # Padding, equalize the lengths, make them even, and then split them.
    X, Y = pad(x.binary_vec, y.binary_vec)
    n = len(X)
    m = n // 2

    # Split into left and right halves.s
    xL, xR = split_number(X)
    yL, yR = split_number(Y)

    # The four recursive products.
    xLyL = binary2int(quadratic_multiply(xL, yL)).decimal_val   # xL*yL
    xLyR = binary2int(quadratic_multiply(xL, yR)).decimal_val   # xL*yR
    xRyL = binary2int(quadratic_multiply(xR, yL)).decimal_val   # xR*yL
    xRyR = binary2int(quadratic_multiply(xR, yR)).decimal_val   # xR*yR

    # Combine them using bit shifts : (xLyL << 2m) + ((xLyR + xRyL) << m) + xRyR = (xL*2^m + xR)*(yL*2^m + yR).
    combined = (xLyL << (2 * m)) + ((xLyR + xRyL) << m) + xRyR
    return list('{0:b}'.format(combined))


# Karatsuba–Ofman (subquadratic work). Uses (xL+xR)(yL+yR) - xL*yL - xR*yR = xL*yR + xR*yL.
def subquadratic_multiply(x, y):

    #Invovles 3 recursive products and a linear time for combination.

    #Product of 0 is 0.
    if x.decimal_val == 0 or y.decimal_val == 0:
        return ['0']

    #  Before padding, make sure to avoid inflating 1-bit x 1-bit to 2 bits and cause endless reucrsion.
    if len(x.binary_vec) == 1 and len(y.binary_vec) == 1:
        return ['1'] if (x.binary_vec[0] == '1' and y.binary_vec[0] == '1') else ['0']

    # Padding, equalize the lengths, make them even, and then split them.

    X, Y = pad(x.binary_vec, y.binary_vec)
    n = len(X)
    m = n // 2

    xL, xR = split_number(X)
    yL, yR = split_number(Y)

    # The two diagonal products.
    xLyL = binary2int(subquadratic_multiply(xL, yL)).decimal_val    # xL*yL  (high*high)
    xRyR = binary2int(subquadratic_multiply(xR, yR)).decimal_val    # xR*yR  (low*low)

    # pThe product of sums needed to recover the cross term.
    sum_x = BinaryNumber(xL.decimal_val + xR.decimal_val)
    sum_y = BinaryNumber(yL.decimal_val + yR.decimal_val)
    sum_prod = binary2int(subquadratic_multiply(sum_x, sum_y)).decimal_val  # (xL+xR)*(yL+yR)

    # cross term = xL*yR + xR*yL.
    cross_mix = sum_prod - xLyL - xRyR

    #Shift and add operations to get the result.

    combined = (xLyL << (2 * m)) + (cross_mix << m) + xRyR
    return list('{0:b}'.format(combined))


## Feel free to add your own tests here.
def test_multiply():
    # compare decimal values so the assert is meaningful
    assert binary2int(quadratic_multiply(BinaryNumber(2), BinaryNumber(2))).decimal_val == 2 * 2
    assert binary2int(subquadratic_multiply(BinaryNumber(2), BinaryNumber(2))).decimal_val == 2 * 2


# timing functions for cmoparison
def time_multiply(x, y, f):
    t0 = time.perf_counter()
    f(x, y)
    return (time.perf_counter() - t0) * 1000.0  # Convert to ms

def compare_multiply():

    #Compare time vs bit length. n = number of bits.

    #Use the worst case b-bit inputs (2^b - 1), allowing the hslves to stay full after splittingand making the recursion depth match a tree model.

    res = []
    for nbits in [8, 12, 16, 20, 24, 28, 32, 40, 48, 56, 64]:
        x = BinaryNumber((1 << nbits) - 1)
        y = BinaryNumber((1 << nbits) - 1)
        qtime = time_multiply(x, y, quadratic_multiply)
        subqtime = time_multiply(x, y, subquadratic_multiply)
        speedup = qtime / subqtime if subqtime > 0 else float("inf")
        res.append((nbits, qtime, subqtime, speedup))
    print_results(res)

def print_results(results):

    #Try to tabulate the results if possible for better aesthetics.
    print("\n")
    try:
        import tabulate
        print(tabulate.tabulate(
            results,
            headers=['bits', 'quadratic (ms)', 'subquadratic (ms)', 'speedup (q/subq)'],
            floatfmt=".3f",
            tablefmt="github"))
    except Exception:
        print(" bits | quadratic (ms) | subquadratic (ms) | speedup (q/subq)")
        for b, q, s, r in results:
            print(f"{b:>5d} | {q:>14.3f} | {s:>17.3f} | {r:>15.2f}")


if __name__ == "__main__":
    test_multiply()
    compare_multiply()
