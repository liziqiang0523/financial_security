import requests
import io,os,json,time

class lik(object):
    def __init__(self):
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'gdp_user_id=gioenc-bd666133%2Cg22e%2C577c%2C819c%2C00d653cc5a04; ba17301551dcbaf9_gdp_user_key=; ba17301551dcbaf9_gdp_session_id=00386404-f2b8-47a9-9ccd-a961a4620f58; ba17301551dcbaf9_gdp_session_id_00386404-f2b8-47a9-9ccd-a961a4620f58=true; ba17301551dcbaf9_gdp_sequence_ids={%22globalKey%22:25%2C%22VISIT%22:2%2C%22PAGE%22:3%2C%22CUSTOM%22:7%2C%22VIEW_CLICK%22:16}',
            'Referer': 'http://www.sse.com.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        self.url ='http://query.sse.com.cn/security/stock/queryCompanyBulletin.do'

    def find_substring_find(self,s, sub):
        """
        使用find方法查找子字符串
        """
        if s.find(sub) != -1:
            return True
        else:
            return False

    def run(self,i):
        params = {
            'jsonCallBack': 'jsonpCallback34032405',
            'isPagination': 'true',
            'pageHelp.pageSize': '25',
            'pageHelp.pageNo': '{}'.format(i),
            'pageHelp.beginPage': '{}'.format(i),
            'pageHelp.cacheSize': '1',
            'pageHelp.endPage': '{}'.format(i),
            'productId': '',
            'securityType': '0101,120100,020100,020200,120200',
            'reportType2': 'DQBG',
            'reportType': 'ALL',
            'beginDate': '2023-02-10',
            'endDate': '2023-05-10',
            '_': '1683567116343',
        }

        response = requests.get(
            self.url,
            params=params,
            headers=self.headers,
            verify=False,
        )
        data = response.text[22:-1]
        datas = json.loads(data)['pageHelp']['data']
        pp = '摘要'
        for i in datas:
            time = i['SSEDATE']
            title = i['TITLE']
            url = i['URL']
            if int(time[8:]) >= 16:
                lk = self.find_substring_find(title, pp)
                if lk == True:
                    os_path = os.getcwd() + '/有摘要/'
                    if not os.path.exists(os_path):
                        os.mkdir(os_path)
                    titles = title.replace('*','').replace('|','').replace('?','').replace('<','').replace('>','').replace('"','').replace(':','').replace('\\','').replace('/','')
                    pdf_name = titles + '_' + time
                    pdf_url = 'http://www.sse.com.cn' + url
                    response = requests.get(pdf_url, headers=self.headers)
                    bytes_io = io.BytesIO(response.content)
                    with open(os_path + "%s.PDF" % pdf_name, mode='wb') as f:
                        f.write(bytes_io.getvalue())
                        print('%s.PDF,下载成功！' % (pdf_name))
                else:
                    os_path = os.getcwd() + '/没有摘要/'
                    if not os.path.exists(os_path):
                        os.mkdir(os_path)
                    titles = title.replace('*','').replace('|','').replace('?','').replace('<','').replace('>','').replace('"','').replace(':','').replace('\\','').replace('/','')
                    pdf_name = titles + '_' + time
                    pdf_url = 'http://www.sse.com.cn' + url
                    response = requests.get(pdf_url, headers=self.headers)
                    bytes_io = io.BytesIO(response.content)
                    with open(os_path + "%s.PDF" % pdf_name, mode='wb') as f:
                        f.write(bytes_io.getvalue())
                        print('%s.PDF,下载成功！' % (pdf_name))
            else:
                return 10
        return 20

    def hj(self):
        for i in range(100,300):
            ii = self.run(i)
            if ii == 10:
                break
            print(i)
            time.sleep(3)

s = lik()
s.hj()














# 定义一个字符串
# string = 'A New String Hello, World!'
# sub_string = "String"
# print('例1，源字符串为：', string, ' 待查找字符串为：', sub_string)

# if __name__ == '__main__':
#     save_path = 'D:/Program/项目/年报/'
#
#     pdf_url="http://static.cninfo.com.cn/finalpage/3892.PDF"
# download_pdf(save_path, pdf_name, pdf_url)