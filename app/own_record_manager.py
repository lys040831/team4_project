class OwnRecordManager:
    def __init__(self):
        self.records = []

    def add_record(self, player_name, result):
        if player_name == "":
            player_name = "사용자"
        record = [player_name, result[0], result[1], result[2]]
        self.records.append(record)
        print("게임 결과가 저장되었습니다.")

    def show_records(self):
        print()
        print("===== 투자 기록 / 점수 확인 =====")
        print()
        if len(self.records) == 0:
            print("아직 저장된 기록이 없습니다.")
        else:
            for i in range(len(self.records)):
                record = self.records[i]
                print(str(i + 1) + "번째 기록")
                print("닉네임: " + record[0])
                print("게임: " + record[1])
                print("점수: " + str(record[2]))
                print("결과: " + record[3])
                print()
