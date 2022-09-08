import wordcloud as wc
import jieba
import re
import os

start_date = ''
end_date = ''


# 判断日期是否满足条件
def dateCheck(str):
    return start_date < str and str < end_date
    

def handle(txt_name,dir_name,checkDate,common):
    # 创建文件夹
    if not os.path.exists('{}'.format(dir_name)):
        os.makedirs('{}'.format(dir_name))


    # 匹配日期
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})')


    with open(txt_name, mode='r', encoding='utf-8') as f:
        txt = f.readlines()
        
    
    xiaoxi = []
    dict = {}

    # 统计发言次数及内容
    for i in range(0, len(txt)-1):
        if pattern.match(txt[i]):
            if( not checkDate or dateCheck(pattern.match(txt[i]).group(1))):
                name = txt[i].split(" ")[2].split("(")[0]
                if '】' in name:
                    name = name.split("】")[1]
                dict[name] = dict.get(name, 0) + 1
                xiaoxi.append(txt[i+1])


    names = dict.keys()
    dict = sorted(dict.items(),key= lambda x:x[1],reverse=True)

    # 输出 昵称 ：发言次数
    with open('{}/people_count.txt'.format(dir_name), mode='w', encoding='utf-8') as h:
        for key,value in dict:
            h.write('{key} {value}'.format(key=key,value=value))
            h.write('\n')
        
        
    str = ' '.join(xiaoxi).replace('[图片]', '').replace('[表情]', '').replace('请使用最新版手机QQ体验新功能','')


    # 定制词库
    jieba.add_word('撤回了一条消息')
    for name in names:
        jieba.add_word(name)
        
        
    # 分词   
    words = jieba.lcut(str)
    counts = []
    count_dict = {}

    
    # 统计词语出现次数
    for word in words:
        if len(word) == 1:    # 单个词语不计算在内
            continue
        elif word not in common:
            counts.append(word)    # 遍历所有词语，每出现一次其对应的值加 1
            count_dict[word] = count_dict.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1


    items = list(count_dict.items())  # 将键值对转换成列表
    items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序


    # 输出词语出现次数
    with open('{}/word_count.txt'.format(dir_name), mode='w', encoding='utf-8') as j:
        num = 200 # 打印个数
        for i in range(num):
            word, count = items[i]
            j.write("{0:<5}{1:>5}".format(word, count))
            j.write('\n')


    text = ' '.join(counts)

    # 生成图片并导出
    wordCloud = wc.WordCloud(font_path='msyh.ttc', background_color='white', width= 1000, height=1000, max_words=120, font_step=1)
    wordCloud.generate(text)
    wordCloud.to_file('{}/{}.png'.format(dir_name,dir_name))

    print('ok')
    
    
if __name__ == "__main__":
    # 聊天消息路径 格式txt
    txt_name = "C:/example.txt"
    # 生成文件夹名
    dir_name = "example"
    # 是否检查日期
    checkDate = False
    # 开始日期
    start_date = '2022-01-01'
    # 结束日期
    end_date = '2022-12-31'
    # 忽略的常用词
    common = ['什么','可以','这个','不是','没有','一个','就是','怎么','还是','这么','确实']
    
    handle(txt_name,dir_name,checkDate,common)