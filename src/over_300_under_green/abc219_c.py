# 入力の受け取り
X=input()
N=int(input())

# 新しいアルファベット→通常のアルファベット変換(convert)辞書
conv_letter=dict()
# 通常のアルファベット変換→新しいアルファベット(inverse convert)辞書
inv_letter=dict()

# それぞれの文字について変換辞書を作成
for i in range(len(X)):
    # chr(97)="a"
    # chr(98)="b"
    # ...
    # Xのi文字目→chr(i+97)
    conv_letter[X[i]]=chr(i+97)
    # chr(i+97)→Xのi文字目
    inv_letter[chr(i+97)]=X[i]
    
# Sを通常のアルファベットへ変換する関数
def conv_name(S):
    # 結果を格納する変数
    result=""
    # Sのそれぞれの文字について
    for i in S:
        # 変換してresultの末尾へ結合
        result+=conv_letter[i]
    # resultを返す
    return result

# Sを新しいアルファベットへ変換する関数
def inv_name(S):
    # 結果を格納する変数
    result=""
    # Sのそれぞれの文字について
    for i in S:
        # 変換してresultの末尾へ結合
        result+=inv_letter[i]
    # resultを返す
    return result

# 通常のアルファベットへ変換後の名前を格納する変数
conv_names=[]

# 入力の受け取り
for i in range(N):
    # Sの受け取り
    S=input()
    # 通常のアルファベットへ変換
    conv_S=conv_name(S)
    # conv_namesへ追加
    conv_names.append(conv_S)

# conv_namesを辞書順へソート
conv_names.sort()

# conv_namesのそれぞれについて
for conv_S in conv_names:
    # 新しいアルファベットへ変換
    inv_S=inv_name(conv_S)
    # 出力
    print(inv_S)