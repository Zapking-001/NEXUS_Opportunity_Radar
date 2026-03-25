import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from data_layer import fetch_market_anomaly

# 1. UNIVERSAL CONFIGURATION
load_dotenv()
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY")

# FLAGSHIP MODEL: llama-3.3-70b-versatile
os.environ["OPENAI_MODEL_NAME"] = "llama-3.3-70b-versatile"
os.environ["CREWAI_TRACING_ENABLED"] = "false"

# 2. AGENT DEFINITIONS
quant_analyst = Agent(
    role='Lead Quant Researcher',
    goal='Identify if mathematical anomalies represent a high-probability breakout.',
    backstory="""Expert in statistical arbitrage and volatility modeling. 
    Specializes in interpreting Volume Z-Scores and SMA deviations to identify 
    non-random market movements.""",
    verbose=True,
    allow_delegation=False
)

strategist = Agent(
    role='Indian Market Strategist',
    goal='Translate technical signals into actionable advice for retail investors.',
    backstory="""Veteran of the Indian equity markets with deep knowledge of 
    NSE liquidity cycles. Expert at synthesizing quant data into risk-managed 
    investment narratives.""",
    verbose=True,
    allow_delegation=False
)

# 3. LIVE DATA INGESTION
symbol = "RELIANCE"
market_stats = fetch_market_anomaly(symbol)

# 4. TASK DEFINITIONS
# Using r""" to handle the backslashes in the LaTeX formula correctly
task_analysis = Task(
    description=r"""Analyze the following metrics for {symbol}: {market_stats}. 
    Evaluate the Volume Z-Score ($Z = (V_t - \mu)/\sigma$). 
    If Z > 2.0, determine if the Bullish trend is sustainable.""".format(symbol=symbol, market_stats=market_stats),
    agent=quant_analyst,
    expected_output="A technical assessment of momentum and statistical significance."
)

task_recommendation = Task(
    description="""Based on the Lead Quant's assessment, provide a 2-sentence 'Action 
    Recommendation' for an Indian retail investor. Be direct: Watch, Wait, or Buy.""",
    agent=strategist,
    expected_output="A clear 'Wait' or 'Watch' recommendation with a brief reason."
)

# 5. ASSEMBLE THE CREW
nexus_crew = Crew(
    agents=[quant_analyst, strategist],
    tasks=[task_analysis, task_recommendation],
    process=Process.sequential
)

print(f"\n[NEXUS] AI Agents are analyzing {symbol}...")
try:
    result = nexus_crew.kickoff()
    
    print("\n" + "="*50)
    print("FINAL OPPORTUNITY RADAR REPORT")
    print("="*50)
    print(result)
except Exception as e:
    print(f"An error occurred during execution: {e}")