import random

def start_game():
    print("어서오세요! 당신은 모험가입니다. 어떤 모험을 떠날까요?")

    while True:
        choice = input("1. 동굴에 들어간다\n2. 숲으로 간다\n3. 집으로 돌아간다\n선택해주세요: ")

        if choice == '1':
            explore_cave()
        elif choice == '2':
            explore_forest()
        elif choice == '3':
            print("집으로 돌아갑니다. 모험이 끝났습니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

def explore_cave():
    print("당신은 동굴 안으로 들어갑니다.")
    # 동굴에서의 이벤트를 정의할 수 있습니다.
    outcome = random.choice(["몬스터를 만났습니다!", "보물을 발견했습니다!", "아무일도 일어나지 않았습니다."])
    print(outcome)

def explore_forest():
    print("당신은 숲 속으로 들어갑니다.")
    # 숲에서의 이벤트를 정의할 수 있습니다.
    outcome = random.choice(["야생 동물을 만났습니다!", "잃어버린 보물을 찾았습니다!", "산길을 잘못 들어갔습니다."])
    print(outcome)

if __name__ == "__main__":
    start_game()
