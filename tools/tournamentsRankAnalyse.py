import json
import matplotlib.pyplot as plt

def load_data(rank_dict):
    cur = 0
    while cur <= 50:
        with open(f'C:/Users/TU/Desktop/soroya20-30/{cur}.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                res = json.loads(line)
                if res['name'] in rank_dict:
                    rank_dict[res['name']].append(res['points'])
                # print(res)
            f.close()
        cur += 1
        for rank in rank_dict:
            if len(rank_dict[rank]) < cur:
                rank_dict[rank].append("0P")


def create_dict():
    rank_dict = {}
    with open(f'C:/Users/TU/Desktop/soroya20-30/{50}.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line_dict = json.loads(line)
            rank_dict[line_dict['name']] = []
        f.close()
    return rank_dict

def delete_p(rank_dict):
    for rank in rank_dict:
        points_list = rank_dict[rank]
        cur = 0
        while cur < len(points_list):
            points_list[cur] = points_list[cur].replace("P", "")
            points_list[cur] = int(points_list[cur] )
            cur += 1

    print(rank_dict)

def draw_plot(rank_dict):
    plt.xlabel("Times")

    plt.ylabel("Points")
    for rank in rank_dict:
        if rank == 'player20-30':
            plt.plot(rank_dict[rank], color='red', linestyle='dashed', marker='+',

                     markerfacecolor='blue', markersize=5)
        else:
            plt.plot(rank_dict[rank])

    plt.show()


if __name__ == '__main__':
    rank_data = create_dict()
    load_data(rank_data)
    delete_p(rank_data)
    draw_plot(rank_data)
