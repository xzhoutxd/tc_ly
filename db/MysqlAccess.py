#-*- coding:utf-8 -*-
#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import traceback
import MysqlPool
sys.path.append('../base')
import Config as Config
import Common as Common

class MysqlAccess():
    '''A class of mysql db access'''
    def __init__(self):
        # 聚划算
        self.tc_db = MysqlPool.g_tcDbPool

    def __del__(self):
        # 聚划算
        self.tc_db = None

    def insertTCItem(self, args_list):
        try:
            sql = 'replace into nd_tc_parser_item_d(crawl_time, item_id, item_name, item_desc, item_url, item_pic_url, item_book_status, item_level, item_area, item_service, item_comment, item_comment_good, item_comment_rate, item_oriprice, item_disprice, item_discount, channel_id, position, c_begindate, c_beginhour) values(%s)' % Common.agg(20)
            self.tc_db.executemany(sql, args_list)
        except Exception, e:
            print '# insert tc Item info exception:', e

    def insertTCTicket(self, args_list):
        try:
            sql = 'replace into nd_tc_parser_ticket_d(crawl_time, item_id, item_name, consumer_type, consumer_type_name, ticket_id, ticket_name, ticket_price, ticket_adprice, ticket_dis_adprice, ticket_unit, ticket_unit_name, ticket_tag, ticket_consumer, ticket_contained, ticket_maintitle, c_begindate, c_beginhour) values(%s)' % Common.agg(18)
            self.tc_db.executemany(sql, args_list)
        except Exception, e:
            print '# insert tc Ticket exception:', e

if __name__ == '__main__':
    pass
    #my = MysqlAccess()