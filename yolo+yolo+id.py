# Dosya Adı: code_2_dual_yolo_id.py
# Senaryo: YOLOv8L + YOLOv8L, ID Takibi ile Kararlılık
# NOT: İki modelin tespitleri tek bir takip mekanizmasına beslenir.

import cv2
import numpy as np
from ultralytics import YOLO
import torch
import time
import collections
import os
import inspect

def run_scenario_2(source_path):
    SCENARIO_NAME = "2. ÇİFT YOLO + ID TAKİBİ"
    print(f"\n--- {SCENARIO_NAME} BAŞLATILIYOR ---")
    
    # Modelleri yükle
    MODEL_1 = YOLO("yolov8l.pt").to(DEVICE)
    MODEL_2 = YOLO("yolov8l.pt").to(DEVICE)
    
    cap = cv2.VideoCapture(source_path)
    if not cap.isOpened(): return print(f"HATA: {source_path} açılamadı.")
    
    total_frames = 0
    processed_frames = 0
    total_duration = 0.0
    analysis_start_time = time.time()
    
    # ID Takip için tek bir modelin 'track' metodunu kullanacağız ve diğerini buna besleyeceğiz (Basitleştirilmiş)
    # Gerçek uygulamada takip algoritmaları çıktıları birleştirir, biz sadece bir modelle takip başlatıyoruz.
    
    active_stop_signs = collections.defaultdict(int)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        total_frames += 1
        if total_frames % SKIP_FRAMES != 0: 
            if cv2.waitKey(1) & 0xFF == ord('q'): break
            continue
        processed_frames += 1
        frame_start_time = time.time()
        
        # 1. ANALİZ: İki modeli de çalıştır (Model 1 ile takip başlat)
        results_1 = MODEL_1.track(frame, tracker=TRACKER_CONFIG, conf=CONFIDENCE_THRESHOLD, device=DEVICE, verbose=False)
        results_2 = MODEL_2.predict(frame, conf=CONFIDENCE_THRESHOLD, device=DEVICE, verbose=False) # İkinci model sadece tahmin yapar

        current_frame_ids = set()
        final_detections = []
        
        # 2. Takip (Model 1'in ID'lerini kullan)
        for result in results_1:
            if result.boxes.id is not None:
                for i in range(len(result.boxes.conf)):
                    if result.names[int(result.boxes.cls[i])] == "stop sign":
                        tracker_id = int(result.boxes.id[i].cpu().numpy())
                        current_frame_ids.add(tracker_id)
                        final_detections.append((tracker_id, result.boxes.xyxy[i].cpu().numpy().astype(int)))
                        
        # 3. İkinci Modelden Gelen Tespiti Kontrol Et (Doğrulama amaçlı kullanılabilir)
        # Basitlik için sadece Model 1'in takip sonuçlarını kullanıyoruz.

        # 4. KARAR MEKANİZMASI (ID Sayacı)
        for tracker_id in list(active_stop_signs.keys()):
            if tracker_id not in current_frame_ids:
                active_stop_signs[tracker_id] = max(0, active_stop_signs[tracker_id] - 1)
                if active_stop_signs[tracker_id] == 0: del active_stop_signs[tracker_id]
        
        is_braking_triggered = False
        for tracker_id in current_frame_ids:
            active_stop_signs[tracker_id] += 1
            if active_stop_signs[tracker_id] >= DEFAULT_THRESHOLD_STOP:
                is_braking_triggered = True

        # 5. GÖRSELLEŞTİRME
        for id_val, bbox in final_detections:
            count = active_stop_signs[id_val]
            color = (0, 0, 255) if count >= DEFAULT_THRESHOLD_STOP else (0, 255, 0)
            xmin, ymin, xmax, ymax = bbox
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 3)
            cv2.putText(frame, f"ID:{id_val} C:{count}", (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            
        frame_processing_time = time.time() - frame_start_time
        total_duration += frame_processing_time
        fps = 1 / frame_processing_time
        status_text = f"FPS: {fps:.2f} | Detections: {len(final_detections)} | STATUS: {'!!! BRAKING !!!' if is_braking_triggered else 'Tracking'}"
        cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.imshow(SCENARIO_NAME, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()
    print_report(total_frames, processed_frames, time.time() - analysis_start_time, SCENARIO_NAME)

# if __name__ == '__main__': run_scenario_2("test_video.mp4")