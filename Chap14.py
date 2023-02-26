# import os
# def walk(dirname):
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)
#
#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)
#
#
# def walk2(dirname):
#
#     for root, dirs, files in os.walk(dirname):
#         for filename in files:
#             print(os.path.join(root, filename))
#
#
# if __name__ == '__main__':
#     walk('.')
#     walk2('.')
#
# try:
#     fin = open('bad_file')
# except:
#     print('Something went wrong.')


def line_count(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count


print(line_count('wc.py'))
