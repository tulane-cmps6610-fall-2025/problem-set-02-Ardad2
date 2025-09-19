# CMPS 6610 Problem Set 02
## Answers

**Name:** Arjun Dadhwal


Place all written answers from `assignment-01.md` here for easier grading.

1. Prove that $\log_2(n!) \in \Theta(n\log_2 n)$?

-----


Let $g(n) = \log_2(n!)$ and $f(n) = n\log_2 n$.  

To prove $\Theta$, we show **both** $g(n)\in O(f(n))$ and $g(n)\in \Omega(f(n))$ using the asymptotic dominance definitions.

#### **Big-O:** Is $\log_2(n!) \in O(n\log_2 n)$?

- By the definition of Big-O, there must exist constants $c>0$ and $n_0>0$ such that:

$$
g(n) \le c \cdot f(n) \quad \forall n \ge n_0
$$

- **Substituting $g(n)$ and $f(n)$:**

$$
\log_2(n!) \le c \cdot n\log_2 n \quad \forall n \ge n_0
$$

- **Upper bound via product comparison (slide trick):** Since $n! \le n^n$,

(n * (n-1) * (n-2) ... * 1 <= (n * n * n))

$$
\log_2(n!) \le \log_2(n^n) = n\log_2 n = f(n)
$$

- **Dividing both sides by $f(n)>0$ to get potential values for $c$:**

$$
\frac{\log_2(n!)}{n\log_2 n} \le 1
$$

- **Choosing $c=1$ and $n_0=2$:**

$$
\log_2(n!) \le 1 \cdot n\log_2 n \quad \forall n \ge 2
$$

**Conclusion (Big-O):**

$$
\boxed{\log_2(n!) \in O(n\log_2 n)}
$$




### **2(a).** Derive an asymptotic upper bound for $T(n)=2T(n/6)+1$

- **Level $i$:** subproblem size is $n/6^i$. There are $2^i$ nodes, each with cost $1$.  
  **Cost at level $i$:**

$$
2^i
$$

- **Number of levels:** solve $n/6^L \le 1$.

$$
L = \lceil \log_6 n \rceil
$$

- **Total cost (sum of per-level costs):**

$$
T(n) \le \sum_{i=0}^{L} 2^i
= \frac{2^{L+1}-1}{2-1}
= 2^{L+1}-1
< 2 \cdot 2^{L}.
$$

- **Turn $2^{L}$ into a power of $n$:** since $L \le \log_6 n + 1$,

$$
2^{L} \le 2^{\log_6 n + 1}
= 2 \cdot 2^{\log_6 n}
= 2 \cdot n^{\log_6 2}.
$$

- **Upper bound:**

$$
T(n) < 2 \cdot 2^{L}
\le 2 \cdot \big(2 \cdot n^{\log_6 2}\big)
= 4 \cdot n^{\log_6 2}.
$$

**Conclusion (upper bound):**

$$
\boxed{T(n) \in O\big(n^{\log_6 2}\big)}
$$

### **2(b).** Derive an asymptotic upper bound for $T(n)=6T(n/4)+n$

- **Level $i$:** subproblem size is $n/4^i$. There are $6^i$ nodes; each node’s cost is $n/4^i$.  
  **Cost at level $i$:**

$$
6^i \cdot \frac{n}{4^i} \;=\; n\left(\frac{6}{4}\right)^i.
$$

- **Number of levels:** solve $n/4^L \le 1$.

$$
L = \lceil \log_4 n \rceil .
$$

- **Total cost:**

$$
T(n) \le \sum_{i=0}^{L} n\left(\frac{6}{4}\right)^i
= n \cdot \frac{(6/4)^{L+1}-1}{(6/4)-1}
= O\Big(n \cdot (6/4)^{L}\Big).
$$

- **Turn $(6/4)^{L}$ into a power of $n$:**

$$
\left(\frac{6}{4}\right)^{L}
\le \left(\frac{6}{4}\right)^{\log_4 n + 1}
= \frac{6}{4} \cdot n^{\log_4(6/4)}.
$$

- **Upper bound:**

$$
T(n) = O\Big(n \cdot n^{\log_4(6/4)}\Big)
= O\big(n^{1+\log_4(6/4)}\big)
= O\big(n^{\log_4 6}\big).
$$

**Conclusion (upper bound):**

$$
\boxed{T(n)\in O\big(n^{\log_4 6}\big)}
$$


### **2(c).** Derive an asymptotic upper bound for $T(n)=7T(n/7)+n$

