# ✍️ English-Word-Recognition (手寫單字辨識系統)

這是我第一個基於深度學習的多模型手寫英文單字辨識專案。本系統結合了傳統 OCR 與現代 Transformer 深度學習技術，提供即時的手寫辨識服務。

## 🚀 核心技術
- **後端架構**: Flask (Python)
- **AI 引擎 A (深度學習)**: 微軟 TrOCR (Transformer-based Optical Character Recognition)
- **AI 引擎 B (傳統 OCR)**: Tesseract OCR (具備容錯處理)
- **前端介面**: HTML5 Canvas + JavaScript (支援滑鼠/觸控書寫)

## 🛠️ 安裝與啟動
1. 建立虛擬環境：
   ```bash
   python -m venv .venv

2.安裝必要套件：pip install Pillow flask pytesseract transformers torch

3.啟動伺服器：python app.py
3. 按下 `Ctrl + S` 存檔。

### 第三步：用手機造訪

1. 確保手機已經連上電腦的熱點。
2. 打開手機瀏覽器（Safari 或 Chrome）。
3. 在網址列輸入：`http://[你的IPv4位址]:5000`
   * 例如：`http://192.168.137.1:5000`
4. **大功告成！** 你應該會在手機上看到辨識介面。

---

### ⚠️ 可能會遇到的障礙：Windows 防火牆

如果手機輸入網址後顯示「連線逾時」，通常是 Windows 防火牆把外面進來的連線擋住了。
* **快速測試法**：暫時關閉 Windows 防火牆，或者在防火牆設定裡將 **5000 埠 (Port)** 設為「允許通過」。

### 💡 總監的進階玩法
手機有觸控螢幕，寫起來比滑鼠順手多了！你可以試試看用手機寫一段**「草寫單字」**，看看這台裝在電腦裡的 AI 坦克能不能在幾秒內把結果回傳到你手機上。

快去用手機連連看！成功在手機上看到畫面了嗎？