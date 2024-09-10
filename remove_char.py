def remove_char(str: str, c: str) -> str:
    if len(c) > 1:
        print("Please enter a simple character e.g 'a', '$' ...")
        return None
    return str.replace(c, '')


if __name__ == '__main__':
    str = input("Enter a message: ")
    c = input("Enter a single character to remove from the message: ")
    new = remove_char(str=str, c=c)
    if new is not None:
        print(f"Old Message: {str}")
        print(f"New Message: {new}")