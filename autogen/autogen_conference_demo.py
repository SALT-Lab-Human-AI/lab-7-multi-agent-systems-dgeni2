"""
Exercise 4: Custom Problem - 3-Day Conference Planning System
Using AutoGen to plan a complete AI/Tech conference

This demonstrates applying multi-agent systems to a different domain:
conference organization and event planning.
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


class ConferencePlanningWorkflow:
    """Multi-agent workflow for planning a 3-day tech conference"""

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
        print("CONFERENCE PLANNING WORKFLOW - EXERCISE 4")
        print("="*80)
        print("Custom Problem: Plan a 3-Day AI & Technology Conference")
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Model: {self.model}\n")

        # Phase 1: Theme & Topics Research
        self.phase_theme_research()

        # Phase 2: Speaker & Session Planning
        self.phase_speaker_planning()

        # Phase 3: Logistics & Venue
        self.phase_logistics()

        # Phase 4: Marketing & Outreach
        self.phase_marketing()

        # Summary
        self.print_summary()

    def phase_theme_research(self):
        """Phase 1: Conference Theme & Topics Research"""
        print("\n" + "="*80)
        print("PHASE 1: CONFERENCE THEME & TOPICS RESEARCH")
        print("="*80)
        print("[ThemeResearchAgent is analyzing current tech trends...]")

        system_prompt = """You are a conference planning expert and tech trend analyst.
Research and propose a compelling conference theme for a 3-day AI & Technology conference.
Include:
- Main conference theme
- 5 key topic tracks (AI, Cloud, Security, DevOps, etc.)
- Target audience
- Current trends that make this timely
Be concise - 150 words."""

        user_message = "Propose a conference theme and key topics for a 3-day AI & Technology conference in 2026."

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["theme"] = response.choices[0].message.content
        print("\n[ThemeResearchAgent Output]")
        print(self.outputs["theme"])

    def phase_speaker_planning(self):
        """Phase 2: Speaker & Session Planning"""
        print("\n" + "="*80)
        print("PHASE 2: SPEAKER & SESSION PLANNING")
        print("="*80)
        print("[SpeakerPlanningAgent is designing the agenda...]")

        system_prompt = """You are a conference program director. Based on the conference 
theme and topics, create a 3-day agenda including:
- Day 1, 2, 3 session breakdown
- Types of sessions (keynotes, workshops, panels)
- Suggested speaker profiles (job titles, not names)
- Session timing (morning/afternoon structure)
Be concise - 150 words."""

        user_message = f"""Conference Theme & Topics:
{self.outputs['theme']}

Create a detailed 3-day conference agenda."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["agenda"] = response.choices[0].message.content
        print("\n[SpeakerPlanningAgent Output]")
        print(self.outputs["agenda"])

    def phase_logistics(self):
        """Phase 3: Logistics & Venue Planning"""
        print("\n" + "="*80)
        print("PHASE 3: LOGISTICS & VENUE PLANNING")
        print("="*80)
        print("[LogisticsAgent is planning venue and operations...]")

        system_prompt = """You are an event logistics coordinator. Based on the conference 
agenda, plan the logistics including:
- Venue requirements (room sizes, tech setup)
- Catering schedule (coffee breaks, lunch, networking)
- Registration and check-in process
- Technical requirements (AV, WiFi, streaming)
Be concise - 150 words."""

        user_message = f"""Conference Agenda:
{self.outputs['agenda']}

Plan the logistics and venue requirements."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["logistics"] = response.choices[0].message.content
        print("\n[LogisticsAgent Output]")
        print(self.outputs["logistics"])

    def phase_marketing(self):
        """Phase 4: Marketing & Outreach Strategy"""
        print("\n" + "="*80)
        print("PHASE 4: MARKETING & OUTREACH STRATEGY")
        print("="*80)
        print("[MarketingAgent is developing promotion strategy...]")

        system_prompt = """You are a conference marketing strategist. Based on the conference 
details, create a marketing plan including:
- Key marketing messages and value propositions
- Target channels (social media, email, partnerships)
- Early bird and regular pricing strategy
- Timeline for promotion (6 months, 3 months, 1 month before)
Be concise - 150 words."""

        user_message = f"""Conference Theme:
{self.outputs['theme']}

Conference Agenda:
{self.outputs['agenda']}

Develop a marketing and outreach strategy."""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=Config.AGENT_TEMPERATURE,
            max_tokens=Config.AGENT_MAX_TOKENS,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        self.outputs["marketing"] = response.choices[0].message.content
        print("\n[MarketingAgent Output]")
        print(self.outputs["marketing"])

    def print_summary(self):
        """Print final summary"""
        print("\n" + "="*80)
        print("FINAL SUMMARY - COMPLETE CONFERENCE PLAN")
        print("="*80)

        print("""
This workflow demonstrated a 4-AGENT collaboration for CONFERENCE PLANNING:
1. ThemeResearchAgent - Researched trends and proposed conference theme
2. SpeakerPlanningAgent - Created 3-day agenda with session structure
3. LogisticsAgent - Planned venue requirements and operations
4. MarketingAgent - Developed marketing and outreach strategy

EXERCISE 4 COMPLETE: Custom problem solving with multi-agent system
Domain: Event planning and conference organization
Result: Complete 3-day conference plan ready for execution
""")

        # Print full results
        print("\n" + "="*80)
        print("COMPLETE CONFERENCE PLAN - ALL PHASES")
        print("="*80)
        
        print("\n" + "-"*80)
        print("PHASE 1: CONFERENCE THEME & TOPICS")
        print("-"*80)
        print(self.outputs["theme"])
        
        print("\n" + "-"*80)
        print("PHASE 2: 3-DAY AGENDA & SESSIONS")
        print("-"*80)
        print(self.outputs["agenda"])
        
        print("\n" + "-"*80)
        print("PHASE 3: LOGISTICS & VENUE")
        print("-"*80)
        print(self.outputs["logistics"])
        
        print("\n" + "-"*80)
        print("PHASE 4: MARKETING STRATEGY")
        print("-"*80)
        print(self.outputs["marketing"])

        # Save to file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"conference_planning_{timestamp}.txt"
        with open(output_file, 'w') as f:
            f.write("="*80 + "\n")
            f.write("3-DAY AI & TECH CONFERENCE PLAN - EXERCISE 4\n")
            f.write("="*80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Model: {self.model}\n\n")
            f.write("Custom Problem: Conference Planning System\n")
            f.write("Domain: Event Organization & Management\n\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 1: CONFERENCE THEME & TOPICS\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["theme"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 2: 3-DAY AGENDA & SESSIONS\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["agenda"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 3: LOGISTICS & VENUE\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["logistics"] + "\n")
            
            f.write("\n" + "-"*80 + "\n")
            f.write("PHASE 4: MARKETING STRATEGY\n")
            f.write("-"*80 + "\n")
            f.write(self.outputs["marketing"] + "\n")
        
        print(f"\n💾 Full conference plan saved to: {output_file}")
        print(f"\nEnd Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)


if __name__ == "__main__":
    try:
        workflow = ConferencePlanningWorkflow()
        workflow.run()
        print("\n✅ Conference planning workflow completed successfully!")
        print("\n📝 EXERCISE 4 COMPLETE - Custom problem: Conference planning system!")
    except Exception as e:
        print(f"\n❌ Error during workflow execution: {str(e)}")
        import traceback
        traceback.print_exc()
