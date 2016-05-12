#coding=utf-8
_author__ = 'Junior'
#建立一个多线程去监控自动化页面的状态
import threading

class exit_or_not():



    def is_print_or_not(self):
        try:
            self.driver.find_element_by_name('admin')
            return True
        except:
            return False

    thread = []
    t1 = threading.Thread(target=is_print_or_not)
    thread.append(t1)
    if __name__ == '__main__':
        t1.setDaemon(True)
        t1.start()
    # def  start(is_print_or_not):
    #     thread = []
    #     t1 = threading.Thread(target=is_print_or_not)
    #     thread.append(t1)
    #     if __name__ == '__main__':
    #         t1.setDaemon(True)
    #         t1.start()






