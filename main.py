import typer 
import time
from logger import log_system_stats

app = typer.Typer()

@app.command()
def logCurrentStats():
    log_system_stats()
    print("System stats logged")

@app.command()
def watch(interval: int = 1):
    print(f"Logging system stats...")
    while (True):
        log_system_stats() 
        time.sleep(interval)
if __name__ == "__main__":
    app()