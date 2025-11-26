**Available Languages:** [English](README.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Français](README-fr.md) | 日本語 | [Português](README-pt.md)

---

> **Active Development** - Updated November 26, 2025

> [coding-with-ai.dev](https://coding-with-ai.dev)

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

### メモリファイルを設定する

プロジェクトの構造、標準、設定を永続的にガイドするコンテキストファイルを作成します。

**Community adoption**: 81% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-contextual-documentation) (n=85)

> "Think of AGENTS.md as a 'README for agents': a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project."
> — [agents.md community](https://agents.md/#:~:text=Think%20of%20AGENTS.md%20as%20a%20README%20for%20agents)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

**新規プロジェクトの場合:**
プロジェクトルートで`/init`を実行すると、スターター`CLAUDE.md`が作成されます。

**既存のコードベースの場合:**
`/init`を実行すると、Claudeがプロジェクト構造、依存関係、設定ファイルを分析し、コードベースで効果的に作業するために必要な情報を自動的に生成します。

Claudeが検査する内容:
• `package.json` - ビルドスクリプト、依存関係、プロジェクトメタデータ
• 設定ファイル - `.eslintrc`、`vite.config.js`、`tsconfig.json`
• プロジェクト構造 - コンポーネントパターン、フォルダ構成
• ドキュメント - `README.md`、既存のルールファイル

生成されるCLAUDE.mdの内容:
• **必須コマンド** - `npm run dev`、`npm test`、`npm run build`
• **技術スタック** - 特定されたフレームワーク、ライブラリ、ツール
• **アーキテクチャ概要** - コンポーネントパターン、状態管理、ルーティング
• **主要な規約** - コードスタイル、ファイル構成、テストアプローチ
• **よくある落とし穴** - ビルドの問題、設定の癖、ワークフローのメモ

**メモリファイルの階層:**
• `~/.claude/CLAUDE.md` - あなた個人のコーディング設定（グローバル）
• `./CLAUDE.md` - プロジェクトチームの標準（プロジェクト固有）

**クイック編集:**
• `/memory` - 完全なエディタインターフェース
• `#` - メモを追加するためのクイックショートカット

**プロのヒント:**
• 生成されたコンテンツをプロジェクトの特定のニーズに合わせてレビューとカスタマイズを行う
• 発見した落とし穴を追加: 「/generated/のファイルは絶対に編集しない」、「設定変更後は必ず再起動」
• プロジェクトドキュメントへのリンク: `@docs/deployment.md`、`@architecture.md`
• 反復的に改善 - Claudeに同じ指示を繰り返していることに気付いたら、CLAUDE.mdに追加する
• CLAUDE.mdをバージョン管理にコミットしてチームと共有する

</details>

<details>
<summary><strong>Cursor</strong></summary>

**プロジェクトルートに`AGENTS.md`を作成:**
Cursorはこのファイル（レガシーの`.cursorrules`もサポート）を読み込み、一貫したプロジェクトガイダンスを提供します。

**AGENTS.mdファイルに含めるべき内容:**
• **必須コマンド** - `npm run dev`、`npm test`、`npm run build`
• **技術スタック** - プロジェクト内のフレームワーク、ライブラリ、ツール
• **コードスタイルガイドライン** - 命名規則、推奨パターン
• **アーキテクチャ概要** - コンポーネント構造、APIルート、ファイル構成
• **よくある落とし穴** - ビルドの問題、ワークフロー要件、制約

**リアルタイムコンテキスト（@メンション）:**
• **@codebase** - プロジェクト全体から関連ファイルを自動的に取り込む
• **@docs** - プロジェクトドキュメントを参照
• **@git** - 最近の変更内容を理解
• **@web** - インターネットから最新のパターンと例を取得

**プロジェクトルールの階層:**
• `.cursor/rules`ディレクトリのグローバルルール
• `AGENTS.md`のプロジェクト固有ルール
• gitignoreスタイルのマッチングによるパス固有ルール

**プロのヒント:**
• 静的ルール（AGENTS.md）と動的コンテキスト（@メンション）を組み合わせる
• Cursorにプロジェクト全体のコンテキストを理解させたい場合は@codebaseを使用
• AGENTS.mdはプロジェクト固有の規約と落とし穴に焦点を当てる
• コード理解の重い作業は@メンションに任せる

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

**プロジェクトルートに`AGENTS.md`を作成:**
Codexはセッション開始時にこのファイルを自動的に読み込みます。

**AGENTS.mdファイルに含めるべき内容:**
• **必須コマンド** - `npm run dev`、`npm test`、`npm run build`
• **技術スタック** - プロジェクト内のフレームワーク、ライブラリ、ツール
• **コードスタイルガイドライン** - 命名規則、推奨パターン
• **アーキテクチャメモ** - コンポーネント構造、ファイル構成
• **セキュリティルール** - 環境変数、入力検証要件
• **プロジェクトの落とし穴** - よくあるミス、ビルドの癖、ワークフローメモ

**モノレポのサポート:**
• 各パッケージディレクトリに`AGENTS.md`を配置
• Codexは作業ディレクトリに最も近いものを使用
• パッケージ固有のガイダンスを自動的に取得

**ビジュアルコンテキスト（Codexのユニークな強み）:**
• スクリーンショットをチャットに直接ドラッグ＆ドロップ
• UIモックアップやデザインファイルを含める
• アーキテクチャ図やフローチャートを共有
• デザインの実装や複雑なシステムの説明に最適

**プロのヒント:**
• プロジェクトの進化に合わせてAGENTS.mdを更新し続ける
• 避けたいよくあるミスを追加: 「/generated/のファイルは絶対に編集しない」
• ビルド依存関係とセットアップ要件を含める
• 特別なデプロイやテスト手順をドキュメント化する

</details>

### まず計画を依頼する

コードに触れる前に、ステップ、リスク、簡単なテストの概要を説明するようアシスタントに指示し、アプローチを確認して調整できるようにします。

> "If you want to iterate on the plan, it helps to explicitly include instructions in the prompt to not proceed with implementation until the plan has been accepted by the user."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=If%20you%20want%20to%20iterate%20on%20the%20plan)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

