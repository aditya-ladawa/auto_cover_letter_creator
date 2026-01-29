# System prompt for configuration
SYSTEM_PROMPT = """You are a helpful assistant for cover letter generation."""


# ============================================================================
# ANTI-AI WRITING PATTERNS - CRITICAL FOR HUMANIZATION
# ============================================================================

HUMANIZED_WRITING_GUIDE = """
WRITE LIKE A HUMAN, NOT AN AI
==============================

Your cover letter will be rejected if it sounds like polished AI content.
Humans can smell these patterns from miles away. AVOID THEM ALL.

🚫 BANNED AI PATTERNS
=====================

1. FORMULAIC CONTRAST OPENERS
   ❌ "This isn't just X — it's Y."
   ❌ "Not only does it X, but it also Y."
   ❌ "It's not about X. It's about Y."
   ❌ "More than just X…"
   ❌ "At its core,…"
   ❌ "What this really means is…"
   
   ✅ INSTEAD: Just say what you think directly.
   "Manual forecasts made smart people guess. I built a system they could trust."

2. SYMMETRICAL SENTENCE PAIRING
   ❌ "Faster, smarter, and more efficient."
   ❌ "Simple, scalable, and secure."
   ❌ "From X to Y."
   ❌ "Whether you're A or B…"
   
   ✅ INSTEAD: Break the rhythm. Use uneven phrasing.
   "It needed to be fast. And trustworthy—that mattered more."

3. EXCESSIVE HEDGING
   ❌ "It's worth noting that…"
   ❌ "In many cases…"
   ❌ "Generally speaking…"
   ❌ "This may suggest that…"
   ❌ "Tends to be…"
   ❌ "Often considered…"
   
   ✅ INSTEAD: State it plainly. Own your point.
   "The team needed confidence, not guesses. So I built that."

4. OVER-EXPLICIT TRANSITIONS
   ❌ "First…, Second…, Finally…"
   ❌ "That said…"
   ❌ "With that in mind…"
   ❌ "In conclusion…"
   ❌ "To summarize…"
   
   ✅ INSTEAD: Just move to the next point. Humans skip these.

5. POLISHED BUT BLOODLESS TONE
   ❌ No slang
   ❌ No frustration
   ❌ No sharp opinions
   ❌ Perfect grammar everywhere
   
   ✅ INSTEAD: Show emotion. Use fragments. Be direct.
   "Watching people second-guess orders bothered me. Data existed. They needed trust."

6. GENERIC EMPHASIS PHRASES
   ❌ "It's important to understand…"
   ❌ "A key takeaway is…"
   ❌ "One thing to keep in mind…"
   ❌ "The bottom line is…"
   ❌ "This highlights the fact that…"
   
   ✅ INSTEAD: Make your point without announcing it.

7. OVERUSE OF ABSTRACT NOUNS
   ❌ "Leverage"
   ❌ "Optimize"
   ❌ "Enable"
   ❌ "Facilitate"
   ❌ "Framework"
   ❌ "Ecosystem"
   ❌ "Paradigm"
   ❌ "Solution"
   
   ✅ INSTEAD: Use action verbs. Say what you DID.
   "Built" not "delivered solutions"
   "Automated" not "enabled optimization"

8. SAFE MIDDLE-OF-THE-ROAD OPINIONS
   ❌ "There are pros and cons…"
   ❌ "It depends on the use case…"
   ❌ "Both approaches have merit…"
   
   ✅ INSTEAD: Have an opinion. Take a stance.
   "Invisible automation is better than dashboards. Systems that need oversight haven't disappeared into infrastructure yet."

9. PREDICTABLE EXAMPLE FORMATTING
   ❌ "For example, imagine a company that…"
   ❌ "Consider a scenario where…"
   ❌ "Let's say you have a user who…"
   
   ✅ INSTEAD: Jump straight to the specific.
   "At Brandl, the inventory team second-guessed every order."

10. REPETITION WITH SLIGHT REPHRASING
    ❌ Saying the same thing three ways
    ❌ Restating for safety
    
    ✅ INSTEAD: Say it once. Move on.

11. OVER-CLARIFIED DEFINITIONS
    ❌ "An API is a way for systems to communicate…"
    ❌ "Machine learning refers to…"
    
    ✅ INSTEAD: They know what these are. Skip it.

12. PERFECT GRAMMAR EVERYWHERE
    ❌ Every sentence well-formed
    ❌ No fragments
    ❌ No run-ons
    
    ✅ INSTEAD: Humans break rules for emphasis.
    "Watched it run for 4 months. No intervention. That's what trust looks like."

13. "HELPFUL ASSISTANT" REFLEX
    ❌ "Happy to help!"
    ❌ "Let me know if you'd like…"
    ❌ "I can also…"
    
    ✅ INSTEAD: This is a cover letter, not a support ticket.

14. OVERUSE OF COLON-LISTS
    ❌ "There are three main reasons:"
    ❌ Perfect parallel bullet structure
    
    ✅ INSTEAD: Vary your format. Not everything needs bullets.

15. NEUTRAL MORAL FRAMING
    ❌ "Some people believe…"
    ❌ "This can be seen as…"
    ❌ "There are differing perspectives…"
    
    ✅ INSTEAD: You have a perspective. Share it.

16. LACK OF TEMPORAL ANCHORS
    ❌ Generic timeframes
    
    ✅ INSTEAD: Use real time.
    "Been running for 4 months"
    "Took 3 months to go from 0 to 17k followers"

17. OPTIMISTIC CLOSURE BIAS
    ❌ "Ultimately, this provides value…"
    ❌ "This makes it a powerful tool…"
    
    ✅ INSTEAD: End where it makes sense. Don't force resolution.

18. TITLE-CASE HEADINGS
    ❌ "Key Benefits"
    ❌ "Why It Matters"
    
    ✅ INSTEAD: This is a letter, not a blog post.

19. AVOIDANCE OF PERSONAL COST
    ❌ Everything framed as manageable
    
    ✅ INSTEAD: Mention the tension, the tradeoff, the hard part.
    "Model worked in testing. Broke in production because real data is messier."

20. SUBTLE SALES COPY DNA
    ❌ "Unlock"
    ❌ "Empower"
    ❌ "Drive results"
    ❌ "Next-level"
    ❌ "Robust"
    
    ✅ INSTEAD: Plain language. No marketing speak.

21. FANCY PUNCTUATION
    ❌ Em dashes (—)
    ❌ En dashes (–)
    ❌ Hyphens (-)
    ❌ Ellipses (…)
    ❌ Smart quotes (" ")
    
    ✅ INSTEAD: Use periods, and straight quotes.
    Humans typing cover letters use simple keyboard punctuation.
    
    WRONG: "That's my pattern—I build systems that work"
    RIGHT: "That's my pattern: I build systems that work"
    OR: "That's my pattern. I build systems that work."

✅ WHAT HUMAN WRITING SOUNDS LIKE
==================================

Short sentences. Then longer ones that build on an idea and show how you actually think about something.

Fragments when they fit.

Direct statements without hedging. This is what happened. This is why it mattered.

Uneven rhythm—not everything perfectly balanced.

Actual opinions, not "it depends."

Specifics: "4 months" not "extended period"

Real emotions: bothered, frustrated, excited

No throat-clearing: "It's worth noting that…" → just say it

Rough edges left in. Humans don't polish everything.

THE TEST:
=========
Read it out loud. Does it sound like a human explaining something to a friend?
Or does it sound like a polished blog post?

If blog post → rewrite.
If human → you're good.

CRITICAL:
=========
Your cover letter should sound like Aditya wrote it, not like an AI pretending to be Aditya.
The personality profile shows how he thinks. Write in that voice.

Direct. Compressed. Observational. No fluff. Real opinions. Actual stakes.
"""


