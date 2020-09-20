if __name__ == '__main__':
    s = "#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"
    ls = list(s)
    hasAlpha = False
    hasDigits = False
    hasLower = False
    hasUpper = False
    for x in ls:
        if x.isalpha():
            hasAlpha = True
            continue
    for x in ls:
        if x.isdigit():
            hasDigits = True
            continue
    for x in ls:
        if x.islower():
            hasLower = True
            continue
    for x in ls:
        if x.isupper():
            hasUpper = True
            continue
    print(hasAlpha | hasDigits)
    print(hasAlpha)
    print(hasDigits)
    print(hasLower)
    print(hasUpper)
