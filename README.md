<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&height=280&color=gradient&customColorList=0,2,2,5,30&text=%7c%24%7cians&fontColor=00ffa8&fontSize=80&stroke=ea00d9&strokeWidth=2&animation=fadeIn&fontAlignY=38&desc=Agentic%20Opportunity%20Radar&descAlignY=58&descSize=20&descColor=ffffff" width="100%"/>

<!-- Badges Row 1 -->
<p>
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/CrewAI-Orchestration-FF4B4B?style=for-the-badge&logo=robot&logoColor=white"/>
  <img src="https://img.shields.io/badge/Groq-LPU%20Inference-FF6B00?style=for-the-badge&logo=lightning&logoColor=white"/>
  <img src="https://img.shields.io/badge/Llama_3.3-70B-blueviolet?style=for-the-badge&logo=meta&logoColor=white"/>
</p>

<!-- Badges Row 2 -->
<p>
  <img src="https://img.shields.io/badge/yFinance-Data%20Layer-00897B?style=for-the-badge&logo=yahoo&logoColor=white"/>
  <img src="https://img.shields.io/badge/NSE%20%7C%20BSE-Indian%20Markets-FF9800?style=for-the-badge&logo=chart-line&logoColor=white"/>
  <img src="https://img.shields.io/badge/ISI-Bangalore-1565C0?style=for-the-badge&logo=graduation-cap&logoColor=white"/>
  <img src="https://img.shields.io/badge/ET%20GenAI%20Hackathon-2026-00ffa8?style=for-the-badge&logo=trophy&logoColor=black"/>
</p>

<br/>

```
███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
        Agentic Opportunity Radar v1.0
```

### *Institutional-Grade Statistical Validation for Retail Investors*

<br/>

> **"The market rewards those who see the signal through the noise."**
>
> NEXUS is a multi-agent AI pipeline that validates stock breakouts using Z-Score volume analysis — putting the quant desk's edge in the hands of every retail trader.

</div>

---

## 📌 Table of Contents

