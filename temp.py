def count_unique_chars(filename):
    char_count = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                for char in line:
                    
                    char_count[char] = char_count.get(char, 0) + 1

        num_unique_chars = len(char_count)

        print("總共有 {} 個不重複的英文字".format(num_unique_chars))
        print("每個英文字出現次數為:")
        for char, count in char_count.items():
            print("{}: {}".format(char, count))

        return num_unique_chars, char_count
    except FileNotFoundError:
        print("找不到文件: {}".format(filename))
    except PermissionError:
        print("權限不足，無法打開文件: {}".format(filename))



count_unique_chars("/Users/linziyin/anaconda3/hw2_data.txt")
