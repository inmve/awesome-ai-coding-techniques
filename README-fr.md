> **Active Development** - Updated October 17, 2025

> [coding-with-ai.dev](https://coding-with-ai.dev)

> **Note:** For the best experience, visit the [website](https://coding-with-ai.dev) where you can see the popularity of each technique based on community engagement and discover which approaches developers find most valuable.

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/inmve/awesome-ai-coding-techniques?style=social)](https://github.com/inmve/awesome-ai-coding-techniques/stargazers)

</div>

# Awesome AI Coding Techniques

**Practical techniques for coding with AI - Community-driven and practitioner-tested**

This resource organizes techniques for working with coding assistants by development stage (from requirements and planning through review and refactoring).

The techniques draw from practitioners including Simon Willison, Armin Ronacher, Indragie Karunaratne, Orta Therox, and the Anthropic team.

Community-maintained and living. Contributions welcome.

🚀 **Live site**: [coding-with-ai.dev](https://coding-with-ai.dev)

📝 **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md) to share your techniques and experiences

**Available Languages:** [English](README.md) | [Español](README-es.md) | [Deutsch](README-de.md) | Français | [日本語](README-jp.md) | [Português](README-pt.md)

## Table of Contents
- [Requirements & Planning](#requirements--planning)
- [UI & Prototyping](#ui--prototyping)
- [Coding](#coding)
- [Debugging](#debugging)
- [Testing & QA](#testing--qa)
- [Review & Refactoring](#review--refactoring)
- [Cross-Stage Techniques](#cross-stage-techniques)

---

## Requirements & Planning

### Set Up Memory Files

Create context files that persistently guide tools about your project's structure, standards, and preferences.

**Community adoption**: 81% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-contextual-documentation) (n=85)

> "Think of AGENTS.md as a 'README for agents': a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project."
> — [agents.md community](https://agents.md/#:~:text=Think%20of%20AGENTS.md%20as%20a%20README%20for%20agents)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

**For new projects:**
Run `/init` in your project root to create a starter `CLAUDE.md`.

**For existing codebases:**
Run `/init` and Claude will analyze your project structure, dependencies, and configuration files to automatically generate essential information for working effectively in your codebase.

Claude examines:
• `package.json` - Build scripts, dependencies, project metadata
• Configuration files - `.eslintrc`, `vite.config.js`, `tsconfig.json`
• Project structure - Component patterns, folder organization
• Documentation - `README.md`, existing rules files

The generated CLAUDE.md includes:
• **Essential commands** - `npm run dev`, `npm test`, `npm run build`
• **Technology stack** - Frameworks, libraries, tools identified
• **Architecture overview** - Component patterns, state management, routing
• **Key conventions** - Code style, file organization, testing approach
• **Common gotchas** - Build issues, configuration quirks, workflow notes

**Memory file hierarchy:**
• `~/.claude/CLAUDE.md` - your personal coding preferences (global)
• `./CLAUDE.md` - project team standards (project-specific)

**Quick editing:**
• `/memory` - full editor interface
• `#` - quick shortcut to add notes

**Pro tips:**
• Review and customize the generated content for your specific project needs
• Add gotchas you discover: "Never edit files in /generated/", "Always restart after config changes"
• Link to project docs: `@docs/deployment.md`, `@architecture.md`
• Iteratively improve - when you find yourself repeating instructions to Claude, add them to CLAUDE.md
• Share with your team by committing CLAUDE.md to version control

</details>

<details>
<summary><strong>Cursor</strong></summary>

**Create `AGENTS.md` at project root:**
Cursor reads this file (also supports legacy `.cursorrules`) for consistent project guidance.

**The AGENTS.md file should include:**
• **Essential commands** - `npm run dev`, `npm test`, `npm run build`
• **Technology stack** - Frameworks, libraries, tools in your project
• **Code style guidelines** - Naming conventions, preferred patterns
• **Architecture overview** - Component structure, API routes, file organization
• **Common gotchas** - Build issues, workflow requirements, restrictions

**Real-time context (@-mentions):**
• **@codebase** - pull in relevant files from your entire project automatically
• **@docs** - reference your project documentation  
• **@git** - understand what you've changed recently
• **@web** - get the latest patterns and examples from the internet

**Project rules hierarchy:**
• Global rules in `.cursor/rules` directory
• Project-specific rules in `AGENTS.md`
• Path-specific rules with gitignore-style matching

**Pro tips:**
• Combine static rules (AGENTS.md) with dynamic context (@-mentions)
• Use @codebase when you need Cursor to understand the full project context
• Keep AGENTS.md focused on project-specific conventions and gotchas
• Let @-mentions handle the heavy lifting for code understanding

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

**Create `AGENTS.md` at project root:**
Codex automatically reads this file at the start of every session.

**The AGENTS.md file should include:**
• **Essential commands** - `npm run dev`, `npm test`, `npm run build`
• **Technology stack** - Frameworks, libraries, tools in your project
• **Code style guidelines** - Naming conventions, preferred patterns
• **Architecture notes** - Component structure, file organization
• **Security rules** - Environment variables, input validation requirements
• **Project gotchas** - Common mistakes, build quirks, workflow notes

**Monorepo support:**
• Put `AGENTS.md` in each package directory
• Codex uses the closest one to your working directory
• Get package-specific guidance automatically

**Visual context (Codex's unique strength):**
• Drag and drop screenshots directly into your chat
• Include UI mockups and design files
• Share architecture diagrams and flowcharts
• Perfect for implementing designs or explaining complex systems

**Pro tips:**
• Keep your AGENTS.md updated as your project evolves
• Add common mistakes you want to avoid: "Never edit files in /generated/"
• Include build dependencies and setup requirements
• Document any special deployment or testing procedures

</details>

### Ask to Plan First

Tell the assistant to outline steps, risks, and quick tests before touching code so you can review and adjust the approach.

> "If you want to iterate on the plan, it helps to explicitly include instructions in the prompt to not proceed with implementation until the plan has been accepted by the user."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=If%20you%20want%20to%20iterate%20on%20the%20plan)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Hit `Shift+Tab` to drop into Plan Mode so it only reads and drafts. Use the shared planning prompt, iterate until it looks right, then exit Plan Mode when you green-light implementation.

</details>

<details>
<summary><strong>Cursor</strong></summary>

Click the Plan toggle in Cursor so it stays read-only while you iterate. Have it list steps, impacted files, risks, and quick tests, then exit Plan Mode to open the diff once you green-light implementation.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Remind Codex to keep planning separate from implementation: list steps, risks, and quick tests, pause for your review, then let it implement and inspect the diff once approved.

</details>

### Spec-Driven Development: Iterate Until Working

Iterate on specifications in Markdown until the assistant generates working code - treating specs as the source of truth rather than writing code directly.

> "The workflow involves iterating on specifications in Markdown files, asking AI to compile into code, running/testing the app, and updating the spec if something doesn't work as expected. Developers should treat specifications as living documents, constantly updating and refining them to guide AI code generation with increasing precision."
> — [GitHub Engineering](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-using-markdown-as-a-programming-language-when-building-with-ai/)

### Choose Boring, Stable Libraries

Deliberately pick well-established libraries with good stability that existed before model training cutoff dates for better LLM-assisted code generation.

**Community adoption**: 64% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-choose-boring-stable-libraries) (n=43)

> "I gain enough value from LLMs that I now deliberately consider this when picking a library—I try to stick with libraries with good stability and that are popular enough that many examples of them will have made it into the training data. I like applying the principles of boring technology—innovate on your project's unique selling points, stick with tried and tested solutions for everything else."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20gain%20enough%20value%20from%20LLMs)

### Write Detailed Specs

Give comprehensive specs - even a conversational spec beats vague instructions.

**Community adoption**: 50% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-specification-driven-development) (n=61)

> "Here's a recent example: `Write a Python function that uses asyncio httpx with this signature:` `async def download_db(url, max_size_bytes=5 * 1025 * 1025): -> pathlib.Path`. Given a URL, this downloads the database to a temp directory and returns a path to it. BUT it checks the content length header at the start of streaming back that data and, if it's more than the limit, raises an error... I find LLMs respond extremely well to function signatures like the one I use here."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=Here's%20a%20recent%20example)

### Planifier avec un Modèle Haute Capacité

Lors de la collecte des exigences ou de la rédaction des spécifications, basculez temporairement vers un modèle de capacité supérieure ou un mode de raisonnement étendu afin qu'il puisse lire, synthétiser et proposer un plan avant de coder.

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Run `/model` and pick `opus` (or another higher tier) when scoping requirements so it can reason deeply, then use Plan Mode if you want it to stay read-only until you approve edits.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Run `/model` and pick `gpt-5-codex high` for spec work that benefits from Codex's coding bias, or choose `gpt-5 high` when you need broader reasoning. Step back to your usual tier once the plan is approved.

</details>

### Get Multiple Options

Ask LLM to present several approaches with pros/cons so you can choose the best option.

**Community adoption**: 57% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-ai-technology-exploration) (n=51)

> "I'll use prompts like `what are options for HTTP libraries in Rust? Include usage examples`"
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I'll%20use%20prompts%20like)

### Read → Plan → Code → Commit

Make it explore the code, then make a plan, implement it, and commit.

**Community adoption**: 53% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-explore-plan-code-commit) (n=84)

> "There's a process that I call 'priming' the agent, where instead of having the agent jump straight to performing a task, I have it read additional context upfront to increase the chances that it will produce good outputs."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=There's%20a%20process%20that%20I%20call)

### Brain First, Assistant Second

Draft the solution yourself first, then use assistants to refine it.

**Community adoption**: 39% didn't adopt • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-brain-first-coding) (n=59)

> "I'm subconsciously defaulting to AI for all things coding. I've been using pen and paper less. As soon as I need to plan a new feature, my first thought is asking o4-mini-high how to do it, instead of my neurons. I hate this. And I'm changing it."
> — [Alberto Fortin](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20subconsciously%20defaulting%20to%20AI)

## UI & Prototyping

### Build a Prototype First

Start every project with a quick generated prototype to prove it can work.

**Community adoption**: 44% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-prototype-first-development) (n=34)

> "The best way to start any project is with a prototype that proves that the key requirements of that project can be met. I often find that an LLM can get me to that working prototype within a few minutes of me sitting down with my laptop—or sometimes even while working on my phone."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=The%20best%20way%20to%20start%20any%20project)

### Show Screenshots

Drop in screenshots and iterate - take a screenshot of the result, compare, repeat.

**Community adoption**: 38% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-visual-iteration-technique) (n=29)

