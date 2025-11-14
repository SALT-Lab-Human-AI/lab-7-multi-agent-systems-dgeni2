"""
Custom AutoGen Demo - E-Learning Platform for Remote Teams
Exercise 2: Modified version with different product and customized agents

This demonstrates how to customize the AutoGen workflow for a different use case.
"""

from datetime import datetime
from config import Config
import json

# Try to import OpenAI client
try:
    from openai import OpenAI
except ImportError:
    print("ERROR: OpenAI client is not installed!")
    print("Please run: pip install -r ../requirements.txt")
    exit(1)


class ELearningPlatformWorkflow:
    """Simplified workflow for e-learning platform planning"""

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
        print("AUTOGEN E-LEARNING PLATFORM WORKFLOW - CUSTOM DEMO")
        print("="*80)
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Model: {self.model}\n")

        # Phase 1: Research
        self.phase_research()

        # Phase 2: Analysis
        self.phase_analysis()

        # Phase 3: Blueprint
        self.phase_blueprint()

        # Phase 4: Review
        self.phase_review()

        # Summary
        self.print_summary()

    def phase_research(self):
        """Phase 1: Market Research - CUSTOMIZED"""
        print("\n" + "="*80)
        print("PHASE 1: MARKET RESEARCH")
        print("="*80)
        print("[ResearchAgent is analyzing the e-learning market...]")

        # CUSTOMIZED: Different system prompt for e-learning market
        system_prompt = """You are a market research analyst specializing in corporate e-learning 
and remote work technologies. Provide a brief analysis of 3 major competitors in the 
enterprise e-learning space (such as Coursera for Business, LinkedIn Learning, Udemy Business).
List their key features, pricing models, and identify market gaps for remote teams in 150 words."""

        # CUSTOMIZED: Different user message for e-learning
        user_message = "Analyze the current market for corporate e-learning platforms targeting remote teams."

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
        """Phase 2: Opportunity Analysis - CUSTOMIZED"""
        print("\n" + "="*80)
        print("PHASE 2: OPPORTUNITY ANALYSIS")
        print("="*80)
        print("[AnalysisAgent is identifying opportunities for remote teams...]")

        # CUSTOMIZED: Focus on remote team learning needs
        system_prompt = """You are a product analyst specializing in remote work and distributed teams.
Based on the market research provided, identify 3 key opportunities for an e-learning platform
specifically designed for remote teams. Focus on collaboration, async learning, and team building.
Be concise in 150 words."""

        user_message = f"""Market research findings:
{self.outputs['research']}

Now identify market opportunities and gaps for remote team e-learning."""

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
        """Phase 3: Product Blueprint - CUSTOMIZED"""
        print("\n" + "="*80)
        print("PHASE 3: PRODUCT BLUEPRINT")
        print("="*80)
        print("[BlueprintAgent is designing the e-learning platform...]")

        # CUSTOMIZED: E-learning platform features
        system_prompt = """You are a product designer specializing in collaborative learning tools.
Based on the market analysis and opportunities, create a brief product blueprint including:
- Key features (3-5) focused on remote team collaboration
- User journey (2-3 steps) for a remote team learning experience
- Integration points with remote work tools (Slack, Zoom, etc.)
Keep it concise - 150 words."""

        user_message = f"""Market Analysis:
{self.outputs['analysis']}

Create a product blueprint for our remote team e-learning platform."""

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

    def phase_review(self):
        """Phase 4: Strategic Review - CUSTOMIZED"""
        print("\n" + "="*80)
        print("PHASE 4: STRATEGIC REVIEW")
        print("="*80)
        print("[ReviewerAgent is providing recommendations...]")

        # CUSTOMIZED: Focus on remote work adoption
        system_prompt = """You are a product reviewer and strategist specializing in SaaS for remote teams.
Review the product blueprint and provide 3 strategic recommendations for successful adoption
by distributed teams. Consider remote work challenges and team engagement.
Be concise - 150 words."""

        user_message = f"""Product Blueprint:
{self.outputs['blueprint']}

Provide strategic review and recommendations for remote team adoption."""

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
This workflow demonstrated a 4-agent collaboration for E-LEARNING PLATFORM:
1. ResearchAgent - Analyzed the corporate e-learning market
2. AnalysisAgent - Identified opportunities for remote teams
3. BlueprintAgent - Designed platform features with remote work focus
4. ReviewerAgent - Provided strategic recommendations for adoption

This is a CUSTOMIZED version (Exercise 2) with:
- Different product domain (e-learning vs interview platform)
- Customized agent roles and expertise
- Modified system prompts for each phase
- Focus on remote teams and collaboration
""")

        # Print full results
        print("\n" + "="*80)
        print("FULL RESULTS - ALL PHASES")
        print("="*80)
        
        print("\n" + "-"*80)
        print("PHASE 1: MARKET RESEARCH (Full Output)")
        print("-"*80)
        print(self.outputs["research"])
        
        print("\n" + "-"*80)
        print("PHASE 2: OPPORTUNITY ANALYSIS (Full Output)")
        print("-"*80)
        print(self.outputs["analysis"])
        
        print("\n" + "-"*80)
        print("PHASE 3: PRODUCT BLUEPRINT (Full Output)")
        print("-"*80)
        print(self.outputs["blueprint"])
        
        print("\n" + "-"*80)
        print("PHASE 4: STRATEGIC REVIEW (Full Output)")
        print("-"*80)
        print(self.outputs["review"])

        # Save to file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"elearning_workflow_outputs_{timestamp}.txt"
        with open(output_file, 'w') as f:
            f.write("="*80 + "\n")
            f.write("AUTOGEN E-LEARNING PLATFORM WORKFLOW - CUSTOM RESULTS\n")
            f.write("="*80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Model: {self.model}\n\n")
            f.write("Exercise 2: Customized AutoGen Demo\n")
            f.write("Product: E-Learning Platform for Remote Teams\n\n")
            
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
            f.write("PHASE 4: STRATEGIC REVIEW\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["review"] + "\n")
        
        print(f"\n💾 Full results saved to: {output_file}")
        print(f"\nEnd Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)


if __name__ == "__main__":
    try:
        workflow = ELearningPlatformWorkflow()
        workflow.run()
        print("\n✅ Custom workflow completed successfully!")
        print("\n📝 EXERCISE 2 COMPLETE - You customized AutoGen for a new product domain!")
    except Exception as e:
        print(f"\n❌ Error during workflow execution: {str(e)}")
        import traceback
        traceback.print_exc()
