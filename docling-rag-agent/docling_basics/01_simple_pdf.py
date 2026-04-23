"""
Simple PDF Parsing with Docling - Dynamic Input Version
======================================================

Processes ALL supported files found in the input directory.
No hardcoded filenames.
"""

from pathlib import Path
from docling.document_converter import DocumentConverter

def main():
    input_dir = Path(r"C:\Users\GrahamNewlon\OneDrive - newlon.io\Documents\AI Project\Docling\Input")
    output_dir = Path(r"C:\Users\GrahamNewlon\OneDrive - newlon.io\Documents\AI Project\Docling\Output")

    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Dynamic Document Processing with Docling")
    print("=" * 60)
    print(f"Input Directory: {input_dir}\n")

    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    files = [f for f in input_dir.iterdir() if f.is_file()]

    if not files:
        print("No files found in input directory.")
        return

    converter = DocumentConverter()

    for file_path in files:
        print(f"\nProcessing: {file_path.name}")

        try:
            result = converter.convert(str(file_path))
            markdown = result.document.export_to_markdown()

            output_file = output_dir / f"{file_path.stem}.md"

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(markdown)

            print(f"✓ Success → {output_file}")
            print(f"✓ Length: {len(markdown)} chars")

        except Exception as e:
            print(f"✗ Failed: {e}")

    print("\nProcessing complete.")

if __name__ == "__main__":
    main()
