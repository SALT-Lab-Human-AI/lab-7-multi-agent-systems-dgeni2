"""
AutoGen Demo with 5 Agents - Exercise 3
Adding a Pricing Strategy Agent to the workflow

This demonstrates how to extend the AutoGen workflow with additional specialized agents.
"""

from datetime import datetime
from config import Config
import json

try:
    from openai import OpenAI
except ImportError:
    print("ERROR: OpenAI client is not installed!")
    print("Please run: pip install -r ../requirements.txt")
    exit(1)


class FiveAgentWorkflow:
    """Extended workflow with 5 agents including a Pricing Strategy Agent"""

    def __init__(self):
        """Initialize the workflow"""
        if not Config.validate_setup():
            print("ERROR: Configuration validation failed!")
            exit(1)

        self.client = OpenAI(api_key=Config.API_KEY, base_url=Config.API_BASE)
        self.outputs = {}
        self.model = Config.OPENAI_MODEL

    def run(self):
        """Execute the complete workflow"""
        print("\n" + "="*80)
        print("AUTOGEN 5-AGENT WORKFLOW - EXERCISE 3")
        print("="*80)
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Model: {self.model}")
        print("NEW: Added Pricing Strategy Agent as 5th agent\n")

        # Phase 1: Research
        self.phase_research()

        # Phase 2: Analysis
        self.phase_analysis()

        # Phase 3: Blueprint
        self.phase_blueprint()

        # Phase 4: Pricing (NEW!)
        self.phase_pricing()

        # Phase 5: Review
        self.phase_review()

        # Summary
        self.print_summary()

    def phase_research(self):
        """Phase 1: Market Research"""
        print("\n" + "="*80)
        print("PHASE 1: MARKET RESEARCH")
        print("="*80)
        print("[ResearchAgent is analyzing the market...]")

        system_prompt = """You are a market research analyst. Provide a brief analysis of
3 competitors in AI interview platforms (HireVue, Pymetrics, Codility).
List their key features and identify market gaps in 150 words."""

        user_message = "Analyze the current market for AI-powered interview platforms."

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["research"] = response.choices[0].message.content
        print("\n[ResearchAgent Output]")
        print(self.outputs["research"])

    def phase_analysis(self):
        """Phase 2: Opportunity Analysis"""
        print("\n" + "="*80)
        print("PHASE 2: OPPORTUNITY ANALYSIS")
        print("="*80)
        print("[AnalysisAgent is identifying opportunities...]")

        system_prompt = """You are a product analyst. Based on the market research provided,
identify 3 key market opportunities or gaps for a new AI interview platform.
Be concise in 150 words."""

        user_message = f"""Market research findings:
{self.outputs['research']}

Now identify market opportunities and gaps."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["analysis"] = response.choices[0].message.content
        print("\n[AnalysisAgent Output]")
        print(self.outputs["analysis"])

    def phase_blueprint(self):
        """Phase 3: Product Blueprint"""
        print("\n" + "="*80)
        print("PHASE 3: PRODUCT BLUEPRINT")
        print("="*80)
        print("[BlueprintAgent is designing the product...]")

        system_prompt = """You are a product designer. Based on the market analysis and opportunities,
create a brief product blueprint including:
- Key features (3-5)
- User journey (2-3 steps)
Keep it concise - 150 words."""

        user_message = f"""Market Analysis:
{self.outputs['analysis']}