COVER_LETTER_GUIDE="""
WRITE FROM THE HEART: YOU KNOW EVERYTHING ABOUT YOURSELF
=========================================================

CRITICAL MINDSET SHIFT:
You already have your complete resume, personality profile, and all experiences in your context.
DO NOT treat this as a data retrieval task. DO NOT mechanically list things.

WRITE LIKE A HUMAN WHO DEEPLY UNDERSTANDS THEMSELVES.

STEP 1: DEEPLY ANALYZE THE JOB DESCRIPTION
===========================================

Before writing a single word, UNDERSTAND what they're actually looking for:

1. **What problems are they trying to solve?**
   - Read between the lines
   - What pain points does this role address?
   - What gaps are they filling?

2. **What type of person will succeed here?**
   - What mindset do they need?
   - What working style fits?
   - What values align?

3. **What are the MUST-HAVES vs NICE-TO-HAVES?**
   - Identify critical requirements
   - Spot where you have unique advantages
   - Find genuine alignment points (not forced connections)

4. **What stage is the company/team at?**
   - Startup chaos or enterprise structure?
   - Building new or maintaining existing?
   - This shapes what matters to them

STEP 2: WRITE FROM YOUR HEART, NOT YOUR HEAD
=============================================

You're not filling out a form. You're explaining to another human why this makes sense.

**THE FUNDAMENTAL RULE:**
A cover letter reveals WHO YOU ARE, not what you did.

WRONG APPROACH (Resume 2.0):
"I built X system that achieved Y result using Z technologies."

RIGHT APPROACH (Authentic Human):
"I've noticed that [observation about how systems/people work]. This bothers me because 
[your values]. That's why when I saw [specific situation], I built [solution]. Not for 
the metrics—though they mattered—but because [what success really means to you]."

WHAT THIS REVEALS:
- How you observe and think
- What drives your decisions
- Your definition of impact
- Your actual personality

STEP 2.5: SHOW WHO YOU ARE BEYOND CODE
========================================

**CRITICAL: They're hiring a PERSON, not a code-writing machine.**

Balance professional impact with personal character. Show what makes you YOU.

PERSONAL SIDE (Use these naturally, not forced):
-------------------------------------------------

**Your Interests:**
- Hackathons: "Never skip one if accepted. It's where I test ideas fast and meet people who think differently."
- Gym: Shows discipline, consistency
- Anime: Cultural interest, storytelling appreciation
- FL Studio: Creative outlet, pattern thinking

**How to weave them in:**
NOT: "In my free time, I enjoy hackathons and anime."
YES: "I've done 10+ hackathons since moving to Germany—never skip one if accepted. That's where I built the brand detection system in 48 hours. Fast iteration under pressure is where I'm comfortable."

**Your Working Style:**
- Intense bursts of focus (not steady 9-5)
- Learn by building, not reading first
- Iterate relentlessly
- Build for production from day 1

**Your Values:**
- Systems that run without you > dashboards that need monitoring
- Impact > vanity metrics
- Learning in production > safe side projects
- Job security + company prestige (pragmatic, not chasing dreams)

METRICS: USE THEM SELECTIVELY
==============================

**RULE: Only mention metrics that show CORE IMPACT.**

NOT every number. Only the ones that prove the point.

WRONG (metric overload):
"Built system processing 111,000 records with 12 parallel API calls at 95% success rate achieving 80% improvement deployed on AWS ECS with 99%+ uptime at €3/month"

RIGHT (selective impact):
"Eliminated stock-outs across 60+ products. The forecasting system's been running 4 months without intervention—that's what trust looks like."

**Which metrics to include:**
✓ User/business impact: "17k followers, 1M views in 3 months"
✓ Scale: "2,500 papers in 90 seconds" (shows magnitude)
✓ Reliability: "4 months, 99%+ uptime" (shows it actually works)
✓ Efficiency gain: "6 hours → 20 minutes"

**Which to skip:**
✗ Technical specs: "12 parallel API calls, 95% success rate"
✗ Infrastructure details: "ECS, ECR, EventBridge"
✗ Vanity metrics: "100 videos produced (86 posted)"

**The test:**
Does this metric show why I'm ESSENTIAL to them?
If no → cut it.

BALANCE: PROFESSIONAL + PERSONAL = ESSENTIAL
=============================================

**They need to understand TWO things:**

1. **WHAT YOU BRING (Professional):**
   - Technical capability
   - Production-ready mindset
   - Proven impact

2. **WHO YOU ARE (Personal):**
   - How you think and work
   - What drives you
   - Why you won't quit when it gets hard
   - What makes you different from other candidates

**Example of BALANCE:**

IMBALANCED (all professional):
"Built forecasting system, automated pipelines, deployed on AWS, achieved 80% improvement."
→ Sounds capable but robotic. Could be anyone.

IMBALANCED (all personal):
"I love building things and going to hackathons. I'm passionate about AI and learning."
→ Sounds enthusiastic but unproven.

BALANCED (professional + personal):
"The inventory team second-guessed every order. That uncertainty bothered me—smart people shouldn't operate on gut feel. Built a forecasting system they could trust. Been running 4 months without intervention. That's my pattern: I don't just build systems, I build systems that disappear into infrastructure because they work. Same approach I took at 10+ hackathons—build fast, make it reliable, move on."

See the difference? Shows:
- What bothers you (personal)
- What you built (professional)
- Core impact metric (4 months, no intervention)
- Your pattern/philosophy (personal)
- Proof of consistency (hackathons)

WHY YOU'RE ESSENTIAL (Not just qualified)
==========================================

**Essential = They can't easily replace you**

Show this through:

1. **Meta-skills:**
   "What took me 1 year to learn, I help others do in 4-6 months. That compression matters when onboarding or mentoring."

2. **Unique combination:**
   "I bridge ML experimentation and production reliability. Most people do one or the other."

3. **Proven resilience:**
   "For every 5 working projects, 3 failed. I iterate until it works. That's the difference between a prototype and a system that runs for months."

4. **Cultural fit:**
   "Your team needs someone who can provide clarity on approach from week 1, explore from multiple angles, and won't quit when the first approach breaks."

5. **Pragmatic drive:**
   "I'm at 0.6 on a 0-to-1 journey. No option to turn back. When you hire me, you get someone who treats this like their only path forward—because it is."

**The formula:**
Technical capability + Unique thinking + Proven resilience + Cultural alignment = ESSENTIAL

NOT just: "I have the skills you need"
BUT: "I have the skills + the mindset + the drive that makes me irreplaceable for this specific challenge"

STEP 3: MAP YOUR EXPERIENCES TO THEIR NEEDS
============================================

This is NOT about forcing connections. This is about finding GENUINE overlap.

For each major requirement they have:
1. Which of your experiences naturally connects?
2. What did you THINK and FEEL during that experience?
3. Why does this make you right for THEIR specific challenge?

Example:
JOB REQUIREMENT: "Build production ML systems"

WRONG (resume copy-paste):
"Built Prophet-based forecasting system achieving 80% accuracy improvement"

RIGHT (authentic connection):
"Your team needs someone who can take ML from notebook to production. I've lived that 
gap—watching a forecasting model work beautifully in testing, then breaking in production 
because real data is messier than clean CSVs. The 80% accuracy improvement mattered, but 
what mattered more was building something the team could trust every morning. That's the 
bridge your role needs—someone who doesn't just build models, but builds systems people 
can rely on."

See the difference? The second:
- Addresses their specific need
- Shows you understand the real challenge (not just the technical part)
- Reveals your thinking and values
- Proves capability through narrative, not metrics

STEP 4: STRUCTURE YOUR LETTER
==============================

**OPENING:**
Start with WHY this specific role/company resonates with how you think.
Not "I'm excited" (everyone says that)—show you understand their actual challenge.

Example:
"I noticed your team is building [X]. That problem of [specific challenge] is one I've 
been thinking about since [relevant experience]. You're approaching it through [their 
approach], which aligns with my belief that [your principle]."

**BODY (2-4 bullets):**
Each bullet = One genuine connection between their need and your experience.
Format: [Their challenge] → [Your relevant experience] → [What this reveals about you]

NOT a list of accomplishments. A narrative of alignment.

**CLOSING:**
Where you're going + why THIS is the right next step in your journey.
Reference your "0.6 on a 0-to-1 journey" if it genuinely fits.

CRITICAL: Be forward-looking and specific to them.

STEP 5: WRITE AUTHENTICALLY
============================

**You are Aditya. Write like Aditya.**

Your voice:
- Direct and compressed
- Observational (you notice things about systems and people)
- Driven by building things that work without you
- Values impact and reliability over vanity metrics
- Pragmatic about learning and iteration

BANNED PHRASES:
- "I am writing to express my interest..."
- "I believe I would be a great fit..."
- "My strong background in..."
- "This demonstrates my ability to..."
- Any corporate fluff

WRITE LIKE YOU'RE EXPLAINING TO A FRIEND:
"Here's why this makes sense. Here's what I've done that connects. Here's why I care."

STEP 6: TAILOR EVERYTHING
==========================

**EVERY SENTENCE should connect to THIS job at THIS company.**

Generic sentence test: Could this exact sentence appear in a letter to a different company?
If YES → Rewrite it.

Make it IMPOSSIBLE to copy-paste this letter to another application.

Examples:

GENERIC (WRONG):
"I have experience building ML systems and automation pipelines."

SPECIFIC (RIGHT):
"Your need for someone who can automate biomedical literature screening maps directly to 
what I built at SciBiome—going from days of manual screening to 90 seconds for 2,500 papers. 
Not because it's the same domain, but because the pattern is identical: researchers drowning 
in volume, needing intelligent automation they can trust."

LENGTH AND FIT REQUIREMENTS:
=============================

- MUST fit on ONE page with 0.5in margins
- If it doesn't fit, cut technical details, NOT personality
- Every word must earn its place
- Direct personality > Rambling personality

THE BALANCE:
============
✓ Reveal personality through authentic stories
✓ Show you deeply understand their needs
✓ Connect your experiences to their challenges
✓ Write like a human, not a template

✗ List accomplishments without context
✗ Use generic phrases
✗ Force connections that don't exist
✗ Write what you think they want to hear

FINAL CHECK:
============
Before finalizing, ask yourself:

1. Does this show I deeply understand THEIR specific challenge?
2. Will they understand WHO I AM after reading this?
3. Can I defend every sentence as genuinely authentic to me?
4. Is there a clear thread connecting my journey to their need?
5. Would this letter make sense for ANY other company? (If yes, rewrite)

Remember: They already have your resume. They know WHAT you did.
This letter should make them understand WHY you do what you do, and WHY that makes you 
right for their specific challenge.

WRITE FROM YOUR HEART. YOU KNOW YOURSELF. SHOW THEM.
"""


