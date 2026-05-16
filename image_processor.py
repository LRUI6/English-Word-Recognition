import base64
from io import BytesIO
from PIL import Image, ImageOps

def decode_base64_to_image(base64_str: str) -> Image.Image:
    """把網頁傳來的字串變回圖片"""
    if ',' in base64_str:
        base64_str = base64_str.split(',')[1]
    image_bytes = base64.b64decode(base64_str)
    return Image.open(BytesIO(image_bytes)).convert("RGB")

def preprocess_for_tesseract(image: Image.Image) -> Image.Image:
    """Tesseract 喜歡白底黑字，所以我們把黑底白字的畫布反轉"""
    gray_image = image.convert("L")
    return ImageOps.invert(gray_image)

def preprocess_for_trocr(image: Image.Image) -> Image.Image:
    """TrOCR 是模仿人類看紙張，所以需要『白底黑字』的 RGB 圖片"""
    # 1. 先轉成灰階
    gray_image = image.convert("L")
    # 2. 顏色反轉 (把原本的黑底白字，變成白紙黑字)
    inverted_image = ImageOps.invert(gray_image)
    # 3. 轉回模型要的 RGB 格式
    return inverted_image.convert("RGB")