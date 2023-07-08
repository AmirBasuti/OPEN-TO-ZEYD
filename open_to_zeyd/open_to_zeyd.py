import sys
from PIL import Image, ImageOps, ImageDraw, ImageFont


def main():
    file_name_input, file_name_output = sys_input()
    try:
        with Image.open("open_to_zeydV2-removebg-preview.png") as circule:
            with Image.open(file_name_input) as person:
                circule = ImageOps.fit(circule , (person.size))
                person.paste(circule , circule)
                person.save(file_name_output)

    except FileNotFoundError:
        sys.exit(f"Input does not exist")


def sys_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        if sys.argv[1:][0][-3:].lower() == sys.argv[1:][1][-3:].lower():
            match sys.argv[1:][1][-3:].lower():
                case "png" | "jpeg" | "jpg":
                    pass
                case _:
                    sys.exit("Invalid output")
            return (sys.argv[1:][0], sys.argv[1:][1])
        else:
            sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
