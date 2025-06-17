import argparse
import re
import shutil
from pathlib import Path

from loguru import logger


class FactorioWikiTool:
    def __init__(self, template_path: Path, language_code: str):
        self.template_path = template_path
        self.template_dict = self.load_template()
        self.language_code = language_code

    def load_template(self) -> dict[str, str]:
        with self.template_path.open() as f:
            lines = f.readlines()

        # This regex matches lines of the form |keyword=translated text
        pattern = re.compile(r"^\|\s*(.*?)\s*=\s*(.+)$")

        template_dict = {}

        for line in lines:
            match = pattern.match(line.strip())
            if match is None:
                continue
            key, translated_text = match.groups()
            template_dict[key.strip().lower()] = translated_text.strip()

        return template_dict

    def replace_line_with_template(self, line_index: int, line: str) -> str:
        # This regex matches [[word]] or [[word|display text]]
        pattern = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")

        def replace_match(match):
            matched_word = match.group(1).strip()
            matched_key = matched_word.lower()
            if matched_key in self.template_dict:
                replaced_link = f"[[{matched_word}/{self.language_code}|{self.template_dict[matched_key]}]]"

                # Check if the display text is provided
                # If has display text, use WARNING level
                level = "INFO" if match.group(2) is None else "WARNING"

                logger.log(
                    level, f"Line {line_index + 1}:      Original: {match.group(0)}"
                )
                logger.log(
                    level, f"Line {line_index + 1}: Replaced with: {replaced_link}"
                )
                return replaced_link

        return pattern.sub(replace_match, line)

    def replace_lines_with_template(self, lines: list[str]) -> list[str]:
        return [
            self.replace_line_with_template(i, line) for i, line in enumerate(lines)
        ]

    def replace_page_with_template(self, page: Path):
        with page.open("r") as f:
            lines = f.readlines()

        replaced_lines = self.replace_lines_with_template(lines)

        with page.open("w") as f:
            f.writelines(replaced_lines)

    def backup_page(self, page: Path):
        page_backup = page.with_suffix(".bak")
        shutil.copy(page, page_backup)


def parse_args():
    parser = argparse.ArgumentParser(description="Factorio Wiki Translation Tool")
    parser.add_argument("template", type=Path, help="Path to the template file")
    parser.add_argument(
        "language_code", type=str, help='Language code for translation (e.g., "ja")'
    )
    parser.add_argument("page", type=Path, help="Path to the file to translate")
    return parser.parse_args()


def main():
    args = parse_args()

    tool = FactorioWikiTool(args.template, args.language_code)

    tool.backup_page(args.page)
    tool.replace_page_with_template(args.page)


if __name__ == "__main__":
    main()