`Shift+Tab`を押してプランモードに入ると、読み取りとドラフト作成のみを行います。共有プランニングプロンプトを使用し、適切に見えるまで反復し、実装を承認したらプランモードを終了します。

</details>

<details>
<summary><strong>Cursor</strong></summary>

Cursorのプラントグルをクリックすると、反復中は読み取り専用のままになります。ステップ、影響を受けるファイル、リスク、クイックテストをリストアップさせ、実装を承認したらプランモードを終了して差分を開きます。

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Codexに計画と実装を分けるよう注意します：ステップ、リスク、クイックテストをリストアップし、レビューのために一時停止し、承認後に実装させて差分を検査します。

</details>

### 高容量モデルで計画する

要件を収集したり仕様を作成したりするときは、一時的により高性能なモデルまたは拡張推論モードに切り替えて、コーディング前に読み取り、合成、計画を提案できるようにします。

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

`/model`を実行し、要件をスコープするときに`opus`（または別の高ティア）を選択すると、深く推論できます。編集を承認するまで読み取り専用にしたい場合はプランモードを使用します。

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

`/model`を実行し、Codexのコーディングバイアスが役立つ仕様作業には`gpt-5-codex high`を選択するか、より広範な推論が必要な場合は`gpt-5 high`を選択します。計画が承認されたら通常のティアに戻ります。

</details>

### 仕様駆動開発：動作するまで反復する

アシスタントが動作するコードを生成するまでMarkdownで仕様を反復します - 直接コードを書くのではなく、仕様を真実の源として扱います。

> "The workflow involves iterating on specifications in Markdown files, asking AI to compile into code, running/testing the app, and updating the spec if something doesn't work as expected. Developers should treat specifications as living documents, constantly updating and refining them to guide AI code generation with increasing precision."
> — [GitHub Engineering](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-using-markdown-as-a-programming-language-when-building-with-ai/)

### 退屈で安定したライブラリを選ぶ

モデルのトレーニングカットオフ日より前に存在していた、優れた安定性を持つ確立されたライブラリを意図的に選択して、LLM支援のコード生成を向上させます。

**Community adoption**: 64% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-choose-boring-stable-libraries) (n=43)

> "I gain enough value from LLMs that I now deliberately consider this when picking a library—I try to stick with libraries with good stability and that are popular enough that many examples of them will have made it into the training data. I like applying the principles of boring technology—innovate on your project's unique selling points, stick with tried and tested solutions for everything else."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20gain%20enough%20value%20from%20LLMs)

### 詳細な仕様を書く

包括的な仕様を提供します - 会話形式の仕様でさえ、曖昧な指示を上回ります。

**Community adoption**: 50% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-specification-driven-development) (n=61)

> "Here's a recent example: `Write a Python function that uses asyncio httpx with this signature:` `async def download_db(url, max_size_bytes=5 * 1025 * 1025): -> pathlib.Path`. Given a URL, this downloads the database to a temp directory and returns a path to it. BUT it checks the content length header at the start of streaming back that data and, if it's more than the limit, raises an error... I find LLMs respond extremely well to function signatures like the one I use here."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=Here's%20a%20recent%20example)

