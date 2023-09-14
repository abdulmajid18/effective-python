from exception_flow import never_returns


def handler() -> None:
    try:
        never_returns()
        print("Never executed")
    except Exception as ex:
        print(f"I caught an exception: {ex!r}")
    print("Executed after the exception")


if __name__ == "__main__":
    handler()