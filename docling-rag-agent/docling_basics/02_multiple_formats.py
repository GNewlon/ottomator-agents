"""
Multi-Format Document Processing with Docling
==============================================
"""

from docling.document_converter import DocumentConverter
from pathlib import Path
import shutil

def process_document(file_path: str, converter: DocumentConverter, output_dir: Path) -> dict:
    try:
        print(f"\n📄 Processing: {Path(file_path).name}")

        result = converter.convert(file_path)
        markdown = result.document.export_to_markdown()

        doc_info = {
            'file': Path(file_path).name,
            'format': Path(file_path).suffix,
            'status': 'Success',
            'markdown_length': len(markdown),
            'preview': markdown[:200].replace('\n', ' ')
        }

        output_file = output_dir / f"{Path(file_path).stem}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)

        doc_info['output_file'] = str(output_file)

        print(f"   ✓ Converted successfully")
        print(f"   ✓ Output: {output_file}")

        return doc_info

    except Exception as e:
        print(f"   ✗ Error: {e}")
        return {
            'file': Path(file_path).name,
            'format': Path(file_path).suffix,
            'status': 'Failed',
            'error': str(e)
        }

def main():
    print("=" * 60)
    print("Multi-Format Document Processing with Docling")
    print("=" * 60)

    input_dir = Path(r"C:\Users\GrahamNewlon\OneDrive - newlon.io\Documents\AI Project\Docling\Input")
    output_dir = Path(r"C:\Users\GrahamNewlon\OneDrive - newlon.io\Documents\AI Project\Docling\Output")
    processed_dir = Path(r"C:\Users\GrahamNewlon\OneDrive - newlon.io\Documents\AI Project\Docling\Processed Files")
    failed_dir = Path(r"C:\Users\GrahamNewlon\OneDrive - newlon.io\Documents\AI Project\Docling\Failed Files")

    for d in [output_dir, processed_dir, failed_dir]:
        d.mkdir(parents=True, exist_ok=True)

    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    documents = [str(f) for f in input_dir.iterdir() if f.is_file()]

    if not documents:
        print("No files found in input directory.")
        return

    converter = DocumentConverter()

    results = []
    for doc_path in documents:
        result = process_document(doc_path, converter, output_dir)
        results.append(result)

        src = Path(doc_path)
        if result['status'] == 'Success':
            shutil.move(str(src), processed_dir / src.name)
        else:
            shutil.move(str(src), failed_dir / src.name)

    print("\n" + "=" * 60)
    print("CONVERSION SUMMARY")
    print("=" * 60)

    for result in results:
        status_icon = "✓" if result['status'] == 'Success' else "✗"
        print(f"{status_icon} {result['file']} ({result['format']})")
        if result['status'] == 'Success':
            print(f"   Length: {result['markdown_length']} chars")
            print(f"   Preview: {result['preview']}...")
        else:
            print(f"   Error: {result.get('error', 'Unknown')}")
        print()

    success_count = sum(1 for r in results if r['status'] == 'Success')
    print(f"Converted {success_count}/{len(results)} documents successfully")

if __name__ == "__main__":
    main()