- **Level $i$:** size $n/7^i$, nodes $7^i$, cost per node $n/7^i$.  
  **Cost at level $i$:**

$$
7^i \cdot \frac{n}{7^i} \;=\; n.
$$

- **Number of levels:**

$$
L = \lceil \log_7 n \rceil .
$$

- **Total cost:**

$$
T(n) \le \sum_{i=0}^{L} n = (L+1)\,n = O(n\log n).
$$

**Conclusion (upper bound):**

$$
\boxed{T(n)\in O(n\log n)}
$$


### **2(d).** Derive an asymptotic upper bound for $T(n)=9T(n/4)+n^2$

- **Level $i$:** size $n/4^i$, nodes $9^i$, cost per node $(n/4^i)^2$.  
  **Cost at level $i$:**

$$
9^i \cdot \left(\frac{n}{4^i}\right)^2 = n^2\left(\frac{9}{16}\right)^i.
$$

- **Number of levels:**

$$
L = \lceil \log_4 n \rceil .
$$

- **Total cost (geometric with ratio $9/16<1$):**

$$
T(n) \le \sum_{i=0}^{L} n^2\left(\frac{9}{16}\right)^i
< \frac{1}{1-\frac{9}{16}}\,n^2
= \frac{16}{7}\,n^2
= O(n^2).
$$

**Conclusion (upper bound):**

$$
\boxed{T(n)\in O(n^2)}
$$


### **2(e).** Derive an asymptotic upper bound for $T(n)=4T(n/2)+n^3$

- **Level $i$:** size $n/2^i$, nodes $4^i$, cost per node $(n/2^i)^3$.  
  **Cost at level $i$:**

$$
4^i \cdot \left(\frac{n}{2^i}\right)^3
= n^3 \left(\frac{1}{2}\right)^i.
$$

- **Number of levels:**

$$
L = \lceil \log_2 n \rceil .
$$

- **Total cost (ratio $1/2<1$):**

$$
T(n) \le \sum_{i=0}^{L} n^3\left(\frac{1}{2}\right)^i
< \frac{1}{1-\frac{1}{2}}\,n^3
= 2\,n^3
= O(n^3).
$$

**Conclusion (upper bound):**

$$
\boxed{T(n)\in O(n^3)}
$$


### **2(f).** Derive an asymptotic upper bound for $T(n)=49T(n/25)+n^{3/2}\log n$

- **Level $i$:** size $n/25^i$, nodes $49^i$, cost per node $(n/25^i)^{3/2}\log(n/25^i)$.  
  **Cost at level $i$ (using $\log(n/25^i)\le \log n$):**

$$
49^i \cdot \left(\frac{n}{25^i}\right)^{3/2}\log\left(\frac{n}{25^i}\right)
\le n^{3/2}\log n \left(\frac{49}{25^{3/2}}\right)^i
= n^{3/2}\log n \left(\frac{49}{125}\right)^i.
$$

- **Number of levels:**

$$
L = \lceil \log_{25} n \rceil .
$$

- **Total cost (ratio $49/125<1$):**

$$
T(n) \le \sum_{i=0}^{L} n^{3/2}\log n \left(\frac{49}{125}\right)^i
< \frac{1}{1-\frac{49}{125}}\,n^{3/2}\log n
= \frac{125}{76}\,n^{3/2}\log n
= O\big(n^{3/2}\log n\big).
$$

**Conclusion (upper bound):**

$$
\boxed{T(n)\in O\big(n^{3/2}\log n\big)}
$$


### **2(g).** Derive an asymptotic upper bound for $T(n)=T(n-1)+2$

- **Unroll $k$ steps:**

$$
T(n) = T(n-k) + 2k.
$$

- **Stop when $n-k=1$** (i.e., $k=n-1$):

$$
T(n) = T(1) + 2(n-1) = 2n + O(1).
$$

**Conclusion (upper bound):**

$$
\boxed{T(n)\in O(n)}
$$


### **2(h).** Derive an asymptotic upper bound for $T(n)=T(n-1)+n^c$, with $c\ge 1$

- **Unroll:**

$$
T(n) = T(1) + \sum_{k=1}^{n} k^c.
$$

- **Bound the sum:**

$$
\sum_{k=1}^{n} k^c = \Theta\big(n^{c+1}\big).
$$

**Conclusion (upper bound):**

$$
\boxed{T(n)\in O\big(n^{c+1}\big)}
$$


### **2(i).** Derive an asymptotic upper bound for $T(n)=T(\sqrt{n})+1$

