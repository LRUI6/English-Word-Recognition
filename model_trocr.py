from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch

# 宣告全域變數
processor = None
model = None

def load_trocr_model() -> None:
    """從 Hugging Face 載入微軟訓練好的 TrOCR 模型"""
    global processor, model
    print("⏳ 正在連線下載/載入 TrOCR 模型... (第一次執行需等待 1.3GB 下載)")
    
# 修改前：
# processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
# model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')

# 修改後（加上離線指令）：
    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten', local_files_only=True)
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten', local_files_only=True)
    
    print("✅ TrOCR 深度學習模型載入完成！")

def predict_word_trocr(image: Image.Image) -> str:
    """使用 TrOCR 模型進行辨識"""
    if processor is None or model is None:
        return "模型尚未載入"
    
    try:
        # 將 PIL 圖片轉換成模型看得懂的格式
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        
        # 讓 AI 產生文字 ID
        generated_ids = model.generate(pixel_values)
        
        # 將 ID 轉回英文單字
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        return generated_text.strip()
    except Exception as e:
        return f"辨識發生錯誤: {str(e)}"