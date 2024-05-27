import os

def list_dir_tree(path, indent=''):

    # 해당 디렉터리의 모든 항목을 가져옵니다.
    items = os.listdir(path)

    for i, item in enumerate(items):
        # 마지막 항목인지 체크 (트리의 가지 모양을 위해)
        is_last = i == len(items) - 1

        # 현재 항목의 전체 경로를 구한다..
        full_path = os.path.join(path, item)

        # 들여쓰기와 함께 항목 이름을 출력
        print(f"{indent}{'└──' if is_last else '├──'} {item}")

        # 현재 항목이 디렉터리인 경우 재귀적으로 탐색
        if os.path.isdir(full_path):
            # 다음 들여쓰기를 계산
            next_indent = indent + ('    ' if is_last else '│   ')
            list_dir_tree(full_path, next_indent)

# 예제 사용
# 특정 디렉터리 (예: '/path/to/directory')를 대상으로 함수를 호출합니다.
list_dir_tree('./')