- **Argument sizes as we recurse:**

$$
n \to \sqrt{n} \to n^{1/4} \to n^{1/8} \to \cdots \to n^{1/2^t}.
$$

- **Stop when the size is constant (say $\le 2$):**

$$
n^{1/2^t} \le 2
\Longleftrightarrow
\frac{\log n}{2^t} \le \log 2
\Longleftrightarrow
t \ge \log_2 \log_2 n.
$$

- **Each level adds $+1$**, so

$$
T(n) = O(t) = O(\log\log n).
$$

**Conclusion (upper bound):**

$$
\boxed{T(n)\in O(\log\log n)}
$$

----

### **3. Choosing among three divide-and-conquer algorithms (work & span)**


### **Algorithm A**

**Work**

- Recurrence:

$$
W_{\mathcal A}(n)=2\,W_{\mathcal A}(n/5)+c\,n^2.
$$

- **Per-level combine cost (tree):** at level $i$, there are $2^i$ nodes of size $n/5^i$, so

$$
\text{cost at level }i = 2^i \cdot c\left(\frac{n}{5^i}\right)^2
= c\,n^2\left(\frac{2}{25}\right)^i.
$$

- **Sum over levels** ($L=\lceil\log_5 n\rceil$):

$$
W_{\mathcal A}(n) \le \sum_{i=0}^{L} c\,n^2\left(\frac{2}{25}\right)^i
< \frac{1}{1-\frac{2}{25}}\,c\,n^2
= O(n^2).
$$

- **Lower bound:** the root combine already costs $\Omega(n^2)$.

**Conclusion (work):**

$$
W_{\mathcal A}(n)=\Theta(n^2).
$$

**Span**

- Recurrence (two subcalls in parallel):

$$
S_{\mathcal A}(n)=S_{\mathcal A}(n/5)+c\,n^2.
$$

- **Unroll (geometric decay in the recursive term):**

$$
S_{\mathcal A}(n) \le c\,n^2 \sum_{i=0}^{L}\left(\frac{1}{25}\right)^i
= O(n^2).
$$

- **Lower bound:** root combine gives $\Omega(n^2)$.

**Conclusion (span):**

$$
S_{\mathcal A}(n)=\Theta(n^2).
$$

### **Algorithm B**
**Work**

- Recurrence:

$$
W_{\mathcal B}(n)=W_{\mathcal B}(n-1)+c\log n.
$$

- **Unroll:**

$$
W_{\mathcal B}(n)=\sum_{k=1}^{n} c\log k
=\Theta(n\log n).
$$

**Span**

- Recurrence:

$$
S_{\mathcal B}(n)=S_{\mathcal B}(n-1)+c\log n.
$$

- **Unroll:**

$$
S_{\mathcal B}(n)=\Theta(n\log n).
$$


### **Algorithm C**

**Work**

- Recurrence:

$$
W_{\mathcal C}(n)=W_{\mathcal C}(n/3)+W_{\mathcal C}(2n/3)+c\,n^{1.1}.
$$

- **Per-level combine cost (tree):** at level $i$, node sizes are products of $(1/3)$ and $(2/3)$.  
  Summing the combine work over all nodes at level $i$ (binomial expansion):

$$
\text{cost at level }i
= c\,n^{1.1}\sum_{k=0}^{i}\binom{i}{k}\left(\frac{2}{3}\right)^{1.1k}\left(\frac{1}{3}\right)^{1.1(i-k)}
= c\,n^{1.1}\left[\left(\frac{2}{3}\right)^{1.1}+\left(\frac{1}{3}\right)^{1.1}\right]^i.
$$

Let $r=\left(\tfrac{2}{3}\right)^{1.1}+\left(\tfrac{1}{3}\right)^{1.1}<1$.

- **Sum over levels** ($L=\Theta(\log n)$, but ratio $r<1$ makes the sum constant-bounded):

$$
W_{\mathcal C}(n) \le c\,n^{1.1}\sum_{i=0}^{L} r^{i}
< \frac{c}{1-r}\,n^{1.1}
= O(n^{1.1}).
$$

- **Lower bound:** root combine gives $\Omega(n^{1.1})$.

**Conclusion (work):**

$$
W_{\mathcal C}(n)=\Theta(n^{1.1}).
$$

**Span**

- Recurrence (max over parallel branches):

