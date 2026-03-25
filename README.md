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
│  🕵️ AGENT 1: Lead Quant Researcher                              |
│  └─ Applies Z-Score gating. Flags signal or noise.              │
│                          │                                      │
│                          ▼                                      │
│  📈 AGENT 2: Indian Market Strategist                           │
│  └─ Translates quant signal into NSE/BSE execution plan         │
│                          │                                      │
│                          ▼                                      │
│  📤 OUTPUT                                                      │
│  └─ Validated Action: BUY / WATCH / AVOID + Rationale           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🧠 The Math Behind the Magic

Traditional volume bars are noisy and context-free. NEXUS replaces them with **Volume Z-Score Analysis** — a rigorous statistical framework that answers one question: *Is today's volume genuinely unusual?*

### Step 1 — Historical Baseline

We establish the 20-day rolling statistics:

$$\mu_{20} = \frac{1}{20}\sum_{i=1}^{20} V_i \qquad \sigma_{20} = \sqrt{\frac{1}{20}\sum_{i=1}^{20}(V_i - \mu_{20})^2}$$

### Step 2 — Z-Score Signal

$$\boxed{Z = \frac{V_{\text{today}} - \mu_{20}}{\sigma_{20}}}$$

### Step 3 — Signal Interpretation

| Z-Score Range | Percentile | Signal | Action |
|:---:|:---:|:---|:---:|
| `Z > 2.0` | Top 2.5% | 🟢 High Institutional Conviction | **BUY** |
| `0 < Z ≤ 2.0` | Above Average | 🟡 Moderate Activity  | **WATCH** |
| `Z ≤ 0` | Below Average | 🔴 Low Conviction / Noise | **AVOID** |

> **Why Z-Score?** It normalizes volume across different market caps, sectors, and trading sessions — eliminating the raw-number bias that misleads most retail tools.

---

## 🤖 Multi-Agent Architecture

Powered by **Llama 3.3 70B** on **Groq's LPU** for sub-second inference, NEXUS runs two specialized AI agents in a sequential crew:

<table>
<tr>
<td width="50%" valign="top">

### 🕵️‍♂️ Agent 1
## Lead Quant Researcher

**Persona:** Cold. Mathematical. Unforgiving.

**Mandate:** Acts as the strict logical gatekeeper. Zero tolerance for narratives — only the Z-Score verdict matters.

**Core Logic:**
- Ingests raw OHLCV data
- Computes the volume Z-Score
- Classifies signal as **High Conviction**, **Moderate**, or **Noise**
- Outputs a structured quant report

**Guardrail:** If `Z < 2.0`, the asset is flagged as *"Insufficient Institutional Participation"* regardless of price action.

</td>
<td width="50%" valign="top">

### 📈 Agent 2
## Indian Market Strategist

**Persona:** Seasoned. Pragmatic. Risk-aware.

**Mandate:** Takes the quant report and translates it into a risk-mitigated execution strategy tuned to the volatile realities of NSE/BSE microstructure.

**Core Logic:**
- Reads Agent 1's conviction rating
- Factors in circuit limits, F&O expiry, and India VIX context
- Defines entry zones, stop-loss levels, and position sizing logic
- Delivers the final **BUY / WATCH / AVOID** verdict

**Guardrail:** Never overrides a `AVOID` signal from Agent 1.

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|:---|:---|:---|
| 🧠 **LLM Engine** | Groq + Llama 3.3 70B | Sub-second inference for agent reasoning |
| 🤖 **Orchestration** | CrewAI | Multi-agent task delegation and pipeline control |
| 📊 **Data Layer** | yFinance + Pandas + NumPy | Live OHLCV ingestion and statistical computation |
| 🐍 **Runtime** | Python 3.11+ | Core execution environment |
| 🌐 **Markets** | NSE / BSE (India) | Target exchange universe |

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
pip install -r requirements.txt
```

**4. Set your API key**
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

When prompted, enter any NSE/BSE ticker:
```
> Enter ticker symbol: RELIANCE.NS
```

---

## 📊 Sample Output
 
```
[SYSTEM] Scanning RELIANCE.NS for anomalies...
[NEXUS] AI Agents are analyzing RELIANCE...
 