Create a product blueprint for our platform."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["blueprint"] = response.choices[0].message.content
        print("\n[BlueprintAgent Output]")
        print(self.outputs["blueprint"])

    def phase_pricing(self):
        """Phase 4: Pricing Strategy (NEW AGENT!)"""
        print("\n" + "="*80)
        print("PHASE 4: PRICING STRATEGY (NEW!)")
        print("="*80)
        print("[PricingAgent is developing pricing strategy...]")

        system_prompt = """You are a pricing strategist for B2B SaaS products. Based on the 
product blueprint provided, develop a pricing strategy including:
- 3 pricing tiers (Starter, Professional, Enterprise)
- Key features in each tier
- Suggested price points
- Reasoning for the pricing structure
Be concise - 150 words."""

        user_message = f"""Product Blueprint:
{self.outputs['blueprint']}

Develop a pricing strategy for this AI interview platform."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["pricing"] = response.choices[0].message.content
        print("\n[PricingAgent Output - NEW AGENT!]")
        print(self.outputs["pricing"])

    def phase_review(self):
        """Phase 5: Strategic Review"""
        print("\n" + "="*80)
        print("PHASE 5: STRATEGIC REVIEW")
        print("="*80)
        print("[ReviewerAgent is providing recommendations...]")

        system_prompt = """You are a product reviewer and strategist. Review the product blueprint
and pricing strategy, then provide 3 strategic recommendations for success.
Be concise - 150 words."""

        user_message = f"""Product Blueprint:
{self.outputs['blueprint']}

Pricing Strategy:
{self.outputs['pricing']}

Provide strategic review and recommendations."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["review"] = response.choices[0].message.content
        print("\n[ReviewerAgent Output]")
        print(self.outputs["review"])

    def print_summary(self):
        """Print final summary"""
        print("\n" + "="*80)
        print("FINAL SUMMARY")
        print("="*80)

        print("""
This workflow demonstrated a 5-AGENT collaboration (EXERCISE 3):
1. ResearchAgent - Analyzed the market
2. AnalysisAgent - Identified opportunities
3. BlueprintAgent - Designed the product
4. PricingAgent - Developed pricing strategy (NEW!)
5. ReviewerAgent - Provided strategic recommendations

The NEW PricingAgent adds critical business model expertise to the workflow,
ensuring the product has a viable monetization strategy from the start.
""")

        # Print full results
        print("\n" + "="*80)
        print("FULL RESULTS - ALL 5 PHASES")
        print("="*80)
        
        print("\n" + "-"*80)
        print("PHASE 1: MARKET RESEARCH")
        print("-"*80)
        print(self.outputs["research"])
        
        print("\n" + "-"*80)
        print("PHASE 2: OPPORTUNITY ANALYSIS")
        print("-"*80)
        print(self.outputs["analysis"])
        
        print("\n" + "-"*80)
        print("PHASE 3: PRODUCT BLUEPRINT")
        print("-"*80)
        print(self.outputs["blueprint"])
        
        print("\n" + "-"*80)
        print("PHASE 4: PRICING STRATEGY (NEW!)")
        print("-"*80)
        print(self.outputs["pricing"])
        
        print("\n" + "-"*80)
        print("PHASE 5: STRATEGIC REVIEW")
        print("-"*80)
        print(self.outputs["review"])

        # Save to file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"5agent_workflow_outputs_{timestamp}.txt"
        with open(output_file, 'w') as f:
            f.write("="*80 + "\n")
            f.write("AUTOGEN 5-AGENT WORKFLOW - EXERCISE 3 RESULTS\n")
            f.write("="*80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Model: {self.model}\n\n")
            f.write("ADDED: PricingAgent as 5th agent for pricing strategy\n\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 1: MARKET RESEARCH\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["research"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 2: OPPORTUNITY ANALYSIS\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["analysis"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 3: PRODUCT BLUEPRINT\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["blueprint"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 4: PRICING STRATEGY (NEW AGENT!)\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["pricing"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 5: STRATEGIC REVIEW\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["review"] + "\n")
        
        print(f"\n💾 Full results saved to: {output_file}")
        print(f"\nEnd Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)


if __name__ == "__main__":
    try:
        workflow = FiveAgentWorkflow()
        workflow.run()
        print("\n✅ 5-agent workflow completed successfully!")
        print("\n📝 EXERCISE 3 COMPLETE - Added PricingAgent as 5th agent!")
    except Exception as e:
        print(f"\n❌ Error during workflow execution: {str(e)}")
        import traceback
        traceback.print_exc()
