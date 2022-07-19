def solution(phone_book):
    answer = True
    while len(phone_book)>0:
        num = min(phone_book)
        phone_book.remove(num)
        for i in phone_book:
            if num == i[:len(num)]:
                answer = False
                return answer
    return answer
