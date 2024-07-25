import sys

from hello_world.bleat import make_bleat


def main() -> int:
    make_bleat(2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
