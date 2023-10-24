import cv2
import mediapipe as mp
import random
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 게임 설정
game_started = False
game_over = False
game_duration = 10  # 게임 지속 시간 (초)
score = 0
score_saved = False  # 게임 종료 시 한 번만 스코어를 저장하기 위한 플래그

# 랭킹 및 점수 기록
scores_list = []  # 스코어 기록을 저장할 리스트
ranking_shown = False  # 랭킹이 표시 중인지 여부

# 두더지 설정
mole_img = cv2.imread("ddg.png", cv2.IMREAD_UNCHANGED)
mole_height, mole_width, _ = mole_img.shape
mole_list = []  # 두더지의 위치와 나타나는 시간을 저장할 리스트

# 카메라 열기
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            continue

        image = cv2.flip(frame, 1)

        if not game_started:
            # 게임이 시작되지 않았을 때, 난이도를 선택할 수 있는 화면을 표시합니다.
            cv2.putText(
                image,
                "Select level:",
                (200, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (1, 1, 1),
                2,
            )
            cv2.putText(
                image,
                "level 1 - Easy",
                (200, 200),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                2,
            )
            cv2.putText(
                image,
                "level 2 - Normal",
                (200, 250),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )
            cv2.putText(
                image,
                "level 3 - Hard",
                (200, 300),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )

            key = cv2.waitKey(1)
            if key in [ord("1"), ord("2"), ord("3")]:
                # 사용자가 1, 2, 3 중 하나를 선택하면 해당 난이도로 게임 초기화
                selected_difficulty = key - ord("0")  # 선택된 난이도 (1, 2, 3)
                game_started = True
                start_time = time.time()  # 게임 시작 시간 기록
                game_over = False
                score = 0
                score_saved = False  # 스코어 저장 플래그 초기화
                # 난이도에 따라 두더지가 나타나는 시간을 조절
                if selected_difficulty == 1:
                    mole_duration = 1.0
                elif selected_difficulty == 2:
                    mole_duration = 0.5
                else:
                    mole_duration = 0.3
                mole_list = []  # 게임 재시작 시 두더지 리스트 초기화

        else:
            # 게임 진행 중

            # 게임 종료 조건 확인
            if time.time() - start_time >= game_duration:
                game_over = True

            if game_over:
                if not ranking_shown:
                    if not score_saved:  # 게임 종료 시 한 번만 스코어를 저장
                        scores_list.append(score)  # 스코어 기록에 추가
                        score_saved = True  # 스코어 저장 플래그 설정

                scores_list.sort(reverse=True)
                ranking = scores_list.index(score) + 1

                if not ranking_shown:
                    cv2.putText(
                        image,
                        "Game Over. Your Score: " + str(score),
                        (100, 150),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        2,
                    )
                    cv2.putText(
                        image,
                        "Ranking: " + str(ranking),
                        (100, 200),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (1, 1, 1),
                        2,
                    )
                    cv2.putText(
                        image,
                        "Press 'q' to View Rankings",
                        (100, 250),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                    )
                    cv2.putText(
                        image,
                        "Press SPACE to Play Again",
                        (100, 300),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 0, 0),
                        2,
                    )

                    key = cv2.waitKey(1)
                    if key == ord(" "):
                        game_started = False
                    elif key == ord("q"):
                        ranking_shown = True

                else:
                    # 랭킹 표시 중일 때, 'q'를 다시 누르면 게임 화면으로 돌아감
                    cv2.putText(
                        image,
                        "Ranking:",
                        (250, 150),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (1, 1, 1),
                        2,
                    )
                    num_rankings_to_show = min(3, len(scores_list))
                    for i in range(num_rankings_to_show):
                        cv2.putText(
                            image,
                            str(i + 1) + ". " + str(scores_list[i]),
                            (250, 200 + i * 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (1, 1, 1),
                            2,
                        )

                    key = cv2.waitKey(1)
                    if key == ord("q"):
                        ranking_shown = False

            else:
                current_time = time.time()

                # 새로운 두더지 추가
                if (
                    not mole_list or current_time - mole_list[-1][2] >= mole_duration
                ):  # 만약 mole_list가 비어있거나, 마지막 두더지가 mole_duration 시간 이상 화면에 머무는 경우, 새로운 두더지를 추가
                    mole_x = random.randint(
                        0, frame.shape[1] - mole_width
                    )  # 새로운 두더지의 x좌표를 랜덤 생성
                    mole_y = random.randint(
                        0, frame.shape[0] - mole_height
                    )  # 새로운 두더지의 y좌표를 랜덤 생성
                    mole_list.append(
                        (mole_x, mole_y, current_time)
                    )  # 새로운 두더지의 위치와 생성 시간을 mole_list에 저장

                # 두더지 그리기 및 사라진 두더지 임시 리스트에 저장
                removed_moles = []  # 사라진 두더지를 저장하기 위한 빈 리스트 생성
                for mole_x, mole_y, mole_start_time in mole_list:
                    if (
                        current_time - mole_start_time >= mole_duration
                    ):  # 두더지가 화면에 나타난 후 mole_duration 시간 이상 지난 경우, 해당 두더지를 removed_moles에 추가
                        removed_moles.append((mole_x, mole_y, mole_start_time))
                    else:
                        for c in range(0, 3):
                            image[
                                mole_y : mole_y + mole_height,
                                mole_x : mole_x + mole_width,
                                c,
                            ] = image[
                                mole_y : mole_y + mole_height,
                                mole_x : mole_x + mole_width,
                                c,
                            ] * (
                                1 - mole_img[:, :, 3] / 255.0
                            ) + mole_img[
                                :, :, c
                            ] * (
                                mole_img[:, :, 3] / 255.0
                            )

                # 사라진 두더지 제거
                for (
                    removed_mole
                ) in (
                    removed_moles
                ):  # removed_moles에 있는 사라진 두더지를 순회하면서 제거, 이로써 두더지가 게임 화면에서 사라짐
                    mole_list.remove(removed_mole)

                # 손 감지 및 손의 위치 확인
                frame_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(frame_rgb)  # 손 감지를 위해 이미지를 처리하고 손의 위치 및 랜드마트 얻음

                if results.multi_hand_landmarks:
                    for (
                        hand_landmarks
                    ) in results.multi_hand_landmarks:  # 감지된 손에 대한 랜드마크를 순회
                        hand_x = int(
                            hand_landmarks.landmark[8].x * frame.shape[1]
                        )  # 손의 중지 부분(landmakr[8])의 x좌표 계산
                        hand_y = int(
                            hand_landmarks.landmark[8].y * frame.shape[0]
                        )  # 손의 중지 부분(landmark[8])의 y좌표 계산

                        # 모든 두더지와의 충돌 확인
                        # 현재 손의 위치를 두더지와 비교하여 충돌 여부를 확인하고, 두더지를 잡았을 경우 score를 증가시키고 해당 두더지를 mole_list에서 제거
                        for mole_x, mole_y, _ in mole_list:
                            if (
                                mole_x < hand_x < mole_x + mole_width
                                and mole_y < hand_y < mole_y + mole_height
                            ):
                                # 두더지를 잡았을 경우
                                score += 1
                                mole_list.remove((mole_x, mole_y, mole_start_time))

                # 현재 시간과 점수를 화면에 표시합니다.
                cv2.putText(
                    image,
                    "Time: {:.1f}s".format(current_time - start_time),
                    (10, 60),  # 시간 표시 위치 조정 가능
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),  # 텍스트 색상 (흰색)
                    2,
                )
                cv2.putText(
                    image,
                    "Score: " + str(score),  # 스코어 값 표시
                    (10, 30),  # 위치 조정 가능
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),  # 텍스트 색상 (흰색)
                    2,
                )

        # 게임 화면을 열어줍니다.
        cv2.imshow("Whack-a-Mole Game", image)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC 키를 누르면 게임 종료
            break

cap.release()  # 카메라를 해제합니다.
cv2.destroyAllWindows()  # 모든 창을 닫습니다.
