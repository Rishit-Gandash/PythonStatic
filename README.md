# PythonStatic

A lightweight static site generator written in Python. It reads user-provided markdown files (in `content/`), and converts them to HTML pages (in `docs/`) and outputs a ready-to-serve static site — with no external dependencies beyond Python.

This project was build using the course from boot.dev.

## How it works

The generator reads source content from the `content/` directory, processes each file through a custom Markdown-to-HTML parser, and injects the result into `template.html` using `{{ Title }}` and `{{ Content }}` placeholders. The finished pages are written to the `docs/` directory, which can then be served directly or deployed to any static hosting provider.

Styling is applied via `index.css`, which is linked from the template and served alongside the generated pages.

The markdown pages follow strict syntax. All blocks (quotes, paragraphs etc.) must be properly typed. All image links must be provided in `static/`

## Project structure

```
PythonStatic/
├── content/          # Source Markdown files
├── docs/             # Generated HTML output (served or deployed)
├── src/              # Python source code
├── static/           # Static assets (images, fonts, etc.)
├── template.html     # HTML template with {{ Title }} and {{ Content }} placeholders
├── index.css         # Stylesheet linked from all generated pages
└── build.sh          # Runs the generator for a given path
```

## Usage

### Build and preview locally

```bash
./main.sh
```

This runs the generator and then starts a local HTTP server at `http://localhost:8888` serving the `docs/` directory.

### Build only

```bash
./build.sh
```

Equivalent to running `python3 src/main.py "/PythonStatic/"` directly.

### Run tests

```bash
./test.sh
```

Discovers and runs all unit tests found under `src/tests/` using Python's built-in `unittest` framework.

## Requirements

- Python 3 (no third-party packages required)

## Customising the template

Edit `template.html` to change the page structure. The generator replaces two placeholders at build time:

- `{{ Title }}` — populated from the content file's filename or front matter
- `{{ Content }}` — the rendered HTML body of the Markdown file

Styles go in `index.css`, which is linked from the template via an absolute path (`/index.css`).

## Todo 
- Allow for loose markdown syntax
- Dynamically handle broken links
- Allow for cross text highlighting (e.g. `<b>some<i>text</b>thats</i> weird`)
