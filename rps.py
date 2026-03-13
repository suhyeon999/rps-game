import random

def play_rps():
    # 전적 기록을 위한 변수
    win = 0
    draw = 0
    lose = 0
    
    options = ["가위", "바위", "보"]
    
    print("✊✌️🖐️ 가위바위보 게임을 시작합니다!")
    print("(게임 종료를 원하시면 '그만'이라고 입력하세요)")

    while True:
        # 1. 사용자 입력 받기
        user_choice = input("\n가위, 바위, 보 중 하나를 선택하세요: ")
        
        if user_choice == "그만":
            break
            
        if user_choice not in options:
            print("❌ 잘못된 입력입니다. 가위, 바위, 보 중에서 골라주세요.")
            continue

        # 2. 컴퓨터의 무작위 선택
        computer_choice = random.choice(options)
        print(f"나: {user_choice} vs 컴퓨터: {computer_choice}")

        # 3. 승패 판정 로직
        if user_choice == computer_choice:
            print("🤝 비겼습니다!")
            draw += 1
        elif (user_choice == "가위" and computer_choice == "보") or \
             (user_choice == "바위" and computer_choice == "가위") or \
             (user_choice == "보" and computer_choice == "바위"):
            print("🎉 이겼습니다!")
            win += 1
        else:
            print("💀 졌습니다...")
            lose += 1
            
        # 현재 전적 출력
        print(f"현재 전적: {win}승 {draw}무 {lose}패")

    print("\n--- 게임 종료 ---")
    print(f"최종 전적은 {win}승 {draw}무 {lose}패입니다. 수고하셨습니다!")

# 게임 실행
play_rps()
