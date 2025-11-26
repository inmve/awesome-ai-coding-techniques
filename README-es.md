**Available Languages:** [English](README.md) | Español | [Deutsch](README-de.md) | [Français](README-fr.md) | [日本語](README-jp.md) | [Português](README-pt.md)

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

### Configurar Archivos de Memoria

Crea archivos de contexto que guíen persistentemente las herramientas sobre la estructura, estándares y preferencias de tu proyecto.

**Community adoption**: 81% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-contextual-documentation) (n=85)

> "Think of AGENTS.md as a 'README for agents': a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project."
> — [agents.md community](https://agents.md/#:~:text=Think%20of%20AGENTS.md%20as%20a%20README%20for%20agents)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

**Para proyectos nuevos:**
Ejecuta `/init` en la raíz de tu proyecto para crear un `CLAUDE.md` inicial.

**Para códigos base existentes:**
Ejecuta `/init` y Claude analizará tu estructura de proyecto, dependencias y archivos de configuración para generar automáticamente información esencial para trabajar efectivamente en tu código base.

Claude examina:
• `package.json` - Scripts de compilación, dependencias, metadatos del proyecto
• Archivos de configuración - `.eslintrc`, `vite.config.js`, `tsconfig.json`
• Estructura del proyecto - Patrones de componentes, organización de carpetas
• Documentación - `README.md`, archivos de reglas existentes

El CLAUDE.md generado incluye:
• **Comandos esenciales** - `npm run dev`, `npm test`, `npm run build`
• **Stack tecnológico** - Frameworks, bibliotecas, herramientas identificadas
• **Visión general de arquitectura** - Patrones de componentes, gestión de estado, enrutamiento
• **Convenciones clave** - Estilo de código, organización de archivos, enfoque de pruebas
• **Problemas comunes** - Problemas de compilación, peculiaridades de configuración, notas de flujo de trabajo

**Jerarquía de archivos de memoria:**
• `~/.claude/CLAUDE.md` - tus preferencias personales de codificación (global)
• `./CLAUDE.md` - estándares del equipo del proyecto (específico del proyecto)

**Edición rápida:**
• `/memory` - interfaz de editor completa
• `#` - atajo rápido para agregar notas

**Consejos profesionales:**
• Revisa y personaliza el contenido generado para las necesidades específicas de tu proyecto
• Agrega problemas que descubras: "Nunca edites archivos en /generated/", "Siempre reinicia después de cambios de configuración"
• Enlaza a documentos del proyecto: `@docs/deployment.md`, `@architecture.md`
• Mejora iterativamente - cuando te encuentres repitiendo instrucciones a Claude, agrégalas a CLAUDE.md
• Comparte con tu equipo commitando CLAUDE.md al control de versiones

</details>

<details>
<summary><strong>Cursor</strong></summary>

**Crea `AGENTS.md` en la raíz del proyecto:**
Cursor lee este archivo (también soporta el legado `.cursorrules`) para orientación consistente del proyecto.

**El archivo AGENTS.md debe incluir:**
• **Comandos esenciales** - `npm run dev`, `npm test`, `npm run build`
• **Stack tecnológico** - Frameworks, bibliotecas, herramientas en tu proyecto
• **Guías de estilo de código** - Convenciones de nomenclatura, patrones preferidos
• **Visión general de arquitectura** - Estructura de componentes, rutas API, organización de archivos
• **Problemas comunes** - Problemas de compilación, requisitos de flujo de trabajo, restricciones

**Contexto en tiempo real (@-menciones):**
• **@codebase** - extrae archivos relevantes de todo tu proyecto automáticamente
• **@docs** - referencia tu documentación del proyecto
• **@git** - entiende lo que has cambiado recientemente
• **@web** - obtén los últimos patrones y ejemplos de internet

**Jerarquía de reglas del proyecto:**
• Reglas globales en el directorio `.cursor/rules`
• Reglas específicas del proyecto en `AGENTS.md`
• Reglas específicas de ruta con coincidencia estilo gitignore

**Consejos profesionales:**
• Combina reglas estáticas (AGENTS.md) con contexto dinámico (@-menciones)
• Usa @codebase cuando necesites que Cursor entienda el contexto completo del proyecto
• Mantén AGENTS.md enfocado en convenciones y problemas específicos del proyecto
• Deja que las @-menciones manejen el trabajo pesado para la comprensión del código

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

**Crea `AGENTS.md` en la raíz del proyecto:**
Codex lee automáticamente este archivo al inicio de cada sesión.

**El archivo AGENTS.md debe incluir:**
• **Comandos esenciales** - `npm run dev`, `npm test`, `npm run build`
• **Stack tecnológico** - Frameworks, bibliotecas, herramientas en tu proyecto
• **Guías de estilo de código** - Convenciones de nomenclatura, patrones preferidos
• **Notas de arquitectura** - Estructura de componentes, organización de archivos
• **Reglas de seguridad** - Variables de entorno, requisitos de validación de entrada
• **Problemas del proyecto** - Errores comunes, peculiaridades de compilación, notas de flujo de trabajo

**Soporte para monorepo:**
• Coloca `AGENTS.md` en cada directorio de paquete
• Codex usa el más cercano a tu directorio de trabajo
• Obtén orientación específica del paquete automáticamente

**Contexto visual (fortaleza única de Codex):**
• Arrastra y suelta capturas de pantalla directamente en tu chat
• Incluye mockups de UI y archivos de diseño
• Comparte diagramas de arquitectura y diagramas de flujo
• Perfecto para implementar diseños o explicar sistemas complejos

**Consejos profesionales:**
• Mantén tu AGENTS.md actualizado a medida que tu proyecto evoluciona
• Agrega errores comunes que quieres evitar: "Nunca edites archivos en /generated/"
• Incluye dependencias de compilación y requisitos de configuración
• Documenta cualquier procedimiento especial de despliegue o prueba

</details>

### Pedir Planificar Primero

Dile al asistente que delinee pasos, riesgos y pruebas rápidas antes de tocar código para que puedas revisar y ajustar el enfoque.

> "If you want to iterate on the plan, it helps to explicitly include instructions in the prompt to not proceed with implementation until the plan has been accepted by the user."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=If%20you%20want%20to%20iterate%20on%20the%20plan)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Presiona `Shift+Tab` para entrar en Modo Plan para que solo lea y redacte borradores. Usa el prompt de planificación compartido, itera hasta que se vea bien, luego sal del Modo Plan cuando des luz verde a la implementación.

