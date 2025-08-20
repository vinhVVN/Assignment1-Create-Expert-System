base = [
    {
        "if": ["sổ mũi", "đau họng", "sốt nhẹ"],
        "then": "cảm lạnh",
        "advice": "Bạn nên nghỉ ngơi nhiều, uống đủ nước và giữ ấm cơ thể. Có thể dùng thêm vitamin C để tăng đề kháng."
    },
    {
        "if": ["sốt cao", "đau nhức cơ thể", "mệt mỏi rõ rệt"],
        "then": "cúm",
        "advice": "Bạn cần nghỉ ngơi tuyệt đối, uống nhiều nước và điện giải. Nếu sốt cao không hạ, hãy đến gặp bác sĩ ngay."
    },
    {
        "if": ["khó ngủ", "cảm thấy lo lắng", "đau đầu căng thẳng"],
        "then": "có dấu hiệu stress",
        "advice": "Bạn nên dành thời gian thư giãn, tập thể dục nhẹ nhàng như thiền hoặc yoga, và hạn chế sử dụng các thiết bị điện tử trước khi ngủ."
    }
]


questions = {
    "sổ mũi": "Bạn có bị sổ mũi hoặc nghẹt mũi không?",
    "đau họng": "Bạn có cảm thấy đau hoặc rát họng không?",
    "không sốt hoặc sốt nhẹ": "Nhiệt độ cơ thể của bạn có bình thường hoặc chỉ sốt nhẹ (dưới 38.5 độ C) không?",
    "sốt nhẹ": "Bạn có bị sốt nhẹ (từ 37,5 đến 38.5 độ C) không?",
    "sốt cao": "Bạn có bị sốt cao (trên 38.5 độ C) không?",
    "đau nhức cơ thể": "Bạn có cảm thấy đau mỏi các cơ bắp không?",
    "mệt mỏi rõ rệt": "Bạn có cảm thấy rất mệt mỏi, kiệt sức không?",
    "khó ngủ": "Gần đây bạn có bị khó ngủ hoặc ngủ không sâu giấc không?",
    "cảm thấy lo lắng": "Bạn có thường xuyên cảm thấy lo lắng, bồn chồn không?",
    "đau đầu căng thẳng": "Bạn có bị đau đầu, đặc biệt là cảm giác căng ở vùng trán hoặc sau gáy không?"
}

keyword_map = {
    "sổ mũi": ["sổ mũi", "nghẹt mũi", "chảy nước mũi"],
    "đau họng": ["đau họng", "rát họng", "viêm họng"],
    "sốt cao": ["sốt cao", "sốt nóng", "nhiệt độ cao"]
}

