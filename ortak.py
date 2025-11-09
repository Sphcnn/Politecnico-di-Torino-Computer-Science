import cv2
import numpy as np
from ultralytics import YOLO
import torch
import time
import collections
import os
import inspect

# --- GENEL AYARLAR ---
DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
CONFIDENCE_THRESHOLD = 0.5
TRACKER_CONFIG = "bytetrack.yaml"

# Geleneksel CV Ayarları
OCTAGON_SIDE_TOLERANCE = 1.0 
MIN_RED_RATIO = 0.15 
LOWER_RED_1 = np.array([0, 70, 70])
UPPER_RED_1 = np.array([10, 255, 255])
LOWER_RED_2 = np.array([165, 70, 70])
UPPER_RED_2 = np.array([179, 255, 255])
DEFAULT_THRESHOLD_STOP = 5     # ID Sayacı Eşiği
SKIP_FRAMES = 3                # Her 3 karede bir işle

# --- CV DOĞRULAMA FONKSİYONU ---
def is_stop_sign_valid(crop_img):
    """Kırpılmış görüntüyü Kırmızı ve Sekizgen olarak doğrular."""
    if crop_img is None or crop_img.size == 0:
        return False
    # Renk Filtreleme
    hsv_crop = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv_crop, LOWER_RED_1, UPPER_RED_1)
    mask2 = cv2.inRange(hsv_crop, LOWER_RED_2, UPPER_RED_2)
    red_mask = mask1 | mask2
    if cv2.countNonZero(red_mask) / (crop_img.shape[0] * crop_img.shape[1]) < MIN_RED_RATIO:
        return False
    # Şekil Doğrulaması
    processed_mask = cv2.GaussianBlur(red_mask, (5, 5), 0)
    kernel = np.ones((3, 3), np.uint8)
    processed_mask = cv2.morphologyEx(processed_mask, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(processed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)
        sides = len(approx)
        if 8 - OCTAGON_SIDE_TOLERANCE <= sides <= 8 + OCTAGON_SIDE_TOLERANCE:
            return True 
    return False

# --- RAPORLAMA FONKSİYONU ---
def print_report(total_frames, processed_frames, duration, scenario_name):
    avg_latency_ms = (duration / processed_frames) * 1000 if processed_frames > 0 else 0
    avg_fps = processed_frames / duration if duration > 0 else 0
    print("\n=======================================================")
    print(f"             📊 ANALİZ RAPORU: {scenario_name} 📊             ")
    print("=======================================================")
    print(f"Toplam Okunan Kare Sayısı:   {total_frames}")
    print(f"İşlenen Kare Sayısı:         {processed_frames}")
    print(f"Toplam Analiz Süresi:        {duration:.2f} saniye")
    print("-------------------------------------------------------")
    print(f"Ortalama İşlem Gecikmesi:    {avg_latency_ms:.2f} ms/kare")
    print(f"Ortalama İşlem Hızı:         {avg_fps:.2f} FPS")
    print("=======================================================")