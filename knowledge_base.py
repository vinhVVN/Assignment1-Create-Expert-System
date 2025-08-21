base = [
    {
        "if": ["sổ mũi", "đau họng", "sốt nhẹ"],
        "then": "cảm lạnh",
        "advice": "Bạn nên nghỉ ngơi nhiều, uống đủ nước và giữ ấm cơ thể. Có thể dùng thêm vitamin C để tăng đề kháng."
    },
    {
        "if": ["sốt cao", "đau nhức cơ thể", "mệt mỏi"],
        "then": "cúm",
        "advice": "Bạn cần nghỉ ngơi tuyệt đối, uống nhiều nước và điện giải. Nếu sốt cao không hạ, hãy đến gặp bác sĩ ngay."
    },
    {
        "if": ["khó ngủ", "cảm thấy lo lắng", "đau đầu căng thẳng"],
        "then": "stress",
        "advice": "Bạn nên dành thời gian thư giãn, tập thể dục nhẹ nhàng như thiền hoặc yoga, và hạn chế sử dụng các thiết bị điện tử trước khi ngủ."
    },
    {
        "if":["tiểu buốt", "tiểu nhiều lần"],
        "then":"nhiễm trùng tiết niệu (UTI)",
        "advice":"Nhiễm trùng đường tiểu nên ăn các loại thực phẩm lành mạnh." + 
                "Ưu tiên nước, nước ép nam việt quất và thực phẩm như quả mọng, rau xanh, trái cây tươi để thúc đẩy quá trình loại bỏ nhiễm trùng, giảm viêm và hồi phục sức khỏe đường tiết niệu."
    },
    {
        "if": ["đau quặn thận", "tiểu ra máu", "buồn nôn", "tiểu buốt", "tiểu nhiều lần"],
        "then": "sỏi thận",
        "advice":"""
- Ăn các thực phẩm giúp lợi niệu và dễ tiêu hóa: Chế độ ăn và uống lợi niệu sẽ có tác dụng bài xuất các mảnh sỏi vụn, các nhân sỏi nhỏ, dịch máu, cặn máu, các thành phần hữu hình trên thận niệu quản theo ống thông xuống bàng quang, tiểu ra ngoài.
- Chế độ ăn dễ tiêu hoá giúp bệnh nhân nhanh hấp thu để hồi phục sức khỏe, liền các tổn thương niêm mạc – thành niệu quản. Các thực phẩm giúp dễ tiêu hóa: rau lang, rau mồng tơi, khoai lang, rau đay, rau nhiếp cá, đậu phụ, chuối, súp lơ,…
- Uống nhiều nước và không nhịn tiểu: Mỗi ngày uống từ 2,5 đén 3 lít nước, cần đi tiểu ngay khi có nhu cầu, tốt nhất là nên rèn luyện đồng hồ sinh học thích hợp để tránh phải nhịn tiểu.
- Giảm thiểu chế độ ăn nhiều oxalat và canxi. Các thực phẩm nên hạn chế: Tôm, cua, đồ hải sản. Đồ uống nên hạn chế: nước chè đặc, cà phê. Hạn chế lòng lợn hay các món chế biến từ óc của động vật… đây là nguồn thực phẩm dễ gây sỏi thận.
        """
    },
    {
        "if": ["bị phù", "mệt mỏi", "chán ăn","buồn nôn","khó thở","cao huyết áp"],
        "then": "suy thận",
        "advice": "thường xuyên đo huyết áp và làm xét nghiệm nước tiểu ít nhất 3 tháng một lần để được kiểm tra protein hoặc microalbumin niệu bằng que thử. Bên cạnh đó, để ngăn ngừa bệnh đái tháo đường, người bệnh cũng cần phải kiểm soát được lượng đường trong máu một cách cẩn thận, duy trì huyết áp dưới 130/ 80 mmHg, giảm đi lượng protein trong khẩu phần ăn và kiểm soát được lipid máu."
    }
    
]


