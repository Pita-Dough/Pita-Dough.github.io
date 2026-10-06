#!/usr/bin/env python3
"""Builds the four side-panel diagrams for the course pages.

Run from anywhere:  python3 _figures/build_figures.py
Writes e212-left.html, e212-right.html, e312-left.html, e312-right.html next to this script.
Each file is a raw-HTML block that the course pages pull in with {{< include >}}.

The diagrams are deliberately sparse: curves, a few symbols, no sentences.
All geometry is computed from the model equations below, so tangencies, intersections and
areas are exact (the asserts check them). Colors and line styles live in styles/course.css
(classes .f-*) so the figures follow the light/dark theme.

ECON 312 left panel follows the Ch. 8 lecture notes: original bundle x-bar, Slutsky ("pivot")
bundle x^s, final bundle x^*; the notes' numbers (p1: 4 -> 1, p2 = 1, m = 12, u = x1 x2).
"""
import pathlib

HERE = pathlib.Path(__file__).parent
W = 280  # common viewBox width


def n(v):
    return f"{v:.1f}"


def path(pts, close=False):
    d = "M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts)
    return d + (" Z" if close else "")


def txt(x, y, s, cls="f-t", anchor="start", extra=""):
    return f'<text x="{n(x)}" y="{n(y)}" class="{cls}" text-anchor="{anchor}" {extra}>{s}</text>'


ZW = "​"  # zero-width space: lets a final dy reset take effect without adding width


def sub(main, low, c="f-sub"):
    """main followed by a subscript (dy shifts; baseline-shift is patchy across browsers)."""
    return f'{main}<tspan dy="3" class="{c}">{low}</tspan><tspan dy="-3">{ZW}</tspan>'


def sup(main, up, c="f-sub"):
    return f'{main}<tspan dy="-5" class="{c}">{up}</tspan><tspan dy="5">{ZW}</tspan>'


def subsup(main, low, up, c="f-sub", w=4.7):
    """main with a subscript and a superscript stacked at the same horizontal position."""
    return (f'{main}<tspan dy="3.5" class="{c}">{low}</tspan>'
            f'<tspan dy="-8.5" dx="-{w}" class="{c}">{up}</tspan><tspan dy="5">{ZW}</tspan>')


def dot(x, y, cls="f-dot-ink"):
    return f'<circle cx="{n(x)}" cy="{n(y)}" r="4.5" class="f-ring"/><circle cx="{n(x)}" cy="{n(y)}" r="3.5" class="{cls}"/>'


def xbar(x, y, cls="f-t", anchor="start"):
    """A bold-ish x with an overbar, drawn (combining macrons render unevenly across fonts)."""
    off = {"start": 0, "middle": -3.5, "end": -7}[anchor]
    return (txt(x, y, "x", cls, anchor) +
            f'<path d="M{n(x+off)},{n(y-9.5)} h7" class="f-bar"/>')


def svg(h, label, body, defs=""):
    return (
        "```{=html}\n"
        f'<svg class="fig" viewBox="0 0 {W} {h}" role="img" aria-label="{label}" '
        f'xmlns="http://www.w3.org/2000/svg">\n<title>{label}</title>\n'
        f"{('<defs>' + defs + '</defs>') if defs else ''}\n{body}\n</svg>\n```\n"
    )


