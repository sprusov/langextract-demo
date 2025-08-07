import os
import textwrap
from dotenv import load_dotenv
import langextract as lx

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Custom prompt for job applications
prompt = textwrap.dedent("""\
Extract applicant details, emotional tone, and references to company or job role in order of appearance.
Use exact text from the document — do not rephrase.
Add relevant attributes like years of experience, skills, tone, or type of interest.
Avoid overlapping or paraphrased entities.""")

# High-quality example
examples = [
    lx.data.ExampleData(
        text=(
            "I am Jane Doe, a senior software engineer with 7 years of experience "
            "in backend development using Python and Java. My expected salary is $130,000. "
            "You can contact me at jane.doe@gmail.com or 555-123-4567."
        ),
        extractions=[
            lx.data.Extraction(
                extraction_class="person",
                extraction_text="Jane Doe",
                attributes={"role": "senior software engineer", "experience_years": 7}
            ),
            lx.data.Extraction(
                extraction_class="emotion",
                extraction_text="I am interested in the role",
                attributes={"tone": "professional interest"}
            ),
            lx.data.Extraction(
                extraction_class="relationship",
                extraction_text="contact me at jane.doe@gmail.com or 555-123-4567",
                attributes={"type": "contact information"}
            ),
        ]
    )
]

def main():
    # Load actual input
    job_app_path = os.path.join(os.path.dirname(__file__), "..", "data", "job_application_email.txt")
    with open(job_app_path, "r") as f:
        input_text = f.read()

    # Run extraction directly with lx.extract()
    result = lx.extract(
        text_or_documents=input_text,
        prompt_description=prompt,
        examples=examples,
        model_id="gemini-2.5-pro",
        api_key=api_key,
    )

    # Print output
    print("\n📄 Extracted Entities from Job Application Email:")
    for item in result.extractions:
        print(f"- Class: {item.extraction_class}")
        print(f"  Text: {item.extraction_text}")
        print(f"  Attributes: {item.attributes}")