</details>

<details>
<summary><strong>Cursor</strong></summary>

Haz clic en el toggle de Plan en Cursor para que permanezca en solo lectura mientras iteras. Haz que liste pasos, archivos impactados, riesgos y pruebas rápidas, luego sal del Modo Plan para abrir el diff una vez que des luz verde a la implementación.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Recuerda a Codex mantener la planificación separada de la implementación: lista pasos, riesgos y pruebas rápidas, pausa para tu revisión, luego déjalo implementar e inspeccionar el diff una vez aprobado.

</details>

### Planificar con Modelo de Alta Capacidad

Al recopilar requisitos o redactar especificaciones, cambia temporalmente a un modelo de mayor capacidad o modo de razonamiento extendido para que pueda leer, sintetizar y proponer un plan antes de codificar.

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Ejecuta `/model` y elige `opus` (u otro nivel superior) al definir requisitos para que pueda razonar profundamente, luego usa el Modo Plan si quieres que permanezca en solo lectura hasta que apruebes las ediciones.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Ejecuta `/model` y elige `gpt-5-codex high` para trabajo de especificaciones que se beneficie del sesgo de codificación de Codex, o elige `gpt-5 high` cuando necesites razonamiento más amplio. Regresa a tu nivel habitual una vez que el plan esté aprobado.

</details>

### Desarrollo Basado en Especificaciones: Iterar Hasta que Funcione

Itera sobre especificaciones en Markdown hasta que el asistente genere código funcional - tratando las especificaciones como la fuente de verdad en lugar de escribir código directamente.

> "The workflow involves iterating on specifications in Markdown files, asking AI to compile into code, running/testing the app, and updating the spec if something doesn't work as expected. Developers should treat specifications as living documents, constantly updating and refining them to guide AI code generation with increasing precision."
> — [GitHub Engineering](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-using-markdown-as-a-programming-language-when-building-with-ai/)

### Elegir Bibliotecas Aburridas y Estables

Elige deliberadamente bibliotecas bien establecidas con buena estabilidad que existieron antes de las fechas de corte del entrenamiento del modelo para una mejor generación de código asistida por LLM.

**Community adoption**: 64% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-choose-boring-stable-libraries) (n=43)

> "I gain enough value from LLMs that I now deliberately consider this when picking a library—I try to stick with libraries with good stability and that are popular enough that many examples of them will have made it into the training data. I like applying the principles of boring technology—innovate on your project's unique selling points, stick with tried and tested solutions for everything else."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20gain%20enough%20value%20from%20LLMs)

### Escribir Especificaciones Detalladas

Da especificaciones completas - incluso una especificación conversacional supera las instrucciones vagas.

**Community adoption**: 50% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-specification-driven-development) (n=61)

> "Here's a recent example: `Write a Python function that uses asyncio httpx with this signature:` `async def download_db(url, max_size_bytes=5 * 1025 * 1025): -> pathlib.Path`. Given a URL, this downloads the database to a temp directory and returns a path to it. BUT it checks the content length header at the start of streaming back that data and, if it's more than the limit, raises an error... I find LLMs respond extremely well to function signatures like the one I use here."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=Here's%20a%20recent%20example)

### Obtener Múltiples Opciones

