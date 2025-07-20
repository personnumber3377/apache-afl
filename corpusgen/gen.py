import os
import sys



def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_binary_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    out_dir = "out"

    # Make sure output directory exists
    os.makedirs(out_dir, exist_ok=True)

    with open(input_path, "rb") as f:
        data = f.read()

    original = b"/a"
    if original not in data:
        print("Warning: '/a' not found in the input file.")

    # for c in range(ord("b"), ord("z") + 1):

    strings = os.listdir("/home/oof/apache-afl/install_dir/htdocs/")
    for c in strings:
        replaced = data.replace(original, b"/" + c.encode("ascii"))
        out_path = os.path.join(out_dir, f"file_"+c+".bin")
        with open(out_path, "wb") as out_file:
            out_file.write(replaced)
        print(f"Wrote: {out_path}")

if __name__ == "__main__":
    main()