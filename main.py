from algorithm import suy_luan, phantach_thongtin, known_facts
from knowledge_base import base

print(''' 
          Chao ban, toi la mot AI tu van cham soc suc khoe \n
          Toi duoc dua tren hinh mau bac si Tran Quoc Phong - idol cua Vinh
          ''')
name = input('Vi khach cua chung ta ten la gi nao?:')


while True:
   thongtin = input(f'Hom nay {name} cam thay nguoi minh nhu the nao? [Nhan q de thoat]')
   
   if thongtin == "q":
       break
   else:
        data = phantach_thongtin(thongtin)
        while not data:
                thongtin += input(f'Toi chua nhan dien duoc trieu chung cu the... {name} co the mo ta ro hon khong?')
                data = phantach_thongtin(thongtin)
        print(f"Cam on {name}. Dua vao viec ban co trieu chung '{','.join(data)}', toi se hoi them mot vai cau de lam ro nhe!")
        

        
        dauhieu = set() # tìm xem triệu chứng ban đầu
        for note in base:
            if any(symptom in data for symptom in note["if"]):
                dauhieu.add(note["then"]) # thêm nếu phát hiện có khớp khớp
            
        if not dauhieu:
            print(f'Day la lan dau toi nghe day! \n Hen {name} den truc tiep gap bac si Phong nhe!')
            break
        
        xacnhan_benh = []
        for trieuchung in dauhieu:
            print(f"Dang kiem tra kha nang ban bi '{trieuchung}' ....")
            if suy_luan(trieuchung):
                xacnhan_benh.append(trieuchung)
        
        if xacnhan_benh:
            print("------------------------------------------ \n")
            print(f"Dua tren cac trieu chung, co kha nang {name} dang bi:")
            for trieuchung in xacnhan_benh:
                for note in base:
                    if note["then"] == trieuchung:
                        print(f"**{trieuchung}**")
                        print(f"Loi khuyen: {note['advice']}")
        else:
            print("""Sau bao nhieu lan hoi, toi van chua the dua ra ket luan \n
                  Hen ban gap toi o Saigon Medicine""")
            
        break
    
                    