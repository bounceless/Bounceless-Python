#!/usr/bin/python  
# _*_ coding:utf-8 _*_  

import requests  
import datetime  
import pycurl  

class BouncelessOne():  
    """
    Class for individual email verification.
    """
    def __init__(self, key, email):  
        self.key = key  
        self.email = email  
        self.verif = "https://apps.bounceless.io/api/singlemaildetails?secret="  
        self.url = f"{self.verif}{self.key}&email={self.email}"  

    def control(self):  
        """
        Verifies the email and returns a JSON response.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()  # returns a JSON response  

class BouncelessBulk():  
    """
    Class for bulk email verification.
    """
    def __init__(self, key, user_file):  
        datenow = datetime.datetime.now()  
        self.key = key  
        self.name = f'File{datenow.strftime("%Y-%m-%d %H:%M")}'
        self.user_file = user_file  
        self.url = f'https://apps.bounceless.io/api/verifyApiFile?secret={key}&filename={self.name}'

    def upload(self):  
        """
        Uploads the file for verification.
        """
        with open('id_file', 'w') as infile:  
            c = pycurl.Curl()  
            c.setopt(c.POST, 1)  
            c.setopt(c.URL, self.url)  
            c.setopt(c.HTTPPOST, [('file_contents', (  
                c.FORM_FILE, self.user_file,  
                c.FORM_CONTENTTYPE, 'text/plain',  
                c.FORM_FILENAME, self.name.replace(' ','_'),))])  
            c.setopt(c.WRITEFUNCTION, infile.write)  
            c.setopt(c.VERBOSE, 1)  
            c.perform()  
            c.close()  

    def get_info(self):  
        """
        Gets the verification results.
        """
        with open('id_file','r') as f:  
            ids = f.read()  
            url = f'https://apps.bounceless.io/api/getApiFileInfo?secret={self.key}&id={ids}'
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
            else:
                with open('result.txt', 'a') as res:  
                    res.write(response.content+'\n')  
                print(response.content)

if __name__ == '__main__':  
    pass
