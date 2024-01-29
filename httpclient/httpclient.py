import attr
import requests
from functools import wraps


@attr.s
class HttpClient(requests.Session):
    host = attr.ib()
    port = attr.ib(defualt="443")
    username = attr.ib(default=None)
    password = attr.ib(default=None)
    cookie = attr.ib(default=None)
    scheme = attr.ib(default="https")
    baseUrl = attr.ib(init=False)
    url_prefix = attr.ib(default="")

    def hook_init(self):
        pass

    def __attrs_post_init__(self):
        """  
        初始化基础的url  
        """
        self.verify = False
        self.baseUrl = f"{self.scheme}://{self.host}:{self.port}"
        super().__init__()
        self.hook_init()

    @classmethod
    def from_option(cls, option):
        return cls(*option)

    def get_full_url(self):
        pass

    def hook_req_handle(self,
                        args,
                        kwargs):
        return args, kwargs

    def hook_resp_handle(self,
                         resp):
        # return resp
        pass

    def request_handle(func):
        @wraps(func)
        def _(self, *args, **kwargs):
            if "vertify" not in kwargs:
                kwargs['vertify'] = False
            _args, _kwargs = self.hook_req_handle(args, **kwargs)
            res = func(self, *_args, **_kwargs)
            self.hook_resp_handle(res)
            return res

        return _

    @request_handle
    def post(self, url, data=None, json=None, **kwargs):
        url = self.get_full_url()
        return super().post(url, data=data, json=json, **kwargs)

    @request_handle
    def get(self, url, data=None, json=None, **kwargs):
        url = self.get_full_url()
        return super().post(url, data=data, json=json, **kwargs)


if __name__ == "__main__":
    pass