# ---------------------------------------------------------------- ECON 212, left
def e212_left():
    X0, X1, Y0, Yb = 34, 262, 20, 220

    def X(q): return X0 + (X1 - X0) * q / 100
    def Y(p): return Yb - (Yb - Y0) * p / 100

    D = lambda q: 100 - q
    S = lambda q: 0.6 * q
    qe = 100 / 1.6
    pe = S(qe)

    b = []
    b.append(f'<path d="M{X0},{Y0-6} V{Yb} H{X1+6}" class="f-axis"/>')
    b.append(txt(X0 - 6, Y0 - 2, "P", "f-t", "end"))
    b.append(txt(X1 + 6, Yb + 14, "Q", "f-t", "end"))
    b.append(f'<path d="{path([(X(0), Y(100)), (X(100), Y(0))])}" class="f-line c1"/>')
    b.append(f'<path d="{path([(X(0), Y(0)), (X(100), Y(60))])}" class="f-line c2"/>')
    # three points on D: elastic, unit elastic, inelastic
    for q, lab in [(25, "|ε| &gt; 1"), (50, "|ε| = 1"), (80, "|ε| &lt; 1")]:
        b.append(dot(X(q), Y(D(q)), "f-dot-1"))
        b.append(txt(X(q) + 9, Y(D(q)) - 7, lab, "f-t"))
    b.append(dot(X(qe), Y(pe), "f-dot-ink"))
    b.append(txt(X(qe), Y(pe) + 19, "E", "f-t", "middle", 'font-style="italic"'))
    b.append(txt(X(7), Y(97), "D", "f-t f-b"))
    b.append(txt(X(100) - 2, Y(60) - 8, "S", "f-t f-b", "end"))
    b.append(txt(W / 2, Yb + 36, "ε = (%ΔQ) / (%ΔP)", "f-t", "middle"))
    return svg(Yb + 46, "Supply and demand; elasticity is above one on the upper part of demand, one at the midpoint, below one on the lower part", "\n".join(b))


# ---------------------------------------------------------------- ECON 212, right
def e212_right():
    X0, X1, Y0, Yb = 34, 262, 20, 220

    def X(q): return X0 + (X1 - X0) * q / 20
    def Y(p): return Yb - (Yb - Y0) * p / 20

    D = lambda q: 20 - q
    MR = lambda q: 20 - 2 * q
    MC = lambda q: 2 + q
    ATC = lambda q: 12.0 / q + 2 + 0.5 * q
    qm = 6.0
    pm = D(qm)
    mc_m = MC(qm)
    atc_m = ATC(qm)
    qs = 9.0
    ps = D(qs)
    assert abs(MR(qm) - MC(qm)) < 1e-9 and abs(D(qs) - MC(qs)) < 1e-9

    b = []
    b.append(f'<path d="M{X0},{Y0-6} V{Yb} H{X1+6}" class="f-axis"/>')
    b.append(txt(X0 - 6, Y0 - 2, "$", "f-t", "end"))
    b.append(txt(X1 + 6, Yb + 14, "Q", "f-t", "end"))
    b.append(f'<rect x="{n(X(0))}" y="{n(Y(pm))}" width="{n(X(qm)-X(0))}" height="{n(Y(atc_m)-Y(pm))}" class="f-wash1"/>')
    b.append(f'<path d="{path([(X(qm), Y(pm)), (X(qm), Y(mc_m)), (X(qs), Y(ps))], close=True)}" class="f-washred"/>')
    b.append(f'<path d="M{n(X0)},{n(Y(pm))} H{n(X(qm))} M{n(X(qm))},{n(Y(pm))} V{n(Yb)} '
             f'M{n(X0)},{n(Y(atc_m))} H{n(X(qm))}" class="f-guide"/>')
    b.append(f'<path d="{path([(X(0), Y(20)), (X(20), Y(0))])}" class="f-line c1"/>')
    b.append(f'<path d="{path([(X(0), Y(20)), (X(10), Y(0))])}" class="f-line c1 f-dash"/>')
    b.append(f'<path d="{path([(X(0), Y(2)), (X(18), Y(20))])}" class="f-line c2"/>')
    pts = [(X(q / 10), Y(ATC(q / 10))) for q in range(8, 171) if ATC(q / 10) <= 20]
    b.append(f'<path d="{path(pts)}" class="f-line c2 f-dash"/>')
    b.append(dot(X(qm), Y(pm), "f-dot-1"))
    b.append(dot(X(qm), Y(mc_m), "f-dot-2"))
    b.append(txt(X0 - 5, Y(pm) + 4, sub("P", "m"), "f-s", "end"))
    b.append(txt(X(qm), Yb + 14, sub("Q", "m"), "f-s", "middle"))
    b.append(txt(X(qm) - 4, Y(pm) + 17, "π", "f-t f-halo", "end"))
    b.append(f'<path d="{path([(X(qs) + 6, Y(ps)), (X(qs) + 22, Y(ps))])}" class="f-leader"/>')
    b.append(txt(X(qs) + 26, Y(ps) + 4, "DWL", "f-t", "start"))
    b.append(txt(X(19.6), Y(1.5), "D", "f-t f-b", "end"))
    b.append(txt(X(10) + 5, Y(0.2) - 4, "MR", "f-t f-b"))
    b.append(txt(X(18) + 5, Y(20) + 4, "MC", "f-t f-b"))
    b.append(txt(X(16.2), Y(ATC(16.0)) + 14, "ATC", "f-t f-b"))
    return svg(Yb + 26, "Monopolist's demand, marginal revenue, marginal and average cost, with profit and deadweight loss shaded", "\n".join(b))


