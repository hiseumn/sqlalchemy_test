import os, sys

print('環境変数')
for k, v in os.environ.items():
    print(f'{k}={v}')

print('引数')
for i in range(len(sys.argv)):
    print(f'{i}={sys.argv[i]}')
    