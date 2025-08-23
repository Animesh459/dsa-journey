
def dubstep_remix(s: str) -> str:
    # Split the string by "WUB"
    words = s.split("WUB")
    # Remove empty strings and join with space
    return " ".join([word for word in words if word])


if __name__ == "__main__":
    remix = input().strip()
    print(dubstep_remix(remix))