# Dosya Adı: code_4_cv_yolo_id.py
# Senaryo: Kırmızı/Sekizgen Tespiti -> YOLOv8L Doğrulaması -> ID Takibi
# NOT: İşlem yükü en düşüktür, ancak ilk aşama (Kırmızı Filtre) kötü havada en zayıf halkadır.

def run_scenario_4(source_path):
    SCENARIO_NAME = "4. CV TESPİTİ + YOLOv8L DOĞRULAMASI + ID"
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
        
        # 1. TESPİT: Kırmızı/Sekizgen ile Hızlı Tarama (Geleneksel CV)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv_frame, LOWER_RED_1, UPPER_RED_1)
        mask2 = cv2.inRange(hsv_frame, LOWER_RED_2, UPPER_RED_2)
        red_mask = mask1 | mask2
        
        processed_mask = cv2.GaussianBlur(red_mask, (5, 5), 0)
        kernel = np.ones((3, 3), np.uint8)
        processed_mask = cv2.morphologyEx(processed_mask, cv2.MORPH_CLOSE, kernel)
        contours, _ = cv2.findContours(processed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        yolo_validation_list = []
        for contour in contours:
            if cv2.contourArea(contour) < 500: continue # Küçük konturları at
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)
            if 7 <= len(approx) <= 9: # Sekizgen adayı bulundu
                x, y, w, h = cv2.boundingRect(contour)
                # Kırpma kutusu oluştur (biraz genişletilmiş alan)
                yolo_validation_list.append(frame[max(0, y-10):y+h+10, max(0, x-10):x+w+10]) 

        current_frame_ids = set()
        final_detections = []
        
        # 2. DOĞRULAMA: YOLO ile sadece adayları kontrol et
        if yolo_validation_list:
            # YOLO'ya sadece kırpılmış adayları gönderiyoruz
            results = MODEL_YOLO.predict(yolo_validation_list, conf=0.6, device=DEVICE, verbose=False)
            
            # Bu basit senaryoda, YOLO'dan ID almak zor olduğu için (takip yok)
            # YOLO'nun tespitini geçici bir ID ile işaretliyoruz.
            for result_idx, result in enumerate(results):
                for i in range(len(result.boxes.conf)):
                    if result.names[int(result.boxes.cls[i])] == "stop sign":
                        # Burada gerçek ID yerine sahte bir ID kullanıyoruz veya takip mantığını devre dışı bırakıyoruz.
                        # Gerçek ID takibi için, bu adımda alınan sonuçlar ayrı bir takip algoritmasına beslenmelidir.
                        
                        # Basitlik için sahte ID ve ham kutu çizimi yapalım:
                        # Bu senaryo ID takibi ile tam uyumlu değildir, ancak mantığı gösterir.
                        x, y, w, h = cv2.boundingRect(contours[result_idx]) # Orijinal kontur kutusunu kullan
                        final_detections.append((999 + result_idx, x, y, x+w, y+h)) # Sahte ID

        # 3. ID TAKİP VE KARAR MEKANİZMASI (Bu senaryoda sınırlı)
        # Sadece geçici tespitleri gösteriyoruz, kalıcı ID takibi bu ham yapıda zor.

        # 4. GÖRSELLEŞTİRME
        is_braking_triggered = bool(final_detections) # Tespit varsa tetikle

        for id_val, x1, y1, x2, y2 in final_detections:
            color = (0, 0, 255) if is_braking_triggered else (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)
            cv2.putText(frame, "CV+YOLO CONFIRMED", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            
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

if __name__ == '__main__': 
    run_scenario_4("test_video.mp4")