#bounceless

this is api for bounceless.io

#Usage
  check your 'pycurl' module
(if it is not install use pip or easy_install
  http://pycurl.io/docs/latest/install.html)

  For OneByOne Verefication:

    from emailverify import bouncelessOne


    E = bouncelessOne('PUT_YOUR_KEY', 'test@mail.com')
    result = E.control()
    print result // answer is string 'ok' or 'fail'

  To Upload a Bulk

    from emailverify import bouncelessBulk   

    B = bouncelessBulk('PUT_YOUR_KEY', 'path/to/file.csv')
    B.upload()       //upload file in server and get id_file from server
    B.get_info()     // here will be answer from server  
                    something like that:
                    135094|6565_clean.csv|no|7|7|finished|1456415517
                    or
                    |https://apps.bounceless.io/app/webroot/files/4195/6565/result_ok_6565_2016-02-25.csv
                    |https://apps.bounceless.io/app/webroot/files/4195/6565/result_all_6565_2016-02-25.csv
#Contributing

 This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the Contributor Covenant code of conduct.

