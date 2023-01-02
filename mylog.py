import os
import sys
import traceback
from pathlib import Path
import loguru
from loguru import logger
#from __future__ import annotations
#=================config========================
IS_CONSOLE = True
LOG_SIZE = "100 MB"
LOG_RETENTION = "6 month"
LOG_COMPERSSION = "tar.gz"
LOG_SEP = True
#=================config========================

def make_filter(name):
    pass
    # def filter(record: loguru.Record):
    #     """过滤函数
    #
    #     Args:
    #         record (loguru.Record): the |dict| containing all contextual information of the logged message.
    #
    #     Returns:
    #         bool: 日志文件名称相同时返回 True，不相同时返回 False
    #     """
    #     return record["extra"].get("name") == name
    # return filter
class CLog:

    def __init__(self,log_path,is_console=IS_CONSOLE,is_code=True,size=LOG_SIZE,retention=LOG_RETENTION,
                 compression=LOG_COMPERSSION,proc_desc="",sep_log=LOG_SEP):
        """

        :param log_path:  log路径
        :param is_console: 是否终端显示
        :param is_code: 是否显示代码
        :param size: 日志文件切割大小
        :param retention: 日志文件保存时长
        :param compression: 日志文件压缩格式
        :param proc_desc: 多进程日志，进程描述
        :param sep_log:
        """
        self.sep_log = sep_log
        if sep_log and len(proc_desc) > 0:
            log_path = f'{log_path}_{proc_desc}'
        self.is_code = is_code
        self.log_path = log_path
        self.log_api= log_path
        self.proc_desc = proc_desc
        #是否开启终端输出
        if not is_console:
            logger.remove(handler_id=None)
        #获取日志文件句柄
        dict_handlers = dict(logger._core.handlers)

        #获取句柄中的文件名
        list_sink = []

        #遍历每个句柄,获取文件名
        for k in dict_handlers.keys():
            #单个文件是句柄
            obj = dict_handlers[k]
            #格式化文件路径,去除sink中单引号
            list_sink.append(os.path.normcase(obj._name.replace('\'','')))
        #判断日志是否在句柄中防止日志多写
        if len(str(self.log_path)) > 0 and os.path.normcase(self.log_path) not in list_sink:
            log_dir = os.path.dirname(self.log_path)
            if not os.path.exists(log_dir):
                os.makedirs(log_dir,0o775)
            try:
                logger.add(self.log_path, format="{time:YYYY-MM-DD HH:mm:ss SSS Z} | {level} | {message}",
                           filter=make_filter(self.log_api), rotation=size, enqueue=True, retention=retention,
                           compression=compression)
            except OSError:
                logger.add(self.log_path, format="{time:YYYY-MM-DD HH:mm:ss SSS Z} | {level} | {message}",
                           filter=make_filter(self.log_api), rotation=size, enqueue=False, retention=retention,
                           compression=compression)

        self.mylog = logger.bind(name=self.log_api)
    def log(self,message,depth=1,level="INFO"):
        """
        write log
        :param message: log message
        :param depth:  parent depth
        :param level: log level
        :return:
        """
        try:
            #路径存在
            if(len(str(self.log_path))==0):
                return
            obj_parent = sys._getframe(depth)
            #filename
            file_name = Path(obj_parent.f_code.co_filename).name
            #linename
            line = obj_parent.f_lineno
            #functionname
            func = obj_parent.f_code.co_name
            #用户输入初始化进程描述存在,日志中加上进程信息
            if len(self.proc_desc) > 0 and not self.sep_log:
                message = f'proc_{self.proc_desc},{message}'
            #Format message
            str_msg = f'{file_name}:{line}-{func}|{message}'
            if not self.is_code:
                str_msg = f'message'
            if level.lower()=="info":
                self.mylog.info(str_msg)
            if level.lower()=="error":
                self.mylog.error(str_msg)
            if level.lower()=="warning":
                self.mylog.warning(str_msg)
            if level.lower()=="debug":
                self.mylog.debug(str_msg)
            if level.lower()=="success":
                self.mylog.success(str_msg)
            if level.lower()=="critical":
                self.mylog.critical(str_msg)
            if level.lower()=="trace":
                self.mylog.trace(str_msg)
            if level.lower()=="success":
                self.mylog.success(str_msg)
        except Exception as e:
            self.mylog.error(e.args[0])
            self.mylog.error(traceback.format_exc())

    def info(self,message,depth=2,log_switch=True):
        """
        write log message which's level is info
        :param message: logmessage
        :param depth: depth,Default value:2
        :param log_switch: log switch
        :return:
        """
        if log_switch:
            self.log(str(message),depth=depth,level="info")

    def warnig(self,message,depth=2,log_switch=True):
        """
        write log message which's level is info
        :param message: logmessage
        :param depth: depth,Default value:2
        :param log_switch: log switch
        :return:
        """
        if log_switch:
            self.log(str(message),depth=depth,level="warnig")

    def debug(self,message,depth=2,log_switch=True):
        """
        write log message which's level is info
        :param message: logmessage
        :param depth: depth,Default value:2
        :param log_switch: log switch
        :return:
        """
        if log_switch:
            self.log(str(message),depth=depth,level="debug")

    def critical(self,message,depth=2,log_switch=True):
        """
        write log message which's level is info
        :param message: logmessage
        :param depth: depth,Default value:2
        :param log_switch: log switch
        :return:
        """
        if log_switch:
            self.log(str(message),depth=depth,level="critical")

    def trace(self,message,depth=2,log_switch=True):

        """
        write log message which's level is info
        :param message: logmessage
        :param depth: depth,Default value:2
        :param log_switch: log switch
        :return:
        """
        if log_switch:
            self.log(str(message),depth=depth,level="trace")

    def exception(self,message,depth=2,log_switch=True):
        """
        write log message which's level is info
        :param message: logmessage
        :param depth: depth,Default value:2
        :param log_switch: log switch
        :return:
        """
        if log_switch:
            self.log(str(message),depth=depth,level="exception")

    def success(self,message,depth=2,log_switch=True):
        """
        write log message which's level is info
        :param message: logmessage
        :param depth: depth,Default value:2
        :param log_switch: log switch
        :return:
        """
        if log_switch:
            self.log(str(message),depth=depth,level="success")

    def enter(self,depth=1,log_switch=True,skip=[]):
        """
        save prarameter into the log
        :param depth: function depth
        :param log_switch: log switch
        :param skip: skip para list ,all :skip all the parameter save log,[]:the skip parameter list
        :return:
        """
        try:
            if log_switch:
                self.info("Enter function:{func}()".format(
                    func=sys._getframe(depth).f_code.co_name),depth=3)
                #全部跳过则忽略参数打印
                if str(skip).lower() == 'all':
                    return
                dict_params = dict(sys._getframe(1).f_locals)
                for k in dict_params:
                    # if the parameters is in the skip list,do not save the parameter into the log
                    if str(k).lower() == "self" or str(k).lower()=="log_switch" or k in skip:
                        continue
                    val = dict.get(k)
                    if len(str(val)) == 0:
                        val = "value is empty"
                    self.info(
                        f"Input parameter:{k},value:{val}",depth=3
                    )
        except:
            self.info(traceback.format_exc(),depth=3)
            raise

    def leave(self,**kwargs):
        try:
            if not isinstance(kwargs,dict):
                return
            depth = 1
            if kwargs.get("log_switch",True):
                for k in kwargs:
                    val = kwargs.get(k)
                    #skip the log_switch
                    if k == "log_switch":
                        continue
                    self.info(f"Result parameter :{k},value:{val}",depth=3)
                self.info("Leave function : {func}()".format(
                    func=sys._getframe(depth).f_code.co_name,depth=3
                ))
        except:
            self.info(traceback.format_exc(),depth=3)
            raise