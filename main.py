import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from data_layer import get_nse_data

# Load environment variables (.env must contain GROQ_API_KEY)
load_dotenv()

# 1. Initialize Native CrewAI LLM (Bypasses Pydantic/LangChain errors)
groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.1
)

# 2. Define Agents
quant_analyst = Agent(
    role='Lead Quant Researcher',
    goal='Analyze market data and filter noise using Volume Z-Scores. Flag any Z-Score > 2.0 as a significant breakout.',
    backstory='An ISI-trained statistician specialized in high-frequency data and mathematical filtering.',
    llm=groq_llm,
    verbose=True,
    allow_delegation=False
)

market_strategist = Agent(
    role='Indian Market Strategist',
    goal='Provide actionable NSE/BSE trade verdicts based on the Quant Researcher\'s statistical analysis.',
    backstory='Expert in Indian market liquidity, circuit limits, and institutional retail traps.',
    llm=groq_llm,
    verbose=True,
    allow_delegation=False
)

# 3. Main Execution
def run_nexus_radar(ticker: str):
    print(f"\n--- Initiating NEXUS Opportunity Radar for {ticker} ---")
    
    # Fetch real data
    print("Fetching market data and calculating Z-Scores...")
    market_data = get_nse_data(ticker)
    
    # Define Tasks
    quant_task = Task(
        description=f"Analyze the following market data for {ticker}. Focus heavily on the Volume Z-Score. \nData:\n{market_data}\n\nDetermine if this is a true breakout or a retail bull trap.",
        expected_output="A statistical summary stating whether the Volume Z-Score indicates a significant anomaly (> 2.0) and the mathematical confidence.",
        agent=quant_analyst
    )

    strategist_task = Task(
        description=f"Review the Quant Researcher's statistical summary for {ticker}. Formulate a final, actionable trading verdict (BUY, SELL, or HOLD/TRAP).",
        expected_output="A concise final verdict with clear risk management advice.",
        agent=market_strategist
    )

    # Assemble Crew
    nexus_crew = Crew(
        agents=[quant_analyst, market_strategist],
        tasks=[quant_task, strategist_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = nexus_crew.kickoff()
    
    print("\n================================================")
    print("FINAL NEXUS VERDICT")
    print("================================================")
    print(result)

if __name__ == "__main__":
    # Target stock for your 90-second demo
    TARGET_STOCK = "RELIANCE.NS" 
    run_nexus_radar(TARGET_STOCK)