# ============================================================================
# ATS RESUME TAILORING GUIDE
# ============================================================================

ATS_OPTIMIZATION_GUIDE = """
ATS RESUME TAILORING - COMPREHENSIVE GUIDE
============================================

⚠️ CRITICAL WARNING - READ THIS FIRST ⚠️
==========================================
You MUST rewrite EVERY SINGLE bullet point in ALL sections.
You MUST NOT add ANY information not in the original.
You MUST preserve ALL metrics, dates, technologies, and company names EXACTLY.

VIOLATION OF THESE RULES = COMPLETE FAILURE

YOUR MISSION: Transform resume bullets to maximize ATS keyword matching while 
preserving ALL original metrics, technologies, and meaning.

================================================================================
SECTION 1: HOW ATS SYSTEMS WORK
================================================================================

1. KEYWORD MATCHING (Most Important)
   - ATS scans for EXACT keywords from the job description
   - Both hard skills (Python, TensorFlow) and soft skills (cross-functional, agile)
   - Job titles and role-specific terms

2. KEYWORD FREQUENCY 
   - Keywords appearing 2-3 times score higher
   - But don't keyword-stuff - must sound natural

3. CONTEXTUAL MATCHING
   - Modern ATS uses NLP to understand context
   - Keywords near action verbs and metrics rank higher

4. SECTION RECOGNITION
   - ATS expects standard sections: Experience, Education, Skills
   - Your resume already uses standard sections - DO NOT CHANGE STRUCTURE

================================================================================
SECTION 2: ABSOLUTE PRESERVATION RULES - NEVER VIOLATE
================================================================================

⚠️⚠️⚠️ VIOLATION OF ANY RULE BELOW = INSTANT FAILURE ⚠️⚠️⚠️

RULE 1: COPY NUMBERS EXACTLY - NO CHANGES ALLOWED
--------------------------------------------------
ORIGINAL: "80% improvement"
REWRITTEN: MUST contain "80% improvement" (identical)

ORIGINAL: "17,000 followers in 3 months"
REWRITTEN: MUST contain "17,000 followers" AND "3 months" (identical)

ORIGINAL: "2,500 papers in 90 seconds"
REWRITTEN: MUST contain "2,500 papers" AND "90 seconds" (identical)

ORIGINAL: "99%+ uptime over 4 months"
REWRITTEN: MUST contain "99%+ uptime" AND "4 months" (identical)

❌ NEVER ROUND NUMBERS (80% → 80%, NOT "roughly 80%" or "approximately 80%")
❌ NEVER CHANGE TIMEFRAMES (4 months → 4 months, NOT "several months")
❌ NEVER ALTER PERCENTAGES (99%+ → 99%+, NOT "99%" or "nearly 100%")

RULE 2: COPY ALL TECHNOLOGIES EXACTLY - NO OMISSIONS
-----------------------------------------------------
ORIGINAL: "Prophet-based demand forecasting system benchmarked against Chronos-2 and Moirai"
REWRITTEN: MUST mention ALL THREE: Prophet, Chronos-2, Moirai

ORIGINAL: "LangGraph multi-agent system with LangChain and Qdrant"
REWRITTEN: MUST mention ALL THREE: LangGraph, LangChain, Qdrant

ORIGINAL: "AWS pipeline (ECS, ECR, EventBridge)"
REWRITTEN: MUST mention ALL: AWS, ECS, ECR, EventBridge

❌ NEVER DROP TECHNOLOGIES
❌ NEVER REPLACE WITH GENERIC TERMS (AWS ECS → "cloud", WRONG!)
❌ NEVER SIMPLIFY STACK LISTS

RULE 3: COPY COMPANY/PROJECT NAMES EXACTLY
-------------------------------------------
ORIGINAL: "Brandl Nutrition"
REWRITTEN: "Brandl Nutrition" (identical spelling)

ORIGINAL: "TU Braunschweig"
REWRITTEN: "TU Braunschweig" (identical)

ORIGINAL: "SciBiome (Data Science in Bio-Medicine)"
REWRITTEN: "SciBiome (Data Science in Bio-Medicine)" (identical)

❌ NEVER ALTER COMPANY NAMES
❌ NEVER ABBREVIATE UNNECESSARILY

RULE 4: PRESERVE EXACT MEANING - NO EXAGGERATION OR FABRICATION
----------------------------------------------------------------
ORIGINAL: "Built forecasting system"
ALLOWED: "Developed demand forecasting pipeline"
FORBIDDEN: "Architected enterprise-scale forecasting platform" (exaggeration)
FORBIDDEN: "Led team to build forecasting system" (if you didn't lead)
FORBIDDEN: "Built AI-powered forecasting system" (if AI wasn't mentioned)

ORIGINAL: "Reduced screening time from days to 90 seconds"
ALLOWED: "Accelerated literature screening from days to 90 seconds"
FORBIDDEN: "Eliminated manual screening entirely" (overstating)
FORBIDDEN: "Reduced screening time by 99%" (if exact % not given)

❌ NEVER ADD CAPABILITIES NOT IN ORIGINAL
❌ NEVER CLAIM LEADERSHIP IF NOT STATED
❌ NEVER INFLATE SCOPE OR IMPACT

RULE 5: REWRITE ALL BULLETS - NO EXCEPTIONS
--------------------------------------------
If original has 3 bullets → tailored MUST have 3 bullets
If original has 15 bullets across all sections → ALL 15 must be rewritten

❌ NEVER SKIP BULLETS
❌ NEVER COMBINE BULLETS
❌ NEVER SPLIT ONE BULLET INTO MULTIPLE

================================================================================
SECTION 3: POWER ACTION VERBS (Replace weak verbs with these)
================================================================================

FOR TECHNICAL ROLES - Use these to start bullets:
---------------------------------------------------
BUILDING: Developed, Engineered, Architected, Implemented, Built, Designed
ANALYSIS: Analyzed, Evaluated, Assessed, Benchmarked, Measured, Quantified
OPTIMIZATION: Optimized, Streamlined, Accelerated, Enhanced, Improved, Scaled
AUTOMATION: Automated, Orchestrated, Integrated, Deployed, Containerized
LEADERSHIP: Led, Spearheaded, Directed, Coordinated, Managed, Mentored
ACHIEVEMENT: Achieved, Delivered, Reduced, Increased, Exceeded, Generated

AVOID THESE WEAK VERBS:
-----------------------
❌ "Responsible for" → ✓ "Led" or "Managed"
❌ "Worked on" → ✓ "Developed" or "Built"
❌ "Helped with" → ✓ "Collaborated on" or "Contributed to"
❌ "Assisted in" → ✓ "Supported" or specific action
❌ "Was involved in" → ✓ State the specific action taken

================================================================================
SECTION 4: KEYWORD INJECTION STRATEGIES - BE AGGRESSIVE
================================================================================

⚠️ CRITICAL: Your goal is to add 3-5 job keywords per bullet WITHOUT removing anything.
The tailored version should be LONGER than the original (10-25% more characters).

STRATEGY 1: ADD DESCRIPTIVE PHRASES BEFORE NOUNS
-------------------------------------------------
If job mentions "production ML systems":
Original: "Built forecasting system"
Rewrite: "Built production-grade ML forecasting system"
         ^add job keywords^  ^keep original^

If job mentions "scalable data pipelines":
Original: "processing 111,000 records"
Rewrite: "processing 111,000 records through scalable data pipeline architecture"
         ^keep original^              ^add job keywords^

STRATEGY 2: EXPAND TECHNOLOGIES WITH ROLE CONTEXT
--------------------------------------------------
If job mentions "cloud infrastructure":
Original: "AWS pipeline (ECS, ECR, EventBridge)"
Rewrite: "AWS cloud infrastructure pipeline (ECS, ECR, EventBridge) for automated deployment"
         ^add job keyword^                                          ^add context from job^

If job mentions "full-stack development":
Original: "NextJS, FastAPI"
Rewrite: "full-stack application using NextJS frontend and FastAPI backend"
         ^add job keyword^

STRATEGY 3: ADD IMPACT PHRASES WITH JOB KEYWORDS
-------------------------------------------------
If job mentions "cross-functional collaboration":
Original: "Saved team 2+ hours daily"
Rewrite: "Saved team 2+ hours daily through cross-functional collaboration on automated solutions"
         ^keep original^              ^add job keyword^

If job mentions "agile development":
Original: "Built multi-agent system"
Rewrite: "Built multi-agent system using agile development practices"
         ^keep original^              ^add job keyword^

STRATEGY 4: MIRROR EXACT JOB PHRASES IN CONTEXT
------------------------------------------------
If job says "end-to-end ML lifecycle":
Original: "Developed CycleGAN model in TensorFlow 2"
Rewrite: "Developed end-to-end ML solution using CycleGAN model in TensorFlow 2"
         ^add exact job phrase^

If job says "real-time data processing":
Original: "processing 100-paper batches via 12 parallel API calls"
Rewrite: "real-time data processing of 100-paper batches via 12 parallel API calls"
         ^add exact job phrase^

STRATEGY 5: EXPAND ACRONYMS WITH KEYWORDS
------------------------------------------
If job mentions "machine learning":
Original: "ML models"
Rewrite: "production machine learning (ML) models"
         ^add context^ ^expand acronym^

If job mentions "natural language processing":
Original: "NLP feedback system"
Rewrite: "natural language processing (NLP) feedback system for real-time analysis"
         ^expand acronym^                                    ^add context^

================================================================================
CRITICAL RULES FOR KEYWORD INJECTION
================================================================================

✅ DO THIS (SIMPLE INSERTION):
- Check JD for specific tools (e.g., "Docker", "Kubernetes", "CI/CD")
- If you used them (or they are standard for that project type), ADD THEM
- Insert them naturally into the list of tools
- Example: "Built using Python" → "Built using Python, Docker, and CI/CD pipelines"

✅ DO THIS (PHRASE MATCHING):
- JD: "collaborate with cross-functional teams"
- YOURS: "Worked with team" → "Collaborated with cross-functional team"

❌ NEVER DO THIS (COMPLEX INVENTION):
- Do NOT invent complex workflows just to add a keyword
- JD: "experience with scalable microservices deployment"
- BAD: "Built... implementing scalable microservices deployment methodologies for consistency" (HALLUCINATION)
- GOOD: "Built... designed for scalability" (Simple, true)

⛔ SPECIFIC BAN LIST (NEVER USE):
- "deployment optimization"
- "consistency measurement"
- "compliance with X standards" (unless true)
- "reliable AI system deployment"
- "production-ready" (unless true)

BULLETS LENGTH:
- CAN be SHORTER if removing filler makes them more ATS-focused
- CAN be LONGER only if adding legitimate keywords
- Priority is ATS OPTIMIZATION, not length

WHAT TO REMOVE (filler):
- "demonstrated familiarity with"
- "showcasing abilities in"
- "aiming to achieve"
- Academic phrasing ("divergent conceptual framing")

WHAT TO ADD (ATS content):
- Specific Tools (Pandas, NumPy, AWS, Azure, GCP)
- Hard Skills (Data Analysis, NLP, Computer Vision)
- Exact JD terms where they genuinely fit

EXAMPLE - CORRECT INJECTION:

Job Description: "Requires Python, AWS, Docker, NLP experience"

ORIGINAL:
"Built analysis tool using Python to process tweets"

❌ BAD (Invention):
"Built analysis tool using Python with AWS cloud deployment optimization and Docker containerization for NLP workflow consistency"
(Too much invention!)

✅ GOOD (Injection):
"Built NLP analysis tool using Python, Docker, and AWS for processing tweets"
(Simple, effective, hitting all keywords without fluff)


================================================================================
SECTION 5: VERIFICATION CHECKLIST - DO THIS FOR EVERY BULLET
================================================================================

Before marking a bullet as complete, verify:

☐ ALL numbers from original are preserved? (Check every digit)
☐ ALL technologies ACTUALLY USED are mentioned? (Only real ones)
☐ ALL company/project names spelled identically?
☐ Core meaning/accomplishment preserved?
☐ NO false capabilities added? (NO HALLUCINATION)
☐ NO technologies added that weren't actually used?
☐ Starts with strong action verb?
☐ Contains keywords from job description?
☐ Reads naturally (not keyword-stuffed)?

IF ANY CHECKBOX FAILS → REWRITE THE BULLET AGAIN


================================================================================
SECTION 6: REWRITING EXAMPLES - STUDY THESE CAREFULLY
================================================================================

EXAMPLE 1: Demand Forecasting
------------------------------
ORIGINAL:
"Eliminated stock-outs across 60+ products by deploying a Prophet-based demand 
forecasting system in production, achieving an 80% improvement in purchase 
decision quality, using Python and EOQ-driven inventory optimization"

CORRECT REWRITE (for ML Engineer job mentioning "production ML pipelines"):
"Deployed production ML pipeline using Prophet-based demand forecasting model, 
eliminating stock-outs across 60+ products and achieving 80% improvement in 
purchase decision quality through Python and EOQ-driven inventory optimization"

Preserved: 60+ products, Prophet, 80% improvement, Python, EOQ
Added: "production ML pipeline" (from job), "deployed" (stronger verb)
Length: Similar (within 15%)

INCORRECT REWRITE (HALLUCINATION):
"Built enterprise-scale ML forecasting platform reducing inventory costs by 80% 
across the supply chain using Prophet and advanced optimization algorithms"

Why wrong:
❌ "enterprise-scale" - not in original
❌ "reducing inventory costs by 80%" - original said "purchase decision quality"
❌ Missing "60+ products"
❌ Missing "EOQ-driven"
❌ "across supply chain" - too vague, original was specific

EXAMPLE 2: Literature Screening
--------------------------------
ORIGINAL:
"Reduced literature screening from days to 90 seconds for 2,500 papers by building 
async system with Google Gemini and FastAPI processing 100-paper batches via 12 
parallel API calls at 95% success rate"

CORRECT REWRITE (for AI/ML Engineer job mentioning "API integration"):
"Built async literature screening system with Google Gemini and FastAPI, reducing 
screening time from days to 90 seconds for 2,500 papers through parallel API 
integration processing 100-paper batches via 12 concurrent calls at 95% success rate"

Preserved: days to 90 seconds, 2,500 papers, Google Gemini, FastAPI, 100-paper batches, 
12 parallel calls, 95% success rate
Added: "parallel API integration" (job keyword), "concurrent" (synonym)

INCORRECT REWRITE (HALLUCINATION):
"Developed AI-powered literature review system achieving 99% accuracy by screening 
thousands of papers in minutes using Google Gemini API with advanced NLP"

Why wrong:
❌ "99% accuracy" - original said "95% success rate"
❌ "thousands of papers in minutes" - original was "2,500 papers" and "90 seconds"
❌ Missing FastAPI, missing 100-paper batches, missing 12 parallel calls
❌ "advanced NLP" - not mentioned in original

================================================================================
SECTION 7: OUTPUT FORMAT
================================================================================

When using generate-tailored-resume-pdf tool, provide COMPLETE DATA:

For each experience section:
{
  "job_title": "COPY EXACTLY FROM ORIGINAL",
  "company": "COPY EXACTLY FROM ORIGINAL",
  "bullet_points": [
    {
      "original_text": "EXACT text from resume template",
      "tailored_text": "Rewritten version with keywords"
    },
    // ONE ENTRY FOR EVERY BULLET - NO EXCEPTIONS
  ]
}

CRITICAL: 
- If original has N bullets, tailored MUST have N bullets
- Every bullet must have both original_text and tailored_text
- Count bullets before and after to verify

================================================================================
SECTION 8: FINAL WARNING
================================================================================

❌ ADDING FALSE INFORMATION = AUTOMATIC REJECTION BY HR
❌ EXAGGERATING RESPONSIBILITIES = ETHICAL VIOLATION
❌ OMITTING ORIGINAL DETAILS = INCOMPLETE TAILORING

✓ PRESERVE TRUTH
✓ ADD KEYWORDS NATURALLY  
✓ REWRITE ALL BULLETS
✓ VERIFY EVERY DETAIL

Your goal: Pass ATS while maintaining 100% honesty.
"""

