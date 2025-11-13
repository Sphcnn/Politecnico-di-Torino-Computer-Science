# Dosya Adı: code_1_dual_yolo_ham.py
# Senaryo: YOLOv8L + YOLOv8L, Ham Karar (ID ve CV Yok)
# NOT: Bu kod çok yavaştır, çünkü iki büyük model aynı anda çalışır.

import cv2
import numpy as np
from ultralytics import YOLO
import torch
import time
import collections
import os
import inspect

def run_scenario_1(source_path):
    SCENARIO_NAME = "1. ÇİFT YOLO HAM ANALİZ (YOLOv8L + YOLOv8L)"
    print(f"\n--- {SCENARIO_NAME} BAŞLATILIYOR ---")
    
    # Modelleri yükle (İki kez büyük model)
    MODEL_1 = YOLO("yolov8l.pt").to(DEVICE)
    MODEL_2 = YOLO("yolov8l.pt").to(DEVICE)
    
    cap = cv2.VideoCapture(source_path)
    if not cap.isOpened(): return print(f"HATA: {source_path} açılamadı.")
    
    total_frames = 0
    processed_frames = 0
    total_duration = 0.0
    
    analysis_start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break

        total_frames += 1
        if total_frames % SKIP_FRAMES != 0: 
            if cv2.waitKey(1) & 0xFF == ord('q'): break
            continue

        processed_frames += 1
        frame_start_time = time.time()
        
        # 1. ANALİZ: İki modeli birden çalıştır
        results_1 = MODEL_1.predict(frame, conf=CONFIDENCE_THRESHOLD, device=DEVICE, verbose=False)
        results_2 = MODEL_2.predict(frame, conf=CONFIDENCE_THRESHOLD, device=DEVICE, verbose=False)
        
        # 2. SONUÇLARI BİRLEŞTİR
        stop_detections = []
        for results in [results_1, results_2]:
            for result in results:
                if result.boxes is not None:
                    for i in range(len(result.boxes.conf)):
                        if result.names[int(result.boxes.cls[i])] == "stop sign":
                            stop_detections.append(result.boxes.xyxy[i].cpu().numpy().astype(int))

        num_final_detections = len(stop_detections)
        is_braking_triggered = num_final_detections >= 1 # Basit mantık: Bir tane bile tespit yeterli
        
        # 3. GÖRSELLEŞTİRME
        for xmin, ymin, xmax, ymax in stop_detections:
            color = (0, 0, 255) if is_braking_triggered else (0, 255, 255)
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 3)
            
        # Raporlama
        frame_processing_time = time.time() - frame_start_time
        total_duration += frame_processing_time
        fps = 1 / frame_processing_time
        status_text = f"FPS: {fps:.2f} | Detections: {num_final_detections} | STATUS: {'!!! BRAKING !!!' if is_braking_triggered else 'Tracking'}"
        cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.imshow(SCENARIO_NAME, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()
    print_report(total_frames, processed_frames, time.time() - analysis_start_time, SCENARIO_NAME)

# if __name__ == '__main__': run_scenario_1("test_video.mp4")