### 複数のオプションを取得する

LLMに賛否両論を含むいくつかのアプローチを提示させて、最適なオプションを選択できるようにします。

**Community adoption**: 57% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-ai-technology-exploration) (n=51)

> "I'll use prompts like `what are options for HTTP libraries in Rust? Include usage examples`"
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I'll%20use%20prompts%20like)

### 読む → 計画 → コード → コミット

コードを探索させ、計画を立て、実装し、コミットさせます。

**Community adoption**: 53% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-explore-plan-code-commit) (n=84)

> "There's a process that I call 'priming' the agent, where instead of having the agent jump straight to performing a task, I have it read additional context upfront to increase the chances that it will produce good outputs."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=There's%20a%20process%20that%20I%20call)

### 脳が最初、アシスタントは次

まず自分で解決策を下書きし、次にアシスタントを使って洗練します。

**Community adoption**: 39% didn't adopt • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-brain-first-coding) (n=59)

> "I'm subconsciously defaulting to AI for all things coding. I've been using pen and paper less. As soon as I need to plan a new feature, my first thought is asking o4-mini-high how to do it, instead of my neurons. I hate this. And I'm changing it."
> — [Alberto Fortin](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20subconsciously%20defaulting%20to%20AI)

## UI & Prototyping

### まずプロトタイプを構築する

すべてのプロジェクトを、機能することを証明するための迅速に生成されたプロトタイプから始めます。

**Community adoption**: 44% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-prototype-first-development) (n=34)

> "The best way to start any project is with a prototype that proves that the key requirements of that project can be met. I often find that an LLM can get me to that working prototype within a few minutes of me sitting down with my laptop—or sometimes even while working on my phone."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=The%20best%20way%20to%20start%20any%20project)

### スクリーンショットを見せる

スクリーンショットを入れて反復します - 結果のスクリーンショットを撮り、比較し、繰り返します。

**Community adoption**: 38% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-visual-iteration-technique) (n=29)

> "Give Claude a visual mock by copying / pasting or drag-dropping an image... take screenshots of the result, and iterate until its result matches the mock."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Give%20Claude%20a%20visual%20mock)

### ASCIIワイヤーフレームを依頼する

レイアウトを洗練するときは、アシスタントにASCIIワイヤーフレームをスケッチさせて、CSSに触れる前に階層と間隔を評価できるようにします。

### もっと美しくする

UIを`もっと美しく`または`もっとエレガントに`するように頼むだけで - 機能します。

**Community adoption**: 21% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-iterative-ui-refinement) (n=33)

> "If Claude doesn't produce a well-designed UI the first time, you can just tell it to `make it more beautiful/elegant/usable`."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=If%20Claude%20doesn't%20produce)

### バイブコーディング

従来のコーディングの代わりに会話を通じてプロジェクトを構築します - 話し、変更を受け入れ、動作するまで反復します。

**Community adoption**: 30% didn't adopt • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-experimental-vibe-coding) (n=47)

> "...I ask for the dumbest things like `decrease the padding on the sidebar by half` because I'm too lazy to find it. I `Accept All` always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment, usually that fixes it. The code grows beyond my usual comprehension, I'd have to really read through it for a while. Sometimes the LLMs can't fix a bug so I just work around it or ask for random changes until it goes away. It's not too bad for throwaway weekend projects, but still quite amusing. I'm building a project or webapp, but it's not really coding—I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works."
> — [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383)

## Coding

### 重要な部分を扱い、残りを委任する

コードの重要で複雑な部分は自分で書き、残りの単純な実装をアシスタントに委任します。

> "Write the critical parts and ask AI to do the rest."
> — [Anton Zhiyanov](https://antonz.org/write-code/#:~:text=Write%20the%20critical%20parts%20and%20ask%20AI%20to%20do%20the%20rest)

### 退屈なタスクをオフロードする

退屈で、体系的で、時間のかかるタスクをアシスタントに委任します - 小さな変数の名前変更から、深いアーキテクチャ思考を必要としない大きな移行まで。

**Community adoption**: 64% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-offload-tedious-tasks) (n=22)

> "I'm using LLMs, but for dumber things: `rename all occurrences of this parameter`"
> — [Alberto Fortin](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20using%20LLMs,%20but%20for%20dumber%20things)

### コーディング前に理解を確認する

実装を開始する前に、ツールにタスクの理解を明示的に確認させて、整合性を確保し、期待のずれを減らします。

### アシスタントをデジタルインターンとして扱う

アシスタントに、インターンに対するように、極めて正確で詳細な指示を与えます - 正確な関数シグネチャを提供し、実装を扱わせます。

**Community adoption**: 60% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-treat-ai-as-intern) (n=20)

