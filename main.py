import sys

print("Provide a subdomain file path (Not URls) and Output filename. \nExample: \npython3 main.py input.txt output.txt")
try:
    input_file = sys.argv[1]
    try:
        output_file = sys.argv[2]
    except:
        output_file = "wordlist.txt"
except Exception as error:
    print("Input file name not provided!")


def gen_words(domain):
    word_lst = []
    extenstions = [".zip",".tar",".gz",".bz2",".xz",".7z",".rar",".tar.gz",
                  ".tgz",".tar.bz2",".tbz2",".tar.xz",".config",".sql",".txt"]
    for ext in extenstions:
        try:
            sub_lst = domain.split(".")
            t_1 = f"{domain}{ext}"
            t_2 = f"{domain.replace('.','_')}{ext}"
            t_3 = f"{domain.replace('.','-')}{ext}"
            word_lst += [t_1,t_2,t_3]
        except Exception as error:
            print(f"Error: {error}")
    word_lsts = list(set(word_lst))
    # print(len(word_lsts), len(word_lst))
    return word_lsts


def write_file(lst,file_name="wordlist.txt"):
    try:
        with open(file_name,"a") as writer:
            for line in lst:
                writer.write(f"{line}\n")
    except Exception as error:
        print(f"Error: {error}")

print(f"[+]  Generating Wordlist................")

try:
    file = open(input_file)
except Exception as error:
    print(f"Error: {error}")

for sub in file:
    sub = sub.strip("\n")
    print(f"[+] Done: {sub}")
    words = gen_words(sub)
    set_words = list(set(words))
    write_file(set_words,output_file)

