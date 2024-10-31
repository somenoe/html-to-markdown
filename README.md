# HTML to Markdown Converter

A Python utility for batch converting HTML documents to standardized Markdown format. Built on the [Markdownify](https://github.com/matthewwithanm/python-markdownify/blob/develop/README.rst) library, this tool provides:

- Preservation of source directory structure
- Comprehensive logging and error handling
- Clean, consistent Markdown output formatting

## Installation

Install all required dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

```
html-to-markdown/
├── data/
│   ├── input/          # Source HTML files
│   ├── output/         # Converted Markdown files
│   └── logs/           # Application logs
├── prompts/
│   ├── step.md        # Processing workflow documentation
│   └── gen-commit.md  # Commit message templates
├── logger/
│   └── config.py      # Logging configuration
└── main.py            # Application entry point
```

## Usage Guide

### Basic Conversion

Execute the conversion process:

```bash
python main.py
```

This command processes all HTML files from `data/input` and generates corresponding Markdown files in `data/output`.

### Quality Control

Enforce consistent Markdown formatting using [MarkdownLint CLI2](https://github.com/DavidAnson/markdownlint-cli2):

```bash
npx markdownlint-cli2 --fix "data/output/**/*.md"
```

## Development

I recommend checking type before committing changes.

### Type Checking

Ensure type safety with MyPy:

```bash
mypy .
```

### Best Practices

- Run type checking before committing changes
- Follow the established logging patterns for error handling
- Maintain test coverage for new features
- Update documentation for significant changes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Markdownify](https://github.com/matthewwithanm/python-markdownify) team for the core conversion engine
- [MarkdownLint CLI2](https://github.com/DavidAnson/markdownlint-cli2) for quality assurance tools