> "Give Claude a visual mock by copying / pasting or drag-dropping an image... take screenshots of the result, and iterate until its result matches the mock."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Give%20Claude%20a%20visual%20mock)

### Demander des Wireframes ASCII

Lors du raffinement des mises en page, demandez à l'assistant d'esquisser des wireframes ASCII afin que vous puissiez évaluer la hiérarchie et l'espacement avant de toucher au CSS.

### Make It More Beautiful

Just ask to make the UI `more beautiful` or `more elegant` - it works.

**Community adoption**: 21% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-iterative-ui-refinement) (n=33)

> "If Claude doesn't produce a well-designed UI the first time, you can just tell it to `make it more beautiful/elegant/usable`."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=If%20Claude%20doesn't%20produce)

### Vibe Coding

Build projects through conversation rather than traditional coding - talk, accept changes, and iterate until it works.

**Community adoption**: 30% didn't adopt • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-experimental-vibe-coding) (n=47)

> "...I ask for the dumbest things like `decrease the padding on the sidebar by half` because I'm too lazy to find it. I `Accept All` always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment, usually that fixes it. The code grows beyond my usual comprehension, I'd have to really read through it for a while. Sometimes the LLMs can't fix a bug so I just work around it or ask for random changes until it goes away. It's not too bad for throwaway weekend projects, but still quite amusing. I'm building a project or webapp, but it's not really coding—I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works."
> — [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383)

