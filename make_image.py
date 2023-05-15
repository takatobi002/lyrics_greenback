import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

# 環境”lyrics_greenback”を有効にすること

# 使うフォント，サイズ，描くテキストの設定
ttfontname = "/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"
fontsize = 36
text = "暗黙の型宣言"

# 画像サイズ，背景色，フォントの色を設定
canvasSize    = (300, 150)
backgroundRGB = (0, 255, 0)
textRGB       = (0, 0, 0)

# 文字を描く画像の作成
img  = PIL.Image.new('RGB', canvasSize, backgroundRGB)
draw = PIL.ImageDraw.Draw(img)

# 用意した画像に文字列を描く
font = PIL.ImageFont.truetype(ttfontname, fontsize)
textWidth, textHeight = draw.textsize(text,font=font)
textTopLeft = (canvasSize[0]//6, canvasSize[1]//2-textHeight//2) # 前から1/6，上下中央に配置
draw.text(textTopLeft, text, fill=textRGB, font=font)

img.save("image.png")