> "Once I've completed the initial research I change modes dramatically. For production code my LLM usage is much more authoritarian: I treat it like a digital intern, hired to type code for me based on my detailed instructions."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20treat%20it%20like%20a%20digital%20intern)

### コードを非常にシンプルに保つ

明確な関数名を持つわかりやすいコードを書き、継承や巧妙なハックを避けます - シンプルなコードはアシスタントでより良く機能します。

**Community adoption**: 40% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-keep-code-dead-simple) (n=20)

> "Simple code significantly outperforms complex code in agentic contexts. I just recently wrote about ugly code and I think in the context of agents this is worth re-reading. Have the agent do `the dumbest possible thing that will work`."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Simple%20code%20significantly%20outperforms%20complex%20code)

### 既存のコードでプライミングする

既存のコードをチャットに投入してコンテキストをシードし、そこから変更します。

**Community adoption**: 36% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-context-priming) (n=31)

> "I often start a new chat by dumping in existing code to seed that context, then work with the LLM to modify it in some way."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20often%20start%20a%20new%20chat)

### 構造を定義し、実装を委任する

構造 - 関数シグネチャ、コードのアウトライン、または足場を提供し、アシスタントに実装の詳細を埋めさせます。

**Community adoption**: 35% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-precise-function-specification) (n=23)

> "I find LLMs respond extremely well to function signatures like the one I use here. I get to act as the function designer, the LLM does the work of building the body to my specification. I'll often follow-up with `Now write me the tests using pytest`. Again, I dictate my technology of choice—I want the LLM to save me the time of having to type out the code that's sitting in my head already."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20find%20LLMs%20respond%20extremely%20well)

### 新しいライブラリのコンテキストを提供する

モデルのトレーニングデータ外のライブラリを使用する場合は、最近の例とドキュメントを提供して、ライブラリの動作を教えます。

**Community adoption**: 35% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-providing-context-for-unfamiliar-apis) (n=20)

> "LLMs can still help you work with libraries that exist outside their training data, but you need to put in more work—you'll need to feed them recent examples of how those libraries should be used as part of your prompt."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=LLMs%20can%20still%20help%20you%20work%20with%20libraries)

### コードを生成し、依存関係は生成しない

アシスタントと作業するときは、より多くのライブラリを導入するのではなく、カスタムコードを記述します。

**Community adoption**: 27% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-conservative-dependency-management) (n=30)

> "Be even more conservative about upgrades than before... I strongly prefer more code generation over using more dependencies."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Be%20even%20more%20conservative%20about)

## Debugging

### アシスタントが苦労したら方向転換する

アシスタントが特定の問題を繰り返し解決できない場合は、同じ解決策を続けるのではなく、代替アプローチに方向転換します。

> "It's at this point that I know I need to step back, review what it did, and come up with my own plans. It's time to educate myself and think critically. AI is no longer the solution; it is a liability."
> — [Mitchell Hashimoto](https://mitchellh.com/writing/non-trivial-vibing#:~:text=It's%20at%20this%20point)

### アシスタントデバッグのためにすべてをログに記録する

包括的なログ記録を備えたシステムを設計して、エージェントがログを読んで何が起こっているかを理解し、問題を自己診断できるようにします。

**Community adoption**: 35% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-log-everything-for-debugging) (n=17)

> "In general logging is super important. For instance my app currently has a sign in and register flow that sends an email to the user. In debug mode (which the agent runs in), the email is just logged to stdout. This is crucial! It allows the agent to complete a full sign-in with a remote controlled browser without extra assistance. It knows that emails are being logged thanks to a CLAUDE.md instruction and it automatically consults the log for the necessary link to click."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=In%20general%20logging%20is%20super%20important)

### テストして自分で修正させる

変更を加え、テストを実行し、失敗したものを確認し、自分で再試行するツールを設定します。

**Community adoption**: 27% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-ai-feedback-loops) (n=22)

> "Claude is most useful when it's capable of independently driving feedback loops that allow it to make a change, test the change, and gather context on what failed to try another iteration."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=Claude%20is%20most%20useful%20when)

### サブエージェントを使用してダブルチェックする

詳細を確認したり、特定の質問を調査したりするためにサブエージェントを生成します。

**Community adoption**: 22% didn't adopt • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-subagent-verification) (n=23)

> "Telling Claude to use subagents to verify details or investigate particular questions it might have, especially early on in a conversation or task, tends to preserve context availability without much downside in terms of lost efficiency."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Telling%20Claude%20to%20use%20subagents)

## Testing & QA

### 常に自分でコードをテストする

テストを絶対にアウトソーシングすることはできません - コードが実際に機能することを常に検証してください。

