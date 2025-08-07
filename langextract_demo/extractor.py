import os
from dotenv import load_dotenv
from langextract.extractor import LangExtract

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

extractor = LangExtract(model="gemini-pro", api_key=api_key)

def extract_info(text, schema):
    result = extractor.extract(schema=schema, text=text)
    print("🔍 Extracted Info:")
    print(result)

def main():
    email_path = os.path.join(os.path.dirname(__file__), "..", "data", "job_application_email.txt")
    invoice_path = os.path.join(os.path.dirname(__file__), "..", "data", "invoice.txt")

    with open(email_path, "r") as f:
        email_text = f.read()

    email_schema = {
        "name": "string",
        "email": "string",
        "phone": "string",
        "years_experience": "number",
        "skills": "list[string]",
        "expected_salary": "string",
        "joining_time": "string"
    }

    print("\n=== Job Application Email ===")
    extract_info(email_text, email_schema)

    with open(invoice_path, "r") as f:
        invoice_text = f.read()

    invoice_schema = {
        "invoice_number": "string",
        "date": "string",
        "company_name": "string",
        "company_address": "string",
        "items": "list[string]",
        "total_due": "string",
        "due_date": "string"
    }

    print("\n=== Invoice ===")
    extract_info(invoice_text, invoice_schema)

if __name__ == "__main__":
    main()
