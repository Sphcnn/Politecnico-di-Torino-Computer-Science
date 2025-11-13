# Dosya Adı: code_3_yolo_cv_id.py
# Senaryo: YOLOv8L Tespiti -> Kırmızı/Sekizgen Doğrulaması -> ID Takibi
# NOT: Yüksek güvenilirlik ve kararlılık.
import cv2
import numpy as np
from ultralytics import YOLO
import torch
import time
import collections
import os
import inspect

def run_scenario_3(source_path):
    SCENARIO_NAME = "3. YOLOv8L + CV DOĞRULAMASI + ID"
    print(f"\n--- {SCENARIO_NAME} BAŞLATILIYOR ---")
    
    MODEL_YOLO = YOLO("yolov8l.pt").to(DEVICE)
    
    cap = cv2.VideoCapture(source_path)
    if not cap.isOpened(): return print(f"HATA: {source_path} açılamadı.")
    
    total_frames = 0
    processed_frames = 0
    total_duration = 0.0
    analysis_start_time = time.time()
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
        
        # 1. ANALİZ: YOLO ile takip ve ilk tespit
        results = MODEL_YOLO.track(frame, tracker=TRACKER_CONFIG, conf=CONFIDENCE_THRESHOLD, device=DEVICE, verbose=False)
        
        current_frame_ids = set()
        final_detections = []

        for result in results:
            if result.boxes.id is not None:
                for i in range(len(result.boxes.conf)):
                    label = result.names[int(result.boxes.cls[i])]
                    if label == "stop sign":
                        
                        # 2. CV DOĞRULAMASI
                        xy = result.boxes.xyxy[i]
                        x1, y1, x2, y2 = map(int, xy.cpu().numpy())
                        crop_img = frame[max(0, y1):min(frame.shape[0], y2), max(0, x1):min(frame.shape[1], x2)]
                        
                        if is_stop_sign_valid(crop_img): # Kırmızı ve Sekizgen Kontrolü
                            tracker_id = int(result.boxes.id[i].cpu().numpy())
                            current_frame_ids.add(tracker_id)
                            final_detections.append((tracker_id, x1, y1, x2, y2))
                        else:
                            # Yanlış Pozitif elendi
                            cv2.putText(frame, "REJECTED (CV)", (x1, y1 - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


        # 3. ID TAKİP VE KARAR MEKANİZMASI
        for tracker_id in list(active_stop_signs.keys()):
            if tracker_id not in current_frame_ids:
                active_stop_signs[tracker_id] = max(0, active_stop_signs[tracker_id] - 1)
                if active_stop_signs[tracker_id] == 0: del active_stop_signs[tracker_id]
        
        is_braking_triggered = False
        for tracker_id in current_frame_ids:
            active_stop_signs[tracker_id] += 1
            if active_stop_signs[tracker_id] >= DEFAULT_THRESHOLD_STOP:
                is_braking_triggered = True

        # 4. GÖRSELLEŞTİRME
        for id_val, x1, y1, x2, y2 in final_detections:
            count = active_stop_signs[id_val]
            color = (0, 0, 255) if count >= DEFAULT_THRESHOLD_STOP else (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)
            cv2.putText(frame, f"ID:{id_val} C:{count}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            
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

# if __name__ == '__main__': run_scenario_3("test_video.mp4")