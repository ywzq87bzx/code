import re

import execjs
import requests


class BaiduSpider:
    def __init__(self):
        self.post_url ='https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        self.get_url='https://fanyi.baidu.com/'
        self.post_headers ={
            "accept": "*/*",
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'content-length':'150',
            'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie':'BAIDUID=0494F8D75D1CD5904AF3A75D4D08C005:FG=1; BIDUPSID=0494F8D75D1CD5904AF3A75D4D08C005; PSTM=1607911099; __yjs_duid=1_16757e908b84b128619edd182cec932c1609053824189; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=jnPOJeC62AWK55TrpDHq25BS-250oYTTH6aoO8SeQtp50DtTOAyhEG0PVf8g0Kub1VDqogKKy2OTH9DF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=JJAO_IKMtCvbfP0k2Jo_5-4Hbp7t2D62aKDs0q3gBhcqJ-ovQTb6bpJyK4ILbh8HJmrgsCocW-Q4hUbeWfvpQxAn0xRHLPr4HGRp0bQ12l5nhMJmBUTFWq4TqfQa-qby523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0D63Lea-Jt6_s2TTW0CPyHJOoDDvdqJocy4LdjG5tWbOe5KOHWJ5C-K_hEx8zDxRvLl4B3-Aq54RM2aR-WD-KLlcT8CThMxbkQfbQ0-7hqP-jW5TaBnjRJn7JOpvwDxnxy5FvQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6IHtn4DoKL-JCv5eJ6x-tJqq4-0-q60etJyaR3HhIbvWJ5WqR7jDPnAMpDX3tjgaTDt0HALsxQ1LhjDShbXXMoSjxPVDtndaxclXacwWIOO3l02V-bIbn7NyxKVKf5dW4RMW20j0h7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjC5Dj5-jatJJ5nbKC5QB4Taajr5e-n4bbJSMPTH-UIsWP5rB2Q-5KL-J-5Ceb5nKR3UyMnXjt5ge6DttIOk-UbdJJjoqRTlLqbsQfRWqtQNXxbaJeTxoUty5DnJhhvG-xJEMf_ebPRih6j9Qg-8KpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0hCKmjTtMDj5M5pJfeJbKaDnyLRTMHJOoDDvFhl3cy4LdjG5CLMPtJGnHQpbd-C_hEx8zD6_2hpF73-Aq54R9fN7-b4bMJCJUfMbOLJrsQfbQ0bjhqP-jW5TaoxQg-R7JOpvwDxnxy5FvQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ht6T2-DA_oKtMtCQP; BDSFRCVID_BFESS=jnPOJeC62AWK55TrpDHq25BS-250oYTTH6aoO8SeQtp50DtTOAyhEG0PVf8g0Kub1VDqogKKy2OTH9DF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=JJAO_IKMtCvbfP0k2Jo_5-4Hbp7t2D62aKDs0q3gBhcqJ-ovQTb6bpJyK4ILbh8HJmrgsCocW-Q4hUbeWfvpQxAn0xRHLPr4HGRp0bQ12l5nhMJmBUTFWq4TqfQa-qby523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0D63Lea-Jt6_s2TTW0CPyHJOoDDvdqJocy4LdjG5tWbOe5KOHWJ5C-K_hEx8zDxRvLl4B3-Aq54RM2aR-WD-KLlcT8CThMxbkQfbQ0-7hqP-jW5TaBnjRJn7JOpvwDxnxy5FvQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6IHtn4DoKL-JCv5eJ6x-tJqq4-0-q60etJyaR3HhIbvWJ5WqR7jDPnAMpDX3tjgaTDt0HALsxQ1LhjDShbXXMoSjxPVDtndaxclXacwWIOO3l02V-bIbn7NyxKVKf5dW4RMW20j0h7mWIQvsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjC5Dj5-jatJJ5nbKC5QB4Taajr5e-n4bbJSMPTH-UIsWP5rB2Q-5KL-J-5Ceb5nKR3UyMnXjt5ge6DttIOk-UbdJJjoqRTlLqbsQfRWqtQNXxbaJeTxoUty5DnJhhvG-xJEMf_ebPRih6j9Qg-8KpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0hCKmjTtMDj5M5pJfeJbKaDnyLRTMHJOoDDvFhl3cy4LdjG5CLMPtJGnHQpbd-C_hEx8zD6_2hpF73-Aq54R9fN7-b4bMJCJUfMbOLJrsQfbQ0bjhqP-jW5TaoxQg-R7JOpvwDxnxy5FvQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ht6T2-DA_oKtMtCQP; delPer=0; H_PS_PSSID=33423_33482_33354_33259_31660_33285_33286_33414_26350_33264_33389_33386_33370; PSINO=3; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1609204273,1610444099; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1610445374; __yjsv5_shitong=1.0_7_126544a3cd11642be1e102bb1a85b1bdc0db_300_1610445375108_101.39.225.103_9552e9cc; yjs_js_security_passport=e162a649a25e7bc26cf72d5cffd846d431a021c2_1610445375_js; BA_HECTOR=0g0k0l8l0k0la0257q1fvshlt0r',
            'origin':'https://fanyi.baidu.com',
            'referer':'https://fanyi.baidu.com/?aldtype=16047',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
            'x-requested-with':'XMLHttpRequest'
            }
        self.get_headers={
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
        }
        self.word = input("请输入要翻译的单词:")

    def get_gtk(self):
        html=requests.get(url=self.get_url,
                          headers=self.get_headers
                          ).text
        gtk=re.findall("window.gtk = '(.*?)'",html,re.S)[0]
        return gtk

    def get_sign(self,word):
        with open('1.js', 'r') as f:
            gtk=self.get_gtk()
            print(gtk)
            js_code = f.read()
            js_obj = execjs.compile(js_code)
            sign = js_obj.eval('e("{}","{}")'.format(word,gtk))
            return sign
    def attack_bd(self):
        sign=self.get_sign(self.word)
        print(sign)
        data={
            'from':'zh',
            # 'from':'en',
            'to':'en',
            # 'to':'zh',
            'query':self.word,
            'transtype':'translang',
            'simple_means_flag':'3',
            'sign':sign,
            'token':'b06e91cd48fde5f5d8ec37eafba52191',
            'domain':'common',}
        html = requests.post(url=self.post_url,
                             data=data,
                             headers=self.post_headers).json()
        print(html)
        result = html['trans_result']['data'][0]['dst']
        print(result)

if __name__ == '__main__':
    spider=BaiduSpider()
    spider.attack_bd()