**Community adoption**: 67% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-comprehensive-testing-mandate) (n=27)

> "The one thing you absolutely cannot outsource to the machine is testing that the code actually works. Your responsibility as a software developer is to deliver working systems. If you haven't seen it run, it's not a working system. You need to invest in strengthening those manual QA habits."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=The%20one%20thing%20you%20absolutely%20cannot%20outsource)

### 最初にテストを書く

最初にテストを書き、失敗することを確認してから、合格するまで実装します。

**Community adoption**: 19% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-test-driven-development-ai) (n=21)

> "Write test first (red), Implement - Minimal code to pass (green), Refactor - Clean up with tests passing"
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Test-driven%20when%20possible)

## Review & Refactoring

### アシスタント出力を自分で反復する

アシスタントが作業を完了した後、そのまま受け入れるのではなく、手動で反復し実装を洗練させます。

> "I almost always go in after an AI does work and iterate myself for awhile, too."
> — [Mitchell Hashimoto](https://mitchellh.com/writing/non-trivial-vibing#:~:text=I%20almost%20always%20go%20in)

### AIコードをプルリクエストとして扱う

AI生成コードを同僚のプルリクエストのようにレビューし、自分で直接編集するのではなく、アシスタントが対処するための反復的なフィードバックコメントを提供します。

> "treating the generated code as a Merge Request on which you submit comment for correction"
> — [HN Discussion](https://news.ycombinator.com/item?id=45415232)

### エージェントに自分のコードをレビューさせる

人間のレビューの前に、アシスタントに自分の作業のコードレビューを実行させて、問題と改善を明らかにします。

> "Asking the agent to perform a code review on its own work is surprisingly fruitful."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Asking%20the%20agent%20to%20perform%20a%20code%20review)

### 実際にコードを読む

立ち止まって、書かれたものを実際に検査してください - 驚くかもしれません。

**Community adoption**: 63% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-critical-code-review-strategy) (n=19)

> "Asking the agent to perform a code review on its own work is surprisingly fruitful. AI-generated code is often incorrect or inefficient. It's important for me to call out that I believe I'm ultimately responsible for the code that goes into a PR with my name on it, regardless of how it was produced. Therefore, especially in any professional context, I manually review all AI-written code and test cases."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Asking%20the%20agent%20to%20perform%20a%20code%20review)

### 常に完全な差分をレビューする

バイブコーディングは意図しない副作用を引き起こす可能性があります - アシスタントが要求以上のものを変更する可能性があるため、常に差分を注意深くレビューしてください。

**Community adoption**: 56% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-check-for-unintended-changes) (n=16)

> "I believe I'm ultimately responsible for the code that goes into a PR with my name on it, regardless of how it was produced. Therefore, especially in any professional context, I manually review all AI-written code and test cases."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/Getting-Good-Results-from-Claude-Code.html#:~:text=I%20believe%20I'm%20ultimately%20responsible,manually%20review%20all%20AI-written%20code)

### 変更を求め続ける

人間とは異なり、アシスタントは決してイライラしません - 満足するまでリファクタリングを求め続けてください。

**Community adoption**: 47% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-conversational-code-refinement) (n=17)

> "If I don't like what an LLM has written, they'll never complain at being told to refactor it! `Break that repetitive code out into a function`, `use string manipulation methods rather than a regular expression`, or even `write that better!`—the code an LLM produces first time is rarely the final implementation, but they can re-type it dozens of times for you without ever getting frustrated or bored."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=If%20I%20don't%20like%20what%20an%20LLM%20has%20written)

### 差分でコードを編集する

差分ビューで変更をレビューし、コミットする前に差分に直接修正を入力します。

**Community adoption**: 27% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-diff-based-iterative-refinement) (n=15)

> "I manually review all AI-written code and test cases. I'll add test cases for anything I think is missing or needs improvement, either manually or by asking the LLM to write those cases (which I then review)."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=I%20manually%20review%20all)

### 1つが書き、別の1つがレビューする

1つのエージェントにコードを書かせ、次に新しいエージェントを使ってレビューし、問題を見つけます。

**Community adoption**: 31% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-multi-agent-verification) (n=16)

> "Use Claude to write code. Run `/clear` or start a second Claude in another terminal. Have the second Claude review the first Claude's work. Start another Claude (or `/clear` again) to read both the code and review feedback. Have this Claude edit the code based on the feedback. This separation often yields better results than having a single Claude handle everything."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Have%20one%20Claude%20write%20code)

## Cross-Stage Techniques

### アシスタント出力スタイルを切り替える

現在の目標に合わせてアシスタント出力スタイルを選択します。

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

