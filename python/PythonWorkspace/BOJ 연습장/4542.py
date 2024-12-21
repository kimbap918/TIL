def find_lcs(sequences):
    def is_common(subseq, sequences): # 현재 부분 문자열이 모든 시퀀스에 공통으로 포함되는지 확인
        return all(subseq in seq for seq in sequences)
        # all 함수는 생성된 Boolean 값들 중 하나라도 False가 있으면 False를 반환
        
    first_sequence = sequences[0] # 입력된 시퀀스 중 첫번째 문자열
    max_length = 0
    result = None

    for start in range(len(first_sequence)):
        for end in range(start+3, len(first_sequence)+1):
            # 첫번째 문자열에서 부분 문자열을 생성
            # end는 항상 start+3이므로, 문자열의 최소 길이가 3이상
            subseq = first_sequence[start:end]
            if is_common(subseq, sequences): # 공통된 부분 문자열이 확인됐을때

                # 해당 부분 문자열 길이가 기존의 max_length보다 크다면 새로운 결과로 업데이트
                # 부분 문자열 길이가 동일할 경우, 사전순 비교를 통해 더 작은 문자열을 결과로 저장
                if len(subseq) > max_length or (len(subseq) == max_length and (result is None or subseq < result)):
                    max_length = len(subseq)
                    result = subseq
    return result if result else "no significant commonalities"
    # 공통된 부분 문자열이 없는 경우 "no significant commonalities" 반환


M = int(input())

for _ in range(M):
    m = int(input())
    sequence = [input().strip() for _ in range(m)] 
    print(find_lcs(sequence))

