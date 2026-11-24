import os

JOKE = "My cat fell in the bathtub once. She has held it against me for four years, which is fair \u2014 I held the camera."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
