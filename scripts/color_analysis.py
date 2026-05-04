import numpy as np
import colorsys
import cv2
from PIL import Image
from sklearn.cluster import KMeans

def extract_dominant_colors(image_path, k=5):
    img = Image.open(image_path).resize((200, 200))
    img_np = np.array(img).reshape(-1, 3)
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(img_np)
    return kmeans.cluster_centers_.astype(int)

def rgb_to_hue(rgb):
    r, g, b = rgb / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h * 360

def analyze_harmony(colors):
    hues = [rgb_to_hue(c) for c in colors]
    diffs = []
    for i in range(len(hues)):
        for j in range(i + 1, len(hues)):
            diff = abs(hues[i] - hues[j])
            diff = min(diff, 360 - diff)
            diffs.append(diff)
    avg_diff = np.mean(diffs)
    if 150 < avg_diff < 210: return "complementary"
    elif avg_diff < 60: return "analogous"
    elif 90 < avg_diff < 150: return "triadic_like"
    else: return "mixed"

def analyze_temperature(colors):
    warm, cool = 0, 0
    for c in colors:
        hue = rgb_to_hue(c)
        if 0 <= hue <= 60 or 300 <= hue <= 360: warm += 1
        elif 120 <= hue <= 240: cool += 1
    if warm > cool: return "warm"
    elif cool > warm: return "cool"
    else: return "neutral"

def analyze_emotion(temp):
    if temp == "warm": return "energetic / exciting"
    elif temp == "cool": return "calm / professional"
    else: return "balanced"

def analyze_balance(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    left = img[:, :w//2].mean()
    right = img[:, w//2:].mean()
    diff = abs(left - right) / 255
    if diff < 0.05: return "balanced"
    elif diff < 0.15: return "slightly unbalanced"
    else: return "unbalanced"

def analyze_complexity(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img, 100, 200)
    edge_density = np.sum(edges > 0) / edges.size
    if edge_density < 0.03: return "minimalist"
    elif edge_density < 0.08: return "moderate"
    else: return "complex"