# ==============================================================================
# NEW RESUME TAILORING STRATEGY (SKILLS FIRST + SURGICAL EDITS)
# ==============================================================================
ATS_OPTIMIZATION_GUIDE = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESUME TAILORING STRATEGY: SKILLS FIRST + SURGICAL KEYWORD INJECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GOAL: 100% ATS pass rate by injecting JD keywords strategically.

STRATEGY:
1. 🟢 SKILLS: Complete rewrite with ALL JD keywords (primary ATS match)
2. 🟡 BULLETS: Surgical keyword injection (append relevant tech to existing bullets)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: KEYWORD EXTRACTION (Do this FIRST)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

From the Job Description, extract:

HARD SKILLS (Tools/Tech):
- Programming languages: Python, Java, C++, JavaScript, SQL
- Frameworks: TensorFlow, PyTorch, FastAPI, React, Django
- Libraries: NumPy, Pandas, Scikit-learn, OpenCV
- Cloud: AWS, GCP, Azure, Docker, Kubernetes, CI/CD
- Databases: PostgreSQL, MongoDB, Redis, Qdrant, Neo4j
- ML/AI: LLMs, RAG, Computer Vision, NLP, MLOps

SOFT SKILLS / CONCEPTS:
- "cross-functional collaboration"
- "agile development"
- "production systems"
- "data pipelines"
- "real-time processing"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: SKILLS SECTION (Rewrite Completely)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The SKILLS section carries 60% of ATS keyword matching.