Pide al LLM que presente varios enfoques con pros/contras para que puedas elegir la mejor opción.

**Community adoption**: 57% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-ai-technology-exploration) (n=51)

> "I'll use prompts like `what are options for HTTP libraries in Rust? Include usage examples`"
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I'll%20use%20prompts%20like)

### Leer, Planificar, Codificar, Confirmar

Haz que explore el código, luego haga un plan, lo implemente y lo confirme.

**Community adoption**: 53% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-explore-plan-code-commit) (n=84)

> "There's a process that I call 'priming' the agent, where instead of having the agent jump straight to performing a task, I have it read additional context upfront to increase the chances that it will produce good outputs."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=There's%20a%20process%20that%20I%20call)

### Cerebro Primero, IA Segundo

Bosqueja la solución tú mismo primero, luego usa asistentes para refinarla.

**Community adoption**: 39% didn't adopt • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-brain-first-coding) (n=59)

> "I'm subconsciously defaulting to AI for all things coding. I've been using pen and paper less. As soon as I need to plan a new feature, my first thought is asking o4-mini-high how to do it, instead of my neurons. I hate this. And I'm changing it."
> — [Alberto Fortin](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20subconsciously%20defaulting%20to%20AI)

## UI & Prototyping

### Construir un Prototipo Primero

Comienza cada proyecto con un prototipo generado rápido para demostrar que puede funcionar.

**Community adoption**: 44% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-prototype-first-development) (n=34)

> "The best way to start any project is with a prototype that proves that the key requirements of that project can be met. I often find that an LLM can get me to that working prototype within a few minutes of me sitting down with my laptop—or sometimes even while working on my phone."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=The%20best%20way%20to%20start%20any%20project)

### Mostrar Capturas de Pantalla

Incluye capturas de pantalla e itera - toma una captura del resultado, compara, repite.

**Community adoption**: 38% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-visual-iteration-technique) (n=29)

> "Give Claude a visual mock by copying / pasting or drag-dropping an image... take screenshots of the result, and iterate until its result matches the mock."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Give%20Claude%20a%20visual%20mock)

### Pedir Wireframes ASCII

Al refinar diseños, haz que el asistente dibuje wireframes ASCII para que puedas evaluar la jerarquía y el espaciado antes de tocar CSS.

### Hazlo Más Hermoso

Solo pide hacer la UI `más hermosa` o `más elegante` - funciona.

**Community adoption**: 21% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-iterative-ui-refinement) (n=33)

> "If Claude doesn't produce a well-designed UI the first time, you can just tell it to `make it more beautiful/elegant/usable`."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=If%20Claude%20doesn't%20produce)

### Codificación por Vibra

Construye proyectos a través de conversación en lugar de codificación tradicional - habla, acepta cambios e itera hasta que funcione.

**Community adoption**: 30% didn't adopt • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-experimental-vibe-coding) (n=47)

> "...I ask for the dumbest things like `decrease the padding on the sidebar by half` because I'm too lazy to find it. I `Accept All` always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment, usually that fixes it. The code grows beyond my usual comprehension, I'd have to really read through it for a while. Sometimes the LLMs can't fix a bug so I just work around it or ask for random changes until it goes away. It's not too bad for throwaway weekend projects, but still quite amusing. I'm building a project or webapp, but it's not really coding—I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works."
> — [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383)

## Coding

### Manejar las Partes Críticas, Delegar el Resto

Escribe tú mismo las partes críticas y complejas del código y delega la implementación directa restante al asistente.

> "Write the critical parts and ask AI to do the rest."
> — [Anton Zhiyanov](https://antonz.org/write-code/#:~:text=Write%20the%20critical%20parts%20and%20ask%20AI%20to%20do%20the%20rest)

### Delegar Tareas Tediosas

Delega tareas aburridas, sistemáticas y que consumen tiempo a la IA - desde pequeñas renombraciones de variables hasta grandes migraciones que no requieren pensamiento arquitectónico profundo.

**Community adoption**: 64% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-offload-tedious-tasks) (n=22)

> "I'm using LLMs, but for dumber things: `rename all occurrences of this parameter`"
> — [Alberto Fortin](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20using%20LLMs,%20but%20for%20dumber%20things)

### Confirmar Comprensión Antes de Codificar

Pide explícitamente a la herramienta que confirme su comprensión de la tarea antes de comenzar la implementación para garantizar la alineación y reducir las expectativas desalineadas.

### Tratar la IA como un Interno Digital

Da a la IA instrucciones extremadamente precisas y detalladas como lo harías con un interno - proporciona firmas de función exactas y deja que maneje la implementación.

**Community adoption**: 60% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-treat-ai-as-intern) (n=20)

> "Once I've completed the initial research I change modes dramatically. For production code my LLM usage is much more authoritarian: I treat it like a digital intern, hired to type code for me based on my detailed instructions."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20treat%20it%20like%20a%20digital%20intern)