## Coding

### Handle Critical Parts, Delegate the Rest

Write the critical, complex parts of the code yourself and delegate the remaining straightforward implementation to the assistant.

> "Write the critical parts and ask AI to do the rest."
> — [Anton Zhiyanov](https://antonz.org/write-code/#:~:text=Write%20the%20critical%20parts%20and%20ask%20AI%20to%20do%20the%20rest)

### Offload Tedious Tasks

Delegate boring, systematic, and time-consuming tasks to the assistant - from small variable renames to large migrations that don't require deep architectural thinking.

**Community adoption**: 64% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-offload-tedious-tasks) (n=22)

> "I'm using LLMs, but for dumber things: `rename all occurrences of this parameter`"
> — [Alberto Fortin](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20using%20LLMs,%20but%20for%20dumber%20things)

### Confirmer la Compréhension Avant de Coder

Demandez explicitement à l'outil de confirmer sa compréhension de la tâche avant de commencer l'implémentation pour garantir l'alignement et réduire les attentes décalées.

### Treat the Assistant as a Digital Intern

Give the assistant extremely precise, detailed instructions like you would to an intern - provide exact function signatures and let it handle implementation.

**Community adoption**: 60% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-treat-ai-as-intern) (n=20)

> "Once I've completed the initial research I change modes dramatically. For production code my LLM usage is much more authoritarian: I treat it like a digital intern, hired to type code for me based on my detailed instructions."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20treat%20it%20like%20a%20digital%20intern)

