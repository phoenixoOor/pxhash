import typer
import sys
import json
from pathlib import Path
from typing import Optional, List
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from pxhash.core.analyzer import HashAnalyzer
from pxhash.models import AnalysisResult, BatchResult
from pxhash.logger import logger

app = typer.Typer(help="Phoenix Hash Identification & Analysis Framework")
console = Console()
analyzer = HashAnalyzer()

def display_analysis(result: AnalysisResult):
    """Prints analysis result to console using rich."""
    console.print(Panel(f"[bold blue]Hash:[/bold blue] {result.hash_string}", expand=False))
    
    # Stats Table
    stats_table = Table(show_header=True, header_style="bold magenta")
    stats_table.add_column("Property", style="dim")
    stats_table.add_column("Value")
    
    stats_table.add_row("Length", str(result.length))
    stats_table.add_row("Entropy", f"{result.entropy:.4f}")
    stats_table.add_row("Char Set", result.char_set)
    
    console.print(stats_table)
    
    # Matches Table
    if result.matches:
        match_table = Table(title="Detected Hash Types", show_header=True, header_style="bold green")
        match_table.add_column("Type", style="bold")
        match_table.add_column("Confidence", justify="right")
        match_table.add_column("Category")
        
        for match in result.matches:
            match_table.add_row(
                match.name, 
                f"{match.confidence_score:.2f}",
                match.category
            )
        console.print(match_table)
    else:
        console.print("[yellow]No hash types identified.[/yellow]")
        
    # Recommendations
    if result.recommendations:
        console.print("\n[bold cyan]Recommendations:[/bold cyan]")
        for rec in result.recommendations:
            console.print(f" • {rec}")

@app.command()
def identify(hash_string: str = typer.Argument(..., help="The hash string to identify")):
    """Identify a single hash string."""
    result = analyzer.analyze(hash_string)
    display_analysis(result)

@app.command()
def analyze(
    input_file: Path = typer.Argument(..., help="File containing hashes (one per line)"),
    output_json: Optional[bool] = typer.Option(False, "--json", help="Output results in JSON format")
):
    """Analyze multiple hashes from a file."""
    if not input_file.exists():
        logger.error(f"File not found: {input_file}")
        raise typer.Exit(1)
        
    results = []
    with open(input_file, "r") as f:
        for line in f:
            hash_str = line.strip()
            if hash_str:
                results.append(analyzer.analyze(hash_str))
                
    batch = BatchResult(
        results=results,
        total_processed=len(results),
        summary={} # Could aggregate summary here
    )
    
    if output_json:
        console.print_json(batch.model_dump_json())
    else:
        for res in results:
            display_analysis(res)
            console.print("-" * 40)

@app.command()
def detect():
    """Read hashes from STDIN and identify them."""
    if sys.stdin.isatty():
        console.print("[yellow]Waiting for STDIN... (Ctrl+D to finish)[/yellow]")
    
    for line in sys.stdin:
        hash_str = line.strip()
        if hash_str:
            result = analyzer.analyze(hash_str)
            display_analysis(result)
            console.print("-" * 40)

if __name__ == "__main__":
    app()
