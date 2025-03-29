
def process_keyword(keyword, rules):
    lines = rules.splitlines()
    keyword.lower()
    for line in lines:
        rule = line.lower()
        if keyword in rule:
            print(line)