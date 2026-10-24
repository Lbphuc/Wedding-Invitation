#!/usr/bin/env python3
"""Build site.min.css safely from editable source stylesheets.

Whitespace is collapsed outside quoted strings, but spaces that can be meaningful
in descendant selectors (especially before pseudo-classes such as :is/:not) are
preserved. This intentionally favors correct selectors over a few saved bytes.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCES = ['styles.css', 'design-system.css', 'responsive.css', 'layout-system.css', 'groom-simple.css']
OUTPUT = ROOT / 'site.min.css'


def strip_comments(text: str) -> str:
    """Remove CSS comments without modifying quoted strings."""
    out = []
    i = 0
    quote = None
    while i < len(text):
        ch = text[i]
        if quote:
            out.append(ch)
            if ch == '\\' and i + 1 < len(text):
                i += 1
                out.append(text[i])
            elif ch == quote:
                quote = None
            i += 1
            continue
        if ch in ('"', "'"):
            quote = ch
            out.append(ch)
            i += 1
            continue
        if ch == '/' and i + 1 < len(text) and text[i + 1] == '*':
            end = text.find('*/', i + 2)
            if end == -1:
                raise ValueError('Unclosed CSS comment')
            i = end + 2
            continue
        out.append(ch)
        i += 1
    return ''.join(out)


def compact(text: str) -> str:
    """Collapse whitespace conservatively, retaining selector combinator spaces."""
    text = strip_comments(text)
    out = []
    i = 0
    quote = None
    pending_space = False
    while i < len(text):
        ch = text[i]
        if quote:
            out.append(ch)
            if ch == '\\' and i + 1 < len(text):
                i += 1
                out.append(text[i])
            elif ch == quote:
                quote = None
            i += 1
            continue
        if ch in ('"', "'"):
            if pending_space and out and out[-1] not in '{},;' and ch not in '{},;':
                out.append(' ')
            pending_space = False
            quote = ch
            out.append(ch)
            i += 1
            continue
        if ch.isspace():
            pending_space = True
            i += 1
            continue
        if pending_space and out:
            prev = out[-1]
            # Whitespace around braces, commas, and semicolons is never a
            # descendant combinator; whitespace around ':' and '>' may be.
            if prev not in '{},;' and ch not in '{},;':
                out.append(' ')
        pending_space = False
        out.append(ch)
        i += 1
    return ''.join(out).strip()


combined = '\n'.join((ROOT / item).read_text(encoding='utf-8') for item in SOURCES)
minified = compact(combined)
OUTPUT.write_text(minified + '\n', encoding='utf-8')
print(f'Built {OUTPUT.name}: {len(combined.encode())} -> {len(minified.encode())} bytes')