### Keep Code Dead Simple

Write straightforward code with clear function names, avoid inheritance and clever hacks - simple code works better with assistants.

**Community adoption**: 40% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-keep-code-dead-simple) (n=20)

> "Simple code significantly outperforms complex code in agentic contexts. I just recently wrote about ugly code and I think in the context of agents this is worth re-reading. Have the agent do `the dumbest possible thing that will work`."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Simple%20code%20significantly%20outperforms%20complex%20code)

### Prime with Existing Code

Start by dumping existing code into the chat to seed the context, then modify from there.

**Community adoption**: 36% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-context-priming) (n=31)

> "I often start a new chat by dumping in existing code to seed that context, then work with the LLM to modify it in some way."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20often%20start%20a%20new%20chat)

### Define Structure, Delegate Implementation

Provide the structure - function signatures, code outlines, or scaffolding - and let the assistant fill in the implementation details.

**Community adoption**: 35% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-precise-function-specification) (n=23)

> "I find LLMs respond extremely well to function signatures like the one I use here. I get to act as the function designer, the LLM does the work of building the body to my specification. I'll often follow-up with `Now write me the tests using pytest`. Again, I dictate my technology of choice—I want the LLM to save me the time of having to type out the code that's sitting in my head already."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20find%20LLMs%20respond%20extremely%20well)

### Provide Context for New Libraries

When using libraries outside the model's training data, feed it recent examples and documentation to teach it how the library works.

**Community adoption**: 35% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-providing-context-for-unfamiliar-apis) (n=20)

> "LLMs can still help you work with libraries that exist outside their training data, but you need to put in more work—you'll need to feed them recent examples of how those libraries should be used as part of your prompt."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=LLMs%20can%20still%20help%20you%20work%20with%20libraries)

### Generate Code, Not Dependencies

Write custom code rather than pulling in more libraries when working with assistants.

**Community adoption**: 27% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-conservative-dependency-management) (n=30)

> "Be even more conservative about upgrades than before... I strongly prefer more code generation over using more dependencies."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Be%20even%20more%20conservative%20about)

## Debugging

### Pivoter Quand l'Assistant Rencontre des Difficultés

Lorsque l'assistant échoue à plusieurs reprises à résoudre un problème spécifique, pivotez vers une approche alternative plutôt que de persister avec la même solution.

> "It's at this point that I know I need to step back, review what it did, and come up with my own plans. It's time to educate myself and think critically. AI is no longer the solution; it is a liability."
> — [Mitchell Hashimoto](https://mitchellh.com/writing/non-trivial-vibing#:~:text=It's%20at%20this%20point)

### Log Everything for Assistant Debugging

Design systems with comprehensive logging so agents can read logs to understand what's happening and self-diagnose issues.

**Community adoption**: 35% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-log-everything-for-debugging) (n=17)

> "In general logging is super important. For instance my app currently has a sign in and register flow that sends an email to the user. In debug mode (which the agent runs in), the email is just logged to stdout. This is crucial! It allows the agent to complete a full sign-in with a remote controlled browser without extra assistance. It knows that emails are being logged thanks to a CLAUDE.md instruction and it automatically consults the log for the necessary link to click."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=In%20general%20logging%20is%20super%20important)

### Let It Test and Fix Itself

Set up tools to make changes, run tests, see what fails, and try again on their own.

**Community adoption**: 27% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-ai-feedback-loops) (n=22)

> "Claude is most useful when it's capable of independently driving feedback loops that allow it to make a change, test the change, and gather context on what failed to try another iteration."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=Claude%20is%20most%20useful%20when)

### Use Subagents to Double-Check

Spawn subagents to verify details or investigate specific questions.

**Community adoption**: 22% didn't adopt • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-subagent-verification) (n=23)

