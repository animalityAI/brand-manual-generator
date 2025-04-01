# Brand Manual Generator

A Python script that generates comprehensive HTML/CSS brand manuals with guidelines for logo usage, colors, typography, and platform-specific guidelines across multiple platforms and environments.

## Features

- **Comprehensive Brand Guidelines**: Covers all aspects of brand identity and usage
- **Multi-platform Support**: Includes guidelines for web, iOS, Android, Apple Vision Pro, Apple Watch, and physical spaces
- **Customizable**: Easy to configure with your brand's colors, fonts, and logo
- **Responsive Design**: The generated manual looks great on all devices
- **Self-contained HTML**: Single HTML file with embedded CSS (no external dependencies)
- **Interactive Navigation**: Sidebar for easy section access

## Platforms & Elements Covered

- Logo usage guidelines
- Color palette
- Typography system
- Web guidelines
- iOS (iPhone) guidelines
- Android guidelines
- Vision Pro guidelines
- Apple Watch guidelines
- API documentation standards
- Robotics & AI applications
- SEO best practices
- Physical space branding (buildings, signage, etc.)

## Installation

Clone this repository:

```bash
git clone https://github.com/animalityAI/brand-manual-generator.git
cd brand-manual-generator
```

No additional dependencies are required beyond Python's standard library!

## Usage

Run the script with your brand details:

```bash
python brand_manual_generator.py --brand-name "YourBrand" --primary-color "#3498db" --secondary-color "#2ecc71"
```

### Command-line Arguments

| Argument | Description | Default Value |
|----------|-------------|---------------|
| `--brand-name` | Name of your brand (required) | None |
| `--primary-color` | Primary brand color (HEX) | #3498db (blue) |
| `--secondary-color` | Secondary brand color (HEX) | #2ecc71 (green) |
| `--font-primary` | Primary font for headings | Montserrat |
| `--font-secondary` | Secondary font for body text | Open Sans |
| `--logo-path` | Path to your logo file (optional) | None |
| `--output-dir` | Output directory | ./output |

## Example Output

The script generates a single HTML file with embedded CSS that includes:

- Interactive sidebar navigation
- Logo usage guidelines with do's and don'ts
- Color palette with visual swatches
- Typography examples
- Platform-specific guidelines
- SEO best practices
- And much more...

The output is saved to `./output/yourbrand_brand_manual.html` by default.

## Customization

You can extend the `BrandManualGenerator` class to add or modify sections to meet your specific needs. The modular design makes it easy to customize.

## Contributing

Contributions are welcome! Feel free to submit a pull request with improvements or additional features.

## License

MIT License
