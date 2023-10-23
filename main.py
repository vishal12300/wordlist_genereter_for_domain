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
    extenstions = [".zip",".tar",".gz",".bz2",".xz",".7z",".rar",".cab",".tar.gz",
                  ".tgz",".tar.bz2",".tbz2",".tar.xz",".txz",".zipx",".ace",".arj",
                  ".lzh",".sit",".z",".cbr",".cbz",".jar",".config",".sql",".txt"]
    for ext in extenstions:
        try:
            sub_lst = domain.split(".")
            t_1 = f"{domain}{ext}"
            t_2 = f"{domain.upper()}{ext}"
            t_3 = f"{domain.replace('.','_')}{ext}"
            t_4 = f"{domain.replace('.','-')}{ext}"
            for sub in sub_lst:
                t_5 = f"{sub}{ext}"
                t_6 = f"{sub.upper()}{ext}"
                t_7 = f"{sub.replace('.', '_')}{ext}"
                t_8 = f"{sub.replace('.', '-')}{ext}"
                word_lst += [t_1,t_2,t_3,t_4,t_5,t_6,t_7,t_8]
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

