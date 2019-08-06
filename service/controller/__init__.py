# blueprint 정의
from flask import Blueprint

# ~/
bp_home =  Blueprint('homebp',
                     __name__,
                     template_folder='../templates',
                     static_folder='../static',)

# ~/user 계열
bp_user =  Blueprint('userbp',
                     __name__,
                     template_folder='../templates',
                     static_folder='../static',)

#~/search 계열
bp_search = Blueprint('searchbp',
                    __name__,
                    template_folder='../templates',
                    static_folder='../static')
#~/my 계열
bp_my = Blueprint('mybp',
                    __name__,
                    template_folder='../templates',
                    static_folder='../static')



