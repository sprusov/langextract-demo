import langextract_demo.extractor_job
import langextract_demo.extractor_invoice

def main():
    print("=== Job Application Extraction ===")
    langextract_demo.extractor_job.main()
    print("\n=== Invoice Extraction ===")
    langextract_demo.extractor_invoice.main()

if __name__ == "__main__":
    main()