╭────────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────────╮
│                                                                                                                      │
│  Agent: Lead Quant Researcher                                                                                        │
│                                                                                                                      │
│  Task: Analyze the following metrics for RELIANCE: {'ticker': 'RELIANCE', 'price': np.float64(1415.2), 'sma_20':     │
│  np.float64(1397.21), 'vol_zscore': np.float64(-1.83), 'status': 'Normal Activity', 'trend': 'Bullish'}.             │
│      Evaluate the Volume Z-Score ($Z = (V_t - \mu)/\sigma$).                                                         │
│      If Z > 2.0, determine if the Bullish trend is sustainable.                                                      │
│                                                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
 
╭─────────────────────────────────────────────── ✅ Agent Final Answer ────────────────────────────────────────────────╮
│                                                                                                                       │
│  Agent: Lead Quant Researcher                                                                                         │
│                                                                                                                       │
│  Final Answer:                                                                                                        │
│  The Volume Z-Score for RELIANCE is -1.83, indicating that the current volume is 1.83 standard deviations below       │
│  the mean. This does not meet the Z > 2.0 threshold for high institutional conviction. While the price at 1415.2      │
│  is above the SMA_20 of 1397.21 (Bullish), the low volume participation suggests the trend lacks strong market        │
│  conviction and may not be sustainable based solely on volume analysis.                                               │
│                                                                                                                       │
│  Recommendation: Monitor volume and other technical indicators for signs of increasing market participation           │
│  to support the continuation of the Bullish trend.                                                                    │
│                                                                                                                       │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
 
╭────────────────────────────────────────────────── 🤖 Agent Started ──────────────────────────────────────────────────╮
│                                                                                                                      │
│  Agent: Indian Market Strategist                                                                                     │
│                                                                                                                      │
│  Task: Based on the Lead Quant's assessment, provide a 2-sentence 'Action                                            │
│      Recommendation' for an Indian retail investor. Be direct: Watch, Wait, or Buy.                                  │
│                                                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
 
╭─────────────────────────────────────────────── ✅ Agent Final Answer ────────────────────────────────────────────────╮
│                                                                                                                      │
│  Agent: Indian Market Strategist                                                                                     │
│                                                                                                                      │
│  Final Answer:                                                                                                       │
│  Wait for RELIANCE to demonstrate higher volume participation, as indicated by a Volume Z-Score greater than 2.0,    │
│  to confirm the sustainability of the current Bullish trend before considering a buy position. This cautious         │
│  approach allows investors to monitor the stock's behavior and potentially avoid entering a position that lacks      │
│  broad market conviction, thereby managing their risk more effectively.                                              │
│                                                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
 
================================================================
                FINAL OPPORTUNITY RADAR REPORT
================================================================
Wait for RELIANCE to demonstrate higher volume participation,
as indicated by a Volume Z-Score greater than 2.0, to confirm
the sustainability of the current Bullish trend before
considering a buy position.
================================================================
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
  <td>CrewAI pipeline design, LLM prompt engineering, agent persona tuning</td>
</tr>
</tr>
<tr>
  <td><b>Saurav Kumar</b></td>
  <td>⚙️ Data Engineer</td>
  <td>yFinance data pipeline, OHLCV processing, dependency management & quant logic</td>
</tr>
<tr>
  <td><b>Pritham Prajwin</b></td>
  <td>📐 Systems Architect</td>
  <td>Lead Z-Score framework, system architecture, technical docs & product strategy</td>
</table>

---

## ⚠️ Disclaimer

> NEXUS is a **research and educational tool** built for the ET GenAI Hackathon 2026. It does not constitute financial advice. All trading decisions involve risk. Past statistical patterns do not guarantee future returns. Always consult a SEBI-registered financial advisor before investing.

---

## 🏆 Submission Details

```
Track   : Democratizing Investment Intelligence
Event   : ET GenAI Hackathon 2026
Team    : |$|ians
Institute: ISI Bangalore
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=gradient&customColorList=0,2,2,5,30&section=footer&reversal=false"/>

*Built with `Groq` and `GitHub` by Team |$|ians at ISI Bangalore*

**[⭐ Star this repo](https://github.com/Zapking-001/NEXUS_Opportunity_Radar) if NEXUS helped you see through the noise.**

</div>