**スタイルを素早く切り替え**
`/output-style`を実行してピッカーを開くか、`/output-style learning`で学習モードに直接ジャンプします。選択は`.claude/settings.local.json`でプロジェクトごとに保存されます。

**自己学習モード**
デフォルトは出荷に集中し続け、`explanatory`はインサイトコールアウトを挿入し、`learning`は`TODO(human)`マーカーを追加するため、重要な部分を自分で埋めることができます。

**カスタムスタイルを作成**
`/output-style:new I want ...`を実行して`~/.claude/output-styles`にマークダウンファイルをスキャフォールドします。フロントマターと指示を調整します。プロジェクト固有のバリアントは`.claude/output-styles/`に配置されます。

**スタイルが異なる理由**
スタイルはClaude Codeのデフォルトシステムプロンプトを置き換えます。`CLAUDE.md`（ユーザーメッセージ）や`--append-system-prompt`（追加）とは異なります。

</details>

### タスク間でコンテキストをクリアする

関連のないタスク間でアシスタントのコンテキストウィンドウをリセットして、混乱を防ぎ、新しい問題でのパフォーマンスを向上させます。

**Community adoption**: 67% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-clear-context-between-tasks) (n=15)

> "During long sessions, Claude's context window can fill with irrelevant conversation, file contents, and commands. This can reduce performance and sometimes distract Claude. Use the `/clear` command frequently between tasks to reset the context window."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=During%20long%20sessions%2C%20Claude's%20context)

### 会話スタイルでツールを選ぶ

人間のような協力か、構造化されたロボットのような効率のどちらを好むかでコーディングアシスタントを選択します - 会話の個性が生産性と楽しさに大きく影響します。

> "In terms of personality, it's the opposite for me: Claude Code feels like my pair-programming partner, while Codex feels like a robot (very structured but not very human in its conversational style).

Problem is after a while, the 'You are absolutely right!' kinda gets on my nerves.

Codex is dry. You can insult it and it doesn't even answer. No personality. Claude is like, a friend who admits messing up. I spend like close to 10 hours a day coding between CC and Codex CLI and I see huge differences in personality and creativity. I like Claude better for that. Much more creative.

Codex is monotone straight to the point, but most importantly the reason why it is better is because it's not agreeable at all. It will challenge you when you're suggesting something wrong and stay with its opinion."
> — [Reddit Community](https://www.reddit.com/r/ClaudeAI/comments/1nk4v4k/comment/nev86ot)

### タスクに適したモデルを選択する

新しいタスクを開始する前に、2つのレバーを選択してください：適切なモデル（モダリティ、コンテキスト長、ツール呼び出しの信頼性、レイテンシ、コスト）と適切な推論レベル（思考トークンを多く/少なく割り当てる）— 盲目的にデフォルトにしないでください。

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

タスク開始時の2つのレバー:
1. `/model` - 通常の編集には`fast`、マルチファイルや長いドキュメントには`long-context`、UI/スクリーンショットには`vision-strong`を選択
2. 推論レベル - 複雑なデバッグ、アーキテクチャ作業、曖昧な仕様には拡張思考を有効にして、アシスタントがより多くの推論トークンを割り当てられるようにする

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

クイック編集には`gpt-5-minimal`/`gpt-5-low`から始め、複雑さが増したら高推論バリアント`gpt-5-high`/`gpt-5-medium`を選択します。

</details>

### メモリファイルを一元化する

1つの正規の指示ドキュメントを保持し、他のすべてのエージェントファイルを、目立つポインター行、シンボリックリンク、または@fileインクルードでそれにルーティングして、ツール間のガイダンスが一貫性を保つようにします。

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

`CLAUDE.md`を信頼できる情報源として保持し、次の3つの方法のいずれかを使用します。

1. `AGENTS.md`に`@CLAUDE.md`を入れる。

2. `ln -sf CLAUDE.md AGENTS.md`で`AGENTS.md`を`CLAUDE.md`にシンボリックリンクして、両方のツールが同じファイルを共有するようにする。

3. `AGENTS.md`を1行のみにする：`READ CLAUDE.md FIRST!!!`。

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Codex側から同じ3つの方法を使用します。

1. Codexがプライマリテキストを保持している場合、`AGENTS.md`を完全に残し、`CLAUDE.md`内に`@AGENTS.md`を配置して、両方のツールが同じドキュメントに到達するようにする。

2. `ln -sf CLAUDE.md AGENTS.md`を実行して、Codexが読み取るファイルが`CLAUDE.md`へのシンボリックリンクになるようにする。

3. `CLAUDE.md`が正規の場合、`AGENTS.md`を1行のみにする：`READ CLAUDE.md FIRST!!!`。

</details>

### 頻繁に中断してリダイレクトする

アシスタントが間違った道を進みすぎないようにします - 問題に気付いたらすぐに中断し、フィードバックを提供して、リダイレクトします。

**Community adoption**: 60% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-interrupt-and-redirect-often) (n=15)