$$
S_{\mathcal C}(n)=\max\{S_{\mathcal C}(n/3),\,S_{\mathcal C}(2n/3)\}+c\,n^{1.1}
= S_{\mathcal C}(2n/3)+c\,n^{1.1}.
$$

- **Unroll along the larger branch**:

$$
S_{\mathcal C}(n) \le c\,n^{1.1}\sum_{i=0}^{L}\left(\frac{2}{3}\right)^{1.1 i}
= O(n^{1.1}).
$$

- **Lower bound:** root combine $\Omega(n^{1.1})$.

**Conclusion (span):**

$$
S_{\mathcal C}(n)=\Theta(n^{1.1}).
$$


### **Choice**

Collecting the bounds:

- $\mathcal A$: $W=\Theta(n^2)$, $S=\Theta(n^2)$  
- $\mathcal B$: $W=\Theta(n\log n)$, $S=\Theta(n\log n)$  
- $\mathcal C$: $W=\Theta(n^{1.1})$, $S=\Theta(n^{1.1})$

**Algorithm B** has the smallest work and span, so it is asymptotically the best choice and will minimize the upper bound of the running time. For parallel time $T_P \le W/P + S$, minimizing $W$ is decisive for practical $P$, so B is the best choice.





### **4. Choosing among three divide-and-conquer algorithms (work & span)**


### **Algorithm A**

**Work**

- Recurrence:

$$
W_{\mathcal A}(n)=5\,W_{\mathcal A}(n/2)+c\,n.
$$

- **Cost at level $i$** (there are $5^i$ nodes of size $n/2^i$; per-node combine \(=c(n/2^i)\) ):

$$
5^i \cdot c\frac{n}{2^i} = c \cdot n\left(\frac{5}{2}\right)^i.
$$

- **Sum over levels** ($L=\lceil\log_2 n\rceil$):

$$
W_{\mathcal A}(n)\le c\,n\sum_{i=0}^{L}\left(\frac{5}{2}\right)^i
= c\,n\cdot\frac{(5/2)^{L+1}-1}{(5/2)-1}
=\Theta\big(n(5/2)^L\big).
$$

- **Turn $(5/2)^L$ into a power of $n$** (use $a^{\log_b n}=n^{\log_b a}$):

$$
(5/2)^L \le (5/2)^{\log_2 n+1}=\tfrac{5}{2}\,n^{\log_2(5/2)}.
$$

**Conclusion (work):**

$$
W_{\mathcal A}(n)=\Theta\big(n^{1+\log_2(5/2)}\big)=\Theta\big(n^{\log_2 5}\big).
$$

**Span**

- Recurrence (five equal subcalls in parallel):

$$
S_{\mathcal A}(n)=S_{\mathcal A}(n/2)+c\,n.
$$

- **Unroll:**

$$
S_{\mathcal A}(n)\le c\,n\sum_{i=0}^{L}\left(\tfrac{1}{2}\right)^i < 2c\,n = O(n).
$$

**Conclusion (span):**

$$
S_{\mathcal A}(n)=\Theta(n).
$$


### **Algorithm B$**
**Work**

- Recurrence:

$$
W_{\mathcal B}(n)=2\,W_{\mathcal B}(n-1)+c.
$$

- **Recursion tree** (level $i$ has $2^i$ nodes; about $n$ levels):

$$
W_{\mathcal B}(n)\ge c\sum_{i=0}^{n-1}2^i=c(2^n-1)=\Theta(2^n).
$$

**Conclusion (work):**

$$
W_{\mathcal B}(n)=\Theta(2^n).
$$

**Span**

- Recurrence (two size $n-1$ subcalls can run in parallel):

$$
S_{\mathcal B}(n)=S_{\mathcal B}(n-1)+O(1).
$$

- **Unroll:**

$$
S_{\mathcal B}(n)=\Theta(n).
$$

---

### **Algorithm C**

**Work**

- Recurrence:

$$
W_{\mathcal C}(n)=9\,W_{\mathcal C}(n/3)+c\,n^2.
$$

- **Cost at level $i$** (there are $9^i$ nodes of size $n/3^i$; per-node combine $(n/3^i)^2$):

$$
9^i \cdot c\left(\frac{n}{3^i}\right)^2=c\,n^2.
$$

- **Sum over levels** ($L=\lceil\log_3 n\rceil$):

$$
W_{\mathcal C}(n)\le \sum_{i=0}^{L} c\,n^2
= c\,n^2(L+1)=\Theta(n^2\log n).
$$

**Conclusion (work):**

$$
W_{\mathcal C}(n)=\Theta(n^2\log n).
$$

