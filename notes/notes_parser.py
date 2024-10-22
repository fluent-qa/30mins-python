import os

from jupyter_notebook_parser import JupyterNotebookParser as Parser

PY_MD_CODE_TEMPLATE = """
```python
{CODE}
```
"""


class JupyterNotesComposer:
    def __init__(self, note_path):
        self.note_path = note_path
        self.parsed = Parser(self.note_path)
        self.md_content = []

    def compose_md_files(self):
        cells = self.parsed.get_all_cells()
        for cell in cells:
            if cell["cell_type"] == "code":
                self.md_content.append(
                    PY_MD_CODE_TEMPLATE.format(CODE="".join(cell["source"]))
                )
            if cell["cell_type"] == "markdown":
                self.md_content.append("".join(cell["source"]))
        return self

    def to_md_files(self, md_file_path):
        self.compose_md_files()
        with open(md_file_path, "w") as md_file:
            md_file.writelines(self.md_content)
        return self


def covert_all_notes_to_md(notes_dir: str, md_dir: str):
    notes = os.listdir(notes_dir)
    for note in notes:
        p = JupyterNotesComposer("/".join([notes_dir, note]))
        md_path = "/".join([md_dir, note.replace(".ipynb", ".md")])
        p.to_md_files(md_path)


if __name__ == "__main__":
    covert_all_notes_to_md("./crawler", "../docs/topics")
    # notes = os.listdir("./itermedia")
    # print(notes)
    # for note in notes:
    #     p = JupyterNotesComposer("./itermedia/" + note)
    #     p.to_md_files("../docs/itermedia/" + note.replace(".ipynb", ".md"))
