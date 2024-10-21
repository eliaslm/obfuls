from IPython.display import Markdown, display

def display_src(filepath: str) -> None:
    """Display Python source code as markdown."""
    with open(filepath, 'r') as src_file:
        src = src_file.read()

    display(Markdown(f"```python\n{src}\n```"))
