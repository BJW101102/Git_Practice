class HelloMessage():
        def __init__(self, msg: str):
            self._msg = msg

        def print_message(self) -> None:
              """Prints Hello, {user_msg}"""
              print(f'Hello, {self._msg}')

if __name__ == "__main__":
    h = HelloMessage(msg='World!')
    h.print_message()