> "Press Escape to interrupt Claude during any phase (thinking, tool calls, file edits), preserving context so you can redirect or expand instructions. Double-tap Escape to jump back in history, edit a previous prompt, and explore a different direction. You can edit the prompt and repeat until you get the result you're looking for."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Press%20Escape%20to%20interrupt%20Claude)

### エージェントをコーディングパートナーとして使う

コーディングパートナーとして協力します - 問題を説明し、フィードバックを得て、解決策に一緒に取り組みます。

**Community adoption**: 63% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-ai-coding-partner) (n=16)

> "Claude Code feels like pairing with someone with a few years under their belt who just needs the occasional nudge. Then like with pairing, it's review, refactor and test time because it's still your name on the git commit."
> — [Orta Therox](https://blog.puzzmo.com/posts/2025/06/07/orta-on-claude/#:~:text=Claude%20Code%20feels%20like%20pairing)

### それから学び、自分でコードを書く

アシスタントを使って新しい言語や概念を学び、コーディング時にその知識を適用します。

**Community adoption**: 43% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-learning-oriented-ai-interaction) (n=14)

> "I'm leveraging them to learn Go, to upskill myself. And then I apply this new knowledge when I code."
> — [Alberto Fortin](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20leveraging%20them%20to%20learn%20Go)

### プロンプトで強い強調を使用する

プロンプトでIMPORTANT、NEVER、ALWAYSを自由に使用して、一般的なミスからモデルを遠ざけます - これは今でも最も効果的なアプローチです。

**Community adoption**: 50% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-use-strong-emphasis-words) (n=14)

> "Unfortunately CC is no better when it comes to asking the model to not do something. IMPORTANT, VERY IMPORTANT, NEVER and ALWAYS seem to be the best way to steer the model away from landmines. I expect the models to get more steerable in the future and avoid this ugliness. But for now, CC uses this liberally, and so should you."
> — [Vivek (MinusX AI Team)](https://minusx.ai/blog/decoding-claude-code/#:~:text=Unfortunately%20CC%20is%20no%20better)

### 高速で確実なツールを構築する

迅速に応答し、明確なエラーメッセージを提供し、エージェントによる誤用から保護するツールを作成します。

**Community adoption**: 17% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-build-fast-foolproof-tools) (n=12)

> "Tools need to be fast. The quicker they respond (and the less useless output they produce) the better. Crashes are tolerable; hangs are problematic. Tools need to be user friendly! Tools must clearly inform agents of misuse or errors to ensure forward progress. Tools need to be protected against an LLM chaos monkey using them completely wrong. There is no such thing as user error or undefined behavior!"
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Tools%20need%20to%20be%20fast)

### 複数のエージェントを並列実行する

あるエージェントが終了するのを待ってから別のエージェントを開始するのをやめましょう - 別々の機能で複数のエージェントを並列実行し、競合や混乱がないようにします。

**Community adoption**: 14% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-run-multiple-agents-parallel) (n=14)

> "We are exploring solving both of these issues in sketch.dev using containers. By default sketch creates a little development environment in a container with a copy of the source code and the runner has the ability to extract git commits from the container. This lets you run many simultaneously."
> — [David Crawshaw](https://crawshaw.io/blog/programming-with-agents#:~:text=We%20are%20exploring%20solving%20both%20of%20these%20issues)

### 簡単なタスクには権限なしで実行する

とにかくすべての変更を受け入れるほど簡単なタスクの場合は、自律モードを有効にします - 監視をスキップします。

> "I disable all permission checks. Which basically means I run `claude --dangerously-skip-permissions`. More specifically I have an alias called claude-yolo set up."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=I%20disable%20all%20permission%20checks)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

`claude --dangerously-skip-permissions`を実行すると、Claudeが権限プロンプトなしで中断なく実行されるYOLOモードが有効になります。

**セッション中に切り替え:** `/permissions`を使用して、再起動せずにセッション途中でツール権限を管理します。特定のツールに対して許可ルールを設定し、承認プロンプトをスキップします。

**使用するタイミング:**
• 複数ファイルにわたるlintエラーの修正
• シンプルなリファクタリングと変数の名前変更
• 日常的なコード更新と移行
• とにかくすべての変更を受け入れそうなタスク

**安全性の考慮事項:**
• 隔離のためにコンテナやVMで使用するのがベスト
• 重要な本番システムでは避ける
• 一括権限ではなく`allowedTools`設定を使用して詳細な制御を検討する