### Mantener el Código Súper Simple

Escribe código directo con nombres de función claros, evita la herencia y trucos inteligentes - el código simple funciona mejor con asistentes.

**Community adoption**: 40% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-keep-code-dead-simple) (n=20)

> "Simple code significantly outperforms complex code in agentic contexts. I just recently wrote about ugly code and I think in the context of agents this is worth re-reading. Have the agent do `the dumbest possible thing that will work`."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Simple%20code%20significantly%20outperforms%20complex%20code)

### Preparar con Código Existente

Comienza volcando código existente en el chat para sembrar el contexto, luego modifica desde ahí.

**Community adoption**: 36% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-context-priming) (n=31)

> "I often start a new chat by dumping in existing code to seed that context, then work with the LLM to modify it in some way."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20often%20start%20a%20new%20chat)

### Definir Estructura, Delegar Implementación

Proporciona la estructura - firmas de función, esquemas de código o andamiaje - y deja que el asistente complete los detalles de implementación.

**Community adoption**: 35% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-precise-function-specification) (n=23)

> "I find LLMs respond extremely well to function signatures like the one I use here. I get to act as the function designer, the LLM does the work of building the body to my specification. I'll often follow-up with `Now write me the tests using pytest`. Again, I dictate my technology of choice—I want the LLM to save me the time of having to type out the code that's sitting in my head already."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=I%20find%20LLMs%20respond%20extremely%20well)

### Proporcionar Contexto para Nuevas Bibliotecas

Cuando uses bibliotecas fuera de los datos de entrenamiento del modelo, proporciónale ejemplos recientes y documentación para enseñarle cómo funciona la biblioteca.

**Community adoption**: 35% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-providing-context-for-unfamiliar-apis) (n=20)

> "LLMs can still help you work with libraries that exist outside their training data, but you need to put in more work—you'll need to feed them recent examples of how those libraries should be used as part of your prompt."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=LLMs%20can%20still%20help%20you%20work%20with%20libraries)

### Generar Código, No Dependencias

Escribe código personalizado en lugar de incorporar más bibliotecas cuando trabajes con asistentes.

**Community adoption**: 27% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-conservative-dependency-management) (n=30)

> "Be even more conservative about upgrades than before... I strongly prefer more code generation over using more dependencies."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Be%20even%20more%20conservative%20about)

## Debugging

### Cambiar de Enfoque Cuando el Asistente Lucha

Cuando el asistente falla repetidamente en resolver un problema específico, cambia a un enfoque alternativo en lugar de persistir con la misma solución.

> "It's at this point that I know I need to step back, review what it did, and come up with my own plans. It's time to educate myself and think critically. AI is no longer the solution; it is a liability."
> — [Mitchell Hashimoto](https://mitchellh.com/writing/non-trivial-vibing#:~:text=It's%20at%20this%20point)

### Registrar Todo para Depuración del Asistente

Diseña sistemas con registros exhaustivos para que los agentes puedan leer registros para entender qué está pasando y autodiagnosticar problemas.

**Community adoption**: 35% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-log-everything-for-debugging) (n=17)

> "In general logging is super important. For instance my app currently has a sign in and register flow that sends an email to the user. In debug mode (which the agent runs in), the email is just logged to stdout. This is crucial! It allows the agent to complete a full sign-in with a remote controlled browser without extra assistance. It knows that emails are being logged thanks to a CLAUDE.md instruction and it automatically consults the log for the necessary link to click."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=In%20general%20logging%20is%20super%20important)

### Deja que se Pruebe y se Arregle Solo

Configura herramientas para hacer cambios, ejecutar pruebas, ver qué falla, e intentar de nuevo por su cuenta.

**Community adoption**: 27% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-ai-feedback-loops) (n=22)

> "Claude is most useful when it's capable of independently driving feedback loops that allow it to make a change, test the change, and gather context on what failed to try another iteration."
> — [Indragie Karunaratne](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code#:~:text=Claude%20is%20most%20useful%20when)

### Usar Subagentes para Verificar Dos Veces

Generar subagentes para verificar detalles o investigar preguntas específicas.

**Community adoption**: 22% didn't adopt • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-subagent-verification) (n=23)

> "Telling Claude to use subagents to verify details or investigate particular questions it might have, especially early on in a conversation or task, tends to preserve context availability without much downside in terms of lost efficiency."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Telling%20Claude%20to%20use%20subagents)

## Testing & QA

### Siempre Probar el Código Tú Mismo

Absolutamente no puedes externalizar las pruebas - siempre verifica que el código realmente funcione.

**Community adoption**: 67% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-comprehensive-testing-mandate) (n=27)

> "The one thing you absolutely cannot outsource to the machine is testing that the code actually works. Your responsibility as a software developer is to deliver working systems. If you haven't seen it run, it's not a working system. You need to invest in strengthening those manual QA habits."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=The%20one%20thing%20you%20absolutely%20cannot%20outsource)

