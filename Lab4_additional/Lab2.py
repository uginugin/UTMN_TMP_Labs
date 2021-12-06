import tree

import random
import string
import hashlib
import time
import random


global FILENAME
FILENAME = '/opt/result.txt'


def generate_random_string(length = 12):
    letters = string.ascii_letters+string.punctuation
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def gethash(s):
   return (int(hashlib.md5(s.encode('utf-8')).hexdigest(), 16)%10**8)#генерируем md5-хэш строки и отрезаем хвостик


def tree_search_timings(t, hashes): 
    for hash in hashes:
        t.search(t.get_root, hash)


def file_search_timings(hashes):
    f = open(FILENAME).readlines()
    for i in hashes:
        for line in f:
            if str(i) in line:
                break


def main():
    t = tree.Tree()
    hashes = []#массив всех хэшей
    search_hashes = []#массив хэшей, которые будем искать

    with open(FILENAME, 'w') as f:
        for i in range(10000):
            tmp_string =  generate_random_string()
            tmp_hash = gethash(tmp_string)
            hashes.append(tmp_hash)
            t.add(tmp_hash, i)
            f.write(tmp_string + " - " + str(tmp_hash) + '\n')
        
        for i in range(1000):
            search_hashes.append(random.choice(hashes))#заполняем массив поисков

    print(f"Ищем {len(search_hashes)} хешей из файла")
    start_time = time.process_time()
    file_search_timings(search_hashes)
    print(f"Нашли все за {time.process_time()-start_time}\n")


    print(f"Ищем {len(search_hashes)} хешей из дерева")
    start_time = time.process_time()
    tree_search_timings(t, search_hashes)
    print(f"Нашли все за {time.process_time()-start_time}")

if __name__ == '__main__':
    main()
