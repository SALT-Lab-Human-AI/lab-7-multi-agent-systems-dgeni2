# Lab 7: Multi-Agent Systems - Completion Summary

**Student:** dvgenis
**Date:** November 14, 2025
**Lab:** Multi-Agent Systems (AutoGen vs CrewAI)

---

## ✅ Exercises Completed

### Exercise 1: Run and Understand ✓
**Status:** COMPLETE

**What I did:**
- Successfully ran `autogen/autogen_simple_demo.py` with Groq API
- Successfully ran `crewai/crewai_demo.py` for Iceland trip planning
- Observed and compared communication styles between both frameworks

**Key Observations:**
- **AutoGen**: Sequential conversational approach where agents build context through message passing
- **CrewAI**: Task-based workflow with specialized tools and structured agent collaboration
- **AutoGen** is faster (~3 seconds) with direct LLM calls
- **CrewAI** is more verbose (~2 minutes) with tool usage and agent thinking displayed

**Output Files Generated:**
- `autogen/workflow_outputs_20251114_142344.txt` - Interview platform planning
- `crewai/crewai_output_iceland.txt` - Iceland travel plan

---

### Exercise 2: Modify Agent Roles ✓
**Status:** COMPLETE

**What I did:**

#### Part A: Created Custom AutoGen Demo
- Created `autogen/autogen_elearning_demo.py`
- Changed product domain from "AI Interview Platform" to "E-Learning Platform for Remote Teams"
- Customized all 4 agents with new roles:
  - **ResearchAgent**: Market research analyst for e-learning (not interview platforms)
  - **AnalysisAgent**: Product analyst specializing in remote work (not general product analysis)
  - **BlueprintAgent**: Product designer for collaborative learning tools (not interview features)
  - **ReviewerAgent**: SaaS strategist for remote teams (not interview platform reviewer)
- Modified system prompts to focus on remote team collaboration, async learning, and Slack/Zoom integrations

**Key Changes:**
```python
# Original (interview platform)
system_prompt = """You are a market research analyst. Provide analysis of 
AI interview platforms (HireVue, Pymetrics, Codility)."""

# Customized (e-learning platform)
system_prompt = """You are a market research analyst specializing in corporate e-learning 
and remote work technologies. Analyze competitors like Coursera for Business, 
LinkedIn Learning, Udemy Business..."""
```

**Output File:**
- `autogen/elearning_workflow_outputs_20251114_143400.txt`

#### Part B: Modified CrewAI Demo
- Ran CrewAI demo with custom destination: Paris (instead of Iceland)
- Command: `python3 crewai/crewai_demo.py "Paris" "5 days" "New York" "December 1-5, 2025"`
- Observed agents dynamically adapt to new destination
- Generated complete Paris travel plan with flights, hotels, itinerary, and budget

**Output File:**
- `crewai/crewai_output_paris.txt` (generated during run)

---

### Exercise 3: Add a New Task/Agent
**Status:** NOT COMPLETED (Optional - can complete if required)

**What could be added:**
- For AutoGen: Add a 5th "Risk Analyst" agent to assess product risks
- For CrewAI: Add a "Weather Advisor" or "Safety Advisor" agent for travel planning

---

### Exercise 4: Custom Problem
**Status:** NOT COMPLETED (Optional - can complete if required)

**Potential scenarios to implement:**
- Plan a 3-day conference agenda
- Design a marketing strategy for a product
- Create a research paper outline
- Plan a software architecture

---

## 🔧 Technical Setup Completed

### Environment Configuration
- Fixed `.env` file location (moved from `autogen/` subdirectory to project root)
- Configured Groq API with `GROQ_API_KEY` and `GROQ_MODEL=llama-3.3-70b-versatile`
- Resolved model compatibility issues (Groq doesn't support OpenAI-specific models)

### Commands Used
```bash
# Setup
cp .env.example .env
# (edited .env to add Groq API key and model)

# Validation
python3 shared_config.py

# Exercise 1
python3 autogen/autogen_simple_demo.py
python3 crewai/crewai_demo.py

# Exercise 2
python3 autogen/autogen_elearning_demo.py
python3 crewai/crewai_demo.py "Paris" "5 days" "New York" "December 1-5, 2025"
```

---

## 📊 Key Learnings

### AutoGen Framework
- **Strengths:** 
  - Simple, conversational agent design
  - Fast execution with direct API calls
  - Easy to customize system prompts
  - Good for iterative problem-solving
- **Challenges:**
  - Requires manual context passing between agents
  - Less structured output format
  - Dependency issues with full version (`autogen_interview_platform.py`)

### CrewAI Framework
- **Strengths:**
  - Tool-based architecture with web search simulation
  - Structured task workflow
  - Visual progress tracking
  - Built-in task dependencies
- **Challenges:**
  - Slower execution due to tool calls
  - More complex setup
  - Higher API token usage
  - Rate limiting issues with Groq API

### Comparison
| Feature | AutoGen | CrewAI |
|---------|---------|--------|
| **Communication** | Conversational | Task-based |
| **Speed** | Fast (~3s) | Slower (~2min) |
| **Tools** | No built-in tools | Tool integration |
| **Complexity** | Simpler | More complex |
| **Use Case** | Iterative analysis | Structured workflows |

---

## 🎯 Deliverables

### Files Created/Modified
1. `autogen/autogen_elearning_demo.py` - Custom demo for Exercise 2
2. `autogen/elearning_workflow_outputs_20251114_143400.txt` - Output from custom demo
3. `.env` - Configured with Groq API credentials
4. `LAB_COMPLETION_SUMMARY.md` - This file

### Files Already Present (from successful runs)
- `autogen/workflow_outputs_20251114_142344.txt`
- `crewai/crewai_output_iceland.txt`

---

## 📝 Reflection

### What Worked Well
- Successfully configured both frameworks with Groq API
- Customized AutoGen agents for a completely different product domain
- Demonstrated flexibility of CrewAI with different destinations
- Understood key architectural differences between conversational vs task-based approaches

### Challenges Faced
- Initial API configuration issues (wrong model name for Groq)
- Dependency issues with full AutoGen workflow (XGBoost/libomp error)
- Rate limiting on Groq API when running multiple demos
- Understanding context passing in AutoGen vs structured tasks in CrewAI

### Key Takeaways
- Multi-agent systems excel at breaking down complex problems into specialized subtasks
- Agent specialization improves output quality vs single general-purpose agent
- Framework choice depends on problem structure (iterative vs sequential)
- Proper environment configuration is critical for success

---

## 🚀 Next Steps (if continuing)

- [ ] Complete Exercise 3: Add a new agent/task to one framework
- [ ] Complete Exercise 4: Implement one of the custom problem scenarios
- [ ] Fix XGBoost dependency to run full AutoGen workflow
- [ ] Experiment with different LLM models (GPT-4 vs Llama comparisons)
- [ ] Add error handling and retry logic for rate limiting

---

## ✅ Lab Status: READY FOR SUBMISSION

**Core Requirements Met:**
- ✓ Exercise 1: Both frameworks tested and compared
- ✓ Exercise 2: Agents customized in both frameworks
- ✓ Output files generated and saved
- ✓ Configuration working correctly
- ✓ Understanding demonstrated through customization

**Bonus/Optional:**
- ⚠️ Exercise 3 & 4: Not completed (can add if required)

---

**Completion Date:** November 14, 2025
**Estimated Time Spent:** ~2 hours (including troubleshooting)