### Escribir Pruebas Primero

Escribe pruebas primero, confirma que fallen, luego implementa hasta que pasen.

**Community adoption**: 19% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-test-driven-development-ai) (n=21)

> "Write test first (red), Implement - Minimal code to pass (green), Refactor - Clean up with tests passing"
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Test-driven%20when%20possible)

## Review & Refactoring

### Iterar en la Salida del Asistente Tú Mismo

Después de que el asistente complete el trabajo, itera y refina manualmente la implementación en lugar de aceptarla tal cual.

> "I almost always go in after an AI does work and iterate myself for awhile, too."
> — [Mitchell Hashimoto](https://mitchellh.com/writing/non-trivial-vibing#:~:text=I%20almost%20always%20go%20in)

### Tratar el Código de la IA como Pull Request

Revisa el código generado por la IA como si fuera un pull request de un colega, proporcionando comentarios iterativos para que el asistente los aborde en lugar de editarlo directamente tú mismo.

> "treating the generated code as a Merge Request on which you submit comment for correction"
> — [HN Discussion](https://news.ycombinator.com/item?id=45415232)

### Pedir al Agente que Revise su Propio Código

Haz que la IA realice una revisión de código de su propio trabajo antes de la revisión humana para descubrir problemas y mejoras.

> "Asking the agent to perform a code review on its own work is surprisingly fruitful."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Asking%20the%20agent%20to%20perform%20a%20code%20review)

### Realmente Leer el Código

Detente y realmente inspecciona lo que se ha escrito - podrías sorprenderte.

**Community adoption**: 63% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-critical-code-review-strategy) (n=19)

> "Asking the agent to perform a code review on its own work is surprisingly fruitful. AI-generated code is often incorrect or inefficient. It's important for me to call out that I believe I'm ultimately responsible for the code that goes into a PR with my name on it, regardless of how it was produced. Therefore, especially in any professional context, I manually review all AI-written code and test cases."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=Asking%20the%20agent%20to%20perform%20a%20code%20review)

### Siempre Revisar el Diff Completo

La codificación por vibra puede introducir efectos secundarios no intencionales - siempre revisa los diffs cuidadosamente ya que el asistente puede alterar más de lo solicitado.

**Community adoption**: 56% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-check-for-unintended-changes) (n=16)

> "I believe I'm ultimately responsible for the code that goes into a PR with my name on it, regardless of how it was produced. Therefore, especially in any professional context, I manually review all AI-written code and test cases."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/Getting-Good-Results-from-Claude-Code.html#:~:text=I%20believe%20I'm%20ultimately%20responsible,manually%20review%20all%20AI-written%20code)

### Seguir Pidiendo Cambios

A diferencia de los humanos, los asistentes nunca se molestan - sigue pidiendo refactorizaciones hasta que estés contento.

**Community adoption**: 47% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-conversational-code-refinement) (n=17)

> "If I don't like what an LLM has written, they'll never complain at being told to refactor it! `Break that repetitive code out into a function`, `use string manipulation methods rather than a regular expression`, or even `write that better!`—the code an LLM produces first time is rarely the final implementation, but they can re-type it dozens of times for you without ever getting frustrated or bored."
> — [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#:~:text=If%20I%20don't%20like%20what%20an%20LLM%20has%20written)

### Editar Código en el Diff

Revisa los cambios en la vista de diff y escribe correcciones directamente en el diff antes de confirmar.

**Community adoption**: 27% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-diff-based-iterative-refinement) (n=15)

> "I manually review all AI-written code and test cases. I'll add test cases for anything I think is missing or needs improvement, either manually or by asking the LLM to write those cases (which I then review)."
> — [Chris Dzombak](https://www.dzombak.com/blog/2025/08/getting-good-results-from-claude-code/#:~:text=I%20manually%20review%20all)

### Uno Escribe, Otro Revisa

Haz que un agente escriba código, luego usa un agente nuevo para revisar y encontrar problemas.

**Community adoption**: 31% situational • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-multi-agent-verification) (n=16)

> "Use Claude to write code. Run `/clear` or start a second Claude in another terminal. Have the second Claude review the first Claude's work. Start another Claude (or `/clear` again) to read both the code and review feedback. Have this Claude edit the code based on the feedback. This separation often yields better results than having a single Claude handle everything."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Have%20one%20Claude%20write%20code)

## Cross-Stage Techniques

### Cambiar Estilos de Salida del Asistente

Selecciona el estilo de salida del asistente que coincida con tu objetivo actual.

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

**Cambiar estilos rápidamente**
Ejecuta `/output-style` para abrir el selector, o `/output-style learning` para saltar directamente al modo Aprendizaje. La selección se almacena por proyecto en `.claude/settings.local.json`.

