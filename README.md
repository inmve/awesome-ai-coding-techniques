<!-- Generated from data/entries.json by scripts/build_readme.py. Do not edit by hand. -->

# Software Practices

An open reference of software development practices, from older engineering practices to work with coding agents.
For each practice: a definition, when it appeared, where it grew from, and the sources that describe it.

- **Site:** [https://inmve.github.io/software-practices/](https://inmve.github.io/software-practices/) (the same data, with a timeline and quotes on hover)
- **Data:** [`data/entries.json`](data/entries.json), the single source; this README is generated from it
- **Survey for your team:** [team-survey](https://github.com/inmve/team-survey), a GitHub template that asks the same practices inside your team

94 entries, 162 sources, 152 of them with a verbatim quote stored in the data. Preliminary edition: dates are not verified yet.

Inside every section the newest entries come first; practices from before coding agents come last.

## Contents

- [Approaches](#approaches)
- [Planning](#planning)
- [UI & Prototype](#ui--prototype)
- [Coding](#coding)
- [Debugging](#debugging)
- [Testing & QA](#testing--qa)
- [Review](#review)
- [Across stages: Prompting](#across-stages-prompting)
- [Across stages: Context and memory](#across-stages-context-and-memory)
- [Across stages: Sessions and parallel work](#across-stages-sessions-and-parallel-work)
- [Across stages: Models and budget](#across-stages-models-and-budget)
- [Across stages: The human's part](#across-stages-the-humans-part)
- [Teams and projects](#teams-and-projects)

## Approaches

- **Software factory** (2026). An approach in which a team agrees that people neither write nor review the code: the team states the intent, and evals control the quality.
  Sources: [Justin McCarthy, 2026-02-06](https://factory.strongdm.ai/); [Ryan Lopopolo, 2026-02-11](https://openai.com/index/harness-engineering/).
  Grew from: Software factory (1968).
- **Dark factory** (2026). An approach in which the development process works as a black box that turns specifications into software, and people do not write the code.
  Sources: [Dan Shapiro, 2026-01-23](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/).
  Grew from: Lights-out manufacturing.
- **Spec-driven development** (2025). An approach in which the specification is the source of truth: the developer edits the specification, and the agent generates the code from it.
  Sources: [GitHub Engineering, 2025-09-30](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-using-markdown-as-a-programming-language-when-building-with-ai/); [Anton Zhiyanov](https://antonz.org/write-code/#:~:text=If%2C%20given%20the%20prompt%2C%20AI%20does%20the%20job%20perfectly%20on%20first%20or%20second%20iteration%20%E2%80%94%20fine.%20Otherwise%2C%20stop%20refining%20the%20prompt); [Simon Willison, 2025-03-11](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=Here's%20a%20recent%20example); [Ryan Lopopolo, 2026-02-11](https://openai.com/index/harness-engineering/).
  Grew from: Waterfall.
- **Vibe coding** (2025). Building software by talking to an agent without reading the code: every change is accepted, errors are pasted back until it works.
  Sources: [Andrej Karpathy, 2025-02-02](https://x.com/karpathy/status/1886192184808149383).
- **Lights-out manufacturing**. An approach to manufacturing in which a factory runs without people on site, so it can work with the lights off.
  Sources: [Owen Sweeney, 2026-09-23](https://www.openhands.dev/blog/what-is-an-ai-dark-factory).
  Led to: Dark factory.
- **Agile** (2001). Developing in short iterations with frequent feedback instead of a detailed upfront plan.
  Sources: [Claude Code team director (page event summary names Fiona Fung), 2026-06-03](https://claude.com/de/resources/articles/running-an-ai-native-engineering-org).
- **Extreme Programming** (1999). An agile method: pair programming, tests before code, continuous integration, frequent releases.
  Sources: [Benji Weber, 2025-07-14](https://benjiweber.co.uk/blog/?p=2657).
- **Waterfall** (1970). A development model where stages run strictly in order: requirements, design, code, testing, deployment.
  Sources: [Marc Brooker, 2026-04-09](https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec).
  Led to: Spec-driven development.
- **Software factory (1968)**. An approach in which software is produced the way industry produces goods, with standard tools and a managed process.
  Sources: [Addy Osmani, 2026-07-20](https://addyosmani.com/blog/software-factories/).
  Led to: Software factory.

## Planning

- **Plan before code** (2025). The practice in which the agent first lays out steps, risks and checks, and the developer corrects that outline before any code is written.
  Sources: [Indragie Karunaratne, 2025-07-01](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=If%20you%20want%20to%20iterate%20on%20the%20plan); [Jesse Vincent, 2025-10-05](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/#:~:text=Check%20out%20the%20current%20state); [Mitchell Hashimoto, 2025-10-11](https://mitchellh.com/writing/non-trivial-vibing#:~:text=Creating%20a%20comprehensive%20plan).
- **Stable libraries** (2025). The practice in which the developer picks established libraries that existed before the model's training cutoff.
  Sources: [Simon Willison, 2025-03-11](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20gain%20enough%20value%20from%20LLMs).
  Grew from: Choose boring technology.
- **Vertical slices in agent work plans**. The practice in which the agent's work plan for a feature is cut into vertical slices that cross backend and frontend, so that integration is exercised before the end of the work.
  Sources: [shinpr](https://github.com/shinpr/claude-code-workflows).
- **Choose boring technology** (2015). The practice in which a team spends a small, fixed number of «innovation tokens» on new technologies and uses well-known ones for everything else.
  Sources: [Dan McKinley, 2015-03-30](https://mcfunley.com/choose-boring-technology); [Simon Willison, 2026-03-09](https://simonwillison.net/2026/Mar/9/not-so-boring/).
  Led to: Stable libraries.
- **User story** (1999). A short requirement written from the user's side: who, what they want, and why.
  Sources: [Ron Jeffries, 2001-08-30](https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/).

## UI & Prototype

- **Screenshot iteration** (2026). The practice in which the agent is given a screenshot of the result or of a mock-up, and the change and the screenshot are repeated until they match.
  Sources: [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Give%20Claude%20a%20visual%20mock); [David Crawshaw](https://crawshaw.io/blog/programming-with-agents#:~:text=I%20opened%20a%20second%20copy%20of%20Sketch); [Anthropic](https://docs.anthropic.com/en/docs/claude-code/common-workflows#:~:text=You%20can%20use%20any%20of%20these%20methods); [kent-tokyo (DEV Community handle), 2026-06-03](https://dev.to/kent-tokyo/what-i-do-before-letting-claude-code-touch-web-app-design-53n0).
- **Generated prototype** (2025). The practice in which a project starts with a quickly generated prototype that shows whether the key requirement can be met.
  Sources: [Simon Willison, 2025-03-11](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=The%20best%20way%20to%20start%20any%20project).
- **Low-fidelity wireframes**. The practice in which a screen layout is sketched roughly, without visual detail, before the interface is designed or built.
  Sources: [Carlos Chinchilla, 2025-12-25](https://medium.com/@calufa/ascii-driven-development-850f66661351).

## Coding

- **CLI tools instead of MCP** (2025). The practice in which services are given to the agent as small command-line tools, each with a README that the agent reads only when it needs the tool, instead of MCP servers.
  Sources: [Shrivu Shankar, 2025-11-02](https://blog.sshh.io/p/how-i-use-every-claude-code-feature); [Mario Zechner, 2025-11-30](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/).
- **Tools built for agents** (2025). The practice in which the tools an agent calls are made to respond quickly, report errors clearly and withstand misuse.
  Sources: [Armin Ronacher, 2025-06-12](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Tools%20need%20to%20be%20fast); [Shrivu Shankar, 2025-11-02](https://blog.sshh.io/p/how-i-use-every-claude-code-feature).
- **Simple code for agents** (2025). The practice in which code is kept plain: descriptive function names, no inheritance, no clever constructs.
  Sources: [Armin Ronacher, 2025-06-12](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Simple%20code%20significantly%20outperforms%20complex%20code).
  Grew from: KISS.
- **Generated code in place of dependencies** (2025). The practice in which the agent writes the needed code in the project, and a new library is not added.
  Sources: [Armin Ronacher, 2025-06-12](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Be%20even%20more%20conservative%20about); [Ryan Lopopolo, 2026-02-11](https://openai.com/index/harness-engineering/).
- **Codemods**. The practice in which a large mechanical change across a codebase is made by a program that rewrites the code.
  Sources: [Codegen Technical Staff, 2025-03-01](https://codegen.com/swe-agents-are-better-with-codemods/).
  Led to: Delegation of routine tasks.
- **Feature branch** (2005). A separate version-control branch per feature, merged into the main branch when ready.
  Sources: [Martin Fowler, 2020-05-07](https://martinfowler.com/bliki/FeatureBranch.html).
  Led to: Parallel agents, Feature sessions.
- **Pair programming** (1999). Two people work on the same code: one types, the other watches and thinks ahead.
  Sources: [Benji Weber, 2025-07-14](https://benjiweber.co.uk/blog/?p=2657); [Matt Wynne, 2026-03-04](https://mattwynne.net/pair-programming-in-the-age-of-agents).
  Led to: Agent as a pair partner.
- **KISS** (1960). A design principle: a simple system is more reliable than a complex one.
  Sources: [Erick, 2025-10-30](https://matsen.fredhutch.org/general/2025/10/30/agentic-coding-principles.html).
  Led to: Simple code for agents.

## Debugging

- **Agent feedback loop** (2025). The practice in which the agent is given a check it can run (tests, a build, a linter) and repeats the change and the check until the check passes.
  Sources: [Indragie Karunaratne, 2025-07-01](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=Claude%20is%20most%20useful%20when); [Simon Willison, 2025-10-05](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/#:~:text=Warnings%20are%20a%20great%20example).
  Grew from: Continuous integration.
- **Logs for agent debugging** (2025). The practice in which a system is built with detailed logging, so that an agent can read the logs and find the cause of a problem.
  Sources: [Armin Ronacher, 2025-06-12](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=In%20general%20logging%20is%20super%20important).
- **Rubber duck debugging** (1999). Finding a bug by explaining the code line by line out loud to anyone, even a rubber duck.
  Sources: [Emma Klint, 2026-03-17](https://emmaklint.substack.com/p/why-i-explain-my-problems-to-a-robot).
  Led to: Agent as a pair partner.

## Testing & QA

- **Browser checks by an agent** (2026). The practice in which an agent drives a browser on the running application to check a change against each acceptance criterion and reports what it saw, with screenshots, for each criterion.
  Sources: [Abhishek Ray, 2026-03-10](https://www.claudecodecamp.com/p/i-m-building-agents-that-run-while-i-sleep).
- **Tests before agent code** (2025). The practice in which tests are written first and shown to fail, and the agent then writes the implementation until they pass.
  Sources: [Chris Dzombak, 2025-08](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Test-driven%20when%20possible); [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Ask%20Claude%20to%20write%20tests); [Arpan Patel, 2026-05-26](https://arps18.github.io/posts/claude-code-mastery/).
  Grew from: Test-driven development.
- **Manual verification of agent code** (2025). The practice in which the developer runs agent-written code and confirms that it works, without relying on the agent's own report about tests.
  Sources: [Simon Willison, 2025-03-11](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=The%20one%20thing%20you%20absolutely%20cannot%20outsource).
- **Test-driven development** (2002). Write a failing test first, then the minimal code to pass it, then refactor.
  Sources: [thoughtbot (author name not shown in the saved text), 2026-01-12](https://thoughtbot.com/blog/prevent-the-robocalypse-with-tdd).
  Led to: Tests before agent code.
- **Continuous integration** (1991). Merging changes into the shared branch often, with an automatic build and tests on every merge.
  Sources: [Ryan Lopopolo, 2026-02-11](https://openai.com/index/harness-engineering/); [Giles Edwards-Alexander, 2026-09-02](https://martinfowler.com/articles/exploring-gen-ai/an-accidental-blackboard.html).
  Led to: Agent feedback loop.

## Review

- **Vulnerability hunting agents with test proof** (2026). The practice in which agents search parts of an application for one category of vulnerability, a separate verifier agent proves each finding with a test in the application's own test suite, and findings arrive as pull requests.
  Sources: [Zack Deveau, 2026-07-29](https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model).
- **Adversarial review** (2026). The practice in which one agent does the work and a second agent, often on a different model, reviews it with the task of finding problems.
  Sources: [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Have%20one%20Claude%20write%20code); [Jesse Vincent, 2025-10-05](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/#:~:text=I%20typically%20double); [Arpan Patel, 2026-05-26](https://arps18.github.io/posts/claude-code-mastery/).
- **Agent self-review** (2025). The practice in which the agent reviews its own code before a person reviews it.
  Sources: [Chris Dzombak, 2025-08](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Asking%20the%20agent%20to%20perform%20a%20code%20review); [Mario Zechner, 2025-11-30](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/).
- **Reading agent-written code** (2025). The practice in which the developer reads the code an agent wrote before accepting it.
  Sources: [Chris Dzombak, 2025-08](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Asking%20the%20agent%20to%20perform%20a%20code%20review); [Mitchell Hashimoto, 2025-10-11](https://mitchellh.com/writing/non-trivial-vibing#:~:text=I'm%20not%20shipping%20code); [Mitchell Hashimoto, 2025-10-11](https://mitchellh.com/writing/non-trivial-vibing#:~:text=Please%20don't%20ever%20ship); [Chris Dzombak, 2025-08](https://www.dzombak.com/blog/2025/08/Getting-Good-Results-from-Claude-Code.html#:~:text=I%20believe%20I'm%20ultimately%20responsible,manually%20review%20all%20AI-written%20code).
- **Edits in the diff** (2025). The practice in which the developer reviews the changes in a diff view and types corrections into the diff before committing.
  Sources: [Chris Dzombak, 2025-08](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=I%20manually%20review%20all); [Justin Paul, 2026-07-30](https://www.jpaul.me/2026/07/the-workflow-reviewing-ai-code/).
- **Subagent verification**. The practice in which the agent starts subagents to verify details or to investigate separate questions.
  Sources: [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Telling%20Claude%20to%20use%20subagents).
- **Pull request** (2008). A request to merge changes that hosts the discussion and review.
  Sources: [GitHub Blog (author name not shown in the saved text), 2026-05-07](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/); [GitHub](https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results).

## Across stages: Prompting

- **Open questions** (2025). A prompting habit in which the model is asked for pros and cons, alternatives and missing points, instead of being asked to confirm an opinion.
  Sources: [Jesse Vincent, 2025-10-05](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/#:~:text=My%20best%20current%20technique).
- **“More beautiful” prompt** (2025). A prompting habit in which the agent is asked to make an interface “more beautiful” or “more elegant”, with no further detail.
  Sources: [Indragie Karunaratne, 2025-07-01](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=If%20Claude%20doesn't%20produce).
- **Several options with trade-offs** (2025). A prompting habit in which the model is asked for several approaches with the pros and cons of each.
  Sources: [Simon Willison, 2025-03-11](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I'll%20use%20prompts%20like).
- **Developer-defined structure** (2025). The practice in which the developer gives function signatures, an outline or scaffolding, and the agent fills in the implementation.
  Sources: [Simon Willison, 2025-03-11](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20find%20LLMs%20respond%20extremely%20well); [Anton Zhiyanov, 2025-09-26](https://antonz.org/write-code/#:~:text=Write%20an%20outline%20of%20the%20code%20and%20ask%20AI%20to%20fill%20the%20missing%20parts); [Mitchell Hashimoto, 2025-10-11](https://mitchellh.com/writing/non-trivial-vibing#:~:text=AI%20is%20very%20good%20at%20fill); [Between the Prompts](https://betweentheprompts.com/design-partner/#:~:text=But%20instead%20of%20fixing%20the%20code%20myself%2C%20I%20explained%20why%20it%20was%20wrong%20and%20gave%20it%20more%20precise%20instructions.%20When%20I%20told%20it%20%E2%80%9CYou%20misunderstood%2C%20it%20should%E2%80%A6%E2%80%9D%20and%20provided%20clearer%20guidance%2C%20I%20was%20impressed%20at%20how%20it%20could%20understand%20the%20problem%20and%20update%20the%20code%20accordingly.).

## Across stages: Context and memory

- **Single source for agent instructions** (2026). The practice in which one instruction document is canonical and the documents of other agent tools point to it through a pointer line, a symlink or an include.
  Sources: [Przemek, 2026-09-23](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/); [FerroxLabs](https://github.com/FerroxLabs/agents-md).
- **Check that the instruction file is loaded** (2026). The practice in which the developer checks which instruction file the agent tool actually reads, for example with a marker word, before relying on it.
  Sources: [Systima, 2026-07-12](https://systima.ai/blog/claude-code-vs-opencode-token-overhead); [Przemek, 2026-09-23](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/).
- **Compaction** (2026). The practice in which a long agent session is summarized at a milestone or near the context limit, with instructions on what the summary keeps, and work continues in a new context from the summary.
  Sources: [Arpan Patel, 2026-05-26](https://arps18.github.io/posts/claude-code-mastery/).
- **Repository knowledge as the system of record** (2026). The practice in which decisions, plans, conventions and other context are kept as versioned files in the repository instead of chats, documents and people's heads, so that agents can read them.
  Sources: [Ryan Lopopolo, 2026-02-11](https://openai.com/index/harness-engineering/); [shinpr](https://github.com/shinpr/claude-code-workflows).
- **Harness engineering** (2026). The practice in which, after each agent mistake, the developer adds a rule, a script or a check to the agent's environment so that the mistake does not happen again.
  Sources: [Mitchell Hashimoto, 2026-02-05](https://mitchellh.com/writing/my-ai-adoption-journey); [Ryan Lopopolo, 2026-02-11](https://openai.com/index/harness-engineering/).
- **Evals for agent instructions** (2026). The practice in which a team runs the same agent tasks as evals with and without a change to instruction files or documentation, and keeps the change only after several runs show an improvement.
  Sources: [Jude Gao, 2026-01-27](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals); [Addie Beach, Rui Martins Lacerda, 2026-09-09](https://www.datadoghq.com/blog/ai-development-golden-paths/).
- **Repeated prompt as a skill** (2025). The practice in which a prompt or workflow that the developer keeps repeating is saved as a skill or command file, checked into git and run by name.
  Sources: [Harper Reed, 2025-12-03](https://harper.blog/2025/12/03/claude-code-email-productivity-mcp-agents/); [Arpan Patel, 2026-05-26](https://arps18.github.io/posts/claude-code-mastery/).
- **Document & Clear** (2025). The practice in which, for a large task, the agent writes its plan and progress to a file, the context is cleared, and a new session reads the file and continues the work.
  Sources: [Shrivu Shankar, 2025-11-02](https://blog.sshh.io/p/how-i-use-every-claude-code-feature); [Mario Zechner, 2025-11-30](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/).
- **Agent session log review** (2025). The practice in which saved agent session logs are reviewed regularly, by scripts, people or another agent, for repeated errors and permission requests, and the agent's instructions and tools are changed in response.
  Sources: [Shrivu Shankar, 2025-11-02](https://blog.sshh.io/p/how-i-use-every-claude-code-feature); [OpenAI](https://developers.openai.com/codex/learn/best-practices).
- **Context priming with code** (2025). The practice in which a session starts by placing existing code into the context, and changes are made from there.
  Sources: [Simon Willison, 2025-03-11](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20often%20start%20a%20new%20chat); [Lee Robinson, 2026-01-09](https://cursor.com/blog/agent-best-practices).
- **Documentation for new libraries** (2025). The practice in which the agent is given current documentation and examples for a library that is missing from the model's training data.
  Sources: [Simon Willison, 2025-03-11](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=LLMs%20can%20still%20help%20you%20work%20with%20libraries); [Jude Gao, 2026-01-27](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals).
- **Memory file** (2025). The practice in which project instructions for the agent (commands, conventions, constraints) are kept in a text document that the agent reads at the start of every session.
  Sources: [agents.md community](https://agents.md/#:~:text=Think%20of%20AGENTS.md%20as%20a%20README%20for%20agents); [Shrivu Shankar, 2025-11-02](https://blog.sshh.io/p/how-i-use-every-claude-code-feature).
- **Context reset between tasks**. The practice in which the agent's context is cleared before an unrelated task begins.
  Sources: [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=During%20long%20sessions%2C%20Claude's%20context); [aider.chat](https://aider.chat/docs/usage/tips.html).

## Across stages: Sessions and parallel work

- **Recurring cleanup process** (2026). The practice in which a team records its code rules in the repository and on a regular cadence runs background agent tasks that look for deviations from the rules or stale documentation and open pull requests with fixes.
  Sources: [Ryan Lopopolo, 2026-02-11](https://openai.com/index/harness-engineering/); [Anthropic](https://code.claude.com/docs/en/common-workflows).
- **Bootable app per worktree** (2026). The practice in which the application can be started separately in each git worktree, so that every agent runs and checks its own instance.
  Sources: [Ryan Lopopolo, 2026-02-11](https://openai.com/index/harness-engineering/).
- **Orchestrator and workers** (2026). The practice in which one agent holds the plan, hands subtasks to worker agents and merges their results.
  Sources: [Anthropic (engineering blog, no personal byline in saved text), 2025-06-13](https://www.anthropic.com/engineering/multi-agent-research-system); [Wilson Lin, 2026-01-14](https://cursor.com/blog/scaling-agents).
- **Feature sessions** (2026). The practice of keeping each feature or task in its own agent session so the context does not bloat.
  Sources: [Fabien Sanglard, 2026-08-21](https://fabiensanglard.net/agent.md/index.html); [Lee Robinson, 2026-01-09](https://cursor.com/blog/agent-best-practices).
  Grew from: Feature branch.
- **Disposable machine for the agent** (2026). The practice in which the agent runs with broad permissions, up to root, on a throwaway machine or virtual machine that has no access to production systems or secrets beyond what development needs.
  Sources: [Granda, 2026-01-02](https://granda.org/en/2026/01/02/claude-code-on-the-go/); [Harper Reed, 2026-09-22](https://harper.blog/2026/09/22/break-away/).
- **Parallel attempts** (2025). The practice in which several agents or models work on the same problem at the same time, each with its own approach, and the developer compares the results.
  Sources: [Saffron Huang, Bryan Seethor, Esin Durmus, Kunal Handa, Miles McCain, Michael Stern, Deep Ganguli, 2025-12-02](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic); [Lee Robinson, 2026-01-09](https://cursor.com/blog/agent-best-practices).
- **Asynchronous agent work** (2025). The practice in which the agent works on a task while the developer is busy with something else.
  Sources: [Mitchell Hashimoto, 2025-10-11](https://mitchellh.com/writing/non-trivial-vibing#:~:text=I%20think%20the%20faster); [Granda, 2026-01-02](https://granda.org/en/2026/01/02/claude-code-on-the-go/).
- **Permission-free mode** (2025). The practice in which permission prompts are switched off for tasks whose changes the developer would accept anyway.
  Sources: [Armin Ronacher, 2025-06-12](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=I%20disable%20all%20permission%20checks); [Jökull Sólberg, 2025-07-03](https://www.solberg.is/claude-devcontainer).
- **Parallel agents** (2025). The practice in which several agents work on separate tasks at the same time, each in its own isolated copy of the repository.
  Sources: [David Crawshaw, 2025-06-08](https://crawshaw.io/blog/programming-with-agents#:~:text=We%20are%20exploring%20solving%20both%20of%20these%20issues); [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=I%20disable%20all%20permission%20checks); [Anthropic](https://docs.anthropic.com/en/docs/claude-code/common-workflows#:~:text=Git%20worktrees%20allow%20you%20to%20check%20out%20multiple%20branches).
  Grew from: Feature branch.

## Across stages: Models and budget

- **Model choice per task** (2026). The practice in which the model and its reasoning level are chosen for each task by modality, context length, tool-call reliability, latency and cost.
  Sources: [Abhishek Ray, 2026-03-10](https://www.claudecodecamp.com/p/i-m-building-agents-that-run-while-i-sleep).
- **Model escalation** (2025). The practice in which work starts on a faster and cheaper model and moves to a more capable one when the task turns out to be hard.
  Sources: [Sankalp, 2025-07-17](https://sankalp.bearblog.dev/my-claude-code-experience-after-2-weeks-of-usage/#:~:text=Sonnet%204%20handles%2090%25).

## Across stages: The human's part

- **Early interruption** (2026). The practice in which the developer stops the agent as soon as it goes in a wrong direction and gives it a correction.
  Sources: [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Press%20Escape%20to%20interrupt%20Claude); [Mikayla Maki, 2026-01-23](https://zed.dev/blog/on-programming-with-agents).
- **Learning with an agent** (2026). The practice in which the developer uses an agent to learn a language or a concept and then writes the code without it.
  Sources: [Alberto Fortin](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20leveraging%20them%20to%20learn%20Go); [Lee Robinson, 2026-01-09](https://cursor.com/blog/agent-best-practices).
- **Deliberate practice without agents** (2025). The practice in which an engineer now and then solves a problem without an agent, even one the agent could solve, to keep their own skills.
  Sources: [Saffron Huang, Bryan Seethor, Esin Durmus, Kunal Handa, Miles McCain, Michael Stern, Deep Ganguli, 2025-12-02](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic).
- **Manual refinement of agent output** (2025). The practice in which the developer reworks the agent's implementation by hand after the agent has finished.
  Sources: [Mitchell Hashimoto, 2025-10-11](https://mitchellh.com/writing/non-trivial-vibing#:~:text=I%20almost%20always%20go%20in); [Conrad Irwin](https://zed.dev/blog/not-building-ai-for-the-money).
- **Change of approach after repeated failures** (2025). The practice in which, after the agent fails at the same problem several times, the developer switches to a different approach.
  Sources: [Mitchell Hashimoto, 2025-10-11](https://mitchellh.com/writing/non-trivial-vibing#:~:text=It's%20at%20this%20point); [aider.chat](https://aider.chat/docs/usage/tips.html).
- **Critical parts by hand** (2025). The practice in which the developer writes the critical and complex parts of the code and hands the rest to the agent.
  Sources: [Anton Zhiyanov, 2025-09-26](https://antonz.org/write-code/#:~:text=Write%20the%20critical%20parts%20and%20ask%20AI%20to%20do%20the%20rest); [Saffron Huang, Bryan Seethor, Esin Durmus, Kunal Handa, Miles McCain, Michael Stern, Deep Ganguli, 2025-12-02](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic).
- **Own draft first** (2025). The practice in which the developer drafts the solution without an agent and then gives it to an agent to review and improve.
  Sources: [Alberto Fortin](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20subconsciously%20defaulting%20to%20AI); [Anton Zhiyanov, 2025-09-26](https://antonz.org/write-code/#:~:text=Write%20the%20initial%20version%20yourself%20and%20ask%20AI%20to%20review%20and%20improve%20it); [Mitchell Hashimoto, 2025-10-11](https://mitchellh.com/writing/non-trivial-vibing#:~:text=So%20I%20pulled%20out%20my%20AI%20tooling).
- **Agent as a pair partner** (2025). The practice in which the developer explains a problem to the agent, gets its feedback and works out the solution together with it.
  Sources: [Orta Therox, 2025-06-07](https://blog.puzzmo.com/posts/2025/06/07/orta-on-claude/#:~:text=Claude%20Code%20feels%20like%20pairing).
  Grew from: Pair programming, Rubber duck debugging.
- **Delegation of routine tasks** (2025). The practice in which systematic and time-consuming tasks, from renames to large migrations, are handed to the agent.
  Sources: [Alberto Fortin, 2025-05-15](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20using%20LLMs,%20but%20for%20dumber%20things); [Colton, 2025-08-05](https://colton.dev/blog/curing-your-ai-10x-engineer-imposter-syndrome/#:~:text=AI's%20best%20use%20case%20for%20me).
  Grew from: Codemods.
- **Repeated rework requests** (2025). The practice in which the developer asks the agent to rework the code as many times as it takes to reach an acceptable result.
  Sources: [Simon Willison, 2025-03-11](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=If%20I%20don't%20like%20what%20an%20LLM%20has%20written).

## Teams and projects

Rules that engineering teams and open-source projects set for work done with agents: how agent-written changes are disclosed and reviewed, who may let an agent act in shared spaces, who owns the shared agent setup, and how hiring interviews change.

- **Ownership of agent controls** (2026). The practice in which shared agent controls used by many teams, such as skills, commands and root-level instruction files, have an owning team or guild that watches monitoring data and updates them.
  Sources: [Addie Beach, Rui Martins Lacerda, 2026-09-09](https://www.datadoghq.com/blog/ai-development-golden-paths/).
- **Analyze, not create** (2026). The practice in which a project lets contributors use language models to answer questions, analyze, check and review their work, but not to create the content they submit.
  Sources: [Jynn Nelson, 2026-08-05](https://blog.rust-lang.org/inside-rust/2026/08/05/rust-langrust-is-adopting-an-llm-policy/).
- **Build session in the interview** (2026). The practice in which an interview gives the candidate a few hours to build a working prototype with coding agents and tools of their choice.
  Sources: [Applied Intuition, 2026-07-22](https://www.appliedintuition.com/engineering-blog/hiring-engineers-age-of-agents); [DigitalOcean, 2026-06-09](https://digitalocean.com/blog/ai-native-engineering-interview).
- **Review of a draft change in the interview** (2026). The practice in which a candidate reviews and improves a colleague's draft pull request in an unfamiliar codebase, with agents allowed.
  Sources: [Sierra, 2026-04-22](https://sierra.ai/blog/the-ai-native-interview).
- **Candidate's own agents in the interview** (2026). The practice in which a candidate may use their own coding agents and tools during an interview, the same ones they would use at work.
  Sources: [Elicit, 2026-03-30](https://elicit.com/blog/engineering-interviews-in-the-era-of-agents); [Omnea, 2026-05-26](https://www.omnea.co/resource/ai-in-our-programming-interviews).
- **Interviews without agents** (2026). The practice in which some interviews are deliberately held without agents, next to interviews where agents are expected.
  Sources: [Elicit, 2026-03-30](https://elicit.com/blog/engineering-interviews-in-the-era-of-agents).
- **Assessing how a candidate directs agents** (2026). The practice in which interviewers score how a candidate plans the work, steers the agent and checks what it produced.
  Sources: [Elicit, 2026-03-30](https://elicit.com/blog/engineering-interviews-in-the-era-of-agents); [Augment Code, 2026-03-12](https://augmentcode.com/blog/how-we-hire-ai-native-engineers-now).
- **Agent review of every pull request** (2026). The practice in which a team has an agent review every pull request, and review by a person becomes optional.
  Sources: [Ryan Lopopolo, 2026-02-11](https://openai.com/index/harness-engineering/); [OpenAI](https://developers.openai.com/codex/learn/best-practices).
- **Disclosure of agent use** (2025). The practice in which contributors state in the pull request, commit message or post whether and how a model or agent produced the content.
  Sources: [rnk, 2025-12-17](https://discourse.llvm.org/t/rfc-llvm-ai-tool-policy-human-in-the-loop/89159); [Jynn Nelson, 2026-08-05](https://blog.rust-lang.org/inside-rust/2026/08/05/rust-langrust-is-adopting-an-llm-policy/).
- **Contributor review of generated code** (2025). The practice in which a project requires contributors to read and review all generated code or text, and to be able to explain it, before they ask maintainers for review.
  Sources: [rnk, 2025-12-17](https://discourse.llvm.org/t/rfc-llvm-ai-tool-policy-human-in-the-loop/89159); [Jynn Nelson, 2026-08-05](https://blog.rust-lang.org/inside-rust/2026/08/05/rust-langrust-is-adopting-an-llm-policy/).
- **Own words in project communication** (2025). The practice in which a project requires issues, pull request descriptions, comments and replies to review to be written in the contributor's own words, not pasted model output.
  Sources: [rnk, 2025-12-17](https://discourse.llvm.org/t/rfc-llvm-ai-tool-policy-human-in-the-loop/89159); [Jellyfin project](https://jellyfin.org/docs/general/contributing/llm-policies/).
- **Agents in project spaces only with approval** (2025). The practice in which an agent may comment on or act in shared project spaces only after people approve it or explicitly invoke it.
  Sources: [rnk, 2025-12-17](https://discourse.llvm.org/t/rfc-llvm-ai-tool-policy-human-in-the-loop/89159); [Wirasm](https://github.com/Wirasm/prp).
- **Extractive contribution handling** (2025). The practice in which maintainers who judge a generated contribution to cost more review time than it is worth reply with a standard request, label it, and stop engaging or close it.
  Sources: [rnk, 2025-12-17](https://discourse.llvm.org/t/rfc-llvm-ai-tool-policy-human-in-the-loop/89159); [Jynn Nelson, 2026-08-05](https://blog.rust-lang.org/inside-rust/2026/08/05/rust-langrust-is-adopting-an-llm-policy/).
- **Extra approval for agent pull requests** (2025). The practice in which pull requests started by an agent or generated by a model must clear a higher bar than other pull requests, such as more human approvals or required tests.
  Sources: [Shrivu Shankar, 2025-11-02](https://blog.sshh.io/p/how-i-use-every-claude-code-feature); [Jynn Nelson, 2026-08-05](https://blog.rust-lang.org/inside-rust/2026/08/05/rust-langrust-is-adopting-an-llm-policy/).
- **Ban on generated contributions**. The practice in which a project does not accept contributions that include content generated, in part or in full, by language models or similar systems.
  Sources: [OpenJDK Governing Board](https://openjdk.org/legal/ai).
- **Agent questions in incident retrospectives**. The practice in which a team's regular incident retrospective adds two questions: whether agent-written code contributed to the incident, and whether the larger volume of change strained review, testing, rollout or observability.
  Sources: [Tyson Singer](https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity/).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Changes go into `data/entries.json`; then run `python3 scripts/build_readme.py`.
