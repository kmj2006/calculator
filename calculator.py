def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if(b!=0):
        return a/b
def main():
    while True:
        print('[ 메뉴 ]\n덧셈,뺄셈,곱셈,나눗셈,종료 중 하나를 골라주세요\n만약 종료를 입력하면 계산기는 종료됩니다')
        menu=str(input())

        if menu=='덧셈':
            a,b=map(int,input("두 정수 입력:").split())
            print(add(a,b))
        elif menu=='뺄셈':
            a,b=map(int,input("두 정수 입력:").split())
            print(sub(a,b))
        elif menu=='곱셈':
            a,b=map(int,input("두 정수 입력:").split())
            print(mul(a,b))
        elif menu=='나눗셈':
            if a or b == 0:
                print('계산이 불가합니다')
            a,b=map(int,input("두 정수 입력:").split())
            print(div(a,b))
        elif menu=='종료':
            print('종료합니다...')
            break
        else:
            print('잘못된 값입니다 종료합니다')
            break
if __name__ == "__main__":
    main()