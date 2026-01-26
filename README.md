# pxhash (Phoenix Hash Identification & Analysis Framework)

`pxhash` is a professional defensive cybersecurity tool designed for identifying and analyzing cryptographic hash strings. It is intended for use by SOC analysts, DFIR investigators, pentesters, and students.

**Note: This tool is for identification and analysis only. It does NOT include any hash cracking or password recovery logic.**

## Features

- **Hash Identification**: Detects 50+ hash types based on length, character set, regex patterns, and structural signatures.
- **Confidence Scoring**: Assigns probability scores to each match to help prioritize results.
- **Entropy Analysis**: Calculates Shannon entropy to measure randomness and detect potential anomalies.
- **Statistical Analysis**: Identifies character sets (Hex, Base64, etc.) and structural patterns.
- **Batch Processing**: Efficiently handles large datasets from files or STDIN pipes.
- **Rich Reporting**: Beautifully formatted CLI output with `rich`, plus support for JSON reporting.
- **Extensible Signatures**: Easily add new hash types via an external JSON signature database.

## Installation

Requires Python 3.11+.

```bash
pip install -r requirements.txt
```

## Usage

### Identify a single hash
```bash
python -m pxhash.main identify 5e543256c480ac577d30f76f9120eb74
```

### Analyze a file of hashes
```bash
python -m pxhash.main analyze hashes.txt --json
```

### Pipe from STDIN
```bash
echo "5e543256c480ac577d30f76f9120eb74" | python -m pxhash.main detect
```

## Supported Hash Types
- **Standard**: MD5, SHA-1, SHA-2 Family (SHA-256, SHA-512, etc.)
- **Password**: bcrypt, scrypt, Argon2, PBKDF2
- **Enterprise**: NTLM, MySQL, PostgreSQL, Oracle
- **Other**: JWT signatures, Unix crypt formats

## Architecture

- **`cli/`**: CLI command definitions using `typer`.
- **`core/`**: Core logic for identification, entropy, and confidence scoring.
- **`signatures/`**: Extensible signature database in JSON format.
- **`models.py`**: Data models using Pydantic for type safety and validation.
- **`logger.py`**: Rich-based logging for clear, actionable feedback.

## Ethical Usage Notice

This tool is designed for defensive security purposes, forensic investigation, and educational use. Always ensure you have proper authorization before analyzing data in a professional or corporate environment.

## License

MIT License - See [LICENSE](LICENSE) for details.
