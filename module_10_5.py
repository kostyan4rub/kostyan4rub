from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start = datetime.now()
for f in file_list:
    read_info(f)
end = datetime.now()
print(end - start)


# if __name__ == '__main__':
#     with multiprocessing.Pool(processes=4) as pool:
#         start = datetime.now()
#         pool.map(read_info, file_list)
#     end = datetime.now()
#     print(end-start)