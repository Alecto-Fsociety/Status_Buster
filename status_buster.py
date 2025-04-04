import socket,ssl,sys,random,pathlib,chardet,os,re,argparse,traceback
from urllib.parse import urlparse
from datetime import datetime
from multiprocessing import Pool

banner = """

███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗    ██████╗ ██╗   ██╗███████╗████████╗███████╗██████╗
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██████╔╝██║   ██║███████╗   ██║   █████╗  ██████╔╝
╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██╔══██╗██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗
███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝╚██████╔╝███████║   ██║   ███████╗██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

by Alecto-Fsocity (https://github.com/Alecto-Fsociety)
"""

print(banner)

class Status:
    def __init__(self,url_path):

        self.url_path = url_path
        self.url_list = self.url_lists()

        self.date = datetime.now()
        self.out_dir_name = "checked_url"
        self.out_file_name = f"{self.date.year}_{self.date.month}-{self.date.day}_{self.date.hour}-{self.date.minute}_checked_url.log"

        self.cache_file_name = self.out_file_name
        self.err_dir_name = "err_logs"
        self.err_file_name = f"errs.log"
        self.err_log = f"{self.date.year}_{self.date.month}-{self.date.day}_{self.date.hour}-{self.date.minute}_Error_Log"
        self.ua_list = self.ua_lists()

        self.status_list = {"200","301","302"}

    def url_lists(self):
        return [url.strip("\n") for url in open(self.url_path,"r",encoding="utf-8").readlines()]

    def ua_lists(self,ua_path="ua.txt"):
        return [ua.strip("\n") for ua in open(ua_path,"r",encoding="utf-8").readlines()]

    def get_headers(self,domain,path):
        return f"GET /{path} HTTP/1.1\r\nHost:{domain}\r\nUser-Agent:{random.choice(self.ua_list)}\r\nConnection:close\r\nAccept:*/*\r\n\r\n"

    def checked_log_files(self,list_data=[]):
        try:
            lines = [line.strip("\n") for line in open(f"{self.out_dir_name}/{self.cache_file_name}","r",encoding="utf-8").readlines()]
            for data in lines:
                if data and data not in list_data:
                    list_data.append(data)
            new_file_name = ((self.cache_file_name).split(".")[0]) + "_checked.log"
            with open(f"{self.out_dir_name}/{new_file_name}","w+",encoding="utf-8")as save_files:
                [save_files.write(f"{data}\n") for data in list_data]

        except KeyboardInterrupt:
            pass

    def check_status(self):
        url_list = self.url_list;lines = len(url_list)
        pathlib.Path(self.out_dir_name).mkdir(exist_ok=True)
        for point,url_data in enumerate(url_list,start=1):
            try:
                base_parse = urlparse(url_data);scheme = base_parse.scheme;domain = base_parse.netloc;path = (base_parse.path).split(":")[0]
                if scheme == "https":
                    with (ssl.create_default_context()).wrap_socket(
                        socket.create_connection((domain,443)),server_hostname=domain
                        )as ssock:

                        ssock.settimeout(3)
                        ssock.send(bytes(self.get_headers(domain,path),"utf-8"))

                        response = ssock.recv(1024*10)
                        
                        detected = chardet.detect(response)
                        encoding = detected["encoding"] if detected["encoding"] else "utf-8"
                        response_data = response.decode(encoding,errors="ignore")

                        status_match = re.search(r"HTTP/\d\.\d (\d+)",response_data)
                        status = status_match.group(1) if status_match else "000"

                        print(f"[-INFO-] Status_Check : {url_data} <{status}> [{point}/{lines}]")

                        if status in self.status_list:
                            with open(f"{self.out_dir_name}/{self.out_file_name}","a+",encoding="utf-8")as files:
                                files.write(f"[GET/443/{status}] {url_data}\n")
                else:
                    with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as sock:
                        sock.settimeout(3)
                        sock.connect((domain,80))

                        sock.sendall(bytes(self.get_headers(domain,path),"utf-8"))
                        
                        response = sock.recv(1024*10)
                        
                        detected = chardet.detect(response)
                        encoding = detected["encoding"] if detected["encoding"] else "utf-8"
                        response_data = response.decode(encoding,errors="ignore")

                        status_match = re.search(r"HTTP/\d\.\d (\d+)",response_data)
                        status = status_match.group(1) if status_match else "000"

                        print(f"[-INFO-] Status_Check : {url_data} <{status}> [{point}/{lines}]")

                        if status in self.status_list:
                            with open(f"{self.out_dir_name}/{self.out_file_name}","a+",encoding="utf-8")as files:
                                files.write(f"[GET/80/{status}] {url_data}\n")

            except Exception as e:
                pathlib.Path(self.err_dir_name).mkdir(exist_ok=True)
                with open(f"{self.err_dir_name}/{self.err_file_name}","a+",encoding="utf-8")as err:
                    err.write(f"[-] {self.err_log}\n{traceback.format_exc()}\n")

def base_func(instance):
    instance.check_status()

def main():
    try:
        arg = argparse.ArgumentParser()
        arg.add_argument("-ul",type=str,required=True,help="[>] URL_List_Path / -ul <url_list_path>")
        arg.add_argument("-t",type=int,default=4,help="[>] Pool_Thread / -t <pool_Thread>")
        parse = arg.parse_args()
        instance_data = Status(parse.ul)
        with Pool(parse.t) as pool:
            pool.starmap(base_func, [(instance_data,)] * parse.t,chunksize=1)
        instance_data.checked_log_files()
    except KeyboardInterrupt:
        instance_data.checked_log_files()
        sys.stdout.write("\n[!] Stop_Checker...\n")

if __name__ == "__main__":
    main()
