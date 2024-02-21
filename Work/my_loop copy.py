def while_loop():
    lang_list = ["Python", "Javascript", "PHP", "Rust", "Solidity", "Assembly"]
    counter = 0
    while (counter < len(lang_list)):
        print(lang_list[counter])
        counter += 1

def for_loop():
    lang_list = ["Python", "Javascript", "PHP", "Rust", "Solidity", "Assembly"]
    for lang in lang_list:
        print(lang, end=" ")

def my_msg(loop_type) :
    print("#")
    print("Running",loop_type,"loop")
    print("#")

def main():
    my_msg("for")
    for_loop()
    my_msg("while")
    while_loop()

if __name__ == "__main__":
    main()