**Modos de auto-enseñanza**
Predeterminado se mantiene enfocado en entregar; `explanatory` inserta llamadas de atención de conocimientos; `learning` agrega marcadores `TODO(human)` para que completes piezas clave tú mismo.

**Crear estilos personalizados**
Ejecuta `/output-style:new I want ...` para crear un archivo markdown en `~/.claude/output-styles`. Ajusta el frontmatter y las instrucciones; las variantes específicas del proyecto viven en `.claude/output-styles/`.

**Por qué los estilos difieren**
Los estilos reemplazan el prompt del sistema predeterminado de Claude Code, a diferencia de `CLAUDE.md` (mensaje de usuario) o `--append-system-prompt` (añade).

</details>

### Limpiar Contexto Entre Tareas

Reinicia la ventana de contexto de la IA entre tareas no relacionadas para prevenir confusión y mejorar el rendimiento en nuevos problemas.

**Community adoption**: 67% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-clear-context-between-tasks) (n=15)

> "During long sessions, Claude's context window can fill with irrelevant conversation, file contents, and commands. This can reduce performance and sometimes distract Claude. Use the `/clear` command frequently between tasks to reset the context window."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=During%20long%20sessions%2C%20Claude's%20context)

### Elegir Herramientas por Estilo Conversacional

Selecciona asistentes de codificación según prefieras colaboración humana o eficiencia estructurada como robot - la personalidad conversacional afecta significativamente la productividad y el disfrute.

> "In terms of personality, it's the opposite for me: Claude Code feels like my pair-programming partner, while Codex feels like a robot (very structured but not very human in its conversational style).

Problem is after a while, the 'You are absolutely right!' kinda gets on my nerves.

Codex is dry. You can insult it and it doesn't even answer. No personality. Claude is like, a friend who admits messing up. I spend like close to 10 hours a day coding between CC and Codex CLI and I see huge differences in personality and creativity. I like Claude better for that. Much more creative.

Codex is monotone straight to the point, but most importantly the reason why it is better is because it's not agreeable at all. It will challenge you when you're suggesting something wrong and stay with its opinion."
> — [Reddit Community](https://www.reddit.com/r/ClaudeAI/comments/1nk4v4k/comment/nev86ot)

### Elegir el Modelo Adecuado para el Trabajo

Antes de comenzar una nueva tarea, elige dos palancas: el modelo correcto (modalidad, longitud de contexto, confiabilidad de llamadas a herramientas, latencia, costo) y el nivel de razonamiento correcto (asigna más/menos tokens de pensamiento) — no uses el predeterminado ciegamente.

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Dos palancas al inicio de la tarea:
1. `/model` - elige `fast` para ediciones rutinarias, `long-context` para multi-archivo o documentos largos, `vision-strong` para UI/capturas de pantalla.
2. Nivel de razonamiento - habilita pensamiento extendido para depuración compleja, trabajo de arquitectura o especificaciones ambiguas para que el asistente asigne más tokens de razonamiento.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Comienza con `gpt-5-minimal`/`gpt-5-low` para ediciones rápidas; elige una variante de mayor razonamiento `gpt-5-high`/`gpt-5-medium` cuando la complejidad aumente.

</details>

### Centralizar Archivos de Memoria

Mantén un documento de instrucciones canónico y dirige todos los demás archivos del agente hacia él con una línea de puntero llamativa, un enlace simbólico o una inclusión @file para que la orientación entre herramientas se mantenga consistente.

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Mantén `CLAUDE.md` como la fuente de verdad y usa una de estas tres formas.

1. Pon `@CLAUDE.md` en `AGENTS.md`.

2. Enlaza simbólicamente `AGENTS.md` a `CLAUDE.md` con `ln -sf CLAUDE.md AGENTS.md` para que ambas herramientas compartan el mismo archivo.

3. Deja `AGENTS.md` como una sola línea: `READ CLAUDE.md FIRST!!!`.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Usa el mismo trío desde el lado de Codex.

1. Si Codex contiene el texto principal, deja `AGENTS.md` completo y coloca `@AGENTS.md` dentro de `CLAUDE.md` para que ambas herramientas lleguen al mismo documento.

2. Ejecuta `ln -sf CLAUDE.md AGENTS.md` para que el archivo que Codex lee sea solo un enlace simbólico a `CLAUDE.md`.

3. Cuando `CLAUDE.md` es canónico, mantén `AGENTS.md` en una línea: `READ CLAUDE.md FIRST!!!`.

</details>

### Interrumpir y Redirigir a Menudo

No dejes que el asistente vaya demasiado lejos por el camino equivocado - interrumpe, proporciona retroalimentación y redirige tan pronto como notes problemas.

**Community adoption**: 60% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-interrupt-and-redirect-often) (n=15)

