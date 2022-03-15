def one():
    url='https://j1.pupuapi.com/client/product/storeproduct/detail/4dcdeca2-f5a3-4be8-9e2f-e099889a23a0/ccac09fa-5171-4f1e-9263-e731be3400d7'
    head={
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    requests=requests.get(url,headers=head)