# ---------------------------------------------------------------- ECON 312, left (Ch. 8 notation)
def e312_left():
    X0, X1, Y0, Yb = 34, 264, 14, 208
    XM = YM = 13.4

    def X(x): return X0 + (X1 - X0) * x / XM
    def Y(y): return Yb - (Yb - Y0) * y / YM

    # The Ch. 8 notes: u = x1 x2, p2 = 1, m = 12, p1: 4 -> 1.
    xbar_ = (1.5, 6.0)      # original choice, on 4 x1 + x2 = 12
    xs = (3.75, 3.75)       # Slutsky ("pivot") choice, on x1 + x2 = 7.5  (m' = p1' xbar1 + p2 xbar2)
    xst = (6.0, 6.0)        # final choice, on x1 + x2 = 12
    assert abs(4 * xbar_[0] + xbar_[1] - 12) < 1e-9 and abs(xbar_[1] / xbar_[0] - 4) < 1e-9
    assert abs(1 * xbar_[0] + xbar_[1] - 7.5) < 1e-9                    # xbar affordable on the pivoted line
    assert abs(xs[0] + xs[1] - 7.5) < 1e-9 and abs(xs[1] / xs[0] - 1) < 1e-9
    assert abs(xst[0] + xst[1] - 12) < 1e-9 and abs(xst[1] / xst[0] - 1) < 1e-9
    k0, k1, k2 = (p[0] * p[1] for p in (xbar_, xs, xst))

    def ic(k):
        pts = []
        for i in range(161):
            x = k / YM + (XM - k / YM) * i / 160
            pts.append((X(x), Y(k / x)))
        return pts

    b = []
    b.append(f'<path d="M{X0},{Y0-6} V{Yb} H{X1+6}" class="f-axis"/>')
    b.append(txt(X0 - 6, Y0 + 1, "x₂", "f-t", "end"))
    b.append(txt(X1 + 6, Yb + 14, "x₁", "f-t", "end"))
    # budget lines: original, pivoted through xbar, final
    b.append(f'<path d="{path([(X(0), Y(12)), (X(3), Y(0))])}" class="f-line f-thin"/>')
    b.append(f'<path d="{path([(X(0), Y(7.5)), (X(7.5), Y(0))])}" class="f-line c1 f-bc"/>')
    b.append(f'<path d="{path([(X(0), Y(12)), (X(12), Y(0))])}" class="f-line c2 f-bc"/>')
    # indifference curves
    b.append(f'<path d="{path(ic(k0))}" class="f-line f-thin"/>')
    b.append(f'<path d="{path(ic(k1))}" class="f-line c1"/>')
    b.append(f'<path d="{path(ic(k2))}" class="f-line c2"/>')
    for p in (xbar_, xs, xst):
        b.append(f'<path d="M{n(X(p[0]))},{n(Y(p[1]))} V{n(Yb)}" class="f-guide"/>')
    # bundles
    b.append(dot(X(xbar_[0]), Y(xbar_[1]), "f-dot-ink"))
    b.append(xbar(X(xbar_[0]) + 7, Y(xbar_[1]) - 7, "f-t f-b"))
    b.append(dot(X(xs[0]), Y(xs[1]), "f-dot-1"))
    b.append(txt(X(xs[0]) + 7, Y(xs[1]) - 7, sup("x", "s"), "f-t f-b"))
    b.append(dot(X(xst[0]), Y(xst[1]), "f-dot-2"))
    b.append(txt(X(xst[0]) + 7, Y(xst[1]) - 7, sup("x", "*"), "f-t f-b"))

    # braces under the axis: the same three colors as the equation below
    def brace(xa, xb, y, cls, label):
        s = f'<path d="M{n(X(xa))},{n(y-3)} V{n(y)} H{n(X(xb))} V{n(y-3)}" class="f-brk {cls}"/>'
        return s + txt((X(xa) + X(xb)) / 2, y + 15, label, "f-s", "middle")
    y1, y2 = Yb + 22, Yb + 50
    b.append(brace(xbar_[0], xs[0], y1, "bk1", subsup("Δx", "1", "s", "f-sub-s")))
    b.append(brace(xs[0], xst[0], y1, "bk2", subsup("Δx", "1", "n", "f-sub-s")))
    b.append(brace(xbar_[0], xst[0], y2, "bkink", sub("Δx", "1", "f-sub-s")))

    # ---- the equation (derivative form from the notes), stacked fractions
    cy = y2 + 62
    fw, ow = 38, 24
    num = lambda up: subsup("∂x", "1", up, "f-sub-eq", 5.5)
    pieces = [("frac", num("*"), sub("∂p", "1", "f-sub-eq"), fw),
              ("op", "=", ow),
              ("frac", num("s"), sub("∂p", "1", "f-sub-eq"), fw),
              ("op", "−", ow),
              ("var", "", 18),
              ("frac", num("*"), "∂m", fw)]
    total = sum(p[-1] for p in pieces)
    x = W / 2 - total / 2
    spans = []
    for p in pieces:
        w = p[-1]
        cx = x + w / 2
        if p[0] == "frac":
            b.append(txt(cx, cy - 5, p[1], "f-eq", "middle"))
            b.append(f'<path d="M{n(x+2)},{n(cy)} H{n(x+w-2)}" class="f-fraclin"/>')
            b.append(txt(cx, cy + 17, p[2], "f-eq", "middle"))
        elif p[0] == "op":
            b.append(txt(cx, cy + 5, p[1], "f-eq", "middle"))
        else:   # xbar_1
            b.append(txt(cx - 4, cy + 5, sub("x", "1", "f-sub-eq"), "f-eq", "middle"))
            b.append(f'<path d="M{n(cx-8.5)},{n(cy-7)} h8" class="f-bar"/>')
        spans.append((x, x + w))
        x += w
    te, se, ie = spans[0], spans[2], (spans[3][0] + 2, spans[5][1])
    yb_ = cy + 32
    for (a, c), cls, lab in [(te, "bkink", sub("Δx", "1", "f-sub-s")),
                             (se, "bk1", subsup("Δx", "1", "s", "f-sub-s")),
                             (ie, "bk2", subsup("Δx", "1", "n", "f-sub-s"))]:
        b.append(f'<path d="M{n(a)},{n(yb_-3)} V{n(yb_)} H{n(c)} V{n(yb_-3)}" class="f-brk {cls}"/>')
        b.append(txt((a + c) / 2, yb_ + 15, lab, "f-s", "middle"))
    return svg(int(yb_ + 26), "Slutsky decomposition for a fall in the price of good 1, and the Slutsky equation in derivative form", "\n".join(b))


