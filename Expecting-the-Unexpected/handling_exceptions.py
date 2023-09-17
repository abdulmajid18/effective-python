from exception_flow import never_returns


def handler() -> None:
    try:
        never_returns()
        print("Never executed")
    except Exception as ex:
        print(f"I caught an exception: {ex!r}")
    print("Executed after the exception")


some_exceptions = [ValueError, TypeError, IndexError, None]


def exception_flow(errors):
    for error in errors:
        try:
            print(f"\nRaising {error}")
            if error:
                raise error("An error")
            else:
                print("no exception raised")
        except ValueError:
            print("Caught a ValueError")
        except TypeError:
            print("Caught a TypeError")
        except Exception as e:
            print(f"Caught some other error: {e.__class__.__name__}")
        else:
            print("This code called if there is no exception")
        finally:
            print("This cleanup code is always called")


if __name__ == "__main__":
    # handler()
    exception_flow(some_exceptions)
