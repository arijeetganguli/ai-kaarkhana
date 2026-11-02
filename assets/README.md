# Assets

Original, version controlled visuals for the handbook: a logo, a hero image and nine diagrams. They are all **SVG**, so they stay sharp at any size, diff cleanly and need no external fonts or images.

| Folder | Contents |
| --- | --- |
| [`logos/`](logos/README.md) | Wordmark and the gear mark |
| [`images/`](images/README.md) | The hero image used at the top of the repository README |
| [`diagrams/`](diagrams/README.md) | Nine explanatory diagrams used across the handbook |

## How the assets are made

The SVGs are **generated** by [`scripts/generate_svgs.py`](../scripts/generate_svgs.py) so that the visual identity stays consistent. To change one, edit the script, run it, and commit the script and the regenerated files together:

```bash
python scripts/generate_svgs.py
```

Do not hand edit the generated SVG files; the next run would overwrite your changes.

## Design rules

- **Self contained.** Each SVG draws its own dark panel, so it is readable on light and dark pages alike. No scripts, no external references, no remote fonts.
- **One palette.** Deep indigo panels with saffron, teal, leaf green and coral accents. The accents carry meaning in the diagrams (for example coral is the red phase of TDD) but no information depends on colour alone: every state is also labelled with text.
- **One icon language.** Rounded cards and a gear mark. The gear with a diamond at its centre is the project's mark: a *kaarkhana* is a workshop, and the diamond stands for the engineer's judgement at the centre of the machine.
- **Accessible.** Every SVG has a `<title>` and a `<desc>`. Meaningful images are always given alt text where they are embedded.
- **Plain system fonts.** A generic sans serif stack, so text renders the same without downloading anything.

The design is deliberately restrained. It uses a subtle Indian inspired palette and the workshop idea in the name, not decorative motifs.

## The diagrams

Each one is embedded and described in the [diagrams gallery](diagrams/README.md), which also lists the pages that use it.

| Diagram | Shows |
| --- | --- |
| [AI assisted engineering lifecycle](diagrams/ai-assisted-engineering-lifecycle.svg) | The loop from understanding to learning |
| [Developer and AI responsibility model](diagrams/developer-ai-responsibility-model.svg) | Who owns what |
| [TDD red, green, refactor](diagrams/tdd-red-green-refactor.svg) | The test first cycle |
| [Requirement to test traceability](diagrams/requirement-to-test-traceability.svg) | The chain from requirement to evidence |
| [Edge case discovery](diagrams/edge-case-discovery.svg) | Eight categories of edge case |
| [AI skill execution workflow](diagrams/ai-skill-execution-workflow.svg) | How a skill is used and validated |
| [Code review and quality gate workflow](diagrams/code-review-quality-gate-workflow.svg) | Gates before merge |
| [AI engineering maturity model](diagrams/ai-engineering-maturity-model.svg) | Five adoption levels |
| [End to end feature development workflow](diagrams/feature-development-workflow.svg) | Ten steps with the skill for each |

## Adding or changing a visual

1. Add a function to the generator and call it from `main`.
2. Give the SVG a title and a description.
3. Render it and look at it. Check that no text overflows its box and that arrows touch what they connect.
4. Embed it with a relative path and meaningful alt text, for example `![AI assisted engineering lifecycle](../assets/diagrams/ai-assisted-engineering-lifecycle.svg)`.
5. Run `python scripts/validate_docs.py`, which checks that SVGs are well formed and that every embedded image exists.

For simple flows inside a page, prefer a [Mermaid](https://mermaid.js.org/) diagram, which GitHub renders from text.

Back to the [repository README](../README.md).
