import string
from collections import Counter

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
    
def get_top10_words(text, top_n=10):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    return Counter(words).most_common(top_n)

def save_results(data, output_filepath):
    with open(output_filepath, 'w', encoding='utf-8') as f:
        for word, count in data:
            f.write(f"{word}-{count}\n")

def main():
    """Основна логіка виконання програми."""
    input_file = "input.txt"   
    output_file = "output.txt" 
    content = read_file(input_file)
    top_words = get_top10_words(content)
    save_results(top_words, output_file) 
    print(f"10 найпопулярніших слів записано в {output_file}")

if __name__ == "__main__":
    main()