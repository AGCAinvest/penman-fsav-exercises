# FSAV Cap 5 — Notes
**Penman, S. H. (2013). *Financial Statement Analysis and Security Valuation* (5th ed.). McGraw-Hill.**

*Chapter 5: Accrual Accounting and Valuation — Pricing Book Values*

---

## Mastery Checklist

*The Analyst's Checklist (p. 141) lists what Penman expects you to understand and be able to do after reading the chapter. Use this section to track progress.*

**Status legend:** ✅ mastered · ⚠️ partial · ❌ not yet covered

### After reading this chapter you should **understand**:

| # | Item | Where in chapter | Status | Note |
|---|---|---|---|---|
| 1 | What "residual earnings" is | p. 142, Eq. 5.2 | ✅ | Covered in §Definitions + §Equations (RE_t formula + opportunity cost intuition) |
| 2 | How forecasting RE gives the premium over book value and the P/B ratio | p. 145, Eq. 5.1 | ✅ | Covered in §Equations (Eq. 5.1 + intrinsic premium + intrinsic P/B) |
| 3 | How RE are driven by ROCE and growth in book value | p. 148, Figure 5.1 | ⚠️ | ROCE mentioned in central thesis. Formal drivers (RE = (ROCE − r) × B) not yet covered. |
| 4 | The difference between Case 1, 2, and 3 valuation | pp. 152–155 | ⚠️ | Mapped informally in §Bridge to WP 2026.01. Formal cases not yet derived. |
| 5 | How the RE model captures value added in a strategy | pp. 159–161, Table 5.4 | ❌ | Strategy evaluation not yet covered |
| 6 | Advantages and disadvantages of RE vs DDM and DCF | Box 5.5, p. 161 | ❌ | Comparison not yet covered |
| 7 | How RE protects from paying too much for earnings added by investment | pp. 162–163, Exhibit 5.3 | ❌ | Not yet covered |
| 8 | How RE protects from paying for earnings created by accounting methods | pp. 163–164, Exhibit 5.4 | ❌ | Not yet covered |

### After reading this chapter you should **be able to**:

| # | Item | Test exercise | Status | Note |
|---|---|---|---|---|
| 9 | Calculate residual earnings | E5.1 | ⚠️ | Formula understood; exercise not yet done |
| 10 | Calculate the value of equities and strategies from forecasts | E5.3, E5.4 | ❌ | Exercises not yet done |
| 11 | Calculate an intrinsic P/B ratio | E5.5 | ⚠️ | Formula understood; exercise not yet done |
| 12 | Calculate value added in a strategy | E5.7 | ❌ | Exercise not yet done |
| 13 | Convert an analyst's earnings forecast into a valuation | E5.13 (Nike) | ❌ | Exercise not yet done — cornerstone of mastery |

**Summary as of May 7, 2026:** 2 ✅ · 4 ⚠️ · 7 ❌

---

## Foundational observations

- Firms trade at prices that differ from book value because some assets and liabilities are marked to market while others are recorded at historical cost — so book value may not reflect the firm's full value. (p. 140)

- The value of shareholders' investment is based on how much the investment is expected to earn in the future. So book value is worth more or less depending upon the future earnings that net assets are likely to generate. (p. 141)

- Profitability has a strong impact on the determination of the P/B ratio.

---

## Definitions

- **Book value**: shareholders' investment in the firm. Net assets recognized on the balance sheet. (p. 141)

- **Profitability**: the rate of return on book value. (p. 141)

- **Residual Earnings (RE)**: a measure that captures the value added to book value during a period. (p. 142)

- **P/B ratio**: prices the expected return on book value. (p. 142)

- **Intrinsic premium over book**: the difference between the intrinsic value of equity and its book value (V₀ᴱ − B₀). Represents the value not yet recognized on the balance sheet. (p. 145)

- **Intrinsic price-to-book ratio**: V₀ᴱ / B₀. The intrinsic counterpart of the observed market P/B. (p. 145)

---

## Equations

### Eq. 5.2 — Residual Earnings

```
RE_t = Earn_t − r × B_(t−1)
```

**Penman notation:**

```
RE_t = Earn_t − (ρ_E − 1) × B_(t−1)
```

where `ρ_E = 1 + r` (one plus the required equity return).

**Variables:**

| Symbol | Meaning |
|---|---|
| `r` | required rate of return on equity (cost of capital) |
| `B_(t−1)` | book value of equity on the balance sheet of the previous year |
| `Earn_t` | comprehensive income for the current year |
| `ρ_E` | one plus the required equity return |

**Intuition (opportunity cost).** `B_(t−1)` is the capital necessary to generate `Earn_t`. Had this capital not been deployed in this business, it would have been employed elsewhere. From this reality emerges, intuitively, the concept of opportunity cost — and thus the logical justification of the required return `r` in the RE equation. RE captures only the earnings *above* this required minimum.

**Economic interpretation:**

