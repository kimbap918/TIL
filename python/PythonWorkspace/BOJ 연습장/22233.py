import sys
input = sys.stdin.readline

N, M = map(int, input().split())
keywords = set()

for _ in range(N):
    keywords.add(input().strip())

for _ in range(M):
    blog_words = input().strip().split(',')
    for word in blog_words:
        keywords.discard(word)  
    print(len(keywords))
