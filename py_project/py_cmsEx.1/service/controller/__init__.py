# blueprint 정의 
from flask import Blueprint

#~/user
bp_user=Blueprint('userbp',
                    __name__, 
                    template_folder='../templates',
                    static_folder='../static')


#~/epl #'name=eplbp
bp_epl=Blueprint('eplbp',
                    __name__, 
                    template_folder='../templates',
                    static_folder='../static')

#~/bbs
bp_bbs=Blueprint('bbsbp',
                    __name__, 
                    template_folder='../templates',
                    static_folder='../static')