> "Press Escape to interrupt Claude during any phase (thinking, tool calls, file edits), preserving context so you can redirect or expand instructions. Double-tap Escape to jump back in history, edit a previous prompt, and explore a different direction. You can edit the prompt and repeat until you get the result you're looking for."
> — [Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices#:~:text=Press%20Escape%20to%20interrupt%20Claude)

### Usar un Agente como Compañero de Codificación

Colabora como con un compañero de codificación - explica problemas, obtén retroalimentación y trabajen juntos en soluciones.

**Community adoption**: 63% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-ai-coding-partner) (n=16)

> "Claude Code feels like pairing with someone with a few years under their belt who just needs the occasional nudge. Then like with pairing, it's review, refactor and test time because it's still your name on the git commit."
> — [Orta Therox](https://blog.puzzmo.com/posts/2025/06/07/orta-on-claude/#:~:text=Claude%20Code%20feels%20like%20pairing)

### Aprender de Ello, Codificar Tú Mismo

Usa asistentes para aprender nuevos lenguajes y conceptos, luego aplica ese conocimiento cuando codifiques.

**Community adoption**: 43% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-learning-oriented-ai-interaction) (n=14)

> "I'm leveraging them to learn Go, to upskill myself. And then I apply this new knowledge when I code."
> — [Alberto Fortin](https://albertofortin.com/writing/coding-with-ai#:~:text=I'm%20leveraging%20them%20to%20learn%20Go)

### Usar Énfasis Fuerte en Prompts

Usa IMPORTANTE, NUNCA, SIEMPRE liberalmente en prompts para dirigir a la IA lejos de errores comunes - sigue siendo el enfoque más efectivo.

**Community adoption**: 50% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-use-strong-emphasis-words) (n=14)

> "Unfortunately CC is no better when it comes to asking the model to not do something. IMPORTANT, VERY IMPORTANT, NEVER and ALWAYS seem to be the best way to steer the model away from landmines. I expect the models to get more steerable in the future and avoid this ugliness. But for now, CC uses this liberally, and so should you."
> — [Vivek (MinusX AI Team)](https://minusx.ai/blog/decoding-claude-code/#:~:text=Unfortunately%20CC%20is%20no%20better)

### Construir Herramientas Rápidas y a Prueba de Tontos

Crea herramientas que respondan rápidamente, proporcionen mensajes de error claros y se protejan contra mal uso por agentes.

**Community adoption**: 17% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-build-fast-foolproof-tools) (n=12)

> "Tools need to be fast. The quicker they respond (and the less useless output they produce) the better. Crashes are tolerable; hangs are problematic. Tools need to be user friendly! Tools must clearly inform agents of misuse or errors to ensure forward progress. Tools need to be protected against an LLM chaos monkey using them completely wrong. There is no such thing as user error or undefined behavior!"
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=Tools%20need%20to%20be%20fast)

### Ejecutar Múltiples Agentes en Paralelo

Deja de esperar a que termine un agente antes de iniciar otro - ejecuta múltiples agentes en paralelo en funciones separadas sin conflictos o confusión.

**Community adoption**: 14% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-run-multiple-agents-parallel) (n=14)

