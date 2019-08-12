import datetime
import smtplib
import sys
import os

sys.path.append("./")

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.utils import parseaddr, formataddr
from email.header import Header
from email import encoders

from common.readConfig import ReadConfig


class SendEmail:
    def __format__addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, "utf-8").encode(), addr))

    def smtp(self):
        readconfig = ReadConfig()
        smtp_server = readconfig.get_email("smtp_server")
        smtp_server_host = readconfig.get_email("smtp_server_host")
        from_address = readconfig.get_email("from_address")
        password = readconfig.get_email("password")
        to_address = readconfig.get_email("to_address")
        result_path = os.path.join(os.path.abspath("."), "result", "report.html")
        server = smtplib.SMTP_SSL(smtp_server, smtp_server_host)
        server.set_debuglevel(1)
        server.login(from_address, password)
        content = """
                  执行测试中....
                  测试已完成！！！
                  生成报告中....
                  报告已生成....
                  报告已邮件发送！！！
                  """
        msg = MIMEMultipart()
        msg["From"] = self.__format__addr("%s" % from_address)
        msg["To"] = self.__format__addr("%s" % to_address)
        msg["Subject"] = Header("测试报告", "utf-8").encode()

        msg.attach(MIMEText(content, "plain", "utf-8"))

        with open(result_path, "rb") as f:
            mime = MIMEBase("file", "html", filename="result.html")
            mime.add_header("Content-Disposition", "attachment", filename="result.html")
            mime.add_header("X-Attachment-Id", "0")
            # 把附件内容读进来：
            mime.set_payload(f.read())
            # 用base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart：
            msg.attach(mime)
        server.sendmail(from_address, [to_address], msg.as_string())
        server.quit()


if __name__ == "__main__":
    print("测试报告")
    # send_email().outlook()
    SendEmail().smtp()
    print("send email ok!!!!!")