> "Telling Claude to use subagents to verify details or investigate particular questions it might have, especially early on in a conversation or task, tends to preserve context availability without much downside in terms of lost efficiency."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Telling%20Claude%20to%20use%20subagents)

## Testing & QA

### Always Test Code Yourself

You absolutely cannot outsource testing - always verify the code actually works.

**Community adoption**: 67% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-comprehensive-testing-mandate) (n=27)

> "The one thing you absolutely cannot outsource to the machine is testing that the code actually works. Your responsibility as a software developer is to deliver working systems. If you haven't seen it run, it's not a working system. You need to invest in strengthening those manual QA habits."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=The%20one%20thing%20you%20absolutely%20cannot%20outsource)

### Write Tests First

Write tests first, confirm they fail, then implement until they pass.

**Community adoption**: 19% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-test-driven-development-ai) (n=21)

> "Write test first (red), Implement - Minimal code to pass (green), Refactor - Clean up with tests passing"
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Test-driven%20when%20possible)

## Review & Refactoring

### Itérer Vous-même sur la Sortie de l'Assistant

Après que l'assistant ait terminé le travail, itérez et affinez manuellement l'implémentation plutôt que de l'accepter telle quelle.

> "I almost always go in after an AI does work and iterate myself for awhile, too."
> — [Mitchell Hashimoto](https://mitchellh.com/writing/non-trivial-vibing#:~:text=I%20almost%20always%20go%20in)

### Treat AI Code as Pull Request

Review AI-generated code as if it were a colleague's pull request, providing iterative feedback comments for the assistant to address rather than editing directly yourself.

> "treating the generated code as a Merge Request on which you submit comment for correction"
> — [HN Discussion](https://news.ycombinator.com/item?id=45415232)

### Ask the Agent to Review Its Own Code

Have the assistant perform a code review on its own work before human review to surface issues and improvements.

> "Asking the agent to perform a code review on its own work is surprisingly fruitful."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Asking%20the%20agent%20to%20perform%20a%20code%20review)

### Actually Read the Code

Stop and actually inspect what has been written - you might be surprised.

**Community adoption**: 63% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-critical-code-review-strategy) (n=19)

> "Asking the agent to perform a code review on its own work is surprisingly fruitful. AI-generated code is often incorrect or inefficient. It's important for me to call out that I believe I'm ultimately responsible for the code that goes into a PR with my name on it, regardless of how it was produced. Therefore, especially in any professional context, I manually review all AI-written code and test cases."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Asking%20the%20agent%20to%20perform%20a%20code%20review)

### Always Review the Full Diff

Vibe coding can introduce unintended side effects - always review diffs carefully as the assistant may alter more than requested.

**Community adoption**: 56% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-check-for-unintended-changes) (n=16)

> "I believe I'm ultimately responsible for the code that goes into a PR with my name on it, regardless of how it was produced. Therefore, especially in any professional context, I manually review all AI-written code and test cases."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/Getting-Good-Results-from-Claude-Code.html#:~:text=I%20believe%20I'm%20ultimately%20responsible,manually%20review%20all%20AI-written%20code)

### Keep Asking for Changes

Unlike humans, assistants never get annoyed - keep asking for refactors until you're happy.

**Community adoption**: 47% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-conversational-code-refinement) (n=17)

> "If I don't like what an LLM has written, they'll never complain at being told to refactor it! `Break that repetitive code out into a function`, `use string manipulation methods rather than a regular expression`, or even `write that better!`—the code an LLM produces first time is rarely the final implementation, but they can re-type it dozens of times for you without ever getting frustrated or bored."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=If%20I%20don't%20like%20what%20an%20LLM%20has%20written)

### Edit Code in the Diff

Review changes in diff view and type corrections directly into the diff before committing.

**Community adoption**: 27% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-diff-based-iterative-refinement) (n=15)

> "I manually review all AI-written code and test cases. I'll add test cases for anything I think is missing or needs improvement, either manually or by asking the LLM to write those cases (which I then review)."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=I%20manually%20review%20all)

### One Writes, Another Reviews

Have one agent write code, then use a fresh agent to review and find problems.

**Community adoption**: 31% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-multi-agent-verification) (n=16)