# ---------------------------------------------------------------- ECON 312, right
def e312_right():
    BX0, BY1, S = 38, 236, 2.18       # box left edge, box bottom edge, pixels per unit
    BX1, BY0 = BX0 + 100 * S, BY1 - 100 * S

    def X(xa): return BX0 + S * xa
    def Y(ya): return BY1 - S * ya

    aA, aB = 0.7, 0.3                        # Cobb-Douglas exponents on good 1
    omega = (45.0, 55.0)                     # A's endowment of (good 1, good 2)
    uA = lambda x, y: x ** aA * y ** (1 - aA)
    uB = lambda xa, ya: max(100 - xa, 0.0) ** aB * max(100 - ya, 0.0) ** (1 - aB)
    uA0, uB0 = uA(*omega), uB(*omega)
    ic_a = lambda x: uA0 ** (1 / (1 - aA)) / x ** (aA / (1 - aA))
    ic_b = lambda x: 100 - (uB0 / (100 - x) ** aB) ** (1 / (1 - aB))
    beta = (aB / (1 - aB)) / (aA / (1 - aA))
    cc = lambda x: beta * x * 100 / (100 - (1 - beta) * x)
    for x in (10, 40, 80):                    # MRS_A = MRS_B on the contract curve
        y = cc(x)
        assert abs(aA / (1 - aA) * y / x - aB / (1 - aB) * (100 - y) / (100 - x)) < 1e-9
    assert abs(ic_a(omega[0]) - omega[1]) < 1e-9 and abs(ic_b(omega[0]) - omega[1]) < 1e-9

    def root(f, lo, hi):
        flo = f(lo)
        for _ in range(80):
            mid = (lo + hi) / 2
            if (f(mid) > 0) == (flo > 0):
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    g = lambda x: ic_b(x) - ic_a(x)
    xs_ = [0.5 + i * 0.01 for i in range(0, 9800)]
    roots = [root(g, a, c) for a, c in zip(xs_, xs_[1:]) if g(a) * g(c) < 0 and abs(a - omega[0]) > 0.5]
    x_far = roots[0]
    core = [x for x in [i * 0.05 for i in range(0, 2001)]
            if uA(x, cc(x)) >= uA0 - 1e-9 and uB(x, cc(x)) >= uB0 - 1e-9]
    c0, c1 = min(core), max(core)

    curveA = [(X(x), Y(ic_a(x))) for x in [1.0 + i * 0.25 for i in range(0, 396)] if ic_a(x) <= 100.5]
    curveB = [(X(x), Y(ic_b(x))) for x in [i * 0.25 for i in range(0, 395)] if -0.5 <= ic_b(x) <= 100]
    ccurve = [(X(x), Y(cc(x))) for x in [i * 0.5 for i in range(0, 201)]]
    coreseg = [(X(x), Y(cc(x))) for x in [c0 + (c1 - c0) * i / 40 for i in range(41)]]
    lo_x, hi_x = sorted([omega[0], x_far])
    up = [(X(x), Y(ic_b(x))) for x in [lo_x + (hi_x - lo_x) * i / 60 for i in range(61)]]
    dn = [(X(x), Y(ic_a(x))) for x in [hi_x - (hi_x - lo_x) * i / 60 for i in range(61)]]

    defs = f'<clipPath id="e312-box"><rect x="{n(BX0)}" y="{n(BY0)}" width="{n(100*S)}" height="{n(100*S)}"/></clipPath>'
    b = []
    b.append(f'<rect x="{n(BX0)}" y="{n(BY0)}" width="{n(100*S)}" height="{n(100*S)}" class="f-box"/>')
    b.append('<g clip-path="url(#e312-box)">')
    b.append(f'<path d="{path(up + dn, close=True)}" class="f-wash0"/>')
    b.append(f'<path d="{path(curveA)}" class="f-line c1"/>')
    b.append(f'<path d="{path(curveB)}" class="f-line c2"/>')
    b.append(f'<path d="{path(ccurve)}" class="f-line f-thin"/>')
    b.append(f'<path d="{path(coreseg)}" class="f-core"/>')
    b.append('</g>')
    b.append(dot(X(omega[0]), Y(omega[1]), "f-dot-ink"))
    b.append(txt(X(omega[0]) - 7, Y(omega[1]) + 15, "ω", "f-t f-b", "end", 'font-style="italic"'))
    b.append(txt(BX0 - 5, BY1 + 13, sub("O", "A"), "f-t", "end"))
    b.append(txt(BX1 + 5, BY0 - 5, sub("O", "B"), "f-t", "start"))
    xa_top = (uA0 ** (1 / (1 - aA)) / 100) ** ((1 - aA) / aA)
    b.append(txt(X(xa_top) + 6, Y(96), sub("u", "A"), "f-t f-b f-halo", "start"))
    b.append(txt(X(1.5), Y(ic_b(1.5)) - 8, sub("u", "B"), "f-t f-b f-halo", "start"))
    info = dict(x_far=x_far, core=(c0, c1))
    return svg(int(BY1 + 24), "Edgeworth box: indifference curves through the endowment, the lens of mutually beneficial trades, the contract curve and the core", "\n".join(b), defs), info


if __name__ == "__main__":
    outs = {"e212-left": e212_left(), "e212-right": e212_right(), "e312-left": e312_left()}
    right, info = e312_right()
    outs["e312-right"] = right
    for name, s in outs.items():
        (HERE / f"{name}.html").write_text(s)
        print("wrote", name, len(s), "bytes")
    print("edgeworth:", info)
