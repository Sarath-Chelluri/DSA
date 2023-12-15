import re


def getGetResponces(valid_auth_tokens, requests):
    res = []
    name = []
    for j, i in enumerate(requests):
        name.append(re.split(r"&|(\w+)-|=", i[1]))
        if name[j][2] in valid_auth_tokens:
            if i[0] == "GET":
                res.append(f"VALID,{name[j][5]},{name[j][6]}")
            else:
                if "csrf" in i[1]:
                    if len(name[j][6]) >= 8:
                        res.append(f"VALID,{name[j][8]},{name[j][10]}")
                else:
                    res.append("INVALID")
        else:
            res.append("INVALID")
    return res


print(
    getGetResponces(
        valid_auth_tokens=["ah37j2ha483u", "safh34ywb0p5", "ba34wyi81902"],
        requests=[
            ["GET", "https://example.com/?token=347sd6yk8iu2&name-alex"],
            ["GET", "https://example.com/?token=safh34ywb0p5&name-sam"],
            ["POST", "https://example.com/?token=safh34ywb0p5&name=alex"],
            [
                "POST",
                "https://example.com/?token-safh34ywb0p5&csrf-ak2sh32dy&name=chris",
            ],
        ],
    )
)
