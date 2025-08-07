import os
import textwrap
from dotenv import load_dotenv
import langextract as lx

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Prompt for invoices
invoice_prompt = textwrap.dedent("""\
Extract invoice number, date, recipient, itemized services, total amount due, and due date from the document.
Use exact text spans — do not infer or reword.
Group line items into a list with description and price.
""")

# Example for invoice extraction
invoice_example = lx.data.ExampleData(
    text=(
        "Invoice #INV-10123\nDate: August 5, 2025\n\n"
        "Bill To:\nAcme Corp\n1234 Market St, San Francisco, CA\n\n"
        "Items:\n- Website design: $3000\n- Hosting (12 months): $240\n\n"
        "Total Due: $3240\nDue Date: August 20, 2025"
    ),
    extractions=[
        lx.data.Extraction(
            extraction_class="invoice_number",
            extraction_text="INV-10123",
            attributes={}
        ),
        lx.data.Extraction(
            extraction_class="date",
            extraction_text="August 5, 2025",
            attributes={"type": "issue_date"}
        ),
        lx.data.Extraction(
            extraction_class="recipient",
            extraction_text="Acme Corp",
            attributes={"address": "1234 Market St, San Francisco, CA"}
        ),
        lx.data.Extraction(
            extraction_class="item",
            extraction_text="Website design: $3000",
            attributes={"price": "$3000"}
        ),
        lx.data.Extraction(
            extraction_class="item",
            extraction_text="Hosting (12 months): $240",
            attributes={"price": "$240"}
        ),
        lx.data.Extraction(
            extraction_class="total_due",
            extraction_text="$3240",
            attributes={}
        ),
        lx.data.Extraction(
            extraction_class="due_date",
            extraction_text="August 20, 2025",
            attributes={}
        ),
    ]
)

def main():
    # Load actual invoice input
    invoice_path = os.path.join(os.path.dirname(__file__), "..", "data", "invoice.txt")
    with open(invoice_path, "r") as f:
        invoice_text = f.read()

    # Run extraction
    result = lx.extract(
        text_or_documents=invoice_text,
        prompt_description=invoice_prompt,
        examples=[invoice_example],
        model_id="gemini-2.5-pro",
        api_key=api_key,
    )

    # Print output
    print("\n📄 Extracted Entities from Invoice:")
    for item in result.extractions:
        print(f"- Class: {item.extraction_class}")
        print(f"  Text: {item.extraction_text}")
        print(f"  Attributes: {item.attributes}")