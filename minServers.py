def getMinServers(expected_load, n, server):
    output = []
    if max(server) == expected_load or min(server) == expected_load:
        return 1
    while expected_load != sum(output) and expected_load != sum(server):
        if server == []:
            return -1
        output.append(min(server))
        server.remove(min(server))
    if sum(server) == expected_load:
        return len(server)
    return len(output)


print(getMinServers(7, 5, [1, 7, 2, 5]))
