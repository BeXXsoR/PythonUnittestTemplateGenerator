"""Application to create a unittest template file for a given python file."""

# ----- Imports --------
import argparse
import re
import os

# ----- Constants ------
REGEX_PATTERNS = {"class": r"^class (([^\s\(]+)([\s\(].*)?):$",
                  "class_method": r"^\s+def (([^\s\(]+)\(.*):$",
                  "global_method": r"^def (([^\s\(]+)\(.*):$",}
NEW_LINE = "\n"


# ----- Methods --------
def create_setup_and_tear_down(tab: str) -> str:
    """Crate the setup and tear down methods."""
    trg_text = tab + "def setUp(self) -> None:" + NEW_LINE + tab + tab + "pass" + NEW_LINE * 2
    trg_text += tab + "def tearDown(self) -> None:" + NEW_LINE + tab + tab + "pass" + NEW_LINE * 2
    return trg_text


def create_method_texts(tab: str, start: str, groups: list[str]) -> str:
    """Create the methods texts"""
    trg_text = start + f"def test_{groups[1].strip('_')}(self):" + NEW_LINE
    trg_text += start + tab + f'"""Test the method {groups[0]}"""' + NEW_LINE
    trg_text += start + tab + "self.fail()" + NEW_LINE
    return trg_text


def create_global_methods_class(tab: str) -> str:
    """Create the text for the test class of the global methods."""
    return NEW_LINE + "class TestGlobalMethods(unittest.TestCase):" + NEW_LINE + tab + '"""Test case for all global methods."""' + NEW_LINE


def parse_cmd_line_args() -> argparse.Namespace:
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(description='Generate a unittest template file.')
    parser.add_argument('source', metavar='S', type=str, help="Specify the source python filename.")
    parser.add_argument('target', metavar='T', type=str, help="Specify the target filename for the unittest file.")
    parser.add_argument('-ts', '--tab_size', metavar='TS', type=int, default=4, help="Specify the number of spaces for a tab in the target file. Use 0 to use the tab character.")
    return parser.parse_args()


# ----- Main script ----
if __name__ == "__main__":
    args = parse_cmd_line_args()
    tab = " " * args.tab_size if args.tab_size > 0 else "\t"
    header = f'"""Unittest for the file {os.path.split(args.source)[1]}."""' + NEW_LINE * 2 + "import unittest" + NEW_LINE * 2
    global_methods_text = ""
    class_text = ""
    regex_objects = {key: re.compile(patt) for key, patt in REGEX_PATTERNS.items()}
    need_setup_and_tear_down = False
    try:
        with open(args.source, "r") as f:
            for line in f:
                if need_setup_and_tear_down:
                    class_text += create_setup_and_tear_down(tab)
                    need_setup_and_tear_down = False
                for key, regex in regex_objects.items():
                    if match := regex.match(line):
                        groups = match.groups()
                        if key == "class":
                            class_text += NEW_LINE + f"class Test{groups[1]}(unittest.TestCase):" + NEW_LINE
                            class_text += tab + f'"""Test case for all methods of the class {groups[0]}."""' + NEW_LINE
                            need_setup_and_tear_down = True
                        elif key == "class_method":
                            class_text += create_method_texts(tab, tab, groups) + NEW_LINE
                        elif key == "global_method":
                            if global_methods_text == "":
                                global_methods_text = create_global_methods_class(tab)
                            global_methods_text += create_method_texts(tab, tab, groups) + NEW_LINE
        with open(args.target, "w") as f:
            f.write(header + global_methods_text + class_text)
        print("Unittest file successfully created.")
    except FileNotFoundError as exc:
        print(f"Can't open file {exc.filename}.")