| RE | Meaning |
|---|---|
| RE > 0 | Firm creates value (earns above cost of capital) |
| RE = 0 | Firm preserves value (earns exactly cost of capital) |
| RE < 0 | Firm destroys value (earns below cost of capital) |

---

### Eq. 5.1 — Residual Earnings Valuation Model

```
V_0^E = B_0 + RE_1/ρ_E + RE_2/ρ_E² + RE_3/ρ_E³ + ...     (p. 145)
```

**Compact form:**

```
V_0^E = B_0 + Σ (RE_t / ρ_E^t)     for t = 1 to ∞
```

**Variables:**

| Symbol | Meaning |
|---|---|
| `V_0^E` | intrinsic value of common equity at time 0 |
| `B_0` | current book value of equity |
| `RE_t` | residual earnings forecast for year t |
| `ρ_E^t` | (1 + r)^t — compound discount factor at horizon t |

**Two derived quantities:**

```
Intrinsic premium over book:    V_0^E − B_0 = Σ RE_t / ρ_E^t
```

```
Intrinsic price-to-book ratio:  V_0^E / B_0 = 1 + (Σ RE_t / ρ_E^t) / B_0
```

**Going concern assumption.** The sum extends to infinity because the firm is assumed to operate indefinitely. Under liquidation assumption, the model would change.

---

## Principles

- **Anchoring principle.** Fundamental analysis anchors valuation in the financial statements. Book value, presented as the bottom line of the balance sheet, provides the anchor. The investor anchors on what is recognized in the books, then proceeds to assess the value not yet recognized — the premium over book value. (p. 142)

  ```
  Value = Book value + Premium
  ```

- **Central thesis of the chapter.** The four following statements are equivalent — different ways of saying the same thing:

  ```
  RE > 0  ⟺  V > B  ⟺  P/B > 1  ⟺  ROCE > r
  ```

  When this equivalence becomes intuitive, the chapter is conceptually mastered.

---

## Quotable passages

- *"Book value is worth more or less, depending upon the future earnings that the net assets are likely to generate."* — Penman (2013, p. 141)

- *"We calculate the intrinsic premium over book value, V_0^E − B_0, as the present value of forecasted residual income."* — Penman (2013, p. 145)

- *"Income (earnings) represents the growth of the capital within a period of the operation made in economic activity."* — Magni (2020, p. 7)

  → Convergence with Penman: earnings is the accounting instrument that captures the value added by economic operations during a period.

---

## My reflections

**On Penman's modal language.** This is why valuing a firm is so hard, and why Penman uses careful modal words: *"expected to earn"*, *"likely to generate"*. Both expressions carry a belief that something *might* happen in the future. Valuation is probabilistic, not deterministic — and the framework respects this by anchoring on what is verified (book value) before extending into what is expected.

**On opportunity cost as the foundation of RE.** The required return `r` is not arbitrary. It reflects the alternative use of capital: had `B_(t−1)` been employed in another business of equivalent risk, it would have earned `r` there. RE is therefore not "earnings minus an accounting charge" — it is **earnings above the alternative**. This is the economic substance behind the formula.

**On Eq. 5.1 and the closing of the foundational argument.** In the foundational part we observed that when value differs from book, something is missing. To formalize this idea, Penman presents the intrinsic premium over book, V₀ᴱ − B₀ — the missing value in the balance sheet. When this premium is denominated by B₀, it becomes the intrinsic price-to-book ratio V₀ᴱ/B₀. A positive RE means equity is worth more than its book value, and the firm should trade at a premium over book. Equation 5.1 formally states that the current value of equity equals its current book plus the present value of all upcoming residual earnings, summed to infinity because we are dealing with going-concern firms. (Penman, 2013, p. 145)

---

## Bridge to WP 2026.01

The economic interpretation of RE maps directly to the three Brazilian archetypes:

| Archetype | RE behavior | Penman case |
|---|---|---|
| **VIVA3** (Vivara) | RE > 0, persistent | Case 2 — constant positive RE |
| **MDIA3** (M. Dias Branco) | RE ≈ 0 or slightly negative | Case 1 — RE drifts to zero |
| **RADL3** (RD Saúde) | RE > 0, growing | Case 3 — RE growing |

The central thesis equivalence (`RE > 0 ⟺ V > B ⟺ P/B > 1 ⟺ ROCE > r`) is the analytical core of Section VIII of the Working Paper. The cases in Penman are not pedagogical curiosities — they are categories of value creation that map onto real Brazilian firms.

---

## Open questions

- *(to be filled as reading progresses)*

---

## References

- Magni, C. A. (2020). *Investment Decisions and the Logic of Valuation: Linking Finance, Accounting, and Engineering*. Springer.
- Penman, S. H. (2013). *Financial Statement Analysis and Security Valuation* (5th ed.). McGraw-Hill.

---

*Notes compiled May 7, 2026 — covers pp. 140–145 (introduction, P/B concept, RE definition, valuation model Eq. 5.1).*
