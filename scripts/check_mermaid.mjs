// Parse every Mermaid block in the repository's Markdown files with the real Mermaid parser.
//
// This checks syntax only (what `mermaid.parse` accepts); it does not render the diagrams, so it
// cannot catch layout problems. It complements the structural lint in validate_docs.py.
//
// Usage (from the repository root):
//     npm install --no-save mermaid jsdom
//     node scripts/check_mermaid.mjs .
//
// Last run locally with mermaid 12.2.0 and jsdom; the result is recorded in docs/implementation_status.md.

import { JSDOM } from 'jsdom';
import fs from 'fs';
import path from 'path';

const dom = new JSDOM('<!DOCTYPE html><body></body>');
globalThis.window = dom.window;
globalThis.document = dom.window.document;
try { globalThis.navigator = dom.window.navigator; } catch {}
const mermaid = (await import('mermaid')).default;
mermaid.initialize({ startOnLoad: false });

const root = process.argv[2] || '.';

const skip = new Set(['node_modules', 'target', '.git', '__pycache__']);
function* walk(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    if (skip.has(e.name)) continue;
    const p = path.join(d, e.name);
    if (e.isDirectory()) yield* walk(p);
    else if (e.name.endsWith('.md')) yield p;
  }
}
let total = 0, bad = 0;
for (const f of walk(root)) {
  const lines = fs.readFileSync(f, 'utf8').split('\n');
  for (let i = 0; i < lines.length; i++) {
    if (/^\s*```+\s*mermaid\s*$/.test(lines[i])) {
      let j = i + 1;
      while (j < lines.length && !/^\s*```+\s*$/.test(lines[j])) j++;
      const src = lines.slice(i + 1, j).join('\n');
      total++;
      try { await mermaid.parse(src); }
      catch (e) { bad++; console.log(`FAIL ${path.relative(root, f)}:${i + 1}: ${String(e.message || e).split('\n').slice(0, 4).join(' | ')}`); }
      i = j;
    }
  }
}
console.log(`mermaid blocks: ${total}, failed: ${bad}`);
process.exit(bad ? 1 : 0);