> "We are exploring solving both of these issues in sketch.dev using containers. By default sketch creates a little development environment in a container with a copy of the source code and the runner has the ability to extract git commits from the container. This lets you run many simultaneously."
> — [David Crawshaw](https://crawshaw.io/blog/programming-with-agents#:~:text=We%20are%20exploring%20solving%20both%20of%20these%20issues)

### Ejecutar Sin Permisos para Tareas Fáciles

Habilita el modo autónomo cuando las tareas son lo suficientemente directas como para aceptar todos los cambios de todos modos - evita la supervisión constante.

> "I disable all permission checks. Which basically means I run `claude --dangerously-skip-permissions`. More specifically I have an alias called claude-yolo set up."
> — [Armin Ronacher](https://lucumr.pocoo.org/2025/6/12/agentic-coding/#:~:text=I%20disable%20all%20permission%20checks)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Ejecuta `claude --dangerously-skip-permissions` para habilitar el modo YOLO donde Claude se ejecuta ininterrumpidamente sin prompts de permiso.

**Cambiar durante sesión:** Usa `/permissions` para gestionar permisos de herramientas a mitad de sesión sin reiniciar. Establece reglas de permiso para herramientas específicas para omitir prompts de aprobación.

**Cuándo usar:**
• Corregir errores de lint en múltiples archivos
• Refactorización simple y renombrado de variables
• Actualizaciones de código rutinarias y migraciones
• Tareas donde probablemente aceptarías todos los cambios de todos modos

**Consideraciones de seguridad:**
• Mejor usar en contenedores o VMs para aislamiento
• Evitar en sistemas de producción críticos
• Considera usar la configuración `allowedTools` para control granular en lugar de permisos generales

**Configurar alias:** Muchos usuarios crean `alias cc='claude --dangerously-skip-permissions'` para acceso rápido.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Habilita el modo autónomo completo con `codex --full-auto` o usa el comando `/mode` en sesión.

**Cambiar durante sesión:** Usa `/mode` para intercambiar entre niveles de permiso sin perder el contexto de sesión. Selecciona con las teclas de flecha de los modos suggest/auto-edit/full-auto.

**Modos de permisos:**
• `--suggest` - Sugiere cambios, requiere aprobación
• `--auto-edit` - Auto-edita archivos, pide aprobación de comandos
• `--full-auto` - Autonomía completa para archivos y comandos

**Cuándo usar full-auto:**
• Tareas de refactorización sistemática
• Operaciones de archivos en masa
• Correcciones de lint y limpieza de código
• Operaciones bien definidas y de bajo riesgo

</details>

### Una Sesión Debe Tener Un Objetivo

Usa el prompt `El objetivo de esta sesión es <objetivo específico>. Infórmame si nos desviamos del camino.` ya sea al comienzo de cada sesión o agrégalo a tu archivo de memoria (AGENTS.md, CLAUDE.md) para prevenir el envenenamiento del contexto y aumentar la dirigibilidad del agente - aplicando el Principio de Responsabilidad Única a las conversaciones con IA.

### Dejar que el Asistente Trabaje Mientras Haces Otras Cosas

Usa asistentes de forma asíncrona para que puedan trabajar en tareas mientras manejas otras responsabilidades.

> "I think the faster/slower argument for me personally is missing the thing I like the most: the AI can work for me while I step away to do other things."
> — [Mitchell Hashimoto](https://mitchellh.com/writing/non-trivial-vibing#:~:text=I%20think%20the%20faster)

### Usar Sesiones de Características

Aísla cada característica o tarea en sesiones separadas para reducir la sobrecarga de contexto y mejorar la precisión, al igual que las ramas de características en git aíslan los cambios de código.

### Haz Preguntas Abiertas, No Dirigidas

Evita preguntas como '¿Tengo razón en que...?' - en su lugar, pide pros/contras, alternativas y '¿Qué me estoy perdiendo?' para contrarrestar la tendencia del LLM a estar de acuerdo.

> "My best current technique for avoiding this is a bit of role-play that gives the coding agent a reason not to blindly trust the code review... 'A reviewer did some analysis of this PR. They're external, so reading the codebase cold... 1) should we hire this reviewer 2) which of the issues they've flagged should be fixed?'"
> — [Jesse Vincent](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/#:~:text=My%20best%20current%20technique)

### Empezar barato y rápido; escalar cuando te atasques

Comienza con modelos más rápidos/baratos para tareas rutinarias, luego escala a modelos más potentes solo cuando encuentres problemas complejos.

**Community adoption**: 19% essential • [Vote on coding-with-ai.dev](https://coding-with-ai.dev#tech-smart-model-escalation) (n=16)

> "Sonnet 4 handles 90% of tasks effectively. Switch to Opus when Sonnet gets stuck. Recommend starting with Sonnet and providing comprehensive context."
> — [Sankalp](https://sankalp.bearblog.dev/my-claude-code-experience-after-2-weeks-of-usage/#:~:text=Sonnet%204%20handles%2090%25)

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Usa `/model` para cambiar. Más barato, más rápido, pero menos preciso: `Claude Sonnet 4`. Top calificado: `Claude Opus 4.1`.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Usa `/model` para cambiar. Más barato, más rápido, pero menos preciso: `gpt-5-medium`. Top calificado: `gpt-5-high`.

</details>

### Crear Puntos de Reversión Al Codificar

Crea puntos de control a los que puedas revertir cuando los experimentos fallen—captura estados de trabajo conocidos-buenos antes de cambios riesgosos.

**Tool Implementations:**

<details>
<summary><strong>Claude Code</strong></summary>

Commitea estados conocidos como buenos antes de experimentos. Ejemplo: `git commit -m "Working state before refactor"`. Para cambios riesgosos, primero crea una rama: `git checkout -b experiment/feature`. Si falla, `git reset --hard HEAD~1` o regresa a `main`. Usa `git stash` para guardados temporales rápidos.

</details>

<details>
<summary><strong>Cursor</strong></summary>

Cursor registra ediciones de IA como puntos de control deshacibles. Usa Cmd+Z/Ctrl+Z para retroceder a través de cambios. Para reversión duradera, commitea estados funcionales con mensajes como 'Checkpoint before schema rewrite'; usa ramas para experimentos y revisa diffs antes de merge.

</details>

<details>
<summary><strong>Codex CLI</strong></summary>

Antes de ediciones grandes, ejecuta un commit de estado guardado: `git commit -am "Checkpoint before Codex changes"`. Para experimentos, crea rama: `git checkout -b codex/experiment`. Si los resultados decepcionan, `git reset --hard HEAD~1` o abandona la rama. Usa separación de sesiones para intentos riesgosos.

</details>

