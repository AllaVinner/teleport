from pathlib import Path
import sys
import click
from teleport.clear import clear
from teleport.exceptions import TeleportException
from teleport.add import WriteMode, add
from teleport.init import init
from teleport.get import get
from teleport.list_destinations import list_destinations
from teleport.shell import shell
from teleport.remove import remove


def cli_error_handler(f):
    def inner(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except TeleportException as e:
            click.echo(e.message)
            sys.exit(1)

    return inner


@click.group()
def cli():
    pass


@click.command("get")
@click.argument("name", type=str, required=True)
@cli_error_handler
def get_dest(name: str):
    res = get(name)
    click.echo(res)


@click.command("remove")
@click.argument("name", type=str, required=True)
@cli_error_handler
def remove_dest(name: str):
    remove(name)


@click.command("init")
@click.argument("mode", required=False)
@cli_error_handler
def init_project(mode) -> None:
    init()


@click.command("add")
@click.argument("name", type=str, required=True)
@click.argument("path", type=click.Path(path_type=Path), required=True)
@click.option("-m", "--mode", type=click.Choice(WriteMode), default=WriteMode.ensure)
@cli_error_handler
def add_destination(name: str, path: Path, mode: WriteMode) -> None:
    add(name, path, write_mode=mode)


@click.command("list")
@click.argument("scope", required=False)
@cli_error_handler
def list_dests(scope: str | None) -> None:
    res = list_destinations()
    max_name = max([len(name) for name in res.keys()])
    msg = "\n".join([f"{name:<{max_name}}: {path}" for name, path in res.items()])
    click.echo(msg)


@click.command("clear")
@cli_error_handler
def clear_config() -> None:
    clear()


@click.command("shell")
@click.argument("scope", required=False)
@cli_error_handler
def shell_command(scope) -> None:
    res = shell()
    click.echo(res)


cli.add_command(get_dest)
cli.add_command(init_project)
cli.add_command(add_destination)
cli.add_command(list_dests)
cli.add_command(shell_command)
cli.add_command(clear_config)
cli.add_command(remove_dest)


def main() -> None:
    cli()
