import os
import re

directory = r"c:\Users\tanmoy\Documents\jast work on this now\basic web"
buy_btn_pattern = re.compile(r'<a href="[^"]+" class="buy-btn"[^>]*>🛒 (Amazon|Flipkart)</a>')
price_pattern = re.compile(r'<p class="product-price">~₹([\d,]+)</p>')

for filename in os.listdir(directory):
    if filename.endswith(".html") and filename not in ["index.html", "about.html"]:
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Update buy buttons
            def replace_btn(match):
                return '<a href="#" class="buy-btn" onclick="window.open(\'https://www.google.com/search?tbm=shop&q=\' + encodeURIComponent(this.closest(\'.product-card\').querySelector(\'h4\').textContent + \' India\'), \'_blank\'); return false;">🔍 Check Price</a>'
            
            new_content = buy_btn_pattern.sub(replace_btn, content)

            # Update prices
            def replace_price(match):
                price_str = match.group(1).replace(",", "")
                price = int(price_str)
                min_p = int(price * 0.85 // 100 * 100 + 25) # Just some variation
                max_p = int(price * 1.15 // 100 * 100 + 75)
                return f'<p class="product-price">₹{min_p:,} – ₹{max_p:,} (Avg: ₹{price:,})</p>'
            
            new_content = price_pattern.sub(replace_price, new_content)

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
