from search import *

def split_info(info):
    last_char = None
    info_norm = []
    for curr_char in info:
        if curr_char.isalnum():
            if last_char.isalnum():
                info_norm[-1] += curr_char
            else :
                info_norm.append(curr_char)
        elif not curr_char.isspace():
            info_norm.append(curr_char)
        last_char = curr_char
    return info_norm


def change_form(info_norm):
    i = 0
    f_pare = 0
    map_info = []
    while f_pare < 3:
        curr_char = info_norm[i]
        if curr_char == '(':
            f_pare += 1
        i += 1
    i -= 1
    pare_pair = 0
    while i < len(info_norm):
        curr_char = info_norm[i]
        if curr_char == '(':
            pare_pair += 1
            curr_content = []
            while pare_pair != 0:
                i += 1
                curr_char = info_norm[i]
                if curr_char == ')':
                    pare_pair -= 1
                if pare_pair != 0:
                    curr_content.append(int(curr_char))
            map_info.append(curr_content)
        if curr_char == ')' and info_norm[i+1] == ')':
            break
        i += 1
    return map_info


def linear_distance(x, y):
    dis = int(math.sqrt(x**2+y**2))
    return dis


def build_map(data):
    ug = UndirectedGraph()
    ug.locations = {}
    loc = []
    for i in data:
        p1 = str(i[1]) + "," + str(i[2])
        p2 = str(i[3]) + "," + str(i[4])
        if p1 not in loc:
            loc.append(p1)
        if p2 not in loc:
            loc.append(p2)
    for i in loc:
        ug.locations[i] = (int(i.split(",", 3)[0]), int(i.split(",", 3)[1]))

    for i in data:
        distance = linear_distance((i[3] - i[1]), (i[4] - i[2]))
        if i[0] == 1:
            ug.connect1(str(i[1]) + "," + str(i[2]), str(i[3]) + "," + str(i[4]), distance)
        if i[0] == 2:
            ug.connect(str(i[1]) + "," + str(i[2]), str(i[3]) + "," + str(i[4]), distance)
    return ug


def main():
    filename = 'mapinfo.txt'
    with open(filename) as f_obj:
        contents = f_obj.read()
    res = split_info(contents)
    info = change_form(res)
    mnmap = build_map(info)

    # start_x = input("Starting point x coordinates:")
    # start_y = input("Starting point y coordinates:")
    # end_x = input("Destination x coordinates:")
    # end_y = input("Destination y coordinates:")
    #
    # start_p = str(start_x) + ',' + str(start_y)
    # end_p = str(end_x) + ',' + str(end_y)
    # np = GraphProblem(start_p, end_p, mnmap)
    np = GraphProblem('2321,8977', '2460,6686', mnmap)
    print("a*:")
    print(astar_search(np).path_cost)
    #list = astar_search(np).
    print(list)
    print("\nDijkstra:")
    print(djikstra_search(np).path_cost)
    


if __name__ == '__main__':
    main()

