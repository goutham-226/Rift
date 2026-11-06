"""
Command line entry point for Rift

everything is left empty intentionally
agentic loop will be added later.
"""
from pathlib import Path
from typing import Annotated

import typer
from rich import print

# init Typer application
# --help is automatically added to the CLI
app = typer.Typer(help="Rift CLI", no_args_is_help=True)


@app.callback()
def main() -> None:
    """
    Rift CLI 
    Intentionaly left empty for now, 
    will be filled with agentic loop later.
    """
    pass

def run_cli(
        task: Annotated[str, typer.Argument(help="Task to run")],
        repo: Annotated[Path, 
                        typer.Option(
                                "--repo",
                                help="Path to the repository Rift should work on.",
                                exists=True,
                                file_okay=False,
                                dir_okay=True,
                                resolve_path=True,
                      ),],
) -> None:
    """
    Run the Rift CLI with the specified task and repository path.

    Args:
        task (str): The task to run.
        repo (Path): The path to the repository Rift should work on.
    """
    print(f"Running task: {task} in repository: {repo}")

if __name__ == "__main__":
    app()
    