> "Use Claude to write code. Run `/clear` or start a second Claude in another terminal. Have the second Claude review the first Claude's work. Start another Claude (or `/clear` again) to read both the code and review feedback. Have this Claude edit the code based on the feedback. This separation often yields better results than having a single Claude handle everything."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Have%20one%20Claude%20write%20code)

## Cross-Stage Techniques

### Laissez l'Assistant Travailler Pendant Que Vous Faites Autre Chose

Utilisez les assistants de manière asynchrone afin qu'ils puissent travailler sur des tâches pendant que vous gérez d'autres responsabilités.

> "I think the faster/slower argument for me personally is missing the thing I like the most: the AI can work for me while I step away to do other things."
> — [Mitchell Hashimoto](https://mitchellh.com/writing/non-trivial-vibing#:~:text=I%20think%20the%20faster)

### Changer les Styles de Sortie de l'Assistant

Sélectionnez le style de sortie de l'assistant qui correspond à votre objectif actuel.

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

**Switch styles quickly**
Run `/output-style` to open the picker, or `/output-style learning` to jump straight into Learning mode. The selection is stored per project in `.claude/settings.local.json`.

**Teach-yourself modes**
Default stays focused on shipping; `explanatory` inserts insight callouts; `learning` adds `TODO(human)` markers so you fill in key pieces yourself.

**Create custom styles**
Run `/output-style:new I want ...` to scaffold a markdown file in `~/.claude/output-styles`. Tweak the frontmatter and instructions; project-specific variants live in `.claude/output-styles/`.

**Why styles differ**
Styles replace Claude Code's default system prompt, unlike `CLAUDE.md` (user message) or `--append-system-prompt` (appends).

</details>

### Clear Context Between Tasks

Reset the assistant's context window between unrelated tasks to prevent confusion and improve performance on new problems.

**Community adoption**: 67% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-clear-context-between-tasks) (n=15)

> "During long sessions, Claude's context window can fill with irrelevant conversation, file contents, and commands. This can reduce performance and sometimes distract Claude. Use the `/clear` command frequently between tasks to reset the context window."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=During%20long%20sessions%2C%20Claude's%20context)

### Choose Tools by Conversational Style

Pick coding assistants based on whether you prefer human-like collaboration or structured, robot-like efficiency - conversational personality significantly affects productivity and enjoyment.

> "In terms of personality, it's the opposite for me: Claude Code feels like my pair-programming partner, while Codex feels like a robot (very structured but not very human in its conversational style).

Problem is after a while, the 'You are absolutely right!' kinda gets on my nerves.

Codex is dry. You can insult it and it doesn't even answer. No personality. Claude is like, a friend who admits messing up. I spend like close to 10 hours a day coding between CC and Codex CLI and I see huge differences in personality and creativity. I like Claude better for that. Much more creative.

Codex is monotone straight to the point, but most importantly the reason why it is better is because it's not agreeable at all. It will challenge you when you're suggesting something wrong and stay with its opinion."
> — [Reddit Community](https://www.reddit.com/r/ClaudeAI/comments/1nk4v4k/comment/nev86ot)

### Choisir le Bon Modèle pour le Travail

Avant de commencer une nouvelle tâche, choisissez deux leviers : le bon modèle (modalité, longueur de contexte, fiabilité des appels d'outils, latence, coût) et le bon niveau de raisonnement (allouer plus/moins de tokens de réflexion) — ne pas utiliser aveuglément les paramètres par défaut.

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Two levers at task start:
1. `/model` - pick `fast` for routine edits, `long-context` for multi-file or long docs, `vision-strong` for UI/screenshots.
2. Reasoning level - enable extended thinking for complex debugging, architecture work, or ambiguous specs so the assistant budgets more reasoning tokens.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Start with `gpt-5-minimal`/`gpt-5-low` for quick edits; choose a higher‑reasoning variant `gpt-5-high`/`gpt-5-medium` when complexity rises.

</details>

### Centraliser les Fichiers de Mémoire

Gardez un document d'instructions canonique et dirigez tous les autres fichiers d'agent vers celui-ci avec une ligne de pointeur criante, un lien symbolique ou une inclusion @file afin que les conseils inter-outils restent cohérents.

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Keep `CLAUDE.md` as the source of truth and use one of these three ways.

1. Put `@CLAUDE.md` into `AGENTS.md`.

2. Symlink `AGENTS.md` to `CLAUDE.md` with `ln -sf CLAUDE.md AGENTS.md` so both tools share the same file.

3. Leave `AGENTS.md` as a single line: `READ CLAUDE.md FIRST!!!`.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Use the same trio from the Codex side.

1. If Codex holds the primary text, leave `AGENTS.md` full and place `@AGENTS.md` inside `CLAUDE.md` so both tools land in the same doc.

2. Run `ln -sf CLAUDE.md AGENTS.md` so the file Codex reads is just a symlink to `CLAUDE.md`.

3. When `CLAUDE.md` is canonical, keep `AGENTS.md` to one line: `READ CLAUDE.md FIRST!!!`.

</details>

### Interrupt and Redirect Often

Don't let the assistant go too far down the wrong path - interrupt, provide feedback, and redirect as soon as you notice issues.

**Community adoption**: 60% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-interrupt-and-redirect-often) (n=15)

> "Press Escape to interrupt Claude during any phase (thinking, tool calls, file edits), preserving context so you can redirect or expand instructions. Double-tap Escape to jump back in history, edit a previous prompt, and explore a different direction. You can edit the prompt and repeat until you get the result you're looking for."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Press%20Escape%20to%20interrupt%20Claude)

