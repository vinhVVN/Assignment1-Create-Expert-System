from knowledge_base import base, questions, keyword_map

known_facts = {}

def xac_nhan(fact):
    if fact in known_facts:
        return known_facts[fact]
    
    if fact in questions:
        while True:
            answer = input(f'Xin phép cho tôi hỏi: {questions[fact]}')
            if answer in ["có", "ừ"]:
                known_facts[fact] = True
                return True
            elif answer in ["không", "ko"]:
                known_facts[fact] = False
                return False
            else:
                print('Chỉ cần trả lời có hoặc không thôi bạn nhé!')
    else:
        return False # câu hỏi này lạ quá
    
def suy_luan(trieuchung):
    if trieuchung in known_facts: # nếu triệu chứng đã được chuẩn đoán rồi thì ko cần xét nữa
        return known_facts[trieuchung]
    
    for note in base:
        if note["then"] == trieuchung:
            dieukien = True
            for condition in note["if"]:
                if not suy_luan(condition): # xem có khớp hết điều kiện để có thể kết luận
                    dieukien = False
                    break
            if dieukien:
                known_facts[trieuchung] = True
                return True
            
    return xac_nhan(trieuchung) # chưa xác định rõ thì có thể hỏi lại

def phantach_thongtin(txt):
    detected_data = []
    for fact, keywords in keyword_map.items():
        for keyword in keywords:
            if keyword in txt.lower() and (fact not in detected_data):
                detected_data.append(fact)
    return detected_data

