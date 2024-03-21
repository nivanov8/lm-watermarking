from datasets import load_dataset


def main():
    realnewslike = load_dataset("allenai/c4", "realnewslike", streaming=True)
    dataset = realnewslike["train"]
    for example in dataset:
        print(example)
        break



# --------------------------training split
# not watermarked
# watermarked
# adversarial 
    

if __name__ == "__main__":
    main()