**エイリアスの設定:** 多くのユーザーは`alias cc='claude --dangerously-skip-permissions'`を作成してクイックアクセスしています。

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

`codex --full-auto`で完全自律モードを有効にするか、セッション内`/mode`コマンドを使用します。

**セッション中に切り替え:** `/mode`を使用してセッションコンテキストを失わずに権限レベル間をホットスワップします。suggest/auto-edit/full-autoモードから矢印キーで選択します。

**権限モード:**
• `--suggest` - 変更を提案、承認が必要
• `--auto-edit` - ファイルを自動編集、コマンド承認を求める
• `--full-auto` - ファイルとコマンドの完全な自律性

**full-autoを使用するタイミング:**
• 体系的なリファクタリングタスク
• 一括ファイル操作
• lintの修正とコードクリーンアップ
• 明確に定義された低リスクの操作

</details>

### セッションには1つの目標があるべき

`このセッションの目標は<具体的な目標>です。コースから外れたら知らせてください。`というプロンプトを各セッションの開始時に使用するか、メモリファイル（AGENTS.md、CLAUDE.md）に追加して、コンテキストの汚染を防ぎ、エージェントの操縦性を高めます — AI会話に単一責任の原則を適用します。

### 他のことをしながらアシスタントに作業させる

アシスタントを非同期で使用して、他の責任を処理している間にタスクに取り組めるようにします。

> "I think the faster/slower argument for me personally is missing the thing I like the most: the AI can work for me while I step away to do other things."
> — [Mitchell Hashimoto](https://mitchellh.com/writing/non-trivial-vibing#:~:text=I%20think%20the%20faster)

### 機能セッションを使用する

各機能またはタスクを別々のセッションに分離して、コンテキストの肥大化を減らし、精度を向上させます。gitの機能ブランチがコード変更を分離するのと同じです。

### 誘導的ではなく、開かれた質問をする

「私は正しいですよね...」という質問を避けます - 代わりに、賛否両論、代替案、「何を見逃していますか？」と尋ねて、LLMの同意する傾向に対抗します。

> "My best current technique for avoiding this is a bit of role-play that gives the coding agent a reason not to blindly trust the code review... 'A reviewer did some analysis of this PR. They're external, so reading the codebase cold... 1) should we hire this reviewer 2) which of the issues they've flagged should be fixed?'"
> — [Jesse Vincent](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/#:~:text=My%20best%20current%20technique)

### 安価で高速から開始し、行き詰まったらエスカレートする

日常的なタスクには高速/安価なモデルから始め、複雑な問題に遭遇した場合のみ、より強力なモデルにエスカレートします。

**Community adoption**: 19% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-smart-model-escalation) (n=16)

> "Sonnet 4 handles 90% of tasks effectively. Switch to Opus when Sonnet gets stuck. Recommend starting with Sonnet and providing comprehensive context."
> — [Sankalp](https://sankalp.bearblog.dev/my-claude-code-experience-after-2-weeks-of-usage/#:~:text=Sonnet%204%20handles%2090%25)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

`/model`を使用して切り替えます。より安価で高速だが精度は低い：`Claude Sonnet 4`。最高評価：`Claude Opus 4.1`。

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

`/model`を使用して切り替えます。より安価で高速だが精度は低い：`gpt-5-medium`。最高評価：`gpt-5-high`。

</details>

### コーディング中にロールバックポイントを作成する

実験が失敗したときに戻ることができるチェックポイントを作成します—リスクの高い変更の前に既知の良好な動作状態をキャプチャします。

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

実験の前に既知の良好な状態をコミットします。例：`git commit -m "Working state before refactor"`。リスクの高い変更の場合は、最初にブランチ：`git checkout -b experiment/feature`。失敗した場合は、`git reset --hard HEAD~1`またはmainに戻ります。クイック一時保存には`git stash`を使用します。

</details>

<details>
<summary><strong>Cursor</strong></summary>

CursorはAI編集をアンドゥ可能なチェックポイントとして記録します。Cmd+Z/Ctrl+Zを使用して変更を遡ります。耐久性のあるロールバックには、「スキーマ書き換え前のチェックポイント」のようなメッセージで動作状態をコミットします。実験にはブランチを使用し、マージ前に差分をレビューします。

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

大きな編集の前に、保存状態のコミットを実行します：`git commit -am "Checkpoint before Codex changes"`。実験の場合は、ブランチ：`git checkout -b codex/experiment`。結果が期待外れの場合は、`git reset --hard HEAD~1`またはブランチを放棄します。リスクの高い試みにはセッション分離を使用します。

</details>

