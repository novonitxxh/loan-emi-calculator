# 💰 Loan EMI Calculator

A simple, interactive tool to calculate **Equated Monthly Installments (EMI)** for any loan — home loan, car loan, personal loan — using the standard amortization formula.

**[➡ Try the live demo](https://YOUR_USERNAME.github.io/loan-emi-calculator/)**

---

## How it works

The EMI formula used is the standard reducing-balance loan amortization formula:

```
EMI = P × R × (1 + R)^N / [(1 + R)^N − 1]
```

| Symbol | Meaning |
|--------|---------|
| `P` | Principal loan amount |
| `R` | Interest rate **per month** (annual rate ÷ 12 ÷ 100) |
| `N` | Loan tenure in **months** |

If the interest rate is 0%, the formula simplifies to `EMI = P / N`.

---

## What's in this repo

| File | Description |
|------|--------------|
| `index.html` | Browser-based calculator with live sliders — hosted via GitHub Pages |
| `emi_calculator.py` | Command-line Python version with input validation and formatted output |

---

## Run the Python version locally

```bash
git clone https://github.com/YOUR_USERNAME/loan-emi-calculator.git
cd loan-emi-calculator
python emi_calculator.py
```

You'll be prompted for:
- Principal amount
- Annual interest rate (in %)
- Loan tenure (in months)

The program then prints a full breakdown: monthly EMI, total payment, and total interest payable.

### Example

```
Principal amount (P): 1000000
Annual interest rate (in %, e.g. 10.5): 10.5
Loan tenure (in months): 240

==================================================
           LOAN EMI CALCULATION SUMMARY
==================================================
Principal Amount (P)    : 1,000,000.00
Annual Interest Rate    : 10.50%
Monthly Interest Rate   : 0.8750%
Loan Tenure             : 240 months (20.0 years)
--------------------------------------------------
Monthly EMI              : 9,983.80
Total Payment            : 2,396,112.61
Total Interest Payable   : 1,396,112.61
==================================================
```

---

## Run the web version locally

Just open `index.html` in any browser — no build step, no dependencies. It's a single self-contained file.

---

## Tech stack

- **Python 3** (standard library only — no external packages needed)
- **HTML / CSS / vanilla JavaScript** for the web version (no frameworks)
- Hosted on **GitHub Pages**

---

## License

MIT — free to use, modify, and share.
