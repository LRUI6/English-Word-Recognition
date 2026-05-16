import pytesseract
from PIL import Image
import os

# 💡 這是你剛才提供的精確路徑，指向 tesseract 執行檔
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lrui6\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def predict_word_tesseract(image: Image.Image) -> str:
    """使用傳統的 Tesseract 進行辨識"""
    try:
        # 檢查該路徑下的檔案是否真的存在
        if not os.path.exists(pytesseract.pytesseract.tesseract_cmd):
            return "錯誤：找不到 Tesseract 執行檔，請檢查路徑。"
            
        # --psm 8 告訴 AI：這是一張「單一單字」的圖片
        text = pytesseract.image_to_string(image, config='--psm 8')
        return text.strip()
    except Exception as e:
        return f"辨識發生錯誤: {str(e)}"