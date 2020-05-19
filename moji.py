#FILENAME = 変換したい元のtxtファイル
#OUTPUTNAME = 変換した後のtxtファイル。FILENAMEと同じにすると元データは消える。
#同じディレクトリで実行すること


#改行する文字数、改行するためのtextを突っ込めば勝手にやってくれる便利な関数。予定。
def text_list_maker(text, num):
    t_e_x_t = ','.join(text).rstrip(',\n')
    #print(t_e_x_t)

    #改行する回数の選定。num*2(2=1文字char+,)で1つの改行
    cutter = num*2
    count = (len(t_e_x_t)+1) // cutter

    if count >= 1:
        result_text = t_e_x_t[0:cutter-1]
        #print(result_text)
        for n in range(count):
            #print(t_e_x_t[(cutter)*(n+1):(cutter)*(n+2) -1])
            result_text = result_text  + "\n" + t_e_x_t[(cutter)*(n+1):(cutter)*(n+2) -1]
        return result_text
    else:
        return t_e_x_t


FILENAME = "hoge.txt"
OUTPUTNAME = "output.csv"

output_list = []

with open(FILENAME,'r') as f:
    for r in f:
        #print(r)
        #補足。Excelは文字コード絶対 Shift_Jis過激派。なので丁寧に書き換えて差し上げよう。
        sentence = r.encode('shift_jis')
        char_list = []
        for sentence in r:
            char_list.append(sentence)
        output_list.append(char_list)

with open(OUTPUTNAME, "w", encoding="shift_jis") as f:
    for x in output_list:
        text = text_list_maker(x, 20)
        #print(text)
        f.write(text + "\n")
