def extract_md(md: str):
    lines = md.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:]
        else:
            raise ValueError("No title found")
