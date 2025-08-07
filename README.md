# LangExtract Demo

A Gemini-powered information extraction demo using LangExtract.
# LangExtract Demo

This is a Gemini-powered Python project that extracts structured information from unstructured text (like job application emails or invoices) using the [LangExtract](https://pypi.org/project/langextract/) library and Gemini 2.5 Pro model.

It includes:
- Custom prompt-based extraction
- Example-driven guidance for more accurate results
- Docker-based environment for easy setup and execution
- Makefile for common tasks

---

##  Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/sprusov/langextract-demo.git
cd langextract-demo
```

### 2. Set up your API key

Create a `.env` file in the root with your Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 3. Build the Docker container

```bash
docker-compose build --no-cache
```

### 4. Run the extractors

To run both the job application and invoice extractors:

```bash
make run
```

This will process both `job_application_email.txt` and `invoice.txt` and display extracted entities.
---

## Makefile Commands

| Command            | Description                                         |
|--------------------|-----------------------------------------------------|
| `make install`     | Install package locally                             |
| `make dev`         | Install dev dependencies (pytest, ruff)            |
| `make test`        | Run tests from `tests/`                             |
| `make lint`        | Run linter using `ruff`                             |
| `make run`         | Run both extractors (job application and invoice)  |
| `make run-custom`  | Run the custom prompt/example extractor             |
| `make clean`       | Remove `__pycache__`                                |
| `make docker-build`| Rebuild Docker container                            |
| `make docker-run`  | Run the container using Compose                     |

*Note: Make sure to create a `.env` file with your Gemini API key before running.*

---

## Data Samples

Input files are located in the `data/` directory:

- `job_application_email.txt`
- `invoice.txt`

You can modify these files and rerun the extractor to test different inputs.

---

## Output Example

```bash
  Extracted Entities from Job Application Email:
- Class: person
  Text: Jane Doe
  Attributes: {'role': 'senior software engineer', 'experience_years': '7'}

- Class: emotion
  Text: I am interested in the role at your company
  Attributes: {'tone': 'professional interest'}

- Class: relationship
  Text: contact me at jane.doe@gmail.com or 555-123-4567
  Attributes: {'type': 'contact information'}
```

```bash
  Extracted Entities from Invoice:
- Class: invoice_number
  Text: INV-10123
  Attributes: {}

- Class: recipient
  Text: Acme Corp
  Attributes: {'address': '1234 Market St, San Francisco, CA'}

- Class: item
  Text: Website design: $3000
  Attributes: {'price': '$3000'}
```

---

## Requirements (only if running locally)

- Python 3.11+
- Docker & Docker Compose
- `pip install -r requirements.txt`

---

## License

MIT © 2025 [Sergei Prusov]