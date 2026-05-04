import cv2
import numpy as np

def detect_focal_point(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image at {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ۱. استخراج لبه‌های تصویر (پیدا کردن جزئیات و سوژه‌ها)
    edges = cv2.Canny(gray, 50, 150)

    # ۲. ایجاد نقشه حرارتی با تار کردن بسیار شدید لبه‌ها
    # این کار باعث می‌شود لبه‌های متراکم به یک توده یکپارچه (Hotspot) تبدیل شوند
    # سایز کرنل بلور باید بزرگ باشد، متناسب با سایز تصویر آن را داینامیک می‌کنیم
    h, w = gray.shape
    kernel_size = int(min(h, w) * 0.1) 
    if kernel_size % 2 == 0: kernel_size += 1 # کرنل باید فرد باشد
    
    heatmap = cv2.GaussianBlur(edges, (kernel_size, kernel_size), 0)

    # ۳. پیدا کردن درخشان‌ترین نقطه در نقشه حرارتی (مرکز ثقل بصری)
    y, x = np.unravel_index(np.argmax(heatmap), heatmap.shape)

    fx = x / w
    fy = y / h

    # تشخیص موقعیت سوژه
    if 0.33 < fx < 0.66 and 0.33 < fy < 0.66:
        region = "center"
    elif fx < 0.33:
        region = "left"
    elif fx > 0.66:
        region = "right"
    elif fy < 0.33:
        region = "top"
    elif fy > 0.66:
        region = "bottom"
    else:
        region = "mixed"

    return {
        "x": int(x),
        "y": int(y),
        "region": region
    }

def draw_focal_point(image_path, output_path):
    img = cv2.imread(image_path)
    data = detect_focal_point(image_path)

    x = data["x"]
    y = data["y"]

    # کشیدن یک دایره و یک نقطه در مرکز کانون توجه
    cv2.circle(img, (x, y), 60, (0, 0, 255), 4) # دایره توخالی
    cv2.circle(img, (x, y), 10, (0, 0, 255), -1) # نقطه توپر مرکز

    cv2.imwrite(output_path, img)

    return data
