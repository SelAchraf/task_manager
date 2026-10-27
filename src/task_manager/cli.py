import argparse

def build_parser() -> argparse.ArgumentParser: ...   # subcommands: add, list, update, done, delete
def main(argv: list[str] | None = None) -> int: ...  # returns 0 on success, 1 on error