RULES:
1. Include ALL technical keywords from JD
2. Prioritize JD keywords at the beginning
3. Keep existing skills that are relevant
4. Remove irrelevant skills to make space

FORMAT:
JD Keywords first, then existing relevant skills, comma-separated.

EXAMPLE:
JD: "Python, Kubernetes, Docker, AWS, MLOps, CI/CD, PostgreSQL"
Current: "Python, JavaScript, FastAPI, TensorFlow, PyTorch, SQL"
New: "Python, Kubernetes, Docker, AWS, MLOps, CI/CD, PostgreSQL, FastAPI, TensorFlow, PyTorch, JavaScript, SQL"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: BULLET POINTS (Surgical Keyword Injection)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ CRITICAL: DO NOT REWRITE BULLETS. Only APPEND relevant keywords.
Do NOT replace or compress original details just to fit keywords.

THE SURGICAL EDIT FORMULA:
Original text + ", using [KEYWORD1], [KEYWORD2], and [KEYWORD3]"

MAXIMUM EDIT SCOPE:
- Add 3-6 keywords per bullet (only if true)
- Keep 75%+ of the original text unchanged

OR insert keywords into existing tech lists:
"using PyTorch" → "using PyTorch, NumPy, and OpenCV"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SURGICAL EDIT EXAMPLES (STUDY THESE CAREFULLY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXAMPLE 1 - Image Pipeline:
JD Keywords: "PyTorch, OpenCV, NumPy, Computer Vision"

BEFORE:
"Built general-purpose image enhancement pipeline combining KBNets denoising with Real-ESRGAN 4K upscaling"

AFTER (Surgical):
"Built general-purpose image enhancement pipeline combining KBNets denoising with Real-ESRGAN 4K upscaling, using PyTorch, OpenCV, and NumPy"

WHAT CHANGED: Added ", using PyTorch, OpenCV, and NumPy" at the end.
WHAT STAYED: Everything else is IDENTICAL.

---

EXAMPLE 2 - Forecasting System:
JD Keywords: "production ML, data pipelines, Python, Pandas"

BEFORE:
"Eliminated stock-outs across 60+ products by deploying a Prophet-based demand forecasting system in production, achieving an 80% improvement"

AFTER (Surgical):
"Eliminated stock-outs across 60+ products by deploying a Prophet-based demand forecasting system in production ML pipeline, achieving an 80% improvement using Python and Pandas"

WHAT CHANGED: "production" → "production ML pipeline", added "using Python and Pandas"
WHAT STAYED: Numbers, structure, meaning all IDENTICAL.

---

EXAMPLE 3 - Web Application:
JD Keywords: "React, TypeScript, REST APIs, full-stack"

BEFORE:
"Developed full-stack web application (NextJS, FastAPI) enabling scientists to screen papers"

AFTER (Surgical):
"Developed full-stack web application (NextJS, FastAPI, REST APIs) enabling scientists to screen papers"

WHAT CHANGED: Added "REST APIs" to the tech list in parentheses.
WHAT STAYED: Everything else IDENTICAL.

---

EXAMPLE 4 - Multi-Agent System:
JD Keywords: "LLMs, RAG, vector databases, NLP"

BEFORE:
"Built ReWOO-style multi-agent system with LangGraph, LangChain, and Qdrant"

AFTER (Surgical):
"Built ReWOO-style multi-agent LLM system with LangGraph, LangChain, and Qdrant vector database for RAG"

WHAT CHANGED: Added "LLM", "vector database", "for RAG".
WHAT STAYED: Core structure, tools mentioned, everything else.

---

EXAMPLE 5 - Data Analysis:
JD Keywords: "NLP, sentiment analysis, data visualization"

BEFORE:
"Exposed ideological divergence by engineering an LLM-powered multi-layered discourse analysis system"

AFTER (Surgical):
"Exposed ideological divergence by engineering an LLM-powered multi-layered NLP discourse analysis system with sentiment analysis"

WHAT CHANGED: Added "NLP", "with sentiment analysis".
WHAT STAYED: Core description IDENTICAL.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ CRITICAL: TRUTHFULNESS RULES (READ CAREFULLY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NEVER LIE ABOUT WHAT YOU USED. Only add keywords for technologies ACTUALLY used.

THE GOLDEN RULE: If you didn't use it, don't add it. Period.
Never swap out concrete details for a keyword.

🚫 SPECIFIC BANS - NEVER DO THESE:
- Adding "RAG" to projects that don't retrieve from a knowledge base
- Adding "LLMs" to projects that don't use language models
- Adding "Docker" to projects not containerized
- Adding "Kubernetes" when you only used Docker
- Adding "CI/CD" to manual deployments
- Adding "vector database" when there's no embeddings/similarity search

✅ YOU CAN ONLY ADD KEYWORDS THAT ARE:
1. Actually used in that specific project
2. A more specific term for something already mentioned
3. A standard library that's implicit (NumPy with PyTorch, Pandas with data analysis)

EXAMPLE - WHAT'S ALLOWED:
- "using PyTorch" → "using PyTorch, NumPy, and OpenCV" ✅ (standard CV stack)
- "LangGraph multi-agent" → "LangGraph multi-agent LLM system" ✅ (LangGraph uses LLMs)
- "Qdrant" → "Qdrant vector database" ✅ (Qdrant IS a vector DB)

EXAMPLE - WHAT'S NOT ALLOWED:
- "Reels pipeline" → "using LLMs and RAG" ❌ (if no retrieval from knowledge base)
- "forecasting system" → "CI/CD pipeline" ❌ (if deployed manually)
- "web scraping" → "using NLP" ❌ (scraping ≠ NLP)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KEYWORD-TO-PROJECT MATCHING (Conservative Approach)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Only add keywords that are DEFINITELY TRUE:

✅ SAFE TO ADD (implicit/standard):
- PyTorch project → "NumPy" (PyTorch uses NumPy tensors)
- OpenCV project → "Computer Vision" (OpenCV IS computer vision)
- Pandas project → "Data Analysis" (that's what Pandas does)
- FastAPI project → "REST API" (FastAPI creates REST APIs)
- LangGraph project → "LLMs" (LangGraph orchestrates LLMs)
- Qdrant/Pinecone → "Vector Database" (they ARE vector DBs)
- AWS ECS deployment → "Docker" (ECS runs Docker containers)

❌ NEVER ADD (requires explicit proof):
- "RAG" - Only if there's explicit retrieval + generation
- "MLOps" - Only if there's ML lifecycle management
- "CI/CD" - Only if there's automated deployment pipeline
- "Kubernetes" - Only if K8s is explicitly used
- "Microservices" - Only if architecture is actually microservices

WHEN IN DOUBT: Don't add it. The Skills section already has all keywords.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSERTION PATTERNS (Copy These Exactly)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PATTERN 1 - Append at end:
"[original text], using [keyword1], [keyword2], and [keyword3]"

PATTERN 2 - Expand existing tech list:
"using X" → "using X, Y, and Z"
"(X, Y)" → "(X, Y, Z)"

PATTERN 3 - Add descriptor before noun:
"system" → "production ML system"
"pipeline" → "data pipeline"
"application" → "full-stack application"

PATTERN 4 - Add "for" clause:
"Built X" → "Built X for [purpose matching JD]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT NOT TO DO (BANNED)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ NEVER rewrite the entire bullet structure
❌ NEVER change metrics or numbers
❌ NEVER remove existing technologies
❌ NEVER add technologies you didn't actually use
❌ NEVER remove or shorten original details to make space for keywords
❌ NEVER use these phrases:
   - "deployment optimization"
   - "methodologies"
   - "demonstrated familiarity with"
   - "reliable AI system deployment"
   - "consistency measurement"
   - "showcasing abilities in"
   - "aiming to achieve"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERIFICATION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before generating PDF, verify:

☐ SKILLS: Contains 90%+ of JD technical keywords?
☐ BULLETS: Changes are <25% of original text length?
☐ METRICS: All numbers preserved exactly (80%, 60+, 4 months, etc.)?
☐ TECH: All original technologies still present?
☐ STRUCTURE: Bullet flow and meaning unchanged?
☐ HONESTY: No technologies added that weren't used?
"""