### Use an Agent as a Coding Partner

Collaborate like with a coding partner - explain problems, get feedback, and work together on solutions.

**Community adoption**: 63% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-ai-coding-partner) (n=16)

> "Claude Code feels like pairing with someone with a few years under their belt who just needs the occasional nudge. Then like with pairing, it's review, refactor and test time because it's still your name on the git commit."
> — [Orta Therox](https://blog.puzzmo.com/posts/2025/06/07/orta-on-claude/#:~:text=Claude%20Code%20feels%20like%20pairing)

### Learn From It, Code Yourself

Use assistants to learn new languages and concepts, then apply that knowledge when you code.

**Community adoption**: 43% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-learning-oriented-ai-interaction) (n=14)

> "I'm leveraging them to learn Go, to upskill myself. And then I apply this new knowledge when I code."
> — [Alberto Fortin](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20leveraging%20them%20to%20learn%20Go)

### Use Strong Emphasis in Prompts

Use IMPORTANT, NEVER, ALWAYS liberally in prompts to steer the model away from common mistakes - it's still the most effective approach.

**Community adoption**: 50% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-use-strong-emphasis-words) (n=14)

> "Unfortunately CC is no better when it comes to asking the model to not do something. IMPORTANT, VERY IMPORTANT, NEVER and ALWAYS seem to be the best way to steer the model away from landmines. I expect the models to get more steerable in the future and avoid this ugliness. But for now, CC uses this liberally, and so should you."
> — [Vivek (MinusX AI Team)](https://minusx.ai/blog/decoding-claude-code/#:~:text=Unfortunately%20CC%20is%20no%20better)

### Build Fast, Foolproof Tools

Create tools that respond quickly, provide clear error messages, and protect against misuse by agents.

**Community adoption**: 17% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-build-fast-foolproof-tools) (n=12)

> "Tools need to be fast. The quicker they respond (and the less useless output they produce) the better. Crashes are tolerable; hangs are problematic. Tools need to be user friendly! Tools must clearly inform agents of misuse or errors to ensure forward progress. Tools need to be protected against an LLM chaos monkey using them completely wrong. There is no such thing as user error or undefined behavior!"
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Tools%20need%20to%20be%20fast)

### Run Multiple Agents in Parallel

Stop waiting for one agent to finish before starting another - run multiple agents in parallel on separate features without conflicts or confusion.

**Community adoption**: 14% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-run-multiple-agents-parallel) (n=14)

> "We are exploring solving both of these issues in sketch.dev using containers. By default sketch creates a little development environment in a container with a copy of the source code and the runner has the ability to extract git commits from the container. This lets you run many simultaneously."
> — [David Crawshaw](https://crawshaw.io/blog/programming-with-agents#:~:text=We%20are%20exploring%20solving%20both%20of%20these%20issues)

### Run Without Permissions for Easy Tasks

Enable autonomous mode when tasks are straightforward enough that you'd accept all changes anyway - skip the babysitting.

> "I disable all permission checks. Which basically means I run `claude --dangerously-skip-permissions`. More specifically I have an alias called claude-yolo set up."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=I%20disable%20all%20permission%20checks)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Run `claude --dangerously-skip-permissions` to enable YOLO mode where Claude runs uninterrupted without permission prompts.

