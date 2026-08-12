def read_resume(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    return content

# This stuff means, only run the stuff below if this file is directly being run from the terminal not when it is being imported
if __name__ == "__main__":
    print(read_resume("resume.tex"))