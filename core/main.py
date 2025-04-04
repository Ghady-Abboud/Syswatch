import typer 
import time
from logger import log_system_stats

app = typer.Typer()

@app.command()
def monitor_resources(interval: int = 1):
    while (True):
        log_system_stats() 
        time.sleep(interval)
if __name__ == "__main__":
    app()