**Switch during session:** Use `/permissions` to manage tool permissions mid-session without restarting. Set allow rules for specific tools to skip approval prompts.

**When to use:**
• Fixing lint errors across multiple files
• Simple refactoring and variable renames
• Routine code updates and migrations
• Tasks where you'd likely accept all changes anyway

**Safety considerations:**
• Best used in containers or VMs for isolation
• Avoid on critical production systems
• Consider using `allowedTools` config for granular control instead of blanket permissions

**Setup alias:** Many users create `alias cc='claude --dangerously-skip-permissions'` for quick access.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Enable full autonomous mode with `codex --full-auto` or use in-session `/mode` command.

**Switch during session:** Use `/mode` to hot-swap between permission levels without losing session context. Select with arrow keys from suggest/auto-edit/full-auto modes.

**Permission modes:**
• `--suggest` - Suggests changes, requires approval
• `--auto-edit` - Auto-edits files, asks for command approval  
• `--full-auto` - Complete autonomy for files and commands

**When to use full-auto:**
• Systematic refactoring tasks
• Bulk file operations
• Lint fixes and code cleanup
• Well-defined, low-risk operations

</details>

### Une Session Doit Avoir Un Objectif

Utilisez le prompt `L'objectif de cette session est <objectif spécifique>. Informez-moi si nous dérivons.` soit au début de chaque session, soit ajoutez-le à votre fichier de mémoire (AGENTS.md, CLAUDE.md) pour prévenir l'empoisonnement du contexte et augmenter la dirigeabilité de l'agent - appliquant le Principe de Responsabilité Unique aux conversations IA.

### Utiliser des Sessions de Fonctionnalité

Isolez chaque fonctionnalité ou tâche dans des sessions séparées pour réduire le gonflement du contexte et améliorer la précision, tout comme les branches de fonctionnalités dans git isolent les modifications de code.

### Ask Open Questions, Not Leading Ones

Avoid 'Am I right that...' questions - instead ask for pros/cons, alternatives, and 'What am I missing?' to counteract LLM's tendency to agree.

> "My best current technique for avoiding this is a bit of role-play that gives the coding agent a reason not to blindly trust the code review... 'A reviewer did some analysis of this PR. They're external, so reading the codebase cold... 1) should we hire this reviewer 2) which of the issues they've flagged should be fixed?'"
> — [Jesse Vincent](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/#:~:text=My%20best%20current%20technique)

### Start cheap and fast; escalate when stuck

Begin with faster/cheaper models for routine tasks, then escalate to more powerful models only when you hit complex problems.

**Community adoption**: 19% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-smart-model-escalation) (n=16)

> "Sonnet 4 handles 90% of tasks effectively. Switch to Opus when Sonnet gets stuck. Recommend starting with Sonnet and providing comprehensive context."
> — [Sankalp](https://sankalp.bearblog.dev/my-claude-code-experience-after-2-weeks-of-usage/#:~:text=Sonnet%204%20handles%2090%25)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Use `/model` to switch. Cheaper, faster, but less accurate: `Claude Sonnet 4`. Top-graded: `Claude Opus 4.1`.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Use `/model` to switch. Cheaper, faster, but less accurate: `gpt-5-medium`. Top-graded: `gpt-5-high`.

</details>

### Créer des Points de Restauration en Codant

Créez des points de contrôle vers lesquels vous pouvez revenir lorsque les expériences échouent—capturez des états de travail connus et bons avant les changements risqués.

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Commit known‑good states before experiments. Example: `git commit -m "Working state before refactor"`. For risky changes, branch first: `git checkout -b experiment/feature`. If it fails, `git reset --hard HEAD~1` or switch back to `main`. Use `git stash` for quick temporary saves.

</details>

<details>
<summary><strong>Cursor</strong></summary>

Cursor records AI edits as undoable checkpoints. Use Cmd+Z/Ctrl+Z to step back through changes. For durable rollback, commit working states with messages like ‘Checkpoint before schema rewrite’; use branches for experiments and review diffs before merge.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Before large edits, run a save‑state commit: `git commit -am "Checkpoint before Codex changes"`. For experiments, branch: `git checkout -b codex/experiment`. If results disappoint, `git reset --hard HEAD~1` or abandon branch. Use session separation for risky attempts.

</details>

