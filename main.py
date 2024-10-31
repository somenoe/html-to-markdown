from pathlib import Path
from typing import Iterator

from logger.config import setup_logger
from markdownify import markdownify as md


class HtmlToMarkdownConverter:

    def __init__(self, input_dir: Path = Path("data/input"), output_dir: Path = Path("data/output")) -> None:
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.logger = setup_logger(__name__)
        self.logger.info(f"Initialized converter with input_dir: {
                         input_dir}, output_dir: {output_dir}")

    def get_input_items(self) -> Iterator[Path]:
        """Get all folders and HTML files from the input directory."""
        self.logger.debug(f"Scanning for items in {self.input_dir}")
        items = [
            item for item in self.input_dir.iterdir()
            if item.is_dir() or (item.is_file() and item.suffix.lower() == '.html')
        ]
        self.logger.info(f"Found {len(items)} items to process")
        return iter(items)

    def process_html_file(self, file_path: Path, output_folder: Path) -> None:
        """Convert a single HTML file to markdown and save it."""
        try:
            # Only process .html files
            if file_path.suffix.lower() != '.html':
                self.logger.debug(f"Skipping non-HTML file: {file_path}")
                return

            # Read and convert HTML content
            html_content = file_path.read_text(encoding='utf-8')
            markdown_content = md(html_content, strip=[
                                  'title', 'button', 'a', 'img'])

            # Write markdown content
            output_file = output_folder / f"{file_path.stem}.md"
            output_file.write_text(markdown_content, encoding='utf-8')
            self.logger.info(f"Converted {file_path.name} -> {
                             output_file.name}")

        except Exception as e:
            self.logger.error(f"Error processing file {
                              file_path}: {str(e)}", exc_info=True)

    def convert(self) -> None:
        """Main conversion process."""
        self.logger.info("="*50)
        self.logger.info("Starting HTML to Markdown conversion process")
        self.logger.info("="*50)

        try:
            # Process each item (folder or file) in input directory
            for item in self.get_input_items():
                if item.is_dir():
                    # Process folder
                    folder_name = item.name
                    self.logger.info("-"*30)
                    self.logger.info(f"Processing folder: {folder_name}")
                    self.logger.info("-"*30)

                    # Create output folder if it doesn't exist
                    output_folder = self.output_dir / folder_name
                    if not output_folder.exists():
                        self.logger.debug(
                            f"Creating output folder: {output_folder}")
                        output_folder.mkdir(parents=True, exist_ok=True)
                    else:
                        self.logger.debug(
                            f"Output folder already exists: {output_folder}")

                    # Process each file in the folder
                    files = list(item.iterdir())
                    total_files = len(files)
                    processed_files = 0
                    html_files = 0

                    for file_path in files:
                        if file_path.is_file():
                            processed_files += 1
                            if file_path.suffix.lower() == '.html':
                                html_files += 1
                            self.process_html_file(file_path, output_folder)
                            self.logger.debug(
                                f"Progress: {processed_files}/{total_files} files processed")

                    self.logger.info(
                        f"Folder summary for {folder_name}: "
                        f"Total files processed: {processed_files}, "
                        f"HTML files converted: {html_files}"
                    )
                else:
                    # Process single HTML file
                    self.logger.info("-"*30)
                    self.logger.info(f"Processing file: {item.name}")
                    self.logger.info("-"*30)
                    self.process_html_file(item, self.output_dir)

            self.logger.info("="*50)
            self.logger.info("Conversion process completed successfully")
            self.logger.info("="*50)

        except Exception as e:
            self.logger.error("="*50)
            self.logger.error("Conversion process failed!")
            self.logger.error(f"Error: {str(e)}")
            self.logger.error("="*50, exc_info=True)
            raise


def main() -> None:
    INPUT_DIR = Path("data/input")
    OUTPUT_DIR = Path("data/output")

    converter = HtmlToMarkdownConverter(
        input_dir=INPUT_DIR,
        output_dir=OUTPUT_DIR
    )
    converter.convert()


if __name__ == "__main__":
    main()
