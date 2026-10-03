import click

@click.command()
@click.option("--date", required=True)
def run_pipeline(date):
    click.echo(f"Running Pipeline for {date}")

if __name__ == "__main__":
    run_pipeline()
