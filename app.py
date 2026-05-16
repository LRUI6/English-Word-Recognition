from flask import Flask, request, jsonify, render_template
# 💡 這裡改成從 image_processor 載入，絕對不會再撞名了！
from image_processor import decode_base64_to_image, preprocess_for_tesseract, preprocess_for_trocr
from model_tesseract import predict_word_tesseract
from model_trocr import predict_word_trocr, load_trocr_model
import traceback

print("🚀 系統準備啟動，正在載入核心元件...")

app = Flask(__name__)

# 伺服器啟動時，先喚醒微軟的超強 AI 模型
load_trocr_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    try:
        data = request.get_json()
        base64_str = data.get('image', '')
        
        # 1. 解碼圖片
        raw_image = decode_base64_to_image(base64_str)

        # 2. 準備兩種模型需要的圖片格式
        img_tes = preprocess_for_tesseract(raw_image)
        img_trocr = preprocess_for_trocr(raw_image)

        # 3. 雙引擎同時預測 (交叉驗證)
        res_tes = predict_word_tesseract(img_tes)
        res_trocr = predict_word_trocr(img_trocr)

        return jsonify({
            "success": True,
            "tesseract_result": res_tes,
            "trocr_result": res_trocr
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    # 這裡的 host='0.0.0.0' 是讓電腦對外開門的密碼
    app.run(host='0.0.0.0', debug=True, port=5000)