**Span**

- Recurrence (nine equal subcalls in parallel):

$$
S_{\mathcal C}(n)=S_{\mathcal C}(n/3)+c\,n^2.
$$

- **Unroll:**

$$
S_{\mathcal C}(n)\le c\,n^2\sum_{i=0}^{L}\left(\tfrac{1}{9}\right)^i
< \tfrac{9}{8}\,c\,n^2 = O(n^2).
$$

**Conclusion (span):**

$$
S_{\mathcal C}(n)=\Theta(n^2).
$$

---

### **Choice**

Summary:

- $\mathcal A$: $W=\Theta(n^{\log_2 5})\approx \Theta(n^{2.32})$, $S=\Theta(n)$  
- $\mathcal B$: $W=\Theta(2^n)$, $S=\Theta(n)$  
- $\mathcal C$: $W=\Theta(n^2\log n)$, $S=\Theta(n^2)$

**Algorithm C has the smallest **work** (sequential cost), minimizing W which will help decrease the upper bound of the running time. For parallel time $T_P \le W/P + S$, minimizing $W$ is decisive for practical $P$, so $\mathcal C$ is the best choice.


### **5. Integer multiplication (work, span, and empirical check)**

We analyze both algorithms **only** with the class methods: the **recursion tree** and the **brick method** (root/leaf-dominated). Logs are base 2.

---

### Grade School multiplication**


**Work**

- **Recurrence:**

Split both inputs in half and do **4** sub-multiplications of size $n/2$. Combines in **linear** time.

$$
W_{\mathcal A}(n)=4\,W_{\mathcal A}(n/2)+c\,n.
$$

- **Cost at level $i$** (there are $4^i$ nodes of size $n/2^i$; per-node combine \(=c(n/2^i)\)):

$$
4^i \cdot c\frac{n}{2^i} = c \cdot n \cdot 2^i.
$$

- **Sum over levels** ($L=\lceil\log_2 n\rceil$):

$$
W_{\mathcal A}(n)\le c\,n\sum_{i=0}^{L}2^i
= c\,n\cdot\frac{2^{L+1}-1}{2-1}
=\Theta\big(n\cdot 2^L\big).
$$

- **Turn $2^L$ into a power of $n$** (use $2^{\log_2 n}=n$):

$$
n\cdot 2^L=\Theta(n\cdot n)=\Theta(n^2).
$$

**Conclusion (work):**

$$
W_{\mathcal A}(n)=\Theta(n^2).
$$

**Span**

- **Recurrence (four equal subcalls in parallel):**

$$
S_{\mathcal A}(n)=S_{\mathcal A}(n/2)+c\,n.
$$

- **Unroll (geometric decay along the path):**

$$
S_{\mathcal A}(n)\le c\,(n+n/2+n/4+\cdots)=O(n).
$$

**Conclusion (span):**

$$
S_{\mathcal A}(n)=\Theta(n).
$$

### **Karatsuba–Ofman Multiplication**

Work

- **Recurrence:**
Use $(x_L+x_R)(y_L+y_R)-x_Ly_L-x_Ry_R=x_Ly_R+x_Ry_L$ to do **3** sub-multiplications of size $n/2$. Combine in **linear** time.

$$
W_{\mathcal B}(n)=3\,W_{\mathcal B}(n/2)+d\,n.
$$

- **Cost at level $i$** (there are $3^i$ nodes of size $n/2^i$; per-node combine $=d(n/2^i)$):

$$
3^i \cdot d\frac{n}{2^i}=d\,n\!\left(\frac{3}{2}\right)^{\!i}.
$$

- **Sum over levels** ($L=\lceil\log_2 n\rceil$):

$$
W_{\mathcal B}(n)\le d\,n\sum_{i=0}^{L}\!\left(\frac{3}{2}\right)^{\!i}
= d\,n\cdot\frac{(3/2)^{L+1}-1}{(3/2)-1}
=\Theta\!\big(n(3/2)^L\big).
$$

- **Turn $(3/2)^L$ into a power of $n$** (use $a^{\log_2 n}=n^{\log_2 a}$):

$$
n(3/2)^L=\Theta\!\big(n\cdot n^{\log_2(3/2)}\big)
=\Theta\!\big(n^{1+\log_2(3/2)}\big)
=\Theta\!\big(n^{\log_2 3}\big).
$$

**Conclusion (work):**

$$
W_{\mathcal B}(n)=\Theta\!\big(n^{\log_2 3}\big)\approx \Theta(n^{1.585}).
$$

