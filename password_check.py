def check_password(password, lens):
    verify = [False, False]
    if password[0].isdigit():
        return 0
    if lens <= 4:
        return 0
    if "/" in password or " " in password:
        return 0
    for i in password:
        if i.isdigit():
            verify[0] = True
        if i >= "A" and i <= "Z":
            verify[1] = True
    if all(verify) is True:
        return 1
    else:
        return 0


print(check_password("a987S ", 6))
