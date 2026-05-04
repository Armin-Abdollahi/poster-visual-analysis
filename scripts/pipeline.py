import os
import json

from color_analysis import (
    extract_dominant_colors,
    analyze_harmony,
    analyze_temperature,
    analyze_emotion,
    analyze_balance,
    analyze_complexity
)

from focal_point import detect_focal_point, draw_focal_point


POSTERS_DIR = "../posters"
RESULTS_DIR = "../results"

os.makedirs(RESULTS_DIR, exist_ok=True)


def process_posters():

    posters = [f for f in os.listdir(POSTERS_DIR)
               if f.lower().endswith((".jpg",".png",".jpeg"))]

    for poster in posters:

        print("Processing:", poster)

        poster_path = os.path.join(POSTERS_DIR, poster)
        name = os.path.splitext(poster)[0]

        # رنگ‌ها
        colors = extract_dominant_colors(poster_path)

        harmony = analyze_harmony(colors)
        temperature = analyze_temperature(colors)
        emotion = analyze_emotion(temperature)

        # ترکیب بندی
        balance = analyze_balance(poster_path)
        complexity = analyze_complexity(poster_path)

        # کانون توجه
        focal = detect_focal_point(poster_path)

        focal_path = os.path.join(RESULTS_DIR, f"{name}_focal.png")
        draw_focal_point(poster_path, focal_path)

        # JSON خروجی
        data = {
            "file_name": poster,
            "dominant_colors": colors.tolist(),
            "color_harmony": harmony,
            "color_temperature": temperature,
            "color_emotion": emotion,
            "composition_balance": balance,
            "visual_complexity": complexity
        }

        json_path = os.path.join(RESULTS_DIR, f"{name}.json")

        with open(json_path,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=2)

        print("Saved:", json_path)


if __name__ == "__main__":
    process_posters()