Span

- **Recurrence (three equal subcalls in parallel):**

$$
S_{\mathcal B}(n)=S_{\mathcal B}(n/2)+d\,n.
$$

- **Unroll (geometric decay along the path):**

$$
S_{\mathcal B}(n)\le d\,(n+n/2+n/4+\cdots)=O(n).
$$

**Conclusion (span):**

$$
S_{\mathcal B}(n)=\Theta(n).
$$


### **Checking Performance**

Both methods timed on the **worst-case ($b$)-bit inputs** ($(2^b-1)$), with **one timing per size**.

| bits | grade-school (ms) | Karatsuba (ms) | speedup (grade-school/Karatsuba) |
|-----:|------------------:|---------------:|---------------------------------:|
| 8  | 0.084 | 0.123 | 0.68 |
| 12 | 0.266 | 0.198 | 1.34 |
| 16 | 0.317 | 0.346 | 0.92 |
| 20 | 0.736 | 0.422 | 1.75 |
| 24 | 1.036 | 0.591 | 1.75 |
| 28 | 1.241 | 0.809 | 1.53 |
| 32 | 1.185 | 0.996 | 1.19 |
| 40 | 2.776 | 1.208 | 2.30 |
| 48 | 3.752 | 1.642 | 2.28 |
| 56 | 4.224 | 2.112 | 2.00 |
| 64 | 4.287 | 2.589 | 1.66 |

**Observation.** Crossover **20–24 bits**, however, as bits get larger, Karatsuba consistently outperforms grade-school multiplicatoin (≈ **1.7×–2.3×** here). This aligns with the recursion-tree/brick-method analysis:
$W_{\text{school}}(n)=\Theta(n^2),\qquad
W_{\text{Karatsuba}}(n)=\Theta\!\big(n^{\log_2 3}\big)\approx \Theta(n^{1.585}).$

---
### **6. White hats vs. black hats**

For a pair $(A,B)$ we may ask each about the other:

- Both say “white” $\Rightarrow$ either **both white** or **both black** (one pair test cannot distinguish).
- At least one says “black” $\Rightarrow$ **at least one is black**.


### **6a. Black hats form a strict majority**

**Claim.** If more than $n/2$ students are black, pairwise tests alone cannot uniquely determine the white hats.

**Reason.** Consider two colorings:

- $I$: the true instance (with $> n/2$ blacks).
- $I'$: the coloring obtained by flipping every color of $I$ (whites $\leftrightarrow$ blacks).

For any pair $(A,B)$:
- If they have the **same** color in $I$, they also have the same color in $I'$; in both worlds “white/white” can appear (truth in one, coordinated answers in the other).
- If they have **different** colors in $I$, they are also different in $I'$; in both worlds at least one is black, so “(at least one says) black” can occur.

Thus the **entire transcript** of pairwise interviews can be the **same** in $I$ and $I'$. Since the colorings differ but yield the same transcript, no algorithm using only pairwise tests can identify the whites when blacks are a strict majority. $\square$


### **6b. Constant-fraction reduction when whites are a strict majority**

Assume that **strictly more than $n/2$** students are white. Do one round:

1. **Pair** students arbitrarily (drop one unpaired if $n$ is odd).
2. For each pair $(A,B)$:
   - If at least one says “black,” **discard both** (removes $\ge 1$ black and $\le 1$ white).
   - If both say “white,” **keep exactly one** representative of the pair.

After the round there are at most $\lceil n/2\rceil$ survivors (a constant-factor shrink), and a strict white majority remains a strict majority among the survivors. Therefore, round uses at most $\lfloor n/2\rfloor$ interviews.


### **6c. Finding all white hats**

**Phase 1.**  
Apply the step from 6b repeatedly until one **candidate** $C$ remains.  
Cost: $\frac{n}{2}+\frac{n}{4}+\frac{n}{8}+\cdots=O(n)$.

**Phase 2.**  
Ask everyone about $C$. With a strict white majority, a majority vote certifies $C$ if and only if $C$ is white. Let the certified trusted white be $W$.  
Cost: $O(n)$.

**Phase 3.**  
For each remaining student $X$, interview $(W,X)$. Since $W$ tells the truth, $W$’s answer gives $X$’s color.  
Cost: $(n-1)=O(n)$.

**Total:** Cost(Phase 1) + Cost(Phase 2) + Cost(Phase 3) = $O(n)+O(n)+O(n)=\boxed{\Theta(n)}$.

--