- [The Problem We Solve](#-the-problem-we-solve)
- [How NEXUS Works](#-how-nexus-works)
- [The Math Behind the Magic](#-the-math-behind-the-magic)
- [Multi-Agent Architecture](#-multi-agent-architecture)
- [Tech Stack](#%EF%B8%8F-tech-stack)
- [Quick Start](#-quick-start)
- [Sample Output](#-sample-output)
- [Team](#-team-ians)

---

## 🎯 The Problem We Solve

```
[ Retail Trader ] ──→ Sees price breakout ──→ Buys in excitement ──→ 📉 Bull Trap
[ Institutional ] ──→ Sees volume Z-Score ──→ Validates conviction ──→ 📈 Wins
```

Retail investors bleed not from lack of information — but from **information asymmetry**. Institutional desks run proprietary volume models that detect whether a price spike is backed by real conviction or is just a low-liquidity fake-out designed to shake out weak hands.

**NEXUS bridges that gap.**

By reframing market analysis as a **multi-agent statistical validation pipeline**, we give any retail trader access to the same z-score guardrails that quant funds rely on — free, open, and running in seconds.

---

## ⚙️ How NEXUS Works

```
┌─────────────────────────────────────────────────────────────────┐
│                        NEXUS PIPELINE                           │
│                                                                 │
│  📥 INPUT                                                       │
│  └─ Ticker (e.g. RELIANCE.NS) + 20-Day OHLCV via yFinance       │
│                          │                                      │
│                          ▼                                      │
│  🧮 STATISTICAL ENGINE                                          │
│  └─ Compute μ, σ, and Volume Z-Score                            │
│                          │                                      │
│                          ▼                                      │
│  🕵️ AGENT 1: Lead Quant Researcher                              │
│  └─ Applies Z-Score gating. Flags signal or noise.              │
│                          │                                      │
│                          ▼                                      │
│  📈 AGENT 2: Indian Market Strategist                           │
│  └─ Translates quant signal into NSE/BSE execution plan         │
│                          │                                      │
│                          ▼                                      │
│  📤 OUTPUT                                                      │
│  └─ Validated Action: BUY / SELL / HOLD/TRAP + Rationale        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🧠 The Math Behind the Magic

Traditional volume bars are noisy and context-free. NEXUS replaces them with **Volume Z-Score Analysis** — a rigorous statistical framework that answers one question: *Is today's volume genuinely unusual?*

### Step 1 — Historical Baseline

We establish the 20-day rolling statistics (with `min_periods=1` to handle sparse data and new listings):

$$\mu_{20} = \frac{1}{20}\sum_{i=1}^{20} V_i \qquad \sigma_{20} = \sqrt{\frac{1}{20}\sum_{i=1}^{20}(V_i - \mu_{20})^2}$$

### Step 2 — Z-Score Signal

$$\boxed{Z_v = \frac{V_t - \mu_{20}}{\sigma_{20}}}$$

> **Robust Pre-processing:** Zero values in σ are replaced with `NaN` before division (zero-volatility guard for thinly traded assets), with `NaN` Z-Scores subsequently filled to `0`. This prevents `ZeroDivisionError` on penny stocks and SME-listed securities.

### Step 3 — Signal Interpretation

| Z-Score Range | Percentile | Signal | Verdict |
|:---:|:---:|:---|:---:|
| `Z ≥ 2.0` | Top 2.3% | 🟢 High Institutional Conviction | **BUY** |
| `1.0 ≤ Z < 2.0` | Above Average | 🔵 Rising Interest | **WATCH+** |
| `-1.0 < Z < 1.0` | Normal | ⚪ No Statistical Edge | **NEUTRAL** |
| `-2.0 < Z ≤ -1.0` | Below Average | 🟡 Reduced Participation | **HOLD/TRAP** |
| `Z ≤ -2.0` | Bottom 2.3% | 🔴 Institutional Exit Risk | **SELL** |

> **Why Z-Score?** It normalizes volume across different market caps, sectors, and trading sessions — eliminating the raw-number bias that misleads most retail tools. A `Z ≥ 2.0` event occurs in only **2.3% of trading sessions**, making it a statistically rare and reliable institutional footprint.

---

## 🤖 Multi-Agent Architecture

Powered by **Llama 3.3 70B** on **Groq's LPU** for sub-second inference, NEXUS runs two specialised AI agents in a sequential crew via CrewAI's native `LLM()` class — no LangChain wrapper required.

<table>
<tr>
<td width="50%" valign="top">

### 🕵️‍♂️ Agent 1
## Lead Quant Researcher

**Persona:** ISI-trained statistician. Rigorous. Threshold-bound.

**Mandate:** Acts as the strict statistical gatekeeper. Zero tolerance for narratives — only the Z-Score verdict matters.

**Core Logic:**
- Ingests the `get_nse_data()` market report
- Evaluates Volume Z-Score against the 2.0 threshold
- Classifies signal as **Breakout** or **Retail Bull Trap**
- Outputs a structured statistical assessment

**Guardrail:** If `Z < 2.0`, the asset is flagged as *"Insufficient Institutional Participation"* regardless of price action.

**Temperature:** `0.1` — near-deterministic output

</td>
<td width="50%" valign="top">

### 📈 Agent 2
## Indian Market Strategist

**Persona:** Expert in Indian market liquidity, circuit limits, and institutional retail traps.

**Mandate:** Takes the quant assessment and translates it into a risk-mitigated execution verdict tuned to NSE/BSE microstructure.

**Core Logic:**
- Reads Agent 1's statistical assessment
- Factors in circuit limits, F&O expiry, and India VIX context
- Delivers the final **BUY / SELL / HOLD/TRAP** verdict
- Includes explicit risk management advice

**Guardrail:** Never contradicts the Z-Score classification set by Agent 1.

**Temperature:** `0.1` — grounded, consistent verdicts

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|:---|:---|:---|
| 🧠 **LLM Engine** | Groq LPU + Llama 3.3 70B | Sub-second inference (~85ms vs 380ms on A100) |
| 🤖 **Orchestration** | CrewAI + Native `LLM()` | Multi-agent pipeline; no LangChain dependency |
| 📊 **Data Layer** | yFinance + Pandas + NumPy | Live OHLCV ingestion, rolling Z-Score computation |
| 🐍 **Runtime** | Python 3.11+ | Core execution environment |
| 🌐 **Markets** | NSE / BSE (India) | Auto `.NS`/`.BO` suffix handling |

---

## ▶️ Quick Start

### Prerequisites

- Python 3.11+
- A [Groq API key](https://console.groq.com) (free tier works)

### Installation

**1. Clone the repo**
```bash
git clone https://github.com/Zapking-001/NEXUS_Opportunity_Radar.git
cd NEXUS_Opportunity_Radar
```

**2. Create and activate virtual environment**
```bash
# Linux / macOS
python -m venv venv && source venv/bin/activate

# Windows (Git Bash)
python -m venv venv && source venv/Scripts/activate
```

**3. Install dependencies**
```bash
pip install crewai yfinance pandas numpy python-dotenv
```

**4. Set your API key**

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_key_here
```

Or export directly:
```bash
# Linux / macOS
export GROQ_API_KEY="your_key_here"

# Windows (PowerShell)
$env:GROQ_API_KEY="your_key_here"
```

**5. Launch NEXUS**
```bash
python main.py
```

NEXUS will automatically scan `RELIANCE.NS` by default, or edit `TARGET_STOCK` in `main.py`:
```python
TARGET_STOCK = "TCS.NS"   # or INFY.NS, HDFCBANK.NS, etc.
```

---

## 📊 Sample Output

```
--- Initiating NEXUS Opportunity Radar for RELIANCE.NS ---
Fetching market data and calculating Z-Scores...

╭──────────────────────────────────── 🤖 Agent Started ─────────────────────────────────────╮
│                                                                                            │
│  Agent: Lead Quant Researcher                                                              │
│                                                                                            │
│  Task: Analyze the following market data for RELIANCE.NS. Focus heavily on the Volume      │
│  Z-Score.                                                                                  │
│                                                                                            │
│  Data:                                                                                     │
│    Market Data Report for RELIANCE.NS (Latest Trading Session):                            │
│    - Close Price: ₹2847.35                                                                 │
│    - Trading Volume: 8473920                                                               │
│    - 20-Day Avg Volume: 5021438.00                                                         │
│    - Volume Z-Score: 2.47                                                                  │
│    Recent Trend (Last 5 Days Close Prices): {…2791.2, …2803.5, …2819.8, …2834.1, …2847.4} │
│                                                                                            │
│  Determine if this is a true breakout or a retail bull trap.                               │
│                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────╯

╭──────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────╮
│                                                                                            │
│  Agent: Lead Quant Researcher                                                              │
│                                                                                            │
│  Final Answer:                                                                             │
│  The Volume Z-Score of 2.47 confirms a statistically significant anomaly, exceeding the   │
│  2.0 high-conviction threshold. This places today's session in the top 2.3% of volume     │
│  activity over the rolling 20-day window — consistent with institutional accumulation.     │
│  The 5-day close price trend shows steady upward momentum (+2.0% over the window).        │
│  Mathematical confidence: HIGH. This is not a retail bull trap; volume conviction is real. │
│                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────╯

╭──────────────────────────────────── 🤖 Agent Started ─────────────────────────────────────╮
│                                                                                            │
│  Agent: Indian Market Strategist                                                           │
│                                                                                            │
│  Task: Review the Quant Researcher's statistical summary for RELIANCE.NS.                  │
│  Formulate a final, actionable trading verdict (BUY, SELL, or HOLD/TRAP).                  │
│                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────╯

╭──────────────────────────────────── ✅ Agent Final Answer ─────────────────────────────────╮
│                                                                                            │
│  Agent: Indian Market Strategist                                                           │
│                                                                                            │
│  Final Answer:                                                                             │
│  VERDICT: BUY (High Conviction)                                                            │
│                                                                                            │
│  Reliance exhibits a statistically validated volume breakout above the high-conviction     │
│  threshold with a confirmed upward price trend — consistent with institutional             │
│  accumulation on NSE. Risk management: consider a phased entry with a stop-loss            │
│  anchored below the 20-day average volume level; exit if Z-Score retreats below 1.0        │
│  on the next session.                                                                      │
│                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────╯

================================================
FINAL NEXUS VERDICT
================================================
BUY | High Conviction | RELIANCE.NS
Z-Score: +2.47 | Trend: Bullish | Close: ₹2847.35
================================================
```

---

## 👥 Team |$|ians

<table align="center">
<tr>
  <th>Name</th>
  <th>Role</th>
  <th>Responsibilities</th>
</tr>
<tr>
  <td><b>Garg Parashar</b></td>
  <td>🧠 AI Orchestration Lead</td>
  <td>CrewAI pipeline design, native <code>LLM()</code> integration, LLM prompt engineering, agent persona tuning, LangChain-to-CrewAI migration</td>
</tr>
<tr>
  <td><b>Saurav Kumar</b></td>
  <td>⚙️ Data Engineer</td>
  <td><code>get_nse_data()</code> implementation, yFinance OHLCV pipeline, <code>min_periods=1</code> sparse-data guard, zero-volatility NaN pre-processing</td>
</tr>
<tr>
  <td><b>Pritham_Prajwin_V</b></td>
  <td>📐 Systems Architect</td>
  <td>Z-Score statistical framework, threshold calibration, model-agnostic architecture design, system architecture & technical docs</td>
</tr>
</table>

---

## ⚠️ Disclaimer

> NEXUS is a **research and educational tool** built for the ET GenAI Hackathon 2026. It does not constitute financial advice. All trading decisions involve risk. Past statistical patterns do not guarantee future returns. Always consult a SEBI-registered financial advisor before investing.

---

## 🏆 Submission Details

```
Track    : Democratizing Investment Intelligence
Event    : ET GenAI Hackathon 2026
Team     : |$|ians
Institute: ISI Bangalore
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=gradient&customColorList=0,2,2,5,30&section=footer&reversal=false"/>

*Built with `Groq` and `GitHub` by Team |$|ians at ISI Bangalore*

**[⭐ Star this repo](https://github.com/Zapking-001/NEXUS_Opportunity_Radar) if NEXUS helped you see through the noise.**

</div>
