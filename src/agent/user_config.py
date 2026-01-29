"""
User Configuration for Auto Cover Letter Creator
=================================================

This file contains user-specific information used for generating resumes and cover letters.
To customize for a different user, modify the values in the UserConfig class below.

IMPORTANT: Keep all information accurate and factual. Do not add false information.
"""

from datetime import datetime


class UserConfig:
    """
    User configuration for resume and cover letter generation.
    
    Modify these values to customize for your own use.
    """
    
    # Personal Information
    FULL_NAME = "Aditya Ghanashyam Ladawa"
    LOCATION = "Braunschweig, Germany"
    PHONE = "+49 15510 030840"
    EMAIL = "adityaladawa12@gmail.com"
    
    # Professional Links
    LINKEDIN_URL = "https://www.linkedin.com/in/aditya-ladawa"
    GITHUB_URL = "https://github.com/aditya-ladawa"
    PORTFOLIO_URL = ""  # Optional: Add if you have a portfolio website
    
    # File Naming
    # This will be used in PDF filenames: {NAME_FOR_FILES}_{resume|cover_letter}_{YEAR}.pdf
    NAME_FOR_FILES = "ADITYA_LADAWA"
    
    # Output Directory Configuration
    # Base directory where all job applications will be saved
    BASE_OUTPUT_DIR = "/home/aditya-ladawa/Aditya/FOR JOB/Jan2026_jobs"
    
    # Current year for file naming
    CURRENT_YEAR = datetime.now().year
    
    # Languages for cover letter generation
    GENERATE_ENGLISH = True
    GENERATE_GERMAN = True
    
    # Resume Path (for reference when tailoring)
    RESUME_LATEX_PATH = "src/agent/templates/resume_template.tex"
    
    # Professional Profile Text (used in agent prompts)
    # PROFESSIONAL_PROFILE = """
    # Aditya Ghanashyam Ladawa is an AI and backend engineer whose work philosophy centers on system ownership, automation, and scalable execution. He treats code as an asset and inefficiency as a structural failure. His cognition is optimized for throughput, and he codes 15+ daily to maintain deep fluency in agentic architecture, infrastructure logic, and automation pipelines.
    # 
    # He specializes in building self-replacing agentic systems using LangGraph, LangChain, and LangSmith—favoring deterministic multi-agent workflows with explicit state control, memory orchestration, and persistent, asynchronous execution. These systems autonomously handle document retrieval, multimodal processing, summarization, and insight generation without runtime LLM dependency.
    # 
    # His backend engineering stack is centered on Python and FastAPI, with Postgres, Redis, and MongoDB for data storage. In RAG-based architectures, he uses Qdrant or FAISS and ensures tight control over memory and pipeline flow. His principles enforce modularity, testability, and production readiness—no demos, only robust deployments.
    # 
    # In ML, he develops models using TensorFlow, PyTorch, and scikit-learn, integrating them into end-to-end pipelines without black-box reliance. His computer vision stack includes OpenCV, FFmpeg, PIL, Real-ESRGAN, CycleGAN, and MediaPipe, with applications in real-time video processing and autonomous feedback systems.
    # 
    # He built fully automated content pipelines for Instagram and YouTube—agent-driven systems that script, edit, caption, and publish character-based content autonomously. Tooling includes Selenium, spaCy, Playwright, and FFmpeg orchestrated into a single-click, zero-touch pipeline.
    # 
    # DevOps workflows include Docker for containerization, Git for version control, and CI/CD pipelines for deployment. Systems are scaled via GCP with enforced uptime guarantees and reproducible environments.
    # 
    # Aditya views his MSc in Data Science (TU Braunschweig) as a legal shield while independently building monetizable, passive-return systems. He rejects legacy work structures, prioritizing autonomous infrastructure, long-term leverage, and absolute control over execution environments.
    # 
    # His philosophy is binary: if it doesn't scale, it's discarded; if it doesn't generate recurring value without oversight, it's re-architected. Status and motivation are irrelevant—only bandwidth, system durability, and measurable output matter.
    # """
    
    # Resume Content (structured text for agent reference)
    RESUME_TEXT = r"""
ADITYA GHANASHYAM LADAWA
+49 15510 030840 | Braunschweig, Germany | adityaladawa12@gmail.com
LinkedIn: https://www.linkedin.com/in/aditya-ladawa | GitHub: https://github.com/aditya-ladawa

EDUCATION
M.Sc. Data Science, Technische Universität Braunschweig (https://www.tu-braunschweig.de/)
Oct 2024 – Present

B.E Artificial Intelligence and Data Science, PES Modern College of Engineering (https://moderncoe.edu.in/)
Jan 2021 – Jun 2024
GPA: 8.98/10 | Thesis: Published in IJCSE (Vol. 12, Issue 8)

PROFESSIONAL WORK EXPERIENCE

AI & Processes Engineer | Brandl Nutrition (https://brandl-nutrition.de/) | Braunschweig, Germany
Aug 2025 – Present
- Eliminated stock-outs across 60+ products by deploying a Prophet-based demand forecasting system in production, achieving an 80% improvement in purchase decision quality, using Python and EOQ-driven inventory optimization; with forecasts benchmarked against Chronos-2 and Moirai models across 55 SKUs.
- Automated inventory planning from weekly manual updates to daily runs by deploying AWS pipeline (ECS, ECR, EventBridge, CloudWatch) processing 111,000 records with Looker Studio dashboards at €3/month, maintaining 99%+ uptime over 4 months
- Saved team 2+ hours daily on customer support by building multi-modal AI Email Agent in n8n, with DHL, and Shopify integrations; handling 10+ customer support scenarios; 70% of responses require minor or no edits across 12-20 daily tickets

Research Assistant | TU Braunschweig – SciBiome (Data Science in Bio-Medicine) (https://scibiome.tu-bs.de/) | Braunschweig, Germany
May 2025 – Sep 2025
- Reduced literature screening from days to 90 seconds for 2,500 papers by building async system with Google Gemini and FastAPI processing 100-paper batches via 12 parallel API calls at 95% success rate
- Developed full-stack web application (NextJS, FastAPI, IBM Docling) enabling scientists to screen papers and extract tables, figures, and metrics from PDFs; generates image-aware structured reports with methodology details and experimental results
- Building deep research agent with LangGraph, LightRAG (knowledge graphs with Neo4j, Qdrant Vector DB) using Context Engineering principles deep biomedical research synthesis

AI/ML Engineer Intern | TECHR – AI/ML Solutions (https://techr.co.in/) | Pune, India
Jun 2023 – Mar 2024
- Developed CycleGAN model in TensorFlow 2 for harmonizing 1.5T-to-3T Brain MRI scans
- Built general-purpose image enhancement pipeline combining KBNets denoising with Real-ESRGAN 4K upscaling using PyTorch and OpenCV

PROJECTS

Ideological Polarization in the 2024 U.S. Election | Jul 2025 - Sep 2025
Open Report: https://drive.google.com/drive/folders/1E-KFOLOurF_BMpMjMF8zm3hy4TDkqhZf?usp=sharing
- Exposed ideological divergence and echo chambers by engineering an LLM-powered multi-layered discourse analysis system that extracted semantic triples and stance annotations from 7,500 tweets, constructing knowledge graphs and bipartite stance networks across 36 temporal windows revealing divergent conceptual framing of identical terms
- Quantified polarization dynamics and identified discourse amplifiers by analyzing reply network structures, calculating normalized engagement metrics across 50,000 tweets, and tracking stance drift patterns; revealed broadcasting hubs and attitudinal shifts over time

AI-Driven Reels Pipeline | Jun 2025 – Aug 2025
GitHub: https://github.com/aditya-ladawa/infra_peter | Instagram: https://www.instagram.com/infra.peter/
- Grew Instagram channel to 17,000 followers and 1M views in 3 months by fully automating video production from topic to published reel; reduced creation time from 6 hours to 20 minutes at €0.20/video
- Produced 100 videos (86 posted) using LangGraph multi-agent system with Gemini, DeepSeek and Tavily AI search to research topics from 10+ sources, writes scripts, generates voiceovers, and assembles final videos; received 12+ partnership and 2 channel acquisition offers

AI – ReAs (Research Assistant) | Oct 2024 – Feb 2025
GitHub: https://github.com/aditya-ladawa/ai-reas
- Built ReWOO-style multi-agent system (https://arxiv.org/abs/2305.18323) with LangGraph, LangChain, and Qdrant enabling automated research through web search, sandboxed code execution, and cross-thread PostgreSQL memory
- Achieved 5x reduction in API costs and 30% faster insight generation while improving multi-step reasoning accuracy by 4% compared to single-agent baselines

Workout Monitoring Robot | Dec 2023 – Apr 2024
GitHub: https://github.com/aditya-ladawa/Workout_monitoring_robot
- Built autonomous exercise coaching robot using Raspberry Pi 5, Arduino, and OpenCV pose estimation running at 10 FPS with 100ms feedback latency; reduced workout form errors by 30% and increased user retention by 40%
- Published research paper demonstrating hardware-software integration for real-time CV, NLP, and ML feedback system

HACKATHON PROJECTS

SynthMotion (Hera Hackathon Berlin) | Dec 2025
GitHub: https://github.com/aditya-ladawa/Hera_hack_deep_explainer | Demo: https://aditya-ladawa.github.io/Hera_hack_deep_explainer/
Transformed complex educational content (research papers, physics problems, theoretical concepts) into professional motion graphics videos by building 6-stage autonomous pipeline with deep research agent, scripting, TTS, and video assembly using LangGraph, Gemini, Hera API, and ElevenLabs; reduced production time from 4-8 hours to 10-20 minutes

Brand Presence Detection (KI Sports Hackathon) | Nov 2025
GitHub: https://github.com/aditya-ladawa/brand_presence_prediction
Automated sponsorship ROI measurement for Bundesliga broadcasts by fine-tuning YOLOv11-Large on custom 71-class logo dataset; achieved 96% precision at 17-21 FPS real-time inference (RTX 4060), tracking brand exposure duration, frequency, and screen position across live match footage

PUBLICATIONS

Workout Monitoring Robot: A Robotic Approach for Real-Time Workout Monitoring
Shreyas Walke, Yash Wadekar, Aditya Ladawa, Pratik Khopade, Shraddha V. Pandit
International Journal of Computer Sciences and Engineering, Vol.12, Issue.8, pp.1-9, 2024
DOI: https://doi.org/10.26438/ijcse/v12i8.19

LANGUAGES
English (IELTS – Advanced), German (Goethe – Good)

SKILLS
Python, JavaScript, Bash, SQL, FastAPI, LangChain, LangGraph, LangSmith, HuggingFace, TensorFlow, PyTorch, Scikit-learn, Time Series, Transformers, Artificial Intelligence, RAG, LLMs, OpenCV, PIL, OCR, PostgreSQL, MongoDB, Redis, Qdrant, Neo4j, AWS, Docker, GitHub, Vertex AI, OpenAI, Claude, Google Gemini, CI/CD, n8n, Selenium, Playwright, BeautifulSoup
"""

    # ========================================================================
    # PERSONALITY PROFILE (For Authentic Cover Letter Writing)
    # ========================================================================
    
    PERSONALITY_PROFILE = """
WORK APPROACH & PHILOSOPHY
--------------------------
- Technical Philosophy: "Build production-ready from day one, iterate relentlessly, and learn by doing"
- Methodology: Plan rough architecture, componentize, build incrementally, test in production-like environments from start
- Thinking Process: Judge current skillset → research what's needed → sketch pipeline → build & test components → integrate → iterate
- Work Style: Intense bursts of focus (not steady, but gets work done), constant experimentation and iteration
- Version Control Habit: Commits after each successful integration and before major changes
- Adaptability: "I would adapt and do whatever needed to provide value"

MOTIVATION & LEARNING
----------------------
- Primary Drivers: Building impactful solutions, learning through doing (not extensive research upfront)
- Project Inspiration: Inspired by existing solutions or learning goals, always with production/impact in mind
- Learning Style: Apply immediately or read to know "this is possible" for future reference
- Education Approach: Pragmatic - focused on production-level skillsets alongside M.Sc. Data Science at TU Braunschweig
- AI Tools: Uses LLMs and AI coding assistants extensively, adapted from pre-GPT coding background
- Failure Philosophy: For every 5 working projects, there are 3 failed/prototype ones - learning by building means some things don't work out

PROJECT EXAMPLES & THOUGHT PROCESS
-----------------------------------
- Infra Peter (AI Reels): Needed to overlay images with script → designed schema with researcher model → LLM judges descriptions → integrated with pipeline
- AI ReAs (Oct 2024): No code sandboxes existed → restricted to workspace dir with .venv → built HITL approval system in LangGraph
- CEFLANN Trading Algo: Wanted to learn deep learning, algo trading, TensorFlow → replicated research paper as first DL project
- General Approach: Scalable from day 1, parallelism, deployability baked in from start
- Learning Pattern: Takes code/inspiration from failed prototypes to build better solutions

HACKATHONS & COLLABORATION
---------------------------
- Hackathon Participation: 10+ hackathons since moving to Germany, never skips if accepted
- Role in Teams: Usually the builder (strong skillset), enjoys networking and tech discussions
- Collaboration Style: Mostly solo projects (except Workout Monitoring Robot), works with AI tools/LLMs

PERSONAL INTERESTS
------------------
- Hobbies: Gym, anime, FL Studio (music creation)
- Coding Passion: "I enjoy coding a lot, a lot" - even builds tools to eliminate repetitions (like this cover letter automation)
- When Free: Occupies time with personal projects

CAREER DIRECTION & GOALS
-------------------------
- Target Role (1-2 years): Senior AI Engineer, Cloud AI (AWS focus), System Design
- Interested In: AI-based roles, Backend+AI, Cloud practice positions
- Current Goal: Working student job or internship at multinational company for job security post-M.Sc. (or even before completion)
- Decision Criteria: If multiple offers → company prestige and job security
- Value Proposition: "Jack of all trades, expert enough in everything to provide value from week 1"
- Technical Interests: AI agents, AI systems, Cloud AI, AI engineering, ML

COMMUNICATION STYLE
-------------------
- Approach: Compressed, concise, highly detailed
- Structure: What's done → what's ahead → problem solved → future/production impact
- Philosophy: Include all necessary details in most concise manner possible

CONTEXT & BACKGROUND
--------------------
- Why Germany/TU Braunschweig: Honest answer - family could only afford this option
- M.Sc. Reality: Finds it challenging, already has strong AI engineering skillset, focuses on production skills alongside degree completion
- Perspective: Education valuable, but deep technical details can be learned on the job when needed

WHAT'S NOT ON RESUME
--------------------
- Relentless drive to keep building despite setbacks and failed projects
- Adapted from pre-GPT era to mastering AI-assisted development
- Meta-skill: Builds tools to solve inefficiencies (automation mindset)
- Pragmatic realism: Values job security and company prestige, not chasing perfect dream job
- Multiple unfinished prototypes that fed into successful projects

CHARACTER & VALUES
------------------
- Sacrifice: "Sacrificed personal life, love life, relationships, parties, social life for coding and learning"
- Primary Drive: Learn in production environments, apply knowledge, make massive impact while improving skillset
- Proudest Achievement: AI Reels Pipeline (1M+ views, 17k followers in 3.5 months, partnership offers, opened doors to mentors/connections)
- Journey: YouTube automation (psychology topics) → Instagram automation → connections that guide him forward
- Philosophy: Paycheck is secondary priority to learning and impact

RESILIENCE & HANDLING FAILURE
------------------------------
- When Projects Fail: "Frustrated. I try my best to make it work, learn a lot along the way. What I envisioned broke in front of me due to me - how does it feel? You tell me."
- Job Rejections: Doesn't pay much attention, conveyed best effort and skillset, will improve automation or personally tailor next time
- Fuel to Keep Going: "I'm at 0.6 on a 0-to-1 journey - why turn back now? Plus, parents to take care of in future."
- No Quitting: Already invested too much (skills, sacrifice) to pivot - coding is the path forward

TEAM CONTRIBUTIONd
-----------------
- Week 1 Approach: Provide clarity on how to tackle tasks, what will be done, planned approach
- Exploration Philosophy: "More we explore, more dots are connected, more easier to work towards working prototype"
- Mentorship: Guides others - what took him 1 year to learn, he helps others accomplish in 4-6 months
- Team Culture Boundary: Won't stay if credits are hogged (recognizes when it's disadvantageous)

FRUSTRATION WITH GERMAN SYSTEM
-------------------------------
- Pain Point: Companies care about grades despite top skillset
- Their Philosophy: "He knows few things, we'll teach him what we want"
- His Counter: "Ok he knows a lot already, we'll teach him, but due to his good skillset, he has meta-intuition to explore from multiple angles and necessary depth"
- Reality: Above-average skillset compared to other M.Sc. students

COMPETITIVE ADVANTAGE
---------------------
- Unfair Advantage: Above-average skillset vs peers, drive and passion about coding
- Meta-Intuition: Deep skillset enables exploring problems from multiple angles with necessary depth
- Compression: Can accelerate others' learning (1 year → 4-6 months)
- All-In Commitment: 0.6 on 0-to-1 journey with no option to turn back

WHY HIRE ADITYA? (The "Aditya Difference")
-------------------------------------------
"I'm at 0.6 on a 0-to-1 journey with no option to turn back. I've sacrificed personal life, relationships, everything for coding. When you hire me, you get someone with meta-intuition to explore problems from multiple angles, who's built systems that gained 1M views in 3 months, who compresses learning (what took me 1 year, I teach others in 4-6 months), and who won't quit when things break - I'll iterate until it works. I don't need grades to prove I can deliver production impact from week 1."
"""

# Singleton instance for easy import
config = UserConfig()