questions = {
    "cao huyết áp": "Cảm thấy huyết áp trong người bạn có đang cao không?",
    "khó thở" : "Bạn có thấy khó thở không?",
    "chán ăn" : "Dạo này bạn có thấy chán ăn không?",
    "bị phù" : "Người bạn có bị sưng ở đâu không?",
    "buồn nôn": "Bạn có thấy buồn nôn không?",
    "tiểu ra máu" : "Gần đây bạn có tiểu ra máu lần nào không?",
    "đau quặn thận": "Bạn có hay đau lưng dữ dội, lan xuống bụng dưới và háng (khu vực quanh thận)",
    "tiểu nhiều lần": "Bạn có hay buồn đi tiểu nhiều lần, nhưng mỗi lần chỉ đi có một chút?",
    "tiểu buốt" : "Bạn có hay đau rát khi đi tiểu không?",
    "sổ mũi": "Bạn có bị sổ mũi hoặc nghẹt mũi không?",
    "đau họng": "Bạn có cảm thấy đau hoặc rát họng không?",
    "không sốt hoặc sốt nhẹ": "Nhiệt độ cơ thể của bạn có bình thường hoặc chỉ sốt nhẹ (dưới 38.5 độ C) không?",
    "sốt nhẹ": "Bạn có bị sốt nhẹ (từ 37,5 đến 38.5 độ C) không?",
    "sốt cao": "Bạn có bị sốt cao (trên 38.5 độ C) không?",
    "đau nhức cơ thể": "Bạn có cảm thấy đau mỏi các cơ bắp không?",
    "mệt mỏi": "Bạn có cảm thấy rất mệt mỏi, kiệt sức không?",
    "khó ngủ": "Gần đây bạn có bị khó ngủ hoặc ngủ không sâu giấc không?",
    "cảm thấy lo lắng": "Bạn có thường xuyên cảm thấy lo lắng, bồn chồn không?",
    "đau đầu căng thẳng": "Bạn có bị đau đầu, đặc biệt là cảm giác căng ở vùng trán hoặc sau gáy không?"
}

keyword_map = {
    "cao huyết áp": ["cao huyết áp", "lên máu", "hoa mắt", "chóng mặt", "ù tai"],
    "khó thở" : ["khó thở", "thở không ra hơi", "thở mệt", "nặng ngực"],
    "chán ăn" : ["chán ăn", "không thấy đói", "không ngon", "vị dở", "không muốn ăn", "ngán"],
    "bị phù" : ["phù", "sưng"],
    "buồn nôn" : ["nôn", "buồn nôn", "ói"],
    "tiểu ra máu" : ["tiểu máu", "ra máu", "nước tiểu đỏ"],
    "đau quặn thận": ["đau thận", "đau lưng", "đau bụng", "đau chỗ háng"],
    "sổ mũi": ["sổ mũi", "nghẹt mũi", "chảy nước mũi"],
    "đau họng": ["đau họng", "rát họng", "viêm họng"],
    "sốt cao": ["sốt cao", "sốt nóng", "nhiệt độ cao"],
    "tiểu nhiều lần": ["buồn tiểu", "tiểu nhiều"],
    "tiểu buốt": ["tiểu đau", "tiểu buốt", "tiểu rát"],
    "đau nhức cơ thể" : ["đau nhức", "ê người", "mỏi người", "đau cơ"],
    "mệt mỏi" : ["mệt mỏi", "lười", "đuối"],
    "khó ngủ" : ["khó ngủ", "ngủ không được", "không ngủ được", "không buồn ngủ"],
    "cảm thấy lo lắng" : ["lo lắng", "lo âu", "sợ", "suy nghĩ nhiều"],
    "đau đầu căng thẳng" : ["đau đầu", "căng thẳng", "khó chịu", "mệt mỏi", "chóng mặt"]
}

