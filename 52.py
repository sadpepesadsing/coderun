def main():
    synonyms = {}
    for i in range(int(input())):
        string = input()
        synonyms[string.split()[0]] = string.split()[1]
        synonyms[string.split()[1]] = string.split()[0]

    print(synonyms[input()])

if __name__ == '__main__':
    main()
